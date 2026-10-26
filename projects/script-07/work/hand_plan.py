"""Hand-built plan for script-07 (104.9 s voiceover, 147.2 s recording, baked recorder zoom: no zooms/ripples).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed]);
pieces without a fixed speed share the group's slack uniformly."""
import json
P = 'projects/script-07/work/'
DUR = 104.908
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(10.03, 12.4), (14.07, 16.83), (18.1, 20.2)],
 2: [(22.7, 25.1)],
 3: [(27.9, 29.87), (30.9, 32.4)],
 4: [(36.0, 36.67), (38.23, 40.57)],
  5: [(46.0, 46.97), (55.0, 56.5), (58.07, 59.33), (63.4, 64.6), (66.1, 67.4), (68.27, 70.0)],
 6: [(70.0, 72.1)],
 7: [(72.1, 77.27)],
 8: [(53.6, 54.4), (79.7, 80.5), (84.0, 85.5)],
 9: [(80.5, 86.0)],
 10: [(50.57, 54.4)],
 11: [(88.0, 90.17), (90.97, 96.0)],
 12: [(106.0, 108.5), (114.67, 116.7), (118.07, 121.7)],
 13: [(127.0, 129.5), (130.5, 131.5)],
 14: [(131.5, 136.0), (139.4, 141.0)],
 15: [(123.5, 124.7), (125.7, 127.0)],
 16: [(45.1, 46.97), (72.1, 76.2)],
 17: [(41.7, 43.3), (45.1, 46.0)],
 18: [(131.0, 134.7)],
 19: [(58.07, 59.33), (63.4, 64.4)],
 20: [(66.1, 67.4), (68.27, 69.5), (139.4, 145.2)],
 21: [(133.0, 135.9), (123.5, 124.7)],
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
plan = {"output": {"duration": DUR, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
