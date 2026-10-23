"""Hand-built plan for script-11 (recording has baked-in recorder zoom: no zooms/ripples; 171 s of footage for
96.27 s of voiceover; pieces follow the narration order, jumps are cross-faded)."""
import json
P = 'projects/script-11/work/'
END = 96.27
# (out_start, out_end, src_start, src_end)
G = [
 (0, 5.66, 107.0, 112.66),        # L1 intro: custom font applied
 (5.66, 12.76, 7.9, 13.4),        # L2-3 download icon + download popup
 (12.76, 20.5, 19.2, 25.1),       # L4 zip extracted, folder in Explorer
 (20.5, 23.6, 25.1, 27.5),        # L5 Explorer closes, back in editor
 (23.6, 33.2, 35.4, 43.1),        # L6-7 text tab, font search, Brand click
 (33.2, 37.7, 43.1, 49.0),        # L7-8 Brand panel, brand kit picker
 (37.7, 41.03, 52.0, 57.0),       # L9 Fonts, Edit
 (41.03, 47.2, 62.8, 71.8),       # L9-10 Manage uploaded fonts, Choose files, file, Open, confirm
 (47.2, 49.92, 72.0, 77.0),       # L11 upload progress (wait, ~1.9x)
 (49.92, 51.8, 90.4, 92.4),       # L12 open design, select text box
 (51.8, 60.12, 96.3, 106.2),      # L13-14 font name, Uploaded fonts, select
 (60.12, 71.2, 106.2, 117.3),     # L15-17 check the letters
 (71.2, 78.44, 126.3, 134.4),     # L18-19 font list, regular / bold styles
 (78.44, 83.0, 144.6, 149.6),     # L20 font list scrolls
 (83.0, 86.94, 153.3, 156.3),     # L20 static font files
 (86.94, 92.52, 119.9, 124.6),    # L21 font search for the missing font
 (92.52, END, 163.8, 167.5),      # L22 brand kit fonts page, editor
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
