"""Hand-built plan for script-08 (Canva clickable PDF links). Recording has baked-in recorder zoom: no zooms/ripples.
218 s of footage for a 92.74 s voiceover: pieces per narration group taken from freezedetect moving windows (n=0.003,d=0.8)."""
import json
P = 'projects/script-08/work/'
END = 92.74
G = [
 (0, 5.68, [(3.2, 6.6), (9.0, 10.0)]),
 (5.68, 9.06, [(16.07, 19.2)]),
 (9.06, 13.52, [(19.2, 22.43), (29.67, 31.0)]),
 (13.52, 16.0, [(31.0, 33.37)]),
 (16.0, 20.9, [(36.83, 41.5)]),
 (20.9, 24.7, [(41.5, 43.53), (55.67, 57.5)]),
 (24.7, 30.52, [(57.5, 63.3)]),
 (30.52, 35.98, [(67.1, 73.77)]),
 (35.98, 41.28, [(75.4, 78.2), (80.9, 83.5)]),
 (41.28, 45.98, [(83.5, 87.2), (106.6, 107.6)]),
 (45.98, 49.48, [(120.97, 124.47)]),
 (49.48, 53.18, [(124.47, 128.2)]),
 (53.18, 56.94, [(128.2, 132.0)]),
 (56.94, 61.58, [(132.0, 133.27), (142.47, 144.97), (147.53, 148.8)]),
 (61.58, 63.34, [(150.0, 151.8)]),
 (63.34, 65.9, [(152.2, 154.43)]),
 (65.9, 70.86, [(168.83, 173.27), (174.6, 175.2)]),
 (70.86, 74.7, [(175.2, 176.83), (182.1, 183.6)]),
 (74.7, 78.76, [(156.53, 160.6)]),
 (78.76, 83.92, [(188.87, 194.0)]),
 (83.92, 89.64, [(194.0, 195.47), (197.27, 201.27)]),
 (89.64, END, [(210.93, 214.0)]),
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
