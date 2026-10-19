"""Hand-budgeted plan for script-10 (plan_builder cannot slow footage below 1x; see docs/lessons.md)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
# (src_a, src_b, out_a, out_b, xfade)
Q = [
 (5.3, 9.3, 0.0, 5.33, False), (25.2, 32.0, 5.33, 14.4, True), (9.3, 12.4, 14.4, 18.4, True),
 (36.12, 37.3, 18.4, 19.58, True), (37.3, 38.3, 19.58, 20.58, False), (31.8, 36.0, 20.58, 26.1, True),
 (47.15, 49.8, 26.1, 28.75, True), (49.8, 50.5, 28.75, 29.45, False), (55.75, 56.4, 29.45, 30.1, True),
 (56.4, 59.5, 30.1, 31.9, False), (77.4, 79.4, 31.9, 33.9, True), (82.3, 83.8, 33.9, 35.46, True),
 (83.8, 102.8, 35.46, 59.12, False), (102.8, 106.8, 59.12, 63.9, False), (106.8, 115.9, 63.9, 75.1, False),
 (182.3, 184.5, 75.1, 77.3, True), (184.5, 185.8, 77.3, 78.32, False), (185.8, 189.5, 78.32, 82.939, False),
]
segs = []
for a, b, oa, ob, x in Q:
    s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": oa, "out_end": ob}
    if x: s["xfade"] = True
    segs.append(s)
words = json.load(open(os.path.join(here, "words.json")))
W = words["words"] if isinstance(words, dict) else words
def idx(t): return min(range(len(W)), key=lambda i: abs(W[i]["start"] - t))
sync = []
for act, line, word, t in [("A3",5,"captions",19.58),("A4",7,"select",28.7),("A5",7,"generate",30.1),("A7",9,"Play",35.46),
                           ("A8",14,"first",59.12),("A9",15,"caption",63.9),("A10",18,"Download",77.3),("A11",18,"MP4",78.32)]:
    sync.append({"action": act, "line": line, "word": word, "word_index": idx(t), "word_t": t})
plan = {"output": {"duration": 82.939, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": sync, "style": {},
        "notes": ["hand-built by hand_plan.py"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
