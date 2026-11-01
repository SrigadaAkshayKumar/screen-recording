"""Hand-built plan for script-07 (95.666 s voiceover, 209.9 s recording, 1920x1080, no zooms/ripples).
Groups start exactly on each narration line's start. Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-07/work/'
DUR = 95.666
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(5.2, 7.6, 1.0), (7.6, 9.0), (9.63, 11.87)],
 2: [(13.67, 15.97), (16.77, 18.23)],
 3: [(19.3, 23.3)],
 4: [(24.3, 27.0)],
 5: [(43.17, 44.93), (45.8, 49.0)],
 6: [(61.33, 64.3)],
 7: [(64.3, 69.0)],
 8: [(69.0, 71.23), (72.3, 74.9)],
 9: [(79.6, 83.9), (84.93, 86.33), (89.73, 91.0)],
 10: [(99.3, 102.0), (117.0, 119.5)],
 11: [(119.5, 121.77), (123.6, 124.5)],
 12: [(135.0, 141.77)],
 13: [(145.5, 147.8)],
 14: [(152.47, 156.67), (162.63, 164.5)],
 15: [(164.5, 165.27), (166.13, 168.67), (173.03, 175.0)],
 16: [(175.0, 176.3), (178.8, 180.47), (182.6, 185.0)],
 17: [(202.7, 205.6)],
 18: [(205.6, 209.9)],
 19: [(185.0, 187.4)],
 20: [(197.73, 199.27), (143.77, 147.0)],
 21: [(116.73, 121.77), (123.6, 124.5)],
 22: [(187.4, 188.6), (190.03, 193.7)],
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
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": o1, "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]; t = o1
        print('line', n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f-%.2f' % (seg['out_start'], o1))
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
