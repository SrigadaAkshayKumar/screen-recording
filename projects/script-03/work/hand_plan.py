"""Hand-built plan for script-03: each group fills a narration interval with source pieces at one
uniform speed. No zooms/ripples: the recording has baked-in recorder zoom (docs/lessons.md)."""
import json
P = 'projects/script-03/work/'
END = 91.208
# (out_start, out_end, [(src_start, src_end), ...])
G = [
 (0, 7.22, [(0, 7.0)]),
 (7.22, 9.96, [(9.5, 12.3)]),
 (9.96, 12.74, [(12.4, 15.2)]),
 (12.74, 16.62, [(24.6, 28.3)]),
 (16.62, 22.16, [(31.5, 37.2)]),
 (22.16, 25.36, [(40.4, 43.8)]),
 (25.36, 26.88, [(44.2, 45.6)]),
 (26.88, 31.18, [(46.0, 50.0)]),
 (31.18, 36.8, [(56.4, 62.0)]),
 (36.8, 40.6, [(67.0, 70.6)]),
 (40.6, 45.22, [(72.8, 76.0), (80.4, 82.6)]),
 (45.22, 48.72, [(96.0, 101.0)]),
 (48.72, 54.06, [(101.2, 106.8)]),
 (54.06, 56.26, [(112.0, 114.2)]),
 (56.26, 61.52, [(117.6, 119.0), (122.4, 126.0)]),
 (61.52, 64.84, [(131.2, 134.6)]),
 (64.84, 68.34, [(142.0, 145.5)]),
 (68.34, 73.62, [(156.5, 164.3)]),
 (73.62, 76.0, [(164.3, 166.7)]),
 (76.0, 81.78, [(188.0, 195.5)]),
 (81.78, 87.46, [(223.0, 229.3)]),
 (87.46, END, [(238.8, 242.6)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    T = o1 - o0
    tot = sum(b - a for a, b in pieces)
    t = o0
    for k, (a, b) in enumerate(pieces):
        d = (b - a) / tot * T
        s = {"src_start": a, "src_end": b, "mode": "speed", "out_start": t,
             "out_end": o1 if k == len(pieces) - 1 else t + d}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = s["out_end"]
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [], "style": {},
        "notes": ["hand-built by work/hand_plan.py; no zooms/ripples (baked-in recorder zoom)"]}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
