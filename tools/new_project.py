"""Create projects/<name>/ and copy the inputs in under their fixed names.

    python tools/new_project.py demo --video rec.mp4 --audio vo.mp3 [--script script.md] [--clicks clicks.json]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

from common import AUDIO_EXTS, ROOT, VIDEO_EXTS, die, file_fingerprint, write_json


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name", help="project name (letters, digits, - and _)")
    ap.add_argument("--video", required=True, help="silent screen recording")
    ap.add_argument("--audio", required=True, help="voiceover audio")
    ap.add_argument("--script", help="narration script (markdown or text); without it the transcript is used")
    ap.add_argument("--clicks", help="clicks.json from tools/click_logger.py (optional)")
    ap.add_argument("--force", action="store_true", help="replace inputs of an existing project")
    ap.add_argument("--move", action="store_true", help="move the files instead of copying (saves disk)")
    a = ap.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", a.name):
        die(f"bad project name {a.name!r}: use letters, digits, - and _")

    src = {"video": Path(a.video), "audio": Path(a.audio)}
    if a.script:
        src["script"] = Path(a.script)
    if a.clicks:
        src["clicks"] = Path(a.clicks)
    for k, p in src.items():
        if not p.is_file():
            die(f"--{k} file not found: {p}")
    if src["video"].suffix.lower() not in VIDEO_EXTS:
        die(f"--video must be one of {sorted(VIDEO_EXTS)}, got {src['video'].suffix}")
    if src["audio"].suffix.lower() not in AUDIO_EXTS:
        die(f"--audio must be one of {sorted(AUDIO_EXTS)}, got {src['audio'].suffix}")
    if "clicks" in src:
        try:
            data = json.loads(src["clicks"].read_text(encoding="utf-8"))
            if not isinstance(data.get("clicks"), list) or "screen" not in data:
                raise ValueError("expected keys 'screen' and 'clicks'")
        except (ValueError, json.JSONDecodeError) as e:
            die(f"--clicks is not a click_logger file: {e}")

    root = ROOT / "projects" / a.name
    inp = root / "input"
    if inp.exists() and any(inp.iterdir()) and not a.force:
        die(f"{root} already has inputs - pass --force to replace them")
    for d in (inp, root / "work" / "frames", root / "output"):
        d.mkdir(parents=True, exist_ok=True)
    if a.force:
        for old in inp.glob("*"):
            old.unlink()

    # Fixed stems; the original extension is kept so nothing is re-encoded.
    targets = {
        "video": inp / ("recording" + src["video"].suffix.lower()),
        "audio": inp / ("voiceover" + src["audio"].suffix.lower()),
    }
    if "script" in src:
        targets["script"] = inp / "script.md"
    if "clicks" in src:
        targets["clicks"] = inp / "clicks.json"
    for k, dst in targets.items():
        if a.move:
            shutil.move(str(src[k]), dst)
        else:
            shutil.copy2(src[k], dst)
        print(f"  {src[k]} -> {dst.relative_to(ROOT)}")
    # Which recording/voiceover the work/ files belong to (cloud_run starts fresh when this changes).
    write_json(root / "work" / "inputs.json", {"video": file_fingerprint(targets["video"]),
                                               "audio": file_fingerprint(targets["audio"])})

    rel = root.relative_to(ROOT).as_posix()
    print(f"\nCreated {rel}. Next: python tools/probe.py --project {rel}")


if __name__ == "__main__":
    main()
