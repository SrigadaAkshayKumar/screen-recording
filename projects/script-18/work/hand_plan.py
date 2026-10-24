"""Hand-built plan for script-18 (269 s take, baked-in recorder zoom) for
91.9 s of voiceover. Each group fills one narration interval; pieces are (src_a, src_b[, speed]).
Pieces are taken from the moving windows (freezedetect n=0.003). No zooms/ripples (recorder zoom is baked in)."""
import json
P = 'projects/script-18/work/'
END = 91.905
G = [
 (0, 6.06, [(11.0, 14.4), (21.0, 22.2)]),
 (6.06, 10.38, [(14.4, 16.6), (22.2, 23.3)]),
 (10.38, 16.22, [(29.4, 34.5)]),
 (16.22, 19.72, [(40.9, 42.6), (43.8, 45.0)]),
 (19.72, 24.54, [(45.0, 46.6), (47.2, 49.3)]),
 (24.54, 27.76, [(49.3, 51.0), (57.7, 58.5)]),
 (27.76, 29.78, [(58.5, 60.5)]),
 (29.78, 33.82, [(61.5, 62.4), (64.3, 66.1), (74.7, 77.3)]),
 (33.82, 36.56, [(86.2, 87.7), (91.0, 92.3)]),
 (36.56, 40.14, [(134.0, 137.5)]),
 (40.14, 44.94, [(169.5, 171.9), (173.4, 175.7)]),
 (44.94, 47.84, [(140.7, 142.7), (179.2, 180.2)]),
 (47.84, 53.58, [(142.7, 147.2), (148.6, 150.2)]),
 (53.58, 58.6, [(151.4, 153.6), (154.5, 156.2)]),
 (58.6, 65.3, [(191.2, 195.1), (196.9, 201.4)]),
 (65.3, 72.4, [(220.8, 226.5)]),
 (72.4, 76.78, [(226.5, 231.0)]),
 (76.78, 82.26, [(231.0, 233.0), (236.9, 240.5)]),
 (82.26, 85.9, [(241.4, 245.3)]),
 (85.9, END, [(253.1, 254.7), (255.7, 257.3), (260.3, 263.0)]),
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
        "segments": segs, "zooms": [{"out_t": 11.0, "x": 710, "y": 580, "scale": 1.6, "in": 0.6, "hold": 12.9, "out": 0.6}], "ripples": [], "intro": None, "outro": None,
        "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
