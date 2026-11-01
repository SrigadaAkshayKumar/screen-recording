"""Hand-built plan for script-13 (90.001 s voiceover, 148.8 s recording 3420x1922, baked recorder zoom: no zooms/ripples).
Groups start on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-13/work/'
DUR = 90.001
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(0.0, 1.2, 1.0), (23.0, 24.4), (30.63, 32.67), (38.0, 39.57)],
 2: [(4.9, 8.17), (13.57, 14.87)],
 3: [(16.23, 19.17), (20.4, 21.2)],
 4: [(34.5, 37.2)],
 5: [(43.03, 46.77), (49.2, 52.67)],
 6: [(74.1, 78.5), (93.43, 97.0)],
 7: [(107.5, 111.0), (100.2, 102.07)],
 8: [(64.3, 71.03), (58.47, 61.4)],
 9: [(116.9, 118.67), (102.07, 103.9)],
 10: [(120.03, 124.0)],
 11: [(124.0, 126.5)],
 12: [(53.47, 57.67), (58.47, 60.5)],
 13: [(126.5, 130.0)],
 14: [(130.0, 133.87)],
 15: [(138.6, 140.47), (144.77, 146.2)],
 16: [(74.1, 76.8), (93.43, 95.0)],
 17: [(95.0, 97.7), (76.8, 78.5)],
 18: [(111.0, 114.07), (146.2, 148.8)],
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
