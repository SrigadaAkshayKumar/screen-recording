"""Hand-built plan for script-04 (new 261 s take, 85.264 s voiceover). The recording has baked-in
recorder zoom and long idle spells, so each narration line gets source pieces taken only from the
moving windows (freezedetect n=0.003 d=0.8 on the source) at 0.75-1.5x. No zooms, no ripples."""
import json
P = 'projects/script-04/work/'
END = 85.264
G = [
 (0, 6.6, [(3.2, 8.4)]),
 (6.6, 13.92, [(8.6, 10.1), (12.4, 14.4), (22.0, 24.0), (30.0, 32.1)]),
 (13.92, 16.7, [(40.0, 42.2), (47.5, 48.2)]),
 (16.7, 20.88, [(60.8, 63.5), (78.0, 79.5)]),
 (20.88, 30.46, [(72.8, 75.5), (96.4, 98.7), (99.7, 102.7), (104.0, 105.7)]),
 (30.46, 33.52, [(121.0, 124.0)]),
 (33.52, 36.48, [(129.5, 132.5)]),
 (36.48, 40.3, [(136.5, 140.3)]),
 (40.3, 46.4, [(160.5, 163.7), (166.0, 169.0)]),
 (46.4, 48.66, [(174.5, 176.8)]),
 (48.66, 54.2, [(177.0, 180.5), (214.7, 216.5)]),
 (54.2, 59.86, [(195.0, 196.9), (200.9, 202.0), (148.4, 150.6)]),
 (59.86, 62.18, [(124.0, 126.3)]),
 (62.18, 67.1, [(218.0, 219.4), (220.0, 223.0), (223.8, 224.4)]),
 (67.1, 74.22, [(224.4, 227.0), (230.0, 232.8), (248.0, 249.0)]),
 (74.22, 77.5, [(249.0, 251.0), (253.7, 255.2)]),
 (77.5, 81.1, [(80.7, 83.0), (116.8, 118.2)]),
 (81.1, END, [(255.2, 261.0)]),
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
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
