"""Hand-built plan for script-10 (261.667 s recording, 89.118 s voiceover, no clicks log, no zooms/ripples).
Pieces come from freezedetect (n=0.003, d=0.8) moving windows; one group per narration line, starting on the line's start.
A piece may carry a 3rd value: a fixed output duration (used for the short static opening shots, played at 1x)."""
import json
P = 'projects/script-10/work/'
END = 95.016
G = [
 (0, 5.96, [(5.0, 7.4, 2.4), (12.7, 16.0)]),
 (5.96, 9.54, [(16.0, 19.0)]),
 (9.54, 15.82, [(23.5, 27.97), (36.1, 37.9)]),
 (15.82, 17.96, [(39.3, 40.9)]),
 (17.96, 24.44, [(40.9, 42.4), (43.57, 45.1), (46.03, 47.9)]),
 (24.44, 31.06, [(57.2, 63.7)]),
 (31.06, 33.14, [(13.0, 15.1)]),
 (33.14, 37.3, [(87.1, 91.77)]),
 (37.3, 39.3, [(100.93, 103.27)]),
 (39.3, 45.66, [(105.4, 106.37), (109.83, 111.07), (131.5, 133.07), (134.23, 135.5)]),
 (45.66, 48.62, [(112.4, 115.4)]),
 (48.62, 52.2, [(115.4, 119.27)]),
 (52.2, 57.38, [(123.33, 126.8), (136.2, 138.37)]),
 (57.38, 59.52, [(168.43, 170.6)]),
 (59.52, 65.44, [(172.13, 178.05)]),
 (65.44, 69.96, [(181.87, 186.4)]),
 (69.96, 74.38, [(194.0, 198.4)]),
 (74.38, 85.68, [(198.4, 209.2)]),
 (85.68, 88.9, [(189.6, 192.57)]),
 (88.9, 91.82, [(243.2, 246.1)]),
 (91.82, END, [(224.0, 227.2)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    free = [p for p in pieces if len(p) == 2]
    sp = sum(b - a for a, b in free) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        dur = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + dur
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 261.667}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
