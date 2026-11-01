"""Hand-built plan for script-12 (124.4 s Canva jacket-recolor take, 95.06 s voiceover, 3420x1922, baked recorder zoom).
One group per narration line, pieces chosen from non-static spans (freezedetect n=0.003 d=0.8)."""
import json
P = 'projects/script-12/work/'
END = 95.062
STARTS = [0,6.76,10.76,18.1,22.58,26.16,32.66,39.24,41.98,46.0,50.18,57.68,61.92,67.14,69.84,74.12,82.76,88.0,END]
PIECES = [
 [(71.27, 77.0)],                                  # 1 intro: jacket + sliders moving
 [(30.0, 31.93), (33.2, 35.5)],                    # 2 select photo, Edit
 [(36.77, 38.4), (88.0, 93.6)],                    # 3 Adjust, Area selection
 [(38.4, 40.4), (42.2, 44.53)],                    # 4 scroll to colour, swatch
 [(45.9, 48.4), (50.13, 51.0)],                    # 5 hue
 [(54.47, 60.6)],                                  # 6 saturation / brightness
 [(63.57, 64.73), (67.67, 69.63), (71.27, 74.5)],  # 7 small changes
 [(74.5, 77.0)],                                   # 8 zoom edges
 [(79.33, 80.63), (81.43, 84.0)],                  # 9 other objects
 [(90.5, 94.7)],                                   # 10 refine area
 [(98.77, 100.07), (101.33, 102.6), (104.9, 108.83)], # 11 white/dark
 [(33.2, 35.5), (36.77, 38.4)],                    # 12 Magic Edit
 [(45.9, 48.4), (50.13, 52.43)],                   # 13 describe change to blue
 [(84.0, 86.8)],                                   # 14 part tutorials skip
 [(71.27, 75.3)],                                  # 15 related shades
 [(45.9, 48.4), (50.13, 52.43), (54.47, 57.5)],    # 16 hue recolor
 [(81.43, 82.8), (82.8, 86.8)],                    # 17 compare
 [(114.0, 117.67), (118.57, 120.7), (121.5, 122.7)], # 18 download
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
