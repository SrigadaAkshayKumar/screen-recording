"""Hand-built plan for script-06 (136.9 s recording 3420x1922, 90.14 s voiceover, baked recorder zoom: no zooms/ripples).
Moving windows from freezedetect n=0.003 d=0.8 on the source, extended <=0.5 s into stills, streamed in source order
per narration line (groups start on lines.json starts), ~0.8-1.2x, no holds."""
import json
P = 'projects/script-06/work/'
END = 90.14
L = json.load(open(P + 'lines.json'))
L = L['lines'] if isinstance(L, dict) else L
starts = [l['start'] for l in L]
B = [0.0] + [round(s, 2) for s in starts[1:]] + [END]
FIXED = {0: [(0.0, 1.5), (8.0, 12.3)]}
M = [(11.9, 19.13), (24.27, 26.97), (28.5, 29.97), (34.17, 40.2), (41.43, 44.9), (46.53, 47.8), (48.67, 51.27),
     (57.17, 58.63), (59.5, 61.63), (62.57, 63.77), (67.07, 71.1), (72.37, 74.73), (76.97, 80.1), (83.77, 86.57),
     (87.93, 91.1), (93.07, 94.27), (96.93, 101.0), (101.87, 103.63), (110.03, 111.37), (115.63, 118.83),
     (120.07, 122.8), (124.77, 132.23)]
EXT = 0.5
S = []
for a, b in M:
    a -= EXT; b += EXT
    if S and a - S[-1][1] < 0.3:
        S[-1][1] = b
    else:
        S.append([a, b])
S[0][0] = 12.3
S = [tuple(x) for x in S]
tot = sum(b - a for a, b in S)
need = END - B[1]
TARGET = tot / need
print('available', round(tot, 1), 'need', round(need, 1), 'speed', round(TARGET, 2))
queue = [list(w) for w in S]
qi = 0
def take(n):
    global qi
    out = []
    while n > 0.45:
        w = queue[qi % len(queue)]
        a, b = w
        use = min(n, b - a)
        if (b - a) - use < 0.5:
            use = b - a
        out.append((round(a, 3), round(a + use, 3)))
        n -= use
        if use >= b - a - 1e-6:
            qi += 1
            queue[qi % len(queue)] = list(S[qi % len(S)])
        else:
            w[0] = a + use
    return out
G = []
for i in range(len(B) - 1):
    o0, o1 = B[i], B[i + 1]
    pieces = FIXED.get(i) or take(TARGET * (o1 - o0))
    G.append((o0, o1, pieces))
segs, prev_end = [], None
for o0, o1, pieces in G:
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 3420, "height": 1922, "fps": 30, "duration": 136.933}, "sync": {"source": "frames"},
           "actions": [{"id": "A1", "t_click": 14.0, "x": 1000, "y": 600, "kind": "click", "target": "Create a design",
                        "result": "design opens", "t_result_visible": 20.0, "confidence": "low"}],
           "junk": []}, open(P + 'actions.json', 'w'), indent=1)
