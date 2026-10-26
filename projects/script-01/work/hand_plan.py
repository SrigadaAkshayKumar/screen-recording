"""Hand-built plan for script-01 (144.8 s recording 3420x1922, 93.16 s voiceover; baked-in recorder zoom: no zooms/ripples).
One group per narration line: pieces share the group's speed; cross-fade at every source jump.
Pieces come from the moving windows of freezedetect n=0.003 d=0.8 on the source."""
import json
P = 'projects/script-01/work/'
END = 93.158
B = [0, 7.9, 11.4, 15.3, 18.6, 20.8, 25.8, 31.6, 34.5, 39.5, 43.2, 48.0, 53.3, 57.2, 62.1, 64.5, 69.0, 74.3,
     80.3, 83.3, 89.5, END]
S = [
 [(2.23, 3.6), (4.7, 6.47), (133.3, 136.0), (136.0, 136.6)],  # L1 intro: home, create, finished table
 [(9.53, 11.23), (12.63, 14.9)],        # L2 open design, elements
 [(16.4, 18.7), (19.97, 21.0)],         # L3 tables category
 [(21.0, 22.27), (23.57, 24.9)],        # L4 place table, first cell
 [(24.9, 26.9)],                        # L5 continue filling
 [(27.7, 30.8), (33.07, 34.4)],         # L6 three columns
 [(68.57, 74.7)],                       # L7 add row
 [(64.33, 66.83)],                      # L8 add column
 [(78.57, 80.43), (82.27, 84.6)],       # L9 row/column menus
 [(48.07, 49.37), (50.6, 52.37)],       # L10 drag divider
 [(60.0, 62.77), (55.17, 56.57)],       # L11 table menu
 [(85.87, 88.53), (90.07, 92.43)],      # L12 header fill colour
 [(93.87, 96.13), (98.1, 100.0)],       # L13 bold, text colour
 [(103.33, 106.5), (108.23, 110.0)],    # L14 border
 [(110.0, 110.93), (112.1, 113.37)],    # L15 aside
 [(136.6, 139.0), (142.4, 143.6)],      # L16 do not shrink
 [(38.07, 40.5), (41.7, 42.7), (50.9, 52.37)],  # L17 widen column
 [(28.5, 30.8), (34.4, 35.63), (82.27, 84.6)],  # L18 paste cells
 [(139.0, 141.5)],                      # L19 check result
 [(118.93, 121.23), (122.03, 124.9), (126.67, 129.1)],  # L20 share, download
 [(114.3, 116.67), (143.6, 144.7)],     # L21 keep design
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
