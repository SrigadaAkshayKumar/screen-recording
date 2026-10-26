"""Hand-built plan for script-11 (printable calendar in Canva, 464 s recording, 99.056 s voiceover, no zooms: baked recorder zoom).
One group of source pieces per narration line (start = line start); pieces come from freezedetect moving windows."""
import json
P = 'projects/script-11/work/'
END = 99.056
# (line out_start, [(src_start, src_end), ...])
L = [
 (0.0,   [(299.8, 307.74)]),                         # L1 intro: finished calendar with photo
 (7.94,  [(9.73, 11.93)]),                           # L2 size dialog
 (9.9,   [(13.83, 16.4), (18.23, 21.3)]),            # L3 90x120 mm
 (16.4,  [(23.83, 25.1), (30.83, 33.13)]),           # L4 create custom
 (19.44, [(61.63, 63.8), (75.0, 77.3)]),             # L5 search templates
 (23.16, [(92.1, 94.8)]),                            # L6 simple layout
 (25.88, [(101.37, 102.63), (103.63, 105.0), (106.0, 108.83), (114.17, 116.5)]),  # L7 copy/paste
 (32.18, [(117.0, 121.33)]),                         # L8 group/resize
 (35.7,  [(125.0, 128.03), (129.47, 130.97)]),       # L9 position
 (40.36, [(131.9, 133.6)]),                          # L10 month/year
 (42.04, [(134.0, 136.0)]),                          # L11 weekday headings
 (43.86, [(138.8, 141.57), (147.77, 149.33)]),       # L12 first day
 (48.86, [(150.23, 153.03), (154.4, 157.0)]),        # L13 text boxes
 (53.92, [(163.13, 165.0), (296.0, 297.4)]),         # L14 heading + photo
 (57.2,  [(171.7, 174.5), (318.67, 321.5)]),         # L15 font
 (61.78, [(346.0, 350.2)]),                          # L16 contrast
 (65.96, [(187.3, 189.7)]),                          # L17
 (68.36, [(220.0, 225.2)]),                          # L18 month name
 (73.56, [(263.97, 266.7), (268.5, 269.9)]),         # L19 verify grid
 (77.96, [(391.5, 396.96)]),                         # L20 duplicate
 (83.42, [(414.5, 417.1)]),                          # L21 download PDF
 (86.0,  [(419.87, 422.5)]),                         # L22 print
 (88.66, [(432.37, 434.7), (437.87, 440.27), (449.67, 452.13)]),  # L23
 (95.72, [(453.5, 456.84)]),                         # L24
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
