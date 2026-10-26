"""Hand-built plan for script-02 (206 s Canva busy-book recording 3420x1922, 100.5 s voiceover, recorder zoom baked in: no zooms/ripples).
Each group fills one narration interval (ends at the next line's start) with source pieces chosen where the picture
moves (freezedetect n=0.003 d=0.8 on the source). A piece is (src_a, src_b) or (src_a, src_b, speed)."""
import json
P = 'projects/script-02/work/'
END = 100.496
G = [
 (8.14,  [(7.0, 9.43), (11.13, 13.37), (14.87, 17.17)]),   # L1 intro: finished sheet
 (13.24, [(21.6, 23.53), (26.17, 28.37)]),                 # L2 create a design, editor opens
 (18.8,  [(30.03, 32.23), (37.73, 39.1), (41.37, 42.47), (44.03, 46.33)]),  # L3 blank page / templates
 (22.12, [(48.6, 51.9)]),                                  # L4 title
 (25.5,  [(98.0, 100.3), (101.43, 103.0)]),                # L5 elements panel
 (31.3,  [(107.43, 109.73), (112.53, 114.87), (117.3, 118.57), (120.73, 122.03)]),  # L6 shapes
 (35.8,  [(90.07, 93.0), (93.87, 94.9)]),                  # L7 instruction
 (39.76, [(94.9, 96.83), (66.2, 68.2)]),                   # L8 same font
 (41.46, [(141.03, 142.73)]),                              # L9 duplicate page
 (46.68, [(144.5, 148.53), (149.4, 150.4)]),               # L10 delete text
 (49.74, [(150.4, 152.4), (162.4, 164.5)]),                # L11 colors / spread
 (51.7,  [(178.0, 180.0)]),                                # L12 piece sheet
 (57.9,  [(132.93, 138.07), (130.37, 131.4)]),             # L13 back to activity page
 (61.96, [(168.83, 172.9)]),                               # L14 more pages
 (66.54, [(172.9, 177.5)]),                                # L15 duplicate layout
 (69.06, [(180.0, 182.23)]),                               # L16 tutorials skip
 (72.92, [(124.6, 128.6)]),                                # L17 same size
 (77.64, [(152.4, 156.07), (159.0, 160.2)]),               # L18 duplicate targets
 (80.24, [(164.5, 167.5)]),                                # L19 fit after printing
 (84.32, [(185.1, 189.2)]),                                # L20 share download PDF print
 (88.24, [(189.2, 190.33), (191.4, 193.9)]),               # L21 export
 (91.92, [(198.23, 201.9)]),                               # L22 print one pair
 (97.0,  [(201.9, 206.2)]),                                # L23 check and assemble
 (END,   [(17.97, 20.3), (21.2, 21.6)]),                   # L24 closing
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
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
