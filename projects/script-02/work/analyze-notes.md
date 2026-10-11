# analyze notes (script-02)

- No click log: every click time was read from frames (±0.1-0.2 s). Confidence per action is in actions.json.
- **x/y are approximate** for most actions and not checked with a crosshair (the recorder's auto-zoom makes
  the recording-pixel position change between frames). The sync step therefore uses `no_ripple` for all clicks.
- **Baked-in recorder zoom**: the footage is already auto-zoomed on most clicks (e.g. 43.5, 58.5, 89.4, 111, 165, 177, 277 s).
  The plan adds no zooms of its own.
- The recording is 291 s, the voiceover 81 s: the footage has long idle stretches (waiting on the slide 18-32 s,
  hovering in the animate panel 141-155 s, trying animations 201-250 s).
- Low-confidence items: A6 (the Edit panel was already open when Edit was clicked), A7 (the HR row removal moment),
  A8/A9 (colour swatch + hex field, the picker is only visible zoomed), A12, A15, A16, A18, A22.
- Narration vs recording: "search for Charts" - the recording browses the Apps grid and clicks the Charts icon, nothing is typed.
  "Preview the slide in presentation mode" - no presentation mode was recorded; the closest is the animation
  preview playing on page 2 (263-268 s) (A22).
- Drag-resize of the chart at 156-162 s is not narrated and was undone: junk (cut, no fast-forward).
- The recording ends with the Windows tray popup at 288 s: not used.
