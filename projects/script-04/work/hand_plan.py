"""Hand plan for script-04. Group = one narration line (or two merged), from its start to the next group's start.
piece: (a, b) speed piece, (a, b, out_dur) fixed-duration speed piece, ('H', t, dur) hold at source t.
Pieces without a fixed duration share the remaining group time by source length."""
import json
P = 'projects/script-04/work/'
lines = {l['id']: l for l in json.load(open(P + 'lines.json'))}
END = 86.723
G = [
 (1, [(71.8, 77.4)]),
 (2, [(13.6, 16.25), ('H', 16.25, 1.44)]),
 (3, [(16.7, 21.0)]),
 (4, [(15.9, 16.9, 1.0), (23.7, 29.9, 3.7), (29.9, 31.5)]),   # L4 + L5
 (6, [(31.3, 33.0)]),
 (7, [(36.2, 40.1)]),
 (8, [(33.0, 35.9)]),
 (9, [(41.8, 44.3), ('H', 44.3, 1.4)]),
 (10, [(44.3, 45.75), (46.3, 47.3)]),
 (11, [(40.1, 41.8), ('H', 41.8, 1.0)]),
 (12, [(47.3, 48.4), (49.8, 51.2), ('H', 51.2, 1.4)]),
 (13, [(51.2, 57.3)]),
 (14, [(58.4, 62.6)]),
 (15, [(77.2, 83.4)]),
 (16, [(62.6, 64.2), (83.0, 84.8), ('H', 84.8, 1.0)]),
 (17, [(14.3, 16.2), (93.4, 96.7), ('H', 96.7, 1.0)]),
 (18, [(25.0, 28.0)]),
 (19, [(84.4, 87.3), ('H', 87.3, 1.45)]),   # end hold kept <= 1.5 s
]
segs, prev_end = [], None
for k, (ln, pieces) in enumerate(G):
    o0 = 0.0 if ln == 1 else lines[ln]['start']
    o1 = lines[G[k + 1][0]]['start'] if k + 1 < len(G) else END
    fixed = sum(p[2] if (p[0] == 'H' or len(p) == 3) else 0 for p in pieces)
    var = sum(p[1] - p[0] for p in pieces if p[0] != 'H' and len(p) == 2)
    sp = var / (o1 - o0 - fixed) if var else 1
    t = o0
    for j, p in enumerate(pieces):
        last = j == len(pieces) - 1
        if p[0] == 'H':
            end = o1 if last else t + p[2]
            s = {"src_start": p[1], "src_end": p[1], "out_start": t, "out_end": end, "mode": "hold"}
            a = b = p[1]
        else:
            a, b = p[0], p[1]
            end = o1 if last else t + (p[2] if len(p) == 3 else (b - a) / sp)
            s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
        print(f"L{ln} out {s['out_start']:.2f}-{end:.2f} src {a}-{b} {s['mode']} {(b-a)/(end-s['out_start']) if b!=a else 0:.2f}x")
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
