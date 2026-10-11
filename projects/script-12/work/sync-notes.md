# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Projects | 7.080 | A1 Projects in sidebar | 15.100 | 0.93x |
| 2 | Add | 8.060 | A2 Add new (+) button | 16.650 | 1.58x |
| 2 | Upload | 9.380 | A3 Upload files menu item | 18.300 | 1.25x |
| 3 | PDF | 11.380 | A4 sample-resume PDF in file picker | 24.900 | 3.30x |
| 3 | Open. | 12.260 | A5 Open button | 25.950 | 1.19x |
| 6 | Open | 19.160 | A7 imported sample-resume.pdf design | 33.600 | 1.11x |
| 7 | scroll | 22.960 | A8 document page | 43.300 | 2.55x |
| 9 | text | 29.000 | A9 text area on the page | 53.200 | 1.64x |
| 10 | size | 35.120 | A10 font size control | 72.000 | 3.07x |
| 10 | alignment. | 36.000 | A11 spacing / alignment button | 74.800 | 3.18x |
| 17 | Share | 68.060 | A13 Share button | 213.100 | 1.07x |
| 17 | Download. | 68.720 | A14 Download in Share panel | 214.700 | 2.42x |
| 18 | Choose | 69.920 | A15 File type dropdown | 216.300 | 1.33x |
| 18 | PDF | 72.400 | A16 PDF file type option | 220.200 | 1.57x |
| 19 | Download | 76.920 | A17 Download button | 233.600 | 2.96x |
| 19 | PDF | 79.260 | A18 downloaded sample-resume.pdf in downloads panel | 240.700 | 3.03x |

## Builder decisions

- A3->A4: fast-forwarded src 19.30-24.50 instead of cutting it (junk: browsing file picker)
- A7->A8: fast-forwarded src 37.00-42.80 instead of cutting it (junk: idle on loaded doc)
- A9->A10: fast-forwarded src 54.80-71.00 instead of cutting it (junk: selection idle, cursor wandering)
- A11->A13: fast-forwarded src 80.50-103.00 instead of cutting it (junk: idle on doc)
- A11->A13: fast-forwarded src 209.00-212.70 instead of cutting it (junk: idle on doc before Share)
- A16->A17: fast-forwarded src 221.00-233.30 instead of cutting it (junk: idle on download panel)
- A17->A18: fast-forwarded src 234.50-239.50 instead of cutting it (junk: download in progress)

## Judgment calls
- Follows audio order; recording order already matched narration, so no `src_from`/`prev_until` needed.
- Anchors on the control-naming word (Projects, Add, Upload, PDF/Open, Share, Download). A16 on 2nd "PDF" so the 3.9 s dropdown hover fits at 1.6x.
- No zooms: recorder bakes in auto-zoom (see analyze-notes); ripples only.
- One cut (104-208 s: image insert + ID-card retake, off-topic), cross-faded. All in-scene dead time fast-forwarded (ff_max 3.5; peaks ~3.3x).
- src_start 8.5 (idle homepage before cursor moves); src_end 245.5.
- Unanchored: A6 (wait/upload), A12 (line-spacing drag). Narrated but not shown: drag-onto-homepage (L4), selecting images (L11); L12-16 play over idle doc footage.
- A18 result lands 0.5 s after narration ends (hold on final frame).
