"""Hand-built plan for script-08 (Canva foldable business card take, 230.6 s, 1920x1080, baked recorder zoom), 92.026 s voiceover (20 lines).
One group per narration line, starting on its lines.json start. Piece formats:
 (a,b) scaled to share the group's remaining time; (a,b,dur) fixed output duration; ('H',t,dur) hold of frame t."""
import json
P = 'projects/script-08/work/'
END = 92.026
G = [
 (0, 6.48, [(2.2, 4.2, 2.3), (4.2, 7.4)]),                      # L1 title: static home, Create design click
 (6.48, 10.24, [(7.4, 10.4)]),                                  # L2 decide size: Create menu, units
 (10.24, 17.3, [(10.4, 12.0), ('H', 12.0, 0.7), (12.0, 13.03), (13.03, 15.27, 2.4), (15.27, 15.75)]),  # L3 85 wide, 55 tall typed
 (17.3, 21.68, [(15.75, 19.4)]),                                # L4 Create design click -> blank sheet
 (21.68, 26.24, [(19.4, 21.27, 2.1), (21.27, 23.3)]),           # L5 unfolded blank sheet
 (26.24, 30.32, [(44.2, 49.5)]),                                # L6 File > Rulers and guides > show rulers
 (30.32, 34.66, [(71.8, 74.6), (81.2, 83.2)]),                  # L7 Add guides panel, rows = 2
 (34.66, 36.68, [(86.0, 88.4)]),                                # L8 guide appears = fold
 (36.68, 39.46, [(88.6, 91.0)]),                                # L9 page one
 (39.46, 43.34, [(91.0, 92.9), (98.0, 100.2, 2.2)]),            # L10 lower half selected
 (43.34, 50.22, [(103.87, 108.9), (109.8, 112.2)]),             # L11 upper half / back cover text
 (50.22, 52.14, [(137.8, 139.8)]),                              # L12 page two
 (52.14, 58.5, [(139.8, 145.0), (152.4, 154.0, 1.5)]),          # L13 inside panels
 (58.5, 62.56, [(112.2, 116.4)]),                               # L14 essential check (zoomed-out design)
 (62.56, 69.8, [(116.4, 121.3), (158.8, 161.1)]),               # L15 mark panels, print/download
 (69.8, 77.54, [(161.1, 168.0)]),                               # L16 duplex / printer settings (file types)
 (77.54, 80.3, [(67.1, 70.0)]),                                 # L17 remove line (File > Clear guides)
 (80.3, 84.3, [(86.4, 88.4), (100.4, 102.4, 2.0)]),             # L18 guide does not print
 (84.3, 88.88, [(210.2, 212.4), (221.0, 224.0)]),               # L19 PDF, Print preset, bleed/crop marks
 (88.88, END, [(184.0, 187.2)]),                                # L20 file downloaded
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    src = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = src / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        last = k == len(pieces) - 1
        if p[0] == 'H':
            end = o1 if last else t + p[2]
            s = {"src_start": p[1], "src_end": p[1], "out_start": t, "out_end": end, "mode": "hold"}
            a = b = p[1]
        else:
            a, b = p[0], p[1]
            d = p[2] if len(p) == 3 else (b - a) / sp
            end = o1 if last else t + d
            s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
