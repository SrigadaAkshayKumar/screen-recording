"""Hand-built plan for script-06 (234.8 s take, 96.967 s voiceover, 1920x1080). One group per narration line
(L1-L3 merged), pieces chosen from contact sheets and freezedetect (n=0.002, d=0.8)."""
import json
P = 'projects/script-06/work/'
END = 96.967
S = [0, 12.0, 17.2, 21.26, 25.74, 30.58, 36.88, 41.44, 47.32, 50.82, 55.12, 58.9, 63.88, 69.94, 74.32, 79.68, 83.16, 84.72, 88.64, 91.44, END]
# S index: boundaries between groups; groups:
W = [
 [(1.5, 6.3, 2.4), (6.3, 11.4), (12.6, 15.0)],  # L1-3 intro, open design (opening static at 2x)
 [(15.0, 20.2)],               # 4 text box + typing
 [(31.0, 35.1)],               # 5 font
 [(53.0, 57.0), (58.6, 60.7)], # 6 colour
 [(64.9, 69.7)],               # 7 uploads
 [(71.6, 78.5)],               # 8 logo placed
 [(96.2, 100.8)],              # 9 position
 [(80.0, 86.4)],               # 10 transparency
 [(102.3, 105.8)],             # 11 30 %
 [(120.0, 124.3)],             # 12 rotate
 [(125.5, 129.3)],             # 13 smaller
 [(149.5, 154.5)],             # 14 copy to another design
 [(157.6, 161.3, 'H1.1')],    # 15 separate design
 [(164.0, 167.9)],             # 16 separate page
 [(175.6, 181.0)],             # 17 share/download
 [(181.8, 185.3)],             # 18 paid plan
 [(191.3, 192.7)],             # 19 distinction
 [(217.9, 221.8)],             # 20 element transparency
 [(194.4, 197.0)],             # 21 transparent bg
 [(226.7, 232.8)],             # 22 download
]
# group 1 spans out 0-12.0 ; S has 21 entries -> 20 groups
segs, prev_end = [], None
for i, pieces in enumerate(W):
    o0, o1 = S[i], S[i + 1]
    fixed = sum(p[2] for p in pieces if len(p) > 2 and not isinstance(p[2], str))
    hold = sum(float(p[2][1:]) for p in pieces if len(p) > 2 and isinstance(p[2], str))
    free = sum(p[1] - p[0] for p in pieces if len(p) == 2 or isinstance(p[2], str))
    sp = free / (o1 - o0 - fixed - hold)
    print(i + 1, round(sp, 2))
    t = o0
    for k, pc in enumerate(pieces):
        a, b = pc[0], pc[1]
        if len(pc) > 2 and not isinstance(pc[2], str):
            end = t + pc[2]
        else:
            end = t + (b - a) / sp
        if k == len(pieces) - 1 and not (len(pc) > 2 and isinstance(pc[2], str)):
            end = o1
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
        if len(pc) > 2 and isinstance(pc[2], str):
            h = float(pc[2][1:])
            segs.append({"src_start": b, "src_end": b, "out_start": round(t, 3), "out_end": round(t + h, 3), "mode": "hold"})
            t += h
pr = json.load(open(P + 'probe.json'))['recording']
plan = {"output": {"duration": END, "fps": 30.0, "width": pr['width'], "height": pr['height']},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
