"""Hand-built plan for script-20 (97.059 s voiceover, 731.1 s recording, 1920x1080, baked recorder zoom: no zooms/ripples).
Each line's footage is the step the line describes (work/actions.json, output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-20/work/'
DUR = 97.059
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(706.0, 710.0), (666.8, 669.9)],   # countdown playing back (result)
 2: [(14.3, 20.8)],     # new design: page, Create a design dialog, blank page
 3: [(24.7, 29.1)],     # blank page, timeline extended to 20 s
 4: [(60.0, 62.4)],     # Add a heading
 5: [(109.0, 114.1)],   # building rows (rank numbers)
 6: [(138.9, 141.7)],   # numbers 1-5 in order
 7: [(159.0, 163.1)],   # names typed
 8: [(267.3, 273.3)],   # alignment guides: consistent spacing
 9: [(460.0, 463.1)],   # select 5 inshort -> Group
 10: [(463.1, 465.0)],  # next entry grouped
 11: [(465.5, 470.8)],  # other entries grouped, numbers stay visible
 12: [(508.7, 512.4)],  # timeline group bars
 13: [(512.4, 520.9)],  # dragging bars to set start times
 14: [(524.0, 527.6)],  # bars stay to the end
 15: [(577.6, 580.3)],  # animation markers on bars
 16: [(585.2, 591.2)],  # entries/animation on timeline
 17: [(630.0, 632.9)],  # timeline at the end
 18: [(638.0, 640.8)],  # holding time at end
 19: [(647.7, 653.6)],  # extend final bar
 20: [(653.6, 656.8), (560.0, 563.4)],  # extend, tooltip
 21: [(718.7, 724.76)], # share -> download panel
}
N = len(G)
assert N == len(L), (N, len(L))
segs, prev = [], None
for n in range(1, N + 1):
    t0 = L[n - 1] if n > 1 else 0.0
    t1 = L[n] if n < N else DUR
    pcs = G[n]
    fixed = sum((p[1] - p[0]) / p[2] for p in pcs if len(p) == 3)
    free = sum(p[1] - p[0] for p in pcs if len(p) == 2)
    sp = free / (t1 - t0 - fixed) if free else 0
    t = t0
    for i, p in enumerate(pcs):
        s = p[2] if len(p) == 3 else sp
        d = (p[1] - p[0]) / s
        o1 = t1 if i == len(pcs) - 1 else round(t + d, 3)
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": round(o1, 3), "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]; t = o1
        print('line', n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f-%.2f' % (seg['out_start'], o1))
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
