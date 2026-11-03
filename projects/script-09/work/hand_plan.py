"""script-09 (244 s Canva bulk background remover take, 101.611 s voiceover, 1920x1080).
One group per narration line (or pair), starting on the line's start (lines.json). Pieces come from
freezedetect (n=0.003, d=0.8) moving windows; static source spans only as fixed-length pieces <= 2x."""
import json
P = 'projects/script-09/work/'
D = 101.611
# group start times (out) then end
S = [0.0, 5.48, 11.38, 14.54, 19.78, 27.74, 32.64, 35.02, 41.34, 45.78, 49.1, 56.32, 65.7, 69.9, 74.58, 76.38, 82.7, 89.1, 95.7, D]
# piece = (src_a, src_b) or (src_a, src_b, fixed_out_seconds)
G = [
 [(0.16, 5.13, 2.5), (5.13, 7.4)],                 # L1-2 static home (2x) then home scroll
 [(7.4, 11.88)],                                   # L3 intro, home page
 [(11.88, 14.3)],                                  # L4 open projects
 [(14.3, 17.7, 2.0), (17.7, 20.4)],                # L5 create folder, open it
 [(20.4, 29.4)],                                   # L6-7 add new -> upload files dialog
 [(48.67, 51.3), (54.03, 56.7)],    # L8 folder listing, hover, 3-dot menu
 [(62.6, 66.17, 2.38)],                            # L9 select remove background
 [(66.17, 68.83), (70.2, 73.43)],                  # L10 processing, new folder
 [(80.0, 84.23, 2.4), (84.23, 86.03)],             # L11 edited folder alongside original
 [(88.67, 91.4)],                                  # L12 open edited folder
 [(105.1, 107.47), (110.0, 111.17), (118.8, 120.57), (121.87, 124.5)],  # L13 check cutouts
 [(147.0, 153.47), (155.1, 157.6)],                # L14 original folder, tick, BG remover
 [(157.6, 160.07), (161.5, 163.67, 1.73)],         # L15 copies added to same folder
 [(124.5, 127.13), (128.73, 131.5)],               # L16 which version / placing into design
 [(176.33, 178.2)],                                # L17 account menu (limit)
 [(178.2, 178.9), (182.23, 187.6)],                # L18 plans and pricing
 [(189.8, 190.77), (202.23, 206.27), (206.27, 210.97, 2.4)],  # L19 home folders
 [(211.0, 214.77), (196.0, 200.4, 2.4)],           # L20
 [(225.0, 229.03), (229.87, 233.0)],               # L21 download
]
segs = []
prev_end = None
for i, pieces in enumerate(G):
    o = S[i]; end = S[i + 1]
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    tot = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    avail = end - o - fixed
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) == 3 else (b - a) / tot * avail
        o1 = end if k == len(pieces) - 1 else o + d
        seg = {"src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": round(o1, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 1e-6:
            seg["xfade"] = True
        segs.append(seg); prev_end = b; o = o1
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.2f}-{s['src_end']:6.2f} {(s['src_end']-s['src_start'])/d:.2f}x")
