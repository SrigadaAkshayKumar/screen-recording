"""script-01 (385 s Canva filmstrip take, 92.087 s voiceover, 1920x1080): per-line plan, pieces from 1 s / 2 s sheets.
Each group starts on its line's lines.json start; pieces are played at ~1x, joined with cross-fades."""
import json
P = 'projects/script-01/work/'
D = 92.087
L = json.load(open(P + 'lines.json'))
starts = [l['start'] for l in L] + [D]
starts[0] = 0.0
# per line: list of (src_a, src_b[, fixed_out_duration])
G = {
 1: [(3.5, 7.9, 2.2), (370.0, 373.0)],
 2: [(9.3, 10.6), (11.7, 13.0)],
 3: [(35.2, 36.9), (44.0, 45.6), (49.2, 53.4)],
 4: [(25.7, 29.3)],
 5: [(70.8, 72.0), (75.0, 77.4), (82.0, 83.5)],
 6: [(84.2, 86.6), (91.2, 95.8)],
 7: [(167.8, 171.2)],
 8: [(198.0, 199.6), (208.5, 211.5)],
 9: [(235.3, 240.5)],
 10: [(255.0, 256.8), (279.7, 281.6)],
 11: [(283.5, 285.6)],
 12: [(287.8, 289.0), (290.0, 293.7)],
 13: [(293.5, 296.0)],
 14: [(296.6, 298.8)],
 15: [(306.8, 309.8), (311.0, 313.2)],
 16: [(316.0, 321.2)],
 17: [(323.0, 324.8), (331.3, 333.3)],
 18: [(347.4, 351.0)],
 19: [(333.8, 338.0)],
 20: [(360.4, 362.8), (364.8, 368.0)],
 21: [(375.8, 380.6)],
 22: [(349.0, 351.6)],
}
segs = []
first = True
for i in range(1, 23):
    o0, o1 = starts[i - 1], starts[i]
    pcs = G[i]
    fixed = sum(p[2] for p in pcs if len(p) > 2)
    var = sum(p[1] - p[0] for p in pcs if len(p) == 2)
    k = (o1 - o0 - fixed) / var
    o = o0
    for j, p in enumerate(pcs):
        d = p[2] if len(p) > 2 else (p[1] - p[0]) * k
        oe = o1 if j == len(pcs) - 1 else o + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": round(o, 3), "out_end": round(oe, 3), "mode": "speed"}
        if not first: s["xfade"] = True
        first = False
        segs.append(s); o = oe
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.2f}-{s['src_end']:6.2f} {(s['src_end']-s['src_start'])/d:.2f}x")
