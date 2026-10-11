# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | Add | 11.960 | A1 Upload item in the create menu | 22.400 | 1.00x +7.2s hold |
| 3 | Upload | 13.440 | A2 Upload files button | 23.850 | 0.98x |
| 4 | PDF | 15.360 | A3 Open button of the file picker | 26.500 | 1.38x |
| 5 | Open | 18.200 | A5 uploaded file in the toast | 34.550 | 2.83x |
| 6 | logos, | 23.200 | A6 chart legend | 51.100 | 3.31x |
| 9 | enlarging | 32.780 | A13 small image on the page (resize handle) | 214.000 | 2.39x |
| 10 | Share, | 40.220 | A7 Share button | 113.100 | 1.22x |
| 10 | Print. | 42.360 | A9 File type dropdown (PDF) | 119.200 | 2.85x |
| 13 | Download | 52.800 | A10 Download button | 121.800 | 1.00x +7.8s hold |
| 13 | viewer. | 56.880 | A12 downloaded PDF in the downloads list | 137.500 | 3.12x |
| 17 | export. | 81.500 | A14 Download button (test export) | 232.900 | 1.56x |

## Builder decisions

- A13: after A6 (until src 71.00) jumps ahead to src 211.00 - narration order
- A6->A13: fast-forwarded src 61.00-68.23 instead of cutting it (junk: idle on the design)
- A7: after A13 (until src 218.00) jumps back to src 108.00 - narration order
- A10->A12: cut src 133.10-136.07 - too long to fast-forward at <= 2.00x (junk: idle after export)
- A14: after A12 (until src 165.00) jumps ahead to src 222.00 - narration order
- A12->A14: fast-forwarded src 151.07-158.70 instead of cutting it (junk: idle on the design while the viewer is in another tab)
- A12->A14: fast-forwarded src 164.43-168.33 instead of cutting it (junk: idle in the viewer)

## Judgment calls

- Follow the audio: lines 1-2 play over the Canva home (src 17.7+, held); the "Projects / Add New" words are shown by A1 (Upload item) since the recording has no Projects step; A2 "Upload", A3 "PDF" (file picked + Open).
- Wait for import (A4, 27.5-34.5 s) is fast-forwarded (wait action, up to 8x), not cut.
- No zooms: the recorder baked in auto-zoom/pan (see lessons). Ripples only.
- A6 (chart legend click) on "logos" for the zoom-in-on-details narration; lines 7-8 play on from the design (src to 71 s, with idle 61-68 s fast-forwarded).
- Reorder: line 9 "enlarging" shows A13 (src 214, image enlarged) with a cross-fade; then back to the Share/Download steps (src 108+). Line 17 "export" shows the test export A14 (src 232.9) after the PDF-viewer footage (src to 165). "place it on a matching page" has no separate action (the image was placed before the recording of A13's source span; those frames are shown with A13's lead-in, src_from 211).
- A7 "Share" and A9 on "Print" (the Print preset is never clicked; the PDF file-type dropdown lands there). A8 (Download in share panel) is unanchored: 0.7 s between "Share" and "Download" words is too short. Its ripple still plays.
- Cuts (off-topic): script doc 0-17.7, unnarrated chart edits 195-211, desktop at the end. Idle spans 61-68, 76.8-79.5 (n/a if unused), 151-158.7, 164-168 are fast-forwarded. 133.1-136.07 idle after export could not be fast-forwarded within 2x and is cut.
- A12 result (viewer open) lands at 57.5 s, 0.3 s after line 13 ends; acceptable.
