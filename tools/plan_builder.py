"""Turn the screencast-sync skill's decisions (work/sync.json) into work/plan.json.

The skill decides WHICH word each action lands on, which actions get a zoom, and what to cut.
This tool does the arithmetic: segments that put every click on its word, speeds within
0.75-4x (still spans up to 8x), holds where the source runs short, zoom timing, ripples.
It also writes the table part of work/sync-notes.md and validates the result.

work/sync.json:
{
  "anchors": [{"action": "A1", "line": 2, "word": "Upload"},            # first "Upload" in line 2
              {"action": "A2", "line": 3, "word": "Open", "occurrence": 2},
              {"action": "A3", "word_index": 57, "lead": 0.05},          # index into words.json
              {"action": "A4", "out_t": 31.2},                           # explicit output time
              {"action": "A7", "line": 7, "word": "videos", "src_from": 112.0, "prev_until": 90.2}],
                # narration order wins: A7 is clicked earlier in the recording than the anchor before
                # it, so after the previous action's footage (until src 90.2) the plan cross-fades to
                # src 112.0 and plays up to A7's click. A backward jump without these gets
                # src_from = click - 1.5 s and prev_until = previous result + 1 s.
  "zooms": [{"actions": ["A1"], "scale": 1.8}, {"actions": ["A3", "A4"]},
            {"actions": ["A6"], "include": [[1500, 400]]}],                # also frame where the result appears
  "no_ripple": ["A5"],
  "cuts": [{"src_start": 40.0, "src_end": 52.5, "reason": "upload wait", "xfade": true},
           {"src_start": 61.0, "src_end": 66.0, "reason": "idle", "ff": true}],
                                 # ff: in-scene dead time - kept and fast-forwarded with its interval when
                                 # that plays at <= ff_max (default 2x), cut only when it doesn't fit.
                                 # actions.json junk takes "ff" too.
  "ff_max": 2.0,
  "use_junk": true,              # also cut actions.json junk spans (default true)
  "hold_at": {"A2": "before_click"},   # where the slack before A2 is held; default: --settle s after
                                       # the previous action's t_result_visible; or a source time
  "src_start": null, "src_end": null,  # trim the recording's head/tail
  "style": {"ripple_color": "#2F80ED"}
}
"""
from __future__ import annotations

import hashlib
import json
import sys

from align_script import norm
from check import (SPEED_MAX, SPEED_MIN, WAIT_MAX, ZOOM_MAX, ZOOM_MIN, report, speed, src_to_out,
                   src_to_outs, validate_plan)
from common import Project, _round, die, parser, write_json

MIN_PIECE = 0.02


def plan_hash(plan: dict) -> str:
    body = {k: v for k, v in plan.items() if k != "generated_hash"}
    return hashlib.sha1(json.dumps(_round(body), sort_keys=True).encode()).hexdigest()[:12]


def subtract(a: float, b: float, cuts: list[tuple[float, float, bool]]):
    """Kept source pieces of [a, b] after removing cuts -> [(start, end, xfade_at_start)]."""
    pieces, cur, xf = [], a, False
    for c0, c1, cx in cuts:
        if c1 <= cur or c0 >= b:
            continue
        if c0 > cur:
            pieces.append((cur, c0, xf))
        cur, xf = max(cur, c1), cx
    if b > cur:
        pieces.append((cur, b, xf))
    return [p for p in pieces if p[1] - p[0] >= MIN_PIECE]


def split_stills(pieces, stills):
    """Tag the parts of each piece that fall inside a still span."""
    out = []
    for a, b, xf in pieces:
        cur = a
        for s0, s1 in stills:
            if s1 <= cur or s0 >= b:
                continue
            if s0 > cur:
                out.append([cur, s0, False, xf]); xf = False
            out.append([max(cur, s0), min(b, s1), True, xf]); xf = False
            cur = min(b, s1)
        if b > cur:
            out.append([cur, b, False, xf])
    return [p for p in out if p[1] - p[0] >= MIN_PIECE / 2]


def fit(pieces, T: float, hold_at: float | None, hold_first: bool = False, vmax: float = SPEED_MAX * 0.99):
    """Lay pieces [[a, b, still, xfade]] into T output seconds -> [(seg dict w/o out times, dur)].
    Pieces are in play order; the source may jump back between them (narration order).
    vmax caps the speed of non-still footage (still spans may still go up to 8x)."""
    L = sum(p[1] - p[0] for p in pieces)
    if T <= 1e-6:
        return [] if L < 0.05 else None
    if L < 1e-6:
        h = hold_at if hold_at is not None else 0.0
        return [({"mode": "hold", "src_start": h, "src_end": h}, T)]
    u = L / T
    Ls = sum(p[1] - p[0] for p in pieces if p[2])
    La = L - Ls
    v_a = v_s = u
    hold = 0.0
    if u < SPEED_MIN:
        v_a = v_s = 1.0
        hold = T - L
    elif Ls > 0 and u > 1.25:
        if La < 1e-6:
            v_s = u
        else:
            v_s = WAIT_MAX * 0.99                    # margin so 3-decimal rounding stays under the limit
            rem = T - Ls / v_s
            if rem <= 0:
                return None
            v_a = La / rem
            if v_a < 1.0:
                v_a = 1.0
                v_s = Ls / (T - La)
        if v_a > vmax or v_s > WAIT_MAX * 0.99 + 1e-9:
            return None
    elif u > vmax:
        if not (La < 1e-6 and u <= WAIT_MAX * 0.99):
            return None
    segs = []
    for a, b, still, xf in pieces:
        v = v_s if still else v_a
        seg = {"mode": "speed", "src_start": a, "src_end": b}
        if xf:
            seg["xfade"] = True
        if still and v > SPEED_MAX:
            seg["wait"] = True
        segs.append((seg, (b - a) / v))
    if hold > 1e-6:
        if hold_first or hold_at is None:
            h = pieces[0][0]
            k = 0
        else:
            h = hold_at
            k = None
            for i, (s, d) in enumerate(segs):
                if s["src_start"] <= h <= s["src_end"]:
                    if i == 0 and h - s["src_start"] < 1e-6:
                        k = 0
                    elif s["src_end"] - h < MIN_PIECE:       # only ever snap forward: never
                        h, k = s["src_end"], i + 1          # hold a frame from before the result
                    else:
                        h = max(h, s["src_start"] + MIN_PIECE)
                        v = (s["src_end"] - s["src_start"]) / d
                        first = dict(s, src_end=h)
                        second = {k2: v2 for k2, v2 in s.items() if k2 not in ("xfade",)}
                        second["src_start"] = h
                        segs[i:i + 1] = [(first, (h - s["src_start"]) / v), (second, (s["src_end"] - h) / v)]
                        k = i + 1
                    break
            if k is None:                                # h fell in a cut: hold where footage resumes
                k = len(segs)
                for i, (s, _) in enumerate(segs):
                    before = segs[i - 1][0]["src_end"] if i else float("-inf")
                    if before <= h <= s["src_start"]:
                        k = i
                        break
                h = segs[k][0]["src_start"] if k < len(segs) else segs[-1][0]["src_end"]
        segs.insert(k, ({"mode": "hold", "src_start": h, "src_end": h}, hold))
    return segs


def resolve_anchor(an: dict, acts: dict, lines: list, words: list) -> tuple[dict, float, dict]:
    aid = an.get("action")
    if aid not in acts:
        die(f"sync.json anchor {an}: unknown action {aid!r}")
    act = acts[aid]
    lead = float(an.get("lead", 0.0))
    meta = {"action": aid, "line": an.get("line"), "word": an.get("word")}
    if an.get("out_t") is not None:
        return act, float(an["out_t"]), dict(meta, word_t=float(an["out_t"]))
    if an.get("word_index") is not None:
        i = int(an["word_index"])
        if not 0 <= i < len(words):
            die(f"anchor {aid}: word_index {i} out of range")
        w = words[i]
        line = next((ln["id"] for ln in lines if ln["word_range"] and ln["word_range"][0] <= i <= ln["word_range"][1]), None)
        return act, w["start"] + lead, dict(meta, word=w["word"], word_index=i, line=meta["line"] or line,
                                              word_t=w["start"])
    if an.get("line") is None or not an.get("word"):
        die(f"anchor {aid}: give out_t, word_index, or line + word")
    ln = next((l for l in lines if l["id"] == an["line"]), None)
    if not ln:
        die(f"anchor {aid}: no line {an['line']} in lines.json")
    target = norm(an["word"].split()[0])
    hits = [w for w in ln["words"] if norm(w["word"]) == target]
    occ = int(an.get("occurrence", 1))
    if len(hits) < occ:
        said = " ".join(w["word"] for w in ln["words"])
        die(f"anchor {aid}: word {an['word']!r} (occurrence {occ}) not found in line {ln['id']}: \"{said}\"")
    w = hits[occ - 1]
    return act, w["start"] + lead, dict(meta, word=w["word"], word_index=w["i"], word_t=w["start"])


def main():
    ap = parser(__doc__)
    ap.add_argument("--zoom-in", type=float, default=0.45)
    ap.add_argument("--zoom-out", type=float, default=0.5)
    ap.add_argument("--zoom-hold", type=float, default=0.8, help="minimum hold at full zoom")
    ap.add_argument("--force", action="store_true", help="overwrite a hand-edited plan.json (kept as plan.hand.json)")
    ap.add_argument("--settle", type=float, default=0.15, help="hold this long after t_result_visible")
    ap.add_argument("--merge-gap", type=float, default=1.2, help="merge zoomed clicks closer than this")
    ap.add_argument("--ff-max", type=float, default=2.0,
                    help="fast-forward an \"ff\" cut instead of cutting it if its interval then plays at or below this")
    a = ap.parse_args()
    pr = Project(a.project)
    probe = pr.need("probe.json", "tools/probe.py")
    actions = pr.need("actions.json", "the screencast-analyze skill")
    lines = pr.need("lines.json", "tools/align_script.py")
    words = pr.need("words.json", "tools/transcribe.py")
    sync = pr.need("sync.json", "the screencast-sync skill")
    scenes = pr.maybe("scenes.json") or {"stills": []}
    old_plan = pr.maybe("plan.json")
    if old_plan and old_plan.get("generated_hash") != plan_hash(old_plan):
        if not a.force:
            die("work/plan.json was edited by hand since plan_builder wrote it. Move those edits into "
                "sync.json, or pass --force (the edited file is kept as work/plan.hand.json)", 1)
        write_json(pr.w("plan.hand.json"), old_plan)
    rec, vo = probe["recording"], probe["voiceover"]
    W, H, RD, D = rec["width"], rec["height"], rec["duration"], vo["duration"]
    acts = {x["id"]: x for x in actions["actions"]}
    notes: list[str] = []

    # ---- cuts
    cuts = [(float(c["src_start"]), float(c["src_end"]), bool(c.get("xfade", True)), c.get("reason", ""),
             bool(c.get("ff", False))) for c in sync.get("cuts", [])]
    if sync.get("use_junk", True):
        cuts += [(float(j["start"]), float(j["end"]), True, "junk: " + j.get("reason", ""), bool(j.get("ff", False)))
                 for j in actions.get("junk", []) or []]
    s_lo = float(sync.get("src_start") or 0.0)
    s_hi = float(sync.get("src_end") or RD)
    ff_max = min(float(sync.get("ff_max") or a.ff_max), SPEED_MAX * 0.99)
    cuts = sorted((max(0.0, c0), min(RD, c1), xf, r, ff) for c0, c1, xf, r, ff in cuts if c1 > c0)
    merged: list[list] = []
    for c in cuts:
        if merged and c[0] <= merged[-1][1] + 0.05:
            merged[-1][1] = max(merged[-1][1], c[1])
            merged[-1][4] = merged[-1][4] and c[4]   # touching a hard cut makes the whole span hard
            merged[-1][3] += "; " + c[3]
        else:
            merged.append(list(c))
    cuts3 = [(c0, c1, xf) for c0, c1, xf, _, _ in merged]
    # ff spans: in-scene dead time that is fast-forwarded (kept) when its interval fits at <= ff_max
    soft = {(c0, c1, xf): r for c0, c1, xf, r, ff in merged if ff}

    # ---- anchors
    anchors = []
    for an in sync.get("anchors", []):
        act, out_t, meta = resolve_anchor(an, acts, lines, words)
        c = act["t_click"]
        if any(c0 < c < c1 for c0, c1, _ in cuts3):
            die(f"{act['id']} (src {c:.3f}) lies inside a cut - shrink the cut or drop the anchor")
        anchors.append((c, out_t, act, meta, an))
    if not anchors:
        die("sync.json has no anchors")
    anchors.sort(key=lambda x: x[1])                 # narration order; the source may jump back
    for (c1, o1, a1, *_), (c2, o2, a2, *_) in zip(anchors, anchors[1:]):
        if o2 <= o1 + 0.05:
            die(f"{a1['id']} and {a2['id']} land on the same moment (out {o1:.2f} / {o2:.2f}): "
                f"anchor one of them to another word")
    if anchors[0][1] < 0 or anchors[-1][1] > D:
        die("an anchor lies outside the voiceover")

    stills = [(s["start"], s["end"]) for s in scenes.get("stills", [])]
    # wait actions (progress bars) fast-forward like still spans, up to 8x
    stills += [(x["t_click"], x["t_result_visible"]) for x in actions["actions"]
               if x["kind"] == "wait" and x.get("t_result_visible") is not None]
    stills.sort()
    merged_st: list[list[float]] = []
    for s0, s1 in stills:
        if merged_st and s0 <= merged_st[-1][1]:
            merged_st[-1][1] = max(merged_st[-1][1], s1)
        else:
            merged_st.append([s0, s1])
    stills = [tuple(s) for s in merged_st]
    hold_at = sync.get("hold_at", {}) or {}
    plan_segs: list[tuple[dict, float]] = []
    approach: dict[str, str] = {}

    kept_ff: set = set()

    def pieces_of(parts):
        out = []
        cutset = [c for c in cuts3 if c not in kept_ff]
        for p0, p1, jump in parts:
            ps = split_stills(subtract(p0, p1, cutset), stills)
            if jump and ps:
                ps[0][3] = True                          # cross-fade into the jump
            out += ps
        return out

    def lay(parts, T, h, hold_first, label, aid=None, outro=False):
        src_a, src_b = parts[0][0], parts[-1][1]
        kept_ff.clear()
        if not outro:                                    # fast-forward ff spans instead of cutting them,
            here = [c for c in cuts3 if c in soft and any(c[0] < p1 and c[1] > p0 for p0, p1, _ in parts)]
            for c in sorted(here, key=lambda c: c[1] - c[0]):   # shortest first: fewest cuts left
                kept_ff.add(c)
                if fit(pieces_of(parts), T, h, hold_first, ff_max) is None:
                    kept_ff.discard(c)
            for c in sorted(kept_ff):
                notes.append(f"{label}: fast-forwarded src {c[0]:.2f}-{c[1]:.2f} instead of cutting it ({soft[c]})")
            for c in sorted(set(here) - kept_ff):
                notes.append(f"{label}: cut src {c[0]:.2f}-{c[1]:.2f} - too long to fast-forward at "
                             f"<= {ff_max:.2f}x ({soft[c]})")
        pieces = pieces_of(parts)
        if outro:
            L = sum(p[1] - p[0] for p in pieces)
            if L >= T:                                   # plenty of footage: play 1x, stop at the end
                keep, acc = [], 0.0
                for p in pieces:
                    take = min(p[1] - p[0], T - acc)
                    if take > MIN_PIECE / 2:
                        keep.append([p[0], p[0] + take, False, p[3]])
                    acc += take
                pieces = keep
                h = None
            else:
                h = pieces[-1][1] if pieces else src_a
            res = fit([[p[0], p[1], False, p[3]] for p in pieces], T, h, False)
        else:
            res = fit(pieces, T, h, hold_first)
        if res is None and label == "intro":
            L_need = 1.5 * T                             # trim the head: last 1.5*T s before the first click
            acc, keep = 0.0, []
            for p in reversed(pieces):
                take = min(p[1] - p[0], L_need - acc)
                keep.insert(0, [p[1] - take, p[1], False, p[3]])
                acc += take
                if acc >= L_need - 1e-6:
                    break
            notes.append(f"intro: source before the first click was too long; started at src {keep[0][0]:.2f}s")
            res = fit(keep, T, None, True)
        while res is None:
            cand = [(p[1] - p[0], p) for p in pieces if p[2] and p[1] - p[0] > 1.2]
            if not cand:
                act_len = sum(p[1] - p[0] for p in pieces)
                die(f"{label}: {act_len:.2f}s of source must fit in {T:.2f}s of narration (> {SPEED_MAX:g}x) "
                    f"and there is no still span left to cut. Add a cut to sync.json (src {src_a:.2f}-{src_b:.2f}), "
                    f"set src_from/prev_until on the anchor "
                    f"or move an anchor to a later word.")
            _, p = max(cand, key=lambda x: x[0])
            c0, c1 = p[0] + 0.4, p[1] - 0.4
            notes.append(f"{label}: auto-cut still span src {c0:.2f}-{c1:.2f} with a cross-fade")
            cuts3.append((c0, c1, True)); cuts3.sort()
            pieces = pieces_of(parts)
            res = fit(pieces, T, h, hold_first)
        if aid:
            L = sum(p[1] - p[0] for p in pieces)
            hold = sum(d for s, d in res if s["mode"] == "hold")
            approach[aid] = f"{(L / (T - hold)) if T - hold > 1e-6 else 0:.2f}x" + (f" +{hold:.1f}s hold" if hold > 0.05 else "")
        plan_segs.extend(res)

    c1, o1, act1, *_ = anchors[0]
    lay([(s_lo, c1, False)], o1, s_lo, True, "intro", act1["id"])
    for (ca, oa, acta, _, ana), (cb, ob, actb, _, anb) in zip(anchors, anchors[1:]):
        tr = acta.get("t_result_visible")
        jump = anb.get("src_from")
        if cb < ca and jump is None:
            jump = cb - 1.5
        if jump is not None:                         # play A's result, then cross-fade to B's approach
            jump = min(max(float(jump), s_lo), cb)
            until = max(float(anb.get("prev_until", (tr if tr is not None else ca) + 1.0)), ca)
            if jump >= ca:
                until = min(until, jump)
            parts = [(ca, until, False), (jump, cb, True)]
            notes.append(f"{actb['id']}: after {acta['id']} (until src {until:.2f}) jumps "
                         f"{'back' if jump < until else 'ahead'} to src {jump:.2f} - narration order")
        else:
            until, parts = cb, [(ca, cb, False)]
        mode = hold_at.get(actb["id"], "after_result")
        if isinstance(mode, (int, float)):
            h = float(mode)
        elif mode == "before_click":
            h = cb
        elif tr is not None:                         # a beat after the result, once the UI settles
            h = min(tr + a.settle, (until if jump is not None else cb) - 0.05)
        else:
            h = ca
        lay(parts, ob - oa, h, False, f"{acta['id']}->{actb['id']}", actb["id"])
    cl, ol, actl, *_ = anchors[-1]
    lay([(cl, max(cl, s_hi), False)], D - ol, None, False, "outro", outro=True)

    # ---- absolute out times; merge continuous equal-speed neighbours
    segs: list[dict] = []
    t = 0.0
    for s, d in plan_segs:
        if d <= 1e-6:
            continue
        seg = dict(s, out_start=t, out_end=t + d)
        t += d
        if segs:
            p = segs[-1]
            if (p["mode"] == seg["mode"] == "speed" and not seg.get("xfade")
                    and abs(p["src_end"] - seg["src_start"]) < 1e-6
                    and abs(speed(p) - speed(seg)) < 1e-3 and p.get("wait") == seg.get("wait")):
                p["src_end"], p["out_end"] = seg["src_end"], seg["out_end"]
                continue
            if p["mode"] == seg["mode"] == "hold" and abs(p["src_start"] - seg["src_start"]) < 1e-6:
                p["out_end"] = seg["out_end"]
                continue
        segs.append(seg)
    # round on shared boundaries so segments stay contiguous
    bounds = [0.0] + [round(s["out_end"], 3) for s in segs]
    bounds[-1] = round(D, 3)
    for s, b0, b1 in zip(segs, bounds, bounds[1:]):
        s.update(out_start=b0, out_end=b1, src_start=round(s["src_start"], 3), src_end=round(s["src_end"], 3))
    segs = [s for s in segs if s["out_end"] > s["out_start"]]
    for s in segs:
        if s["mode"] == "hold":
            s["src_end"] = s["src_start"]

    # ---- ripples
    anchor_out = {act["id"]: o for _, o, act, *_ in anchors}

    def click_out(aid):
        return src_to_out(segs, acts[aid]["t_click"], near=anchor_out.get(aid))

    no_rip = set(sync.get("no_ripple", []) or [])
    ripples = []
    for act in actions["actions"]:
        if act["kind"] in ("click", "drag") and act["id"] not in no_rip:
            for ot in src_to_outs(segs, act["t_click"]):   # every time the click is on screen
                ripples.append({"out_t": ot, "x": act["x"], "y": act["y"], "action": act["id"]})
    ripples.sort(key=lambda r: r["out_t"])

    # ---- zooms
    margin = 120 * W / 1920
    groups = []
    for z in sync.get("zooms", []) or []:
        ids = [i for i in z.get("actions", []) if i in acts]
        if len(ids) != len(z.get("actions", [])):
            die(f"zoom {z}: unknown action id")
        groups.append({"ids": ids, "scale": z.get("scale"), "include": z.get("include") or []})

    def times(g):
        outs, res = [], []
        for i in g["ids"]:
            ot = click_out(i)
            if ot is None:
                continue
            outs.append(ot)
            tr = acts[i].get("t_result_visible")
            rt = next((o for o in src_to_outs(segs, tr) if o >= ot - 1e-3), None) if tr is not None else None
            res.append(rt if rt is not None else ot)
        return outs, res

    groups = [g for g in groups if times(g)[0]]
    groups.sort(key=lambda g: min(times(g)[0]))
    i = 0
    while i + 1 < len(groups):                       # rule: zoomed clicks < merge-gap apart share a zoom
        if min(times(groups[i + 1])[0]) - max(times(groups[i])[0]) < a.merge_gap:
            notes.append(f"zooms {groups[i]['ids']} and {groups[i + 1]['ids']} merged (clicks < {a.merge_gap}s apart)")
            sc = [s for s in (groups[i]["scale"], groups[i + 1]["scale"]) if s]
            groups[i] = {"ids": groups[i]["ids"] + groups[i + 1]["ids"], "scale": min(sc) if sc else None,
                         "include": groups[i]["include"] + groups[i + 1]["include"]}
            del groups[i + 1]
        else:
            i += 1
    zooms = []
    for g in groups:
        pts = []
        for i in g["ids"]:
            pts.append((acts[i]["x"], acts[i]["y"]))
            if acts[i].get("x2") is not None:
                pts.append((acts[i]["x2"], acts[i]["y2"]))
        pts += [(float(p[0]), float(p[1])) for p in g["include"]]
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        bw, bh = max(xs) - min(xs), max(ys) - min(ys)
        fit_s = min(W / (bw + 2 * margin), H / (bh + 2 * margin))
        s = min(float(g["scale"] or 1.8), fit_s, ZOOM_MAX)
        if s < ZOOM_MIN:
            notes.append(f"zoom {g['ids']} skipped: targets too far apart to frame at {ZOOM_MIN}x")
            continue
        outs, res = times(g)
        t0, t_end = min(outs), max(max(outs), max(res))
        zin = min(a.zoom_in, max(0.15, t0))
        hold = max(a.zoom_hold, t_end + 0.4 - t0)
        zooms.append({"out_t": t0, "x": (min(xs) + max(xs)) / 2, "y": (min(ys) + max(ys)) / 2, "scale": round(s, 2),
                      "in": zin, "hold": hold, "out": a.zoom_out, "actions": g["ids"]})
    for z, nz in zip(zooms, zooms[1:]):              # zoom out between steps where there is room
        start_next = nz["out_t"] - nz["in"]
        if z["out_t"] + z["hold"] + z["out"] > start_next:
            z["hold"] = max(0.3, start_next - z["out"] - z["out_t"])
            if z["out_t"] + z["hold"] + z["out"] > start_next:
                z["out"] = max(0.35, start_next - z["out_t"] - z["hold"])
            if z["out_t"] + z["hold"] + z["out"] > start_next + 1e-3:
                notes.append(f"zooms at {z['out_t']:.2f}s and {nz['out_t']:.2f}s overlap; render blends them")
    for z in zooms:
        if z["out_t"] + z["hold"] + z["out"] > D:
            z["hold"] = max(0.0, D - z["out"] - z["out_t"])

    first_out = anchors[0][1]
    intro = {"mode": "hold" if segs[0]["mode"] == "hold" else "play", "until": first_out} if first_out > 0.3 else None
    tail = segs[-1]
    outro = {"mode": tail["mode"], "from": tail["out_start"]} if tail["mode"] == "hold" else None
    plan = {
        "output": {"duration": D, "fps": rec["fps"], "width": W, "height": H},
        "segments": segs, "zooms": zooms, "ripples": ripples,
        "intro": intro, "outro": outro,
        "sync": [m for _, _, _, m, _ in anchors],
        "style": sync.get("style", {}),
        "notes": notes,
        "generated_by": "tools/plan_builder.py from work/sync.json",
    }
    plan["generated_hash"] = plan_hash(plan)
    write_json(pr.w("plan.json"), plan)

    rows = ["| line | word | out time | action | src time | speed (approach) |", "|---|---|---|---|---|---|"]
    for c, o, act, meta, _ in anchors:
        rows.append(f"| {meta.get('line') or ''} | {meta.get('word') or ''} | {click_out(act['id']) or 0:.3f} | "
                    f"{act['id']} {act['target']} | {c:.3f} | {approach.get(act['id'], '')} |")
    body = "# Sync notes\n\n" + "\n".join(rows) + "\n"
    if notes:
        body += "\n## Builder decisions\n\n" + "\n".join(f"- {n}" for n in notes) + "\n"
    old = pr.w("sync-notes.md")
    if old.exists():
        prev = old.read_text(encoding="utf-8")
        if "## Judgment calls" in prev:            # keep the skill's own commentary
            body += "\n" + prev[prev.index("## Judgment calls"):]
    old.write_text(body, encoding="utf-8")

    print("\n".join(rows))
    for n in notes:
        print(f"note: {n}")
    print(f"{len(segs)} segments, {len(zooms)} zooms, {len(ripples)} ripples -> {pr.w('plan.json')}")
    ok = report("plan.json", *validate_plan(plan, probe, actions, lines))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
