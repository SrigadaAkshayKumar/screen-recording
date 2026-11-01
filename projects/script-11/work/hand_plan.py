"""Hand-built plan for script-11 (Canva SVG-icon export, 116.2 s recording, 96.27 s voiceover, no zooms: baked recorder zoom).
One group of source pieces per narration line (start = line start); windows come from freezedetect (n=0.002, d=0.8) gaps."""
import json
P = 'projects/script-11/work/'
END = 96.27
L = [
 (0.0,   [(0.0, 2.3), (30.33, 34.7)]),               # L1 intro: icon design, then icon being edited
 (6.92,  [(8.87, 10.6)]),                            # L2 open icon design
 (8.64,  [(34.7, 41.0)]),                            # L3 clean example, shapes
 (14.7,  [(42.23, 43.6), (46.43, 47.8)]),            # L4 keep only artwork
 (17.4,  [(47.8, 50.63), (51.43, 54.0)]),            # L5 remove extras, centre
 (24.14, [(66.87, 69.55)]),                          # L6 Share / Download
 (26.82, [(69.55, 73.05)]),                          # L7 File type SVG
 (30.32, [(64.8, 65.73), (74.7, 76.23), (79.23, 81.77)]),  # L8 plan / upgrade indicator
 (36.06, [(87.27, 92.0)]),                           # L9 download
 (40.84, [(92.0, 94.13), (95.27, 96.2)]),            # L10 open saved SVG in browser
 (43.86, [(96.2, 97.53), (98.97, 100.0)]),           # L11 sharp
 (46.16, [(100.0, 105.7)]),                          # L12 zoom in / inspect
 (51.9,  [(105.7, 107.7)]),                          # L13
 (53.92, [(107.7, 111.8), (58.47, 62.4)]),           # L14 blurry PNG
 (62.0,  [(62.4, 63.87), (26.03, 28.7)]),            # L15 vector artwork
 (66.24, [(12.3, 15.0), (19.2, 22.13), (23.23, 24.93)]),  # L16 several icons / pages
 (74.02, [(54.0, 57.33)]),                           # L17 whole layout
 (77.94, [(36.0, 40.5)]),                            # L18 stock element
 (82.7,  [(100.0, 103.6), (108.0, 111.0)]),          # L19 own artwork
 (89.98, [(102.0, 107.0), (115.23, 116.17)]),        # L20 light/dark test
]
segs, prev = [], None
for i, (o0, pieces) in enumerate(L):
    o1 = L[i + 1][0] if i + 1 < len(L) else END
    tot = sum(b - a for a, b in pieces)
    t = o0
    for j, (a, b) in enumerate(pieces):
        e = o1 if j == len(pieces) - 1 else t + (b - a) / tot * (o1 - o0)
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b
        print(f"{t:7.2f}-{e:7.2f} {(b-a)/(e-t):.2f}x src {a}-{b}")
        t = e
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
