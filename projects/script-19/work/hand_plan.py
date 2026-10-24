"""Hand-built plan for script-19 (359 s recording, 103.4 s voiceover, recorder zoom baked in: no zooms/ripples).
Pieces come from the moving windows of the recording (freezedetect n=0.003 d=0.8), one group per narration line (or pair of lines)."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
# (out_start, out_end, [(src_a, src_b)])
G = [
 (0, 10.86, [(3.33, 5.83), (13.07, 20.13)]),
 (10.86, 14.66, [(111.77, 115.6)]),
 (14.66, 18.14, [(22.93, 26.33)]),
 (18.14, 23.54, [(38.8, 41.67), (29.87, 32.17)]),
 (23.54, 27.72, [(150.87, 155.05)]),
 (27.72, 30.8, [(173.77, 176.85)]),
 (30.8, 33.36, [(176.85, 179.1)]),
 (33.36, 40.38, [(187.97, 192.8), (196.7, 198.9)]),
 (40.38, 46.5, [(198.9, 200.3), (201.33, 202.63), (184.33, 186.77)]),
 (46.5, 53.02, [(134.63, 140.37)]),
 (53.02, 58.42, [(306.1, 311.5)]),
 (58.42, 64.48, [(223.43, 225.73), (229.9, 232.47), (217.0, 218.23)]),
 (64.48, 67.94, [(233.53, 237.0)]),
 (67.94, 71.58, [(237.0, 240.64)]),
 (71.58, 74.04, [(248.8, 251.3)]),
 (74.04, 79.06, [(251.3, 256.1)]),
 (79.06, 84.52, [(257.43, 262.9)]),
 (84.52, 90.84, [(262.9, 265.53), (269.73, 272.03), (279.77, 280.9)]),
 (90.84, 99.46, [(332.6, 339.57), (281.9, 283.5)]),
 (99.46, END, [(289.4, 293.3)]),
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
