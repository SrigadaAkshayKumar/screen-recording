"""Hand-built plan for script-18: 275.6 s of recording (baked-in recorder zoom, long idle spells) for 83.9 s of
voiceover. Each group fills one narration interval; pieces are (src_a, src_b[, speed]). No zooms/ripples
(recorder zoom is baked in, so recording-pixel ripples would land wrong)."""
import json
P = 'projects/script-18/work/'
END = 83.917
G = [
 (0, 6.04, [(0.0, 6.0)]),
 (6.04, 9.82, [(6.0, 10.5)]),
 (9.82, 16.34, [(10.5, 17.0)]),
 (16.34, 21.0, [(33.0, 37.5)]),
 (21.0, 25.42, [(37.5, 42.0)]),
 (25.42, 28.28, [(45.2, 48.0)]),
 (28.28, 33.56, [(62.3, 66.6)]),
 (33.56, 36.88, [(66.6, 70.0)]),
 (36.88, 43.42, [(71.8, 75.6, 1.0), (75.6, 78.1, 2.0), (78.1, 79.6)]),
 (43.42, 47.38, [(80.6, 84.6)]),
 (47.38, 50.0, [(112.2, 115.0)]),
 (50.0, 56.68, [(127.6, 132.1), (143.9, 146.07)]),
 (56.68, 59.74, [(163.0, 166.0)]),
 (59.74, 65.9, [(166.0, 172.15)]),
 (65.9, 70.74, [(172.15, 177.0)]),
 (70.74, 76.22, [(204.0, 210.0)]),
 (76.22, END, [(229.1, 232.7), (258.0, 266.1)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    explicit = [p for p in pieces if len(p) == 3]
    if explicit:
        rest = o1 - o0 - sum((p[1]-p[0])/p[2] for p in explicit)
        fill = [p for p in pieces if len(p) == 2]
        spf = sum(p[1]-p[0] for p in fill) / rest
        durs = [(p[1]-p[0]) / (p[2] if len(p) == 3 else spf) for p in pieces]
    else:
        sp = sum(p[1]-p[0] for p in pieces) / (o1 - o0)
        durs = [(p[1]-p[0]) / sp for p in pieces]
    t = o0
    for k, (p, d) in enumerate(zip(pieces, durs)):
        end = o1 if k == len(pieces)-1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0]-prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
