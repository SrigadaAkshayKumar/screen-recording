"""Hand-built plan for script-14 (314 s recorder-zoomed recording, 99.985 s voiceover).
Pieces are (src_a, src_b, out_a, out_b), budgeted per narration line. No zooms/ripples: the footage has baked-in zoom."""
import json, sys
P = 'projects/script-14/work/'
D = 99.985
PIECES = [
 (0.0, 1.3, 0, 1.73),
 (5.5, 14.9, 1.73, 14.26),
 (14.9, 17.5, 14.26, 16.46),
 (17.5, 18.9, 16.46, 17.2),
 (19.9, 20.9, 17.2, 18.42),
 (20.9, 24.0, 18.42, 19.97),
 (24.0, 26.8, 19.97, 23.54),
 (26.8, 34.5, 23.54, 30.64),
 (89.1, 95.4, 30.64, 35.98),
 (175.0, 179.0, 35.98, 39.62),
 (123.2, 129.4, 39.62, 45.82),
 (233.0, 236.4, 45.82, 49.22),
 (245.2, 248.4, 49.22, 52.42),
 (283.2, 287.1, 52.42, 56.3),
 (289.0, 293.0, 56.3, 60.22),
 (293.0, 299.0, 60.22, 66.08),
 (299.0, 303.5, 66.08, 70.56),
 (303.5, 305.2, 70.56, 72.8),
 (256.9, 262.3, 72.8, 78.08),
 (262.3, 267.0, 78.08, 83.54),
 (267.0, 269.2, 83.54, 85.76),
 (271.8, 274.0, 85.76, 87.92),
 (279.1, 285.0, 87.92, 93.8),
 (199.0, 205.19, 93.8, D),
]
segs, prev = [], None
for a, b, o0, o1 in PIECES:
    s = {"src_start": a, "src_end": b, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = b
A = [  # id, t_click, x, y, target, result, t_result, confidence
 ("A1", 234.5, 1860, 167, "Share button", "Share design panel opens", 244.0, "low"),
 ("A2", 258.9, 1657, 697, "Create template link button", "template link created and copied", 264.0, "low"),
 ("A3", 284.2, 1642, 760, "Download button in the download panel", "PDF downloads, browser shows the file", 290.0, "low"),
]
actions = {"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 314.3},
           "sync": {"clicks_offset": 0, "source": "frames"},
           "actions": [{"id": i, "t_click": t, "x": x, "y": y, "kind": "click", "target": tg, "result": r,
                        "t_result_visible": tr, "confidence": c} for i, t, x, y, tg, r, tr, c in A],
           "junk": []}
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [], "ripples": [],
        "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(actions, open(P + 'actions.json', 'w'), indent=1)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
