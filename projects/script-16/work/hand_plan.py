"""Hand-built plan for script-16 (recording has baked-in recorder zoom: no zooms/ripples).
Pieces are (src_a, src_b, speed, line) taken from the moving windows of the source."""
import json
P = 'projects/script-16/work/'
DUR = 94.83
PC = [
 (9.7, 11.4, 1.0, 1), (11.4, 15.0, 0.75, 1),
 (16.4, 22.1, 1.45, 2),
 (27.0, 28.5, 0.8, 3), (36.0, 37.5, 1.0, 3),
 (37.5, 41.7, 1.3, 4),
 (53.1, 54.8, 0.9, 5), (56.4, 57.6, 0.8, 5),
 (68.7, 70.2, 0.8, 6),
 (119.9, 121.8, 1.0, 7), (128.0, 132.1, 1.3, 7), (135.3, 138.9, 0.9, 8),
 (68.7, 73.9, 1.0, 9),
 (77.4, 83.5, 1.2, 10),
 (85.3, 87.7, 0.85, 11),
 (87.7, 89.2, 1.0, 12), (92.4, 95.1, 0.75, 12),
 (98.9, 101.4, 0.9, 13),
 (104.3, 111.6, 1.0, 14),
 (110.4, 111.6, 0.75, 15), (111.6, 113.4, 1.0, 15),
 (161.1, 162.3, 0.8, 16), (167.0, 169.3, 0.75, 16),
 (139.9, 142.0, 0.75, 17),
 (142.0, 143.9, 0.75, 18), (144.4, 147.0, 0.75, 19),
 (102.6, 104.3, 0.8, 20), (105.4, 106.7, 0.75, 20), (108.0, 109.2, 0.75, 20),
 (172.1, 174.7, 0.9, 21),
 (163.9, 165.2, 0.75, 22), (162.3, 163.9, 0.8, 22),
 (180.4, 188.1, 1.4, 23),
]
tot = sum((b - a) / s for a, b, s, _ in PC)
print('total', round(tot, 2), 'target', DUR)
# scale the last piece to land exactly on DUR
a, b, s, l = PC[-1]
rest = tot - (b - a) / s
PC[-1] = (a, b, (b - a) / (DUR - rest), l)
segs, t, prev, cum = [], 0.0, None, {}
for i, (a, b, s, l) in enumerate(PC):
    d = (b - a) / s
    o1 = round(t + d, 3) if i < len(PC) - 1 else DUR
    seg = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        seg["xfade"] = True
    segs.append(seg); prev = b; t = o1
    cum[l] = o1
print({k: round(v, 1) for k, v in cum.items()})
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
print('last speed', PC[-1][2])
