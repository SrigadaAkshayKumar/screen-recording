"""Hand-built plan for script-01 (441.6 s recording, 104.4 s voiceover; baked-in recorder zoom: no zooms/ripples).
One group per narration line: pieces share the group's speed; cross-fade at every source jump."""
import json
P = 'projects/script-01/work/'
END = 104.397
B = [0, 6.0, 11.26, 16.62, 19.36, 25.38, 31.34, 34.48, 37.44, 42.04, 46.02, 51.14, 57.42, 61.96, 66.72, 69.56,
     74.78, 77.6, 81.14, 86.38, 93.8, 96.14, 100.98, END]
S = [
 [(7.2, 10.2), (430.9, 432.9)],        # L1 intro: home zoom, finished design
 [(41.0, 44.2), (64.9, 66.8)],                     # L2 dimensions: custom size fields
 [(72.9, 76.9), (79.4, 80.9)],         # L3 bleed/safe area: template browsing
 [(20.6, 24.2)],                       # L4 homepage, Create, Custom size
 [(44.2, 45.6), (49.6, 52.2), (55.2, 56.4)],                     # L5 units, dimensions
 [(57.2, 59.5), (62.3, 65.0)],         # L6 24 by 14, create
 [(87.4, 91.4)],                       # L7 background colour
 [(101.7, 104.7)],                     # L8 extend background
 [(105.0, 108.0), (110.7, 112.2)],     # L9 elements panel
 [(110.7, 114.7)],                     # L10 simple shapes
 [(124.8, 130.0)],                     # L11 rounded rectangles
 [(179.2, 185.2)],                     # L12 numbers in zones
 [(130.0, 134.0)],                     # L13 select / group
 [(166.3, 170.3)],                     # L14 position, guides
 [(216.3, 218.6)],                     # L15 aside
 [(170.3, 174.6)],                     # L16 guides
 [(194.6, 197.0)],                     # L17 supplier
 [(225.0, 228.0)],                     # L18 measurements
 [(344.0, 348.4)],                     # L19 share, download
 [(351.4, 358.1)],                     # L20 PDF print
 [(398.9, 400.9)],                     # L21 crop marks
 [(415.6, 419.8)],                     # L22 check exported file
 [(419.8, 423.3)],                     # L23 ready
]
segs, prev = [], None
for k, pieces in enumerate(S):
    o0, o1 = B[k], B[k + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for j, (a, b) in enumerate(pieces):
        e = o1 if j == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b; t = e
    print(f"L{k+1:2d} {o0:7.2f}-{o1:7.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
