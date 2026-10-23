"""Hand-built plan for script-01 (586 s recording, 122.7 s voiceover; baked-in recorder zoom: no zooms/ripples).
One group per narration line: (out_start, out_end, [(src_a, src_b)...]). Pieces share the group's speed."""
import json
P = 'projects/script-01/work/'
END = 122.694
B = [0, 7.86, 12.22, 15.8, 19.54, 27.24, 31.6, 37.12, 43.24, 47.56, 50.6, 54.58, 57.84, 65.14, 68.32, 70.62, 72.4,
     78.02, 81.2, 86.12, 89.34, 95.12, 97.44, 100.88, 107.22, 111.0, 115.86, 118.38, END]
S = [
 [(0.0, 7.0)],                          # L1 intro: title deck, pages
 [(16.2, 21.9)],                        # L2 create blank presentation
 [(21.9, 24.7)],                        # L3 each page = one question
 [(30.5, 34.2)],                        # L4 plan note (deck, no matching footage)
 [(54.8, 61.1)],                        # L5 build first page
 [(61.1, 64.7)],                        # L6 label A B C
 [(74.4, 79.6)],                        # L7 page thumbnail, clock, timing
 [(79.8, 80.8), (83.2, 87.0)],          # L8 element timing (no footage: page timing popup)
 [(91.0, 94.3)],                        # L9 timing handles
 [(94.3, 96.6)],                        # L10 keep question visible
 [(96.6, 98.4), (104.4, 106.8)],        # L11 Apps, search Bulk Create
 [(119.3, 121.7), (123.2, 125.0)],      # L12 Bulk Create, Enter data manually
 [(125.0, 128.0), (189.0, 196.0)],      # L13 clear table, add columns
 [(224.0, 226.4), (254.0, 255.8)],      # L14 rows, Done
 [(255.8, 258.2)],                      # L15 Match and Fill Fields
 [(258.2, 260.2)],                      # L16 review connections
 [(265.6, 268.0), (272.4, 275.6)],                      # L17 correct a connection
 [(402.0, 405.2)],                      # L18 answer box uses Answer
 [(373.0, 378.0)],                      # L19 preview data
 [(473.5, 477.0)],                      # L20 More options
 [(477.0, 482.8)],                      # L21 output, create
 [(492.5, 495.0)],                      # L22 result opens
 [(495.0, 498.2)],                      # L23 preview does not play timing
 [(498.2, 504.5)],                      # L24 play generated design
 [(540.0, 543.8)],                      # L25 correct element timing
 [(556.0, 562.0)],                      # L26 Share, Download, MP4
 [(565.5, 568.0)],                      # L27 select pages, download
 [(569.0, 573.3)],                      # L28 watch exported file
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
