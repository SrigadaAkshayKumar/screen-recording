"""Hand-built plan for script-14 (286.2 s 1920x1080 recording, 99.289 s voiceover, cafe-menu take).
Pieces come from the moving windows of freezedetect (n=0.003 d=0.8) on the source. Each group starts
exactly on its narration line (lines.json start) and its pieces are scaled to fill the group."""
import json
P = 'projects/script-14/work/'
D = 99.289
L = [0, 7.1, 11.24, 15.06, 18.9, 24.22, 28.24, 34.2, 38.52, 40.2, 45.18, 49.8, 55.42, 59.4, 65.32, 67.84, 71.2, 78.1, 86.68, 91.92, 96.04, D]
G = [
 [(7.2, 14.3)], [(14.3, 17.7)], [(20.1, 24.0)],
 [(45.6, 47.5), (96.0, 97.9)],
 [(113.2, 117.7), (118.8, 119.8)],
 [(143.6, 147.6)], [(69.8, 75.8)],
 [(169.2, 171.0), (173.7, 176.5)], [(183.0, 184.8)],
 [(186.1, 188.4), (197.7, 199.9)], [(202.6, 206.6)], [(150.1, 155.7)],
 [(208.1, 212.1)], [(212.1, 216.6), (218.3, 219.8)], [(219.8, 222.3)],
 [(229.5, 232.9)], [(232.9, 239.8)],
 [(120.9, 124.7), (128.4, 129.9), (133.3, 137.3)],
 [(241.8, 245.9), (246.8, 248.0)], [(259.6, 262.0), (269.1, 270.8)], [(274.8, 278.1)],
]
segs, prev = [], None
for g, (o0, o1) in zip(G, zip(L, L[1:])):
    src = sum(b - a for a, b in g); k = src / (o1 - o0); t = o0
    for i, (a, b) in enumerate(g):
        e = o1 if i == len(g) - 1 else round(t + (b - a) / k, 3)
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": e, "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002: s["xfade"] = True
        segs.append(s); prev = b; t = e
        print(a, b, round((b - a) / (e - t + (e - t == 0) - 0 or 1), 2) if False else round((b - a) / (e - s["out_start"]), 2), s["out_start"], e)
actions = {"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 286.233},
           "sync": {"clicks_offset": 0, "source": "frames"}, "actions": [{"id": "A1", "t_click": 259.0, "x": 1440, "y": 270, "kind": "click", "target": "Download button (PDF Standard)",
                        "result": "download starts, PDF Standard toast", "t_result_visible": 261.0, "confidence": "low"}], "junk": []}
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [], "ripples": [],
        "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(actions, open(P + 'actions.json', 'w'), indent=1)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
