"""Hand-built plan for script-04 (new 161 s take, 86.61 s voiceover, 1920x1080). One group per narration
line (starting on its lines.json start), pieces from non-still footage (scenes.json stills avoided or
fast-forwarded <=1.6x), 0.8-1.3x. Piece = (src_a, src_b) or (src_a, src_b, out_len). No holds/zooms."""
import json
P = 'projects/script-04/work/'
END = 86.61
G = [
 (0, 5.98, [(144.0, 150.0)]),                                   # 1 intro: finished MP4 playing (borrowed)
 (5.98, 8.88, [(14.0, 17.0)]),                                  # 2 click Preview, spinner
 (8.88, 15.34, [(17.0, 23.5)]),                                 # 3 preview playing
 (15.34, 19.34, [(35.5, 40.0)]),                                # 4 Share -> panel
 (19.34, 22.9, [(43.5, 47.5)]),                                 # 5 File type menu
 (22.9, 26.78, [(47.5, 51.5)]),                                 # 6 (no pages menu in take) MP4 selected
 (26.78, 31.74, [(52.97, 57.4), (59.6, 60.6)]),                 # 7 borrowed: panel settings
 (31.74, 39.06, [(60.9, 64.8, 2.4), (64.8, 69.45, 4.92)]),      # 8 borrowed: panel
 (39.06, 42.62, [(54.0, 57.4)]),                                # 9 quality
 (42.62, 49.38, [(55.0, 57.4), (59.6, 60.9), (64.8, 69.4)]),    # 10 notice in panel
 (49.38, 52.48, [(69.0, 72.2)]),                                # 11 click Download
 (52.48, 55.24, [(72.2, 75.0)]),                                # 12 downloading toast
 (55.24, 57.42, [(75.0, 77.2)]),                                # 13
 (57.42, 59.98, [(77.2, 80.0)]),                                # 14
 (59.98, 63.74, [(116.0, 119.8)]),                              # 15 share link panel
 (63.74, 70.62, [(119.8, 127.0)]),                              # 16 copy link
 (70.62, 75.88, [(138.9, 144.0)]),                              # 17 explorer -> VLC
 (75.88, 82.2, [(111.0, 117.0)]),                               # 18 share button (borrowed)
 (82.2, END, [(152.0, 156.5)]),                                 # 19 playable result
]
segs, prev_end = [], None
for o0, o1, pieces in G:
    tot = sum(p[2] if len(p) > 2 else 0 for p in pieces)
    free = [p for p in pieces if len(p) == 2]
    sp = sum(b - a for a, b in free) / ((o1 - o0) - tot)
    t = o0
    for k, p in enumerate(pieces):
        a, b = p[:2]
        ln = p[2] if len(p) > 2 else (b - a) / sp
        end = o1 if k == len(pieces) - 1 else t + ln
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
