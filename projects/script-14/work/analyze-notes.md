# analyze notes (script-14, 286.2 s cafe-menu take, baked-in recorder zoom, no click log)
- No per-click analysis: the recorder zooms on its own, so ripples/zooms would land wrong. actions.json holds a single low-confidence action (A1, PDF download click ~259 s, position approximate) and is not used by the plan.
- Source moving windows were found with `freezedetect=n=0.003:d=0.8` on the recording; the plan uses only those.
- The recording does not match the script order exactly: it starts with ~7 s of static home screen and has no clear "group and duplicate item row" step; items are edited as text, then photos resized.
- The "PDF print" download is shown only as the PNG/file-type panel (241-248 s) and the PDF panel/toast (259-262 s).
