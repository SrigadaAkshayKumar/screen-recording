"""Hand-built plan for script-19-new: the recording (256 s) is much longer than the voiceover (81 s) and
has baked-in recorder zoom, so each narration interval gets source pieces chosen by hand (no zooms/ripples)."""
import json
P = 'projects/script-19-new/work/'
probe = json.load(open(P + 'probe.json'))
END = probe['voiceover']['duration']
# (out_start, out_end, [(src_a, src_b[, speed])], sync-or-None)
G = [
 (0, 6.6, [(54.6, 57.8, 1.0), (8.4, 11.15)], None),
 (6.6, 9.62, [(14.3, 16.3), (17.6, 18.6)], ('A1', 2, 'Open')),
 (9.62, 14.02, [(18.6, 20.9, .75), (23.7, 24.7)], None),
 (14.02, 19.04, [(34.3, 38.0), (40.2, 41.5)], None),
 (19.04, 22.68, [(49.4, 53.04)], None),
 (22.68, 26.8, [(60.0, 64.1)], None),
 (26.8, 31.98, [(67.4, 72.6)], None),
 (31.98, 35.52, [(109.4, 112.94)], None),
 (35.52, 42.58, [(112.9, 114.5, .75), (149.4, 154.2)], None),
 (42.58, 46.38, [(114.3, 117.2)], None),
 (46.38, 55.9, [(90.3, 96.5), (126.0, 129.4)], None),
 (55.9, 59.58, [(73.3, 76.2)], None),
 (59.58, 65.78, [(143.2, 149.4)], None),
 (65.78, 69.12, [(169.8, 173.14)], None),
 (69.12, 72.76, [(172.6, 173.4), (175.3, 176.5), (180.0, 181.2)], None),
 (72.76, 75.68, [(235.0, 237.9)], None),
 (75.68, END, [(239.5, 245.0)], None),
]
segs, prev_end = [], None
for o0, o1, pieces, anc in G:
    explicit = [p for p in pieces if len(p) == 3]
    outs = [(p[1] - p[0]) / p[2] for p in explicit]
    rest = o1 - o0 - sum(outs)
    fill = [p for p in pieces if len(p) == 2]
    sp_fill = sum(p[1] - p[0] for p in fill) / rest if fill else 1
    durs = [(p[1] - p[0]) / (p[2] if len(p) == 3 else sp_fill) for p in pieces]
    t = o0
    for k, (p, d) in enumerate(zip(pieces, durs)):
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": p[0], "src_end": p[1], "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(p[0] - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = p[1]; t = end
    print(o0, o1, ['%.2fx' % ((p[1]-p[0])/(d)) for p, d in zip(pieces, durs)])
# hold-free: the last interval may need a final speed fix, so report it
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
