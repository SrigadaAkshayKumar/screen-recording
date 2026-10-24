"""Hand-built plan for script-20 (255 s recording with baked-in recorder zoom: no zooms/ripples; pieces are chosen from
freezedetect (n=0.003, d=0.8) moving windows of the source, 0.75-1.2x)."""
import json
P = 'projects/script-20/work/'
END = 89.675
G = [
 (0, 8.98, [(7.6, 10.83), (12.2, 15.57), (16.37, 17.2)]),
 (8.98, 13.16, [(18.0, 21.47), (22.7, 24.87)]),
 (13.16, 15.7, [(26.23, 29.03)]),
 (15.7, 19.24, [(43.17, 45.5), (48.23, 50.57)]),
 (19.24, 22.92, [(61.8, 63.07), (64.17, 66.4)]),
 (22.92, 29.26, [(70.0, 76.3)]),
 (29.26, 34.02, [(91.47, 92.57), (93.7, 95.9), (97.43, 99.5)]),
 (34.02, 38.1, [(146.0, 149.4), (150.3, 151.5)]),
 (38.1, 41.72, [(107.5, 111.1)]),
 (41.72, 44.64, [(66.4, 69.3)]),
 (44.64, 49.86, [(139.0, 144.0)]),
 (49.86, 53.74, [(112.83, 116.07), (120.73, 121.5)]),
 (53.74, 55.8, [(126.83, 128.9)]),
 (55.8, 65.32, [(167.53, 169.83), (174.73, 176.07), (178.57, 180.13), (181.2, 182.77), (185.03, 188.3)]),
 (65.32, 70.56, [(191.1, 195.47), (198.3, 199.9)]),
 (70.56, 76.58, [(215.8, 221.67)]),
 (76.58, 80.14, [(223.8, 225.83), (227.33, 229.1)]),
 (80.14, 84.76, [(233.03, 238.0)]),
 (84.76, END, [(239.0, 241.07), (242.37, 244.93), (252.13, 253.3)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 255.333}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
