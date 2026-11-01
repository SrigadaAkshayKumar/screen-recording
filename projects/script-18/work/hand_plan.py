"""Hand-built plan for script-18 (152 s side-by-side take, 92.648 s voiceover, 3420x1922). Pieces from freezedetect gaps; no holds/zooms; footage reused where the take lacks a step."""
import json
import json
P = 'projects/script-18/work/'
END = 92.648
S = [0, 7.36, 14.38, 19.02, 24.1, 27.72, 32.94, 37.22, 44.48, 53.54, 63.92, 72.48, 78.34, 86.24, END]
W = [
 [(2.2, 8.3)],                                  # 1 intro: home
 [(10.6, 11.8), (15.87, 17.2), (18.2, 21.0)],    # 2-3 create video design
 [(21.0, 24.6)],                                # 4 elements
 [(25.4, 30.5)],                                # 5 frames/grid positioning
 [(46.9, 50.5)],                                # 6 drag videos
 [(57.5, 62.1)],                                # 7 crop
 [(51.6, 54.5), (56.1, 57.5)],                  # 8 timeline
 [(62.1, 69.4)],                                # 9 upper track
 [(86.0, 95.4)],                                # 10-11 trim
 [(96.43, 101.77), (102.87, 105.63), (107.67, 110.5)],  # 12-14 audio
 [(115.0, 123.5)],                              # 15-16 overlap
 [(123.5, 126.1), (127.0, 130.2)],              # 17
 [(68.0, 70.1), (70.93, 77.5)],                 # 18-19 preview/divider
 [(132.83, 137.07), (137.93, 139.5), (141.0, 142.9)],  # 20 download
]
segs, prev_end = [], None
for i, pieces in enumerate(W):
    o0, o1 = S[i], S[i + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    print(i, round(sp, 2))
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
pr = json.load(open(P + 'probe.json'))['recording']
plan = {"output": {"duration": END, "fps": 30.0, "width": pr['width'], "height": pr['height']},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
