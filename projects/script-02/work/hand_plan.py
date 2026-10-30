"""Hand-built plan for script-02 (266 s Canva Bulk Create quotes take, 1920x1080, 101.425 s voiceover, recorder zoom baked in: no zooms/ripples).
Each group fills one narration interval (ends at the next line's start) with source pieces chosen where the picture
moves (freezedetect n=0.003 d=0.8 on the source). A piece is (src_a, src_b) or (src_a, src_b, speed)."""
import json
P = 'projects/script-02/work/'
END = 101.425
G = [
 (6.76,  [(168.9, 169.87), (169.87, 171.4), (184.0, 186.47), (187.47, 189.0)]),  # L1 intro: preview of the finished quote pages
 (10.38, [(8.0, 11.0)]),                                   # L2 Canva home
 (15.52, [(13.3, 14.5), (19.97, 23.5)]),                   # L3 editor (plan line: no footage)
 (17.76, [(11.0, 13.3)]),                                  # L4 create Instagram post (dialog)
 (23.46, [(23.5, 26.5), (32.93, 36.0)]),                   # L5 background + text box
 (26.42, [(36.0, 38.9)]),                                  # L6 space for the longest quote
 (31.58, [(72.53, 78.43)]),                                # L7 apps / Bulk Create
 (36.16, [(80.17, 82.43), (85.27, 87.5)]),                 # L8 enter data manually
 (40.38, [(88.73, 89.97), (91.0, 92.27), (95.4, 98.27)]),  # L9 columns Quote/Author
 (45.24, [(109.77, 112.77), (127.7, 129.5)]),              # L10 paste rows
 (47.2,  [(141.53, 143.5)]),                               # L11 field matching
 (52.02, [(143.5, 144.93), (146.63, 149.0)]),              # L12 check columns fill boxes
 (60.1,  [(149.0, 150.4), (151.43, 152.57), (153.37, 157.43), (159.37, 160.8)]),  # L13 Match Data
 (62.78, [(165.0, 167.27)]),                               # L14 preview
 (70.46, [(215.5, 217.0), (225.3, 227.8), (230.27, 232.8)]),  # L15 create batch and open
 (77.46, [(172.67, 175.83), (177.73, 181.6)]),             # L16 longer quote may not fit
 (81.34, [(181.6, 184.0), (189.0, 190.73)]),               # L17 check longest quote
 (87.26, [(232.8, 233.8), (236.3, 240.73)]),               # L18 review pages
 (90.8,  [(242.43, 245.5)]),                               # L19 download PNG
 (96.42, [(245.5, 247.1), (248.1, 250.03), (252.27, 253.5)]),  # L20 zip
 (END,   [(253.5, 255.33), (262.4, 264.1), (265.0, 265.97)]),  # L21 closing
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
