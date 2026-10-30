# Analyze notes
- No clicks.json; every click time/position comes from frames. Recording has baked-in recorder auto-zoom (e.g. 16-18, 19-25, 34, 40-43, 64-70, 127-165, 199-209, 226, 236-256), so many coordinates are unzoomed-layout estimates: A1-A5, A9-A18 low/medium.
- Click moments inferred from cursor position and first visible response; low-confidence: A2, A3 (file dialog, native), A10-A13 (timeline drags / zoom control), A12 (Position opened what looks like the colour panel).
- Not turned into actions: the click at ~17.9 that resets to an empty video design (narration "open a video design"), the timeline trim 33-36 s (33.5 s clip shortened to 9.3 s), picking the blue swatch ~132.9, adding a second track 143-147, gradient choice ~157.5, scrubbing 196-210.
- BG Remover processing is visible 43-54 s as the timeline thumbnails turn into cut-outs; 54.5-61.8 is a still span.
- Recording order differs from the audio: the recording plays the cut-out (64.5) BEFORE opening Edit (70.6); the audio opens Edit first. Both are reused in audio order.
- Junk: 0-15.5 idle editor (still cursor), 257.6-261.4 desktop and recorder stop.
- Script note: "BG Remover in the Editor toolbar" is shown; "Layers" panel itself is never opened in the recording.
