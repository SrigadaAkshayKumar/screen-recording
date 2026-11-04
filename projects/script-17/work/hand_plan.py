"""Hand-built plan for script-17 (92.553 s voiceover, 275.7 s recording 1920x1080, baked recorder zoom: no zooms/ripples).
One group per narration line, starting on the line start; pieces (src_a, src_b) picked from 1 s sheets."""
import json
P = 'projects/script-17/work/'
DUR = 92.553
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
L[0] = 0.0
G = {
 1: [(6.9, 10.9)],
 2: [(12.8, 16.5)],
 3: [(20.6, 24.4), (28.0, 30.4)],
 4: [(45.2, 49.9)],
 5: [(61.5, 66.0)],
 6: [(52.0, 56.0)],
 7: [(65.2, 67.6), (72.0, 73.6)],
 8: [(78.7, 82.0)],
 9: [(96.9, 99.2), (104.6, 106.4), (115.0, 118.0)],
 10: [(118.8, 123.0)],
 11: [(139.8, 143.5)],
 12: [(147.6, 151.0)],
 13: [(171.8, 174.8)],
 14: [(182.0, 186.2)],
 15: [(218.8, 221.6)],
 16: [(227.1, 228.0), (230.0, 231.6), (234.9, 238.6)],
 17: [(155.9, 159.2), (239.0, 242.4)],
 18: [(269.3, 272.2)],
 19: [(255.6, 258.8)],
 20: [(227.6, 230.6), (272.2, 275.0)],
 21: [(215.0, 218.8)],
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
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
