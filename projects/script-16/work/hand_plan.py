"""Hand-built plan for script-16 (92.508 s voiceover, 297.4 s recording, baked recorder zoom: no zooms/ripples).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed]);
pieces without a fixed speed share the group's slack uniformly. Windows avoid scenes.json stills."""
import json
P = 'projects/script-16/work/'
DUR = 92.508
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(5.2, 8.5), (15.0, 19.5)],
 2: [(25.2, 27.9)],
 3: [(27.9, 30.2), (108.7, 111.97)],
 4: [(52.4, 56.4)],
 5: [(65.2, 67.8), (79.8, 81.2)],
 6: [(81.2, 84.5)],
 7: [(84.5, 87.1), (89.2, 90.8)],
 8: [(92.7, 95.9), (97.0, 101.2)],
 9: [(129.0, 131.5), (132.5, 135.0)],
 10: [(171.4, 173.4)],
 11: [(175.1, 180.1)],
 12: [(137.4, 141.4), (143.6, 145.7), (147.4, 148.5)],
 13: [(148.5, 151.6), (153.3, 155.6)],
 14: [(205.9, 207.3)],
 15: [(207.3, 209.3)],
 16: [(212.2, 216.4), (217.3, 220.7)],
 17: [(238.2, 242.4)],
 18: [(285.0, 289.0)],
 19: [(273.6, 279.3)],
 20: [(280.0, 284.6)],
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
