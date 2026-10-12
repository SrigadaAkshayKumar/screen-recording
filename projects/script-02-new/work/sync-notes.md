# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 5 | go | 16.500 | A1 Uploads in side panel | 16.500 | 1.00x |
| 5 | file. | 18.280 | A2 Upload files button | 21.200 | 1.35x |
| 6 | open | 20.060 | A3 Text in side panel | 29.000 | 1.12x |
| 6 | text | 21.360 | A4 Add a heading in Text panel | 32.900 | 1.38x |
| 6 | channel | 22.820 | A5 text box | 50.800 | 1.30x |
| 7 | place | 26.820 | A6 text box | 56.000 | 1.30x |
| 9 | Select | 36.820 | A7 Crack IT text (watermark) | 64.300 | 0.83x |
| 9 | transparency | 37.980 | A8 Transparency button in toolbar | 80.800 | 1.03x |
| 9 | toolbar | 39.000 | A9 Transparency slider | 81.600 | 0.78x |
| 12 | Use | 52.360 | A10 Position button in toolbar | 114.300 | 1.16x |
| 12 | layers | 53.220 | A11 Layers tab | 115.500 | 1.40x |
| 13 | timeline | 56.760 | A12 timeline layer end | 137.000 | 1.07x |
| 13 | add | 59.480 | A13 Add page (+) in timeline | 150.800 | 1.32x |
| 13 | when | 60.320 | A14 Blank | 151.700 | 1.07x |
| 15 | watermark | 64.900 | A15 Text colour button | 166.000 | 1.00x |
| 16 | dark | 70.820 | A17 black swatch under Background colours | 176.500 | 0.79x |
| 17 | Finish | 75.780 | A19 Share button | 206.500 | 0.93x |
| 17 | MP4 | 77.520 | A20 Download in Share panel | 210.200 | 1.32x |
| 18 | file | 79.960 | A22 Download button | 215.300 | 1.52x |
| 18 | remains | 81.460 | A23 timeline playhead / play | 220.400 | 1.20x |

## Builder decisions

- A10: after A9 (until src 95.40) jumps ahead to src 112.60 - narration order

## Judgment calls
- Narration order = recording order: no reordering. No zooms (baked-in recorder zoom), no ripples.
- A2 anchored on "file." and A5 on "channel" (not "add"/"type") so approach speeds stay <= 1.5x; A8/A9 on "transparency"/"toolbar", A10 on "Use" (lead 0.1), A14 on "when", A23 on "remains", A22 on "file": same reason.
- A15 (text colour) is anchored on "watermark" in line 15 rather than on "white": the footage between it and the black background (A17 "dark") cannot be shown in 1.8 s. The colour-picker steps therefore play a few seconds before "white version" is spoken.
- A19/A20: Share on "Finish", Download on "MP4"; file type dropdown (A21) and the timeline stretch (A18), A16 are not narrated, no anchor.
- Cuts (cross-faded): file picker cancel + idle 22.6-28.4, 17.9-20.2, 29.9-32.0, 34.4-50.4 (heading selected, idle), 64.9-80.2, 118.5-136.2, 140-150.2, 155.5-165.2, 170-175.8, 178-203.4, 208.2-209.6, 211.6-213.0, 216-219.3 (download wait). 84.6-95.4 (cursor resting) is played at ~1.1-1.6x and the rest (95.4-112.6) jumped over with prev_until/src_from.
- Not shown: adding a logo (A2 shows only the picker opening); narrated "light and dark parts of footage" is the idle page.
- Remaining warnings: A2 result 0.35 s after line 5; A5 result 0.36 s after line 6; A9 drag result ~0.9 s late (anchored to keep pace). No pace warnings.
