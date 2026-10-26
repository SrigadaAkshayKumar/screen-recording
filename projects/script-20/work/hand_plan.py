"""Hand plan for script-20 (new 116.9 s sticker-sheet take, 101.285 s voiceover, 3420x1922, baked recorder zoom: no zooms).
Moving windows (freezedetect n=0.003 d=0.8, each extended 0.8 s into the following stillness) played in recording order
at one uniform speed, cross-faded between windows."""
import json
P = 'projects/script-20/work/'
END = 101.285
M = [(8.93,11),(12.83,17.17),(18.23,20.37),(26.83,39.47),(41.47,48.3),(49.43,55.07),(56.1,57.8),(58.6,64.17),(70.2,74.77),(76.73,78.23),(79.27,80.37),(81.37,96.87),(97.93,102.1),(105.6,114.37)]
EXT = 0.8
W = [(a, b + EXT) for a, b in M]
tot = sum(b - a for a, b in W)
sp = tot / END
print("total", tot, "speed", sp)
segs, t, prev = [], 0.0, None
for k, (a, b) in enumerate(W):
    end = END if k == len(W) - 1 else t + (b - a) / sp
    s = {"src_start": a, "src_end": b, "out_start": round(t, 3), "out_end": round(end, 3), "mode": "speed"}
    if prev is not None and abs(a - prev) > 0.002: s["xfade"] = True
    segs.append(s); prev = b; t = end
plan = {"output": {"duration": END, "fps": 30, "width": 3420, "height": 1922}, "segments": segs, "zooms": [],
        "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
json.dump({"recording": {"width": 3420, "height": 1922, "fps": 30, "duration": 116.9}, "sync": {"source": "frames"},
           "actions": [{"id": "A1", "t_click": 9.5, "x": 400, "y": 300, "kind": "click", "target": "canvas",
                        "result": "design changes", "t_result_visible": 10.5, "confidence": "low"}],
           "junk": []}, open(P + 'actions.json', 'w'), indent=1)
