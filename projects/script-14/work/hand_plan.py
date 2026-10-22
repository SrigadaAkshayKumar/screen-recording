"""Hand-built plan + actions for script-14 (220 s recorder-zoomed recording, 77.5 s voiceover).
Pieces are (src_a, src_b, out_a, out_b); a click sits at the end of the piece group that leads up to it."""
import json
P = 'projects/script-14/work/'
D = 77.462
lines = json.load(open(P + 'lines.json'))
widx = {(l['id'], w['word'].strip('.,').lower(), round(w['start'], 2)): w['i'] for l in lines for w in l['words']}
# (src_a, src_b, out_a, out_b)
PIECES = [
 (2.7, 8.45, 0, 6.54),
 (8.45, 9.3, 6.54, 7.59),
 (15.2, 16.12, 7.59, 8.28),
 (16.12, 17.21, 8.28, 9.73),
 (25.0, 26.95, 9.73, 11.3),
 (26.95, 31.35, 11.3, 17.1),
 (31.35, 32.55, 17.1, 18.1),
 (32.55, 34.43, 18.1, 20.56),
 (74.0, 79.2, 20.56, 25.38),
 (79.2, 87.1, 25.38, 34.0),
 (109.6, 116.3, 34.0, 42.78),
 (98.1, 102.6, 42.78, 46.28),
 (120.0, 124.65, 46.28, 50.58),
 (124.65, 125.5, 50.58, 51.46),
 (125.5, 128.1, 51.46, 54.9),
 (165.9, 177.0, 54.9, 69.4),
 (181.0, 181.9, 69.4, 70.3),
 (188.1, 189.2, 70.3, 71.38),
 (200.6, 202.65, 71.38, 73.42),
 (202.65, 203.95, 73.42, 75.06),
 (203.95, 206.0, 75.06, D),
]
segs, prev = [], None
for a, b, o0, o1 in PIECES:
    s = {"src_start": a, "src_end": b, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = b

A = [  # id, t_click, x, y, target, result, t_result, conf, (line, word, word_t) or None
 ("A1", 8.45, 970, 575, "video on the canvas", "video selected, its toolbar appears", 9.2, "medium", (2, "video", 6.54)),
 ("A2", 16.12, 1000, 573, "caption on the video", "caption selected (outline + toolbar)", 16.3, "medium", (2, "animate", 8.28)),
 ("A3", 26.95, 1482, 214, "Animate button in the toolbar", "Animate panel opens on the left", 27.4, "high", (3, "available", 11.2)),
 ("A4", 29.45, 335, 695, "Highlight card (Captions section)", "preview plays the Highlight effect", 29.6, "medium", None),
 ("A5", 31.35, 204, 695, "Reveal card (Captions section)", "Reveal selected", 31.45, "high", (5, "reveal", 17.22)),
 ("A6", 32.55, 335, 695, "Highlight card (Captions section)", "Highlight selected, preview plays", 32.7, "high", (5, "highlight", 18.1)),
 ("A7", 79.2, 199, 758, "Typewriter in Suggested text animations", "Typewriter selected, Animate options show", 79.4, "high", (7, "animation", 25.38)),
 ("A8", 124.65, 564, 214, "Captions button in the toolbar", "Captions panel opens", 124.7, "high", (12, "through", 50.58)),
 ("A9", 125.5, 423, 350, "Styles tab", "caption style packs listed", 125.8, "high", (12, "panel", 51.46)),
 ("A10", 177.0, 1015, 715, "Play button", "playback starts (after a short load)", 181.0, "medium", (16, "play", 69.4)),
 ("A11", 189.2, 1015, 715, "Play button", "second playback starts", 200.6, "low", (16, "once", 71.38)),
 ("A12", 202.65, 1818, 160, "Share button", "Share design panel opens", 202.9, "medium", (17, "finished", 73.42)),
 ("A13", 203.95, 1215, 768, "Download in the share panel", "Download panel (MP4 video) opens", 204.2, "medium", (17, "video", 75.06)),
]
actions = {"recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 220.1},
 "sync": {"clicks_offset": 0, "source": "frames"},
 "actions": [{"id": i, "t_click": t, "x": x, "y": y, "kind": "click", "target": tg, "result": r,
              "t_result_visible": tr, "confidence": c} for i, t, x, y, tg, r, tr, c, _ in A],
 "junk": [
  {"start": 0.0, "end": 2.667, "reason": "static opening, cursor only", "ff": True},
  {"start": 34.433, "end": 44.1, "reason": "idle panel, cursor only", "ff": True},
  {"start": 51.567, "end": 64.833, "reason": "idle (frozen) panel", "ff": True},
  {"start": 65.9, "end": 71.9, "reason": "idle panel", "ff": True},
  {"start": 87.167, "end": 96.9, "reason": "idle panel, cursor only", "ff": True},
  {"start": 116.333, "end": 119.567, "reason": "idle panel", "ff": True},
  {"start": 128.1, "end": 137.767, "reason": "idle styles panel", "ff": True},
  {"start": 147.2, "end": 151.033, "reason": "cursor-only slider hover", "ff": True},
  {"start": 154.933, "end": 165.933, "reason": "idle panel", "ff": True},
  {"start": 190.0, "end": 199.9, "reason": "player loading spinner", "ff": False},
  {"start": 216.2, "end": 220.1, "reason": "recorder stop / desktop", "ff": False}]}
sync = []
for (i, *_rest, s) in A:
    if s:
        ln, w, wt = s
        sync.append({"action": i, "line": ln, "word": w, "word_index": next(v for k, v in widx.items() if k[0] == ln and k[1] == w and abs(k[2] - wt) < .02), "word_t": wt})
plan = {"output": {"duration": D, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [], "ripples": [],
        "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(actions, open(P + 'actions.json', 'w'), indent=1)
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
