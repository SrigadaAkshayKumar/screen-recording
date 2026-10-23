"""Hand-built plan for script-08 (Canva mock-up tutorial). The recording has baked-in recorder zoom: no zooms/ripples.
281.8 s of footage for a 91.8 s voiceover: pieces picked per narration line at 0.8-1.2x, scenes.json stills avoided."""
import json
P = 'projects/script-08/work/'
END = 91.765
# (out_start, out_end, [(src_a, src_b)])
G = [
 (0, 5.56, [(1.2, 6.6)]),
 (5.56, 15.3, [(16.8, 27.0)]),
 (15.3, 23.5, [(30.4, 35.6), (43.6, 45.0)]),
 (23.5, 26.22, [(66.0, 68.8)]),
 (26.22, 32.72, [(54.0, 58.5), (68.8, 70.8)]),
 (32.72, 34.4, [(45.0, 46.8)]),
 (34.4, 38.12, [(92.6, 96.5)]),
 (38.12, 40.92, [(96.5, 99.7)]),
 (40.92, 44.78, [(114.5, 118.4)]),
 (44.78, 50.02, [(118.5, 121.4), (125.4, 128.0)]),
 (50.02, 52.64, [(140.6, 143.6)]),
 (52.64, 58.32, [(172.0, 177.8)]),
 (58.32, 63.38, [(182.4, 187.4)]),
 (63.38, 69.74, [(205.9, 210.6), (216.6, 219.2)]),
 (69.74, 74.5, [(231.0, 236.5)]),
 (74.5, 78.04, [(236.5, 240.5)]),
 (78.04, 80.84, [(247.5, 250.8)]),
 (80.84, 87.7, [(256.0, 258.8), (262.8, 267.8)]),
 (87.7, END, [(273.7, 277.6)]),
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
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
