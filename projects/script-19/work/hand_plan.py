"""Hand-built plan for script-19 (159 s take, 101.05 s voiceover, baked recorder zoom: no zooms/ripples).
Moving windows (freezedetect n=0.003 d=0.8) mapped to narration lines by topic; one group per line (or pair)."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
G = [
 (0, 8.22, [(0.0, 1.5), (3.23, 5.2), (44.27, 48.0)]),
 (8.22, 15.56, [(8.77, 10.9), (12.5, 15.8), (18.03, 20.3)]),
 (15.56, 20.02, [(32.63, 33.83), (36.33, 38.57)]),
 (20.02, 27.32, [(22.9, 28.6)]),
 (27.32, 29.56, [(28.6, 29.57), (44.27, 45.4)]),
 (29.56, 33.34, [(66.0, 70.0)]),
 (33.34, 36.42, [(75.47, 77.67), (78.77, 80.0)]),
 (36.42, 38.7, [(80.5, 82.8)]),
 (38.7, 45.6, [(82.8, 85.97), (100.5, 101.0), (103.73, 106.0)]),
 (45.6, 48.76, [(93.4, 96.73)]),
 (48.76, 51.84, [(103.73, 106.8)]),
 (51.84, 56.16, [(106.8, 111.0)]),
 (56.16, 60.08, [(111.0, 113.93), (115.43, 116.5)]),
 (60.08, 63.64, [(116.5, 119.23), (120.1, 121.0)]),
 (63.64, 67.82, [(121.0, 122.4), (127.13, 130.37)]),
 (67.82, 70.5, [(136.23, 138.9)]),
 (70.5, 74.14, [(141.87, 143.17), (143.97, 145.17), (130.37, 131.33)]),
 (74.14, 79.04, [(52.2, 56.4)]),
 (79.04, 83.12, [(107.0, 111.0)]),
 (83.12, 90.16, [(120.1, 122.4), (127.13, 130.37), (131.33, 132.93)]),
 (90.16, 94.2, [(132.93, 135.37), (136.23, 138.0)]),
 (94.2, 95.72, [(137.9, 139.1)]),
 (95.72, END, [(145.17, 149.97), (152.0, 152.5)]),
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
plan = {"output": {"duration": END, "fps": 30.0, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
