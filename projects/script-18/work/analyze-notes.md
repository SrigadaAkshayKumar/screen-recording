# Analyze notes

No click log (clicks.json) was supplied, so all click times/positions were read from contact sheets
at 1-3 s steps plus the scene events; times are good to roughly +-0.3 s, coordinates are rough.
The recording has baked-in recorder auto-zoom (the view zooms on the timeline / panels), so
coordinates in actions.json are approximate recording pixels and are NOT used for zooms or ripples.

- A4 (Open in file dialog, 26.8): low confidence; the dialog closed between 26 and 27.
- A10, A14 (playhead clicks): low; derived from the playhead tooltip, no distinct event.
- A24 (transition icon), A30 (MP4 file type): low.
- Not in the recording although the script narrates it: **text** (L12 "Open text and add a heading",
  L13 font / position / layer) and **crop / reposition** (L16). The recorder never opened Text.
  The scene around 204-211 s trims the clips; no crop is shown.
- L18-L20 (page thumbnails / pencil icon): the recording shows the Editing (pencil) mode menu at
  266-281 s; no page-thumbnail view exists, so that part is narration over idle footage.
- Junk: 5.2-13.9 (leftover finished design before the new design starts), 109.8-111.7 (browser
  context menu opened by mistake), 187-203 and 228.5-265 (idle, ff), 271-292 (mode menu / draw tool
  detour), 341.5-end (after playback, recorder stop).
- 144-152 s: the cursor is clicking Play on the preview; a second play happens at 184 s.
