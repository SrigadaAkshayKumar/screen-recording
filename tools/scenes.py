"""Screen-change detection -> work/scenes.json (+ work/clicks_rec.json when clicks.json exists).

Decodes the recording at reduced size (every frame), measures the per-frame mean absolute
difference, and reports:
  events        visible UI changes (onset t, peak magnitude, bbox in recording pixels)
  minor_events  small changes such as cursor moves and hover highlights
  stills        long low-motion spans (dead time, progress bars, spinners): speed-up/cut candidates
When input/clicks.json exists, the logger-to-recording time offset is estimated by matching
logged clicks to UI changes, and the clicks are converted to recording time and pixels.
"""
from __future__ import annotations

import time

import cv2
import numpy as np

from common import FrameReader, Project, die, even, fps_fraction, parser, read_json, write_json, warn


def rolling(a: np.ndarray, win: int, fn) -> np.ndarray:
    half = win // 2
    pad = np.pad(a, (half, half), mode="edge")
    return fn(np.lib.stride_tricks.sliding_window_view(pad, 2 * half + 1), axis=1)


def runs(mask: np.ndarray, max_gap: int = 0) -> list[tuple[int, int]]:
    """[start, end] index pairs of True runs, bridging gaps up to max_gap frames."""
    idx = np.flatnonzero(mask)
    if not len(idx):
        return []
    out, s, p = [], idx[0], idx[0]
    for i in idx[1:]:
        if i - p > max_gap + 1:
            out.append((s, p))
            s = i
        p = i
    out.append((s, p))
    return out


def estimate_offset(clicks: list[dict], events: list[dict], minor: list[dict]) -> tuple[float, int]:
    """Logger time + offset = recording time. Votes on the lag between each click and the UI
    changes that start 0-0.6 s after it, then takes the low edge of the best cluster."""
    onsets = np.array([e["t"] for e in events] + [m["t"] for m in minor])
    if not len(onsets) or not clicks:
        return 0.0, 0
    lags = []
    for c in clicks:
        d = onsets - c["t"]
        lags += list(d[(d > -20) & (d < 20)])
    if not lags:
        return 0.0, 0
    lags = np.array(lags)
    best, best_n = 0.0, -1
    for cand in np.arange(lags.min() - 0.6, lags.max() + 0.05, 0.02):
        n = 0
        for c in clicks:
            d = onsets - (c["t"] + cand)
            n += bool(np.any((d >= 0) & (d <= 0.6)))
        if n > best_n:
            best, best_n = cand, n
    # Shift to the latest offset that still keeps every matched change at or after its click.
    matched = []
    for c in clicks:
        d = onsets - (c["t"] + best)
        ok = d[(d >= 0) & (d <= 0.6)]
        if len(ok):
            matched.append(ok.min())
    if matched:
        best += float(np.percentile(matched, 20)) - 0.03
    return float(best), int(best_n)


def main():
    ap = parser(__doc__)
    ap.add_argument("--height", type=int, default=480, help="analysis height (default 480)")
    ap.add_argument("--k", type=float, default=6.0, help="threshold = median + k * MAD (default 6)")
    ap.add_argument("--min-magnitude", type=float, default=0.08, help="absolute floor on mean abs diff (0-255)")
    ap.add_argument("--min-area", type=float, default=0.002,
                    help="changed-pixel fraction for a real UI change (smaller = minor, e.g. cursor)")
    ap.add_argument("--min-still", type=float, default=1.5, help="shortest still span in seconds")
    ap.add_argument("--clicks-offset", type=float, help="force logger->recording offset in seconds")
    ap.add_argument("--click-region", help="x,y,w,h of the recorded area in logger coordinates "
                                           "(default: the whole logged screen)")
    a = ap.parse_args()
    pr = Project(a.project)
    probe = pr.need("probe.json", "tools/probe.py")
    rec = probe["recording"]
    fps = fps_fraction(probe)
    W, H = rec["width"], rec["height"]
    ah = min(a.height, H)
    aw = even(W * ah / H)
    sx, sy = W / aw, H / ah
    fpsf = float(fps)

    print(f"decoding {pr.recording.name} at {aw}x{ah}, {fpsf:.3f} fps ...", flush=True)
    t0 = time.time()
    reader = FrameReader(pr.recording, fps, (aw, ah), gray=True, scale_flags="area")
    mags, areas, boxes = [], [], []
    prev = None
    total = max(1, rec["frames"])
    next_pct = 10
    while True:
        f = reader.read()
        if f is None:
            break
        if prev is None:
            mags.append(0.0); areas.append(0.0); boxes.append((0, 0, 0, 0))
        else:
            d = cv2.absdiff(f, prev)
            mags.append(float(d.mean()))
            _, m = cv2.threshold(d, 12, 255, cv2.THRESH_BINARY)
            cnt = cv2.countNonZero(m)
            areas.append(cnt / (aw * ah))
            boxes.append(cv2.boundingRect(m) if cnt else (0, 0, 0, 0))
        prev = f
        pct = 100 * len(mags) // total
        if pct >= next_pct:
            print(f"  {min(pct, 100)}%", flush=True)
            next_pct += 10
    reader.close()
    n = len(mags)
    if n < 2:
        die("could not decode the recording")
    mags_a, areas_a = np.array(mags), np.array(areas)
    bx = np.array(boxes, dtype=float)
    has = bx[:, 2] > 0

    win = max(3, int(2 * fpsf) | 1)
    base = rolling(mags_a, win, np.median)
    mad = rolling(np.abs(mags_a - base), win, np.median)
    thr = np.maximum(a.min_magnitude, base + a.k * 1.4826 * mad)
    above = mags_a > thr
    major = above & (areas_a >= a.min_area)

    def box_union(i0, i1):
        sel = has[i0:i1 + 1]
        if not sel.any():
            return None
        b = bx[i0:i1 + 1][sel]
        x0, y0 = b[:, 0].min(), b[:, 1].min()
        x1, y1 = (b[:, 0] + b[:, 2]).max(), (b[:, 1] + b[:, 3]).max()
        return [int(x0 * sx), int(y0 * sy), int(np.ceil((x1 - x0) * sx)), int(np.ceil((y1 - y0) * sy))]

    events = []
    for i0, i1 in runs(major, max_gap=2):
        pk = i0 + int(np.argmax(mags_a[i0:i1 + 1]))
        events.append({"id": f"E{len(events) + 1}", "t": i0 / fpsf, "t_peak": pk / fpsf,
                       "t_end": (i1 + 1) / fpsf, "magnitude": mags_a[pk], "area": float(areas_a[i0:i1 + 1].max()),
                       "bbox": box_union(i0, i1), "long": (i1 - i0 + 1) / fpsf > 2.0})
    minor = []
    for i0, i1 in runs(above & ~major, max_gap=2):
        if major[max(0, i0 - 3):i1 + 4].any():
            continue
        minor.append({"t": i0 / fpsf, "t_end": (i1 + 1) / fpsf, "bbox": box_union(i0, i1)})

    # Still frames: no major change and every change in the surrounding 1 s fits in a small box.
    big = 1e9
    x0 = np.where(has, bx[:, 0], big); y0 = np.where(has, bx[:, 1], big)
    x1 = np.where(has, bx[:, 0] + bx[:, 2], -big); y1 = np.where(has, bx[:, 1] + bx[:, 3], -big)
    w1 = max(3, int(fpsf) | 1)
    ux = rolling(x1, w1, np.max) - rolling(x0, w1, np.min)
    uy = rolling(y1, w1, np.max) - rolling(y0, w1, np.min)
    small = (ux < 0.08 * aw) & (uy < 0.08 * ah)
    still = ~major & small          # an empty window has negative extent, so it counts as small
    stills = []
    for i0, i1 in runs(still, max_gap=2):
        if (i1 - i0 + 1) / fpsf >= a.min_still:
            seg = slice(i0, i1 + 1)
            stills.append({"start": i0 / fpsf, "end": (i1 + 1) / fpsf,
                           "activity": float(mags_a[seg].mean()),
                           "frozen": bool(areas_a[seg].max() == 0),
                           "bbox": box_union(i0, i1)})

    out = {"analysis_size": [aw, ah], "fps": fpsf, "frames": n,
           "params": {"k": a.k, "min_magnitude": a.min_magnitude, "min_area": a.min_area, "min_still": a.min_still},
           "events": events, "minor_events": minor, "stills": stills}

    if pr.clicks:
        out["clicks_sync"] = sync_clicks(pr, a, rec, events, minor)

    write_json(pr.w("scenes.json"), out)
    print(f"{n} frames in {time.time() - t0:.0f}s: {len(events)} change events, "
          f"{len(minor)} minor, {len(stills)} still spans")
    for s in stills:
        print(f"  still {s['start']:7.2f}-{s['end']:7.2f}  ({s['end'] - s['start']:.1f}s"
              f"{', frozen' if s['frozen'] else ''})")
    print(f"-> {pr.w('scenes.json')}")


def sync_clicks(pr: Project, a, rec: dict, events: list, minor: list) -> dict:
    data = read_json(pr.clicks)
    scr = data.get("screen") or {}
    sw, sh = scr.get("width"), scr.get("height")
    if a.click_region:
        try:
            rx, ry, rw, rh = (float(v) for v in a.click_region.split(","))
        except ValueError:
            die("--click-region must be x,y,w,h")
    else:
        if not sw or not sh:
            die("clicks.json has no screen size; pass --click-region x,y,w,h")
        rx, ry, rw, rh = 0.0, 0.0, float(sw), float(sh)
    kx, ky = rec["width"] / rw, rec["height"] / rh
    if abs(kx - ky) > 0.02 * kx:
        warn(f"recording aspect differs from the logged screen ({kx:.3f} vs {ky:.3f}); "
             f"was only part of the screen recorded? use --click-region")

    def conv(x, y):
        return (x - rx) * kx, (y - ry) * ky

    raw = data.get("clicks", [])
    if a.clicks_offset is not None:
        offset, matched, method = a.clicks_offset, None, "manual"
    else:
        rec_clicks = [{"t": c["t"]} for c in raw]
        offset, matched, method = *estimate_offset(rec_clicks, events, minor), "ui-change correlation"
    clicks = []
    for c in raw:
        t = c["t"] + offset
        if t < 0 or t > rec["duration"]:
            continue
        x, y = conv(c["x"], c["y"])
        item = {"t": t, "x": x, "y": y, "button": c.get("button", "left"), "t_log": c["t"]}
        if "t_up" in c:
            x2, y2 = conv(c["x_up"], c["y_up"])
            item.update({"t_up": c["t_up"] + offset, "x_up": x2, "y_up": y2})
        if not (0 <= x < rec["width"] and 0 <= y < rec["height"]):
            item["outside"] = True
        clicks.append(item)
    res = {"offset": offset, "method": method, "matched": matched, "total": len(raw),
           "scale": [kx, ky], "region": [rx, ry, rw, rh], "clicks": clicks}
    write_json(pr.w("clicks_rec.json"), res)
    conf = f"{matched}/{len(raw)} clicks matched a UI change" if matched is not None else "manual"
    print(f"clicks: offset {offset:+.3f}s ({conf}) -> {pr.w('clicks_rec.json')}")
    if raw:
        first = clicks[0] if clicks else None
        if first:
            print(f"  verify: python tools/frames.py --project {a.project} --at {first['t']:.3f} "
                  f"--mark {first['x']:.0f},{first['y']:.0f}   (cursor should sit on the mark)")
    if matched is not None and raw and matched < 0.4 * len(raw):
        warn("few clicks matched UI changes; check the offset by eye and pass --clicks-offset if needed")
    return {k: v for k, v in res.items() if k != "clicks"}


if __name__ == "__main__":
    main()
