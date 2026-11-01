"""Hand-built plan for script-01 (169 s recording 1920x1080, 95.991 s voiceover, WebP export take).
One group per narration line; pieces share the group's speed; cross-fade at every source jump.
Windows come from moving gaps of freezedetect n=0.002 d=0.8 on the source (see sync-notes.md)."""
import json
P = 'projects/script-01/work/'
END = 95.991
B = [0, 6.3, 9.9, 17.7, 21.4, 25.1, 31.0, 35.9, 37.9, 43.0, 48.0, 53.3, 58.8, 61.2, 66.1, 68.9, 72.5, 80.5, 86.3, 90.4, END]
S = [
 [(1.0, 4.13), (16.73, 18.0), (18.93, 19.43)],       # L1 intro
 [(12.87, 15.73)],                                   # L2 open design
 [(29.6, 37.4)],                                     # L3 dimensions
 [(45.4, 49.1)],                                     # L4 share, download
 [(49.2, 53.0)],                                     # L5 file type webp
 [(53.0, 56.3), (75.1, 77.8)],                       # L6
 [(37.4, 38.4), (29.6, 31.6), (84.5, 85.8)],         # L7
 [(38.4, 40.4)],                                     # L8 page
 [(83.9, 86.5), (40.4, 42.0)],                       # L9 size/quality
 [(86.5, 87.8), (98.1, 101.0)],                       # L10 quality
 [(96.8, 98.1), (98.1, 102.1)],                      # L11 transparent
 [(33.0, 38.4)],                                     # L12 remove bg
 [(113.07, 116.2)],                                  # L13 download
 [(120.87, 124.3), (140.0, 141.5)],                  # L14 check
 [(141.5, 144.3)],                                   # L15
 [(144.3, 147.9)],                                   # L16
 [(147.9, 155.9)],                                   # L17
 [(155.9, 161.7)],                                   # L18
 [(49.2, 53.0)],                                     # L19
 [(163.0, 168.6)],                                   # L20
]
segs, prev = [], None
for k, pieces in enumerate(S):
    o0, o1 = B[k], B[k + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for j, (a, b) in enumerate(pieces):
        e = o1 if j == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b; t = e
    print(f"L{k+1:2d} {o0:7.2f}-{o1:7.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
