"""Hand-built plan for script-12 (245.6 s take, 90.651 s voiceover, 1920x1080, baked recorder zoom).
One group per narration line, pieces chosen from non-static spans (freezedetect) by what they show (see output/report.md)."""
import json
P = 'projects/script-12/work/'
END = 90.651
STARTS = [0,7.0,10.82,16.28,21.68,26.78,32.86,35.96,41.22,47.32,49.7,54.66,57.2,61.14,64.72,67.64,72.88,80.56,85.8,END]
PIECES = [
 [(186.8, 189.8), (190.7, 194.1)],   # 1 result: text circling object
 [(12.7, 17.5)],                     # 2 Create > Videos > blank video design
 [(44.0, 50.0)],                     # 3 search graphics for object
 [(64.5, 68.5), (78.3, 80.3)],       # 4 text panel, add text box
 [(82.0, 88.0)],                     # 5 font / colour toolbar
 [(93.0, 99.5)],                     # 6 Effects > Curve
 [(99.5, 102.5)],                    # 7 adjust curve
 [(136.0, 141.4)],                   # 8 Animate > Create an animation
 [(142.7, 147.4)],                   # 9 drag the route
 [(153.0, 156.0)],                   # 10 release / preview path
 [(158.9, 160.2), (173.2, 177.0)],   # 11 movement settings / redraw
 [(166.1, 168.4)],                   # 12 click Done
 [(212.3, 216.2)],                   # 13 timeline
 [(179.0, 182.1)],                   # 14 central object
 [(217.2, 220.0)],                   # 15 "part tutorials skip"
 [(105.9, 108.9), (110.3, 112.5)],   # 16 curve shapes text
 [(130.1, 132.2), (133.6, 134.9), (118.7, 121.5)], # 17 path moves whole box
 [(190.7, 194.1), (195.1, 197.4)],   # 18 route outside edges
 [(229.0, 231.5), (236.5, 239.5)],   # 19 preview + download
]
segs, prev_end = [], None
for i, pieces in enumerate(PIECES):
    o0, o1 = STARTS[i], STARTS[i + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"line {i+1:2d} {o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [{"out_t": 43.5, "x": 1000, "y": 480, "scale": 1.7, "in": 0.6, "hold": 3.0, "out": 0.6}],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
