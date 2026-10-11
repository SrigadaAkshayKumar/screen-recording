# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 7.080 | A1 Uploads sidebar tab | 15.400 | 1.53x |
| 2 | Files. | 8.640 | A2 Upload files button | 17.300 | 1.22x |
| 3 | file | 10.220 | A3 yellow tractor SVG file | 18.900 | 1.01x |
| 3 | Open. | 12.440 | A4 Open button | 20.000 | 1.00x +1.1s hold |
| 4 | click | 15.420 | A5 tractor thumbnail | 33.650 | 1.39x |
| 5 | Drag | 18.700 | A6 corner handle | 37.200 | 1.08x |
| 8 | swatch | 36.000 | A7 orange colour swatch in toolbar | 82.850 | 1.25x |
| 16 | Upload | 75.580 | A8 Upload files button (second upload) | 131.700 | 1.23x |
| 16 | copy | 76.380 | A9 SVG file in dialog | 133.100 | 1.75x |
| 16 | before | 77.740 | A10 Open button | 135.400 | 1.69x |
| 17 | resize | 82.420 | A11 corner handle | 148.300 | 0.94x |

## Builder decisions

- intro: fast-forwarded src 7.50-11.80 instead of cutting it (junk: idle cursor before the Uploads step)
- A4->A5: cut src 23.00-32.50 - too long to fast-forward at <= 2.00x (junk: idle while thumbnail sits in panel)
- A7: after A6 (until src 55.00) jumps ahead to src 79.00 - narration order
- A6->A7: fast-forwarded src 41.50-55.00 instead of cutting it (junk: idle after resize)
- A7->A8: fast-forwarded src 116.20-129.00 instead of cutting it (junk: idle cursor after colour edits)
- A10->A11: cut src 137.50-146.00 - too long to fast-forward at <= 2.00x (junk: idle after second upload)

## Judgment calls
- Zooms and ripples are off: the recorder baked auto-zoom into the footage, so the cursor/coordinates move with the camera (lessons: script-1).
- Anchors: A1 "Uploads", A2 "Files", A3 "file", A4 "Open", A5 "click" (thumbnail), A6 "Drag", A7 "swatch". Re-upload (L16): A8 "Upload", A9 "copy", A10 "before"; A11 "resize" (L17).
- A6->A7 follows the audio: after the first resize the plan plays the idle tail (ff), then jumps (cross-fade) to src 79.0 so the toolbar swatch click lands on "swatch". Skipped the unnarrated Edit-image panel exploration (src 55-79).
- 23.0-32.5 (thumbnail idle) and 137.5-146.0 (idle after second upload) cut: too long to fast-forward at <= 2x.
- Tail from 150.6 (Share/Download dialogs, desktop) is dropped, never narrated; output ends on the resized graphic.
- Colour-edit footage (src 83-116) plays under L9-L12 ("not every SVG...") at ~1x; it is not narrated step by step.
- L6, L9-L15 have no matching action.
