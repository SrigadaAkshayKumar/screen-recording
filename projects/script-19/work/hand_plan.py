"""Hand-built plan for script-19 (301.6 s recording, 102.7 s voiceover, recorder zoom baked in: no zooms/ripples).
Pieces are taken from the moving windows of the recording (freezedetect n=0.003 d=0.8), one group per narration interval."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
# (out_start, out_end, [(src_a, src_b)])
G = [
 (0, 6.08, [(9.1, 11.5), (13.4, 16.1)]),
 (6.08, 13.72, [(18.1, 21.0), (21.9, 23.1), (24.3, 27.5)]),
 (13.72, 19.66, [(27.5, 29.1), (36.9, 39.5), (56.1, 57.8)]),
 (19.66, 25.24, [(157.6, 163.2)]),
 (25.24, 32.52, [(58.0, 60.7), (75.1, 80.1)]),
 (32.52, 40.52, [(84.6, 87.0), (89.0, 93.5), (94.8, 96.3)]),
 (40.52, 45.14, [(125.8, 127.1), (128.1, 132.1)]),
 (45.14, 49.9, [(132.9, 134.4), (135.5, 139.6)]),
 (49.9, 55.1, [(163.2, 168.4)]),
 (55.1, 57.68, [(168.4, 171.0)]),
 (57.68, 62.84, [(171.0, 175.3), (181.0, 182.6)]),
 (62.84, 68.8, [(188.8, 190.2), (197.9, 202.0)]),
 (68.8, 74.24, [(202.0, 203.1), (209.6, 212.6)]),
 (74.24, 80.26, [(212.6, 213.6), (216.6, 220.5)]),
 (80.26, 84.94, [(224.2, 228.6)]),
 (84.94, 88.02, [(238.3, 241.5)]),
 (88.02, 94.46, [(252.0, 255.6), (258.9, 260.5), (264.7, 266.0)]),
 (94.46, 99.0, [(271.3, 273.9), (276.2, 278.2)]),
 (99.0, END, [(281.9, 285.6)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(o0, o1, '%.2fx' % sp)
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
