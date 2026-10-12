# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | select | 8.040 | A1 animated Welcome text | 21.500 | 1.24x |
| 3 | layer. | 15.040 | A2 Welcome layer in the video timeline | 35.400 | 0.87x |
| 6 | edge | 25.580 | A4 right edge of the layer | 43.400 | 0.76x |
| 8 | select | 36.740 | A5 Welcome text (selected again) | 109.300 | 0.89x |
| 8 | animate. | 38.520 | A6 Animate button in the toolbar | 110.900 | 0.90x |
| 9 | duration | 42.760 | A8 Speed slider | 115.000 | 0.97x |
| 11 | presets, | 52.060 | A13 Speed presets Slow / Medium / Fast | 166.100 | 1.10x |
| 12 | right | 59.640 | A9 welcome text in the presentation design | 131.200 | 0.92x |
| 12 | Show | 61.100 | A10 Show element timing menu item | 133.200 | 1.37x |
| 13 | timeline | 65.200 | A11 layer on the video timeline | 144.400 | 0.88x |
| 17 | Preview | 80.100 | A14 Play button in the preview | 193.000 | 0.93x |

## Builder decisions

- A5: after A4 (until src 50.00) jumps ahead to src 106.00 - narration order
- A13: after A8 (until src 121.10) jumps ahead to src 162.00 - narration order
- A9: after A13 (until src 170.90) jumps back to src 129.00 - narration order
- A11: after A10 (until src 135.40) jumps ahead to src 143.00 - narration order
- A14: after A11 (until src 147.40) jumps ahead to src 182.20 - narration order

## Judgment calls

- Narration order wins: footage is reordered with cross-fades (jumps at out 11.1 [cut of cursor idle], 33.0, 48.3, 57.3, 63.6, 68.4). Recording order was select -> layer -> animate(typewriter) -> presentation -> bird animate; narration wants layer edits, then animate duration controls, then speed presets, then Show Element Timing, then video timeline.
- Anchors: A1 "select" (L2), A2 "layer." (L3), A4 "edge" (L6), A5 "select" + A6 "animate." (L8), A8 "duration" (L9, slider drag; the preview "W-e-l.." plays over L10), A13 "presets" (L11, bird panel), A9 "right" + A10 "Show" (L12), A11 "timeline" (L13), A14 "Preview" (L17, play click then the real preview runs to the end).
- A3, A7, A12 are not anchored: they play in the interval of the neighbouring anchors (A3 drag along the layer inside A2->A4; A7 slider click just before A8; A12 Animate click on the bird before A13). Tying them would need >1.5x or held frames.
- Cuts: src 8.9-20.4 (junk retake), 24.2-32.0 (cursor idle over Animate tooltip; ff did not fit, so a cross-faded cut). Everything else is kept at 0.76-1.37x; no held frames at all.
- No zooms (recorder zoom is baked in) and no ripples (positions during recorder zoom are unreliable).
- L7 plays src 43.4-50.0 slowly (0.89x), including ~3 s of a static W frame (the page preview parked at 0:00); real footage, not a plan hold.
- Closing L14-L16 plays src 182.2-193.0 at 0.93x; the last 4.5 s (src 194.5-199.4) is the preview playing; verify's freeze there is static source (playhead only).
- Pace: check.py --plan prints no pace warnings. The only warnings left are the three unanchored actions above.
