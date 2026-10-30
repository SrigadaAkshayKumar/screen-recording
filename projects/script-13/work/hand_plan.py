"""Hand-built plan for script-13 (478 s recording, 93.2 s voiceover, baked recorder zoom, no clicks log).
One group per narration line, starting on the line's start; pieces come from the moving windows
(ffmpeg freezedetect n=0.003 d=0.8 on the source). No zooms/ripples."""
import json
P = 'projects/script-13/work/'
END = 93.158
G = [
 (0, [(7.9, 10.4), (21.3, 24.8)]),
 (6.8, [(32.1, 35.4)]),
 (10.1, [(35.4, 37.6), (58.7, 60.6)]),
 (14.12, [(64.3, 66.0)]),
 (15.78, [(77.0, 77.9), (79.5, 82.1)]),
 (20.26, [(84.1, 87.1)]),
 (23.24, [(88.0, 89.0), (90.2, 94.3)]),
 (28.26, [(97.3, 100.6), (106.0, 108.4)]),
 (33.3, [(110.1, 113.3)]),
 (36.46, [(124.4, 125.7), (127.6, 131.5)]),
 (41.66, [(289.8, 292.3), (293.4, 295.0), (299.6, 302.8)]),
 (48.56, [(320.4, 321.9)]),
 (50.16, [(461.3, 465.9)]),
 (54.74, [(465.9, 469.9)]),
 (58.78, [(469.9, 473.0), (474.9, 476.1)]),
 (62.62, [(449.0, 453.9)]),
 (67.32, [(256.8, 260.2), (262.6, 266.5)]),
 (74.66, [(411.5, 415.1)]),
 (78.32, [(417.9, 421.5)]),
 (81.86, [(444.0, 448.2)]),
 (85.86, [(455.3, 458.5), (334.0, 337.7)]),
]
segs, prev_end = [], None
for gi, (o0, pieces) in enumerate(G):
    o1 = G[gi + 1][0] if gi + 1 < len(G) else END
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
