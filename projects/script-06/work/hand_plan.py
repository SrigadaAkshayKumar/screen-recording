"""Hand-built plan for script-06 (234.8 s take, 93.317 s voiceover, 19 lines, 1920x1080).
One group per narration line; pieces chosen from 1 s contact sheets (see output/report.md table)."""
import json
P = 'projects/script-06/work/'
END = 93.317
S = [0, 5.4, 8.0, 13.4, 17.4, 21.9, 25.8, 33.1, 37.7, 43.5, 47.0, 51.3, 55.1, 60.0, 66.1, 75.9, 78.7, 84.8, 87.6, END]
W = [
 [(109.6, 113.4), (3.9, 5.8)],                      # L1 intro: faded logo watermark, then blank page
 [(5.8, 8.3)],                                      # L2 open design (page click 6.3)
 [(8.3, 10.2), (13.5, 15.3), (19.8, 22.8)],         # L3 T, text box, add heading, typing
 [(31.5, 36.6)],                                    # L4 font
 [(52.6, 58.4)],                                    # L5 colour light -> dark grey
 [(68.0, 73.5)],                                    # L6 uploads
 [(73.6, 81.0)],                                    # L7 logo placed
 [(96.2, 101.5)],                                   # L8 position
 [(80.6, 85.4)],                                    # L9 select, transparency
 [(103.2, 107.2)],                                  # L10 slider ~30%
 [(120.8, 125.0)],                                  # L11 rotate
 [(116.0, 119.8)],                                  # L12 signature (nearest)
 [(145.6, 151.8)],                                  # L13 copy logo
 [(152.0, 153.8), (157.7, 161.3)],                  # L14 separate design
 [(164.4, 167.8), (175.4, 177.0), (178.4, 181.0), (191.2, 194.7)],  # L15 separate page, share, download, transparent bg
 [(194.7, 196.9)],                                  # L16 paid plan notice
 [(216.0, 221.0)],                                  # L17 element transparency
 [(228.5, 230.9)],                                  # L18 transparent background on
 [(204.2, 206.6), (229.7, 231.8)],                  # L19 download PNG / JPG
]
assert len(W) == len(S) - 1
segs, prev_end = [], None
for i, pieces in enumerate(W):
    o0, o1 = S[i], S[i + 1]
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    free = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = free / (o1 - o0 - fixed)
    print('L%d' % (i + 1), round(sp, 2), [round(p[1] - p[0], 1) for p in pieces])
    t = o0
    for k, pc in enumerate(pieces):
        a, b = pc[0], pc[1]
        end = t + (pc[2] if len(pc) > 2 else (b - a) / sp)
        if k == len(pieces) - 1:
            end = o1
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
pr = json.load(open(P + 'probe.json'))['recording']
plan = {"output": {"duration": END, "fps": 30.0, "width": pr['width'], "height": pr['height']},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
