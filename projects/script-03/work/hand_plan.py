"""Hand-built plan for script-03 (301 s Canva PDF-to-PPT take) for 98.081 s of voiceover. One group per
narration line (or run of lines) starting on the line start; pieces are (src_a, src_b) from moving
windows (freezedetect n=0.002 d=0.8 on the source). No zooms/ripples (no click log)."""
import json
P = 'projects/script-03/work/'
END = 98.081
G = [
 (0, 7.48, [(8.87, 12.23), (17.7, 20.93)]),
 (7.48, 11.12, [(22.17, 22.93), (23.73, 27.0)]),
 (11.12, 15.02, [(30.53, 34.27)]),
 (15.02, 24.1, [(37.67, 40.27), (40.27, 41.5), (47.1, 47.87), (49.27, 50.5), (50.93, 52.3)]),
 (24.1, 26.86, [(52.3, 53.93), (57.17, 58.17)]),
 (26.86, 31.48, [(61.93, 64.1), (67.97, 70.5)]),
 (31.48, 37.12, [(70.5, 73.63), (77.9, 80.5)]),
 (37.12, 43.24, [(80.5, 86.5)]),
 (43.24, 51.5, [(86.5, 88.23), (91.57, 93.6), (94.47, 96.87), (98.33, 100.0)]),
 (51.5, 55.74, [(100.0, 101.7), (106.33, 107.7), (108.57, 109.47)]),
 (55.74, 61.04, [(109.47, 110.4), (111.63, 116.0)]),
 (61.04, 69.18, [(258.0, 264.43), (267.97, 270.0)]),
 (69.18, 72.88, [(283.9, 284.73), (291.07, 292.23), (295.23, 295.87), (299.93, 300.9)]),
 (72.88, 75.22, [(276.23, 278.6)]),
 (75.22, 78.38, [(153.77, 157.0)]),
 (78.38, 82.48, [(157.0, 160.4), (162.9, 164.5)]),
 (82.48, 86.78, [(166.7, 170.3)]),
 (86.78, 93.86, [(172.73, 179.8)]),
 (93.86, END, [(185.63, 187.9), (189.7, 191.7)]),
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
