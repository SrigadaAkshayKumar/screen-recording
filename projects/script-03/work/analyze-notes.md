# Analyze notes

- No click log: every click time/position was read from contact sheets and `--around` frames; all coordinates are estimates (confidence medium/low in actions.json).
- The recording has baked-in recorder auto-zoom (zoom in/out around most clicks). Positions of clicks made while zoomed were reconstructed from the unzoomed layout and are low-confidence; those clicks get no ripple.
- A4 (48.0) and A8 (97.5) are hovers, not clicks (no hover kind exists); A10/A11 (page advances in presentation mode) are guessed click times.
- A6 "On enter" and A7 speed drag (76.8-83.0): the panel scrolls while the cursor moves, so y positions are uncertain.
- Unnarrated actions: A12, A16, A17, A23 (page-1 thumbnail, text speed drag, page-2 thumbnail, MP4 file-type click). Page-1 selection at ~13.8 s is junk (ff).
- Narration mentions "keep apply to all pages off": shown as a hover on the button only.
- Script step "move to the second page" in presentation mode is shown as the page advancing at ~122.4 s.
