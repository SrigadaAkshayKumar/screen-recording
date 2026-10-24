"""Hand-built plan for script-05: 260 s recording (baked-in recorder zoom, no click log) for a 90.1 s voiceover.
Each group fills one narration interval with source pieces; no zooms/ripples (recorder zoom is baked in)."""
import json, sys
sys.path.insert(0, 'tools')
import check
P = 'projects/script-05/work/'
lines = json.load(open(P + 'lines.json'))
END = 90.14
G = [
 (0, 5.4, [(4.6, 10.0)]),
 (5.4, 9.66, [(10.2, 13.4), (18.4, 20.2), (21.2, 22.3)]),
 (9.66, 13.5, [(22.6, 26.4)]),
 (13.5, 17.3, [(41.2, 45.0)]),
 (17.3, 19.8, [(53.2, 56.8)]),
 (19.8, 24.52, [(67.0, 71.7)]),
 (24.52, 32.84, [(71.7, 73.9), (79.2, 85.5)]),
 (32.84, 36.52, [(86.0, 89.7)]),
 (36.52, 43.56, [(107.3, 113.7)]),
 (43.56, 46.26, [(118.0, 121.0)]),
 (46.26, 49.4, [(126.4, 130.0)]),
 (49.4, 51.38, [(140.0, 142.0)]),
 (51.38, 59.22, [(148.4, 156.3)]),
 (59.22, 60.8, [(160.2, 162.0)]),
 (60.8, 67.58, [(169.2, 174.4), (183.0, 184.6)]),
 (67.58, 74.46, [(186.0, 189.0), (199.0, 203.0)]),
 (74.46, 80.3, [(203.0, 208.5)]),
 (80.3, 84.38, [(219.4, 221.9), (225.5, 227.5)]),
 (84.38, 87.76, [(247.8, 251.2)]),
 (87.76, END, [(251.2, 253.6)]),
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
    if abs(t - o) > 0.15: continue
    plan['sync'].append({"action": a['id'], "line": next(l['id'] for l in lines if l['word_range'][0] <= i <= l['word_range'][1]), "word": w.strip('.,'), "word_index": i, "word_t": t, "out_t": round(o, 3)})
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
