"""Hand-budgeted plan for script-10 (300 s recording, 89.1 s voiceover; pieces from freezedetect moving windows).
Recorder zoom is baked into the footage -> no zooms/ripples."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
DUR = 89.118
# (src_a, src_b, speed)
P = [
 (0.0, 2.97, .75), (10.93, 14.9, 1), (22.03, 25.6, 1), (28.3, 32.83, 1),
 (91.77, 93.77, 1), (73.4, 83.1, 1), (136.8, 145.0, 1), (110.4, 111.97, 1), (116.03, 117.3, 1),
 (128.6, 133.5, 1), (165.1, 168.8, 1), (169.8, 172.0, 1), (175.6, 177.6, 1),
 (178.7, 181.2, 1), (184.8, 193.5, 1), (199.2, 204.0, 1), (206.1, 210.6, 1.15),
 (221.0, 223.9, 1), (225.7, 227.6, 1), (228.9, 231.2, 1), (237.9, 240.5, 1), (241.7, 244.5, 1),
 (246.7, 248.7, 1), (251.5, 253.4, 1), (263.5, 265.8, 1),
]
segs, t = [], 0.0
for i, (a, b, sp) in enumerate(P):
    d = (b - a) / sp
    if i == len(P) - 1:
        d = DUR - t; b = a + d * sp
    s = {"mode": "speed", "src_start": a, "src_end": round(b, 3), "out_start": round(t, 3), "out_end": round(t + d, 3)}
    if i: s["xfade"] = True
    segs.append(s); t += d
print("total", t)
plan = {"output": {"duration": DUR, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [], "style": {},
        "notes": ["hand-built by hand_plan.py; no zooms/ripples (recorder zoom is baked into the footage)"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
