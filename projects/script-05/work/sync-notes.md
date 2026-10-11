# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | press | 6.020 | A1 Canvas (press L) | 26.800 | 0.96x |
| 3 | Drag | 8.780 | A6 line endpoint | 64.800 | 0.91x |
| 3 | toolbar | 11.140 | A2 line weight button in toolbar | 40.800 | 1.74x |
| 3 | colour | 12.360 | A4 colour button in toolbar | 44.400 | 2.95x |
| 4 | Position | 14.120 | A10 line | 98.500 | 1.76x |
| 5 | Select | 16.200 | A11 the line under the heading | 125.600 | 3.03x |
| 5 | Animate, | 17.740 | A12 Animate button | 126.600 | 1.00x +0.5s hold |
| 7 | Fade | 24.040 | A13 Fade effect tile | 141.000 | 2.29x |
| 8 | wipe | 26.420 | A14 Wipe effect tile | 150.600 | 4.03x |
| 8 | direction | 30.040 | A15 left-to-right direction arrow | 159.400 | 2.43x |
| 9 | replace | 35.980 | A16 Elements tab in sidebar | 174.300 | 2.51x |
| 10 | rectangle | 39.320 | A18 Rectangle shape | 181.200 | 2.07x |
| 10 | narrow | 40.400 | A19 rectangle bottom handle | 195.200 | 2.78x |
| 11 | wipe | 44.680 | A20 Animate button (rectangle) | 219.600 | 0.79x |
| 12 | speed | 47.980 | A21 Slow speed button | 231.200 | 1.24x |
| 12 | preview | 49.460 | A22 Play preview button | 243.200 | 2.03x |
| 15 | different | 59.580 | A24 Animate button (heading) | 273.400 | 2.94x |
| 17 | handwriting | 67.280 | A25 font dropdown | 295.400 | 1.62x |
| 17 | choose | 68.480 | A26 Brittany font | 299.200 | 3.17x |
| 18 | Download | 73.100 | A27 Share button | 343.500 | 0.97x |
| 18 | mp4 | 74.400 | A29 File type dropdown | 347.900 | 3.38x |
| 18 | GIF | 75.880 | A30 GIF option | 351.700 | 2.57x |

## Builder decisions

- intro: cut src 5.00-26.00 - too long to fast-forward at <= 2.00x (junk: opening Canva home and a new design (navigation))
- A6: after A1 (until src 28.50) jumps ahead to src 64.00 - narration order
- A1->A6: fast-forwarded src 27.50-40.00 instead of cutting it (junk: line selected, cursor idle)
- A2: after A6 (until src 68.40) jumps back to src 40.30 - narration order
- A10: after A4 (until src 47.00) jumps ahead to src 97.50 - narration order
- A4->A10: cut src 80.50-98.00 - too long to fast-forward at <= 2.00x (junk: repositioning the line under the heading)
- A11: after A10 (until src 104.50) jumps ahead to src 125.00 - narration order
- A10->A11: cut src 105.00-125.30 - too long to fast-forward at <= 2.00x (junk: idle after placing line)
- A12->A13: fast-forwarded src 132.00-140.00 instead of cutting it (junk: scrolling/hovering the effects panel)
- A13->A14: fast-forwarded src 143.00-150.00 instead of cutting it (junk: hovering effects)
- A15->A16: fast-forwarded src 160.50-174.00 instead of cutting it (junk: settings idle)
- A19: after A18 (until src 183.00) jumps ahead to src 194.00 - narration order
- A20: after A19 (until src 197.80) jumps ahead to src 218.80 - narration order
- A19->A20: fast-forwarded src 199.80-219.00 instead of cutting it (junk: rectangle finishing/colour touch-ups)
- A21: after A20 (until src 222.00) jumps ahead to src 229.50 - narration order
- A20->A21: fast-forwarded src 221.00-231.00 instead of cutting it (junk: panel idle)
- A22: after A21 (until src 233.00) jumps ahead to src 242.00 - narration order
- A24: after A22 (until src 272.60) jumps ahead to src 273.00 - narration order
- A25: after A24 (until src 285.00) jumps ahead to src 294.50 - narration order
- A24->A25: fast-forwarded src 278.00-295.00 instead of cutting it (junk: trying typewriter animation on the heading)
- A27: after A26 (until src 303.00) jumps ahead to src 342.80 - narration order
- A26->A27: fast-forwarded src 301.00-322.00 instead of cutting it (junk: handwriting font applied, idle)

## Judgment calls
- Audio order followed: L3 shows the endpoint drag (A6, recorded at 64 s) first, then weight (A2) and colour (A4) recorded earlier (40-46 s); cross-faded jumps.
- L4 position anchored on the line move (A10); the heading creation (A7-A9, 73-80 s) is not narrated and is skipped (the heading is simply already there).
- L9/L10: Elements (A16) on "replace", rectangle (A18) on "rectangle", resize drag (A19) on "narrow". Shapes click (A17) plays between.
- L11 "same colour": no distinct step in the recording; A20 (wipe on the rectangle) anchored on "wipe". L13 "layer": no footage; the preview wait (A23) plays there at up to 8x.
- L15/17: heading Animate (A24) on "different"; font dropdown (A25) on "handwriting", Brittany (A26) on "choose".
- L18: Share on "Download", file type on "mp4", GIF on "GIF"; Download-in-share click (A28) unanchored.
- In-scene dead time fast-forwarded (ff_max 2x); intro 5-26 s, 80.5-98 s and 105-125 s were too long to fast-forward and were cut by the builder.
- No zooms: the recorder's auto-zoom is baked into the footage. No ripples (wrong place on zoomed frames).
