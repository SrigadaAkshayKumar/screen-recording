"""script-20 re-edit 3: per-line plan built from 1 s / 0.3 s sheets (work/analyze-notes.md).
Chain L4-L10 in recording order; each UI change lands on its words:
Download page click ~"choose Download", type list opens ~"PNG", Custom click + checklist ~"checklist",
page 3 ticked at "page there", Download click on "click Download"."""
import json, sys
P = 'projects/script-20/work/'
D = 95.202
segs = []
def sp(o0, o1, a, b, xf=False, wait=False):
    s = {"src_start": round(a, 3), "src_end": round(b, 3), "out_start": round(o0, 3), "out_end": round(o1, 3), "mode": "speed"}
    if xf: s["xfade"] = True
    if wait: s["wait"] = True
    segs.append(s)
def hold(o0, o1, a):
    segs.append({"src_start": a, "src_end": a, "out_start": round(o0, 3), "out_end": round(o1, 3), "mode": "hold"})
o = 0.0
def run(a, b, rate, xf=False, wait=False):
    global o
    d = (b - a) / rate; sp(o, o + d, a, b, xf, wait); o += d
def hld(a, d):
    global o
    hold(o, o + d, a); o += d
def fit(a, b, o_end, xf=False, wait=False):
    global o
    sp(o, o_end, a, b, xf, wait); o = o_end

# L1-L3
sp(0, 4.2, 0.0, 3.15); o = 4.2
sp(4.2, 12.42, 3.9, 12.1, xf=True); o = 12.42
# L4: right-click menu already open, cursor to "Download page" (click src 23.0 -> out ~14.4)
run(20.5, 23.0, 1.0, xf=True)
run(23.0, 24.0, 1.0)                      # panel slides in
run(24.0, 26.8, 1.1)                      # panel idle -> file type list opens (~"PNG")
run(26.8, 27.2, 0.75)
HOLD1 = float(sys.argv[1]) if len(sys.argv) > 1 else 1.4
hld(27.2, HOLD1)                          # list fully open while the types are read out
run(27.2, 30.0, 0.75)                      # cursor over the list, PNG chosen
run(30.0, 31.6, 0.75)                     # PNG options, Select pages control
# tail backwards from the Download click: src 41.9 at out 42.85, 0.75x
tail_start = 42.85 - (41.9 - 31.6) / 0.75
slack = tail_start - o
h2 = min(1.4, slack)
if h2 > 0.05: hld(31.6, h2)               # Select pages control framed at "page selection control"
run(31.6, 32.2, 0.75)                     # cursor reaches "This page"
h3 = tail_start + 0.8 - o
print('slack', round(slack, 2), 'h3', round(h3, 2), file=sys.stderr)
if h3 > 0.05: hld(32.2, min(h3, 1.45))
fit(32.2, 41.9, 42.85)
# click -> viewer opens (waiting for the download, <=2x)
fit(41.9, 46.0, 44.9, wait=True)
# L11 file opens
sp(44.9, 47.18, 46.0, 48.3); o = 47.18
# L12: PDF first (narration order), then the image
sp(47.18, 50.4, 55.5, 58.3, xf=True)
sp(50.4, 53.54, 48.3, 50.9, xf=True)
# L13 "part many tutorials skip": Download page click, panel
sp(53.54, 56.32, 22.4, 24.5, xf=True)
# L14: download menu page selection (All / This page / Custom -> checklist)
sp(56.32, 61.82, 31.4, 35.6, xf=True)
# L15: final selection before Download
sp(61.82, 65.22, 39.0, 41.6, xf=True)
# L16: file type list
sp(65.22, 69.94, 26.3, 30.0, xf=True)
# L17: PDF panel, PNG options
sp(69.94, 73.6, 24.0, 26.8, xf=True)
sp(73.6, 76.8, 29.9, 32.3)
# L18: pages (grid) view
sp(76.8, 80.0, 15.1, 17.6, xf=True)
sp(80.0, 82.9, 19.0, 21.2)
# L19: page selection checklist
sp(82.9, 90.08, 33.0, 38.4, xf=True)
# L20
sp(90.08, D, 58.5, 62.4, xf=True)
plan = {"output": {"duration": D, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.2f}-{s['src_end']:6.2f} {s['mode']} {(s['src_end']-s['src_start'])/d:.2f}x")
