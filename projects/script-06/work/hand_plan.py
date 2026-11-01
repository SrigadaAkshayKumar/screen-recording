"""Hand-built plan for script-06 (226 s PNG-transparent take, 94.459 s voiceover, 1920x1080). One group per
narration line (some merged), pieces chosen from contact sheets. No holds/zooms. Footage borrowed where the take
lacks a narrated step (see output/report.md)."""
import json
P = 'projects/script-06/work/'
END = 94.459
S = [0, 5.98, 9.3, 15.02, 18.52, 23.5, 24.88, 32.0, 37.1, 39.16, 43.72, 47.54, 49.36, 56.76, 62.58, 70.38, 73.32, 80.44, 85.84, 89.66, END]
W = [
 [(0.0, 6.0)],                    # 1 intro
 [(9.6, 12.9)],                   # 2 open design
 [(19.2, 24.9)],                  # 3 delete rectangle
 [(27.0, 30.5)],                  # 4 page background white
 [(40.8, 45.8)],                  # 5 share/download/PNG
 [(47.6, 49.0)],                  # 6 transparent toggle
 [(45.0, 48.2), (48.6, 52.0)],    # 7 paid plan note
 [(52.0, 57.0)],                  # 8 click download
 [(57.6, 59.7)],                  # 9 test file
 [(60.0, 64.6)],                  # 10 new design, dark rectangle
 [(72.0, 75.8)],                  # 11 background shows
 [(76.8, 78.6)],                  # 12 tutorials skip
 [(86.4, 93.8)],                  # 13 logo on dark
 [(108.6, 111.3), (114.5, 117.6)],                # 14 JPG white rectangle
 [(161.2, 169.0)],                # 15 bg removal
 [(115.2, 118.1)],                # 16 decorative objects
 [(146.4, 150.4), (151.2, 154.3)],# 17 large white shape
 [(218.4, 223.8)],                # 18 viewer on white
 [(204.0, 207.8)],                # 19 dark test
 [(194.4, 199.2)],                # 20 ready
]
segs, prev_end = [], None
for i, pieces in enumerate(W):
    o0, o1 = S[i], S[i + 1]
    sp = sum(b - a for a, b in pieces) / (o1 - o0)
    print(i + 1, round(sp, 2))
    t = o0
    for k, (a, b) in enumerate(pieces):
        end = o1 if k == len(pieces) - 1 else t + (b - a) / sp
        s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
        if prev_end is not None and abs(a - prev_end) > 0.002:
            s["xfade"] = True
        segs.append(s); prev_end = b; t = end
pr = json.load(open(P + 'probe.json'))['recording']
plan = {"output": {"duration": END, "fps": 30.0, "width": pr['width'], "height": pr['height']},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
