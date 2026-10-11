# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | uploads, | 9.560 | A1 Uploads sidebar tab | 16.000 | 1.67x |
| 5 | Add | 20.160 | A2 logo thumbnail in Uploads | 22.000 | 1.00x +4.6s hold |
| 7 | animate. | 29.020 | A3 Animate button in the toolbar | 90.800 | 2.80x |
| 8 | fade | 31.940 | A4 first featured entrance effect | 94.600 | 1.30x |
| 9 | Preview | 36.720 | A5 effect tiles (hover preview) | 98.500 | 0.82x |
| 10 | speed | 39.960 | A6 Speed option (Fast/Medium) | 139.300 | 1.48x |
| 12 | group | 51.860 | A7 Group button on the selection | 184.300 | 3.78x |
| 13 | Keep | 53.680 | A8 Ungroup button | 195.100 | 2.51x |
| 13 | symbol | 56.040 | A9 entrance effect for the symbol | 204.000 | 3.77x |
| 13 | brand | 57.860 | A10 Tech AI text (brand name) | 226.000 | 2.20x |
| 14 | timeline | 60.220 | A11 logo bar on the timeline | 247.900 | 1.65x |
| 15 | tagline | 63.620 | A12 tagline text box | 271.000 | 2.68x |
| 20 | Download | 82.520 | A13 Share button | 315.000 | 2.33x |
| 20 | check | 85.340 | A14 Download button | 323.900 | 3.16x |

## Builder decisions

- A6->A7: fast-forwarded src 160.00-167.00 instead of cutting it (browsing)
- A7->A8: auto-cut still span src 188.13-194.37 with a cross-fade

## Judgment calls
- No zooms/ripples: the recorder's baked-in auto-zoom (lessons 2026-10-10, 2026-10-11) makes recording-pixel ripples unreliable; every action is in `no_ripple`.
- Anchors follow the audio order. Cuts (all cross-faded): 38-82 s idle page/logo clicking (no background colour change exists), 101-137 effect hovering, 207-225 and 228-246 other effect browsing, 252-266 timeline fiddling. 160-167 fast-forwarded instead of cut.
- A12 (tagline typing) result appears ~0.5 s after line 15 ends (builder warning); accepted.
- Narration L6 (background colour) and L16-19 have no matching action; L16-19 play over fast-forwarded tagline/idle footage (~2-3x).
- Intro/L2: the first 16 s of source play at ~1.7x under L1-L3; no "upload files"/file dialog was visible.
