"""Hand-budgeted plan for script-12 (352 s recording, 98.17 s voiceover, baked-in recorder zoom: no zooms/ripples)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
D = 98.174
# (out_end, src_a, src_b, label); out_start = previous out_end
Q = [
 (2.9, 2.7, 4.9, "L1 editor with portfolio design"),
 (7.3, 10.8, 15.0, "L1-2 website design, title selected"),
 (11.4, 21.1, 25.2, "L2 website panel (zoomed)"),
 (15.96, 25.2, 30.5, "L3 website panel / settings"),
 (19.32, 33.4, 36.77, "L4 Publish changes opens panel"),
 (22.14, 66.2, 70.2, "L5 custom domain dialog opens"),
 (23.4, 138.4, 140.0, "L6 old text cleared"),
 (25.42, 144.0, 148.0, "L6 typing the domain (2x)"),
 (29.12, 107.3, 111.0, "L7 domain field (zoomed)"),
 (31.86, 148.8, 151.9, "L8 Continue"),
 (35.06, 151.9, 154.8, "L9 loading connection step"),
 (36.86, 160.2, 161.9, "L9 connection page appears"),
 (39.48, 178.4, 181.0, "L9 Review steps -> DNS page"),
 (43.98, 181.0, 185.5, "L10 DNS instructions open"),
 (49.6, 185.5, 191.1, "L11 copy record"),
 (53.2, 191.1, 194.7, "L12 record added / next record"),
 (55.4, 194.7, 196.9, "L13 records list"),
 (61.06, 195.0, 199.9, "L14 I've updated my DNS records"),
 (63.98, 199.9, 202.9, "L15 back in Canva"),
 (66.5, 283.6, 286.3, "L16 DNS processing notice"),
 (72.6, 214.6, 220.7, "L16 publish panel settings"),
 (75.0, 220.7, 223.1, "L17 site address"),
 (78.82, 266.3, 270.1, "L18 site address dropdown"),
 (83.38, 273.5, 278.0, "L19 publish"),
 (87.78, 184.5, 188.9, "L20 compare records (reuse)"),
 (92.08, 229.4, 233.7, "L20 pasted record"),
 (D, 342.0, 348.1, "L21 open site"),
]
segs = []; o = 0.0; prev = None
for oe, a, b, lab in Q:
    s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": oe}
    if prev is not None and abs(a - prev) > 0.05: s["xfade"] = True
    segs.append(s); prev = b
    print(f"{lab:42s} {(b-a)/(oe-o):.2f}x")
    o = oe
plan = {"output": {"duration": D, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False},
        "notes": ["hand-built by hand_plan.py; recorder zoom is baked in so no zooms/ripples"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
