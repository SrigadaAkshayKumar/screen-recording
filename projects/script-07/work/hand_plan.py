"""Hand-budgeted plan for script-07 (317 s recording, 86.8 s voiceover, no click log; see sync-notes.md).
Pieces are built from the moving windows of the source (freezedetect n=0.003 d=0.8)."""
import json
D = 86.796
pieces = [  # (out_end, src_start, src_end)
 (4.9, 9.7, 13.4), (5.7, 13.4, 14.1), (9.9, 22.2, 26.1), (10.7, 26.1, 26.7), (15.4, 308.4, 312.0),   # L1-L3
 (17.1, 34.9, 37.3), (19.94, 57.8, 60.6),                                      # L4-L5
 (23.24, 63.3, 65.8), (27.92, 230.3, 234.0),                                   # L6
 (30.8, 82.4, 85.3),                                                           # L7
 (34.1, 88.3, 91.6), (37.72, 98.4, 102.0),                                     # L8
 (40.18, 111.7, 114.2), (44.14, 123.6, 127.9),                                 # L9-L10
 (47.4, 132.4, 135.6), (53.18, 135.6, 141.8), (55.3, 145.2, 147.3),            # L11-L13
 (57.8, 128.7, 130.6), (63.06, 184.0, 189.3), (67.66, 189.3, 194.0),           # L14-L16
 (71.78, 234.0, 238.9), (76.56, 254.6, 259.4), (79.36, 279.2, 282.0),          # L17-L19
 (82.5, 294.3, 297.4), (84.66, 304.1, 306.3), (D, 306.3, 308.4)]               # L20-L21
segs, t = [], 0.0
for i, (oe, a, b) in enumerate(pieces):
    s = dict(src_start=a, src_end=b, out_start=t, out_end=oe, mode="speed")
    if i: s["xfade"] = True
    segs.append(s); t = oe
plan = dict(output=dict(duration=D, fps=30, width=1920, height=1080), segments=segs, zooms=[], ripples=[],
            intro=None, outro=None, sync=[], style=dict(ripple_color="#2F80ED", ripple_alpha=0.6, cursor_halo=False))
json.dump(plan, open('projects/script-07/work/plan.json', 'w'), indent=1)
