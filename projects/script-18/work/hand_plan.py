"""Hand-built plan for script-18 (315 s Canva AI music take, 90.892 s voiceover, 1920x1080).
Pieces (src_a, src_b, out_dur) per narration line, chosen from 1 s sheets + freezedetect.
Run from repo root: python projects/script-18/work/hand_plan.py"""
import json
P = 'projects/script-18/work/'
END = 90.892
PIECES = [
 # L1 intro: b-roll of second take generating -> adding track to the timeline
 (284.3, 289.8, 5.5),
 # L2 open design (click 13.6)
 (12.4, 17.0, 4.7),
 # L3 Canva AI click ~22.8 ; panel opens
 (21.9, 25.2, 4.4),
 # L4 describe: panel idle (2x), zoom to prompt field, empty field (2x)
 (25.2, 28.9, 1.85), (28.9, 31.3, 3.1), (31.3, 33.7, 1.2),
 # L5 paste prompt, typing (borrowed rock-prompt typing), zoom to prompt + submit button
 (33.6, 34.3, 0.7), (239.4, 241.2, 1.8), (47.3, 48.4, 1.47),
 # L6 submit click 48.4, working bubble
 (48.4, 50.6, 2.8),
 # L7 generated track card
 (72.9, 78.3, 5.0),
 # L8 listen / preview (card + page tiles)
 (84.6, 88.7, 4.6),
 # L9 ask for fewer instruments (borrowed follow-up typing + send)
 (243.0, 245.0, 2.0), (277.7, 279.9, 2.4),
 # L10 add track (click 89.7), position on timeline
 (88.7, 91.3, 2.6), (109.0, 112.6, 3.2),
 # L11 trim, lower volume
 (114.0, 116.8, 2.0), (148.4, 150.9, 2.3),
 # L12 fade
 (160.6, 165.0, 4.4),
 # L13 elements -> audio library
 (174.5, 176.5, 2.6), (176.5, 177.6, 0.85), (186.2, 189.2, 2.85),
 # L14 canva ai prompt workflow
 (233.2, 237.0, 4.75),
 # L15 generation availability (generation + done)
 (210.5, 214.2, 3.7),
 # L16 option missing (Canva AI not available in video design)
 (215.6, 219.3, 4.2),
 # L17 musical direction (typing + send)
 (246.5, 248.5, 2.35), (253.0, 255.2, 2.75),
 # L18 terms (second track on timeline / present)
 (293.7, 301.0, 7.5),
 # L19 preview the complete mix
 (265.8, 269.1, 3.322),
]
segs, t, prev = [], 0.0, None
for a, b, d in PIECES:
    s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(t + d, 3), "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        s["xfade"] = True
    print(f"{t:6.2f}-{t+d:6.2f} src {a}-{b} {(b-a)/d:.2f}x")
    segs.append(s); prev = b; t += d
print('total', round(t, 3))
segs[-1]["out_end"] = END
pr = json.load(open(P + 'probe.json'))['recording']
plan = {"output": {"duration": END, "fps": 30.0, "width": pr['width'], "height": pr['height']},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None,
        "sync": [], "style": {}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
