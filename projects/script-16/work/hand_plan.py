"""Hand-built plan for script-16: one source piece per narration line (recording has baked-in
recorder zoom, no zooms/ripples)."""
import json
P = 'projects/script-16/work/'
G = [(0, 6.08, 2.3, 8.0), (6.08, 9.94, 8.0, 11.5), (9.94, 13.88, 23.0, 26.3),
     (13.88, 19.14, 26.3, 31.5), (19.14, 23.5, 44.0, 48.4), (23.5, 25.12, 63.0, 64.6),
     (25.12, 29.6, 82.0, 86.0), (29.6, 32.48, 89.0, 91.9), (32.48, 35.5, 91.9, 94.4),
     (35.5, 39.74, 120.0, 124.2), (39.74, 48.62, 94.4, 101.1), (48.62, 54.32, 103.0, 108.2),
     (54.32, 59.22, 115.0, 119.9), (59.22, 66.48, 124.2, 131.2), (66.48, 70.14, 132.8, 136.46),
     (70.14, 74.582, 136.5, 140.1)]
segs, prev = [], None
for o0, o1, a, b in G:
    s = {"src_start": a, "src_end": b, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = b
plan = {"output": {"duration": 74.582, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
