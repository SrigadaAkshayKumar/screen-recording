"""Hand-built plan for script-14 (283 s recorder-zoomed recording, 90.558 s voiceover).
Pieces are (src_a, src_b, speed) taken from the freezedetect moving windows of the source;
out times are derived and the slack is spread over the pieces. No zooms/ripples (baked-in zoom)."""
import json
P = 'projects/script-14/work/'
D = 90.558
PIECES = [  # src_a, src_b, speed
 (9.2, 12.75, 0.76),     # homepage / create dialog      L1
 (15.8, 19.9, 0.91),     # search T-shirt, new design    L2
 (24.6, 32.1, 1.19),     # custom size, blank canvas
 (45.5, 49.4, 0.87),     # template applied              L3
 (64.9, 67.3, 1.3),
 (77.7, 80.5, 0.95),     # text edit                     L4
 (81.3, 86.0, 1.35),     # font size
 (101.6, 117.0, 1.5),    # upload artwork, insert        L5
 (129.6, 137.9, 1.5),    # arrange / centre              L6
 (138.9, 141.4, 1.0),    # check small text              L7
 (147.0, 160.5, 1.5),    # background colour test        L8-9
 (234.4, 250.0, 1.5),    # T-shirt mockup                L10-12
 (252.0, 257.0, 1.2),    # background colour removed     L13
 (193.0, 201.0, 1.5),    # share + download panel        L14
 (203.7, 206.9, 1.4),    # file type PNG
 (210.9, 216.9, 1.5),    # transparent background, size  L15
 (220.7, 223.1, 1.0),    # download completes            L16
 (226.3, 232.0, 1.4),    # file picker                   L17
 (262.6, 265.8, 1.0),    # shirt with artwork            L18
 (267.0, 268.4, 1.0),    # end                           L19
]
tot = sum((b - a) / s for a, b, s in PIECES)
k = tot / D  # >1 means too long: speed up everything slightly
segs, prev, t = [], None, 0.0
for i, (a, b, s) in enumerate(PIECES):
    d = (b - a) / s / k
    o1 = D if i == len(PIECES) - 1 else round(t + d, 3)
    seg = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        seg["xfade"] = True
    segs.append(seg); prev = b; t = o1
    print(i, a, b, round((b - a) / (o1 - seg["out_start"]), 2), seg["out_start"], o1)
A = [("A1", 194.0, 1590, 100, "Share button", "Share panel opens", 196.0, "low"),
     ("A2", 211.0, 1540, 600, "Transparent background toggle", "toggle turns on", 212.0, "low"),
     ("A3", 215.0, 1100, 880, "Download button", "download starts", 220.7, "low")]
actions = {"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 283.433},
           "sync": {"clicks_offset": 0, "source": "frames"},
           "actions": [{"id": i, "t_click": t_, "x": x, "y": y, "kind": "click", "target": tg, "result": r,
                        "t_result_visible": tr, "confidence": c} for i, t_, x, y, tg, r, tr, c in A],
           "junk": []}
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [], "ripples": [],
        "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(actions, open(P + 'actions.json', 'w'), indent=1)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
