"""Hand-built plan for script-16 (96.27 s voiceover, 133.6 s recording 3420x1922, baked recorder zoom: no zooms/ripples).
Groups start on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed]).
Windows are the moving spans from freezedetect n=0.002 d=0.8 (static: 0-7.67,13.2-14.4,24.2-25.2,30.07-30.9,34-37.03,
57.8-60.27,62.3-64.33,68.17-70.77,92.27-95.2,102.4-103.4,118.9-121.3,122.8-124.4)."""
import json
P = 'projects/script-16/work/'
DUR = 96.27
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(4.0, 5.4, 1.0), (7.67, 13.2)],
 2: [(14.4, 19.5)],
 3: [(41.5, 44.3)],
 4: [(45.5, 47.5)],
 5: [(47.5, 54.5)],
 6: [(64.33, 67.6)],
 7: [(70.77, 76.0)],
 8: [(76.0, 79.0), (107.0, 110.5)],
 9: [(111.0, 114.5)],
 10: [(81.0, 86.0)],
 11: [(114.5, 118.9), (121.3, 122.8)],
 12: [(60.27, 62.3), (88.8, 89.8)],
 13: [(54.5, 57.8)],
 14: [(25.2, 30.07), (30.9, 32.2)],
 15: [(32.2, 34.0), (37.03, 40.0)],
 16: [(95.2, 102.4)],
 17: [(86.5, 92.27)],
 18: [(103.4, 107.0), (100.0, 101.0)],
 19: [(124.4, 130.0)],
}
N = len(G)
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
        print('line', n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f' % (o1 - seg['out_start']))
plan = {"output": {"duration": DUR, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
