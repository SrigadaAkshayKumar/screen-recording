"""Hand-built plan for script-03: each group fills the narration interval between two anchors with
source pieces at one uniform speed (explicit-speed pieces and ('h', src, dur) holds are honoured)."""
import json, sys
P = 'projects/script-03/work/'
lines = json.load(open(P + 'lines.json'))
W = {}
for l in lines:
    for w in l['words']:
        W.setdefault((l['id'], w['word'].strip('.,').lower()), w)
END = 76.382
# (out_start, out_end, pieces, (action, line, word, click_out))
G = [
 (0, 6.88, [('h', 0, 0.3), (0, 4.933, .75)], ('A1', 2, 'open', 6.88)),
 (6.88, 9.74, [(4.933, 7.4), (22.3, 22.9)], ('A2', 2, 'files', 9.74)),
 (9.74, 16.68, [(22.9, 29.3)], ('A3', 3, 'to', 16.68)),
 (16.68, 19.64, [(29.3, 29.8, .75), ('h', 29.8, 1.49), (29.8, 30.4, .75)], ('A4', 4, 'audio', 19.64)),
 (19.64, 21.26, [(30.4, 30.9), (43.6, 44.6)], ('A5', 4, 'add', 21.26)),
 (21.26, 31.36, [(44.6, 50.6), (56.0, 61.8)], ('A7', 7, 'trim', 31.36)),
 (31.36, 33.88, [(61.8, 63.2), (72.0, 72.7)], ('A8', 8, 'play', 33.88)),
 (33.88, 35.86, [(72.7, 74.0), (86.3, 87.3)], ('A9', 9, 'shorten', 35.86)),
 (35.86, 42.6, [(87.3, 92.4), (103.9, 106.2)], ('A10', 10, 'add', 42.6)),
 (42.6, 48.68, [(106.2, 109.0), (115.4, 117.2), (127.0, 129.6)], ('A11', 11, 'reduce', 48.68)),
 (48.68, 53.04, [(129.6, 133.0), (135.0, 136.3)], ('A12', 12, 'voiceover', 53.04)),
 (53.04, 59.06, [(136.3, 141.5), (146.8, 148.0)], ('A13', 14, 'uploading', 59.06)),
 (59.06, 63.72, [(148.0, 154.0)], ('A14', 15, 'timeline', 63.72)),
 (63.72, 68.9, [(154.0, 155.8), (163.4, 168.3)], ('A15', 16, 'check', 68.9)),
 (68.9, 71.94, [(168.3, 171.9)], ('A16', 17, 'download', 71.94)),
 (71.94, 73.78, [(171.9, 174.6)], ('A17', 17, 'video', 73.78)),
 (73.78, END, [(174.6, 175.4), (187.6, 189.9)], None),
]
segs, sync, prev_end = [], [], None
for o0, o1, pieces, anc in G:
    T = o1 - o0
    fixed = 0.0; srcfill = 0.0
    for p in pieces:
        if p[0] == 'h': fixed += p[2]
        elif len(p) == 3: fixed += (p[1] - p[0]) / p[2]
        else: srcfill += p[1] - p[0]
    sp = srcfill / (T - fixed) if srcfill else None
    t = o0
    for k, p in enumerate(pieces):
        last = k == len(pieces) - 1
        if p[0] == 'h':
            d = p[2]; s = {"src_start": p[1], "src_end": p[1], "mode": "hold"}; a, b = p[1], p[1]
        else:
            d = (p[1] - p[0]) / (p[2] if len(p) == 3 else sp)
            s = {"src_start": p[0], "src_end": p[1], "mode": "speed"}; a, b = p[0], p[1]
        s["out_start"] = t; s["out_end"] = o1 if last else t + d
        if prev_end is not None and abs(a - prev_end) > 0.002 and p[0] != 'h':
            s["xfade"] = True
        segs.append(s); prev_end = b; t = s["out_end"]
    if anc:
        aid, ln, w, click = anc
        ww = W[(ln, w)]
        sync.append({"action": aid, "line": ln, "word": ww['word'], "word_index": ww['i'], "word_t": ww['start']})
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {}, "notes": ["hand-built by work/hand_plan.py (builder cannot meet the pace rules); no zooms/ripples: recording has baked-in recorder zoom"]}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
