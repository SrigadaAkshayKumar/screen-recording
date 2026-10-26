"""Hand-built plan for script-04 (new 188 s take, 95.48 s voiceover, recording 3420x1922). Pieces come
only from moving windows (freezedetect n=0.003 d=0.8 on the source), one group per narration line
starting on its lines.json start, 0.75-1.1x. No holds, zooms or ripples."""
import json
P = 'projects/script-04/work/'
END = 95.48
G = [
 (0, 6.44, [(56.13, 57.53), (60.47, 61.83), (63.67, 67.7)]),
 (6.44, 9.06, [(30.93, 31.83), (38.93, 40.2)]),
 (9.06, 14.76, [(8.93, 14.0)]),
 (14.76, 22.22, [(14.0, 15.4), (17.5, 21.6), (22.47, 23.47)]),
 (22.22, 24.16, [(24.47, 26.4)]),
 (24.16, 30.42, [(26.4, 27.2), (28.13, 29.4), (40.9, 44.0)]),
 (30.42, 35.3, [(44.0, 47.2), (53.57, 55.0)]),
 (35.3, 39.92, [(85.43, 87.6), (89.7, 92.4)]),
 (39.92, 43.4, [(32.87, 36.35)]),
 (43.4, 48.86, [(93.4, 96.33), (97.47, 99.57)]),
 (48.86, 55.66, [(69.3, 71.07), (77.93, 83.07)]),
 (55.66, 61.36, [(131.27, 133.63), (136.17, 138.47)]),
 (61.36, 64.32, [(100.67, 103.33)]),
 (64.32, 71.02, [(104.93, 106.7), (109.87, 113.03), (118.27, 119.6)]),
 (71.02, 73.44, [(119.6, 121.53)]),
 (73.44, 76.56, [(123.2, 126.0)]),
 (76.56, 83.78, [(126.0, 129.37), (162.13, 165.5)]),
 (83.78, 87.94, [(170.03, 172.0), (176.53, 178.9)]),
 (87.94, 91.5, [(181.87, 182.93), (183.97, 185.77)]),
 (91.5, END, [(165.5, 168.1), (186.63, 188.0)]),
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
plan = {"output": {"duration": END, "fps": 30.0, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
