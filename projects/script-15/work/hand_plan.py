"""Hand-built plan for script-15 (270 s recording with baked-in recorder zoom: no zooms/ripples; pieces are chosen from
freezedetect (n=0.003, d=0.8) moving windows of the source, 0.75-1.2x)."""
import json
P = 'projects/script-15/work/'
END = 91.58
G = [
 (0, 7.8, [(6.27, 9.87), (15.0, 17.4)]),
 (7.8, 14.5, [(18.37, 23.37), (24.2, 26.5)]),
 (14.5, 16.66, [(52.23, 53.5), (54.33, 55.2)]),
 (16.66, 24.26, [(57.1, 58.9), (59.9, 62.23), (69.4, 71.2), (75.87, 78.5)]),
 (24.26, 27.52, [(36.33, 39.77)]),
 (27.52, 31.96, [(87.0, 90.47), (92.2, 93.5)]),
 (31.96, 35.54, [(93.5, 95.73), (96.97, 97.93)]),
 (35.54, 39.54, [(131.7, 135.7)]),
 (39.54, 43.3, [(135.7, 139.27)]),
 (43.3, 47.5, [(142.8, 146.23), (151.33, 152.0)]),
 (47.5, 52.6, [(152.0, 153.8), (162.8, 166.0)]),
 (52.6, 54.36, [(166.0, 166.77), (177.53, 178.6)]),
 (54.36, 60.02, [(178.6, 180.67), (197.5, 200.5)]),
 (60.02, 64.84, [(200.5, 202.17), (203.9, 207.0)]),
 (64.84, 70.42, [(207.0, 210.47), (217.8, 219.6)]),
 (70.42, 75.0, [(221.77, 226.37)]),
 (75.0, 79.38, [(219.6, 220.8), (227.33, 230.67)]),
 (79.38, 82.3, [(246.1, 247.93), (249.37, 250.47)]),
 (82.3, 86.76, [(251.93, 254.77), (260.2, 261.8)]),
 (86.76, END, [(261.8, 266.6)]),
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
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 270.0}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
