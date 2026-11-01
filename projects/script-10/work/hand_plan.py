"""Hand-built plan for script-10 (243.133 s recording, 97.849 s voiceover, no clicks log, no zooms/ripples).
Pieces come from freezedetect (n=0.002, d=0.8) moving windows; one group per narration line, starting on the line's start.
A piece may carry a 3rd value: a fixed output duration (static opening shot, 1x)."""
import json
P = 'projects/script-10/work/'
END = 97.849
G = [
 (0, 9.82, [(6.0, 8.4, 2.4), (12.2, 18.0)]),
 (9.82, 16.58, [(19.0, 23.6), (35.3, 39.8)]),
 (16.58, 23.18, [(63.5, 68.7), (71.2, 74.0)]),
 (23.18, 27.2, [(41.2, 44.5)]),
 (27.2, 34.96, [(46.5, 48.4), (49.9, 52.7), (56.4, 57.7)]),
 (34.96, 37.82, [(76.4, 78.1), (95.0, 96.0)]),
 (37.82, 43.64, [(101.8, 105.8), (109.5, 113.0)]),
 (43.64, 48.82, [(125.7, 131.0)]),
 (48.82, 56.84, [(137.1, 144.5), (146.2, 148.5)]),
 (56.84, 63.0, [(162.7, 166.5), (177.7, 179.3)]),
 (63.0, 65.74, [(195.8, 198.5)]),
 (65.74, 69.74, [(198.5, 202.0)]),
 (69.74, 75.68, [(202.0, 204.8), (205.8, 207.5)]),
 (75.68, 81.42, [(207.5, 209.1), (222.1, 224.3), (237.3, 240.0)]),
 (81.42, 85.5, [(214.8, 218.0)]),
 (85.5, 91.58, [(218.0, 219.4), (225.9, 230.0)]),
 (91.58, END, [(230.0, 236.3)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    free = [p for p in pieces if len(p) == 2]
    sp = sum(b - a for a, b in free) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        dur = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + dur
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 243.133}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
