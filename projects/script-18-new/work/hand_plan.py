"""Hand-built plan for script-18-new: 215 s of recording (two takes, baked-in recorder zoom) for 78.7 s of
voiceover. Each group fills one narration interval; pieces are (src_a, src_b[, speed]). No zooms/ripples."""
import json, sys
sys.path.insert(0, 'tools')
P = 'projects/script-18-new/work/'
END = 78.681
G = [
 (0, 6.18, [(5.4, 9.5, .75), (12.0, 12.7)]),
 (6.18, 11.78, [(12.7, 14.5, 1.3), (15.0, 17.0, 1.3), (19.0, 20.15, 1.3), (20.15, 21.8)]),
 (11.78, 16.06, [(21.8, 27.5)]),
 (16.06, 20.3, [(27.5, 33.5)]),
 (20.3, 25.76, [(33.5, 41.5)]),
 (25.76, 33.48, [(72.6, 80.0)]),
 (33.48, 38.52, [(85.9, 91.0)]),
 (38.52, 41.78, [(91.2, 94.1)]),
 (41.78, 47.82, [(111.2, 114.3), (114.3, 116.6), (130.0, 131.3)]),
 (47.82, 52.5, [(147.8, 152.3)]),
 (52.5, 60.24, [(160.8, 167.9)]),
 (60.24, 66.04, [(171.0, 174.0), (177.3, 180.0)]),
 (66.04, 74.44, [(182.6, 191.4)]),
 (74.44, END, [(202.0, 208.0)]),
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
        "sync": [{"action": "A1", "line": 2, "word": "fade", "word_index": 32, "word_t": 9.96}],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
