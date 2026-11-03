"""Hand-built plan for script-10 (219.4 s Canva diagonal-crop take, 90.647 s / 20-line voiceover, baked recorder zoom: no zooms/ripples).
One group of source pieces per narration line, starting 0.2 s before the line; windows from freezedetect (n=0.002, d=0.8) + 1 s sheets.
A third tuple item fixes a piece's output duration (static opening)."""
import json
P = 'projects/script-10/work/'
END = 90.647
S = [0.0, 5.9, 8.32, 13.32, 15.82, 19.98, 22.9, 25.1, 34.04, 37.78, 41.06, 44.0, 49.92, 51.64, 57.24, 63.32, 68.42, 74.92, 78.24, 83.38, END]
G = [
 [(0.0, 4.2, 2.2), (4.2, 7.6)],                  # L1 intro: home screen, Create a design menu
 [(8.9, 10.0), (16.9, 18.4)],                    # L2 open design, go to Elements
 [(20.2, 24.6)],                                 # L3 Frames category (click ~21.0), frames list
 [(24.6, 27.1)],                                 # L4 choose a triangle frame, it lands on the page
 [(27.1, 31.3)],                                 # L5 image frame on page
 [(36.9, 39.6)],                                 # L6 frame as container (zoomed view)
 [(65.0, 67.3)],                                 # L7 resize the frame (drag corner handle)
 [(60.3, 62.6), (67.3, 69.9), (71.8, 74.1)],     # L8 right-triangle frame placed large, side free
 [(79.8, 83.5)],                                 # L9 Uploads panel, drag photo to frame
 [(83.5, 86.7)],                                 # L10 photo fills frame on release
 [(86.8, 89.5)],                                 # L11 double-click -> crop panel
 [(99.0, 103.0), (110.8, 112.4)],                # L12 move image in shape
 [(103.0, 104.7)],                               # L13 click outside / Done
 [(154.6, 156.8), (158.3, 161.7)],                             # L14 rotate frame
 [(112.4, 114.5), (115.8, 119.8)],               # L15 bird inside triangle, away from edge
 [(119.8, 124.0)],                               # L16 crop result looks deliberate
 [(144.0, 147.7), (149.8, 152.3)],               # L17 rotate photo, mask stays
 [(161.9, 165.2)],                               # L18 frame defines visible part
 [(189.5, 194.6)],                               # L19 double-click, hidden content, crop again
 [(195.0, 198.0), (200.0, 202.7), (205.8, 209.0)],  # L20 Share > Download, file type list, transparent bg
]
segs, prev_end = [], None
for i, pieces in enumerate(G):
    o0, o1 = S[i], S[i + 1]
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    sp = sum(p[1] - p[0] for p in pieces if len(p) == 2) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"L{i+1:<2} {o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 219.433}, "sync": {"source": "frames"},
           "actions": [], "junk": []}, open(P + 'actions.json', 'w'), indent=1)
