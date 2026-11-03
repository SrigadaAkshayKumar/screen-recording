"""Hand-built plan for script-03 (263.2 s Canva business-card bleed take) for 87.34 s of voiceover.
One group per narration line starting on the line start. Pieces are (src_a, src_b[, fixed_out_dur]);
pieces without a fixed duration share the group's remaining time at one common speed.
Source ranges chosen from second-by-second frames (see output/report.md). No zooms/ripples
(recorder zoom is baked in, no click log)."""
import json
P = 'projects/script-03/work/'
END = 87.34
G = [
 (0.0, 5.8, [(0.5, 5.1, 2.3), (6.33, 9.1)]),                              # L1 home screen
 (5.8, 11.64, [(17.93, 23.63)]),                                          # L2 open design
 (11.64, 14.56, [(28.8, 32.4)]),                                          # L3 resize/size
 (14.56, 18.94, [(45.4, 47.77), (69.4, 71.6), (84.3, 85.5)]),             # L4 File>Rulers>print bleed
 (18.94, 21.02, [(58.8, 61.07)]),                                         # L5 show margins
 (21.02, 23.3, [(85.5, 87.7)]),                                           # L6 check edges
 (23.3, 27.38, [(87.7, 89.5), (91.1, 93.0)]),                             # L7 extend shapes
 (27.38, 33.94, [(93.0, 96.0), (101.6, 104.6)]),                          # L8 background rectangle
 (33.94, 39.8, [(112.1, 114.33), (115.27, 118.9)]),                       # L9 text inside margins
 (39.8, 43.52, [(119.7, 122.6)]),                                         # L10
 (43.52, 48.36, [(104.6, 108.57)]),                                       # L11 rectangle
 (48.36, 53.4, [(144.33, 147.8), (148.67, 150.83)]),                      # L12 whole design
 (53.4, 56.22, [(181.0, 184.37)]),                                        # L13 Share > Download
 (56.22, 62.04, [(186.0, 188.9), (189.8, 191.3), (192.73, 195.27)]),      # L14 PDF/Print/Advanced
 (62.04, 66.34, [(198.4, 200.9), (206.8, 209.23)]),                       # L15 crop marks, download
 (66.34, 74.08, [(86.4, 88.9), (228.6, 232.1), (240.6, 242.7)]),          # L16 bleed guides vs crop marks
 (74.08, 76.44, [(216.2, 218.6)]),                                        # L17 downloaded
 (76.44, 80.08, [(224.0, 225.93), (226.9, 228.6)]),                       # L18 open PDF
 (80.08, END, [(247.2, 249.3), (242.7, 247.1)]),                          # L19 inspect
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    free = [p for p in pieces if len(p) == 2]
    sp = sum(p[1]-p[0] for p in free) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        if len(p) > 2: end = t + p[2]
        else: end = t + (p[1]-p[0]) / sp
        if k == len(pieces)-1: end = o1
        s = {"src_start": p[0], "src_end": p[1], "out_start": round(t,3), "out_end": round(end,3), "mode": "speed"}
        if prev_end is not None and abs(p[0]-prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for g in G:
    print(g[0], round(sum(p[1]-p[0] for p in g[2])/(g[1]-g[0]),2))
