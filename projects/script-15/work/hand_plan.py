"""Hand-built plan for script-15 (recording has baked-in recorder zoom: no zooms/ripples; 220 s of footage, much of it
static, for a 102.6 s voiceover; pieces are chosen on moving spans from freezedetect, 0.75-1.5x)."""
import json
P = 'projects/script-15/work/'
END = 102.586
G = [
 (0, 12.68, [(8.2, 19.4)]),
 (12.68, 17.34, [(21.9, 28.8)]),
 (17.34, 21.56, [(31.5, 37.8)]),
 (21.56, 25.8, [(44.3, 46.9), (51.57, 54.2)]),
 (25.8, 29.32, [(66.0, 68.1), (71.6, 73.4)]),
 (29.32, 32.34, [(78.5, 83.0)]),
 (32.34, 36.42, [(97.6, 102.83)]),
 (36.42, 38.8, [(120.4, 123.4)]),
 (38.8, 43.18, [(123.4, 129.9)]),
 (43.18, 47.9, [(129.9, 134.63)]),
 (47.9, 52.82, [(135.83, 141.63)]),
 (52.82, 55.54, [(144.37, 146.47)]),
 (55.54, 58.76, [(149.53, 152.5)]),
 (58.76, 62.94, [(152.5, 156.5)]),
 (62.94, 68.2, [(157.67, 162.5)]),
 (68.2, 73.44, [(175.97, 177.13), (105.23, 108.77)]),
 (73.44, 81.68, [(110.17, 112.7), (113.97, 116.27), (85.67, 87.63)]),
 (81.68, 86.94, [(123.9, 129.0)]),
 (86.94, 88.78, [(161.0, 162.8)]),
 (88.78, 94.06, [(178.9, 183.87)]),
 (94.06, 97.86, [(189.5, 191.87), (193.5, 195.3)]),
 (97.86, END, [(198.0, 199.4), (206.97, 209.67)]),
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
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 220.7}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
