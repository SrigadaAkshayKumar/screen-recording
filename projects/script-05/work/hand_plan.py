"""Hand-built plan for script-05 (270 s Canva poster + Acrobat tiling take, 91.6 s voiceover, baked recorder zoom).
One group per narration line, starting on the line's start; (a, b) pieces share the remaining time, (a, b, speed) are fixed."""
import json
P = 'projects/script-05/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
G = [
 (0, 10.82, [(7.3, 9.3, 1.0), (9.3, 13.7), (13.7, 15.3, 1.0), (15.3, 16.4)]),  # L1+L2 home, click Create, dialog                         # L1 home, cursor to Create
                                           # L2 Create a design dialog
 (10.82, 16.4, [(16.4, 18.3), (18.3, 22.3, 2.0), (23.5, 24.7)]),          # L3 custom size 60x40, Create new design
 (16.4, 19.0, [(30.4, 33.6)]),                                             # L4 uploads panel, image placed
 (19.0, 23.36, [(33.6, 36.6), (36.6, 39.8, 2.0)]),                         # L5 fit image / crop
 (23.36, 28.58, [(44.6, 51.8)]),                                           # L6 zoom on image, File menu
 (28.58, 33.7, [(53.4, 60.8)]),                                            # L7 Share, Download, PDF, Print
 (33.7, 37.8, [(66.0, 70.1)]),                                             # L8 Download click, toast
 (37.8, 41.84, [(77.6, 81.0), (85.2, 86.2)]),                              # L9 open PDF in Acrobat
 (41.84, 48.34, [(94.2, 95.4, 1.0), (101.8, 103.6, 1.0), (104.4, 109.4)]), # L10 Print, printer, paper size A4
 (48.34, 51.54, [(122.0, 125.2)]),                                         # L11 Poster
 (51.54, 54.28, [(189.6, 192.4)]),                                         # L12 tiles across sheets
 (54.28, 59.82, [(131.6, 134.6), (134.6, 139.2, 2.0)]),                    # L13 tile scale
 (59.82, 65.04, [(145.3, 148.0), (150.6, 154.2)]),                         # L14 overlap, cut marks
 (65.04, 67.76, [(179.4, 182.1)]),                                         # L15 preview / sheet count
 (67.76, 72.76, [(186.0, 188.9), (192.8, 196.0)]),                                         # L16 settings change preview
 (72.76, 78.16, [(45.0, 47.85, .75), (198.6, 200.2, 1.0)]),                # L17 Canva artwork -> Acrobat tiles
 (78.16, 85.0, [(234.5, 238.0), (252.3, 255.0)]),                     # L18 Multiple
 (85.0, END, [(257.6, 260.2, 2.0), (260.2, 266.5)]),                                            # L19 Print
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    outs = [(p[1] - p[0]) / p[2] for p in pieces if len(p) == 3]
    fill = [p for p in pieces if len(p) == 2]
    sp = sum(p[1] - p[0] for p in fill) / (o1 - o0 - sum(outs)) if fill else 1
    t = o0
    for k, p in enumerate(pieces):
        d = (p[1] - p[0]) / (p[2] if len(p) == 3 else sp)
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]
        print('%6.2f-%6.2f src %6.1f-%6.1f %.2fx%s' % (t, end, p[0], p[1], (p[1]-p[0])/(end-t), ' X' if s.get('xfade') else ''))
        t = end
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
