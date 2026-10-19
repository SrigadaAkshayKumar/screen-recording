"""Hand-budgeted plan for script-06 (recording has baked-in zoom and long idle spells; see sync-notes.md)."""
import json
D = 73.143
pieces = [  # (out_end, src_start, src_end)
 (4.94, 1.2, 5.0), (11.74, 17.5, 27.6), (15.46, 43.0, 46.0), (19.48, 57.0, 61.0),
 (22.86, 83.0, 86.8), (26.9, 87.0, 91.0), (30.18, 101.9, 104.9), (35.2, 112.0, 117.0),
 (39.0, 126.0, 130.5), (44.16, 166.0, 172.4), (51.5, 156.0, 162.0), (59.0, 205.0, 211.0),
 (66.04, 218.0, 227.5), (D, 238.0, 246.0)]
segs, t = [], 0.0
for i, (oe, a, b) in enumerate(pieces):
    s = dict(src_start=a, src_end=b, out_start=t, out_end=oe, mode="speed")
    if i: s["xfade"] = True
    segs.append(s); t = oe
plan = dict(output=dict(duration=D, fps=30, width=1920, height=1080), segments=segs, zooms=[], ripples=[],
            intro=None, outro=None, sync=[], style=dict(ripple_color="#2F80ED", ripple_alpha=0.6, cursor_halo=False))
json.dump(plan, open('projects/script-06/work/plan.json', 'w'), indent=1)
