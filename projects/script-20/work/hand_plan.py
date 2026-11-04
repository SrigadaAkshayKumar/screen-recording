"""script-20: per-line hand plan (baked recorder zoom, no click log). Each group starts on its line's
lines.json start; every group is a few pieces of footage that SHOW the step (see output/report.md)."""
import json
P = 'projects/script-20/work/'
D = 96.417
# (out_start, out_end, [(src_a, src_b, out_len or None)...])  out_len None -> share by src length
G = [
 (0.0, 6.86, [(0.0, 2.2, 2.2), (255.0, 259.2, None)]),                              # L1 home, then finished heading
 (6.86, 10.74, [(12.2, 13.8, None), (21.4, 23.2, None), (26.8, 28.6, None)]),       # L2
 (10.74, 16.36, [(28.6, 31.2, None), (42.2, 45.0, None), (45.2, 46.8, None)]),     # L3
 (16.36, 21.12, [(47.9, 51.5, None)]),                                              # L4 duplicate (click 49.2 ~ "D")
 (21.12, 24.54, [(63.0, 65.2, 1.74), (65.2, 66.4, 0.84), (70.3, 71.5, 0.84)]),      # L5
 (24.54, 30.64, [(191.2, 194.2, 2.96), (72.6, 77.2, None)]),                        # L6
 (30.64, 33.70, [(92.8, 95.6, None)]),                                              # L7
 (33.70, 42.00, [(97.8, 100.0, 2.2), (100.0, 108.9, None)]),                        # L8
 (42.00, 46.76, [(141.6, 146.4, None)]),                                            # L9
 (46.76, 53.25, [(195.5, 200.8, None)]),                                            # L10
 (53.25, 58.54, [(181.0, 185.5, None)]),                                            # L11
 (58.54, 64.90, [(147.6, 150.8, 3.2), (216.7, 219.8, None)]),                       # L12
 (64.90, 73.38, [(173.5, 180.8, None)]),                                            # L13
 (73.38, 75.56, [(202.8, 205.2, None)]),                                            # L14
 (75.56, 78.14, [(223.6, 226.6, None)]),                                            # L15
 (78.14, 83.98, [(236.5, 242.5, None)]),                                            # L16
 (83.98, 87.08, [(213.4, 216.5, None)]),                                            # L17
 (87.08, 91.14, [(249.0, 253.1, None)]),                                            # L18
 (91.14, D,     [(121.0, 125.7, 3.14), (193.9, 196.0, None)]),                      # L19
]
segs = []
for o0, o1, pieces in G:
    tot = o1 - o0
    fixed = sum(p[2] for p in pieces if p[2])
    free = [p for p in pieces if not p[2]]
    fs = sum(p[1] - p[0] for p in free)
    o = o0
    for i, (a, b, ol) in enumerate(pieces):
        d = ol if ol else (tot - fixed) * (b - a) / fs
        end = o1 if i == len(pieces) - 1 else o + d
        s = {"src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": round(end, 3), "mode": "speed"}
        if segs and abs(segs[-1]['src_end'] - a) > 0.01: s["xfade"] = True
        segs.append(s); o = end
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.1f}-{s['src_end']:6.1f} {(s['src_end']-s['src_start'])/d:.2f}x")
