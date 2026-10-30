"""Hand-built plan for script-17-new: the recording holds several takes (186 s for a 74 s voiceover), so each
narration interval gets explicit source pieces (uniform speed per group). Run from the repo root."""
import json
P = 'projects/script-17-new/work/'
lines = json.load(open(P + 'lines.json'))
widx = {}
for l in lines:
    for w in l['words']:
        widx.setdefault((l['id'], w['word'].strip('.,').lower()), w)  # first occurrence
END = 73.9
# (out_start, out_end, [(src_a, src_b)], anchor-at-end (action, line, word) or None)
G = [
 (0, 6.9, [(6.4, 13.5)], ('A1', 2, 'bar')),
 (6.9, 9.6, [(13.5, 14.6), (18.2, 19.4)], ('A2', 3, 'volume')),
 (9.6, 11.66, [(19.4, 21.0)], ('A3', 3, 'mute')),
 (11.66, 15.18, [(21.0, 22.4), (29.8, 32.2)], ('A4', 4, 'play')),
 (15.18, 26.8, [(32.2, 46.8), (48.8, 50.0)], ('A5', 7, 'audio')),
 (26.8, 29.04, [(50.0, 52.1)], ('A6', 7, 'volume')),
 (29.04, 29.96, [(52.1, 53.1)], ('A7', 7, 'want')),
 (29.96, 39.26, [(53.1, 55.9), (64.0, 68.0), (73.7, 75.6)], ('A8', 9, 'select')),
 (39.26, 41.4, [(75.6, 78.5)], ('A9', 9, 'volume')),
 (41.4, 50.36, [(78.5, 80.2), (91.0, 96.8), (120.0, 121.4)], ('A13', 11, 'browser')),
 (50.36, 52.98, [(121.4, 125.0)], ('A14', 11, 'changes')),
 (52.98, 56.12, [(125.0, 127.0), (106.9, 108.3)], ('A11', 12, 'track')),
 (56.12, 57.96, [(108.3, 110.6)], ('A12', 12, 'volume')),
 (57.96, 60.94, [(110.6, 114.4)], None),
 (60.94, 64.68, [(131.2, 135.0)], None),
 (64.68, 68.02, [(142.0, 143.9), (162.2, 164.7)], ('A17', 15, 'download')),
 (68.02, 69.92, [(164.7, 165.7), (175.9, 177.0)], ('A18', 15, 'open')),
 (69.92, END, [(177.0, 181.4)], None),
]
segs, sync, prev_end = [], [], None
for o0, o1, pieces, anc in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    if anc:
        aid, ln, w = anc
        wd = widx[(ln, w)]
        sync.append({"action": aid, "line": ln, "word": w, "word_index": wd['i'], "word_t": wd['start']})
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
