"""Hand-built plan for script-17 (378 s recording, 92.648 s voiceover, baked-in recorder zoom, no click log:
no zooms/ripples). One group per narration line starting on its lines.json start; pieces from the moving windows
(freezedetect n=0.003 d=0.8) of the source."""
import json
P = 'projects/script-17/work/'
lines = json.load(open(P + 'lines.json'))
END = 92.648
B = {l['id']: l['start'] for l in lines}
# (line id, [(src_a, src_b[, fixed_out_dur])])
G = [
 (1, [(0.0, 2.4, 2.4), (13.17, 17.8)]),
 (2, [(17.8, 19.77), (20.57, 22.0)]),
 (3, [(22.0, 23.33), (33.1, 37.6)]),
 (4, [(73.0, 75.04)]),
 (5, [(75.04, 77.7), (79.8, 83.3)]),
 (6, [(85.3, 87.84)]),
 (7, [(87.84, 91.7)]),
 (8, [(91.7, 96.0), (102.3, 103.1)]),
 (9, [(46.07, 49.2)]),
 (10, [(49.2, 53.34)]),
 (11, [(114.2, 118.24)]),
 (12, [(165.0, 167.1), (168.5, 170.9), (171.8, 173.6)]),
 (13, [(140.6, 142.4), (143.8, 146.4)]),
 (14, [(205.6, 211.8)]),
 (15, [(213.0, 215.1)]),
 (16, [(215.1, 218.9), (224.5, 225.7)]),
 (17, [(225.7, 227.7), (231.1, 232.6), (239.4, 241.7), (242.6, 243.1)]),
 (18, [(262.5, 264.6)]),
 (19, [(264.6, 266.9), (271.3, 273.15)]),
 (20, [(273.15, 275.7)]),
 (21, [(275.7, 280.8)]),
 (22, [(280.8, 284.1)]),
]
starts = [0.0] + [B[g[0]] for g in G[1:]] + [END]
segs, prev_end = [], None
for k, (lid, pieces) in enumerate(G):
    o0, o1 = starts[k], starts[k + 1]
    fixed = [p[2] for p in pieces if len(p) > 2]
    free = [p for p in pieces if len(p) == 2]
    sp = sum(b - a for a, b in free) / (o1 - o0 - sum(fixed))
    t = o0
    for j, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if j == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} L{lid} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
