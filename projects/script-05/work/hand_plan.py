"""Hand-built plan for script-05 (226.2 s Canva faceless-video take, 95.248 s voiceover, 1920x1080, baked recorder zoom, no click log).
One group per narration line (starts on its lines.json start); pieces are (src_a, src_b[, fixed_out_dur]). No zooms/ripples."""
import json, sys
P = 'projects/script-05/work/'
END = 95.248
G = [
 (0, 7.9, [(0.0, 3.4), (14.4, 17.9)]),
 (7.9, 11.58, [(10.3, 14.4)]),
 (11.58, 18.18, [(19.2, 21.8), (26.4, 31.2)]),
 (18.18, 21.16, [(52.8, 56.0)]),
 (21.16, 24.98, [(56.0, 59.8)]),
 (24.98, 27.6, [(59.8, 62.4)]),
 (27.6, 33.56, [(69.6, 75.6)]),
 (33.56, 37.06, [(120.0, 123.5)]),
 (37.06, 39.34, [(79.2, 81.8)]),
 (39.34, 44.94, [(93.6, 99.0)]),
 (44.94, 49.7, [(99.0, 103.8)]),
 (49.7, 51.86, [(216.0, 218.2)]),
 (51.86, 57.18, [(83.0, 88.0)]),
 (57.18, 60.36, [(194.4, 197.6)]),
 (60.36, 66.2, [(146.0, 151.8)]),
 (66.2, 72.12, [(38.3, 44.2)]),
 (72.12, 74.76, [(128.0, 130.6)]),
 (74.76, 78.14, [(160.8, 164.2)]),
 (78.14, 85.32, [(141.6, 148.8)]),
 (85.32, 87.52, [(206.4, 208.6)]),
 (87.52, 92.32, [(208.6, 213.4)]),
 (92.32, END, [(213.4, 216.3)]),
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
