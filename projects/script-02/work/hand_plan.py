"""Hand-built plan for script-02 (315 s recording for a 105 s voiceover, recorder zoom baked in: no zooms/ripples).
Each group fills one narration interval with source pieces chosen where the picture moves (see report).
A piece is (src_a, src_b) or (src_a, src_b, speed); pieces without a speed share the rest of the interval."""
import json
P = 'projects/script-02/work/'
END = 105.372
G = [
 (18.84, [(4.5, 6.2, .75), (12.8, 14.6, .75), (6.2, 7.9, .75), (14.8, 16.6, .75), (7.9, 9.2, .75), (16.8, 18.6, .75),
          (10.7, 12.8, .75), (18.2, 20.2)]),
 (21.56, [(22.6, 23.7), (28.5, 30.0)]),
 (25.52, [(33.5, 38.0)]),
 (29.38, [(45.0, 49.6)]),
 (35.66, [(50.0, 55.3), (64.7, 66.8)]),
 (40.86, [(118.0, 121.2), (95.5, 97.7)]),
 (43.2, [(134.8, 137.2)]),
 (46.88, [(147.5, 151.2)]),
 (49.9, [(157.4, 160.4)]),
 (54.8, [(172.0, 177.0)]),
 (58.72, [(177.0, 181.0)]),
 (69.94, [(188.7, 195.0), (198.2, 202.8)]),
 (76.8, [(211.7, 218.5)]),
 (82.06, [(218.5, 221.0), (228.8, 232.0)]),
 (87.94, [(237.5, 242.0), (248.5, 250.0)]),
 (91.86, [(250.0, 253.9)]),
 (98.2, [(254.0, 262.0)]),
 (101.46, [(279.5, 283.0)]),
 (END, [(299.0, 301.3), (305.0, 306.6)]),
]
segs, prev_end, o0 = [], None, 0.0
for o1, pieces in G:
    fixed = sum((p[1] - p[0]) / p[2] for p in pieces if len(p) == 3)
    free = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = free / (o1 - o0 - fixed) if free else 1
    t = o0
    for k, p in enumerate(pieces):
        d = (p[1] - p[0]) / (p[2] if len(p) == 3 else sp)
        end = o1 if k == len(pieces) - 1 else t + d
        segs.append({"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed",
                     **({"xfade": True} if prev_end is not None and abs(p[0] - prev_end) > 0.002 else {})})
        prev_end, t = p[1], end
    print(f"{o0:6.2f}-{o1:6.2f} {[(round((s['src_end']-s['src_start'])/(s['out_end']-s['out_start']),2)) for s in segs[-len(pieces):]]}")
    o0 = o1
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
