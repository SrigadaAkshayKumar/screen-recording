"""Hand-built plan for script-18 (new take): 362 s of recording (baked-in recorder zoom, long idle spells) for
103.28 s of voiceover. Each group fills one narration interval; pieces are (src_a, src_b[, speed]).
Pieces are taken from the moving windows (freezedetect n=0.003). No zooms/ripples (recorder zoom is baked in)."""
import json
P = 'projects/script-18/work/'
END = 103.282
G = [
 (0, 7.26, [(3.9, 9.7)]),
 (7.26, 17.04, [(24.9, 30.4), (32.57, 34.5), (53.3, 60.5)]),
 (17.04, 24.64, [(85.2, 88.8), (98.0, 102.4), (104.5, 107.0)]),
 (24.64, 37.64, [(136.5, 140.5), (146.9, 155.0)]),
 (37.64, 44.28, [(155.0, 160.6)]),
 (44.28, 50.88, [(174.2, 178.3), (179.9, 183.0)]),
 (50.88, 56.38, [(205.3, 211.0)]),
 (56.38, 60.58, [(231.9, 237.1)]),
 (60.58, 65.34, [(257.2, 262.0)]),
 (65.34, 72.08, [(110.0, 112.3), (116.7, 121.6)]),
 (72.08, 81.26, [(122.7, 124.0), (194.0, 196.3), (212.1, 219.0)]),
 (81.26, 83.98, [(275.8, 278.6)]),
 (83.98, 88.76, [(292.0, 297.0)]),
 (88.76, 96.5, [(300.6, 303.6), (308.37, 311.8)]),
 (96.5, END, [(342.5, 349.5)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    explicit = [p for p in pieces if len(p) == 3]
    if explicit:
        rest = o1 - o0 - sum((p[1]-p[0])/p[2] for p in explicit)
        fill = [p for p in pieces if len(p) == 2]
        spf = sum(p[1]-p[0] for p in fill) / rest
        durs = [(p[1]-p[0]) / (p[2] if len(p) == 3 else spf) for p in pieces]
    else:
        sp = sum(p[1]-p[0] for p in pieces) / (o1 - o0)
        durs = [(p[1]-p[0]) / sp for p in pieces]
    t = o0
    for k, (p, d) in enumerate(zip(pieces, durs)):
        end = o1 if k == len(pieces)-1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0]-prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
