"""Hand-built plan for script-17 (96.27 s voiceover, 130.5 s recording 3420x1922, baked recorder zoom: no zooms/ripples).
Groups start on each narration line start. Pieces (src_a, src_b) come from freezedetect moving windows."""
import json
P = 'projects/script-17/work/'
DUR = 96.27
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
L[0] = 0.0
G = {
 1: [(4.1, 5.4), (91.6, 95.2)],
 2: [(9.9, 13.0)],
 3: [(17.2, 21.2)],
 4: [(25.2, 28.4), (32.6, 34.2)],
 5: [(34.2, 38.1), (39.4, 40.2)],
 6: [(42.1, 46.6), (48.0, 48.9)],
 7: [(53.2, 55.6), (57.5, 60.5)],
 8: [(68.7, 71.9), (73.1, 74.5)],
 9: [(74.5, 75.6), (76.6, 77.9), (78.8, 79.6)],
 10: [(62.2, 63.5), (79.6, 80.4), (86.0, 88.5)],
 11: [(87.0, 90.8)],
 12: [(103.0, 110.5)],
 13: [(112.9, 115.8), (85.2, 87.4)],
 14: [(118.4, 119.3), (83.7, 85.2)],
 15: [(39.4, 41.3), (42.1, 44.4)],
 16: [(62.2, 64.7), (68.7, 71.9)],
 17: [(53.2, 55.6), (57.5, 58.5)],
 18: [(91.6, 95.4), (97.2, 100.5)],
 19: [(121.0, 124.4)],
 20: [(118.4, 119.3), (98.8, 100.4), (124.4, 128.5)],
}
N = len(G)
assert N == len(L), (N, len(L))
segs, prev = [], None
for n in range(1, N + 1):
    t0 = L[n - 1]
    t1 = L[n] if n < N else DUR
    pcs = G[n]
    sp = sum(p[1] - p[0] for p in pcs) / (t1 - t0)
    t = t0
    for i, p in enumerate(pcs):
        d = (p[1] - p[0]) / sp
        o1 = t1 if i == len(pcs) - 1 else round(t + d, 3)
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": round(o1, 3), "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]; t = o1
    print('line', n, 'x%.2f' % sp)
plan = {"output": {"duration": DUR, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
