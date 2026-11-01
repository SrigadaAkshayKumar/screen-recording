"""Hand-built plan for script-08 (Canva internal-links take, 210.7 s, 1920x1080, baked recorder zoom): no zooms/ripples.
One group per narration line, starting on its lines.json start; pieces from freezedetect moving windows (n=0.002,d=0.8).
(a,b) scaled; (a,b,dur) fixed output duration."""
import json
P = 'projects/script-08/work/'
END = 100.032
G = [
 (0, 8.34, [(6.0, 7.9, 2.4), (14.03, 16.77), (17.57, 20.8)]),   # L1 intro (static home, loading, design)
 (8.34, 10.42, [(20.8, 22.9)]),                                 # L2 destination (design view)
 (10.42, 13.96, [(22.9, 26.4)]),                                # L3 anchor link (same page)
 (13.96, 16.5, [(26.4, 28.4)]),                                 # L4 page link
 (16.5, 24.44, [(28.4, 33.13), (33.13, 34.77, 1.9)]),           # L5 help docs (design browsing)
 (24.44, 27.16, [(34.77, 36.37), (38.1, 39.2)]),                # L6 select contact button
 (27.16, 32.42, [(39.2, 46.2)]),                                # L7 toolbar more > Link
 (32.42, 36.66, [(47.5, 49.5), (53.5, 56.0)]),                  # L8 pages list, Done
 (36.66, 39.38, [(101.73, 104.03)]),                            # L9 Preview
 (39.38, 44.02, [(112.73, 117.67)]),                            # L10 click contact in preview -> page opens
 (44.02, 51.24, [(117.67, 123.5)]),                              # L11 contact details on page
 (51.24, 57.66, [(104.4, 110.23)]),                             # L12 show navigation toggle
 (57.66, 62.52, [(123.5, 128.47)]),            # L13 published/older site test
 (62.52, 69.94, [(135.63, 142.0)]),                              # L14 older designs (re-select contact, link menu)
 (69.94, 72.52, [(158.7, 161.2)]),                              # L15 part tutorials skip
 (72.52, 78.32, [(142.0, 148.4)]),                              # L16 typing in link box
 (78.32, 81.48, [(163.47, 166.4)]),                             # L17 target identifier
 (81.48, 92.92, [(166.4, 176.4), (177.4, 178.6)]),              # L18 page navigation / mobile preview
 (92.92, 97.26, [(188.9, 190.53), (192.77, 195.5)]),            # L19 publish
 (97.26, END, [(201.07, 203.9)]),                               # L20 landing on published site
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    fixed = sum(p[2] for p in pieces if len(p) == 3)
    src = sum(p[1] - p[0] for p in pieces if len(p) == 2)
    sp = src / (o1 - o0 - fixed)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[0], p[1]
        d = p[2] if len(p) == 3 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + d
        s = {"src_start": a, "src_end": b, "out_start": t, "out_end": end, "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
    print(f"{o0:6.2f}-{o1:6.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
