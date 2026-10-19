"""Hand-built plan for script-08 (recording has baked-in recorder zoom: no zooms/ripples; 287 s of footage for
79 s of voiceover, so each narration interval gets hand-picked source pieces at 0.8-1.5x)."""
import json, sys
sys.path.insert(0, 'tools')
P = 'projects/script-08/work/'
lines = json.load(open(P + 'lines.json'))
words = {}
for l in lines:
    for w in l['words']:
        k = (l['id'], w['word'].strip('.,').lower())
        while k in words:
            k = k + ('+',)
        words[k] = w
END = 79.438
# (out_start, out_end, [(src_a, src_b)], anchor-at-end or None)
G = [
 (0, 9.76, [(3.0, 5.6), (15.0, 21.45)], ('A1', 3, 'uploads')),
 (9.76, 15.28, [(21.45, 28.8)], ('A2', 4, 'place')),
 (15.28, 16.9, [(28.8, 29.7), (38.1, 38.7)], ('A3', 4, 'resize')),
 (16.9, 19.4, [(38.7, 40.6), (54.6, 55.45)], ('A4', 5, 'text')),
 (19.4, 21.04, [(55.45, 57.7)], ('A5', 5, 'text+')),
 (21.04, 22.56, [(57.7, 59.0), (66.4, 67.2)], ('A6', 6, 'caption')),
 (22.56, 28.3, [(67.2, 71.9)], ('A7', 7, 'colour')),
 (28.3, 31.56, [(71.9, 75.5)], None),
 (31.56, 34.26, [(129.2, 132.4)], ('A8', 8, 'extend')),
 (34.26, 38.36, [(132.4, 137.4)], None),
 (38.36, 40.0, [(161.4, 163.0)], ('A9', 9, 'move')),
 (40.0, 43.76, [(163.0, 167.2)], None),
 (43.76, 50.54, [(168.6, 176.3)], ('A10', 10, 'preview')),
 (50.54, 64.4, [(176.3, 181.0), (144.0, 150.0), (152.0, 158.0)], None),
 (64.4, 65.38, [(210.3, 211.8)], ('A12', 15, 'download')),
 (65.38, 67.3, [(211.8, 212.5), (224.6, 226.5)], ('A13', 15, 'file')),
 (67.3, 70.26, [(226.5, 227.5), (234.6, 238.0)], ('A14', 16, 'it')),
 (70.26, 71.94, [(238.0, 239.4), (260.8, 261.6)], ('A15', 17, 'gif')),
 (71.94, 75.16, [(261.6, 265.2)], None),
 (75.16, 76.02, [(274.1, 275.0)], ('A16', 18, 'png')),
 (76.02, END, [(275.0, 279.4)], None),
]
segs, sync, prev_end = [], [], None
for g in G:
    o0, o1, pieces, anc = g
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
    if anc:
        w = words[(anc[1], anc[2].rstrip('+'), *(('+',) if anc[2].endswith('+') else ()))]
        sync.append({"action": anc[0], "line": anc[1], "word": w['word'], "word_index": w['i'], "word_t": w['start']})
    if g[3] and g[3][0]=='A12':
        w2 = words[(15,'select')]; sync.insert(-1, {'action':'A11','line':15,'word':w2['word'],'word_index':w2['i'],'word_t':w2['start']})
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
