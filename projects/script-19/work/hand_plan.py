"""Hand-built plan for script-19 (383 s take, 106.02 s voiceover, 1920x1080, baked recorder zoom: no zooms/ripples).
Moving windows (freezedetect n=0.003 d=0.8) mapped to narration lines by what they show (see sync-notes.md)."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
G = [
 (0, 7.2, [(11.23, 13.7), (17.5, 21.0)]),
 (7.2, 10.86, [(21.0, 24.0)]),
 (10.86, 17.86, [(24.0, 26.57), (31.9, 33.4), (33.4, 35.5)]),
 (17.86, 21.36, [(42.8, 46.3)]),
 (21.36, 23.44, [(46.3, 47.7), (48.6, 49.4)]),
 (23.44, 27.1, [(94.9, 96.13), (97.0, 98.17), (99.5, 100.9)]),
 (27.1, 32.22, [(100.9, 101.43), (102.63, 103.93), (105.57, 108.0)]),
 (32.22, 36.22, [(108.0, 111.27)]),
 (36.22, 39.12, [(113.37, 115.9)]),
 (39.12, 44.78, [(168.3, 171.53), (172.57, 175.0)]),
 (44.78, 48.16, [(122.6, 124.9), (126.1, 127.4)]),
 (48.16, 55.64, [(232.03, 234.8), (235.6, 240.0)]),
 (55.64, 60.18, [(242.97, 244.27), (248.33, 251.5)]),
 (60.18, 64.58, [(251.5, 253.07), (254.9, 256.2), (228.3, 229.57)]),
 (64.58, 68.94, [(263.17, 267.13), (268.23, 269.5)]),
 (68.94, 71.82, [(269.5, 272.4)]),
 (71.82, 77.76, [(272.4, 275.83), (276.9, 278.57)]),
 (77.76, 83.06, [(286.5, 290.67), (309.57, 310.97)]),
 (83.06, 88.14, [(204.23, 207.3), (240.0, 241.4)]),
 (88.14, 96.4, [(318.83, 323.4), (333.67, 337.0), (338.4, 339.8)]),
 (96.4, 99.68, [(366.67, 369.9)]),
 (99.68, END, [(369.9, 377.37)]),
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
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
