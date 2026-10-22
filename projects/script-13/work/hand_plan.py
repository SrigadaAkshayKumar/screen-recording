"""Hand-built plan for script-13: each group fills one narration interval with source pieces."""
import json, sys
P = 'projects/script-13/work/'
lines = json.load(open(P + 'lines.json'))
END = 76.487
G = [
 (0, 6.8, [(1.5, 6.6)]),
 (6.8, 10.64, [(6.6, 10.4)]),
 (10.64, 14.78, [(39.0, 43.2)]),
 (14.78, 17.44, [(59.7, 62.4)]),
 (17.44, 23.54, [(64.5, 67.0), (76.5, 80.3)]),
 (23.54, 26.22, [(98.3, 101.0)]),
 (26.22, 33.72, [(101.0, 105.0), (127.5, 131.5)]),
 (33.72, 36.5, [(120.5, 123.3)]),
 (36.5, 41.64, [(160.6, 165.7)]),
 (41.64, 49.7, [(192.8, 197.0), (205.0, 208.5)]),
 (49.7, 56.28, [(208.5, 215.0)]),
 (56.28, 58.88, [(222.0, 224.6)]),
 (58.88, 63.92, [(228.0, 233.0)]),
 (63.92, 68.32, [(256.0, 260.4)]),
 (68.32, 72.44, [(260.5, 264.6)]),
 (72.44, END, [(274.6, 278.7)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
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
