# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 5.840 | A1 Continue designing: sample design card | 9.700 | 1.66x |
| 2 | Elements, | 7.240 | A2 Elements tab in the side bar | 14.500 | 3.43x |
| 2 | basic | 8.260 | A3 Shapes category | 18.200 | 3.63x |
| 3 | circle. | 10.920 | A4 Circle in Basic shapes | 20.550 | 0.88x |
| 4 | color, | 12.240 | A7 colour picker (hue slider) | 45.500 | 2.01x |
| 4 | resize | 12.960 | A5 circle corner handle | 33.500 | 2.78x |
| 4 | position | 14.120 | A6 circle on the page | 35.000 | 1.29x |
| 5 | Select | 16.680 | A8 blue circle | 49.700 | 0.98x |
| 5 | Animate. | 17.960 | A9 Animate button in the toolbar | 51.500 | 1.41x |
| 6 | Element | 19.620 | A10 Element tab in the Animate panel | 54.900 | 2.05x |
| 7 | Rise | 26.040 | A11 Rise style | 71.000 | 2.51x |
| 8 | choose | 29.720 | A12 direction arrow | 81.200 | 2.77x |
| 9 | speed | 32.260 | A13 Medium speed button | 84.200 | 1.18x |
| 10 | Play | 35.460 | A14 Play button | 120.300 | 1.00x +0.8s hold |
| 11 | switch | 39.600 | A15 Pan style (subtler animation) | 134.200 | 0.97x |
| 12 | select | 45.960 | A20 second circle (shift-click) | 236.600 | 1.00x +2.6s hold |
| 12 | Group. | 48.060 | A21 Group button | 238.900 | 1.10x |
| 14 | separate | 52.580 | A16 Animate button for the second shape | 173.900 | 1.00x +1.7s hold |
| 14 | individually. | 54.500 | A17 Fade style for the second shape | 179.900 | 3.12x |
| 15 | timeline | 57.380 | A18 timeline | 216.400 | 1.01x |
| 16 | introducing | 60.820 | A19 timeline play button | 225.700 | 2.70x |
| 19 | ungroup | 73.740 | A22 Ungroup button | 250.600 | 1.04x |
| 20 | Preview | 76.880 | A23 Play button | 263.200 | 0.89x |
| 20 | download | 78.420 | A24 Download in the Share menu | 269.000 | 3.77x |
| 20 | MP4 | 79.240 | A25 MP4 Video file type | 271.300 | 2.80x |
| 21 | GIF | 81.400 | A26 GIF file type | 277.900 | 3.06x |

## Builder decisions

- A7: after A4 (until src 22.40) jumps ahead to src 44.30 - narration order
- A4->A7: cut src 22.00-31.00 - too long to fast-forward at <= 2.00x (idle after placing the circle)
- A5: after A7 (until src 47.00) jumps back to src 33.00 - narration order
- A8: after A6 (until src 36.40) jumps ahead to src 48.60 - narration order
- A14: after A13 (until src 85.30) jumps ahead to src 119.00 - narration order
- A15: after A14 (until src 122.70) jumps ahead to src 132.60 - narration order
- A20: after A15 (until src 135.60) jumps ahead to src 234.20 - narration order
- A16: after A21 (until src 240.20) jumps back to src 172.40 - narration order
- A18: after A17 (until src 181.60) jumps ahead to src 215.20 - narration order
- A22: after A19 (until src 228.50) jumps ahead to src 240.00 - narration order
- A23: after A22 (until src 252.40) jumps ahead to src 262.20 - narration order

## Judgment calls

- **No zooms, no ripples.** The recording has the recorder's own auto-zoom baked in (lessons: script-1, script-18); coordinates inside those zooms are estimates, so every action is in `no_ripple` and `zooms` is empty.
- **Followed the audio order.** L4 says colour, resize, position; the recording does resize (33.5), position (35.0), then colour (45.5). Colour is shown first (A7, `src_from` 44.3), then a cross-fade back to resize/position (A5, A6), then a jump to the circle selection (A8, `src_from` 48.6). Likewise L12 (group, src 234-239) is narrated before L14 (separate animations, src 173-180) although the recording does it the other way round: cross-fade back at A16.
- Forward jumps with `src_from`: A14 (Play 119), A15 (Pan 132.6), A18 (timeline 215.2), A22 (ungroup 240), A23 (play 262.2). In-scene dead time (22-31 s idle, 86-116 s hovering over settings) is marked `ff`; the builder kept it as a cut because it exceeds 2x, i.e. the narration leaves no room.
- Anchors: A1 "Open", A2 "Elements", A3 "basic", A4 "circle", A7 "color", A5 "resize", A6 "position", A8 "Select", A9 "Animate", A10 "Element", A11 "Rise", A12 "choose", A13 "speed", A14 "Play", A15 "switch" (Pan = the subtler animation), A20 "select", A21 "Group", A16 "separate" (A16->A17 on "animate"/"individually" was 1.1 s for 6 s of footage, > 4x), A17 "individually", A18 "timeline", A19 "introducing", A22 "ungroup", A23 "Preview", A24 "download", A25 "MP4", A26 "GIF".
- Unmentioned/missing: L13 "Then animate the group" has no action (group idles on screen); L16 "second shape one second later" is only matched to a timeline play click (A19, low confidence) - the recording never shows a staggered bar; L9 "speed or duration" matched to one Medium click (A13), the rest of the hovering is cut.
- A3 warning: the Shapes list is only loaded 0.3 s after line 2 ends; accepted.
- Trimmed the ending: junk 283.8-288.8 (desktop after export) is removed.
