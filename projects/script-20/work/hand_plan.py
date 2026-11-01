"""script-20 re-edit: per-line plan built from the 1 s sheets (see work/analyze-notes.md / sync-notes.md).
Chain L4-L10 runs in recording order at the 0.75x floor so the Download click lands on 'click Download'."""
import json
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
def piece(o0, a, b, rate, xf=False):
    o1 = o0 + (b - a) / rate
    sp(o0, o1, a, b, xf); return o1

# L1-L3: home screen, design opens, page thumbnails (one 1.0x run from the loading editor)
sp(0, 4.2, 0.0, 3.15)
sp(4.2, 12.42, 3.9, 12.1, xf=True)
# L4-L10 chain: grid -> page menu -> Download page -> panel -> type list -> select pages -> custom -> tick -> Download
o = 12.42
o = piece(o, 19.7, 40.7, 0.75, xf=True)
hold(o, o + 1.0, 40.7); o += 1.0          # 'only page 3 ticked, Download enabled' during "Confirm that only one page..."
o = piece(o, 40.7, 41.6, 0.75)            # Download click lands at ~43.0 (words "click Download")
# click -> file opens (wait footage, ~1.8x)
src = 45.4
sp(o, 44.7, 41.6, src, wait=True)        # <= 2x (client pace rule)
# L11 file opens
sp(44.7, 47.18, src, src + 2.78 * 0.95)
# L12: PDF first (narration order), then the image
sp(47.18, 50.4, 55.5, 58.3, xf=True)
sp(50.4, 53.54, 48.3, 50.9, xf=True)
# L13 reuse: Download menu opening
sp(53.54, 56.32, 22.4, 24.5, xf=True)
# L14: thumbnail click in the editor, then the download menu's page selection
sp(56.32, 59.72, 9.6, 12.2, xf=True)
sp(59.72, 61.82, 30.1, 31.7, xf=True)
# L15: custom page selection
sp(61.82, 65.22, 35.6, 38.2, xf=True)
# L16-L17: file type list, PNG options, back to the PDF panel / type list
sp(65.22, 69.94, 26.0, 29.6, xf=True)
sp(69.94, 73.14, 29.6, 32.0)
sp(73.14, 76.8, 24.2, 27.0, xf=True)
# L18: pages view in the editor
sp(76.8, 82.9, 15.1, 19.9, xf=True)
# L19: page selection control -> pages
sp(82.9, 90.08, 30.6, 36.1, xf=True)
# L20: closing
sp(90.08, D, 58.5, 62.4, xf=True)
plan = {"output": {"duration": D, "fps": 30, "width": 3420, "height": 1922},
        "segments": segs, "zooms": [], "ripples": [], "intro": None, "outro": None, "sync": [],
        "style": {"ripple_color": "#2F80ED", "ripple_alpha": 0.6, "cursor_halo": False}}
json.dump(plan, open(P + 'plan.json', 'w'), indent=1)
for s in segs:
    d = s['out_end'] - s['out_start']
    print(f"out {s['out_start']:7.2f}-{s['out_end']:7.2f} src {s['src_start']:6.2f}-{s['src_end']:6.2f} {s['mode']} {(s['src_end']-s['src_start'])/d:.2f}x")
