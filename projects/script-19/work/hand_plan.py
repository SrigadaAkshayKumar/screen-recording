"""Hand-built plan for script-19 (72 s take, 101.05 s voiceover, baked recorder zoom: no zooms/ripples).
Recording is shorter than the voiceover: moving windows (freezedetect n=0.003 d=0.8) are reused cross-faded by topic.
Pieces are (src_a, src_b[, fixed_out_dur]); one group per narration line (or pair of lines)."""
import json
P = 'projects/script-19/work/'
END = json.load(open(P + 'probe.json'))['voiceover']['duration']
G = [
 (0, 8.22, [(0.0, 3.0, 2.4), (44.0, 49.0)]),
 (8.22, 15.56, [(15.13, 20.17), (20.17, 22.17, 2.0)]),
 (15.56, 20.02, [(23.43, 27.4)]),
 (20.02, 27.32, [(27.4, 28.37), (29.73, 33.1), (34.1, 34.7), (37.5, 38.87)]),
 (27.32, 29.56, [(39.83, 41.9)]),
 (29.56, 33.34, [(24.0, 27.2)]),
 (33.34, 36.42, [(37.5, 38.87), (39.83, 40.9)]),
 (36.42, 38.7, [(31.0, 33.1)]),
 (38.7, 45.6, [(41.9, 48.0)]),
 (45.6, 48.76, [(48.0, 51.0)]),
 (48.76, 51.84, [(42.0, 45.0)]),
 (51.84, 56.16, [(52.63, 54.23), (55.23, 56.53), (46.0, 47.3)]),
 (56.16, 60.08, [(26.0, 28.37), (29.73, 31.2)]),
 (60.08, 63.64, [(31.2, 33.1), (34.1, 34.7), (37.5, 38.4)]),
 (63.64, 67.82, [(62.53, 63.73), (67.2, 70.4)]),
 (67.82, 70.5, [(39.83, 42.3)]),
 (70.5, 74.14, [(43.0, 46.3)]),
 (74.14, 79.04, [(46.3, 51.0)]),
 (79.04, 83.12, [(52.63, 54.23), (55.23, 56.53), (62.53, 63.73)]),
 (83.12, 90.16, [(52.63, 54.23), (55.23, 56.53), (62.53, 63.73), (67.2, 70.4)]),
 (90.16, 94.2, [(44.0, 48.0)]),
 (94.2, 95.72, [(48.0, 49.5)]),
 (95.72, END, [(49.5, 51.3), (29.73, 32.7)]),
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
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
