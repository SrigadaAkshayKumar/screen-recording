"""Hand-built plan for script-14 (125 s embed-video take, 91.672 s voiceover, 3420x1922). One group per narration
line (or pair) starting on its lines.json start; pieces from non-static footage (freezedetect n=0.002 d=0.8 gaps).
Piece = (src_a, src_b). No holds/zooms. Footage reused where the take lacks a step (see output/report.md)."""
import json
P = 'projects/script-14/work/'
END = 91.672
S = [0, 8.4, 18.0, 22.38, 29.76, 34.04, 37.02, 40.66, 46.86, 52.3, 63.76, 70.48, 75.96, 80.3, 84.52, END]
W = [
 [(73.4, 75.77), (81.4, 86.0)],               # 1 intro: video + heading on page
 [(26.0, 33.5), (36.0, 38.5)],                # 2 copy share link, back to Canva
 [(62.0, 65.8)],                              # 3 paste link, add to design
 [(66.0, 69.4), (70.2, 72.6), (73.4, 74.9)],  # 4 placed, resize
 [(86.0, 89.17), (91.2, 92.2)],               # 5 proportions
 [(95.1, 97.5)],                              # 6 playback
 [(97.5, 100.5)],                             # 7
 [(100.5, 106.0)],                            # 8
 [(24.2, 29.5)],                              # 9-10 hosted elsewhere (YouTube)
 [(111.4, 113.3), (114.9, 124.9)],            # 11-12 MP4 / download
 [(36.5, 41.5), (49.47, 51.8)],               # 13 uploads (borrowed apps panel)
 [(66.0, 69.4), (70.2, 72.6)],                # 14 placed clip
 [(95.1, 99.0)],                              # 15 test playback
 [(99.0, 103.0)],                             # 16
 [(103.0, 108.4), (111.4, 113.0)],            # 17
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
