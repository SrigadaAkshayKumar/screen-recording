"""Hand-built plan for script-11 (recording has baked-in recorder zoom: no zooms/ripples; 214 s of footage for
83 s of voiceover; the language-settings screen is not in the recording, so L6-L10 reuse captions-panel footage)."""
import json
P = 'projects/script-11/work/'
END = 83.127
# (out_start, out_end, src_start, src_end)
G = [
 (0, 6.94, 10.0, 16.94),
 (6.94, 11.84, 17.0, 23.0),
 (11.84, 15.24, 30.5, 34.7),
 (15.24, 18.8, 34.7, 37.4),
 (18.8, 20.82, 37.4, 39.4),
 (20.82, 23.12, 42.0, 45.1),
 (23.12, 29.14, 45.1, 50.0),
 (29.14, 34.56, 71.4, 76.0),
 (34.56, 49.3, 118.8, 133.7),
 (49.3, 50.76, 133.7, 135.5),
 (50.76, 54.56, 135.5, 139.3),
 (54.56, 59.2, 88.0, 93.0),
 (59.2, 71.48, 148.0, 158.5),
 (71.48, 76.1, 163.8, 168.4),
 (76.1, 77.6, 197.5, 199.0),
 (77.6, END, 201.0, 208.0),
]
segs, prev = [], None
for o0, o1, s0, s1 in G:
    s = {"src_start": s0, "src_end": s1, "out_start": o0, "out_end": o1, "mode": "speed"}
    if prev is not None and abs(s0 - prev) > 0.002:
        s["xfade"] = True
    segs.append(s); prev = s1
    print(f"{o0:6.2f}-{o1:6.2f} {(s1-s0)/(o1-o0):.2f}x src {s0}-{s1}")
words = {}
for l in json.load(open(P + 'lines.json')):
    for w in l['words']:
        words[(l['id'], w['word'].strip('.,').lower())] = w
# action id, src click time, line, word
A = [("A1", 34.7, 4, "open"), ("A2", 37.4, 5, "dynamic"), ("A3", 43.0, 5, "media"),
     ("A4", 45.1, 5, "toolbar"), ("A5", 133.7, 11, "apply"), ("A6", 135.5, 11, "generate")]
sync = []
for a, t, ln, wd in A:
    w = words[(ln, wd)]
    sync.append({"action": a, "line": ln, "word": w['word'], "word_index": w['i'], "word_t": w['start']})
    for s in segs:
        if s['src_start'] - 1e-6 <= t <= s['src_end'] + 1e-6:
            print(a, 'click at out', round(s['out_start'] + (t - s['src_start']) / (s['src_end'] - s['src_start']) * (s['out_end'] - s['out_start']), 3), 'word', w['start'])
            break
plan = {"output": {"duration": END, "fps": 30, "width": 1920, "height": 1080}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": sync,
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
