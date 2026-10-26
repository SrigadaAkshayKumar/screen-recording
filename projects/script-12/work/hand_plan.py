"""Hand-budgeted plan for script-12 (406 s recording, 99.2 s voiceover, baked-in recorder zoom: no zooms/ripples).
One group of moving-window pieces per narration line, each group starting on that line's start."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
D = 99.196
lines = json.load(open(os.path.join(here, "lines.json")))
L = lines["lines"] if isinstance(lines, dict) else lines
starts = [x["start"] for x in L]; starts[0] = 0.0
G = [  # group per line: list of (src_a, src_b)
 [(7.0, 9.4), (12.6, 16.4)],
 [(16.4, 18.2), (19.1, 20.3), (21.7, 23.5)],
 [(24.3, 26.1), (274.2, 275.7)],
 [(41.2, 46.3)],
 [(103.3, 107.0), (114.8, 116.5)],
 [(120.6, 126.0)],
 [(126.0, 130.8)],
 [(133.9, 135.1), (136.4, 139.9)],
 [(143.8, 146.9), (157.4, 159.6)],
 [(163.6, 166.6)],
 [(175.2, 180.0)],
 [(185.7, 188.0), (191.8, 194.1)],
 [(242.5, 244.8)],
 [(244.8, 247.4), (248.2, 251.5)],
 [(263.8, 268.2)],
 [(292.6, 295.0)],
 [(295.0, 297.4), (303.3, 305.7)],
 [(205.6, 208.9)],
 [(316.0, 319.9)],
 [(335.1, 338.1), (355.0, 356.4)],
 [(374.7, 379.9)],
 [(98.7, 101.3), (108.4, 110.7)],
 [(388.9, 391.1)],
 [(397.0, 400.7)],
]
assert len(G) == len(starts), (len(G), len(starts))
segs = []; prev = None
for i, g in enumerate(G):
    o0 = starts[i]; o1 = starts[i + 1] if i + 1 < len(starts) else D
    tot = sum(b - a for a, b in g); o = o0
    print(f"L{i+1:2d} {tot/(o1-o0):.2f}x")
    for j, (a, b) in enumerate(g):
        oe = o1 if j == len(g) - 1 else round(o + (b - a) / tot * (o1 - o0), 3)
        s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": oe}
        if prev is not None and abs(a - prev) > 0.05: s["xfade"] = True
        segs.append(s); prev = b; o = oe
plan = {"output": {"duration": D, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False},
        "notes": ["hand-built by hand_plan.py; recorder zoom is baked in so no zooms/ripples"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
