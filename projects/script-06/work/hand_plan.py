"""Hand-built plan for script-06 take 3 (403.7 s recording 1920x1080, 94.227 s voiceover, no zooms/ripples).
Pieces per narration line chosen from freezedetect n=0.003 d=0.8 moving windows (no piece reaches into a still span),
mapped by what each line says (see sync-notes.md). Groups start on lines.json starts; speed = piece total / group length."""
import json
P = 'projects/script-06/work/'
END = 94.227
L = json.load(open(P + 'lines.json'))
L = L['lines'] if isinstance(L, dict) else L
B = [0.0] + [round(l['start'], 2) for l in L[1:]] + [END]
PIECES = {
 0: [(1.47, 3.6), (17.63, 22.23)],
 1: [(300.53, 305.2)],
 2: [(54.5, 64.33)],
 3: [(84.67, 88.1)],
 4: [(92.77, 96.5)],
 5: [(165.63, 170.2)],
 6: [(174.5, 178.6), (232.97, 236.2)],
 7: [(244.43, 246.73), (251.43, 254.4)],
 8: [(254.4, 256.7)],
 9: [(256.7, 259.0)],
 10: [(259.0, 262.37), (263.17, 264.5)],
 11: [(275.2, 279.2)],
 12: [(289.5, 292.7)],
 13: [(300.53, 303.1)],
 14: [(303.5, 307.2), (309.3, 311.0)],
 15: [(338.6, 341.2)],
 16: [(356.0, 357.27), (360.0, 364.0)],
 17: [(373.8, 377.7)],
 18: [(109.57, 111.53), (113.4, 116.5)],
 19: [(384.0, 387.5)],
 20: [(293.13, 294.13), (295.33, 298.8)],
}
segs, prev_end = [], None
for i in range(len(B) - 1):
    o0, o1 = B[i], B[i + 1]
    pcs = PIECES[i]
    sp = sum(b - a for a, b in pcs) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pcs):
        end = o1 if k == len(pcs) - 1 else round(t + (b - a) / sp, 3)
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pcs}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
