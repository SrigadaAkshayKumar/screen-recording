"""Hand-budgeted plan for script-12 (213 s recording, 104.8 s voiceover, baked-in recorder zoom: no zooms/ripples)."""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
D = 104.815
# (out_end, src_a, src_b, label); out_start = previous out_end
Q = [
 (8.0, 4.6, 10.7, "L1 homepage, search typed"),
 (10.26, 10.7, 12.73, "L2 results page"),
 (14.3, 12.73, 15.8, "L2-3 template chosen"),
 (17.9, 16.4, 19.8, "L3 editor opens"),
 (21.24, 24.0, 28.4, "L4 title selected and replaced"),
 (27.32, 44.0, 52.5, "L5 date/venue text edit"),
 (30.24, 57.0, 60.0, "L6 (no delete footage) editing continues"),
 (34.04, 117.0, 120.5, "L7 photo section"),
 (37.0, 63.8, 66.77, "L8 layout browsing"),
 (38.1, 66.77, 68.97, "L8 static spell at 2x"),
 (40.52, 68.97, 71.0, "L8 layout browsing"),
 (44.44, 72.0, 76.0, "L9 button/link text"),
 (46.64, 85.5, 87.7, "L10 right-click -> Link"),
 (48.84, 96.0, 99.0, "L10 paste map link"),
 (55.0, 150.0, 156.0, "L11 form link / form tab"),
 (59.64, 132.2, 138.0, "L12 RSVP button link"),
 (63.7, 105.5, 109.5, "L13 button selected"),
 (67.12, 161.5, 165.0, "L14 mobile preview"),
 (71.94, 199.9, 204.4, "L15 site buttons -> destinations"),
 (78.82, 158.0, 164.8, "L16 publish panel"),
 (83.96, 165.0, 170.0, "L17 address / mobile"),
 (86.98, 175.46, 178.0, "L18 publish click"),
 (89.4, 178.0, 182.7, "L19 website live (progress, 2x)"),
 (91.0, 186.3, 187.5, "L20 open site"),
 (94.12, 194.8, 197.8, "L20 site scroll"),
 (98.96, 204.4, 208.4, "L21 form"),
 (101.9, 155.4, 158.0, "L22 republish: back to Publish"),
 (D, 209.0, 212.2, "closing"),
]
segs = []; o = 0.0; prev = None
for oe, a, b, lab in Q:
    s = {"mode": "speed", "src_start": a, "src_end": b, "out_start": round(o, 3), "out_end": oe}
    if prev is not None and abs(a - prev) > 0.05: s["xfade"] = True
    segs.append(s); prev = b
    print(f"{lab:40s} {(b-a)/(oe-o):.2f}x")
    o = oe
plan = {"output": {"duration": D, "fps": 30.0, "width": 1920, "height": 1080}, "segments": segs,
        "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False},
        "notes": ["hand-built by hand_plan.py; recorder zoom is baked in so no zooms/ripples"]}
json.dump(plan, open(os.path.join(here, "plan.json"), "w"), indent=1)
