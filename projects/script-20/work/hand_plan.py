"""Hand-built plan for script-20 (new 46.4 s take, 101.285 s voiceover, baked recorder zoom: no zooms/ripples).
Recording is shorter than the voiceover: moving windows (freezedetect n=0.003 d=0.8, extended <=1 s into stills) are
reused cross-faded, 0.75-1.0x. Groups 1-7 are mapped by topic, 8-21 stream through the windows cyclically."""
import json
P = 'projects/script-20/work/'
END = 101.285
L = json.load(open(P + 'lines.json'))
L = L['lines'] if isinstance(L, dict) else L
starts = [l['start'] for l in L]
B = [0.0] + [round(s - 0.3, 2) for s in starts[1:]] + [END]   # group boundaries (just before each line)
B = [0.0] + [round(s, 2) for s in starts[1:]] + [END]
FIXED = {
 0: [(2.0, 5.8), (7.7, 10.3), (12.87, 14.0)],
 1: [(14.0, 17.9)],
 2: [(18.37, 20.77), (24.67, 27.67)],
 3: [(28.47, 31.9), (31.9, 32.9)],
 4: [(35.93, 39.5)],
 5: [(39.5, 41.9)],
 6: [(41.9, 43.53), (45.43, 46.4), (24.67, 27.1)],
 21: [(38.0, 40.6)],
 22: [(41.4, 43.53), (45.43, 46.4)],
}
S = [(2.0, 5.8), (7.2, 10.5), (12.4, 17.9), (18.0, 21.3), (24.2, 28.0), (28.0, 32.4), (35.4, 43.9), (45.0, 46.4)]
TARGET = 0.9
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
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 46.433}, "sync": {"source": "frames"},
           "actions": [{"id": "A1", "t_click": 4.0, "x": 400, "y": 300, "kind": "click", "target": "search box",
                        "result": "search suggestions", "t_result_visible": 5.0, "confidence": "low"}],
           "junk": []}, open(P + 'actions.json', 'w'), indent=1)
