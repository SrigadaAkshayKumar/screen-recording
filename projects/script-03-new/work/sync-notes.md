# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 4 | Upload | 17.020 | A1 Import button | 37.700 | 1.32x |
| 4 | clip | 17.820 | A2 Open button in file dialog | 41.800 | 1.12x |
| 4 | add | 19.020 | A3 add clip to timeline | 43.400 | 1.33x |
| 5 | Effects, | 20.880 | A4 Effects tab | 45.600 | 1.18x |
| 5 | Video | 22.000 | A5 Video effects | 99.800 | 1.52x |
| 6 | Apply | 24.560 | A6 Blur effect | 104.200 | 1.72x |
| 6 | adjust | 27.140 | A8 Blur strength slider | 114.000 | 0.97x |
| 7 | Extend | 31.020 | A7 effect strip end | 111.600 | 1.42x |
| 8 | Play | 34.480 | A9 play button | 131.000 | 1.21x |
| 9 | Export | 40.020 | A10 Export button | 148.900 | 0.99x |
| 10 | in | 46.460 | A11 Export button in dialog | 171.400 | 1.41x |
| 11 | Return | 47.580 | A12 Uploads in sidebar | 183.500 | 1.70x |
| 11 | upload | 49.800 | A14 Open button in file dialog | 197.800 | 1.31x |
| 12 | Add | 51.700 | A15 uploaded video | 206.500 | 1.16x |
| 12 | adjust | 53.560 | A16 Position button | 218.200 | 1.51x |
| 12 | duration. | 55.460 | A17 duration handle | 240.500 | 1.21x |
| 13 | text, | 57.820 | A18 Text tab | 245.000 | 1.25x |
| 13 | logo | 59.580 | A20 text on the video | 258.900 | 1.42x |
| 14 | transparency | 65.080 | A21 Transparency | 285.400 | 1.11x |
| 16 | Preview | 73.420 | A22 video in the design (preview) | 211.000 | 0.90x |

## Builder decisions

- A8: after A6 (until src 106.00) jumps ahead to src 113.30 - narration order
- A7: after A8 (until src 118.50) jumps back to src 110.60 - narration order
- A9: after A7 (until src 115.00) jumps ahead to src 130.20 - narration order
- A10: after A9 (until src 136.00) jumps ahead to src 148.40 - narration order
- A16: after A15 (until src 208.50) jumps ahead to src 217.40 - narration order
- A17: after A16 (until src 220.00) jumps ahead to src 240.00 - narration order
- A21: after A20 (until src 263.30) jumps ahead to src 283.40 - narration order
- A22: after A21 (until src 287.40) jumps back to src 205.50 - narration order

## Judgment calls

- Recording (287 s) is ~3.7x the voiceover (78 s): the CapCut effects-panel loading (46.4-98.9), dialog browsing, export settings, upload waits and unnarrated text styling are cut with cross-fades; everything else plays at 0.85-1.5x. No pace warnings remain.
- Recording has baked-in recorder zoom in places, so no zooms and no ripples (all clicks `no_ripple`).
- Intro (L1-3, 0-17 s) has no actions: plays Canva footage 0-4.2 and 10.3-24.5 (the Canva Edit/Adjust/Filters panels, matching "Canva's regular photo Blur tool"); frozen 4.2-10.3, the Canva video play test 24.5-30.2 and CapCut idle 32.3-35.75 are junk/cut.
- Order conflicts (narration wins): adjust strength (A8, 114 s) is shown before extending the strip (A7, 111.6 s); play check (A9) and export (A10) jump forward; position/duration (A16/A17) and text (A18/A20) are jumped to, skipping idle time; the transparency step (A21) is at the end of the recording and used on L14.
- A22 is a made-up anchor: the recording ends on the transparency slider and has no preview/download step, so L15-16 reuse Canva footage of the blurred video in the design (205.5-214.8) as its closest picture. Narrated "download as MP4" is not in the recording.
- A9 (play check, ~131 s) is low confidence: the preview shows the blurred clip at 131-138 s, the click itself was not seen. A11/A12/A16/A7/A21 times are also approximate (low confidence).
- A13 (Upload files click) is not anchored: it plays inside the A12->A14 interval. A19 (add heading) was left out; unnarrated.
- Unfixable/accepted: A11 and A12 results are cut out (export finishing, uploads panel loading), so the viewer sees the next step directly after a cross-fade.
