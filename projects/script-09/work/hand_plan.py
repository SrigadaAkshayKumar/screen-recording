"""Hand-built plan for script-09 (192.8 s take, 97.71 s voiceover, 3420x1922, baked recorder zoom: no zooms/ripples).
Pieces come from the moving windows of the source (freezedetect n=0.003 d=0.8); one group per narration line."""
import json
P = 'projects/script-09/work/'
END = 97.71
G = [
 (0, 7.8, [(0.5, 2.0), (134.3, 136.07), (139.77, 143.0)]),
 (7.8, 10.36, [(9.07, 10.2), (12.07, 12.9)]),
 (10.36, 15.92, [(22.17, 24.63), (30.33, 32.53)]),
 (15.92, 18.16, [(34.3, 36.6)]),
 (18.16, 24.42, [(41.47, 46.93), (47.73, 48.4)]),
 (24.42, 28.96, [(48.4, 52.97)]),
 (28.96, 32.08, [(36.6, 39.8)]),
 (32.08, 39.9, [(56.6, 62.43), (63.57, 64.93)]),
 (39.9, 45.68, [(143.0, 148.47)]),
 (45.68, 50.46, [(126.13, 131.27)]),
 (50.46, 55.48, [(67.9, 71.1), (87.77, 89.6)]),
 (55.48, 59.76, [(102.2, 106.5)]),
 (59.76, 64.86, [(106.5, 109.87), (81.67, 83.4)]),
 (64.86, 67.28, [(85.3, 85.9), (89.6, 91.67)]),
 (67.28, 75.32, [(153.33, 160.4)]),
 (75.32, 81.1, [(161.3, 166.47), (168.43, 169.1)]),
 (81.1, 87.18, [(169.1, 170.77), (123.6, 125.0), (83.4, 84.27), (132.7, 134.3)]),
 (87.18, 93.56, [(174.13, 178.43), (182.2, 184.17)]),
 (93.56, END, [(179.5, 180.5), (185.77, 186.83), (189.97, 190.57), (191.47, 192.8)]),
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
