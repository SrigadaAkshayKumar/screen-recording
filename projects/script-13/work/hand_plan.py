"""Hand-built plan for script-13 (102.264 s voiceover, 316 s recording 1920x1080, baked recorder zoom: no zooms/ripples).
Groups start on each narration line's start (lines.json). Pieces: (a, b) free speed; (a, b, 's', speed) fixed speed; (a, b, 'd', out_dur) fixed duration."""
import json
P = 'projects/script-13/work/'
DUR = 102.264
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(5.0, 6.8, 's', 1.0), (6.8, 11.0)],
 2: [(15.0, 18.2)],
 3: [(24.0, 28.6)],
 4: [(33.4, 35.8, 'd', 2.14), (35.8, 38.3, 'd', 1.5), (38.3, 41.0)],
 5: [(48.7, 53.8)],
 6: [(63.2, 64.9)],
 7: [(64.9, 69.0), (69.0, 71.6), (77.1, 79.6), (53.8, 55.3), (55.3, 56.8, 's', 1.0)],
 8: [(86.0, 89.2)],
 9: [(114.6, 117.4), (118.3, 119.7), (121.3, 122.4)],
 10: [(79.6, 84.6)],
 11: [(108.7, 112.6)],
 12: [(181.9, 185.2)],
 13: [(204.8, 207.0, 'd', 2.4), (210.5, 213.6)],
 14: [(222.8, 225.8, 'd', 3.15), (225.8, 228.4), (232.9, 234.4)],
 15: [(234.4, 236.0), (239.67, 243.8)],
 16: [(86.8, 89.6, 'd', 2.9), (122.4, 123.4, 'd', 1.0), (252.5, 255.9)],
 17: [(194.3, 198.6)],
 18: [(266.2, 269.6), (297.6, 300.8), (306.8, 309.9)],
}
N = len(G)
assert N == len(L), (N, len(L))
segs, prev = [], None
for n in range(1, N + 1):
    t0 = L[n - 1] if n > 1 else 0.0
    t1 = L[n] if n < N else DUR
    pcs = G[n]
    def fixed_dur(p):
        if len(p) == 2: return None
        return (p[1] - p[0]) / p[3] if p[2] == 's' else p[3]
    fixed = sum(fixed_dur(p) for p in pcs if len(p) == 4)
    free = sum(p[1] - p[0] for p in pcs if len(p) == 2)
    sp = free / (t1 - t0 - fixed) if free else 0
    t = t0
    for i, p in enumerate(pcs):
        d = fixed_dur(p) if len(p) == 4 else (p[1] - p[0]) / sp
        o1 = t1 if i == len(pcs) - 1 else round(t + d, 3)
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": o1, "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]
        print('line', n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - t)), 'out %.2f-%.2f' % (t, o1))
        t = o1
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
