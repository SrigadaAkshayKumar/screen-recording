"""Validate work/actions.json and work/plan.json against the pipeline rules.

    python tools/check.py --project projects/demo [--actions] [--plan]

Exit 1 when there are errors. Also a library: render.py and plan_builder.py import the
segment mapping and the validators from here so every stage enforces the same rules.
"""
from __future__ import annotations

import sys

from common import Project, parser

SPEED_MIN, SPEED_MAX, WAIT_MAX = 0.75, 4.0, 8.0
# Tutorial pacing (client rule, docs/lessons.md 2026-10-12): hard limits above, comfortable ones here.
PACE_MAX, PACE_WAIT_MAX, PACE_MIN_SEG, PACE_MAX_HOLD, PACE_MAX_END_HOLD = 2.0, 3.0, 0.5, 1.5, 3.0
ZOOM_MIN, ZOOM_MAX = 1.4, 2.2
CLICK_TOL = 0.15
EPS = 0.002
KINDS = {"click", "drag", "type", "scroll", "wait"}


# ---------------------------------------------------------------- segment mapping

def speed(seg: dict) -> float:
    d = seg["out_end"] - seg["out_start"]
    return (seg["src_end"] - seg["src_start"]) / d if d > 0 else 0.0


def out_to_src(segs: list[dict], t: float) -> tuple[float, int]:
    """Output time -> (source time, segment index)."""
    i = 0
    lo, hi = 0, len(segs) - 1
    while lo <= hi:                       # last segment with out_start <= t
        mid = (lo + hi) // 2
        if segs[mid]["out_start"] <= t + 1e-9:
            i, lo = mid, mid + 1
        else:
            hi = mid - 1
    s = segs[i]
    if s["mode"] == "hold":
        return s["src_start"], i
    u = min(max(t - s["out_start"], 0.0), s["out_end"] - s["out_start"])
    return s["src_start"] + u * speed(s), i


def src_to_outs(segs: list[dict], t: float) -> list[float]:
    """Source time -> every output time that shows it (one per continuous run of segments).

    A plan may jump back in the source to follow the narration order, so the same source
    moment can be on screen more than once."""
    outs, run, prev = [], [], None

    def close(run):
        hit = next((o for o in run if o[0] == "hit"), None) or next((o for o in run if o[0] == "end"), None)
        if hit:
            outs.append(hit[1])

    for k, s in enumerate(segs):
        if prev is not None and abs(s["src_start"] - prev["src_end"]) > 1e-3:
            close(run)
            run = []
        if s["mode"] == "hold":
            if abs(t - s["src_start"]) <= 1e-3:
                run.append(("hit", s["out_start"]))
        else:
            last = k == len(segs) - 1
            if s["src_start"] - 1e-6 <= t < s["src_end"] or (last and abs(t - s["src_end"]) < 1e-3):
                run.append(("hit", s["out_start"] + (t - s["src_start"]) / speed(s)))
            elif abs(t - s["src_end"]) <= 1e-3:           # on the end of a segment, a cut right after it
                run.append(("end", s["out_end"]))
        prev = s
    close(run)
    return sorted(outs)


def src_to_out(segs: list[dict], t: float, near: float | None = None) -> float | None:
    """Source time -> the output time that shows it (the earliest, or the one closest to
    `near`), or None when it was cut."""
    outs = src_to_outs(segs, t)
    if not outs:
        return None
    return outs[0] if near is None else min(outs, key=lambda o: abs(o - near))


def zoom_window(z: dict) -> tuple[float, float]:
    return z["out_t"] - z["in"], z["out_t"] + z["hold"] + z["out"]


# ---------------------------------------------------------------- validators

def validate_actions(doc: dict, probe: dict, clicks_rec: dict | None = None):
    err, wrn = [], []
    rec = probe["recording"]
    W, H, D = rec["width"], rec["height"], rec["duration"]
    acts = doc.get("actions")
    if not isinstance(acts, list) or not acts:
        return ["actions.json needs a non-empty 'actions' list"], wrn
    seen = set()
    last_t = -1.0
    for a in acts:
        aid = a.get("id", "?")
        if aid in seen:
            err.append(f"{aid}: duplicate id")
        seen.add(aid)
        for f in ("t_click", "x", "y", "kind", "target", "result"):
            if a.get(f) is None:
                err.append(f"{aid}: missing '{f}'")
        if a.get("kind") not in KINDS:
            err.append(f"{aid}: kind must be one of {sorted(KINDS)}")
        t = a.get("t_click")
        if isinstance(t, (int, float)):
            if not 0 <= t <= D:
                err.append(f"{aid}: t_click {t} outside the recording (0-{D:.3f})")
            if t < last_t:
                wrn.append(f"{aid}: actions are not sorted by t_click")
            last_t = t
            tr = a.get("t_result_visible")
            if tr is not None and tr < t - EPS:
                err.append(f"{aid}: t_result_visible {tr} is before t_click {t}")
        for fx, fy in (("x", "y"), ("x2", "y2")):
            if a.get(fx) is not None and not (0 <= a[fx] < W and 0 <= a.get(fy, -1) < H):
                err.append(f"{aid}: ({fx},{fy}) = ({a.get(fx)},{a.get(fy)}) outside {W}x{H}")
        if a.get("kind") == "drag" and any(a.get(f) is None for f in ("x2", "y2", "t_end")):
            err.append(f"{aid}: drag needs x2, y2 and t_end")
        if clicks_rec and a.get("kind") in ("click", "drag") and isinstance(t, (int, float)):
            near = [c for c in clicks_rec.get("clicks", []) if abs(c["t"] - t) <= 0.1]
            if not near:
                wrn.append(f"{aid}: no logged click within 0.1 s of t_click {t:.3f} (clicks.json is the truth)")
            elif min(abs(c["x"] - a["x"]) + abs(c["y"] - a["y"]) for c in near) > 30:
                wrn.append(f"{aid}: position differs from the logged click by >30 px")
    for j in doc.get("junk", []) or []:
        if not (0 <= j.get("start", -1) < j.get("end", -1) <= D + EPS):
            err.append(f"junk {j}: needs 0 <= start < end <= {D:.3f}")
    return err, wrn


def validate_plan(plan: dict, probe: dict, actions: dict | None = None, lines: list | None = None):
    err, wrn = [], []
    rec, vo = probe["recording"], probe["voiceover"]
    o = plan.get("output") or {}
    for f in ("duration", "fps", "width", "height"):
        if not o.get(f):
            err.append(f"output.{f} is missing")
    if err:
        return err, wrn
    D = o["duration"]
    if abs(D - vo["duration"]) > 0.1:
        err.append(f"output.duration {D} differs from the voiceover ({vo['duration']:.3f}) by more than 0.1 s")
    if (o["width"], o["height"]) != (rec["width"], rec["height"]):
        err.append(f"output size {o['width']}x{o['height']} must match the recording {rec['width']}x{rec['height']}")

    segs = plan.get("segments") or []
    if not segs:
        return err + ["no segments"], wrn
    if abs(segs[0]["out_start"]) > EPS:
        err.append(f"first segment starts at {segs[0]['out_start']}, not 0")
    if abs(segs[-1]["out_end"] - D) > EPS:
        err.append(f"last segment ends at {segs[-1]['out_end']}, output.duration is {D}")
    prev = None
    for i, s in enumerate(segs):
        tag = f"segment {i} (out {s.get('out_start')}-{s.get('out_end')})"
        if any(not isinstance(s.get(f), (int, float)) for f in ("src_start", "src_end", "out_start", "out_end")):
            err.append(f"{tag}: needs numeric src_start, src_end, out_start, out_end")
            continue
        if s["out_end"] <= s["out_start"]:
            err.append(f"{tag}: out_end must be after out_start")
        if s["src_start"] < -EPS or s["src_end"] > rec["duration"] + 0.05:
            err.append(f"{tag}: src range {s['src_start']}-{s['src_end']} outside the recording")
        if s.get("mode") == "hold":
            if abs(s["src_end"] - s["src_start"]) > 1e-3:
                err.append(f"{tag}: hold needs src_start == src_end")
        elif s.get("mode") == "speed":
            sp = speed(s)
            limit = WAIT_MAX if s.get("wait") else SPEED_MAX
            if sp < SPEED_MIN - 0.005:
                err.append(f"{tag}: speed {sp:.2f}x below {SPEED_MIN}x - hold the last frame instead")
            elif sp > limit + 0.005:
                why = "" if s.get("wait") else " (mark waits with \"wait\": true for up to 8x, or cut)"
                err.append(f"{tag}: speed {sp:.2f}x above {limit}x{why}")
        else:
            err.append(f"{tag}: mode must be 'speed' or 'hold'")
        dur = s["out_end"] - s["out_start"]
        if s.get("mode") == "hold":
            cap = PACE_MAX_END_HOLD if i == len(segs) - 1 else PACE_MAX_HOLD
            if dur > cap + EPS:
                wrn.append(f"{tag}: pace: {dur:.1f}s hold looks frozen (max {cap:g}s) - play nearby footage slower")
        elif s.get("mode") == "speed":
            sp, cap = speed(s), (PACE_WAIT_MAX if s.get("wait") else PACE_MAX)
            if sp > cap + 0.005:
                wrn.append(f"{tag}: pace: {sp:.2f}x is hard to follow (aim <= {cap:g}x) - give it more time or cut dead time")
        # A short piece only looks choppy when it stands alone: after a cut, or at a different speed
        # than both neighbours. Same-speed continuous pieces (anchor splits) play as one move.
        if dur < PACE_MIN_SEG - EPS and 0 < i < len(segs) - 1 and s.get("mode") == "speed":
            def same(a):
                return a.get("mode") == "speed" and abs(speed(a) - speed(s)) <= 0.25 * max(speed(s), 1e-6)
            nxt = segs[i + 1]
            joined = (same(prev) and not s.get("xfade")) or (same(nxt) and not nxt.get("xfade"))
            if not joined:
                wrn.append(f"{tag}: pace: {dur:.2f}s piece looks choppy (min {PACE_MIN_SEG:g}s) - merge it with its neighbour")
        if prev:
            if abs(s["out_start"] - prev["out_end"]) > EPS:
                err.append(f"{tag}: gap/overlap with the previous segment ({prev['out_end']} -> {s['out_start']})")
            if s["src_start"] < prev["src_end"] - EPS and not s.get("xfade"):
                wrn.append(f"{tag}: source jumps back ({prev['src_end']} -> {s['src_start']}) without a cross-fade")
            if s.get("xfade") and abs(s["src_start"] - prev["src_end"]) <= EPS:
                wrn.append(f"{tag}: xfade on a continuous join has no effect")
        prev = s

    W, H = rec["width"], rec["height"]
    zs = sorted(plan.get("zooms") or [], key=lambda z: z.get("out_t", 0))
    for i, z in enumerate(zs):
        tag = f"zoom at {z.get('out_t')}"
        if any(not isinstance(z.get(f), (int, float)) for f in ("out_t", "x", "y", "scale", "in", "hold", "out")):
            err.append(f"{tag}: needs out_t, x, y, scale, in, hold, out")
            continue
        if not ZOOM_MIN - 1e-6 <= z["scale"] <= ZOOM_MAX + 1e-6:
            err.append(f"{tag}: scale {z['scale']} outside {ZOOM_MIN}-{ZOOM_MAX}")
        if not (0 <= z["x"] <= W and 0 <= z["y"] <= H):
            err.append(f"{tag}: target ({z['x']},{z['y']}) outside the frame")
        if min(z["in"], z["out"]) <= 0 or z["hold"] < 0:
            err.append(f"{tag}: in/out must be > 0 and hold >= 0")
        a, b = zoom_window(z)
        if a < -EPS or b > D + 0.5:
            wrn.append(f"{tag}: zoom window {a:.2f}-{b:.2f} runs outside the output")
        if i and a < zoom_window(zs[i - 1])[1] - EPS:
            wrn.append(f"{tag}: overlaps the previous zoom - render blends them with no zoom-out between")
    for r in plan.get("ripples") or []:
        if not (0 <= r.get("x", -1) <= W and 0 <= r.get("y", -1) <= H and 0 <= r.get("out_t", -1) <= D):
            err.append(f"ripple {r}: outside the frame or the output time")

    if actions and not err:
        acts = {a["id"]: a for a in actions.get("actions", [])}
        line_by_id = {ln["id"]: ln for ln in lines or []}
        synced = set()
        for s in plan.get("sync") or []:
            a = acts.get(s.get("action"))
            if not a:
                err.append(f"sync entry {s}: unknown action")
                continue
            synced.add(a["id"])
            t_out = src_to_out(segs, a["t_click"], near=s.get("word_t"))
            if t_out is None:
                err.append(f"{a['id']}: its click (src {a['t_click']}) is cut out of the plan")
                continue
            if s.get("word_t") is not None and abs(t_out - s["word_t"]) > CLICK_TOL:
                err.append(f"{a['id']}: click lands at {t_out:.3f}, word '{s.get('word')}' at "
                           f"{s['word_t']:.3f} (off by {t_out - s['word_t']:+.3f}s, limit ±{CLICK_TOL})")
            ln = line_by_id.get(s.get("line"))
            tr = a.get("t_result_visible")
            if ln and tr is not None:
                r_out = next((o for o in src_to_outs(segs, tr) if o >= t_out - EPS), None)
                if r_out is None:
                    wrn.append(f"{a['id']}: its result (src {tr}) is cut out")
                elif r_out > ln["end"] + 0.25:
                    wrn.append(f"{a['id']}: result appears at {r_out:.2f}s, after line {ln['id']} ends ({ln['end']:.2f}s)")
        for aid, a in acts.items():
            if a.get("kind") != "wait" and aid not in synced:
                wrn.append(f"{aid}: not tied to a narration word in plan.sync")
    return err, wrn


def report(name: str, err: list[str], wrn: list[str]) -> bool:
    for m in wrn:
        print(f"  warning: {m}")
    for m in err:
        print(f"  ERROR: {m}")
    print(f"{name}: {'OK' if not err else f'{len(err)} error(s)'}"
          f"{f', {len(wrn)} warning(s)' if wrn else ''}")
    return not err


def main():
    ap = parser(__doc__)
    ap.add_argument("--actions", action="store_true")
    ap.add_argument("--plan", action="store_true")
    a = ap.parse_args()
    pr = Project(a.project)
    both = not (a.actions or a.plan)
    probe = pr.need("probe.json", "tools/probe.py")
    ok = True
    actions = None
    if a.actions or both:
        actions = pr.need("actions.json", "the screencast-analyze skill")
        ok &= report("actions.json", *validate_actions(actions, probe, pr.maybe("clicks_rec.json")))
    if a.plan or both:
        plan = pr.need("plan.json", "the screencast-sync skill")
        actions = actions or pr.maybe("actions.json")
        ok &= report("plan.json", *validate_plan(plan, probe, actions, pr.maybe("lines.json")))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
