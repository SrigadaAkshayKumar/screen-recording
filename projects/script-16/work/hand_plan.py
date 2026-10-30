"""Hand-built plan for script-16 (93.95 s voiceover, 406.6 s recording, baked recorder zoom: no zooms/ripples).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed]);
pieces without a fixed speed share the group's slack uniformly."""
import json
P = 'projects/script-16/work/'
DUR = 93.948
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(5.3, 8.0), (13.3, 16.4)],
 2: [(28.2, 32.2), (59.0, 60.0)],
 3: [(37.9, 41.9)],
 4: [(77.3, 80.6)],
 5: [(83.0, 85.0)],
 6: [(96.7, 100.4)],
 7: [(200.8, 203.6), (205.1, 206.9)],
 8: [(197.1, 199.8), (217.2, 218.5)],
 9: [(120.3, 122.0)],
 10: [(143.0, 148.8)],
 11: [(235.0, 236.8), (237.9, 239.3)],
 12: [(253.7, 256.0), (261.0, 262.2)],
 13: [(265.5, 267.0), (268.4, 270.5)],
 14: [(279.1, 282.5)],
 15: [(282.5, 285.5)],
 16: [(292.5, 297.2)],
 17: [(298.7, 300.9)],
 18: [(308.8, 313.0)],
 19: [(359.1, 364.5)],
 20: [(327.5, 331.9)],
 21: [(332.0, 335.5), (338.7, 341.5)],
 22: [(383.8, 392.0)],
 23: [(397.7, 400.2)],
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
        print(n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f' % (o1 - seg['out_start']))
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
