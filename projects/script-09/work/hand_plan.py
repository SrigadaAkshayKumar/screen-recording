"""Hand-built plan for script-09 (new 305 s take, baked-in recorder zoom elsewhere: only one zoom on the typed prompt, no ripples; 98.8 s voiceover).
Pieces come from the moving windows of the source (freezedetect n=0.003)."""
import json
P = 'projects/script-09/work/'
END = 98.824
# (out_start, out_end, [(src_a, src_b)])
G = [
 (0, 6.06, [(6.4, 11.0)]),
 (6.06, 10.48, [(11.7, 15.2)]),
 (10.48, 14.18, [(38.4, 42.1)]),
 (14.18, 36.96, [(60.0, 105.5)]),
 (36.96, 41.44, [(19.0, 21.5), (22.9, 24.3)]),
 (41.44, 44.2, [(120.4, 123.4)]),
 (44.2, 47.34, [(131.0, 137.2)]),
 (47.34, 54.1, [(191.5, 198.3)]),
 (54.1, 59.2, [(219.0, 220.9), (222.8, 225.0)]),
 (59.2, 64.18, [(246.3, 251.2)]),
 (64.18, 66.86, [(198.3, 201.0)]),
 (66.86, 74.78, [(201.0, 204.7), (207.6, 211.9)]),
 (74.78, 78.02, [(211.9, 214.6)]),
 (78.02, 81.94, [(214.6, 216.1), (249.4, 251.2)]),
 (81.94, 88.82, [(264.0, 266.9), (269.9, 272.5)]),
 (88.82, 94.38, [(272.5, 276.9)]),
 (94.38, END, [(289.3, 294.5)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [{"out_t": 15.0, "x": 960, "y": 830, "scale": 1.8, "in": 0.7, "hold": 20.8, "out": 0.7}],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
