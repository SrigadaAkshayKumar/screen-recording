# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | play | 8.780 | A1 Play button | 16.850 | 1.08x |
| 3 | Pause | 10.600 | A2 Pause button | 17.900 | 1.00x +0.8s hold |
| 4 | text, | 13.060 | A3 Text tab in the sidebar | 26.900 | 1.30x |
| 4 | box. | 14.700 | A4 Add a heading | 28.450 | 0.95x |
| 6 | This | 18.080 | A5 caption text box | 40.400 | 1.26x |
| 7 | font, | 24.780 | A11 font menu | 77.700 | 1.33x |
| 7 | size, | 26.020 | A8 text box right handle | 55.300 | 0.97x |
| 8 | text | 30.120 | A6 Text colour button | 49.900 | 1.00x |
| 8 | shadow | 31.240 | A7 white swatch | 51.400 | 1.34x |
| 9 | element | 35.380 | A9 caption element on the timeline | 64.200 | 0.99x |
| 10 | drag | 39.340 | A10 caption element end edge | 71.900 | 0.76x |
| 11 | Add | 43.320 | A12 Text tab in the sidebar (2nd text box) | 129.500 | 0.98x |
| 11 | box | 44.060 | A13 Add a heading (2nd text box) | 130.350 | 1.15x |
| 11 | first | 46.520 | A14 second caption text | 159.300 | 1.00x |
| 12 | caption | 50.060 | A15 second caption element on the timeline | 184.700 | 1.16x |
| 15 | speed | 61.120 | A16 Animate button | 205.800 | 1.34x |
| 17 | Keep | 66.920 | A17 third caption text | 238.900 | 0.90x |
| 19 | sound | 76.720 | A18 Share button | 259.900 | 0.90x |
| 19 | download | 78.680 | A19 Download icon in the share panel | 262.200 | 1.17x |
| 19 | MP4 | 79.720 | A20 File type dropdown | 263.700 | 1.44x |

## Builder decisions

- A11: after A5 (until src 47.60) jumps ahead to src 76.00 - narration order
- A8: after A11 (until src 78.60) jumps back to src 55.00 - narration order
- A6: after A8 (until src 58.90) jumps back to src 49.40 - narration order
- A9: after A7 (until src 53.90) jumps ahead to src 62.60 - narration order
- A12: after A10 (until src 74.60) jumps ahead to src 128.30 - narration order
- A14: after A13 (until src 131.50) jumps ahead to src 158.00 - narration order
- A15: after A14 (until src 165.30) jumps ahead to src 184.20 - narration order
- A16: after A15 (until src 198.50) jumps ahead to src 204.80 - narration order
- A17: after A16 (until src 210.00) jumps ahead to src 237.90 - narration order
- A18: after A17 (until src 255.50) jumps ahead to src 258.90 - narration order

## Judgment calls
- Narration order wins. The recording does size (55 s) before font (77 s) and colour (50 s) later; anchors A11 (font) -> A8 (size/position) -> A6/A7 (colour) are cross-faded jumps (`src_from`/`prev_until`).
- L8 "text background or shadow": the recording never applies one; the text-colour panel (A6/A7, 49.9-52.5) stands in for it.
- L11 "add another text box ... replace its words": A12/A13 (2nd Text tab + Add a heading), then A14 typing of the clean retake (159.3-165.3). The first typing take (150-157, typo "Thatot") is skipped; 160.6-163.0 of the typing is cut (xfade) to keep it at <= 1.3x.
- L12 "Place each caption": drag on the timeline A15 (184.7-190.4), continued to 198.5 over L13/L14 (1.4x).
- L15 animation: Animate panel A16 (205.8-210). L16-L18: third caption typing A17 (238.9-243.7) and timeline, cut 244.5-253.3 (cursor-only).
- L19: preview playback (253.3-255.5), Share (A18), Download (A19), file type (A20). The final Download click (266.5) is not shown (no time left).
- No zooms and no ripples anywhere: the recorder baked its auto-zoom into the footage (lessons: script-1, script-18), and click x/y read from zoomed tiles are only approximate.
- Cuts: 20.0-25.8 (paused idle), 29.6-37.3 (idle after adding heading), 65.7-70.4 (frozen timeline), 160.6-163.0, 244.5-253.3. Junk 100.4-117.0 (idle Effects) is never reached by the plan.
- Start trimmed to src 7.4 (0-7.4 is a still design with only cursor twitching).
- Warnings left (result after the line ends): A8, A14, A15, A17 - the drag/typing footage is longer than its line and runs into the next line; no pace: warnings.
