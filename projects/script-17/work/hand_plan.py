"""Hand-built plan for script-17 re-edit (92.648 s voiceover, 378.3 s recording, baked recorder zoom: no zooms/ripples).
Each line's footage is the step the line describes (see work/actions.json, output/report.md).
Groups start exactly on each narration line's start (lines.json). Pieces: (src_a, src_b[, fixed_speed])."""
import json
P = 'projects/script-17/work/'
DUR = 92.648
raw = json.load(open(P + 'lines.json'))
L = [r['start'] for r in (raw['lines'] if isinstance(raw, dict) else raw)]
G = {
 1: [(316.0, 322.8)],                      # slideshow playing in the editor (finished result)
 2: [(13.9, 17.0)],                        # Video tile -> Create a design -> Landscape video -> blank design
 3: [(31.5, 34.8), (46.3, 48.2)],          # type "wedding slideshow" in template search; click template
 4: [(73.6, 75.6)],                        # Uploads tab opens
 5: [(68.2, 73.4)],                        # timeline pages in order (years/labels)
 6: [(79.6, 81.8)],                        # drag uploaded photo onto the page frame
 7: [(81.6, 84.6)],                        # photo selected in the frame, crop toolbar
 8: [(84.6, 86.2), (88.3, 92.7)],                        # swap in the whole portrait from Uploads
 9: [(118.6, 121.6)],                      # type the couple's names on the title page
 10: [(141.0, 144.5)],                     # date text selected, font toolbar (Lora)
 11: [(165.4, 168.8)],                     # hover the timeline pages (durations)
 12: [(169.6, 174.8)],                     # open a page's Timing slider and change seconds
 13: [(203.4, 206.4)],                     # timeline between pages (no transition footage)
 14: [(209.9, 211.9), (216.0, 218.0), (228.4, 229.8)],  # add audio track, trim, volume slider
 15: [(238.9, 240.5)],                     # cursor to the end of the timeline
 16: [(240.5, 244.6)],                     # add-page (+) menu, page time readouts
 17: [(244.6, 249.6)],                     # total length readouts on the timeline
 18: [(264.5, 266.2)],                     # press play
 19: [(266.4, 270.1)],                     # slideshow playing: names, photos
 20: [(279.3, 281.5)],                     # Share > Download > MP4 video
 21: [(358.9, 363.0)],                     # download finished, open the exported mp4
 22: [(366.2, 369.0)],                     # exported video playing
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
