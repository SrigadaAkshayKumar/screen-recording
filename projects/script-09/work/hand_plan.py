"""script-09 (244 s Canva bulk bg-remover take, 101.611 s voiceover, 1920x1080, baked recorder zoom). Re-edit:
every narration line gets the footage that SHOWS its step (per-line map in output/report.md).
Third tuple item = fixed output duration (static source played slowly/at <=2x). One group per line start."""
import json
P = 'projects/script-09/work/'
END = 101.611
G = [
 # L1+L2 home screen: short static + home zoom
 (0, 5.48, [(2.9, 5.13, 2.3), (5.13, 7.9)]),
 # L3 finished cutouts folder (what the tutorial produces)
 (5.48, 11.38, [(91.7, 94.3), (105.1, 108.3)]),
 # L4 home -> Projects, All projects -> Add new
 (11.38, 14.54, [(8.0, 9.17), (10.6, 12.4)]),
 # L5 New folder, name typed, Create folder
 (14.54, 19.78, [(12.6, 15.2), (16.2, 19.5)]),
 # L6 folder created / opened, Add new menu
 (19.78, 22.12, [(21.0, 22.3), (24.2, 25.5)]),
 # L7 file picker with the product photos, selected, Open
 (22.12, 27.74, [(28.6, 34.2)]),
 # L8 back to folder listing, hover folder, three-dot menu
 (27.74, 32.64, [(50.0, 56.6)]),
 # L9+L10 click BG Remover, removing / removed toasts, Edited folder appears
 (32.64, 41.34, [(66.35, 73.5)]),
 # L11 folder names: edited + original
 (41.34, 45.78, [(73.5, 75.7, 2.0), (84.23, 85.0), (86.6, 88.4)]),
 # L12 open the edited folder
 (45.78, 49.1, [(88.4, 91.7)]),
 # L13 inspect the cutouts closely
 (49.1, 56.32, [(108.3, 111.2), (123.0, 128.0)]),
 # L14 original folder, tick photo, BG remover in bottom toolbar
 (56.32, 65.7, [(149.8, 150.6), (152.1, 153.57), (155.1, 160.5)]),
 # L15 edited copy added to the same folder
 (65.7, 69.9, [(160.5, 163.8, 2.2), (176.2, 178.0)]),
 # L16 opening a version / placing in a design (editor)
 (69.9, 74.58, [(129.0, 130.6), (131.0, 133.5)]),
 # L17 profile menu -> plan
 (74.58, 76.38, [(178.0, 179.8)]),
 # L18 Plans and pricing page
 (76.38, 82.7, [(181.4, 186.6)]),
 # L19 folder + All projects with designs
 (82.7, 89.1, [(202.0, 208.3)]),
 # L20 folder menu BG Remover option, folder with photos
 (89.1, 95.7, [(210.97, 214.4), (190.2, 192.7)]),
 # L21 use cutouts in a design (editor), download as PNG
 (95.7, END, [(133.5, 135.7), (231.2, 233.0), (234.0, 235.8), (238.35, 239.3)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) > 2)
    sp = sum(p[1] - p[0] for p in pieces if len(p) == 2) / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
