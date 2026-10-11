# Analyze notes

- No clicks.json: every time is read from frames, so t_click is +-0.3 s and x/y are rough.
- **The recording has baked-in recorder zoom** (zoom in/out around most clicks, events with huge magnitude). Coordinates of actions that happen inside a recorder zoom are estimates converted from the unzoomed layout; the sync step therefore uses no zooms and no ripples (lessons: script-1, script-18).
- Low confidence: A1 (open design - the click frame is hidden by the recorder's zoom/transition at 9.4-12.4), A2, A10 (Element tab already looked active when the panel opened), A12, A13, A17, A18, A19, A23.
- The narrated "position it" and "resize it" are both in the recording: position = move drag at 32.5 and 35.1, resize = corner drag at 33.5. Colour was picked after them (35.8-45.5); narration order is colour, resize, position.
- Narrated "Then animate the group" (L13): no click found; the group is selected at ~240 and left idle.
- Narrated "switch to a more subtle animation" (L11) matched to the Pan style click at ~134 (the animated design is a second "Untitled design" tab from 123 s).
- 141-213 s: a second circle is duplicated (156-160) and animated separately (Animate 174, Fade 180, direction/speed 192-205); this is the "animate each one individually" step but happens before the group step in the recording.
- Unnarrated: 100-117 speed/direction hovering, 123-132 timeline/new-tab view, 205-214 idle.
- Junk: 283.8-288.8 export done, desktop shown.
