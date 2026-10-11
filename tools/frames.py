"""Images for Claude to read -> work/frames/ (every image is at most 1600 px wide).

  --sheets              contact sheets: 12 frames per sheet (4x3), one every --every seconds
  --event-sheets        one tile per change event from scenes.json, just after the change
  --sheet-at T1,T2,...  one contact sheet of the given times (e.g. zoom peaks of a preview)
  --at T1,T2,...        single frames; add --crop x,y,w,h to see a region at native resolution
  --around T1,T2,...    0.5 s before and after each time, stacked in one image
Overlays (recording-pixel coordinates): --grid draws labelled gridlines, --mark x,y a crosshair.
--video samples another file, e.g. output/preview.mp4 (coordinates still in recording pixels).
"""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

import cv2
import numpy as np

from common import (Project, die, even, ffbin, fps_fraction, grab_frame, parse_times, parser,
                    save_jpg, tname, video_size)

MAX_W = 1600
FONT = cv2.FONT_HERSHEY_SIMPLEX


def label(img, text, org=None, scale=0.55):
    """Text on a dark box; default bottom-left so toolbars at the top stay visible."""
    (tw, th), base = cv2.getTextSize(text, FONT, scale, 1)
    x, y = org if org else (6, img.shape[0] - th - base - 6)
    cv2.rectangle(img, (x - 4, y - 2), (x + tw + 4, y + th + base + 2), (0, 0, 0), -1)
    cv2.putText(img, text, (x, y + th), FONT, scale, (255, 255, 255), 1, cv2.LINE_AA)


def sheet(tiles: list[tuple[np.ndarray, str]], cols: int = 4) -> np.ndarray:
    th, tw = tiles[0][0].shape[:2]
    rows = math.ceil(len(tiles) / cols)
    gap = 4
    out = np.full((rows * (th + gap) + gap, cols * (tw + gap) + gap, 3), 40, np.uint8)
    for i, (img, txt) in enumerate(tiles):
        r, c = divmod(i, cols)
        y, x = gap + r * (th + gap), gap + c * (tw + gap)
        tile = img.copy()
        label(tile, txt)
        out[y:y + th, x:x + tw] = tile
    return out


class Src:
    """The sampled video plus the mapping from recording pixels to its pixels."""

    def __init__(self, pr: Project, probe: dict, video: str | None):
        rec = probe["recording"]
        self.rec_w, self.rec_h = rec["width"], rec["height"]
        if video:
            self.path = Path(video)
            if not self.path.exists():
                die(f"--video not found: {video}")
            self.fps = None
        else:
            self.path = pr.recording
            self.fps = fps_fraction(probe)
        self.w, self.h = video_size(self.path)
        self.k = self.w / self.rec_w
        self.duration = rec["duration"]

    def frame(self, t: float):
        return grab_frame(self.path, t, self.fps, (self.w, self.h))


def overlay(img, src: Src, crop, grid: bool, marks: list[tuple[float, float]]):
    """Crop (recording px) and draw grid/marks. Returns the image at native sampled resolution."""
    k = src.k
    ox = oy = 0.0
    if crop:
        x, y, w, h = crop
        x0, y0 = max(0, int(x * k)), max(0, int(y * k))
        x1, y1 = min(src.w, int((x + w) * k)), min(src.h, int((y + h) * k))
        if x1 <= x0 or y1 <= y0:
            die(f"--crop {crop} is outside the frame")
        img = img[y0:y1, x0:x1].copy()
        ox, oy = x0 / k, y0 / k
    if grid:
        span = img.shape[1] / k
        step = 50 if span <= 700 else (100 if span <= 2200 else 200)
        lay = img.copy()
        gx = math.ceil(ox / step) * step
        while (gx - ox) * k < img.shape[1]:
            px = int(round((gx - ox) * k))
            cv2.line(lay, (px, 0), (px, img.shape[0]), (0, 200, 255), 1)
            gx += step
        gy = math.ceil(oy / step) * step
        while (gy - oy) * k < img.shape[0]:
            py = int(round((gy - oy) * k))
            cv2.line(lay, (0, py), (img.shape[1], py), (0, 200, 255), 1)
            gy += step
        img = cv2.addWeighted(lay, 0.45, img, 0.55, 0)
        gx = math.ceil(ox / step) * step
        while (gx - ox) * k < img.shape[1]:
            if int(gx) % (2 * step) == 0:
                label(img, str(int(gx)), (int((gx - ox) * k) + 3, 3), 0.4)
            gx += step
        gy = math.ceil(oy / step) * step
        while (gy - oy) * k < img.shape[0]:
            if int(gy) % (2 * step) == 0 and gy > oy:
                label(img, str(int(gy)), (3, int((gy - oy) * k) + 3), 0.4)
            gy += step
    for mx, my in marks:
        px, py = int(round((mx - ox) * k)), int(round((my - oy) * k))
        cv2.circle(img, (px, py), 14, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.line(img, (px - 22, py), (px - 6, py), (0, 0, 255), 2)
        cv2.line(img, (px + 6, py), (px + 22, py), (0, 0, 255), 2)
        cv2.line(img, (px, py - 22), (px, py - 6), (0, 0, 255), 2)
        cv2.line(img, (px, py + 6), (px, py + 22), (0, 0, 255), 2)
    return img


def cap(img, full: bool):
    if full or img.shape[1] <= MAX_W:
        return img
    s = MAX_W / img.shape[1]
    return cv2.resize(img, (MAX_W, int(img.shape[0] * s)), interpolation=cv2.INTER_AREA)


def tile_size(src: Src) -> tuple[int, int]:
    tw = (MAX_W - 5 * 4) // 4
    return tw, even(tw * src.h / src.w)


def periodic_tiles(src: Src, every: float):
    """One sequential decode at tile size through ffmpeg's fps filter (fast)."""
    tw, th = tile_size(src)
    cmd = [ffbin("ffmpeg"), "-v", "error", "-nostdin", "-i", str(src.path), "-an",
           "-vf", f"setpts=PTS-STARTPTS,fps=1/{every},scale={tw}:{th}:flags=area",
           "-f", "rawvideo", "-pix_fmt", "bgr24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    i = 0
    while True:
        buf = p.stdout.read(tw * th * 3)
        if len(buf) < tw * th * 3:
            break
        yield i * every, np.frombuffer(buf, np.uint8).reshape(th, tw, 3)
        i += 1
    p.wait()


def write_sheets(out_dir: Path, prefix: str, tiles: list, per: int = 12) -> list[Path]:
    for old in out_dir.glob(f"{prefix}_*.jpg"):
        old.unlink()
    paths = []
    for n in range(0, len(tiles), per):
        p = out_dir / f"{prefix}_{n // per + 1:02d}.jpg"
        save_jpg(p, sheet(tiles[n:n + per]))
        paths.append(p)
    return paths


def main():
    ap = parser(__doc__)
    ap.add_argument("--sheets", action="store_true")
    ap.add_argument("--every", type=float, help="seconds between sheet tiles (default: ~1 per 2 s, max 96 tiles)")
    ap.add_argument("--event-sheets", action="store_true")
    ap.add_argument("--sheet-at", help="comma-separated times for one custom sheet")
    ap.add_argument("--name", default="custom", help="file prefix for --sheet-at")
    ap.add_argument("--at", help="comma-separated times for single frames")
    ap.add_argument("--around", help="comma-separated times: 0.5 s before/after pairs")
    ap.add_argument("--delta", type=float, default=0.5, help="offset for --around (default 0.5)")
    ap.add_argument("--crop", help="x,y,w,h in recording pixels (native resolution, no downscale)")
    ap.add_argument("--grid", action="store_true", help="labelled gridlines in recording pixels")
    ap.add_argument("--mark", action="append", default=[], help="x,y crosshair (repeatable)")
    ap.add_argument("--full", action="store_true", help="do not cap the width at 1600 px")
    ap.add_argument("--video", help="sample this file instead of the recording")
    ap.add_argument("--out-dir", help="default work/frames")
    a = ap.parse_args()
    pr = Project(a.project)
    probe = pr.need("probe.json", "tools/probe.py")
    src = Src(pr, probe, a.video)
    out_dir = Path(a.out_dir) if a.out_dir else pr.frames
    out_dir.mkdir(parents=True, exist_ok=True)
    crop = None
    if a.crop:
        try:
            crop = tuple(float(v) for v in a.crop.split(","))
            assert len(crop) == 4
        except (ValueError, AssertionError):
            die("--crop must be x,y,w,h")
    marks = []
    for m in a.mark:
        try:
            mx, my = (float(v) for v in m.split(","))
            marks.append((mx, my))
        except ValueError:
            die(f"--mark must be x,y, got {m!r}")
    if not any([a.sheets, a.event_sheets, a.sheet_at, a.at, a.around]):
        die("nothing to do: pass --sheets, --event-sheets, --sheet-at, --at or --around")
    written: list[Path] = []
    dur = src.duration

    if a.sheets:
        every = a.every or max(1.0, round(dur / 96, 1), 2.0 if dur > 60 else 1.0)
        tiles = [(img, f"{t:.1f}s") for t, img in periodic_tiles(src, every)]
        if not tiles:
            die("no frames decoded for the contact sheets")
        written += write_sheets(out_dir, "sheet", tiles)
        print(f"{len(tiles)} tiles, one every {every:g}s")

    if a.event_sheets:
        scenes = pr.need("scenes.json", "tools/scenes.py")
        tw, th = tile_size(src)
        tiles = []
        for e in scenes["events"]:
            t = min(dur - 0.05, e["t_end"] + 0.15)
            img = cv2.resize(src.frame(t), (tw, th), interpolation=cv2.INTER_AREA)
            if e.get("bbox"):
                x, y, w, h = (v * src.k * tw / src.w for v in e["bbox"])
                cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), (0, 0, 255), 1)
            tiles.append((img, f"{e['id']} {e['t']:.2f}s"))
        if tiles:
            written += write_sheets(out_dir, "events", tiles)
        print(f"{len(tiles)} event tiles")

    if a.sheet_at:
        tw, th = tile_size(src)
        tiles = []
        for t in parse_times(a.sheet_at):
            img = overlay(src.frame(t), src, None, a.grid, marks)
            tiles.append((cv2.resize(img, (tw, th), interpolation=cv2.INTER_AREA), f"{t:.2f}s"))
        written += write_sheets(out_dir, a.name, tiles)

    if a.at:
        for t in parse_times(a.at):
            img = cap(overlay(src.frame(t), src, crop, a.grid, marks), a.full or bool(crop))
            label(img, f"{t:.3f}s")
            p = out_dir / f"at_{tname(t)}{'_crop' if crop else ''}.jpg"
            save_jpg(p, img, 92)
            written.append(p)

    if a.around:
        for t in parse_times(a.around):
            pair = []
            for tt, tag in ((max(0.0, t - a.delta), "before"), (min(dur - 0.02, t + a.delta), "after")):
                img = cap(overlay(src.frame(tt), src, crop, a.grid, marks), a.full)
                label(img, f"{tag} {tt:.3f}s")
                pair.append(img)
            sepr = np.full((6, pair[0].shape[1], 3), (0, 0, 255), np.uint8)
            p = out_dir / f"around_{tname(t)}.jpg"
            save_jpg(p, np.vstack([pair[0], sepr, pair[1]]), 90)
            written.append(p)

    for p in written:
        print(f"-> {p}")


if __name__ == "__main__":
    main()
