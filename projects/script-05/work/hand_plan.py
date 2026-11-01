"""Hand-built plan for script-05 (195 s Canva video-blend/transparency take, 96.363 s voiceover, 1920x1080, no click log).
One group per narration line (starts on its lines.json start); pieces are (src_a, src_b[, fixed_out_dur]). No zooms/ripples.
Windows come from freezedetect (n=0.002, d=0.8) gaps on the source."""
import json
P = 'projects/script-05/work/'
END = 96.363
G = [
 (0, 8.96, [(0.0, 2.0, 2.0), (14.2, 21.37)]),
 (8.96, 13.04, [(27.2, 31.63)]),
 (13.04, 19.38, [(35.8, 42.67)]),
 (19.38, 22.94, [(54.9, 58.5)]),
 (22.94, 27.46, [(61.2, 65.23)]),
 (27.46, 32.44, [(68.3, 70.3), (80.7, 83.0)]),
 (32.44, 34.88, [(83.0, 84.97)]),
 (34.88, 40.44, [(182.57, 184.2), (185.57, 188.4)]),
 (40.44, 45.9, [(176.5, 181.7)]),
 (45.9, 51.62, [(98.47, 100.57), (102.6, 105.8)]),
 (51.62, 57.04, [(120.17, 125.6)]),
 (57.04, 60.36, [(125.6, 127.1), (128.0, 129.8)]),
 (60.36, 65.1, [(114.63, 119.3)]),
 (65.1, 68.76, [(148.17, 151.93)]),
 (68.76, 71.36, [(165.63, 168.2)]),
 (71.36, 75.5, [(81.0, 84.97)]),
 (75.5, 79.21, [(168.2, 171.9)]),
 (79.21, 82.62, [(174.43, 177.8)]),
 (82.62, 90.5, [(44.73, 49.57), (50.7, 53.77)]),
 (90.5, END, [(102.6, 108.4)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    sp = sum(p[1] - p[0] for p in pieces if len(p) == 2) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
