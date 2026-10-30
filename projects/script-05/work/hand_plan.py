"""Hand-built plan for script-05 (new 82.6 s take, 98.8 s voiceover, baked recorder zoom, no click log).
One group per narration line (starts on its lines.json start); pieces are (src_a, src_b[, fixed_out_dur]).
No zooms/ripples. Footage is shorter than the voiceover, so some moving windows are reused (cross-faded)."""
import json, sys
sys.path.insert(0, 'tools')
import check
P = 'projects/script-05/work/'
lines = json.load(open(P + 'lines.json'))
END = 98.824
G = [
 (0, 6.62, [(6.9, 9.2, 2.4), (9.2, 12.4)]),
 (6.62, 11.4, [(12.4, 13.07), (13.07, 14.03), (14.03, 16.0)]),
 (11.4, 13.48, [(16.0, 17.8)]),
 (13.48, 18.66, [(17.8, 20.2), (21.8, 23.1), (23.1, 24.9)]),
 (18.66, 22.82, [(32.27, 35.7)]),
 (22.82, 28.42, [(36.78, 41.27)]),
 (28.42, 33.42, [(41.27, 45.9)]),
 (33.42, 40.68, [(45.9, 48.1, 2.2), (48.1, 49.5), (49.5, 52.3)]),
 (40.68, 44.0, [(60.4, 63.7)]),
 (44.0, 47.04, [(63.7, 66.7)]),
 (47.04, 52.28, [(66.7, 68.1), (68.1, 69.47), (69.47, 71.77)]),
 (52.28, 55.96, [(74.07, 77.5)]),
 (55.96, 61.12, [(77.5, 78.73), (78.73, 79.53), (79.53, 82.0)]),
 (61.12, 64.88, [(55.1, 56.37), (48.1, 49.5), (50.67, 51.4)]),
 (64.88, 67.54, [(14.03, 16.6)]),
 (67.54, 71.22, [(9.2, 12.4)]),
 (71.22, 76.28, [(37.97, 42.23)]),
 (76.28, 80.68, [(32.27, 35.6)]),
 (80.68, 84.43, [(43.3, 46.4)]),
 (84.43, 89.2, [(36.78, 41.0)]),
 (89.2, 93.28, [(18.2, 20.2), (21.8, 23.4)]),
 (93.28, END, [(74.07, 76.5), (79.53, 82.5)]),
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
plan = {"output": {"duration": END, "fps": 30.0, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
