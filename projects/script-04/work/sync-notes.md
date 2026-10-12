# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 5.840 | A1 Copy of sample design thumbnail | 10.600 | 0.98x |
| 2 | Elements, | 7.240 | A2 Elements tab | 15.000 | 0.86x |
| 2 | shape. | 8.580 | A3 Shapes category | 18.000 | 1.34x |
| 3 | circle. | 10.920 | A4 circle in Basic shapes | 20.700 | 1.15x |
| 4 | color, | 12.240 | A5 colour swatch in the toolbar | 35.600 | 1.29x |
| 4 | canvas. | 15.500 | A6 blue colour swatch | 44.900 | 1.07x |
| 5 | circle | 17.100 | A7 circle on the canvas | 49.900 | 1.25x |
| 5 | Animate. | 17.960 | A8 Animate button | 51.400 | 1.74x |
| 6 | Element | 19.620 | A9 Element tab in the Animate panel | 55.000 | 1.33x |
| 7 | Preview | 22.640 | A10 Pan style tile | 59.700 | 1.56x |
| 7 | Rise | 26.040 | A11 Rise style tile | 70.200 | 1.26x |
| 8 | choose | 29.720 | A12 Direction down arrow | 82.800 | 1.39x |
| 9 | speed | 32.260 | A13 Fast speed button | 86.000 | 1.26x |
| 10 | Play | 35.460 | A14 Play button | 121.300 | 1.97x |
| 11 | switch | 39.600 | A15 Pan style tile | 136.000 | 1.38x |
| 12 | both | 46.140 | A20 second circle (Shift-click) | 238.600 | 1.01x |
| 12 | Group. | 48.060 | A21 Group button | 241.500 | 1.51x |
| 14 | separate | 52.580 | A16 second circle | 159.200 | 0.93x |
| 14 | each | 53.760 | A17 Animate button | 174.300 | 1.78x |
| 15 | layers | 57.740 | A18 timeline layer bar | 216.200 | 1.36x |
| 16 | first | 61.860 | A19 Play button | 227.900 | 1.99x |
| 19 | ungroup | 73.740 | A22 Ungroup button | 251.600 | 1.20x |
| 20 | Preview | 76.880 | A23 Play button (full preview) | 263.400 | 1.00x +0.8s hold |
| 20 | download | 78.420 | A24 Share button | 269.800 | 1.23x |
| 20 | Video. | 80.080 | A25 Download button (MP4 Video) | 275.500 | 1.51x |
| 21 | GIF | 81.400 | A26 GIF in the file type list | 280.200 | 1.21x |

## Builder decisions

- A3->A4: fast-forwarded src 18.40-19.70 instead of cutting it (shapes panel loading)
- A20: after A15 (until src 138.00) jumps ahead to src 234.00 - narration order
- A16: after A21 (until src 244.50) jumps back to src 158.00 - narration order
- A22: after A19 (until src 233.00) jumps ahead to src 242.50 - narration order

## Judgment calls

- Follow-the-audio reorder: L12 (group) uses footage 234-243; L14-L16 jump back to 158-228; L17-L19 jump forward to 242.5-251.6 (grouped, then Ungroup). Three cross-faded jumps. Continuity oddity: during L16 the circles are separate, and L17 then shows them already grouped.
- Anchors: Open->A1 design click, Elements->A2, "shape"->Shapes category (A3), "circle"->A4, "color"->colour swatch, "canvas"->blue pick (resize/position have no action, see analyze-notes), "Animate"->A8, "Element"->tab, "Preview"/"Rise"->Pan preview / Rise click, "choose"->direction, "speed"->Fast, "Play"->A14, "switch"->Pan, "both"/"Group"->Shift-select + Group, "separate"/"each"/"layers"/"first"->second circle, Animate, timeline bar, Play, "ungroup"->A22, "Preview"/"download"/"Video"/"GIF"->Play, Share, Download, GIF.
- Cuts (all cross-faded): editor loading 11.1-14.3, Elements idle 16.2-17.4, hovering 21.7-34.9, colour browsing 37.8-43.6 and 46-49, idle 53-54.4, extra style previews 61.8-68, idle 73-80.5, repeated speed/timing clicks 88-117, preview/loading 124-133, idle 160.5-173.5, option browsing 177-213.5, scrubbing 218.5-222, idle 253-262.5, preview playback 264.5-269, share-menu/download loading 270.6-273.8 and 276.2-279.3. Most of these are 5-30 s of dead time that cannot be sped up within 2x; the shapes-panel skeleton (18.4-19.7) is fast-forwarded instead.
- Intro: src_start 4.9 so the opening home screen plays at ~1x under the intro line (the cursor is idle there).
- Zooms/ripples: none (recorder zoom baked in). Pace warnings: none left. Remaining warning: A21 result appears 0.3 s after line 12 ends (group button result on screen right after "Group").
