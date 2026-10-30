"""Hand-built plan for script-13 (93.948 s voiceover, 202.7 s recording, 1920x1080, baked recorder zoom: no zooms/ripples).
Each line's footage is the step the line describes (work/actions.json, output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-13/work/'
DUR = 93.948
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(0.0, 3.3), (12.87, 14.6), (16.8, 19.0)],
 2: [(29.4, 31.7)],
 3: [(47.47, 51.3)],
 4: [(51.3, 54.1), (55.8, 57.4)],
 5: [(57.4, 60.2)],
 6: [(60.2, 63.2)],
 7: [(63.2, 66.3), (67.33, 70.0)],
 8: [(70.0, 71.2), (72.47, 73.8)],
 9: [(73.8, 77.93), (87.2, 88.0)],
 10: [(88.0, 89.97)],
 11: [(93.73, 96.3), (104.0, 107.3)],
 12: [(107.3, 108.2), (111.53, 112.2), (113.27, 114.73)],
 13: [(119.13, 122.2), (123.6, 125.37), (127.27, 128.1)],
 14: [(128.1, 129.33), (131.83, 136.4), (137.57, 138.6)],
 15: [(138.6, 139.47), (140.67, 142.17), (152.57, 155.3)],
 16: [(155.3, 156.0), (157.53, 160.27), (161.6, 163.3), (164.53, 165.4)],
 17: [(165.4, 166.13), (180.87, 183.0)],
 18: [(183.0, 185.7)],
 19: [(185.7, 192.0)],
 20: [(192.0, 194.3)],
 21: [(189.0, 192.2)],
 22: [(190.0, 192.0), (194.3, 195.9)],
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
