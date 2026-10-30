"""Hand-built plan for script-15 (345.5 s recording, 89.118 s voiceover, no clicks log, no zooms/ripples).
Pieces come from freezedetect (n=0.003, d=0.8) moving windows; one group per narration line, starting on the line's start.
A piece may carry a 3rd value: a fixed output duration (used for the short static opening shots, played at 1x)."""
import json
P = 'projects/script-15/work/'
END = 89.118
G = [
 (0, 6.04, [(2.0, 4.4, 2.4), (9.9, 12.8)]),
 (6.04, 11.34, [(9.9, 15.0)]),
 (11.34, 15.32, [(13.6, 15.0), (15.5, 17.9, 2.4)]),
 (15.32, 19.72, [(22.5, 24.2), (25.3, 27.1)]),
 (19.72, 22.26, [(39.0, 41.6)]),
 (22.26, 25.98, [(45.7, 48.1), (48.9, 50.0)]),
 (25.98, 28.24, [(52.2, 54.5)]),
 (28.24, 34.48, [(221.5, 227.5)]),
 (34.48, 36.4, [(232.2, 233.4), (236.7, 237.6)]),
 (36.4, 40.6, [(91.8, 95.4)]),
 (40.6, 43.26, [(237.6, 240.3)]),
 (43.26, 46.96, [(30.9, 34.5)]),
 (46.96, 53.38, [(251.2, 254.8), (262.6, 263.7), (265.7, 267.5)]),
 (53.38, 56.7, [(318.5, 321.8)]),
 (56.7, 61.54, [(321.8, 325.8)]),
 (61.54, 63.88, [(77.3, 79.6)]),
 (63.88, 69.44, [(79.6, 83.2), (84.1, 86.0)]),
 (69.44, 71.72, [(136.0, 138.3)]),
 (71.72, 77.72, [(138.3, 140.0), (143.9, 145.5), (147.3, 150.0)]),
 (77.72, 81.68, [(326.2, 330.0)]),
 (81.68, END, [(335.0, 341.0), (342.2, 343.6)]),
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
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 345.5}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
