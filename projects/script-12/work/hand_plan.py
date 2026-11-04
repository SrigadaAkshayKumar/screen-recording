"""script-12 hand plan (favicon script on a 136 s Canva sticker take, 3420x1922, baked recorder zoom).
Pieces: (out_start, out_end, src_a, src_b, xfade, note). Built from 1 s sheets (work/frames/a*,b*)."""
import json
P = 'projects/script-12/work/'
D = 91.95
PIECES = [
 # L1 intro: published result, then Canva home
 (0.0, 3.4, 128.3, 130.9, False, 'L1 result page with the sticker loading'),
 (3.4, 5.6, 12.4, 14.3, True, 'L1 Canva home'),
 (5.6, 8.1, 14.3, 16.6, False, 'L2 Create a design dialog'),
 (8.1, 13.16, 16.6, 22.2, False, 'L3 Custom size, 512 typed'),
 (13.16, 14.36, 22.2, 23.4, False, 'L4 Create new design click'),
 (14.36, 15.06, 27.2, 27.9, True, 'L4 blank square canvas'),
 (15.06, 30.96, 31.4, 44.0, True, 'L5-L8 elements search, sticker inserted, resized'),
 (30.96, 33.8, 44.0, 46.8, False, 'L9 text panel, subheading added'),
 (33.8, 37.7, 48.2, 51.5, True, 'L9 text typed'),
 (37.7, 40.04, 71.0, 73.2, True, 'L10 zoom out to small'),
 (40.04, 45.8, 59.8, 66.0, True, 'L11 zoomed inspection'),
 (45.8, 46.8, 76.4, 77.4, True, 'L12 Share click'),
 (46.8, 47.7, 79.7, 80.6, True, 'L12 Download click, panel'),
 (47.7, 49.4, 82.9, 84.7, True, 'L12 file type list, PNG'),
 (49.4, 53.13, 88.4, 91.2, True, 'L13 Transparent toggle'),
 (53.13, 55.46, 98.2, 100.5, True, 'L13 PNG preview on dark = transparent'),
 (55.46, 58.14, 81.0, 83.0, True, 'L14 panel, toggle off'),
 (58.14, 60.24, 92.3, 94.4, True, 'L15 Download click, toast'),
 (60.24, 62.24, 94.4, 98.2, False, 'L15 download toast (ff)'),
 (62.24, 64.02, 100.5, 102.3, True, 'L15 preview of the file'),
 (64.02, 68.24, 105.4, 109.4, True, 'L16 Share > More ways to publish'),
 (68.24, 73.98, 112.0, 117.2, True, 'L17 Website panel, Publish'),
 (73.98, 76.9, 120.7, 122.9, True, 'L18 website published'),
 (76.9, 80.9, 85.0, 88.3, True, 'L18 file type list / size'),
 (80.9, 83.02, 102.3, 104.2, True, 'L18 preview closing'),
 (83.02, 84.44, 104.2, 105.4, False, 'L19 back to Canva'),
 (84.44, 86.1, 123.0, 124.7, True, 'L20 Website panel, browser opens'),
 (86.1, 88.52, 127.5, 129.9, True, 'L20 published page loads'),
 (88.52, D, 129.9, 133.35, False, 'L21 page with sticker'),
]
segs = []
for o0, o1, a, b, xf, note in PIECES:
    s = {"src_start": a, "src_end": b, "out_start": o0, "out_end": o1, "mode": "speed"}
    if xf: s["xfade"] = True
    segs.append(s)
    print(f"out {o0:6.2f}-{o1:6.2f} src {a:6.1f}-{b:6.1f} {(b-a)/(o1-o0):.2f}x  {note}")
for x, y in zip(PIECES, PIECES[1:]): assert abs(x[1]-y[0]) < 1e-6, (x, y)
plan = {"output": {"duration": D, "fps": 30, "width": 3420, "height": 1922}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
