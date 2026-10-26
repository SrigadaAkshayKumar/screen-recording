"""Hand-built plan for script-08 (Canva wedding invitation, 249 s take, 3420x1922, baked recorder zoom): no zooms/ripples.
Pieces per narration group from freezedetect moving windows (n=0.003,d=0.8). (a,b) scaled; (a,b,dur) fixed duration."""
import json
P = 'projects/script-08/work/'
END = 93.716
G = [
 (0, 6.38, [(2.0, 4.0, 2.0), (9.6, 13.97)]),
 (6.38, 11.22, [(13.97, 16.33), (23.1, 24.33), (26.8, 27.9)]),
 (11.22, 16.58, [(27.9, 30.5), (36.3, 37.9)]),
 (16.58, 19.6, [(42.47, 45.4)]),
 (19.6, 24.96, [(45.4, 47.1), (48.2, 51.1)]),
 (24.96, 28.8, [(54.7, 57.3), (58.1, 59.4)]),
 (28.8, 36.58, [(59.4, 60.73), (62.7, 65.5), (66.67, 68.03), (75.67, 76.87)]),
 (36.58, 38.72, [(171.6, 173.8)]),
 (38.72, 43.0, [(216.8, 221.0)]),
 (43.0, 46.92, [(224.0, 227.9)]),
 (46.92, 50.62, [(184.9, 188.6)]),
 (50.62, 56.14, [(110.57, 112.47), (113.5, 117.1)]),
 (56.14, 59.06, [(117.1, 120.0)]),
 (59.06, 64.72, [(228.4, 233.5)]),
 (64.72, 69.16, [(120.0, 121.47), (122.27, 125.5)]),
 (69.16, 75.02, [(233.0, 234.37), (236.93, 238.03), (244.33, 246.6)]),
 (75.02, 78.12, [(245.6, 246.6), (133.13, 135.2)]),
 (78.12, 81.54, [(239.13, 241.9)]),
 (81.54, 90.16, [(138.1, 142.33), (143.33, 144.63), (145.73, 147.73), (151.17, 152.47)]),
 (90.16, END, [(154.4, 155.7), (157.67, 160.43)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    src = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = src / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) == 3 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
