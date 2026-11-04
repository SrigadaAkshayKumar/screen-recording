"""Hand plan for script-14 (VLC snapshot / Canva freeze-frame take, 154 s): one group per narration line,
starting on lines.json start. Piece = (src_a, src_b) shares the group's remaining time, or (a, b, speed)
for a fixed-speed piece (static source spans at 2x)."""
import json
P = 'projects/script-14/work/'
lines = {l['id']: l for l in json.load(open(P + 'lines.json'))}
END = 86.647
G = [
 (1, [(0.0, 2.0, 1.0), (17.3, 22.6)]),
 (2, [(23.2, 29.0)]),
 (3, [(34.8, 40.5)]),
 (4, [(29.0, 33.5)]),
 (5, [(60.2, 61.9), (61.9, 63.5, 2.0), (63.5, 65.0)]),
 (6, [(76.5, 84.3)]),
 (7, [(85.4, 89.4)]),
 (8, [(92.4, 96.77), (96.77, 98.8, 2.0), (98.8, 100.3)]),
 (9, [(126.0, 129.4)]),
 (10, [(113.2, 117.3)]),
 (11, [(117.6, 121.6)]),
 (12, [(129.3, 131.0)]),
 (13, [(131.0, 134.8), (134.8, 137.0, 2.0)]),
 (14, [(121.7, 125.9)]),
 (15, [(65.4, 69.9)]),
 (16, [(106.5, 112.8)]),
 (17, [(71.0, 76.4)]),
 (18, [(144.4, 149.4), (149.4, 151.1, 2.0), (151.1, 152.0)]),
]
segs, prev_end = [], None
for k, (ln, pieces) in enumerate(G):
    o0 = 0.0 if ln == 1 else lines[ln]['start']
    o1 = lines[G[k + 1][0]]['start'] if k + 1 < len(G) else END
    fixed = sum((p[1] - p[0]) / p[2] for p in pieces if len(p) == 3)
    var = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = var / (o1 - o0 - fixed) if var else 1
    t = o0
    for j, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = (b - a) / (p[2] if len(p) == 3 else sp)
        end = o1 if j == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(ln, f'{o0:.2f}-{o1:.2f} var speed {sp:.2f}x', pieces)
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
