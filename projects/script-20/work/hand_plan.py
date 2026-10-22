"""Hand-built plan for script-20: 256 s recording (baked-in recorder zoom, no click log) for an 84 s voiceover.
Each group fills one narration interval with source pieces; no zooms/ripples."""
import json, sys
sys.path.insert(0, 'tools')
import check
P = 'projects/script-20/work/'
lines = json.load(open(P + 'lines.json'))
END = 83.731
G = [
 (0, 6.54, [(4.5, 10.7)]),
 (6.54, 8.74, [(13.6, 16.2)]),
 (8.74, 13.22, [(16.2, 21.0)]),
 (13.22, 17.54, [(21.0, 25.8)]),
 (17.54, 19.96, [(29.0, 32.2)]),
 (19.96, 26.54, [(32.2, 38.6)]),
 (26.54, 30.22, [(38.6, 41.8)]),
 (30.22, 36.86, [(74.85, 81.4)]),
 (36.86, 40.26, [(81.4, 84.4)]),
 (40.26, 44.34, [(88.3, 92.4)]),
 (44.34, 49.06, [(92.4, 97.0)]),
 (49.06, 57.94, [(153.3, 160.1)]),
 (57.94, 64.74, [(167.4, 173.3)]),
 (64.74, 67.74, [(142.8, 145.8)]),
 (67.74, 72.98, [(145.8, 150.4)]),
 (72.98, 77.5, [(230.3, 234.9)]),
 (77.5, END, [(246.5, 252.8)]),
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
allw = [(w['i'], w['word'], w['start']) for l in lines for w in l['words']]
for a in json.load(open(P + 'actions.json'))['actions']:
    o = check.src_to_out(segs, a['t_click'])
    if o is None: continue
    i, w, t = min(allw, key=lambda x: abs(x[2] - o))
    plan['sync'].append({"action": a['id'], "line": next(l['id'] for l in lines if l['word_range'][0] <= i <= l['word_range'][1]), "word": w.strip('.,'), "word_index": i, "word_t": t, "out_t": round(o, 3)})
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
