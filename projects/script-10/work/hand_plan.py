"""Hand-budgeted plan for script-10 (346 s recording, 98.2 s voiceover; plan_builder cannot slow below 1x)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
# (src_a, src_b, out_a, out_b, xfade)
Q = [
 (2.2, 7.9, 0.0, 6.8, False), (9.8, 13.5, 6.8, 11.0, True), (334.9, 339.0, 11.0, 15.98, True),
 (26.1, 33.0, 15.98, 20.74, True), (35.0, 38.0, 20.74, 23.1, True), (42.3, 44.0, 23.1, 24.94, True),
 (44.0, 46.8, 24.94, 27.7, False), (49.2, 53.2, 27.7, 30.78, True), (58.3, 62.9, 30.78, 34.66, True),
 (87.0, 91.8, 34.66, 38.76, True), (98.0, 99.8, 38.76, 40.5, True), (103.7, 109.6, 40.5, 45.5, True),
 (134.0, 140.0, 45.5, 48.9, True), (142.0, 146.0, 48.9, 52.0, True), (161.0, 163.0, 52.0, 54.0, True),
 (190.0, 193.0, 54.0, 58.0, True),
 (223.0, 227.0, 58.0, 60.9, True), (236.0, 238.6, 60.9, 62.84, True), (241.5, 248.0, 62.84, 69.08, True),
 (277.2, 280.8, 69.08, 72.0, True), (285.2, 288.5, 72.0, 75.4, True), (294.4, 300.0, 75.4, 81.78, True),
 (300.0, 302.0, 81.78, 83.78, False), (311.0, 315.2, 83.78, 88.0, True), (324.2, 327.8, 88.0, 91.62, True),
 (332.4, 334.5, 91.62, 93.78, True), (227.6, 232.0, 93.78, 98.22, True),
]
segs = []
for a, b, oa, ob, x in Q:
    s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": oa, "out_end": ob}
    if x: s["xfade"] = True
    segs.append(s)
plan = {"output": {"duration": 98.22, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [], "style": {},
        "notes": ["hand-built by hand_plan.py; no zooms/ripples (recorder zoom is baked into the footage)"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
