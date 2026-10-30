"""Hand-built plan for script-03 (RSVP form in Canva; 190.2 s recording 3420x1922, 107.65 s voiceover,
baked recorder zoom, no clicks log -> no zooms/ripples). One group per narration line starting on that
line's lines.json start; pieces come from the moving windows of freezedetect (n=0.003, d=0.8) on the source."""
import json
P = 'projects/script-03/work/'
END = 107.648
G = [
 (0, 7.92, [(145.2, 146.3), (147.73, 149.87), (156.37, 157.63), (172.47, 174.4)]),
 (7.92, 10.1, [(28.87, 31.2)]),
 (10.1, 13.38, [(35.3, 39.7)]),
 (13.38, 16.68, [(43.9, 47.33)]),
 (16.68, 22.66, [(48.2, 50.6), (51.63, 54.93)]),
 (22.66, 25.24, [(54.93, 57.5)]),
 (25.24, 29.72, [(61.27, 64.53), (66.0, 67.5)]),
 (29.72, 34.88, [(71.7, 74.47), (75.7, 78.4)]),
 (34.88, 39.36, [(92.0, 94.33), (95.17, 97.47)]),
 (39.36, 42.62, [(97.47, 99.4), (105.1, 106.5)]),
 (42.62, 47.06, [(57.5, 61.27)]),
 (47.06, 55.7, [(82.07, 88.83), (90.73, 92.0)]),
 (55.7, 60.6, [(84.0, 88.8)]),
 (60.6, 65.28, [(168.5, 172.47)]),
 (65.28, 66.96, [(122.6, 124.9)]),
 (66.96, 71.26, [(147.73, 149.87), (151.47, 153.8)]),
 (71.26, 75.14, [(158.9, 161.7), (178.67, 179.97)]),
 (75.14, 80.86, [(181.83, 184.6), (187.5, 188.77), (189.57, 190.17)]),
 (80.86, 82.84, [(119.3, 121.3)]),
 (82.84, 89.96, [(125.83, 133.47)]),
 (89.96, 92.56, [(137.0, 139.8)]),
 (92.56, 103.06, [(10.87, 13.2), (14.8, 17.0), (18.9, 21.17), (22.63, 24.93)]),
 (103.06, END, [(153.9, 158.9)]),
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 3420, "height": 1922, "fps": 30, "duration": 190.167}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
