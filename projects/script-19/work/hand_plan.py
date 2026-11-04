"""Hand-built plan for script-19 (375.7 s take, 98.352 s voiceover, 1920x1080, baked recorder zoom: no zooms/ripples).
Pieces (a,b) share the group's duration; (a,b,speed) are fixed-speed pieces. Mapped by content, see report."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
G = [
 (0.0, 4.76, [(8.3, 10.3), (10.3, 12.8)]),
 (4.76, 11.5, [(12.8, 14.57), (15.43, 17.5), (21.0, 23.0, 1.0)]),
 (11.5, 17.22, [(31.5, 34.0), (52.0, 54.5), (116.23, 119.0)]),
 (17.22, 20.52, [(91.3, 93.77), (83.93, 85.37)]),
 (20.52, 25.12, [(58.0, 60.17), (61.33, 62.73), (66.7, 68.5)]),
 (25.12, 27.5, [(78.3, 80.7)]),
 (27.5, 30.76, [(141.17, 142.3), (143.7, 146.43)]),
 (30.76, 36.34, [(146.43, 149.23, 1.5), (149.23, 150.93), (152.2, 153.5), (158.93, 160.07)]),
 (36.34, 43.4, [(184.47, 187.23), (192.27, 193.33), (203.97, 205.17), (170.1, 171.4)]),
 (43.4, 46.72, [(221.2, 222.93), (229.3, 230.67)]),
 (46.72, 50.56, [(234.63, 235.87), (239.8, 242.2), (246.2, 247.47)]),
 (50.56, 54.94, [(292.2, 295.2), (271.0, 272.17)]),
 (54.94, 60.46, [(252.5, 254.47), (256.77, 257.93), (259.47, 260.97), (274.63, 276.43)]),
 (60.46, 71.58, [(172.3, 175.0), (177.5, 179.33), (180.93, 182.33), (208.73, 210.23), (211.77, 212.93), (194.37, 195.77)]),
 (71.58, 73.8, [(334.1, 335.7), (339.07, 340.07)]),
 (73.8, 77.58, [(283.1, 284.3), (288.77, 292.2)]),
 (77.58, 82.24, [(295.2, 300.7)]),
 (82.24, 88.38, [(306.3, 310.7, 1.0), (314.77, 316.51)]),
 (88.38, 91.54, [(329.7, 333.27)]),
 (91.54, END, [(352.77, 354.27), (359.13, 360.37), (364.0, 367.3)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum((p[1]-p[0])/p[2] for p in pieces if len(p) == 3)
    var = sum(p[1]-p[0] for p in pieces if len(p) == 2)
    sp = var / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = (b-a)/p[2] if len(p) == 3 else (b-a)/sp
        end = o1 if k == len(pieces)-1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
