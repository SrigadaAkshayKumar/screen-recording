# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | presentation | 8.000 | A1 Presentations in Create a design | 16.200 | 2.02x |
| 3 | Upload | 10.660 | A2 Uploads in left sidebar | 24.300 | 0.86x |
| 3 | place | 11.920 | A3 uploaded photo | 26.800 | 1.98x |
| 4 | larger | 14.720 | A4 centre photo resize handle | 37.000 | 3.64x |
| 5 | Duplicate | 17.880 | A5 Duplicate page in page menu | 59.000 | 2.09x |
| 6 | positions | 22.420 | A6 existing photo on page 2 | 66.500 | 1.65x |
| 7 | Resize | 26.440 | A7 photo corner handle | 74.000 | 1.87x |
| 8 | Duplicate | 29.960 | A8 Duplicate page | 79.600 | 1.59x |
| 9 | Move | 34.160 | A9 existing photo on page 3 | 84.000 | 1.05x |
| 10 | Add | 40.840 | A10 Add transition (+) between pages | 107.000 | 1.44x |
| 10 | Match | 42.400 | A11 Match & Move in Transitions panel | 109.000 | 1.28x |
| 12 | second | 49.760 | A12 transition between pages 2 and 3 | 115.400 | 0.87x |
| 13 | sequence. | 54.000 | A13 Duration slider | 134.500 | 2.98x |
| 17 | PNG | 68.700 | A14 PNG in file type list | 179.600 | 2.39x |
| 19 | Share, | 82.980 | A15 file type dropdown | 197.200 | 1.23x |
| 19 | MP4 | 84.780 | A16 MP4 Video in list | 201.000 | 2.11x |
| 19 | pages. | 87.220 | A17 Download button | 210.000 | 3.69x |
| 20 | Play | 88.300 | A18 downloaded mp4 in browser downloads list | 223.500 | 3.80x |

## Builder decisions

- intro: fast-forwarded src 4.67-11.13 instead of cutting it (junk: idle opening)
- A1->A2: cut src 17.40-23.20 - too long to fast-forward at <= 2.00x (junk: editor loading)
- A4->A5: cut src 40.60-56.00 - too long to fast-forward at <= 2.00x (junk: fine alignment of photos)
- A9->A10: cut src 90.60-104.00 - too long to fast-forward at <= 2.00x (junk: idle page 3)
- A12->A13: cut src 118.87-125.33 - too long to fast-forward at <= 2.00x (junk: idle)
- A13->A14: fast-forwarded src 163.37-170.27 instead of cutting it (junk: idle)
- A13->A14: cut src 140.67-150.60 - too long to fast-forward at <= 2.00x (junk: idle)
- A14->A15: fast-forwarded src 181.93-192.63 instead of cutting it (junk: idle in download panel)
- A14->A15: fast-forwarded src 193.67-195.97 instead of cutting it (junk: idle)
- A17->A18: cut src 212.50-221.90 - too long to fast-forward at <= 2.00x (junk: download progress)

## Judgment calls
- No zooms and no ripples (all `no_ripple`): the recorder's auto-zoom is baked into the footage (lessons: script-1, script-18), and there is no click log, so click positions are rough.
- Anchors follow the narration order; the recording is already in that order, so there are no reorders.
- A13 (duration slider) is anchored on "sequence." instead of "duration" so the 19 s of source before it fits in under 4x; the slider result lands about 1 s after line 13 ends (builder warning).
- A15 (file type dropdown) on "Share,", A17 (Download click) on "pages.", A18 (open the export) on "Play": the recording takes its time between them, so these are the closest words that fit.
- Junk spans marked `ff` were fast-forwarded where they fit within 2x. The rest were cut: editor loading (17.4-23.2), fine alignment (40.6-56), idle on page 3 (90.6-104), idle (118.9-125.3 and 140.7-150.6), download progress (212.5-221.9). The desktop at 238-242.3 is cut.
- Narrated but not shown as a distinct action: crown/premium indicator (L11), shortening or lengthening page holds (L14), "separate videos" export (L18, shown only as the Share/Download dialog). The footage plays at whatever speed fits.
- The second transition (A12) and the page-3 drags (A6, A7, A9) have low-confidence times.
