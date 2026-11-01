"""Hand-built plan for script-04 (187 s white-edges take, 94.087 s voiceover, 1920x1080). One group per narration
line (starting on its lines.json start); pieces come from non-static footage (freezedetect n=0.002 d=0.8 gaps).
Piece = (src_a, src_b). No holds/zooms."""
import json
P = 'projects/script-04/work/'
END = 94.087
S = [0, 8.68, 12.32, 17.52, 23.1, 26.6, 31.16, 35.16, 42.92, 48.48, 52.02, 55.44, 63.06, 65.54, 69.06, 75.62, 80.9, 87.28, END]
W = [
 [(10.8, 16.4), (21.0, 24.0)],      # 1 intro: open home -> design
 [(24.0, 26.0), (26.9, 28.6)],      # 2 open design, zoom
 [(30.0, 32.4), (33.2, 36.0)],      # 3 select background
 [(64.0, 69.6)],                    # 4 right-click menu
 [(53.0, 56.5)],                    # 5 enlarge
 [(168.4, 173.0)],                  # 6 rectangle check
 [(177.0, 181.0)],                  # 7 download panel
 [(92.8, 100.6)],                   # 8 test image downloaded
 [(181.5, 187.0)],                  # 9 print: download panel
 [(125.2, 128.7)],                  # 10 share/download
 [(130.0, 133.2)],                  # 11 PDF type
 [(134.0, 136.6), (141.8, 144.8), (145.7, 147.0)],  # 12 PDF download
 [(154.6, 157.2)],                  # 13
 [(158.5, 162.0)],                  # 14
 [(162.0, 164.6), (118.7, 122.7)],  # 15
 [(72.8, 78.0)],                    # 16
 [(36.0, 40.8), (44.9, 46.5)],      # 17
 [(173.0, 176.9), (46.5, 47.1), (51.1, 53.0)],      # 18
]
segs, prev_end = [], None
for i, pieces in enumerate(W):
    o0, o1 = S[i], S[i + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
plan = {"output": {"duration": END, "fps": 30.0, "width": 1920, "height": 1080},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
