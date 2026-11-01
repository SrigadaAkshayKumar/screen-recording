"""script-09 (232 s Canva mobile-layout take, 95.666 s voiceover, 1920x1080).
One group per narration line, starting on that line's start (lines.json). Footage matched by step
(see output/report.md); static source spans from freezedetect are avoided (<2.5 s output)."""
import json
P = 'projects/script-09/work/'
D = 95.666
L = [0.0, 7.86, 10.46, 15.46, 19.98, 27.72, 32.16, 35.76, 41.02, 47.1, 50.0, 53.38, 59.0, 63.8, 68.24, 72.44, 75.18, 77.9, 85.62, 91.54, D]
# group per line: list of (src_a, src_b) pieces, spread over the line's slot proportionally
G = [
 [(0.6, 3.0), (208.8, 214.26)],            # L1 intro (static home 2.4 s, then phone preview)
 [(12.4, 15.8)],                           # L2 open design / Preview
 [(19.1, 24.1)],                           # L3 mobile preview
 [(36.0, 39.9)],                           # L4 publish panel -> settings
 [(42.43, 47.33), (24.8, 27.7)],           # L5 settings Resize on mobile, reflow in preview
 [(50.3, 53.1), (61.83, 63.4)],            # L6 back to design
 [(123.0, 126.6)],                         # L7 resize text box
 [(126.6, 130.3), (131.67, 133.2)],        # L8 boundaries / spacing
 [(84.0, 90.0)],                           # L9 select + group
 [(96.0, 98.9)],                           # L10 preview again
 [(90.4, 93.8)],                           # L11 avoid grouping whole layout
 [(98.6, 100.6), (102.67, 105.9)],         # L12 related items together
 [(109.0, 112.77), (113.67, 114.7)],       # L13 replace oversized element
 [(155.0, 159.2)],                         # L14 buttons / links
 [(159.2, 161.3), (163.5, 165.6)],         # L15 large image
 [(168.0, 170.7)],                         # L16
 [(173.5, 176.2)],                         # L17
 [(202.6, 210.2)],                         # L18 full-screen phone view
 [(211.2, 217.2)],                         # L19 scroll sections
 [(217.9, 222.0)],                         # L20 closing
]
FIXED = {0: [2.4, None]}  # fixed output length for the static opening piece
segs = []
for i, pieces in enumerate(G):
    o = L[i]; end = L[i + 1]
    fixed = FIXED.get(i, [None] * len(pieces))
    rest = [p for p, f in zip(pieces, fixed) if f is None]
    avail = end - o - sum(f for f in fixed if f)
    tot = sum(b - a for a, b in rest)
    for k, ((a, b), f) in enumerate(zip(pieces, fixed)):
        d = f if f else (b - a) / tot * avail
        o1 = end if k == len(pieces) - 1 else o + d
        segs.append({"src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": round(o1, 3), "mode": "speed", **({"xfade": True} if ((k > 0 or i > 0) and not (k > 0 and a == pieces[k-1][1]) and not (k == 0 and i > 0 and a == G[i-1][-1][1])) else {})})
        o = o1
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.2f}-{s['src_end']:6.2f} {(s['src_end']-s['src_start'])/d:.2f}x")
