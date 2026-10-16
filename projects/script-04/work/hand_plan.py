"""Hand-built plan for script-04 (232 s recording, 74 s voiceover, recorder auto-zoom baked in:
no zooms, no ripples). Each group fills one narration interval; an anchor sits at the group end."""
import json
P = 'projects/script-04/work/'
lines = json.load(open(P + 'lines.json'))
W = {}
for l in lines:
    for w in l['words']:
        W.setdefault((l['id'], w['word'].strip('.,').lower()), []).append(w)
END = 74.423
G = [
 (6.32, [(0, 3.8, .75), (11.2, 13.4)], None),
 (7.84, [(13.4, 14.95)], ('A1', 2, 'moment', 0)),
 (10.22, [(14.95, 15.7, .8), (19.3, 20.2), (28.7, 29.6)], ('A2', 3, 'audio', 0)),
 (12.32, [(29.6, 31.7)], ('A3', 3, 'audio', 1)),
 (15.90, [(31.7, 35.4)], ('A4', 4, 'search', 0)),
 (17.42, [(35.4, 37.2)], ('A5', 4, 'whoosh', 0)),
 (26.78, [(37.2, 41.8), (50.9, 59.2)], ('A6', 6, 'preview', 0)),
 (28.44, [(59.2, 60.3), (65.7, 66.6)], ('A7', 6, 'design', 0)),
 (36.06, [(66.6, 72.0), (88.5, 92.9)], ('A8', 8, 'drag', 0)),
 (41.9, [(92.9, 95.4), (99.0, 103.5)], None),
 (43.06, [(116.0, 117.3)], ('A9', 9, 'silence', 0)),
 (44.9, [(117.3, 118.9), (126.2, 126.8)], ('A10', 10, 'select', 0)),
 (46.32, [(126.8, 128.6)], ('A11', 10, 'volume', 0)),
 (47.22, [(128.6, 129.4)], ('A12', 10, 'louder', 0)),
 (49.12, [(129.4, 131.3)], None),
 (51.38, [(131.3, 132.5), (136.6, 138.0)], None),
 (57.3, [(147.4, 153.3)], None),
 (61.84, [(153.3, 157.8)], None),
 (64.72, [(140.5, 143.4)], None),
 (68.96, [(203.0, 207.0)], None),
 (END, [(208.5, 209.3), (210.0, 211.6), (217.6, 221.2)], None),
]
segs, sync, prev_end, o0 = [], [], None, 0.0
for o1, pieces, anc in G:
    explicit = [p for p in pieces if len(p) == 3]
    fill = [p for p in pieces if len(p) == 2]
    rest = o1 - o0 - sum((p[1] - p[0]) / p[2] for p in explicit)
    sp = sum(p[1] - p[0] for p in fill) / rest
    t = o0
    for k, p in enumerate(pieces):
        d = (p[1] - p[0]) / (p[2] if len(p) == 3 else sp)
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
    if anc:
        aid, ln, w, occ = anc
        ww = W[(ln, w)][occ]
        sync.append({"action": aid, "line": ln, "word": w, "word_index": ww['i'], "word_t": ww['start']})
    o0 = o1
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": sync, "style": {}, "notes": [], "generated_by": "projects/script-04/work/hand_plan.py"}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
