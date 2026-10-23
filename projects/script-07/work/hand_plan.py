"""Hand-budgeted plan for script-07 (369 s recording, 119 s voiceover, no click log; see sync-notes.md)."""
import json
D = 119.351
pieces = [  # (out_end, src_start, src_end)
 (6.66, 14.6, 21.4), (11.4, 22.2, 26.0), (15.46, 28.6, 31.7), (24.6, 36.0, 45.2), (33.44, 46.0, 54.9),
 (39.0, 143.7, 149.3), (42.38, 167.0, 170.4), (49.96, 66.0, 73.6), (59.78, 189.6, 199.4),
 (66.22, 209.9, 216.4), (72.3, 121.3, 127.4), (76.76, 243.9, 248.4), (82.46, 252.4, 256.7),
 (87.36, 273.2, 277.9), (91.66, 277.9, 282.5), (96.58, 288.0, 292.9), (105.48, 296.0, 304.9),
 (112.86, 305.0, 312.4), (D, 311.0, 317.5)]
segs, t = [], 0.0
for i, (oe, a, b) in enumerate(pieces):
    s = dict(src_start=a, src_end=b, out_start=t, out_end=oe, mode="speed")
    if i: s["xfade"] = True
    segs.append(s); t = oe
plan = dict(output=dict(duration=D, fps=30, width=1920, height=1080), segments=segs, zooms=[], ripples=[],
            intro=None, outro=None, sync=[], style=dict(ripple_color="#2F80ED", ripple_alpha=0.6, cursor_halo=False))
json.dump(plan, open('projects/script-07/work/plan.json', 'w'), indent=1)
