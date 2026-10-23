"""Hand-built plan for script-05: 305 s recording (baked-in recorder zoom, no click log) for a 96.4 s voiceover.
Each group fills one narration interval with source pieces; no zooms/ripples (recorder zoom is baked in)."""
import json, sys
sys.path.insert(0, 'tools')
import check
P = 'projects/script-05/work/'
lines = json.load(open(P + 'lines.json'))
END = 96.409
G = [
 (0, 6.52, [(13.2, 19.7)]),
 (6.52, 10.66, [(27.3, 33.4)]),
 (10.66, 17.62, [(43.8, 52.4)]),
 (17.62, 20.28, [(60.3, 63.9)]),
 (20.28, 25.26, [(79.8, 86.5)]),
 (25.26, 37.6, [(131.8, 141.6)]),
 (37.6, 40.46, [(155.0, 159.2)]),
 (40.46, 46.16, [(118.8, 124.0)]),
 (46.16, 50.42, [(194.2, 198.6)]),
 (50.42, 53.66, [(198.8, 201.4)]),
 (53.66, 56.46, [(208.2, 210.8)]),
 (56.46, 62.44, [(210.8, 215.4)]),
 (62.44, 65.4, [(223.4, 227.4)]),
 (65.4, 68.46, [(234.2, 236.2), (238.4, 239.6)]),
 (68.46, 73.46, [(239.6, 241.8), (244.3, 245.6), (248.0, 250.8)]),
 (73.46, 75.88, [(250.8, 253.0)]),
 (75.88, 78.6, [(253.0, 255.7)]),
 (78.6, 85.32, [(258.8, 265.4)]),
 (85.32, 92.18, [(277.3, 284.2)]),
 (92.18, END, [(212.3, 216.3)]),
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
    if abs(t - o) > 0.15: continue  # hand plan: only record clicks that really land on a word
    plan['sync'].append({"action": a['id'], "line": next(l['id'] for l in lines if l['word_range'][0] <= i <= l['word_range'][1]), "word": w.strip('.,'), "word_index": i, "word_t": t, "out_t": round(o, 3)})
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
