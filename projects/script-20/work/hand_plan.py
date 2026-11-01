"""Hand-built plan for script-20 (97.059 s voiceover, 731.1 s recording, 1920x1080, baked recorder zoom: no zooms/ripples).
Each line's footage is the step the line describes (work/actions.json, output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-20/work/'
DUR = 95.202
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(1.27, 4.4), (5.33, 6.9)],
 2: [(6.9, 9.83)],
 3: [(12.0, 13.67), (8.0, 9.83)],
 4: [(13.67, 17.57)],
 5: [(17.57, 24.73)],
 6: [(25.7, 28.0)],
 7: [(28.0, 31.0)],
 8: [(31.0, 33.17), (34.27, 36.83)],
 9: [(31.8, 33.17), (34.27, 36.0)],
 10: [(39.53, 43.73)],
 11: [(47.63, 50.0)],
 12: [(50.0, 56.0)],
 13: [(6.9, 9.4)],
 14: [(5.33, 9.83)],
 15: [(31.0, 33.17), (34.27, 35.4)],
 16: [(12.0, 13.67), (15.07, 17.57)],
 17: [(22.23, 24.73), (25.7, 29.0)],
 18: [(1.27, 4.4), (5.33, 7.5)],
 19: [(28.7, 33.17), (34.27, 36.83)],
 20: [(56.0, 62.4)],
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
