"""Hand-built plan for script-03 (Canva education application; 242 s recording 1920x1080, 101.889 s voiceover,
no clicks log -> no zooms/ripples). One group per narration line starting on that line's start; pieces come
from the moving windows of freezedetect (n=0.003, d=0.8). Static page spans reused cross-faded."""
import json
P = 'projects/script-03/work/'
END = 101.889
G = [
 (0, 5.88, [(12.2, 16.67)]),
 (5.88, 9.24, [(17.5, 20.5)]),
 (9.24, 17.02, [(13.6, 16.7), (17.5, 21.3)]),
 (17.02, 22.82, [(21.2, 24.0), (24.6, 27.0)]),
 (22.82, 27.88, [(28.0, 34.2)]),
 (27.88, 32.76, [(40.0, 45.0)]),
 (32.76, 35.58, [(46.2, 48.9)]),
 (35.58, 42.48, [(49.7, 57.0)]),
 (42.48, 48.24, [(57.8, 63.0)]),
 (48.24, 51.04, [(63.0, 65.8)]),
 (51.04, 56.0, [(59.2, 64.2)]),
 (56.0, 63.26, [(72.2, 74.4), (75.9, 80.0)]),
 (63.26, 68.92, [(80.0, 86.0)]),
 (68.92, 75.5, [(86.8, 95.3)]),
 (75.5, 77.82, [(96.3, 98.6)]),
 (77.82, 82.54, [(98.6, 100.6), (101.2, 104.0)]),
 (82.54, 92.78, [(104.0, 104.7), (112.5, 115.4), (116.6, 119.8), (121.5, 124.3)]),
 (92.78, END, [(194.6, 198.8), (213.8, 218.4)]),
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
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 242.0}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
