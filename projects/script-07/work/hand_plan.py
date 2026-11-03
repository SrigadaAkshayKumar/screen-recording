"""Hand-built plan for script-07 (97.756 s voiceover, 311.067 s recording, 1920x1080, no zooms/ripples).
Groups start exactly on each narration line's start; pieces in a group share one speed."""
import json
P = 'projects/script-07/work/'
DUR = 97.756
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(0.0, 3.6)],
 2: [(8.77, 10.8), (12.13, 15.63)],
 3: [(15.63, 21.93)],
 4: [(24.77, 27.13), (34.5, 36.8)],
 5: [(48.1, 52.3)],
 6: [(56.93, 58.63), (60.2, 63.07)],
 7: [(40.63, 42.93)],
 8: [(78.57, 81.2), (98.33, 101.5)],
 9: [(101.5, 104.27)],
 10: [(126.83, 129.2), (148.57, 150.33)],
 11: [(150.33, 152.67), (131.0, 132.7)],
 12: [(156.7, 159.5)],
 13: [(159.5, 163.7)],
 14: [(220.8, 222.6), (205.77, 208.77)],
 15: [(193.73, 199.63)],
 16: [(233.47, 235.77), (237.3, 239.63)],
 17: [(169.53, 173.4)],
 18: [(173.4, 175.2)],
 19: [(175.2, 178.6)],
 20: [(242.23, 246.8)],
 21: [(271.03, 275.0)],
 22: [(290.0, 295.27)],
}
N = len(G)
assert N == len(L), (N, len(L))
segs, prev = [], None
for n in range(1, N + 1):
    t0 = L[n - 1] if n > 1 else 0.0
    t1 = L[n] if n < N else DUR
    pcs = G[n]
    sp = sum(p[1] - p[0] for p in pcs) / (t1 - t0)
    t = t0
    for i, p in enumerate(pcs):
        d = (p[1] - p[0]) / sp
        o1 = t1 if i == len(pcs) - 1 else round(t + d, 3)
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": o1, "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]; t = o1
    print('line', n, 'x%.2f' % sp)
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
