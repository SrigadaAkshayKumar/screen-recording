"""Hand-budgeted plan for script-06 (396 s recording with baked-in recorder zoom, no click log, 87.446 s voiceover).
Pieces are (out_dur, src_start, src_end), chosen from freezedetect moving windows of the source (see freeze_src.txt)."""
import json
D = 87.446
pieces = [
 # L1 intro
 (2.6, 2.63, 5.0), (3.5, 8.8, 12.13),
 # L2 open design, L3 names
 (3.9, 14.57, 17.9), (1.75, 18.87, 20.23), (2.0, 185.6, 188.1),
 # L4 publish/settings, L5 nav menu on
 (2.8, 36.27, 39.53), (2.2, 44.5, 46.77),
 # L6 nav bar added
 (1.9, 58.9, 60.4), (1.35, 63.07, 64.13), (1.6, 67.4, 69.53),
 # L7 toolbar, L8 spacing
 (6.6, 71.27, 77.87), (3.6, 78.77, 82.0), (0.7, 86.6, 87.5),
 # L9 Edit/Items, L10 hide
 (3.2, 103.7, 106.67), (2.0, 130.03, 133.0), (0.8, 136.5, 137.7),
 # L11 add link
 (2.2, 199.77, 202.07), (2.3, 208.47, 211.57), (0.8, 213.0, 214.07),
 # L12 logo
 (1.5, 155.17, 157.13), (0.8, 158.87, 159.87), (0.9, 162.63, 163.73), (1.6, 172.4, 174.77), (1.1, 176.47, 178.0),
 # L13 page label
 (1.7, 274.33, 276.57), (1.8, 279.2, 281.6), (3.2, 282.7, 287.63),
 # L14 short label
 (1.1, 291.07, 292.33), (0.9, 295.03, 296.13), (1.6, 297.07, 299.0),
 # L15 skip
 (1.0, 307.47, 308.5), (1.9, 311.83, 313.87),
 # L16 row of words
 (2.1, 317.2, 319.93), (4.1, 327.43, 333.27),
 # L17 controls/preview
 (2.1, 336.3, 338.93), (2.3, 342.53, 345.33),
 # L18 mobile preview
 (4.0, 361.5, 367.5),
 # L19 publish + live
 (2.95, 375.03, 378.57), (2.8, 384.7, 387.6)]
tot = sum(p[0] for p in pieces)
segs, t = [], 0.0
for i, (d, a, b) in enumerate(pieces):
    d = d * D / tot
    oe = D if i == len(pieces) - 1 else round(t + d, 3)
    s = dict(src_start=a, src_end=b, out_start=round(t, 3), out_end=oe, mode="speed")
    if i: s["xfade"] = True
    segs.append(s); t = oe
plan = dict(output=dict(duration=D, fps=30, width=1920, height=1080), segments=segs, zooms=[], ripples=[],
            intro=None, outro=None, sync=[], style=dict(ripple_color="#2F80ED", ripple_alpha=0.6, cursor_halo=False))
json.dump(plan, open('projects/script-06/work/plan.json', 'w'), indent=1)
print("total pieces", tot)
