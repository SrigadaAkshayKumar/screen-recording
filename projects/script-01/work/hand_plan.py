"""Hand-built plan for script-01 (234.7 s recording 1920x1080, 93.62 s voiceover; baked-in recorder zoom: no ripples; two canvas zooms on the route drawing).
One group per narration line: pieces share the group's speed; cross-fade at every source jump.
Pieces come from the moving windows of freezedetect n=0.003 d=0.8 on the source (see sync-notes.md for the per-line map)."""
import json
P = 'projects/script-01/work/'
END = 93.623
B = [0, 8.0, 11.9, 17.5, 22.0, 27.9, 31.7, 35.9, 40.0, 46.7, 51.3, 61.1, 66.1, 72.4, 75.0, 79.1, 87.2, END]
S = [
 [(127.9, 135.1)],                                  # L1 intro: animate path settings, done, text added
 [(9.6, 14.73)],                                    # L2 canva home, create landscape video
 [(25.5, 29.07), (30.0, 31.77)],                    # L3 open elements
 [(32.83, 34.77), (35.9, 38.5)],                    # L4 pick matching background / objects
 [(38.5, 44.77)],                                   # L5 arrange background
 [(110.9, 114.7)],                                  # L6 select character, animate
 [(114.7, 118.5)],                                  # L7 create an animation, drag
 [(118.5, 122.4)],                                  # L8 drag toward the house
 [(122.4, 124.0), (126.8, 131.0)],                  # L9 release, settings, done
 [(116.5, 121.0)],                                  # L10 route advice (replay of drawing the route)
 [(148.47, 149.8), (152.07, 153.63), (154.67, 158.0), (172.9, 176.1)],  # L11 text box, entrance, timeline bar
 [(196.77, 198.0), (199.7, 201.1), (205.4, 207.8)], # L12 plus button, add scene
 [(177.3, 180.0), (180.9, 183.2), (187.67, 189.93)],# L13 reuse background/character
 [(98.03, 100.6)],                                  # L14 transition line
 [(100.6, 102.9), (104.2, 106.0)],                  # L15 character does not animate
 [(106.43, 110.5), (127.9, 131.9)],                 # L16 animated graphic + custom path
 [(216.1, 218.0), (220.0, 222.5), (223.5, 225.9)],  # L17 share, download, mp4
]
segs, prev = [], None
for k, pieces in enumerate(S):
    o0, o1 = B[k], B[k + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for j, (a, b) in enumerate(pieces):
        e = o1 if j == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(e, 3), "mode": "speed"}
        if prev is not None and abs(a - prev) > 0.002:
            s["xfade"] = True
        segs.append(s); prev = b; t = e
    print(f"L{k+1:2d} {o0:7.2f}-{o1:7.2f} {sp:.2f}x {pieces}")
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [{"out_t": 32.6, "x": 1220, "y": 440, "scale": 2.0, "in": 0.6, "hold": 6.5, "out": 0.6},
                                      {"out_t": 47.4, "x": 1220, "y": 440, "scale": 2.0, "in": 0.6, "hold": 3.2, "out": 0.6}],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
