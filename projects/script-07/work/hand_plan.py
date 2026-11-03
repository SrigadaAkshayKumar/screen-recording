"""Hand-built plan for script-07 (93.506 s voiceover, 20 lines, 311.067 s take, 1920x1080, no zooms/ripples).
Each group starts exactly on its narration line's start; pieces in a group share one speed."""
import json
P = 'projects/script-07/work/'
DUR = 93.506
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(0.0, 2.7), (10.0, 13.4)],
 2: [(13.6, 16.0), (20.9, 24.6)],
 3: [(33.0, 35.9), (40.4, 42.5)],
 4: [(48.4, 50.9), (36.6, 38.4)],
 5: [(58.0, 59.8), (60.4, 63.6)],
 6: [(75.0, 77.3)],
 7: [(77.3, 81.5), (84.4, 85.8)],
 8: [(86.5, 88.2), (93.6, 95.0)],
 9: [(94.3, 96.8), (127.4, 128.7)],
 10: [(148.9, 154.3)],
 11: [(159.4, 162.3)],
 12: [(170.8, 174.1)],
 13: [(200.0, 205.8)],
 14: [(205.8, 211.8)],
 15: [(231.0, 235.8)],
 16: [(235.8, 239.7)],
 17: [(243.2, 248.4)],
 18: [(249.0, 253.0)],
 19: [(276.5, 281.3)],
 20: [(299.9, 305.1)],
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
