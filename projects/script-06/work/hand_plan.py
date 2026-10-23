"""Hand-budgeted plan for script-06 (327 s recording with baked-in recorder zoom, no click log, 100.171 s voiceover).
Pieces are (out_end, src_start, src_end), one or two per narration line, chosen where the UI changes."""
import json
D = 100.171
pieces = [
 (6.4, 4.0, 9.0), (9.7, 10.5, 13.8), (13.0, 16.0, 19.3), (17.0, 22.5, 27.5),
 (19.8, 45.5, 48.3), (22.4, 62.5, 65.1), (25.4, 84.5, 88.5), (28.4, 111.0, 115.0),
 (31.0, 128.5, 131.5), (34.2, 204.0, 207.5), (37.8, 132.0, 135.6), (41.3, 147.5, 151.0),
 (45.1, 162.5, 166.3), (49.5, 167.0, 171.4), (51.6, 220.5, 222.6), (55.2, 223.5, 227.0),
 (62.9, 227.5, 236.0), (67.2, 200.2, 204.5), (70.9, 241.4, 245.1), (74.7, 255.0, 258.8),
 (78.7, 183.0, 187.0), (81.9, 283.5, 286.7), (85.5, 289.0, 292.6), (91.2, 293.0, 299.0),
 (96.8, 306.5, 312.1), (D, 313.0, 316.4)]
segs, t = [], 0.0
for i, (oe, a, b) in enumerate(pieces):
    s = dict(src_start=a, src_end=b, out_start=t, out_end=oe, mode="speed")
    if i: s["xfade"] = True
    segs.append(s); t = oe
plan = dict(output=dict(duration=D, fps=30, width=1920, height=1080), segments=segs, zooms=[], ripples=[],
            intro=None, outro=None, sync=[], style=dict(ripple_color="#2F80ED", ripple_alpha=0.6, cursor_halo=False))
json.dump(plan, open('projects/script-06/work/plan.json', 'w'), indent=1)
