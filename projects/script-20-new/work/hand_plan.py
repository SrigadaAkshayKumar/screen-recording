"""Hand-built plan for script-20-new: each group fills one narration interval with source pieces."""
import json
P = 'projects/script-20-new/work/'
lines = json.load(open(P + 'lines.json'))
widx = {(l['id'], w['word'].strip('.,').lower()): (w['i'], w['start']) for l in lines for w in l['words']}
END = 81.816
# (out_start, out_end, [(src_a, src_b[, speed])])
G = [
 (0, 6.54, [(0, 1.5, .75), (10.0, 14.0)]),
 (6.54, 8.08, [(15.3, 16.8)]),
 (8.08, 9.1, [(20.6, 21.7)]),
 (9.1, 11.76, [(21.9, 23.9)]),
 (11.76, 14.66, [(23.9, 26.9)]),
 (14.66, 17.7, [(39.3, 42.3)]),
 (17.7, 22.08, [(48.4, 52.8)]),
 (22.08, 25.8, [(57.0, 60.7)]),
 (25.8, 28.2, [(63.8, 66.2)]),
 (28.2, 29.26, [(67.4, 68.6)]),
 (29.26, 32.26, [(77.3, 80.3)]),
 (32.26, 39.62, [(69.5, 71.0), (74.5, 77.0), (185.5, 187.2)]),
 (39.62, 42.18, [(99.2, 101.8)]),
 (42.18, 48.34, [(109.2, 115.4)]),
 (48.34, 57.94, [(132.2, 136.4), (136.4, 138.7), (143.9, 145.3)]),
 (57.94, 60.0, [(145.3, 147.4)]),
 (60.0, 62.5, [(155.4, 157.9)]),
 (62.5, 65.02, [(158.1, 160.1)]),
 (65.02, 67.5, [(171.0, 173.4)]),
 (67.5, 69.64, [(177.9, 180.1)]),
 (69.64, 74.06, [(187.2, 191.0)]),
 (74.06, END, [(196.4, 204.2)]),
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
