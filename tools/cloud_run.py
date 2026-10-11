"""Unattended runner for GitHub Actions (or any Linux box): one project, every stage, no questions.

    python tools/cloud_run.py list --drive gdrive:screencast-editor [--want all|name1,name2]
        -> JSON list of everything to edit in <drive>/inbox, any number, whatever the file names:
           * a subfolder with one video + one audio is one project named after the folder (an optional
             .md/.txt in it is the script, a .json the click log); a subfolder with several videos
             pairs them by name;
           * loose files pair by name (lesson 3.mp4 + lesson 3.mp3, lesson 3.md, lesson 3.json). Nothing is skipped as "already done": the inbox is the to-do list.
           Each entry: {"name": project name, "video", "audio", "script", "clicks": Drive file names}.
    python tools/cloud_run.py run <name>
        -> expects inbox/<name>.<video ext> + inbox/<name>.<audio ext> (the workflow downloads them),
           creates/refreshes projects/<name>, then:
           * if the recording or voiceover differ from the ones projects/<name>/work/ was made from
             (work/inputs.json), the old work/ and output/ are cleared: a new batch can reuse a name
           * mechanical stages that are missing (probe always; transcribe, align, scenes, frames)
           * judgment: work/actions.json + work/sync.json for these same inputs (e.g. analysed on a
             laptop and pushed) are used as they are. Otherwise Claude Code runs the screencast-edit
             skill headless when ANTHROPIC_API_KEY or CLAUDE_CODE_OAUTH_TOKEN is set; without a key
             the run stops with status "needs-analysis" (exit 3) after preparing frames.
           * plan_builder (if plan.json is missing), render.py, verify.py
           Writes projects/<name>/output/cloud-status.txt. Exit 0 = final.mp4 rendered and verified.

Script text: inbox/<name>.md|.txt if present, else none (the voiceover transcript becomes the script).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from common import AUDIO_EXTS, ROOT, VIDEO_EXTS

PY = sys.executable
INBOX = ROOT / "inbox"


def sh(cmd: list[str], check: bool = True) -> int:
    print(f"\n$ {' '.join(cmd)}", flush=True)
    rc = subprocess.call(cmd, cwd=ROOT)
    if check and rc != 0:
        raise SystemExit(f"error: step failed (exit {rc}): {' '.join(cmd)}")
    return rc


def tool(name: str, proj: str, *args: str, check: bool = True) -> int:
    return sh([PY, f"tools/{name}.py", "--project", proj, *args], check)


def rclone_lsf(path: str, *args: str) -> list[str]:
    res = subprocess.run(["rclone", "lsf", path, *args], capture_output=True, text=True)
    if res.returncode != 0:
        if "directory not found" in res.stderr.lower():
            return []
        raise SystemExit(f"error: rclone lsf {path} failed: {res.stderr.strip()}")
    return [l.strip() for l in res.stdout.splitlines() if l.strip()]


def slug(stem: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_-]+", "-", stem).strip("-_")
    return s or "project"


def kind_of(f: str) -> str | None:
    ext = os.path.splitext(f)[1].lower()
    return ("video" if ext in VIDEO_EXTS else "audio" if ext in AUDIO_EXTS else
            "script" if ext in (".md", ".txt") else "clicks" if ext == ".json" else None)


def cmd_list(a):
    natural = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]
    groups: dict[str, dict[str, list[str]]] = {}          # stem or folder -> kind -> Drive paths
    loose: dict[str, dict[str, list[str]]] = {}
    for f in rclone_lsf(f"{a.drive}/inbox", "-R", "--files-only"):
        k = kind_of(f)
        if not k:
            continue
        if "/" in f:                                      # inbox/<folder>/...: the folder is the project
            groups.setdefault(f.split("/")[0], {}).setdefault(k, []).append(f)
        else:                                             # loose files pair by name
            loose.setdefault(os.path.splitext(f)[0], {}).setdefault(k, []).append(f)
    cands = []                                            # (label, files by kind)
    for stem, d in loose.items():
        cands.append((stem, d))
    for folder, d in groups.items():
        if len(d.get("video", [])) <= 1 and len(d.get("audio", [])) <= 1:
            cands.append((folder, d))                     # one video + one audio: names don't matter
        else:                                             # several: pair by name inside the folder
            sub: dict[str, dict[str, list[str]]] = {}
            for k, fs in d.items():
                for f in fs:
                    sub.setdefault(os.path.splitext(f.split("/")[-1])[0], {}).setdefault(k, []).append(f)
            for stem, sd in sub.items():
                cands.append((f"{folder}/{stem}", sd))

    items, used = [], set()
    for label, d in sorted(cands, key=lambda c: natural(c[0])):
        if not (d.get("video") and d.get("audio")):
            found = ", ".join(f for fs in d.values() for f in fs)
            print(f"skip {label!r}: needs a video and an audio file (found: {found})", file=sys.stderr)
            continue
        name, n = slug(label), 2
        while name in used:
            name, n = f"{slug(label)}-{n}", n + 1
        used.add(name)
        first = lambda k: (d.get(k) or [""])[0]
        items.append({"name": name, "stem": label, "video": first("video"), "audio": first("audio"),
                      "script": first("script"), "clicks": first("clicks")})
    if a.want.strip().lower() != "all":
        want = [w.strip() for w in a.want.split(",") if w.strip()]
        missing = [w for w in want if not any(w in (i["name"], i["stem"]) for i in items)]
        if missing:
            raise SystemExit(f"error: no video+audio pair in {a.drive}/inbox for: {', '.join(missing)} "
                             f"(found: {', '.join(i['stem'] for i in items) or 'nothing'})")
        items = [i for i in items if i["name"] in want or i["stem"] in want]
    print(json.dumps(items))


def find_input(name: str, exts) -> Path | None:
    hits = [f for f in sorted(INBOX.glob(name + ".*")) if f.suffix.lower() in exts]
    return hits[0] if hits else None


def status(proj_dir: Path, text: str):
    out = proj_dir / "output"
    out.mkdir(parents=True, exist_ok=True)
    (out / "cloud-status.txt").write_text(text + "\n", encoding="utf-8")
    print(f"\nstatus: {text}", flush=True)


def run_claude(name: str) -> None:
    prompt = (
        f"/screencast-edit {name}\n\n"
        "You are running unattended in GitHub Actions on Linux (no user is watching; never ask "
        "questions). The mechanical stages have already run: every file that exists in "
        f"projects/{name}/work/ is current, so reuse it (do not re-transcribe). Do the analyze and "
        "sync stages, the preview review, the final render, verify, and output/report.md exactly as "
        "the skill says. Keep the client's preferences from docs/lessons.md: follow the audio order, "
        "and fast-forward in-scene dead time instead of cutting it."
    )
    cmd = ["claude", "-p", prompt, "--dangerously-skip-permissions", "--output-format", "text"]
    if os.environ.get("CLAUDE_MODEL"):
        cmd += ["--model", os.environ["CLAUDE_MODEL"]]
    print(f"\n$ claude -p '/screencast-edit {name} ...'", flush=True)
    rc = subprocess.call(cmd, cwd=ROOT)
    if rc != 0:
        raise SystemExit(f"error: Claude Code exited with {rc}")


def cmd_run(a):
    name = a.name
    proj = f"projects/{name}"
    pdir = ROOT / proj
    video, audio = find_input(name, VIDEO_EXTS), find_input(name, AUDIO_EXTS)
    if not video or not audio:
        raise SystemExit(f"error: need inbox/{name}.<video> and inbox/{name}.<audio> (got {video}, {audio})")
    script = next((p for p in (INBOX / f"{name}.md", INBOX / f"{name}.txt") if p.exists()), None)
    w = pdir / "work"
    old_inputs = (w / "inputs.json").read_text(encoding="utf-8") if (w / "inputs.json").exists() else None

    args = [PY, "tools/new_project.py", name, "--video", str(video), "--audio", str(audio), "--move", "--force"]
    if script:
        args += ["--script", str(script)]
    if (INBOX / f"{name}.json").exists():                   # click_logger output, optional
        args += ["--clicks", str(INBOX / f"{name}.json")]
    sh(args)
    if old_inputs != (w / "inputs.json").read_text(encoding="utf-8"):
        # A different recording/voiceover under this name (e.g. the next batch): nothing stored applies.
        print(f"\nnew inputs for {name}: clearing the previous work/ and output/", flush=True)
        keep = (w / "inputs.json").read_text(encoding="utf-8")
        shutil.rmtree(w, ignore_errors=True)
        shutil.rmtree(pdir / "output", ignore_errors=True)
        (w / "frames").mkdir(parents=True)
        (pdir / "output").mkdir()
        (w / "inputs.json").write_text(keep, encoding="utf-8")
    # The checkout gives repo files an older mtime than the inputs just downloaded; mark the stored
    # stage outputs as current so nothing (including the skill's freshness rule) redoes them.
    now = time.time()
    for f in (pdir / "work").rglob("*"):
        if f.is_file():
            os.utime(f, (now, now))

    tool("probe", proj)
    if not (w / "words.json").exists():
        tool("transcribe", proj)
    if not (w / "lines.json").exists():
        tool("align_script", proj)
    if not (w / "scenes.json").exists():
        tool("scenes", proj)

    judged = (w / "actions.json").exists() and (w / "sync.json").exists()
    if not judged:
        if not (w / "frames" / "sheet_01.jpg").exists():
            tool("frames", proj, "--sheets", "--event-sheets")
        has_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
        if not (has_key and shutil.which("claude")):
            status(pdir, "needs-analysis: no actions.json/sync.json in the repo and no Claude key; "
                         "run /screencast-edit locally (or add the key) and push work/")
            raise SystemExit(3)
        run_claude(name)
    else:
        if not (w / "plan.json").exists():
            tool("plan_builder", proj)
        tool("check", proj, "--plan")
        tool("render", proj)
        tool("verify", proj, check=False)              # its verdict is read from verify.json below
        rep = pdir / "output" / "report.md"
        if not rep.exists():
            rep.write_text(f"# {name}\n\nRendered in GitHub Actions from the stored plan "
                           f"(work/sync.json). See work/sync-notes.md for the judgment calls.\n",
                           encoding="utf-8")

    final = pdir / "output" / "final.mp4"
    vj = w / "verify.json"
    ok = final.exists() and vj.exists() and json.loads(vj.read_text(encoding="utf-8")).get("ok", True)
    status(pdir, "done: final.mp4 rendered, verify PASS" if ok else "failed: no verified final.mp4")
    raise SystemExit(0 if ok else 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    l = sub.add_parser("list")
    l.add_argument("--drive", required=True, help="rclone path of the Drive folder, e.g. gdrive:screencast-editor")
    l.add_argument("--want", default="all")
    r = sub.add_parser("run")
    r.add_argument("name")
    a = ap.parse_args()
    cmd_list(a) if a.cmd == "list" else cmd_run(a)


if __name__ == "__main__":
    main()
