"""Hand-built plan for script-03 (3x3 Instagram grid): each group fills a narration interval with
source pieces at one uniform speed (0.75-1.5x). No zooms/ripples: the recording has baked-in
recorder zoom (docs/lessons.md). Pieces avoid the static spans listed by freezedetect on the source."""
import json
P = 'projects/script-03/work/'
END = 99.799
# (out_start, out_end, [(src_start, src_end), ...])
G = [
 (0, 8.47, [(2.0, 5.8), (14.03, 18.7)]),
 (8.47, 13.75, [(18.7, 24.0)]),
 (13.75, 21.45, [(24.0, 31.9)]),
 (21.45, 24.85, [(44.0, 49.1)]),
 (24.85, 27.48, [(56.7, 60.6)]),
 (27.48, 30.38, [(60.6, 64.9)]),
 (30.38, 34.43, [(128.3, 134.3)]),
 (34.43, 41.67, [(134.3, 141.3)]),
 (41.67, 44.32, [(149.0, 152.9)]),
 (44.32, 50.63, [(161.0, 169.9)]),
 (50.63, 55.44, [(175.3, 180.0), (198.0, 200.5)]),
 (55.44, 61.0, [(216.6, 220.1), (221.0, 225.0)]),
 (61.0, 68.5, [(236.5, 242.8), (271.0, 275.8)]),
 (68.5, 73.47, [(291.6, 298.9)]),
 (73.47, 76.0, [(315.4, 319.0)]),
 (76.0, 81.7, [(326.7, 335.0)]),
 (81.7, 85.7, [(353.1, 359.0)]),
 (85.7, 91.2, [(286.0, 292.4)]),
 (91.2, 96.8, [(246.8, 252.5)]),
 (96.8, END, [(277.5, 281.5)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    T = o1 - o0
    tot = sum(b - a for a, b in pieces)
    t = o0
    for k, (a, b) in enumerate(pieces):
        d = (b - a) / tot * T
        s = {"src_start": a, "src_end": b, "mode": "speed", "out_start": round(t, 3),
             "out_end": o1 if k == len(pieces) - 1 else round(t + d, 3)}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = s["out_end"]
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [], "style": {},
        "notes": ["hand-built by work/hand_plan.py; no zooms/ripples (baked-in recorder zoom)"]}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
