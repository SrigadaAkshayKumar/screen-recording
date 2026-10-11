"""Batch helper: turn everything in inbox/ into projects and run the mechanical stages.

    python tools/batch.py prep      # pair inbox files, create projects (files are MOVED), run
                                    # probe, transcribe, align, scenes, frames where missing
    python tools/batch.py status    # one line per project: which stages are done

Pairing is by file name: <name>.mp4 + <name>.mp3 (any supported video/audio extension), plus an
optional <name>.md / <name>.txt script and <name>.json click log. <name> becomes the project name.
The judgment stages (analyze, sync, review) are done per project by the screencast-edit skill.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

from common import AUDIO_EXTS, ROOT, VIDEO_EXTS, read_json

INBOX = ROOT / "inbox"
PROJECTS = ROOT / "projects"
PY = sys.executable


def slug(stem: str) -> str:
    s = re.sub(r"[^A-Za-z0-9_-]+", "-", stem).strip("-")
    return s or "project"


def pairs():
    files = [f for f in INBOX.iterdir() if f.is_file()] if INBOX.exists() else []
    by_stem: dict[str, dict[str, Path]] = {}
    for f in files:
        ext = f.suffix.lower()
        kind = ("video" if ext in VIDEO_EXTS else "audio" if ext in AUDIO_EXTS else
                "script" if ext in (".md", ".txt") else "clicks" if ext == ".json" else None)
        if kind:
            by_stem.setdefault(f.stem, {})[kind] = f
    ok, missing = [], []
    for stem, d in sorted(by_stem.items(), key=lambda kv: natural(kv[0])):
        (ok if "video" in d and "audio" in d else missing).append((stem, d))
    return ok, missing


def natural(s: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def run(args: list[str], log) -> bool:
    log.write(f"\n$ {' '.join(args)}\n")
    log.flush()
    return subprocess.run(args, stdout=log, stderr=subprocess.STDOUT, cwd=ROOT).returncode == 0


STAGES = [  # (name, output that marks it done, command)
    ("probe", "probe.json", ["tools/probe.py"]),
    ("transcribe", "words.json", ["tools/transcribe.py"]),
    ("align", "lines.json", ["tools/align_script.py"]),
    ("scenes", "scenes.json", ["tools/scenes.py"]),
    ("frames", "frames/sheet_01.jpg", ["tools/frames.py", "--sheets", "--event-sheets"]),
]


def prep(a):
    ok, missing = pairs()
    for stem, d in missing:
        print(f"skip {stem}: needs both a video and an audio file (found {', '.join(d)})")
    for stem, d in ok:
        name = slug(stem)
        proj = PROJECTS / name
        if (proj / "input").exists() and any((proj / "input").iterdir()):
            print(f"{name}: project exists - leaving inbox files alone")
            continue
        cmd = [PY, "tools/new_project.py", name, "--video", str(d["video"]), "--audio", str(d["audio"]), "--move"]
        if "script" in d:
            cmd += ["--script", str(d["script"])]
        if "clicks" in d:
            cmd += ["--clicks", str(d["clicks"])]
        res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        print(f"{name}: created" if res.returncode == 0 else f"{name}: FAILED to create\n{res.stderr}")

    names = sorted((p.name for p in PROJECTS.iterdir() if (p / "input").is_dir()), key=natural)
    if a.only:
        names = [n for n in names if n in a.only]
    for name in names:
        work = PROJECTS / name / "work"
        work.mkdir(parents=True, exist_ok=True)
        with open(work / "batch.log", "a", encoding="utf-8") as log:
            t0 = time.time()
            done = []
            for stage, marker, cmd in STAGES:
                if (work / marker).exists():
                    continue
                if not run([PY, *cmd[:1], "--project", f"projects/{name}", *cmd[1:]], log):
                    print(f"{name}: {stage} FAILED - see projects/{name}/work/batch.log")
                    break
                done.append(stage)
            if done:
                print(f"{name}: {', '.join(done)} ({time.time() - t0:.0f}s)", flush=True)


def status(_a):
    names = sorted((p.name for p in PROJECTS.iterdir() if (p / "input").is_dir()), key=natural)
    cols = ["prep", "actions", "plan", "preview", "final", "verify"]
    print(f"{'project':<24}" + "".join(f"{c:<9}" for c in cols) + "duration")
    for name in names:
        w, o = PROJECTS / name / "work", PROJECTS / name / "output"
        v = read_json(w / "verify.json") if (w / "verify.json").exists() else None
        cells = [
            all((w / m).exists() for _, m, _ in STAGES),
            (w / "actions.json").exists(), (w / "plan.json").exists(),
            (o / "preview.mp4").exists(), (o / "final.mp4").exists(),
            None if v is None or "final" not in v.get("file", "") else v.get("ok"),
        ]
        sym = {True: "yes", False: "-", None: "-"}
        if v is not None and "final" in v.get("file", "") and not v.get("ok"):
            sym_v = "FAIL"
        else:
            sym_v = sym[cells[5]]
        dur = ""
        if (w / "probe.json").exists():
            p = read_json(w / "probe.json")
            dur = f"rec {p['recording']['duration']:.0f}s / vo {p['voiceover']['duration']:.0f}s"
        print(f"{name:<24}" + "".join(f"{sym[c]:<9}" for c in cells[:5]) + f"{sym_v:<9}" + dur)
    ok, missing = pairs()
    if ok or missing:
        print(f"\ninbox: {len(ok)} ready pair(s), {len(missing)} incomplete")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prep")
    p.add_argument("--only", nargs="*", help="limit the stages to these project names")
    sub.add_parser("status")
    a = ap.parse_args()
    {"prep": prep, "status": status}[a.cmd](a)


if __name__ == "__main__":
    main()
