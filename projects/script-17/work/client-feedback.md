Client review of script-17 (wedding slideshow): "the visuals are not matching" the narration.

The previous version was a hand plan (no actions.json): footage was mapped to lines by guessing from
contact sheets, and several lines showed the wrong step. Redo it properly:
- Watch the recording first (contact sheets, then single frames with frames.py --at/--around at every
  scene change) and write a real actions.json: what is on screen and what changes at each moment
  (template search, uploads panel, dragging photos, double-click crop, title text, timeline durations,
  transitions, audio track, play, Share > Download > MP4). Baked-in recorder zoom is fine - just do not
  use the coordinates for zooms/ripples.
- For each narration line, show the footage of THAT step. Verify every line's chosen footage with a
  frame export at the start and middle of its piece before rendering, and list in the report, per line,
  what the viewer sees.
- Where the recording truly has no footage for a line, say so in the report and use the closest step,
  never an unrelated one.
- Keep the usual rules: each line's footage starts on its lines.json start, 0.75-1.5x, no freezes.
