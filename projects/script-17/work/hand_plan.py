"""Hand-built plan for script-17 (recording has baked-in recorder zoom and no click log: no zooms/ripples;
143.8 s recording, long idle spells, two passes over the same steps; 80.8 s voiceover). Pieces per narration
interval at 0.75-1.5x, idle stills skipped, anchored clicks land on the end of their group."""
import json, sys
sys.path.insert(0, 'tools')
P = 'projects/script-17/work/'
lines = json.load(open(P + 'lines.json'))
words = {}
for l in lines:
    for w in l['words']:
        k = (l['id'], w['word'].strip('.,').lower())
        while k in words:
            k = k + ('+',)
        words[k] = w
END = 80.805
# (out_start, out_end, [(src_a, src_b)], anchor-at-end or None)
G = [
 (0, 8.94, [(72.7, 79.4), (10.35, 10.97)], ('A1', 2, 'click')),
 (8.94, 13.02, [(10.97, 13.0), (16.4, 19.4)], ('A2', 3, 'select')),
 (13.02, 16.34, [(19.4, 22.9)], None),
 (16.34, 22.18, [(119.8, 125.6)], None),
 (22.18, 23.92, [(33.1, 34.85)], ('A3', 5, 'open')),
 (23.92, 25.68, [(34.85, 36.6)], None),
 (25.68, 28.24, [(36.6, 39.9)], None),
 (28.24, 32.86, [(42.7, 46.4)], None),
 (32.86, 36.84, [(46.4, 48.9), (52.2, 53.8)], ('A4', 8, 'file')),
 (36.84, 39.5, [(53.8, 55.2), (61.4, 63.6)], ('A5', 9, 'show')),
 (39.5, 42.08, [(63.6, 66.2)], None),
 (42.08, 47.9, [(90.4, 96.0)], None),
 (47.9, 50.56, [(66.2, 68.5)], None),
 (50.56, 53.68, [(55.8, 58.9)], None),
 (53.68, 59.42, [(110.2, 114.7)], None),
 (59.42, 62.58, [(103.5, 106.8)], None),
 (62.58, 68.42, [(125.6, 131.0)], None),
 (68.42, 73.46, [(28.9, 33.1)], None),
 (73.46, 75.66, [(101.0, 103.3)], None),
 (75.66, 77.62, [(131.9, 133.8)], ('A7', 18, 'download')),
 (77.62, 78.3, [(136.9, 137.7)], ('A8', 18, 'mp4')),
 (78.3, 79.76, [(137.7, 138.6), (139.7, 140.3)], ('A9', 18, 'saved')),
 (79.76, END, [(140.3, 141.4)], None),
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
        w = words[(anc[1], anc[2])]
        sync.append({"action": anc[0], "line": anc[1], "word": w['word'], "word_index": w['i'], "word_t": w['start']})
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
