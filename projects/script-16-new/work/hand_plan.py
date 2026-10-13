"""Hand-built plan for script-16-new: one source piece per narration line (recording has baked-in
recorder zoom and long idle spells, so no zooms/ripples)."""
import json
P = 'projects/script-16-new/work/'
G = [(0, 7.06, 17.0, 24.0), (7.06, 12.06, 24.0, 28.0), (12.06, 17.08, 28.0, 32.0),
     (17.08, 24.66, 33.0, 44.0), (24.66, 27.64, 76.3, 79.0), (27.64, 32.72, 85.5, 90.0),
     (32.72, 37.38, 49.0, 53.5), (37.38, 42.74, 96.0, 101.5), (42.74, 46.86, 101.5, 105.0),
     (46.86, 54.62, 117.7, 125.0), (54.62, 60.6, 136.0, 142.0), (60.6, 68.06, 144.0, 151.5),
     (68.06, 74.475, 168.0, 174.5)]
segs, prev = [], None
for o0, o1, a, b in G:
    s = {"src_start": a, "src_end": b, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = b
plan = {"output": {"duration": 74.475, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
