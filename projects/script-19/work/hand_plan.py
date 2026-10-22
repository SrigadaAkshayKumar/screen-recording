"""Hand-built plan for script-19 (234 s recording, 83.4 s voiceover, recorder zoom baked in: no zooms/ripples)."""
import json
P = 'projects/script-19/work/'
lines = json.load(open(P + 'lines.json'))
words = {(l['id'], w['word'].strip('.,').lower()): (w['start'], w['i']) for l in lines for w in l['words']}
END = 83.406
G = [
 (0, 7.62, [(0.0, 7.0)], None),
 (7.62, 11.36, [(60.6, 64.3)], ('A1', 2, 'captions')),
 (11.36, 16.98, [(150.0, 155.6)], None),
 (16.98, 21.22, [(106.0, 110.2)], None),
 (21.22, 27.24, [(88.0, 94.0)], ('A2', 5, 'edit')),
 (27.24, 30.48, [(76.5, 79.7)], None),
 (30.48, 36.6, [(79.7, 84.9)], None),
 (36.6, 40.24, [(164.0, 167.6)], None),
 (40.24, 44.26, [(126.2, 130.2)], ('A3', 9, 'generate')),
 (44.26, 52.24, [(130.2, 138.2)], None),
 (52.24, 54.48, [(71.0, 73.3)], None),
 (54.48, 57.8, [(67.0, 70.3)], None),
 (57.8, 60.92, [(160.6, 163.7)], None),
 (60.92, 66.76, [(167.0, 172.0)], None),
 (66.76, 78.24, [(191.8, 203.3)], None),
 (78.24, END, [(217.0, 222.2)], ('A5', 17, 'download')),
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
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
