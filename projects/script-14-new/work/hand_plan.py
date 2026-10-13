"""Hand-built plan for script-14-new (the builder could not meet the pace rules): groups of source
pieces, each group fills one narration interval at a uniform speed (or the given per-piece speeds)."""
import json, sys
sys.path.insert(0, 'tools')
P = 'projects/script-14-new/work/'
base = json.load(open(P + 'plan.json'))
lines = json.load(open(P + 'lines.json'))
words = {(l['id'], w['word'].strip('.,').lower()): w['start'] for l in lines for w in l['words']}
widx = {(l['id'], w['word'].strip('.,').lower()): w['i'] for l in lines for w in l['words']}
END = 74.344
# (out_start, out_end, [(src_a, src_b[, speed])], anchor-at-end or None)
G = [
 (0, 11.06, [(0, 1.9, .75), (1.9, 4.77, .75), (4.77, 8.47, 1.7), (8.47, 10.4)], ('A2', 3, 'sound')),
 (11.06, 12.62, [(10.4, 11.6)], ('A3', 3, 'video')),
 (12.62, 18.68, [(11.6, 12.85), (9.9, 13.2)], ('A5', 5, 'left')),
 (18.68, 21.32, [(13.2, 14.7), (20.2, 20.8)], ('A6', 5, 'right')),
 (21.32, 24.24, [(20.8, 22.55), (53.9, 55.3)], ('A9', 6, 'result')),
 (24.24, 29.58, [(55.3, 58.3), (40.9, 42.0)], ('A7', 7, 'trim')),
 (29.58, 31.58, [(42.0, 44.8)], ('A8', 7, 'shortened')),
 (31.58, 38.48, [(44.8, 47.0), (47.0, 48.6), (92.4, 95.7)], ('A10', 8, "audio's")),
 (38.48, 40.04, [(95.7, 97.6)], ('A11', 8, 'adjust')),
 (40.04, 42.54, [(97.6, 98.6), (116.8, 119.0)], ('A12', 9, 'highlighted')),
 (42.54, 58.96, [(119.0, 125.0), (143.3, 148.3), (129.9, 131.6)], ('A13', 12, 'listen')),
 (58.96, 66.5, [(131.6, 137.5), (176.8, 179.3)], ('A14', 14, 'add')),
 (66.5, 68.4, [(179.3, 182.4)], ('A15', 14, 'smoothing')),
 (68.4, 69.54, [(182.4, 183.5), (189.0, 189.6)], ('A16', 15, 'preview')),
 (69.54, 70.68, [(189.6, 191.2)], ('A17', 15, 'download')),
 (70.68, 73.24, [(191.2, 193.0), (194.3, 196.2)], ('A20', 15, 'soundtrack')),
 (73.24, END, [(196.2, 197.304)], None),
]
segs, sync, prev_end = [], [], None
for o0, o1, pieces, anc in G:
    explicit = [p for p in pieces if len(p) == 3]
    if explicit:
        outs = [(p[1] - p[0]) / p[2] for p in pieces if len(p) == 3]
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
    if anc:
        aid, ln, w = anc
        sync.append({"action": aid, "line": ln, "word": w, "word_index": widx[(ln, w)], "word_t": words[(ln, w)]})
plan = dict(base)
plan['segments'] = segs
plan['zooms'] = []
plan['ripples'] = []
plan['sync'] = sync
plan['intro'] = None
plan['output'] = dict(base['output'])
plan.pop('generated_hash', None)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
