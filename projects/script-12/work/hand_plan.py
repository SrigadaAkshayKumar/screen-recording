"""Hand-budgeted plan for script-12 (209 s recording, 75 s voiceover, baked-in recorder zoom: no zooms/ripples)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
D = 74.908
# (src_a, src_b, out_a, out_b, xfade)
Q = [
 (0.0, 5.0, 0.0, 6.67, False),        # L1 intro, cursor approaches play (0.75x)
 (5.0, 6.33, 6.67, 8.0, False),       # play clicked, video starts
 (14.3, 17.2, 8.0, 10.9, True),       # video paused (L3)
 (29.2, 33.6, 10.9, 15.3, True),      # select caption on timeline (L4)
 (38.5, 41.5, 15.3, 17.3, True),      # typing the correction
 (58.5, 64.7, 17.3, 22.9, True),      # Captions toolbar -> panel -> matching line (L5)
 (77.0, 90.0, 22.9, 32.9, True),      # edit line in panel (L6-7)
 (120.5, 134.0, 32.9, 44.9, True),    # timeline segment, drag edge (L8-9)
 (146.0, 153.0, 44.9, 51.2, True),    # caption text edit (L10-11)
 (159.8, 166.3, 51.2, 57.7, True),    # end of timeline (L12)
 (175.5, 183.2, 57.7, 65.4, True),    # replay from earlier point (L13-14)
 (183.2, 187.0, 65.4, 69.2, False),   # preview (L15)
 (193.2, 195.4, 69.2, 71.4, True),    # Share -> download panel (L16)
 (198.0, 201.5, 71.4, D, True),       # MP4 -> Download
]
segs = []
for a, b, oa, ob, x in Q:
    s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": oa, "out_end": ob}
    if x: s["xfade"] = True
    segs.append(s)
w = json.load(open(os.path.join(here, "words.json")))
W = w["words"] if isinstance(w, dict) else w
def idx(t): return min(range(len(W)), key=lambda i: abs(W[i]["start"] - t))
plan = {"output": {"duration": D, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False},
        "notes": ["hand-built by hand_plan.py; recorder zoom is baked in so no zooms/ripples"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
