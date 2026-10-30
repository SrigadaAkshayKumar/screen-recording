"""Hand-built plan for script-17 (83.267 s voiceover, 300.5 s recording, baked recorder zoom: no zooms/ripples).
Each line's footage is the step that line describes (per-line map in output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-17/work/'
DUR = 83.267
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(24.2, 30.0)],                      # finished clip playing in the editor (intro/result)
 2: [(20.4, 23.8)],                        # Create a design menu -> blank design
 3: [(31.0, 37.8)],                        # Uploads: Videos tab, video added to the page
 4: [(49.5, 53.3), (56.0, 60.0)],          # select clip, Edit toolbar, Video Speed in the side panel
 5: [(121.4, 126.5)],                      # Edit toolbar opens the same controls
 6: [(126.7, 131.0)],                      # speed slider moved
 7: [(73.0, 79.0)],                        # slider across its range (readout changes)
 8: [(98.2, 99.4)],                        # press play to preview
 9: [(99.4, 104.8)],                       # clip playing
 10: [(113.5, 117.0)],                     # select the clip in the timeline
 11: [(117.0, 120.9)],                     # Split in the toolbar (playhead/split)
 12: [(155.5, 158.3), (167.4, 170.5)],     # select middle segment, speed panel
 13: [(186.0, 187.4)],                     # timeline afterwards
 14: [(189.1, 195.0)],                     # timeline pages / durations
 15: [(203.5, 206.0)],                     # timeline view
 16: [(227.0, 230.5)],                     # clip playing with its sound
 17: [(233.4, 235.4), (237.5, 242.3)],
 18: [(244.8, 248.8)],                     # playhead to start, press play
 19: [(273.5, 279.7)],                     # Share > Download > MP4 video
}
N = len(G)
assert N == len(L), (N, len(L))
segs, prev = [], None
for n in range(1, N + 1):
    t0 = L[n - 1] if n > 1 else 0.0
    t1 = L[n] if n < N else DUR
    pcs = G[n]
    fixed = sum((p[1] - p[0]) / p[2] for p in pcs if len(p) == 3)
    free = sum(p[1] - p[0] for p in pcs if len(p) == 2)
    sp = free / (t1 - t0 - fixed) if free else 0
    t = t0
    for i, p in enumerate(pcs):
        s = p[2] if len(p) == 3 else sp
        d = (p[1] - p[0]) / s
        o1 = t1 if i == len(pcs) - 1 else round(t + d, 3)
        seg = {"src_start": p[0], "src_end": p[1], "out_start": round(t, 3), "out_end": round(o1, 3), "mode": "speed"}
        if prev is not None and abs(p[0] - prev) > 0.002:
            seg["xfade"] = True
        segs.append(seg); prev = p[1]; t = o1
        print('line', n, p[0], p[1], 'x%.2f' % ((p[1] - p[0]) / (o1 - seg['out_start'])), 'out %.2f' % (o1 - seg['out_start']))
plan = {"output": {"duration": DUR, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
