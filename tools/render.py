"""Apply work/plan.json: retime + zoom + ripple + voiceover -> output/final.mp4.

    python tools/render.py --project projects/demo             # full quality -> output/final.mp4
    python tools/render.py --project projects/demo --preview   # 540p, ultrafast -> output/preview.mp4
    python tools/render.py --project projects/demo --from 20 --to 30 --preview
    python tools/render.py --project projects/demo --check     # validate the plan only

Source frames come from an ffmpeg pipe (rawvideo bgr24); each output frame is built in Python and
piped to libx264 together with the voiceover. Writes work/render.json (zoom peaks, joins, timing).
"""
from __future__ import annotations

import bisect
import math
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import cv2
import numpy as np

from check import out_to_src, report, validate_plan, zoom_window
from common import (FrameReader, Project, die, even, ffbin, fps_fraction, parse_color, parser, r3,
                    write_json)

XFADE_FRAMES = 6
RIPPLE_DUR = 0.5


def ease(u: float) -> float:
    """Cubic ease-in-out on [0, 1]."""
    u = min(max(u, 0.0), 1.0)
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2


class Camera:
    """Virtual camera: a crop rectangle in recording pixels for every output time.

    Each zoom contributes an eased weight (in -> hold -> out). The zoom amount is the smooth union
    1 - prod(1 - w_i) and the target is the weight-averaged zoom rectangle, so overlapping zooms
    pan from one target to the next without snapping. Every rectangle is a convex mix of
    rectangles that lie inside the frame, so the crop never leaves the frame.
    """

    def __init__(self, zooms: list[dict], W: int, H: int):
        self.W, self.H = W, H
        self.z = []
        for z in zooms:
            s = z["scale"]
            w, h = W / s, H / s
            x0 = min(max(z["x"] - w / 2, 0.0), W - w)
            y0 = min(max(z["y"] - h / 2, 0.0), H - h)
            a, b = zoom_window(z)
            self.z.append((a, b, z, np.array([x0, y0, w, h])))
        self.full = np.array([0.0, 0.0, W, H])

    @staticmethod
    def weight(z: dict, t: float) -> float:
        t0, t1, t2 = z["out_t"] - z["in"], z["out_t"], z["out_t"] + z["hold"]
        if t < t0 or t > t2 + z["out"]:
            return 0.0
        if t < t1:
            return ease((t - t0) / z["in"])
        if t <= t2:
            return 1.0
        return 1.0 - ease((t - t2) / z["out"])

    def rect(self, t: float) -> np.ndarray:
        ws, rs = [], []
        for a, b, z, r in self.z:
            if a <= t <= b:
                w = self.weight(z, t)
                if w > 0:
                    ws.append(w)
                    rs.append(r)
        if not ws:
            return self.full
        amount = 1.0 - float(np.prod([1.0 - w for w in ws]))
        target = sum(w * r for w, r in zip(ws, rs)) / sum(ws)
        r = self.full + amount * (target - self.full)
        r[2] = min(r[2], self.W); r[3] = min(r[3], self.H)
        r[0] = min(max(r[0], 0.0), self.W - r[2]); r[1] = min(max(r[1], 0.0), self.H - r[3])
        return r


class Painter:
    """Ripples and the optional cursor halo, drawn in output space."""

    def __init__(self, plan: dict, k_out: float, color, alpha: float, halo: bool):
        self.ripples = sorted(plan.get("ripples") or [], key=lambda r: r["out_t"])
        self.rt = [r["out_t"] for r in self.ripples]
        st = plan.get("style") or {}
        self.color = color
        self.alpha = alpha
        self.r0 = st.get("ripple_r0", 12) * k_out
        self.r1 = st.get("ripple_r1", 50) * k_out
        self.halo = None
        if halo:
            keys = plan.get("cursor") or self.ripples
            self.keys = sorted(({"out_t": c["out_t"], "x": c["x"], "y": c["y"]} for c in keys), key=lambda c: c["out_t"])
            if self.keys:
                R = int(round(st.get("halo_radius", 46) * k_out))
                yy, xx = np.mgrid[-R:R + 1, -R:R + 1].astype(np.float32)
                a = np.exp(-(xx ** 2 + yy ** 2) / (2 * (R / 2.2) ** 2)) * st.get("halo_alpha", 0.45)
                a[(xx ** 2 + yy ** 2) > R * R] = 0
                self.halo = (R, a[..., None], np.array(parse_color(st.get("halo_color", "#FFD84D")), np.float32))

    def cursor_at(self, t: float):
        ks = self.keys
        if t <= ks[0]["out_t"]:
            return ks[0]["x"], ks[0]["y"]
        for a, b in zip(ks, ks[1:]):
            if t <= b["out_t"]:
                move = min(0.6, b["out_t"] - a["out_t"])
                u = ease((t - (b["out_t"] - move)) / move) if move > 0 else 1.0
                return a["x"] + (b["x"] - a["x"]) * u, a["y"] + (b["y"] - a["y"]) * u
        return ks[-1]["x"], ks[-1]["y"]

    def draw(self, img, t: float, to_out):
        if self.halo:
            R, a, col = self.halo
            px, py = to_out(*self.cursor_at(t))
            cx, cy = int(round(px)), int(round(py))
            x0, y0, x1, y1 = cx - R, cy - R, cx + R + 1, cy + R + 1
            sx0, sy0 = max(0, -x0), max(0, -y0)
            x0, y0, x1, y1 = max(0, x0), max(0, y0), min(img.shape[1], x1), min(img.shape[0], y1)
            if x1 > x0 and y1 > y0:
                aa = a[sy0:sy0 + y1 - y0, sx0:sx0 + x1 - x0]
                roi = img[y0:y1, x0:x1].astype(np.float32)
                img[y0:y1, x0:x1] = (roi * (1 - aa) + col * aa).astype(np.uint8)
        i = bisect.bisect_right(self.rt, t)
        j = bisect.bisect_left(self.rt, t - RIPPLE_DUR)
        for r in self.ripples[j:i]:
            u = (t - r["out_t"]) / RIPPLE_DUR
            if not 0 <= u <= 1:
                continue
            rad = self.r0 + (self.r1 - self.r0) * (1 - (1 - u) ** 2)
            fade = 1 - u
            px, py = to_out(r["x"], r["y"])
            pad = int(rad + 6)
            x0, y0 = max(0, int(px) - pad), max(0, int(py) - pad)
            x1, y1 = min(img.shape[1], int(px) + pad + 1), min(img.shape[0], int(py) + pad + 1)
            if x1 <= x0 or y1 <= y0:
                continue
            roi = img[y0:y1, x0:x1]
            c = (int(round((px - x0) * 16)), int(round((py - y0) * 16)))
            rr = int(round(rad * 16))
            fill = roi.copy()
            cv2.circle(fill, c, rr, self.color, -1, cv2.LINE_AA, shift=4)
            cv2.addWeighted(fill, self.alpha * 0.55 * fade, roi, 1 - self.alpha * 0.55 * fade, 0, dst=roi)
            ring = roi.copy()
            cv2.circle(ring, c, rr, self.color, max(2, int(round(3 * self.r1 / 50))), cv2.LINE_AA, shift=4)
            cv2.addWeighted(ring, self.alpha * fade, roi, 1 - self.alpha * fade, 0, dst=roi)


def main():
    ap = parser(__doc__)
    ap.add_argument("--preview", action="store_true", help="540p, ultrafast -> output/preview.mp4")
    ap.add_argument("--from", dest="t_from", type=float, help="render from this output time")
    ap.add_argument("--to", dest="t_to", type=float, help="render up to this output time")
    ap.add_argument("--out", help="output file (default output/final.mp4 or output/preview.mp4)")
    ap.add_argument("--ripple-color", help="#RRGGBB or r,g,b (default plan.style.ripple_color or #2F80ED)")
    ap.add_argument("--ripple-alpha", type=float, help="0-1 (default 0.6)")
    ap.add_argument("--cursor-halo", action="store_true", help="soft yellow halo following the clicks")
    ap.add_argument("--no-xfade", action="store_true", help="hard cuts instead of 6-frame cross-fades")
    ap.add_argument("--check", action="store_true", help="validate plan.json and exit")
    ap.add_argument("--deliver-height", type=int, default=1440,
                    help="final file height: the edit is upscaled (lanczos + light sharpen) to this; YouTube "
                         "streams 1440p uploads at a much higher bitrate than 1080p, so screen text stays "
                         "crisp (default 1440; 0 = keep the recording size)")
    a = ap.parse_args()
    pr = Project(a.project)
    probe = pr.need("probe.json", "tools/probe.py")
    plan = pr.need("plan.json", "the screencast-sync skill")
    err, wrn = validate_plan(plan, probe, pr.maybe("actions.json"), pr.maybe("lines.json"),
                             pr.maybe("scenes.json"))
    if not report("plan.json", err, wrn):
        die("fix plan.json before rendering", 1)
    if a.check:
        return

    rec = probe["recording"]
    W, H = rec["width"], rec["height"]
    o = plan["output"]
    fps = Fraction(o["fps"]).limit_denominator(1001)
    if abs(float(fps) - rec["fps"]) < 0.01:
        fps = fps_fraction(probe)
    src_fps = fps_fraction(probe)
    D = o["duration"]
    if a.preview:
        RH = min(540, H)
        RW = even(W * RH / H)
    else:
        RW, RH = o["width"], o["height"]
    k = RW / W                                       # recording px -> render px
    n_total = int(round(D * float(fps)))
    n0 = int(round((a.t_from or 0.0) * float(fps)))
    n1 = int(round(a.t_to * float(fps))) if a.t_to is not None else n_total
    n0, n1 = max(0, n0), min(n_total, n1)
    if n1 <= n0:
        die("--from/--to select no frames")
    ranged = n0 > 0 or n1 < n_total

    if a.out:
        out = Path(a.out)
    elif ranged:
        out = pr.output / f"{'preview' if a.preview else 'range'}_{n0 / float(fps):.1f}-{n1 / float(fps):.1f}.mp4"
    else:
        out = pr.output / ("preview.mp4" if a.preview else "final.mp4")

    style = plan.get("style") or {}
    color = parse_color(a.ripple_color or style.get("ripple_color", "#2F80ED"))
    alpha = a.ripple_alpha if a.ripple_alpha is not None else style.get("ripple_alpha", 0.6)
    painter = Painter(plan, k, color, alpha, a.cursor_halo or bool(style.get("cursor_halo")))
    cam = Camera(plan.get("zooms") or [], W, H)
    segs = plan["segments"]

    t_a = n0 / float(fps)
    dur = (n1 - n0) / float(fps)
    # Delivery size: upscale the finished frames (never the source) for a sharper stream on YouTube.
    DH = a.deliver_height if (a.deliver_height and not a.preview and a.deliver_height > RH) else RH
    DW = even(RW * DH / RH)
    SHARPEN = ",unsharp=5:5:0.45:5:5:0.0" if DH > RH else ""
    vlog = open(pr.w("render-ffmpeg.log"), "w", encoding="utf-8")
    enc_cmd = [ffbin("ffmpeg"), "-v", "error", "-y", "-nostdin",
               "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{RW}x{RH}",
               "-r", f"{fps.numerator}/{fps.denominator}", "-i", "-",
               "-ss", f"{t_a:.3f}", "-t", f"{dur:.3f}", "-i", str(pr.voiceover),
               "-map", "0:v:0", "-map", "1:a:0",
               *(["-vf", f"scale=w={DW}:h={DH}:flags=lanczos+accurate_rnd+full_chroma_int:out_color_matrix=bt709"
                         f"{SHARPEN},format=yuv420p"] if not a.preview else
                 ["-vf", "scale=out_color_matrix=bt709,format=yuv420p"]),
               "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv",
               "-c:v", "libx264", "-preset", "ultrafast" if a.preview else "slow",
               "-crf", "23" if a.preview else "16", "-pix_fmt", "yuv420p",
               *([] if a.preview else ["-profile:v", "high", "-x264-params", "aq-mode=3:deblock=-1,-1"]),
               "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)]
    enc = subprocess.Popen(enc_cmd, stdin=subprocess.PIPE, stderr=vlog)

    src0 = out_to_src(segs, t_a)[0]
    reader = FrameReader(pr.recording, src_fps, (RW, RH), start_index=int(math.floor(src0 * float(src_fps) + 1e-6)))
    max_idx = int(round(rec["duration"] * float(src_fps))) - 1

    def src_frame(t_src: float):
        idx = min(max(int(math.floor(t_src * float(src_fps) + 1e-6)), 0), max_idx)
        f = reader.get(idx, reseek_after=int(10 * float(src_fps)))
        if f is None:
            die(f"could not decode the recording at {t_src:.3f}s")
        return f

    print(f"rendering {out.name}: {RW}x{RH} @ {float(fps):.3f} fps, frames {n0}-{n1} "
          f"({dur:.1f}s), {len(segs)} segments, {len(cam.z)} zooms, {len(painter.ripples)} ripples", flush=True)
    started = time.time()
    prev_seg, prev_last = None, None
    seg_frame0 = {}
    step = max(1, (n1 - n0) // 20)
    try:
        for n in range(n0, n1):
            t = n / float(fps)
            t_src, si = out_to_src(segs, t)
            frame = src_frame(t_src)
            if si != prev_seg:
                if prev_seg is not None:
                    prev_last = last_src
                seg_frame0[si] = n
                prev_seg = si
            last_src = frame
            seg = segs[si]
            j = n - seg_frame0[si]
            if seg.get("xfade") and not a.no_xfade and prev_last is not None and j < XFADE_FRAMES:
                u = (j + 1) / (XFADE_FRAMES + 1)
                frame = cv2.addWeighted(frame, u, prev_last, 1 - u, 0)

            x0, y0, cw, ch = cam.rect(t)
            z = W / cw
            if abs(z - 1.0) < 1e-4 and abs(x0) < 1e-3 and abs(y0) < 1e-3:
                img = frame.copy()
            else:
                M = np.array([[z, 0, -z * k * x0], [0, z, -z * k * y0]], np.float32)
                img = cv2.warpAffine(frame, M, (RW, RH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

            def to_out(px, py, x0=x0, y0=y0, z=z):
                return (px - x0) * z * k, (py - y0) * z * k

            painter.draw(img, t, to_out)
            enc.stdin.write(np.ascontiguousarray(img).tobytes())
            if (n - n0) % step == 0 and n > n0:
                el = time.time() - started
                print(f"  {100 * (n - n0) // (n1 - n0):3d}%  frame {n - n0}/{n1 - n0}  out {t:6.2f}s  "
                      f"src {t_src:6.2f}s  {(n - n0) / el:5.1f} fps", flush=True)
        enc.stdin.close()
    except (BrokenPipeError, OSError):
        enc.wait()
        vlog.close()
        die(f"the encoder stopped early - see {pr.w('render-ffmpeg.log')}:\n"
            + pr.w("render-ffmpeg.log").read_text(encoding="utf-8")[-1500:])
    finally:
        reader.close()
    rc = enc.wait()
    vlog.close()
    if rc != 0:
        die(f"encoder failed (exit {rc}) - see {pr.w('render-ffmpeg.log')}")
    el = time.time() - started
    print(f"  100%  {n1 - n0} frames in {el:.0f}s ({(n1 - n0) / el:.1f} fps) -> {out}")

    joins = []
    for p, s in zip(segs, segs[1:]):
        joins.append({"out_t": s["out_start"], "cut": abs(s["src_start"] - p["src_end"]) > 1e-3,
                      "xfade": bool(s.get("xfade")), "into": s["mode"]})
    write_json(pr.w("render.json"), {
        "output": str(out), "preview": a.preview, "range": [r3(t_a), r3(t_a + dur)],
        "width": RW, "height": RH, "delivered": [DW, DH], "fps": float(fps), "frames": n1 - n0, "elapsed_s": el,
        "zoom_peaks": [{"out_t": z["out_t"] + z["hold"] / 2, "x": z["x"], "y": z["y"], "scale": z["scale"]}
                       for z in plan.get("zooms") or []],
        "joins": joins,
    })


if __name__ == "__main__":
    main()
