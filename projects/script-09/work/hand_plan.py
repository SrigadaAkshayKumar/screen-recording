"""Hand-built plan for script-09 (298.7 s take, 85.96 s voiceover, 1920x1080, baked recorder zoom: no zooms/ripples).
One group per narration line, pieces chosen by what each source range shows (see output/report.md)."""
import json
P = 'projects/script-09/work/'
END = 85.96
STARTS = [0,6.18,8.94,11.58,16.22,21.34,27.3,32.56,35.28,39.9,43.94,46.86,51.7,58.78,62.8,65.34,69.88,73.8,81.74,END]
PIECES = [
 [(9.1, 15.0)],                      # 1 intro: page + border frame
 [(20.9, 23.7)],                     # 2 click Elements, panel opens
 [(86.5, 89.2)],                     # 3 search rectangle, add it
 [(97.0, 102.0)],                    # 4 resize by corner
 [(103.0, 108.2)],                   # 5 fit inside page edges
 [(116.5, 121.0), (123.5, 125.0)],   # 6 fill colour -> transparent
 [(130.7, 135.2)],                   # 7 stroke style, solid, weight
 [(144.0, 146.7)],                   # 8 stroke colour
 [(136.0, 138.0), (141.2, 143.8)],                   # 9 thin line / weight
 [(179.5, 183.6)],                   # 10 Position panel
 [(216.5, 219.5)],                   # 11 even spacing, finished border
 [(269.3, 273.4)],                   # 12 lock
 [(22.0, 23.6), (27.0, 29.0), (33.0, 36.2)],                     # 13 search Elements for border graphics
 [(71.3, 75.3)],                     # 14 graphics panel
 [(213.0, 215.6)],                   # 15 "part tutorials skip"
 [(246.8, 251.4)],                   # 16 transparency fades outline
 [(254.2, 258.0)],                   # 17 remove fill
 [(270.7, 274.3), (278.5, 282.8)],   # 18 duplicate / next page
 [(288.0, 292.2)],                   # 19 download
]
segs, prev_end = [], None
for i, pieces in enumerate(PIECES):
    o0, o1 = STARTS[i], STARTS[i + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"line {i+1:2d} {o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
