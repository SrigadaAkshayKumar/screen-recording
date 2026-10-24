"""Hand-built plan for script-11 (portfolio website, 310 s recording, 94.23 s voiceover, no zooms: baked recorder zoom).
Pieces come from freezedetect moving windows of the source; pieces follow the narration order, jumps cross-fade."""
import json
P = 'projects/script-11/work/'
END = 94.23
# (out_start, out_end, src_start, src_end)
G = [
 (0, 4.7, 300.2, 304.9),        # L1 intro: finished site scrolling
 (4.7, 8.0, 10.0, 14.8),        # L2 search popup, typing
 (8.0, 10.6, 16.2, 19.8),       # L3 results, editor opens
 (10.6, 12.8, 34.4, 38.4),      # L3-4 template applied
 (12.8, 15.6, 40.2, 42.3),
 (15.6, 17.7, 44.7, 46.3),      # L4 replace name
 (17.7, 21.0, 46.3, 49.0),      # L5
 (21.0, 23.6, 66.9, 69.5),      # L6 uploads panel
 (23.6, 29.0, 69.5, 75.5),      # L7 images
 (29.0, 34.3, 75.5, 83.0),      # L8 drag image
 (34.3, 37.9, 88.3, 92.2),      # L9 add section
 (37.9, 40.6, 92.2, 95.0),      # L10
 (40.6, 42.8, 108.3, 110.8),    # L10 scroll
 (42.8, 47.9, 144.0, 150.0),    # L11 contact button, link
 (47.9, 50.9, 110.6, 116.4),    # L12 contact details
 (50.9, 53.9, 154.0, 157.4),    # L13 publish website
 (53.9, 55.5, 158.7, 160.3),    # L14 settings open
 (55.5, 57.9, 165.0, 167.8),    # L14 settings zoomed
 (57.9, 59.9, 196.2, 198.4),    # L14 toggles
 (59.9, 65.9, 199.0, 207.0),    # L15 preview desktop/mobile
 (65.9, 68.5, 215.8, 221.0),    # L16 publish panel
 (68.5, 71.9, 233.3, 236.0),    # L16 address
 (71.9, 74.6, 255.0, 257.7),    # L17 publishing
 (74.6, 78.7, 257.7, 261.8),    # L18 live, new tab
 (78.7, 83.9, 261.8, 267.8),    # L19 share link
 (83.9, 86.5, 281.0, 284.8),    # L20 private window
 (86.5, 89.0, 287.7, 290.2),    # L20 site loads
 (89.0, END, 295.9, 301.1),     # L21 site scroll
]
segs, prev = [], None
for o0, o1, s0, s1 in G:
    s = {"src_start": s0, "src_end": s1, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(s0 - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = s1
    print(f"{o0:6.2f}-{o1:6.2f} {(s1-s0)/(o1-o0):.2f}x src {s0}-{s1}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
