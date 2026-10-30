"""Hand-built plan for script-08 (Canva stickman take, 377.7 s, 1920x1080, baked recorder zoom): no zooms/ripples.
One group per narration line; pieces from freezedetect moving windows (n=0.003,d=0.8). (a,b) scaled; (a,b,dur) fixed duration."""
import json
P = 'projects/script-08/work/'
END = 90.929
G = [
 (0, 7.5, [(2.1, 5.07), (10.17, 12.93)]),                       # L1 intro: finished design
 (7.5, 10.7, [(14.5, 17.03), (17.93, 19.17)]),                  # L2 create video design
 (10.7, 15.4, [(33.0, 37.4)]),                                  # L3 elements search
 (15.4, 19.5, [(37.4, 41.5)]),                                  # L4 results, choose graphic
 (19.5, 25.4, [(42.0, 45.77), (47.77, 50.5)]),                  # L5 consistent character (borrowed browsing)
 (25.4, 27.8, [(62.87, 65.27)]),                                # L6 place left
 (27.8, 33.2, [(73.27, 78.67)]),                                # L7 ground + object (table search)
 (33.2, 37.5, [(315.2, 319.5)]),                                # L8 animate > create animation
 (37.5, 41.4, [(324.77, 328.33)]),                              # L9 drag
 (41.4, 47.6, [(105.0, 108.23), (109.03, 112.03)]),             # L10 movement settings
 (47.6, 50.35, [(133.0, 135.75)]),                              # L11 text bubble
 (50.35, 54.3, [(216.33, 217.43), (218.23, 218.77), (220.23, 221.63), (224.43, 225.17)]),  # L12 timeline
 (54.3, 56.26, [(261.07, 263.0)]),                              # L13 leave time
 (56.26, 59.5, [(228.77, 230.17), (230.17, 232.0)]),            # L14 add scene
 (59.5, 64.3, [(235.0, 239.8)]),                                # L15 matching pose
 (64.3, 67.1, [(244.73, 247.5)]),                               # L16 part tutorials skip
 (67.1, 72.7, [(329.67, 332.43), (333.3, 335.87), (339.27, 340.9)]),  # L17 static slides
 (72.7, 76.0, [(41.5, 44.8)]),                                  # L18 animated graphic (borrowed)
 (76.0, 81.5, [(272.97, 275.27), (276.5, 278.27), (280.4, 281.7)]),  # L19 static poses
 (81.5, 88.2, [(291.77, 294.07), (354.43, 356.07), (357.23, 360.5)]),  # L20 preview/audio
 (88.2, END, [(367.9, 370.6)]),                                 # L21 download
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    src = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = src / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) == 3 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
