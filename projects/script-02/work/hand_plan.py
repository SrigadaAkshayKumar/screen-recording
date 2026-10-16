"""Hand-built plan for script-02 (recording 2.9x longer than the voiceover): groups of source pieces,
each group fills one narration interval. No zooms/ripples: the recorder baked its own zooms in."""
import json
P = 'projects/script-02/work/'
lines = json.load(open(P + 'lines.json'))
words = {(l['id'], w['word'].strip('.,').lower()): (w['start'], w['i']) for l in lines for w in l['words']}
END = 86.936
# (out_start, out_end, [(src_a, src_b[, speed])], sync-at-end (action, line, word, click_src) or None)
G = [
 (0, 7.4, [(7.9, 15.2)], ('A1', 2, 'uploads')),
 (7.4, 9.8, [(15.3, 16.8), (23.1, 24.3)], ('A2', 2, 'choose')),
 (9.8, 12.2, [(24.3, 26.7)], None),
 (12.2, 13.6, [(34.2, 35.6)], ('A3', 3, 'add')),
 (13.6, 16.4, [(35.6, 38.4)], None),
 (16.4, 18.55, [(47.2, 49.5)], ('A4', 4, 'play')),
 (18.55, 20.0, [(49.5, 51.0)], None),
 (20.0, 21.96, [(57.2, 59.1)], None),
 (21.96, 24.64, [(69.4, 71.9)], ('A5', 5, 'lower')),
 (24.64, 27.08, [(71.9, 74.3)], None),
 (27.08, 30.0, [(82.4, 85.3)], ('A6', 6, 'captions')),
 (30.0, 32.56, [(85.3, 87.9)], None),
 (32.56, 36.7, [(87.9, 92.0)], None),
 (36.7, 40.9, [(96.2, 100.4)], None),
 (40.9, 42.2, [(93.6, 94.9)], None),
 (42.2, 43.2, [(101.6, 102.7)], ('A7', 9, 'captions')),
 (43.2, 44.56, [(102.7, 106.5, 'wait')], None),
 (44.56, 47.92, [(112.3, 114.0), (123.0, 124.66)], None),
 (47.92, 50.6, [(133.0, 135.8)], None),
 (50.6, 54.02, [(150.0, 153.4)], None),
 (54.02, 59.84, [(153.4, 158.0)], None),
 (59.84, 62.46, [(179.5, 182.1)], None),
 (62.46, 66.82, [(193.0, 197.3)], None),
 (66.82, 72.84, [(207.9, 211.0), (213.2, 215.0)], None),
 (72.84, 77.94, [(183.5, 186.4), (215.0, 217.0)], None),
 (77.94, 80.9, [(219.5, 221.0), (223.0, 225.0)], ('A8', 18, 'share')),
 (80.9, END, [(228.4, 234.4)], None),
]
segs, sync, prev_end = [], [], None
for o0, o1, pieces, anc in G:
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if len(p) == 3: s["wait"] = True
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
    if anc:
        aid, ln, w = anc
        wt, wi = words[(ln, w)]
        sync.append({"action": aid, "line": ln, "word": w, "word_index": wi, "word_t": wt})
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
