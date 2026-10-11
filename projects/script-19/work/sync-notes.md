# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 6.820 | A1 Untitled Design thumbnail | 12.330 | 1.81x |
| 2 | uploads, | 8.220 | A2 Uploads in the left sidebar | 16.400 | 2.91x |
| 2 | upload | 9.520 | A3 Upload files button | 18.450 | 1.58x |
| 3 | open. | 13.620 | A4 Open button in the file picker | 20.400 | 1.00x +2.2s hold |
| 4 | click | 16.200 | A5 uploaded image thumbnail | 29.650 | 3.59x |
| 5 | Drag | 18.720 | A6 image (move to position) | 34.750 | 2.02x |
| 5 | resize | 19.740 | A7 bottom-right corner handle | 36.950 | 2.16x |
| 6 | use | 24.540 | A8 page colour swatch in the toolbar | 50.200 | 2.76x |
| 6 | background | 25.440 | A9 add a new colour (+) button | 51.900 | 1.89x |
| 7 | colour | 27.740 | A10 colour picker (black) | 53.050 | 1.00x +1.1s hold |
| 9 | but | 36.340 | A12 Upload files button | 89.350 | 4.22x |
| 9 | also | 37.660 | A13 Open button (Transparent vs White Hummingbird PNG) | 91.100 | 1.33x |
| 9 | white | 38.860 | A14 uploaded comparison image thumbnail | 93.000 | 1.58x |
| 12 | remove | 50.460 | A15 BG Remover in the toolbar | 119.650 | 2.30x |
| 14 | Downloading | 61.100 | A17 Share button | 156.950 | 1.00x +3.3s hold |
| 14 | design | 62.100 | A18 Download in the Share panel | 157.850 | 0.90x |
| 15 | enlarging | 67.460 | A16 corner handle (enlarge) | 148.300 | 1.00x +1.9s hold |

## Builder decisions

- A1->A2: fast-forwarded src 12.70-15.70 instead of cutting it (junk: page loading after opening the design)
- A4->A5: fast-forwarded src 22.20-29.30 instead of cutting it (junk: cursor idle while the upload settles)
- A7->A8: fast-forwarded src 38.30-47.80 instead of cutting it (junk: idle on the resized image)
- A10->A12: fast-forwarded src 54.40-84.20 instead of cutting it (junk: idle on the black page)
- A17: after A15 (until src 124.00) jumps ahead to src 154.00 - narration order
- A15->A17: fast-forwarded src 122.80-146.00 instead of cutting it (junk: idle on the cleaned image)
- A16: after A18 (until src 159.30) jumps back to src 146.30 - narration order
