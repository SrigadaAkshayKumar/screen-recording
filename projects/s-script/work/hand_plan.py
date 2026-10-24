"""Hand-built plan for s-script (133.5 s recording with baked-in recorder zoom, 91.2 s voiceover: no zooms/ripples).
Pieces come from freezedetect (n=0.003, d=0.8) moving windows of the source; a third tuple item fixes a piece's
output duration (used for static source played at <= 1.5x). One group per narration line, starting on its line start."""
import json
P = 'projects/s-script/work/'
END = 91.208
G = [
 (0, 7.22, [(0.0, 4.3, 2.4), (4.3, 5.57), (120.83, 123.3)]),
 (7.22, 17.2, [(6.67, 7.93), (8.0, 9.9, 1.4), (10.37, 14.7), (14.9, 17.1, 1.6)]),
 (17.2, 22.84, [(18.1, 20.47), (21.5, 22.9), (23.0, 24.7, 1.0), (27.47, 29.5)]),
 (22.84, 25.36, [(34.1, 37.1)]),
 (25.36, 26.88, [(38.33, 39.9)]),
 (26.88, 31.18, [(39.9, 42.03), (43.5, 45.97)]),
 (31.18, 36.8, [(45.97, 47.87, 1.4), (47.87, 49.2), (50.1, 52.3)]),
 (36.8, 40.6, [(52.3, 56.1)]),
 (40.6, 45.22, [(60.5, 66.83)]),
 (45.22, 48.72, [(74.77, 78.27)]),
 (48.72, 54.06, [(78.27, 82.97)]),
 (54.06, 56.26, [(86.67, 88.9)]),
 (56.26, 61.52, [(91.67, 96.67)]),
 (61.52, 64.84, [(100.0, 103.3)]),
 (64.84, 68.34, [(103.3, 104.37), (106.23, 108.23), (109.1, 109.6)]),
 (68.34, 73.62, [(109.6, 112.2), (113.27, 115.67)]),
 (73.62, 76.0, [(123.3, 125.3)]),
 (76.0, 81.78, [(67.8, 72.6)]),
 (81.78, 87.46, [(125.3, 129.63)]),
 (87.46, END, [(129.7, 132.63), (132.63, 133.45)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    sp = sum(p[1] - p[0] for p in pieces if len(p) == 2) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) > 2 else (b - a) / sp
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
json.dump({"recording": {"width": 3420, "height": 1922, "fps": 30, "duration": 133.533}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
