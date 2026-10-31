"""Hand-built plan for script-18 (125 s take) for 89.861 s of voiceover. One group per line start;
pieces are (src_a, src_b) from moving windows (freezedetect n=0.002 d=0.8). No zooms/ripples."""
import json
P = 'projects/script-18/work/'
END = 89.861
G = [
 (0, 4.64, [(11.33, 15.0)]),
 (4.64, 7.94, [(15.0, 17.53), (19.8, 21.37)]),
 (7.94, 12.0, [(28.07, 31.7)]),
 (12.0, 15.72, [(32.67, 36.5)]),
 (15.72, 20.4, [(36.5, 39.87), (40.83, 42.03)]),
 (20.4, 24.72, [(43.6, 44.27), (45.57, 48.33), (49.23, 50.9)]),
 (24.72, 30.5, [(58.63, 62.8), (70.73, 72.3)]),
 (30.5, 34.6, [(104.0, 108.2)]),
 (34.6, 37.12, [(108.2, 109.77), (111.73, 112.9)]),
 (37.12, 42.78, [(72.3, 75.2), (112.9, 115.1)]),
 (42.78, 47.88, [(91.93, 96.9)]),
 (47.88, 52.88, [(96.9, 100.0), (118.0, 120.0)]),
 (52.88, 55.98, [(87.7, 90.8)]),
 (55.98, 62.9, [(120.0, 125.13), (101.0, 102.5)]),
 (62.9, 65.32, [(98.0, 100.4)]),
 (65.32, 70.98, [(100.4, 103.0), (105.0, 108.1)]),
 (70.98, 76.22, [(34.0, 39.2)]),
 (76.22, 80.56, [(39.2, 43.6)]),
 (80.56, 83.14, [(45.57, 48.1)]),
 (83.14, END, [(49.23, 51.0), (117.0, 121.3)]),
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
