"""script-20 (239.5 s take, 1920x1080, baked recorder zoom, no click log): per-line hand plan.
Each group starts at its line's lines.json start; pieces are footage that SHOWS the step
(see output/report.md).  (src_a, src_b, out_len|None) - last piece of a group fills the rest."""
import json
P = 'projects/script-20/work/'
D = 96.417
G = [
 (0.0, 6.86,   [(0.0, 2.2, 2.2), (224.0, 227.0, 3.0), (109.2, 110.9, None)]),                      # L1 home -> finished heading
 (6.86, 10.74, [(9.2, 11.1, 1.9), (19.0, 21.0, None)]),                        # L2 open design, add text, type
 (10.74, 16.36,[(24.0, 29.6, None)]),                                          # L3 font size
 (16.36, 21.14,[(43.0, 46.0, 3.2), (71.5, 73.7, None)]),                       # L4 duplicate
 (21.14, 24.54,[(47.4, 51.2, None)]),                                          # L5 effects -> outline
 (24.54, 30.64,[(65.6, 68.4, 2.7), (57.0, 61.4, None)]),                       # L6 colour, thickness
 (30.64, 33.70,[(131.9, 133.9, 1.9), (136.4, 137.5, None)]),                   # L7 Position, Layers
 (33.70, 42.02,[(80.3, 83.6, 2.9), (83.6, 86.6, 2.9), (87.0, 90.4, None)]),    # L8 shadow
 (42.02, 46.76,[(134.0, 137.0, 3.0), (137.4, 139.2, None)]),                   # L9 behind / layers
 (46.76, 53.26,[(130.8, 133.4, 2.4), (133.4, 136.5, None)]),                   # L10 position, align
 (53.26, 58.54,[(115.0, 119.0, 3.0), (122.0, 124.4, None)]),                   # L11 overlap
 (58.54, 64.96,[(72.0, 74.6, 2.8), (133.8, 137.0, None)]),                     # L12 align precisely
 (64.96, 73.38,[(59.0, 61.6, 2.9), (86.0, 89.0, 3.0), (100.6, 103.2, None)]),  # L13 separate effects
 (73.38, 75.58,[(147.1, 148.9, None)]),                                        # L14 group
 (75.58, 78.18,[(180.4, 183.4, None)]),                                        # L15 move/resize
 (78.18, 83.98,[(232.6, 237.6, None)]),                                        # L16 edit both
 (83.98, 87.08,[(74.0, 77.0, None)]),                                          # L17 stop lining up
 (87.08, 91.14,[(203.6, 205.8, 1.9), (217.6, 220.8, None)]),                   # L18 preview, download
 (91.14, D,    [(98.0, 100.7, 2.64), (104.4, 107.0, None)]),                    # L19 offset / colour
]
segs = []
for o0, o1, pieces in G:
    o = o0
    for i, (a, b, ol) in enumerate(pieces):
        end = o1 if i == len(pieces) - 1 else o + ol
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
