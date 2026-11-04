"""Hand-built plan for script-15 (160.033 s recording 3420x1922, 87.677 s voiceover, no clicks log, baked-in recorder zoom -> no zooms/ripples).
One group per narration line, starting on the line's lines.json start; pieces are (src_a, src_b[, fixed_out_dur]) from the 1 s sheets."""
import json
P = 'projects/script-15/work/'
END = 87.677
G = [
 (0, 5.88, [(1.1, 3.4, 2.3), (3.4, 6.4)]),
 (5.88, 9.4, [(6.4, 8.3), (10.4, 11.6)]),
 (9.4, 15.0, [(12.8, 17.8)]),
 (15.0, 17.76, [(22.4, 25.4)]),
 (17.76, 21.76, [(25.9, 30.4)]),
 (21.76, 24.7, [(43.0, 46.2)]),
 (24.7, 31.44, [(46.2, 50.0), (98.0, 100.0)]),
 (31.44, 34.96, [(83.8, 87.0)]),
 (34.96, 39.22, [(100.2, 104.2)]),
 (39.22, 45.54, [(87.8, 92.6)]),
 (45.54, 47.62, [(76.9, 78.9)]),
 (47.62, 52.04, [(80.1, 83.6)]),
 (52.04, 58.64, [(128.8, 133.6), (134.2, 135.4)]),
 (58.64, 62.22, [(135.4, 138.4)]),
 (62.22, 67.34, [(55.0, 59.5)]),
 (67.34, 70.76, [(60.0, 62.7)]),
 (70.76, 76.42, [(65.8, 70.8)]),
 (76.42, 80.8, [(144.0, 148.0)]),
 (80.8, END, [(148.0, 153.5), (156.0, 158.8)]),
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 3420, "height": 1922, "fps": 30, "duration": 160.033}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
