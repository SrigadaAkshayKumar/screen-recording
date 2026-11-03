"""Hand-built plan for script-08 (Canva foldable business card take, 230.6 s, 1920x1080, baked recorder zoom): no zooms/ripples.
One group per narration line, starting on its lines.json start; pieces from freezedetect moving windows (n=0.002,d=0.8).
(a,b) scaled; (a,b,dur) fixed output duration."""
import json
P = 'projects/script-08/work/'
END = 96.316
G = [
 (0, 4.54, [(2.2, 3.2, 1.2), (4.2, 6.86)]),          # L1 title (static home, then Create design)
 (4.54, 10.74, [(6.86, 11.80)]),                      # L2 custom layout (Create a design > Custom size)
 (10.74, 14.52, [(11.80, 13.03), (13.03, 15.27, 2.24)]),                    # L3 decide size (units/size fields)
 (14.52, 21.54, [(15.27, 21.27)]),                    # L4 85 x 55 mm
 (21.54, 26.0, [(21.27, 25.8)]),                      # L5 custom 85 x 110, create
 (26.0, 31.1, [(26.3, 31.4)]),                        # L6 blank sheet / template
 (31.1, 34.5, [(43.2, 47.4)]),                        # L7 File > rulers and guides > show rulers
 (34.5, 39.04, [(47.4, 52.57)]),                      # L8 Add guides panel
 (39.04, 40.92, [(55.3, 57.4)]),                      # L9 guide added
 (40.92, 43.76, [(62.37, 65.0)]),                     # L10 page one, guides locked
 (43.76, 47.62, [(89.57, 93.4)]),                     # L11 front cover lower half
 (47.62, 54.5, [(103.87, 108.9), (109.8, 112.2)]),    # L12 upper half, rotate
 (54.5, 57.02, [(137.83, 140.4)]),                    # L13 page two
 (57.02, 62.8, [(140.4, 146.2)]),                     # L14 inside panels
 (62.8, 64.52, [(112.2, 113.9)]),                     # L15 essential check (zoomed-out design)
 (64.52, 66.86, [(113.9, 116.4)]),                    # L16 mock-up
 (66.86, 74.08, [(116.4, 121.33), (158.83, 161.5)]),  # L17 mark panels, print/download panel
 (74.08, 78.06, [(161.5, 165.0)]),                    # L18 duplex/printer settings (file type list)
 (78.06, 81.84, [(165.0, 168.5)]),                    # L19 provider layout (PDF settings)
 (81.84, 85.08, [(67.1, 70.4)]),                      # L20 remove line (clear guides menu)
 (85.08, 88.6, [(70.4, 74.0)]),                       # L21 guides do not print
 (88.6, 93.16, [(204.0, 206.5), (210.2, 212.4)]),     # L22 PDF, print preset
 (93.16, END, [(184.0, 187.2)]),                      # L23 file downloaded
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
