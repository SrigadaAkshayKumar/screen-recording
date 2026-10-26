"""Hand-built plan for script-18 (336 s take, baked-in recorder zoom) for 97.756 s of voiceover.
One group per narration line, starting on that line's lines.json start; pieces are (src_a, src_b)
taken from the moving windows (freezedetect n=0.003 d=0.8 on the source). No zooms/ripples."""
import json
P = 'projects/script-18/work/'
END = 97.756
G = [
 (0, 7.92, [(15.0, 19.0), (276.0, 279.8)]),
 (7.92, 11.6, [(25.2, 28.9)]),
 (11.6, 17.48, [(33.3, 39.4)]),
 (17.48, 23.76, [(75.2, 81.4)]),
 (23.76, 26.48, [(95.8, 98.7)]),
 (26.48, 30.26, [(102.9, 106.6)]),
 (30.26, 35.84, [(112.3, 118.1)]),
 (35.84, 39.16, [(156.5, 160.0)]),
 (39.16, 44.58, [(160.0, 164.5), (167.3, 168.4)]),
 (44.58, 51.06, [(131.1, 134.7), (136.6, 139.4)]),
 (51.06, 55.74, [(209.9, 214.6)]),
 (55.74, 62.18, [(214.6, 221.0)]),
 (62.18, 68.36, [(223.8, 226.0), (230.7, 232.5), (233.4, 236.0)]),
 (68.36, 70.82, [(236.0, 238.4)]),
 (70.82, 76.86, [(272.6, 276.0), (250.9, 253.4)]),
 (76.86, 82.34, [(194.0, 199.5)]),
 (82.34, 87.2, [(284.9, 289.8)]),
 (87.2, 89.6, [(296.2, 298.6)]),
 (89.6, 94.64, [(305.6, 308.8), (323.6, 325.8)]),
 (94.64, END, [(326.0, 329.1)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(p[1]-p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces)-1 else t + (p[1]-p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0]-prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for g in G:
    print(g[0], round(sum(p[1]-p[0] for p in g[2])/(g[1]-g[0]),2))
