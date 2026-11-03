"""Hand-built plan for script-02: each group fills one narration interval with source pieces."""
import json
P = 'projects/script-02/work/'
lines = json.load(open(P + 'lines.json'))
widx = {(l['id'], w['word'].strip('.,').lower()): (w['i'], w['start']) for l in lines for w in l['words']}
END = 92.322
# (out_start, out_end, [(src_a, src_b[, speed])])
G = [
 (0, 5.82, [(0, 0.7, 1.0), (0.7, 5.1, 2.0), (7.0, 9.92)]),
 (5.82, 10.24, [(10.0, 13.8), (18.4, 20.3)]),
 (10.24, 15.1, [(25.5, 26.1), (32.0, 34.6), (44.4, 46.4)]),
 (15.1, 19.44, [(47.5, 50.2), (51.8, 54.0)]),
 (19.44, 22.52, [(56.2, 58.3), (59.1, 60.9)]),
 (22.52, 25.8, [(67.0, 70.4)]),
 (25.8, 31.72, [(94.26, 100.0)]),
 (31.72, 36.6, [(97.2, 99.6), (99.8, 101.0), (105.2, 106.8)]),
 (36.6, 41.14, [(109.0, 113.0)]),
 (41.14, 45.68, [(113.0, 114.3), (116.3, 120.4)]),
 (45.68, 48.3, [(148.4, 151.0)]),
 (48.3, 55.54, [(153.9, 155.3, 1.0), (163.8, 165.0, 1.0), (168.2, 170.9, 1.0), (172.9, 175.0)]),
 (55.54, 60.38, [(202.4, 205.0, 1.0), (207.2, 209.2)]),
 (60.38, 66.62, [(233.5, 236.2), (237.4, 241.0)]),
 (66.62, 71.78, [(263.9, 269.0)]),
 (71.78, 75.42, [(290.0, 293.5)]),
 (75.42, 85.6, [(293.5, 294.5), (295.3, 298.0), (302.2, 307.0)]),
 (85.6, END, [(246.2, 252.8)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    explicit = [p for p in pieces if len(p) == 3]
    if explicit:
        outs = [(p[1] - p[0]) / p[2] for p in explicit]
        rest = o1 - o0 - sum(outs)
        fill = [p for p in pieces if len(p) == 2]
        sp_fill = sum(p[1] - p[0] for p in fill) / rest
        durs = [(p[1] - p[0]) / (p[2] if len(p) == 3 else sp_fill) for p in pieces]
    else:
        sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
        durs = [(p[1] - p[0]) / sp for p in pieces]
    t = o0
    for k, (p, d) in enumerate(zip(pieces, durs)):
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
import sys
sys.path.insert(0, 'tools')
import check
acts = json.load(open(P + 'actions.json'))['actions']
allw = [(w['i'], w['word'], w['start']) for l in lines for w in l['words']]
for a in acts:
    o = check.src_to_out(segs, a['t_click'])
    if o is None: continue
    i, w, t = min(allw, key=lambda x: abs(x[2] - o))
    plan['sync'].append({"action": a['id'], "line": next(l['id'] for l in lines if l['word_range'][0] <= i <= l['word_range'][1]), "word": w.strip('.,'), "word_index": i, "word_t": t, "out_t": round(o, 3)})
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
