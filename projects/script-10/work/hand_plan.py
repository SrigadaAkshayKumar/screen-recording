"""Hand-built plan for script-10 (219.433 s recording, 94.877 s voiceover, no clicks log, no zooms/ripples).
Pieces come from freezedetect (n=0.002, d=0.8) moving windows + 8 contact sheets; one group per narration line
(or small run), starting on the line's start. A piece may carry a 3rd value: a fixed output duration."""
import json
P = 'projects/script-10/work/'
END = 94.877
G = [
 (0, 10.32, [(2.0, 4.23, 2.4), (4.23, 10.33)]),
 (10.32, 12.74, [(11.9, 13.8)]),
 (12.74, 17.74, [(16.5, 18.9), (20.0, 22.9)]),
 (17.74, 20.24, [(23.93, 25.2), (26.37, 27.6)]),
 (20.24, 24.36, [(26.4, 29.33), (43.0, 44.3)]),
 (24.36, 27.3, [(37.0, 39.63)]),
 (27.3, 29.4, [(43.0, 45.0)]),
 (29.4, 38.46, [(46.43, 48.8), (51.0, 52.63), (58.13, 60.3), (61.27, 63.5)]),
 (38.46, 42.2, [(79.47, 82.8)]),
 (42.2, 45.5, [(82.8, 86.0)]),
 (45.5, 48.48, [(98.6, 101.6)]),
 (48.48, 54.32, [(101.6, 104.83), (109.97, 112.5)]),
 (54.32, 56.06, [(89.0, 90.8)]),
 (56.06, 61.88, [(158.57, 161.07), (161.9, 165.5)]),
 (61.88, 67.74, [(112.5, 114.5), (115.6, 118.5), (120.57, 122.1)]),
 (67.74, 72.8, [(165.5, 169.5), (170.5, 171.6)]),
 (72.8, 74.42, [(142.6, 144.3)]),
 (74.42, 79.3, [(144.3, 147.47), (149.8, 151.5)]),
 (79.3, 82.64, [(151.5, 153.5), (172.0, 173.4)]),
 (82.64, 87.72, [(122.1, 123.37), (146.0, 147.47), (152.0, 153.5)]),
 (87.72, END, [(197.0, 200.2), (203.0, 205.0), (207.0, 209.3)]),
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
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 219.433}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
