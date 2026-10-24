"""Hand-built plan for script-13 (263 s recording, 83.7 s voiceover, baked recorder zoom, no clicks log).
Each group fills one narration interval with source pieces taken from the moving windows
(ffmpeg freezedetect n=0.003 d=0.8 on the source). No zooms/ripples."""
import json
P = 'projects/script-13/work/'
END = 83.731
G = [
 (0, 6.02, [(3.1, 6.17), (12.4, 14.63)]),
 (6.02, 10.12, [(15.2, 17.2), (24.5, 27.47)]),
 (10.12, 15.58, [(39.67, 46.0)]),
 (15.58, 22.58, [(57.0, 60.6), (64.4, 69.4)]),
 (22.58, 26.0, [(70.9, 73.67)]),
 (26.0, 28.28, [(83.0, 85.4)]),
 (28.28, 31.62, [(98.43, 101.5)]),
 (31.62, 36.82, [(103.4, 105.93), (151.0, 154.5)]),
 (36.82, 42.28, [(164.13, 168.6)]),
 (42.28, 45.88, [(175.4, 179.4)]),
 (45.88, 48.16, [(183.9, 186.2)]),
 (48.16, 52.78, [(192.5, 196.07), (203.07, 205.37)]),
 (52.78, 58.38, [(213.9, 218.5), (228.9, 231.0)]),
 (58.38, 60.88, [(122.8, 125.5)]),
 (60.88, 67.56, [(125.5, 131.4), (132.3, 133.57)]),
 (67.56, 71.74, [(134.97, 137.3), (234.53, 235.83), (247.37, 248.37)]),
 (71.74, 74.64, [(240.53, 243.5)]),
 (74.64, 78.1, [(243.5, 247.37)]),
 (78.1, END, [(250.53, 254.63), (255.6, 258.6)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
