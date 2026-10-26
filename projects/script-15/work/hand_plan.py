"""Hand-built plan for script-15 (429.8 s recording, 102.77 s voiceover, no clicks log, no zooms/ripples).
Pieces come from freezedetect (n=0.003, d=0.8) moving windows of the source; one group per narration line,
each group starts on its line's lines.json start."""
import json
P = 'projects/script-15/work/'
END = 102.772
G = [
 (0, 7.9, [(4.9, 9.43), (9.43, 10.9)]),
 (7.9, 11.34, [(15.87, 18.9)]),
 (11.34, 14.82, [(23.57, 28.0)]),
 (14.82, 20.72, [(28.0, 32.63), (32.63, 34.3)]),
 (20.72, 27.58, [(84.0, 88.6), (109.4, 113.77)]),
 (27.58, 30.98, [(118.87, 121.17), (128.77, 131.07)]),
 (30.98, 34.88, [(133.8, 134.9), (137.13, 141.73)]),
 (34.88, 38.6, [(206.5, 210.0), (225.9, 227.7)]),
 (38.6, 41.12, [(215.93, 217.53), (221.97, 223.3)]),
 (41.12, 50.24, [(266.3, 267.5), (269.7, 271.1), (271.93, 276.0), (284.07, 286.37)]),
 (50.24, 53.26, [(290.8, 293.5)]),
 (53.26, 58.18, [(293.5, 298.4)]),
 (58.18, 61.7, [(303.93, 306.73), (307.7, 308.9)]),
 (61.7, 65.32, [(315.5, 319.17)]),
 (65.32, 68.64, [(320.63, 322.2), (323.27, 324.57)]),
 (68.64, 71.12, [(350.47, 352.95)]),
 (71.12, 75.42, [(352.95, 356.77)]),
 (75.42, 80.9, [(365.4, 367.8), (370.1, 372.8)]),
 (80.9, 86.42, [(375.47, 378.3), (385.07, 388.2)]),
 (86.42, 91.76, [(388.2, 393.5)]),
 (91.76, 95.58, [(396.33, 400.33)]),
 (95.58, 100.82, [(409.0, 414.67)]),
 (100.82, END, [(420.7, 423.0)]),
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
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 429.8}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
