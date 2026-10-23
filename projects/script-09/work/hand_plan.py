"""Hand-built plan for script-09 (baked-in recorder zoom: no zooms/ripples; 401 s of footage for 91.7 s of voiceover)."""
import json
P = 'projects/script-09/work/'
END = 91.672
# (out_start, out_end, [(src_a, src_b)])
G = [
 (0, 7.14, [(0.2, 2.17), (2.17, 4.8), (13.2, 15.6)]),
 (7.14, 10.42, [(15.6, 18.9)]),
 (10.42, 14.12, [(21.4, 22.4), (29.0, 31.7)]),
 (14.12, 17.66, [(31.7, 33.5), (47.5, 49.34)]),
 (17.66, 24.7, [(50.5, 52.4), (64.5, 66.6), (75.0, 78.0)]),
 (24.7, 27.96, [(92.0, 95.3)]),
 (27.96, 32.48, [(99.8, 104.3)]),
 (32.48, 34.58, [(54.4, 56.5)]),
 (34.58, 39.7, [(163.4, 168.5)]),
 (39.7, 43.46, [(180.0, 183.8)]),
 (43.46, 46.54, [(218.8, 221.9)]),
 (46.54, 51.9, [(248.7, 251.4), (251.4, 253.0)]),
 (51.9, 56.32, [(254.8, 256.2), (258.3, 260.6)]),
 (56.32, 62.08, [(279.4, 282.6), (291.0, 293.6)]),
 (62.08, 65.34, [(333.0, 336.0)]),
 (65.34, 68.24, [(336.0, 338.9)]),
 (68.24, 72.76, [(338.6, 340.2), (342.4, 345.6)]),
 (72.76, 75.26, [(349.5, 353.2)]),
 (75.26, 78.5, [(354.6, 357.8)]),
 (78.5, 81.84, [(362.6, 365.9)]),
 (81.84, 87.46, [(371.6, 374.4), (380.6, 383.4)]),
 (87.46, END, [(386.0, 390.2)]),
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
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
