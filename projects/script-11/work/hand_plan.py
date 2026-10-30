"""Hand-built plan for script-11 (Canva website sections, 198.8 s recording, 103.05 s voiceover, no zooms: baked recorder zoom).
One group of source pieces per narration line (start = line start); pieces come from freezedetect moving windows."""
import json
P = 'projects/script-11/work/'
END = 103.05
L = [
 (0.0,   [(178.63, 185.2)]),                         # L1 intro: finished live site
 (6.58,  [(6.0, 11.2)]),                             # L2 search 'website', results
 (11.82, [(11.2, 14.27), (19.9, 21.9)]),             # L3 website template opens
 (16.76, [(22.0, 27.17), (31.5, 32.7)]),             # L4 top section / heading
 (23.42, [(44.0, 47.4)]),                            # L5 replace image
 (26.8,  [(71.0, 74.3)]),                            # L6 bottom: Add section
 (30.1,  [(63.53, 66.53), (68.67, 69.57), (74.3, 75.4)]),  # L7 second section
 (34.88, [(75.4, 78.4)]),                            # L8 more sections
 (37.8,  [(58.57, 59.83), (107.5, 110.0)]),          # L9 fonts / button styles
 (41.28, [(139.0, 142.8), (143.67, 146.0)]),         # L10 structure
 (47.4,  [(113.37, 115.0), (117.43, 119.37), (120.83, 122.37)]),  # L11 link control
 (51.82, [(123.4, 128.3)]),                          # L12 test links
 (56.38, [(131.8, 135.7)]),                          # L13 open Preview
 (60.24, [(146.0, 152.03)]),                         # L14 check order / mobile
 (65.84, [(153.63, 155.13), (156.77, 158.0)]),       # L15
 (68.46, [(93.17, 93.97), (94.97, 99.47)]),          # L16 add section vs page
 (73.26, [(71.5, 74.5)]),                            # L17 sections
 (76.3,  [(88.0, 90.3)]),                            # L18 another page
 (78.62, [(186.0, 186.8), (187.6, 191.33)]),         # L19 single page, scrolling
 (84.42, [(158.0, 162.07), (168.23, 169.1)]),        # L20 Publish dropdown
 (88.86, [(171.0, 173.5), (174.5, 175.6)]),  # L21 settings
 (93.16, [(171.5, 173.5), (178.63, 180.5)]),         # L22 domain
 (97.6,  [(192.23, 197.7)]),                         # L23 live site
]
segs, prev = [], None
for i, (o0, pieces) in enumerate(L):
    o1 = L[i + 1][0] if i + 1 < len(L) else END
    tot = sum(b - a for a, b in pieces)
    t = o0
    for j, (a, b) in enumerate(pieces):
        e = o1 if j == len(pieces) - 1 else t + (b - a) / tot * (o1 - o0)
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b
        print(f"{t:7.2f}-{e:7.2f} {(b-a)/(e-t):.2f}x src {a}-{b}")
        t = e
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
