"""Hand-budgeted plan for script-10 (205.7 s recording, 105.05 s voiceover, 3420x1922; pieces from freezedetect moving windows).
Recorder zoom is baked into the footage -> no zooms/ripples. One group of pieces per narration interval."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
DUR = 105.047
# (interval start in output, [source windows])
G = [
 (0.0,   [(194.57, 198.0), (12.27, 14.77)]),
 (6.1,   [(15.2, 23.7)]),
 (14.06, [(27.33, 29.2), (30.2, 31.23), (41.6, 44.43)]),
 (19.9,  [(45.47, 47.5), (57.6, 61.2)]),
 (25.74, [(63.67, 70.67)]),
 (33.0,  [(126.83, 132.3)]),
 (38.56, [(85.27, 95.5)]),
 (47.94, [(166.83, 170.8), (171.6, 174.6)]),
 (54.48, [(175.0, 182.5)]),
 (61.76, [(152.9, 161.0)]),
 (69.84, [(105.7, 110.2)]),
 (74.32, [(110.4, 112.13), (113.07, 115.73), (119.17, 121.5)]),
 (81.08, [(183.0, 190.4)]),
 (87.38, [(148.03, 151.65)]),
 (91.0,  [(136.63, 141.4)]),
 (95.76, [(194.57, 201.97), (203.77, 205.67)]),
]
segs, first = [], True
for gi, (t0, wins) in enumerate(G):
    t1 = G[gi + 1][0] if gi + 1 < len(G) else DUR
    tot = sum(b - a for a, b in wins)
    sp = tot / (t1 - t0)
    print(f"group {gi} {t0}-{t1} speed {sp:.2f}")
    t = t0
    for wi, (a, b) in enumerate(wins):
        d = (b - a) / sp
        e = t1 if wi == len(wins) - 1 else t + d
        s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3)}
        if not first: s["xfade"] = True
        first = False
        segs.append(s); t = e
plan = {"output": {"duration": DUR, "fps": 30.0, "width": 3420, "height": 1922}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [], "style": {},
        "notes": ["hand-built by hand_plan.py; no zooms/ripples (recorder zoom is baked into the footage)"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
