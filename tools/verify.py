"""Quality gate for the rendered video -> work/verify.json; exits 1 when any check fails.

Checks: duration = voiceover +-0.1 s; exactly one video and one audio stream; resolution matches
the recording; no frozen span over 3 s that the plan did not ask for (ffmpeg freezedetect);
no black frame at any segment boundary. Exports a frame at every zoom peak to output/checks/.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

from check import out_to_src
from common import (Project, even, ffbin, ffprobe, fps_fraction, grab_frame, parser, save_jpg, tname,
                    video_size, write_json)
from render import Camera

FREEZE_MAX = 3.0


def intervals_union(iv):
    out = []
    for a, b in sorted(iv):
        if out and a <= out[-1][1] + 1e-3:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def uncovered(a, b, cover):
    left = b - a
    for c0, c1 in cover:
        left -= max(0.0, min(b, c1) - max(a, c0))
    return left


def expected_static(plan, scenes) -> list[list[float]]:
    """Output spans the plan made static on purpose: holds, and source still spans played back."""
    iv = []
    stills = [(s["start"], s["end"]) for s in (scenes or {}).get("stills", [])]
    for s in plan["segments"]:
        if s["mode"] == "hold":
            iv.append((s["out_start"], s["out_end"]))
            continue
        sp = (s["src_end"] - s["src_start"]) / (s["out_end"] - s["out_start"])
        for a, b in stills:
            lo, hi = max(a, s["src_start"]), min(b, s["src_end"])
            if hi > lo:
                iv.append((s["out_start"] + (lo - s["src_start"]) / sp, s["out_start"] + (hi - s["src_start"]) / sp))
    return intervals_union(iv)


def frames_at(path: Path, idx: list[int], w: int = 320):
    """Small grayscale frames at the given frame indices, in one decode pass."""
    if not idx:
        return {}
    vw, vh = video_size(path)
    h = even(w * vh / vw)
    expr = "+".join(f"eq(n\\,{i})" for i in sorted(set(idx)))
    cmd = [ffbin("ffmpeg"), "-v", "error", "-nostdin", "-i", str(path), "-an",
           "-vf", f"select='{expr}',scale={w}:{h}", "-fps_mode", "passthrough",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    res = subprocess.run(cmd, capture_output=True)
    n = w * h
    frames = [np.frombuffer(res.stdout[i:i + n], np.uint8).reshape(h, w)
              for i in range(0, len(res.stdout) - n + 1, n)]
    return dict(zip(sorted(set(idx)), frames))


def is_black(g) -> bool:
    return g is not None and float((g < 26).mean()) >= 0.98


def main():
    ap = parser(__doc__)
    ap.add_argument("--file", help="video to check (default output/final.mp4, or preview.mp4 with --preview)")
    ap.add_argument("--preview", action="store_true", help="check the 540p preview")
    a = ap.parse_args()
    pr = Project(a.project)
    probe = pr.need("probe.json", "tools/probe.py")
    plan = pr.need("plan.json", "the screencast-sync skill")
    scenes = pr.maybe("scenes.json")
    f = Path(a.file) if a.file else pr.output / ("preview.mp4" if a.preview else "final.mp4")
    if not f.exists():
        print(f"error: {f} not found - run tools/render.py first", file=sys.stderr)
        sys.exit(2)
    rec, vo = probe["recording"], probe["voiceover"]
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    info = ffprobe(f)
    dur = float(info["format"].get("duration", 0))
    check("duration", abs(dur - vo["duration"]) <= 0.1, f"{dur:.3f}s vs voiceover {vo['duration']:.3f}s")
    vs = [s for s in info["streams"] if s["codec_type"] == "video"]
    au = [s for s in info["streams"] if s["codec_type"] == "audio"]
    others = [s for s in info["streams"] if s["codec_type"] not in ("video", "audio")]
    check("streams", len(vs) == 1 and len(au) == 1,
          f"{len(vs)} video, {len(au)} audio{f', {len(others)} other' if others else ''}")
    want = (rec["width"], rec["height"])
    rj = pr.maybe("render.json") or {}
    if not a.preview and rj.get("delivered") and not rj.get("preview"):
        want = tuple(rj["delivered"])                    # render.py upscales the final file for delivery
    if a.preview:
        want = (even(rec["width"] * min(540, rec["height"]) / rec["height"]), min(540, rec["height"]))
    got = (int(vs[0]["width"]), int(vs[0]["height"])) if vs else (0, 0)
    check("resolution", got == want, f"{got[0]}x{got[1]} (expected {want[0]}x{want[1]})")

    segs_all = plan["segments"]

    # frozen spans
    cmd = [ffbin("ffmpeg"), "-hide_banner", "-nostats", "-nostdin", "-i", str(f), "-an",
           "-vf", f"scale=480:-2,freezedetect=n=-60dB:d={FREEZE_MAX}", "-f", "null", "-"]
    log = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    starts = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", log)]
    ends += [dur] * (len(starts) - len(ends))
    cover = expected_static(plan, scenes)
    bad, inherent = [], []
    small = (320, even(320 * rec["height"] / rec["width"]))
    for s0, s1 in zip(starts, ends):
        left = uncovered(s0, s1, cover)
        if left <= FREEZE_MAX:
            continue
        # Static in the source too (e.g. narration over an idle screen)? Then render didn't cause it.
        src_ts = [out_to_src(segs_all, t)[0] for t in (s0 + (s1 - s0) * f for f in (0.05, 0.35, 0.65, 0.9))]
        g = [cv2.cvtColor(grab_frame(pr.recording, t, fps_fraction(probe), small), cv2.COLOR_BGR2GRAY)
             for t in src_ts]
        change = max(float(cv2.absdiff(a, b).mean()) for a, b in zip(g, g[1:]))
        if change < 0.5:
            inherent.append(f"{s0:.2f}-{s1:.2f}")
        else:
            bad.append(f"{s0:.2f}-{s1:.2f} ({left:.1f}s not planned, source changes {change:.2f})")
    detail = "; ".join(bad) if bad else f"{len(starts)} freeze(s) over {FREEZE_MAX:g}s, all planned holds/stills"
    if inherent:
        detail += f"; static in the source too (not caused by the edit): {', '.join(inherent)}"
    check("frozen spans", not bad, detail)

    # black frames at segment boundaries (ignoring ones that are black in the source too)
    fps = float(vs[0]["avg_frame_rate"].split("/")[0]) / float(vs[0]["avg_frame_rate"].split("/")[1]) \
        if vs and vs[0].get("avg_frame_rate", "0/0") != "0/0" else plan["output"]["fps"]
    segs = plan["segments"]
    bounds = sorted({s["out_start"] for s in segs} | {segs[-1]["out_end"]})
    idx = []
    for b in bounds:
        n = int(round(b * fps))
        idx += [max(0, n - 1), n]
    last = int(dur * fps) - 1
    got_frames = frames_at(f, [min(i, last) for i in idx])
    blacks = []
    for b in bounds:
        n = int(round(b * fps))
        for i in (max(0, n - 1), min(n, last)):
            if is_black(got_frames.get(i)):
                src_t = out_to_src(segs, i / fps)[0]
                src = cv2.cvtColor(grab_frame(pr.recording, src_t, fps_fraction(probe), (320, even(320 * rec["height"] / rec["width"]))),
                                   cv2.COLOR_BGR2GRAY)
                if not is_black(src):
                    blacks.append(f"{i / fps:.3f}s")
    check("black frames at joins", not blacks,
          f"black at {', '.join(sorted(set(blacks)))}" if blacks else f"{len(bounds)} boundaries clean")

    # zoom peak frames for a human look
    zdir = pr.output / "checks"
    zdir.mkdir(exist_ok=True)
    for old in zdir.glob("zoom_*.jpg"):
        old.unlink()
    vw, vh = got if got != (0, 0) else want
    kk = vw / rec["width"]
    cam = Camera(plan.get("zooms") or [], rec["width"], rec["height"])
    zfiles = []
    for i, z in enumerate(sorted(plan.get("zooms") or [], key=lambda z: z["out_t"])):
        t = z["out_t"] + z["hold"] / 2
        img = grab_frame(f, t, None, (vw, vh))
        x0, y0, cw, _ = cam.rect(t)
        zz = rec["width"] / cw
        px, py = int((z["x"] - x0) * zz * kk), int((z["y"] - y0) * zz * kk)
        cv2.drawMarker(img, (px, py), (0, 0, 255), cv2.MARKER_CROSS, 24, 2)
        if img.shape[1] > 1600:
            img = cv2.resize(img, (1600, int(img.shape[0] * 1600 / img.shape[1])), interpolation=cv2.INTER_AREA)
        p = zdir / f"zoom_{i + 1:02d}_{tname(t)}.jpg"
        save_jpg(p, img)
        zfiles.append(str(p))
    print(f"  {len(zfiles)} zoom-peak frame(s) -> {zdir}")

    ok = all(c["ok"] for c in checks)
    write_json(pr.w("verify.json"), {"file": str(f), "ok": ok, "checks": checks, "zoom_frames": zfiles})
    print(f"verify: {'PASS' if ok else 'FAIL'} -> {pr.w('verify.json')}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
