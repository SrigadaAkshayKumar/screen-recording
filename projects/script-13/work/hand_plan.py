"""Hand-built plan for script-13: each group fills one narration interval with source pieces.
Recording has baked-in recorder zoom -> no zooms/ripples."""
import json
P = 'projects/script-13/work/'
END = 104.118
G = [
 (0, 8.24, [(8.0, 14.3)]),
 (8.24, 16.14, [(14.3, 20.0), (24.2, 26.5)]),
 (16.14, 18.62, [(26.5, 28.4)]),
 (18.62, 21.98, [(31.5, 34.5)]),
 (21.98, 28.02, [(39.5, 45.0)]),
 (28.02, 36.8, [(56.0, 60.0), (80.6, 85.6)]),
 (36.8, 40.96, [(86.0, 90.0)]),
 (40.96, 45.8, [(46.5, 52.8)]),
 (45.8, 48.8, [(88.0, 91.0)]),
 (48.8, 51.06, [(92.0, 94.3)]),
 (51.06, 58.34, [(96.5, 101.5), (109.0, 111.3)]),
 (58.34, 61.02, [(114.5, 117.2)]),
 (61.02, 67.26, [(117.0, 122.0)]),
 (67.26, 71.22, [(122.0, 126.0)]),
 (71.22, 76.0, [(130.5, 135.3)]),
 (76.0, 83.78, [(135.5, 141.5)]),
 (83.78, 90.08, [(141.5, 146.3)]),
 (90.08, 97.78, [(86.0, 88.7), (94.0, 99.0)]),
 (97.78, 101.38, [(151.5, 155.1)]),
 (101.38, END, [(169.5, 172.2)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(p[1] - p[0] for p in pieces) / (o1 - o0)
    t = o0
    for k, p in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (p[1] - p[0]) / sp
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
