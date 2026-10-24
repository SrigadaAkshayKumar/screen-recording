"""Hand-built plan for script-02 (225 s recording, 86.7 s voiceover, recorder zoom baked in: no zooms/ripples).
Each group fills one narration interval (ends at the next line's start) with source pieces chosen where the
picture moves (freezedetect on the source). A piece is (src_a, src_b) or (src_a, src_b, speed); pieces without
a speed share the rest of the interval."""
import json
P = 'projects/script-02/work/'
END = 86.703
G = [
 (5.8,   [(2.2, 6.7)]),                          # L1 intro on the Canva home
 (9.14,  [(12.6, 13.8), (22.03, 24.37)]),        # L2 editor opens, elements
 (15.66, [(28.8, 33.27), (33.27, 35.3)]),        # L3 frames category
 (18.76, [(30.8, 33.27)]),                  # L4 landscape frame in the panel (reuse)
 (23.52, [(37.0, 40.9)]),   # L5 frame placed on the page
 (26.5,  [(52.0, 54.0), (57.5, 59.0)]),          # L6 open uploads / upload dialog
 (30.56, [(73.7, 77.8)]),                        # L7 drag onto the frame
 (33.9,  [(77.8, 79.4), (79.4, 80.4)]),          # L8 result in the shape
 (36.16, [(85.5, 87.8)]),                        # L9 double click -> crop
 (40.98, [(86.8, 90.7)]),          # L10 reposition / handles
 (44.66, [(92.8, 95.9)]),                        # L11 done
 (48.42, [(117.6, 121.4)]),                      # L12 resize the frame
 (52.22, [(118.8, 121.8)]), # L13 masked result keeps its shape
 (58.08, [(138.7, 144.9)]),                      # L14-15 frames from the elements panel
 (60.86, [(144.9, 147.5)]),                      # L16 add shape/frame
 (65.06, [(147.5, 151.5)]),                      # L17 select both
 (68.94, [(171.0, 175.0)]),                      # L18 ready-made frame
 (72.34, [(175.0, 178.0)]),                      # L19 other shapes
 (76.02, [(178.0, 181.6)]),                      # L20 drag replacement
 (79.08, [(181.6, 184.7)]),                      # L21 image changed
 (84.02, [(205.6, 208.6), (215.0, 217.0)]),      # L22 download PNG / MP4
 (END,   [(217.0, 219.7)]),                      # L23 closing
]
segs, prev_end, o0 = [], None, 0.0
for o1, pieces in G:
    fixed = sum((p[1] - p[0]) / p[2] for p in pieces if len(p) == 3)
    free = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = free / (o1 - o0 - fixed) if free else 1
    t = o0
    for k, p in enumerate(pieces):
        d = (p[1] - p[0]) / (p[2] if len(p) == 3 else sp)
        end = o1 if k == len(pieces) - 1 else t + d
        segs.append({"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed",
                     **({"xfade": True} if prev_end is not None and abs(p[0] - prev_end) > 0.002 else {})})
        prev_end, t = p[1], end
    print(f"{o0:6.2f}-{o1:6.2f} {[(round((s['src_end']-s['src_start'])/(s['out_end']-s['out_start']),2)) for s in segs[-len(pieces):]]}")
    o0 = o1
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
