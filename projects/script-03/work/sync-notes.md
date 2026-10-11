# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | second | 11.840 | A1 page 2 thumbnail (Cognizant) | 24.400 | 2.06x |
| 4 | empty | 13.460 | A2 empty area of page 2 | 27.400 | 1.85x |
| 5 | animate | 19.540 | A3 Animate button in the toolbar | 37.300 | 1.63x |
| 6 | Hover | 22.820 | A4 hover over a page animation tile (Simple) | 48.000 | 1.19x |
| 7 | fade, | 27.700 | A5 Fade animation tile | 61.650 | 2.80x |
| 8 | direction, | 32.080 | A6 On enter button | 76.800 | 3.46x |
| 8 | speed | 32.940 | A7 Speed slider | 77.400 | 1.00x +0.3s hold |
| 9 | apply | 36.760 | A8 Apply to all pages button (hovered, not clicked) | 97.500 | 3.09x |
| 10 | preview | 43.400 | A9 Present button | 119.700 | 3.34x |
| 10 | second | 46.600 | A10 advance to page 2 in presentation | 122.400 | 0.84x |
| 10 | third | 49.500 | A11 advance to page 3 in presentation | 124.000 | 1.00x +1.3s hold |
| 11 | select | 55.560 | A13 the welcome text box | 146.900 | 1.09x |
| 11 | element | 57.340 | A14 Animate button in the text toolbar | 148.900 | 1.12x |
| 11 | text | 58.080 | A15 Typewriter text animation | 149.650 | 1.01x |
| 13 | transition | 65.260 | A18 Add transition button between page 1 and 2 | 178.000 | 1.89x |
| 13 | separate | 66.880 | A19 Stack transition tile | 179.350 | 0.83x |
| 14 | inspect | 71.880 | A20 Line Wipe transition tile | 194.600 | 3.05x |
| 15 | present | 75.560 | A21 Present button | 205.850 | 1.21x |
| 15 | download | 78.360 | A22 Share button, then Download | 219.100 | 1.88x |

## Builder decisions

- intro: fast-forwarded src 2.50-22.50 instead of cutting it (junk: idle cursor and an unnarrated page-1 click before the thumbnail step)
- A2->A3: fast-forwarded src 29.80-36.60 instead of cutting it (junk: cursor idle on the selected page)
- A3->A4: cut src 40.10-46.90 - too long to fast-forward at <= 2.00x (junk: cursor wandering over the panel before the hover preview)
- A4->A5: fast-forwarded src 51.60-54.10 instead of cutting it (junk: idle between hovers)
- A4->A5: fast-forwarded src 56.00-60.10 instead of cutting it (junk: idle between hovers)
- A5->A6: fast-forwarded src 65.30-74.50 instead of cutting it (junk: cursor idle on the panel)
- A7->A8: cut src 88.30-96.60 - too long to fast-forward at <= 2.00x (junk: cursor resting on slider)
- A8->A9: fast-forwarded src 98.10-115.90 instead of cutting it (junk: cursor idle on Remove animations)
- A11->A13: cut src 129.50-145.80 - too long to fast-forward at <= 2.00x (junk: idle then unnarrated navigation to page 1)
- A15->A18: cut src 158.70-168.10 - too long to fast-forward at <= 2.00x (junk: cursor idle on slider)
- A15->A18: cut src 172.00-177.40 - too long to fast-forward at <= 2.00x (junk: zoom and hover before Add transition)
- A19->A20: fast-forwarded src 180.00-190.90 instead of cutting it (junk: cursor resting on Stack tile)
- A20->A21: cut src 198.60-205.40 - too long to fast-forward at <= 2.00x (junk: cursor idle, closing panel)
- A21->A22: cut src 215.40-217.30 - too long to fast-forward at <= 2.00x (junk: idle in editor)

## Judgment calls

- Audio order followed; the recording happens in the same order as the narration, so no out-of-order jumps.
- Anchors: A1 "second" (page-2 thumbnail), A2 "empty", A3 "animate", A4 "Hover", A5 "fade", A6 "direction"/A7 "speed", A8 "apply" (hover on Apply to all pages, never clicked - narration says keep it off), A9 "preview", A10 "second", A11 "third", A13 "select", A14 "element", A15 "text", A18 "transition", A19 "separate", A20 "inspect", A21 "present", A22 "download".
- Unanchored: A12 (page-1 thumbnail), A16 (text speed drag), A17 (page-2 thumbnail), A23 (MP4 file-type click). They are not narrated and play inside their intervals.
- The recording has baked-in recorder auto-zoom (see lessons), so no plan zooms. Ripples only on clicks made while the screen was unzoomed (A5, A6, A15, A19); `no_ripple` on all others.
- In-scene idle time is fast-forwarded (ff_max 2x). Spans that did not fit were cut: 40.1-46.9, 88.3-96.6, 129.5-145.8, 158.7-168.1, 172-177.4, 180-190.9, 198.6-205.4, 215.4-217.3, plus an explicit cut of 208.5-214.6 (presentation mode shortened).
- Approach speeds near 3x remain at A6 (3.5x), A9 (3.3x), A8 (3.1x), A20 (3.0x): idle panel time that did not fit at 2x.
- Tail after 228.6 dropped (recorder zooming and the recorder's stop at 232.5); the last frame is held through the closing line.
