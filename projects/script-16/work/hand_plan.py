"""Hand-built plan for script-16 (92.18 s voiceover, 361 s recording, baked recorder zoom: no zooms/ripples).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed]);
pieces without a fixed speed share the group's slack uniformly."""
import json
P = 'projects/script-16/work/'
DUR = 92.183
L = [r['start'] for r in json.load(open(P + 'lines.json'))['lines']] if isinstance(json.load(open(P + 'lines.json')), dict) else [r['start'] for r in json.load(open(P + 'lines.json'))]
G = {
 1: [(0.3, 4.6, 1.9), (4.7, 8.2), (12.1, 13.4)],
 2: [(15.1, 19.7, 1.9), (23.5, 24.7)],
 3: [(25.8, 32.5)],
 4: [(62.3, 65.4), (66.4, 67.8)],
 5: [(67.8, 72.5)],
 6: [(128.2, 130.9)],
 7: [(186.0, 189.5)],
 8: [(80.6, 87.0)],
 9: [(90.9, 94.4)],
 10: [(100.6, 106.7)],
 11: [(224.1, 229.6)],
 12: [(236.8, 240.1), (253.4, 254.8)],
 13: [(272.0, 274.5)],
 14: [(266.5, 271.0)],
 15: [(314.7, 320.6)],
 16: [(284.6, 285.8), (287.0, 289.1), (290.0, 291.5)],
 17: [(296.0, 298.2), (302.2, 303.3)],
 18: [(333.5, 337.0)],
 19: [(342.3, 345.8)],
 20: [(354.1, 358.0)],
}
segs, prev = [], None
for n in range(1, 21):
    t0 = L[n - 1] if n > 1 else 0.0
    t1 = L[n] if n < 20 else DUR
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
        print(n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f' % (o1 - seg['out_start']))
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
