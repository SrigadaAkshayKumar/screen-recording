"""Hand-built plan for script-09 (243.97 s Canva bulk-BG-remover take, 96.381 s voiceover, 17 lines).
One group per narration line; pieces chosen from 0.5-1 s sheets. (a, b) = free piece, (a, b, dur) = fixed out duration."""
import json
P = 'projects/script-09/work/'
END = 96.381
S = [0, 5.9, 9.1, 14.3, 16.5, 22.3, 27.2, 29.1, 35.9, 40.4, 43.7, 50.2, 60.3, 69.2, 76.9, 83.7, 90.3, END]
W = [
 [(123.8, 127.9), (0.6, 4.1, 2.0)],          # L1 result cutouts, then homepage
 [(5.9, 9.1)],                               # L2 homepage -> Projects click ~8.2
 [(12.4, 14.4), (16.9, 18.9), (24.5, 25.8)], # L3 new folder, name+Create, Add new > Upload files
 [(30.6, 32.8)],                             # L4 choose 3 files
 [(34.2, 40.0)],                             # L5 uploaded photos
 [(50.1, 56.2)],                             # L6 listing, hover folder, three-dot menu
 [(66.9, 69.2)],                             # L7 BG Remover click ~67.8
 [(69.2, 74.7)],                             # L8 processing, Edited folder created
 [(84.2, 86.0), (86.0, 88.6, 1.6), (88.6, 89.4)],                           # L9 hover Edited / original folders
 [(89.4, 92.8)],                             # L10 open edited folder
 [(105.3, 109.0), (109.7, 113.0)],           # L11 open a cutout, zoom on hair
 [(148.0, 150.1), (153.3, 160.6)],           # L12 original folder, tick, BG Remover
 [(160.6, 164.2, 2.2), (175.8, 177.2), (119.2, 122.2), (131.0, 133.3)],  # L13 copies added
 [(177.4, 181.0), (184.2, 187.6)],           # L14 profile menu -> plans and pricing
 [(202.9, 209.0)],                           # L15 folder -> All projects designs
 [(213.8, 216.6), (181.0, 184.2)],           # L16 unavailable dialog, plan access
 [(230.0, 235.8)],                           # L17 download
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
