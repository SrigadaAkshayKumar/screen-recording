"""Hand-built plan for the script-20 re-edit (101.285 s voiceover, 116.9 s recording, 3420x1922, baked recorder zoom: no zooms/ripples).
Each line's footage is the step the line describes (work/actions.json, output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-20/work/'
DUR = 101.285
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(6.53, 8.93, 1.0), (8.93, 11.3), (11.3, 12.8, 1.0), (12.83, 13.8)],  # finished design, recorder zoom, Canva home loading
 2: [(14.5, 17.17), (18.23, 20.37)],      # home -> Create a design dialog -> Document -> new design
 3: [(23.2, 25.2), (38.0, 39.45), (100.0, 101.3)],  # blank white A4 page, page with margin guide, whole page
 4: [(28.5, 33.3)],                       # Elements panel, search, star result
 5: [(42.0, 44.0), (73.6, 75.7)],         # circle added; text inside circle
 6: [(77.3, 80.5)],                       # select circle+text, click Group
 7: [(33.8, 38.0), (97.93, 99.3)],        # star added + resized; duplicate page
 8: [(70.2, 73.5)],                       # text on circle retyped
 9: [(50.8, 54.9)],                       # plant placed with space around
10: [(82.4, 85.6)],                       # multi-select star + plant (for align)
11: [(90.0, 93.9)],                       # whole page, check circle near the bottom margin
12: [(94.0, 95.9)],                       # zoom check of layout
13: [(86.0, 90.0)],                       # star group arranged on page
14: [(44.4, 48.3), (49.43, 52.2)],        # circle placed, plant placed (layout, spacing)
15: [(99.3, 102.1)],                      # finished page overview
16: [(105.9, 109.0)],                     # Share -> Download
17: [(109.0, 113.0)],                     # download settings (PDF, toggles)
18: [(113.0, 114.37), (114.37, 116.17, 1.0)],  # Download click, PDF done
19: [(43.8, 47.0)],                       # circle resize with size tooltip (measure)
20: [(110.3, 113.4)],                     # download settings again (page options)
21: [(106.6, 110.4)],                     # Share panel with Print options
22: [(97.93, 100.5)],                     # finished sheet
23: [(114.4, 116.8, 1.0)],                # finished design, PDF downloaded
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
plan = {"output": {"duration": DUR, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
