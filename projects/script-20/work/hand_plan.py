"""Hand plan for script-20: 314 s zoom-baked recording, 108 s voiceover. Each group fills one
narration interval with moving source pieces at a uniform speed."""
import json, sys
sys.path.insert(0, 'tools')
from plan_builder import plan_hash
P = 'projects/script-20/work/'
END = 108.344
G = [
 (0, 16.5, [(152.5, 164.9)]),
 (16.5, 28.5, [(11.2, 21.2)]),
 (28.5, 33.2, [(22.4, 27.1)]),
 (33.2, 37.1, [(54.3, 58.2)]),
 (37.1, 40.08, [(65.0, 68.1)]),
 (40.08, 45.0, [(79.5, 84.4)]),
 (45.0, 50.26, [(85.3, 91.1)]),
 (50.26, 58.56, [(106.9, 111.3), (113.1, 115.4), (116.7, 118.0)]),
 (58.56, 65.56, [(178.8, 183.3), (184.7, 187.2)]),
 (65.56, 72.1, [(187.2, 190.5), (193.9, 197.3)]),
 (72.1, 82.14, [(200.9, 204.6), (205.5, 207.2), (170.1, 171.9), (172.9, 174.2)]),
 (82.14, 93.98, [(244.7, 249.1), (252.8, 255.4), (272.9, 277.5)]),
 (93.98, 97.16, [(261.0, 264.6)]),
 (97.16, 100.96, [(237.8, 242.8)]),
 (100.96, 103.64, [(286.5, 289.7)]),
 (103.64, END, [(299.5, 303.9), (307.8, 310.1)]),
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
    print(f"{o0:7.2f}-{o1:7.2f} speed {sp:.2f}x")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
plan["generated_hash"] = plan_hash(plan)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
