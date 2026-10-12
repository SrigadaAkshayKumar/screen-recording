# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 4 | pencil | 13.380 | A1 page thumbnail / pencil icon | 12.500 | 0.93x |
| 6 | Drag | 19.380 | A2 playhead on the time ruler | 19.200 | 1.12x |
| 6 | inspect | 21.260 | A3 time ruler | 21.500 | 1.22x |
| 7 | play | 23.720 | A4 play button | 66.500 | 1.22x |
| 9 | clips | 30.940 | A6 clip on the main track | 136.200 | 1.00x |
| 10 | headings, | 35.500 | A11 Add a heading | 217.500 | 1.10x |
| 12 | Audio | 43.820 | A5 Add audio | 122.700 | 1.11x |
| 13 | edges | 49.180 | A7 clip edge handle | 147.000 | 0.99x |
| 14 | left | 52.880 | A13 text overlay on the timeline | 245.600 | 1.43x |
| 15 | More, | 60.520 | A8 Split in the clip toolbar | 170.300 | 1.14x |
| 16 | delete | 63.280 | A9 Delete (trash) button | 173.100 | 1.01x |
| 17 | zoom | 67.200 | A10 timeline zoom slider | 182.300 | 0.94x |
| 21 | canvas | 81.880 | A12 Welcome text on the canvas | 240.400 | 0.93x |
| 23 | Preview | 89.680 | A14 play button (preview) | 258.900 | 1.00x |
| 23 | export | 92.480 | A15 Share button | 269.900 | 1.07x |

## Builder decisions

- A4: after A3 (until src 22.50) jumps ahead to src 64.50 - narration order
- A6: after A4 (until src 70.90) jumps ahead to src 133.40 - narration order
- A11: after A6 (until src 137.70) jumps ahead to src 214.00 - narration order
- A5: after A11 (until src 222.50) jumps back to src 118.50 - narration order
- A7: after A5 (until src 125.50) jumps ahead to src 144.50 - narration order
- A13: after A7 (until src 151.00) jumps ahead to src 244.30 - narration order
- A8: after A13 (until src 248.00) jumps back to src 164.00 - narration order
- A10: after A9 (until src 175.00) jumps ahead to src 180.50 - narration order
- A12: after A10 (until src 193.60) jumps ahead to src 238.00 - narration order
- A14: after A12 (until src 246.80) jumps ahead to src 257.50 - narration order
- A15: after A14 (until src 261.00) jumps ahead to src 269.00 - narration order

## Judgment calls

- Recording (284.6 s) is ~3x the narration (95.7 s) and its order differs from the audio, so every step is anchored in narration order with `src_from`/`prev_until` jumps (11 cross-faded jumps, no cuts, no ff spans needed, no holds). All speeds 0.93-1.43x; `check.py --plan` prints no `pace:` warnings.
- Anchors: A1 "pencil", A2 "Drag", A3 "inspect", A4 "play" (play footage is from 66 s, the empty-timeline take), A6 "clips" (clip select; no reorder drag exists in the recording), A11 "headings" (Add a heading, 217 s), A5 "Audio" (Add audio menu), A7 "edges" (trim), A13 "left" (overlay move), A8 "More" (split; chosen so the split result is on screen before "delete"), A9 "delete", A10 "zoom", A12 "canvas", A14 "Preview", A15 "export".
- Zooms: none. The recorder baked in auto-zoom (lessons: script-01/18); ripples only on A1-A3 (unzoomed), `no_ripple` on the rest. A1 ripple point corrected to the cursor after the first preview.
- L8 (main track) and L10-11 (overlays) are shown with footage that follows the related click (clips in the timeline, heading overlaying the video), not with dedicated actions. L20 has no action.
- Warning left: A7 result (trim) appears 0.5 s after line 13 ends; trimming the take earlier was not possible without cutting the drag.
