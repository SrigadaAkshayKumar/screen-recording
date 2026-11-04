"""Hand-built plan for script-16 (249.533 s recording 1920x1080, 93.089 s voiceover, no clicks log -> no zooms/ripples).
One group per narration line, starting 0.15 s before the line's lines.json start; pieces are (src_a, src_b[, fixed_out_dur]) from 1 s sheets."""
import json
P = 'projects/script-16/work/'
END = 93.089
G = [
 (0, 5.89, [(57.0, 59.6), (106.9, 109.4)]),
 (5.89, 8.23, [(9.0, 11.4)]),
 (8.23, 14.55, [(17.3, 20.9), (22.4, 26.9)]),
 (14.55, 16.15, [(36.5, 38.3)]),
 (16.15, 22.01, [(39.8, 46.6)]),
 (22.01, 26.25, [(47.0, 52.2)]),
 (26.25, 28.69, [(43.0, 45.2)]),
 (28.69, 32.35, [(56.8, 59.8)]),
 (32.35, 35.37, [(68.4, 71.5)]),
 (35.37, 39.65, [(71.5, 75.8)]),
 (39.65, 45.53, [(82.4, 88.0)]),
 (45.53, 48.23, [(88.0, 90.5)]),
 (48.23, 51.63, [(101.8, 105.0)]),
 (51.63, 56.93, [(106.8, 113.0)]),
 (56.93, 63.51, [(128.4, 134.0)]),
 (63.51, 67.41, [(149.0, 151.2), (158.3, 160.6)]),
 (67.41, 72.75, [(166.8, 168.6), (196.0, 197.4), (207.4, 208.8), (214.8, 216.2)]),
 (72.75, 79.13, [(168.4, 171.3), (172.9, 175.2)]),
 (79.13, 84.31, [(181.4, 186.6)]),
 (84.31, 89.95, [(188.0, 193.6)]),
 (89.95, END, [(200.4, 203.5)]),
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
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 249.533}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
