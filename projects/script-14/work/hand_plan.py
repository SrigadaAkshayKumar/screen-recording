"""Hand plan for script-14 new 150 s take: one group per narration line, starting on lines.json start."""
import json
P = 'projects/script-14/work/'
lines = {l['id']: l for l in json.load(open(P + 'lines.json'))}
END = 91.672
# (line, [(src_a, src_b), ...])  -- group runs from this line's start to the next line's start
G = [
 (1, [(4.0, 12.3)]),
 (2, [(12.9, 15.9)]),
 (3, [(36.1, 42.8)]),
 (4, [(46.3, 52.8)]),
 (5, [(56.0, 59.5), (67.6, 71.2)]),
 (6, [(71.2, 75.7)]),
 (7, [(60.3, 63.3)]),
 (8, [(16.0, 19.6)]),
 (9, [(19.6, 24.9)]),
 (10, [(77.0, 79.4)]),
 (11, [(52.8, 55.9)]),
 (12, [(63.3, 67.5)]),
 (13, [(129.0, 136.0)]),
 (14, [(81.2, 84.4), (86.2, 88.2), (91.8, 94.0)]),
 (15, [(112.4, 115.0), (106.0, 108.9)]),
 (16, [(95.0, 99.4)]),
 (17, [(72.4, 76.6)]),
 (18, [(141.9, 149.05)]),
]
segs, prev_end = [], None
for k, (ln, pieces) in enumerate(G):
    o0 = 0.0 if ln == 1 else lines[ln]['start']
    o1 = lines[G[k + 1][0]]['start'] if k + 1 < len(G) else END
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for j, (a, b) in enumerate(pieces):
        end = o1 if j == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(ln, f'{o0:.2f}-{o1:.2f} speed {sp:.2f}x', pieces)
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
