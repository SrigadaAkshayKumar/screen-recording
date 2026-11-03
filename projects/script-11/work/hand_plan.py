"""Hand-built plan for script-11 (Canva bulk-create from Google Sheets CSV; 370.4 s take, 94.552 s voiceover,
1920x1080, recorder-zoomed footage so no plan zooms). One group of source pieces per narration line (start = line
start); windows come from freezedetect (n=0.002, d=0.8) gaps and 1 s contact sheets."""
import json
P = 'projects/script-11/work/'
END = 94.552
# (out_start, [(src_a, src_b[, fixed_out_duration])])
L = [
 (0.0,   [(1.0, 2.8, 1.8), (13.0, 17.9)]),                       # L1 intro: Canva home -> Sheets tab opens
 (6.74,  [(19.7, 22.9), (27.3, 29.6), (34.0, 36.3)]),            # L2 type Name / Offer / Website headers
 (12.26, [(44.7, 46.6), (47.6, 49.1)]),                          # L3 one row per design (data filled in)
 (15.18, [(49.9, 53.0)]),                                        # L4 three rows with names/offers
 (18.92, [(62.7, 64.1), (70.1, 71.6), (74.1, 75.4)]),            # L5 headings row, empty rows below
 (23.08, [(82.9, 85.0), (87.8, 90.8)]),                          # L6 File > Download > CSV
 (28.84, [(92.6, 94.9), (97.4, 98.4), (101.8, 104.9)]),          # L7 open Canva template, text boxes
 (34.04, [(107.5, 109.4), (112.7, 115.0)]),                      # L8 shared items left alone
 (38.78, [(129.5, 130.7), (159.6, 161.4)]),                      # L9 Apps -> Bulk Create
 (41.3,  [(167.0, 171.6)]),                                      # L10 Upload data, pick CSV
 (45.34, [(171.6, 173.6), (176.7, 178.7)]),                      # L11 Match and fill fields, inspect
 (49.3,  [(195.2, 198.2), (200.3, 202.6)]),                      # L12 select text box, Match data, connect
 (53.78, [(206.4, 207.7)]),                                      # L13 repeat for remaining field
 (55.08, [(178.9, 185.0)]),                                      # L14 Name / Offer matches on the text boxes
 (61.86, [(233.6, 237.0)]),                                      # L15 results, longest entries
 (65.32, [(248.0, 250.6)]),                                      # L16 back to the template
 (68.06, [(264.0, 268.4), (270.0, 271.3)]),                      # L17 creation options panel
 (73.84, [(219.5, 222.2), (224.0, 225.2), (226.6, 227.3)]),      # L18 create design, open result
 (77.3,  [(300.7, 303.0), (310.3, 312.3)]),                      # L19 sheet vs generated batch
 (81.3,  [(324.7, 330.8)]),                                      # L20 editing the sheet later
 (86.76, [(351.6, 355.6)]),                                      # L21 download a new CSV
 (90.76, [(360.3, 364.4)]),                                      # L22 back in Canva (closing)
]
segs, prev = [], None
for i, (o0, pieces) in enumerate(L):
    o1 = L[i + 1][0] if i + 1 < len(L) else END
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    var = [p for p in pieces if len(p) == 2]
    tot = sum(b - a for a, b in var)
    t = o0
    for j, p in enumerate(pieces):
        a, b = p[0], p[1]
        if len(p) == 3:
            dur = p[2]
        else:
            dur = (b - a) / tot * (o1 - o0 - fixed)
        e = o1 if j == len(pieces) - 1 else t + dur
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b
        print(f"L{i+1:<2} {t:7.2f}-{e:7.2f} {(b-a)/(e-t):.2f}x src {a}-{b}")
        t = e
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
