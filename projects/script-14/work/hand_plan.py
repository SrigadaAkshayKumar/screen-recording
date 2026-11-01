"""Hand plan for script-14 re-edit: one group per narration line, starting on lines.json start."""
import json
P = 'projects/script-14/work/'
lines = {l['id']: l for l in json.load(open(P + 'lines.json'))}
END = 91.672
# (line, [(src_a, src_b), ...])  -- group runs from this line's start to the next line's start
G = [
 (1, [(8.5, 17.8)]),
 (2, [(27.2, 41.4)]),
 (3, [(49.5, 51.8), (53.0, 55.3)]),
 (4, [(61.2, 69.4)]),
 (5, [(70.2, 72.5), (73.4, 75.7)]),
 (6, [(95.1, 98.1)]),
 (7, [(98.1, 101.7)]),
 (8, [(101.7, 108.4)]),
 (9, [(81.4, 83.4)]),
 (10, [(83.4, 86.0)]),
 (11, [(86.0, 89.5)]),
 (12, [(114.9, 120.4)]),
 (13, [(63.0, 69.4)]),
 (14, [(120.4, 125.0)]),
 (15, [(111.4, 113.3), (91.2, 93.1)]),
 (16, [(105.0, 108.4)]),
 (17, [(95.1, 101.7)]),
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
