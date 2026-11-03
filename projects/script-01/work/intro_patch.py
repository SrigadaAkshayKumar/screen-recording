"""Hand patch applied after plan_builder: the opening 7.8 s of the recording is a frozen home page,
so the first 3.6 s of narration show the finished film strip moving (src 347.4-351.0), then
cross-fade to the real start (src 5.2 -> 11.9). Re-run after every plan_builder run."""
import json, sys
f = sys.argv[1] if len(sys.argv) > 1 else "projects/script-01/work/plan.json"
p = json.load(open(f))
s0 = p["segments"][0]
assert s0["src_start"] == 0.0 and s0["out_end"] > 9.9, s0
o1 = s0["out_end"]
a = {"src_start": 347.4, "src_end": 351.0, "out_start": 0.0, "out_end": 3.6, "mode": "speed"}
b = {"src_start": 5.2, "src_end": s0["src_end"], "out_start": 3.6, "out_end": o1, "mode": "speed", "xfade": True}
p["segments"][0:1] = [a, b]
p["intro"] = "flash-forward of the finished film strip (src 347.4-351.0), then the real start"
json.dump(p, open(f, "w"), indent=1)
