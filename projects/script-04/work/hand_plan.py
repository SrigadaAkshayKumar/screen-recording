"""Hand-built plan for script-04: the recording is in a different order than the narration and has
long idle spells, so each narration line gets source pieces at a uniform speed (0.8-1.5x; typing 2x)."""
import json
P = 'projects/script-04/work/'
END = 105.372
# (out_start, out_end, [(src_a, src_b), ...])
G = [
 (0, 7.06, [(0, 7.06)]),
 (7.06, 12.34, [(14.0, 15.4), (18.9, 21.0), (22.0, 24.5)]),
 (12.34, 14.74, [(24.5, 26.9)]),
 (14.74, 17.92, [(27.0, 30.2)]),
 (17.92, 23.47, [(313.0, 318.5)]),
 (23.47, 30.42, [(319.0, 322.0), (332.4, 335.4)]),
 (30.42, 34.44, [(30.4, 32.6), (340.4, 343.0)]),
 (34.44, 40.06, [(55.4, 61.0)]),
 (40.06, 43.98, [(78.0, 81.9)]),
 (43.98, 45.68, [(82.6, 84.3)]),
 (45.68, 57.78, [(115.8, 120.8), (129.0, 133.6), (149.2, 153.4), (175.8, 180.5)]),
 (57.78, 60.96, [(253.4, 256.6)]),
 (60.96, 64.94, [(258.4, 262.4)]),
 (64.94, 70.42, [(273.0, 279.6)]),
 (70.42, 77.06, [(297.5, 303.9)]),
 (77.06, 79.54, [(308.0, 310.5)]),
 (79.54, 84.56, [(335.4, 340.4)]),
 (84.56, 88.16, [(47.2, 50.4)]),
 (88.16, 94.34, [(344.5, 350.7)]),
 (94.34, 100.14, [(50.6, 55.4)]),
 (100.14, END, [(382.0, 387.2)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
