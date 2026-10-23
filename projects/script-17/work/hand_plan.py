"""Hand-built plan for script-17 (265.8 s recording, 105.9 s voiceover, baked-in recorder zoom, no click log:
no zooms/ripples). One group per narration line; pieces from the moving windows of the source."""
import json
P = 'projects/script-17/work/'
lines = json.load(open(P + 'lines.json'))
END = 105.883
B = {l['id']: l['start'] for l in lines}
# (line id whose start begins the group, [(src_a, src_b)], anchor (action, line, word) or None)
G = [
 (1, [(251.5, 259.7)], None),
 (2, [(21.3, 24.5)], None),
 (3, [(36.0, 40.4)], None),
 (4, [(30.3, 35.0)], ('A1', 4, 'uploads')),
 (5, [(41.7, 46.0), (47.9, 48.5)], None),
 (6, [(68.0, 76.0)], None),
 (7, [(76.0, 84.0)], None),
 (8, [(86.9, 89.4), (92.1, 93.8), (95.0, 96.0)], None),
 (9, [(96.0, 98.5)], None),
 (10, [(98.5, 103.8)], None),
 (11, [(107.4, 111.7)], None),
 (12, [(113.9, 117.1)], None),
 (13, [(119.5, 122.1)], None),
 (14, [(123.7, 126.1), (127.0, 127.9)], None),
 (15, [(130.4, 134.7), (136.0, 138.8)], None),
 (16, [(157.9, 162.0)], None),
 (17, [(185.6, 192.2), (193.8, 195.0)], None),
 (18, [(205.9, 210.2)], None),
 (19, [(211.5, 215.9)], None),
 (20, [(224.1, 226.4), (229.0, 231.3)], None),
 (21, [(231.3, 233.5), (240.0, 241.8)], None),
 (22, [(244.0, 246.8), (261.3, 262.7), (264.7, 265.77)], None),
]
starts = [0.0] + [B[g[0]] for g in G[1:]] + [END]
words = {}
for l in lines:
    for w in l['words']:
        words.setdefault((l['id'], w['word'].strip('.,').lower()), w)
segs, sync, prev_end = [], [], None
for k, (lid, pieces, anc) in enumerate(G):
    o0, o1 = starts[k], starts[k + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for j, (a, b) in enumerate(pieces):
        end = o1 if j == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    if anc:
        w = words[(anc[1], anc[2])]
        sync.append({"action": anc[0], "line": anc[1], "word": w['word'], "word_index": w['i'], "word_t": w['start']})
    print(f"{o0:6.2f}-{o1:6.2f} L{lid} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
