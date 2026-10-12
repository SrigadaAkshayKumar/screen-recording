# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | presentation | 6.720 | A1 Landscape video design tile | 22.550 | 1.00x |
| 3 | circle | 10.460 | A2 circle in Elements > Recently used | 48.700 | 1.30x |
| 4 | Duplicate | 13.680 | A3 Duplicate in page right-click menu | 75.000 | 1.15x |
| 4 | circle | 15.440 | A4 circle on page 2 | 86.200 | 1.36x |
| 5 | Duplicate | 18.140 | A5 Duplicate in page 1 menu | 91.300 | 1.44x |
| 5 | place | 20.300 | A6 duplicated page thumbnail | 99.000 | 1.16x |
| 7 | first | 27.640 | A7 junction between pages 1 and 2 | 128.000 | 1.27x |
| 7 | match | 29.240 | A8 Match and move transition | 129.900 | 1.19x |
| 8 | second | 32.660 | A9 junction between pages 2 and 3 | 136.800 | 0.99x |
| 9 | Match | 34.860 | A10 Match and move transition | 139.300 | 1.14x |
| 12 | Preview | 46.300 | A11 Play button in preview | 170.000 | 1.02x |
| 15 | Click | 57.740 | A12 Share button | 202.300 | 1.01x |
| 15 | GIF. | 59.680 | A15 GIF option | 208.300 | 0.98x |
| 16 | download | 62.060 | A16 Download button | 219.200 | 1.05x |
| 16 | browser | 63.660 | A18 downloaded GIF in browser toast | 242.400 | 1.38x |
| 19 | Shorten | 76.120 | A19 page 3 end handle (shorten hold to 0.4 s) | 266.200 | 0.77x |
| 20 | MP4 | 79.600 | A20 File type dropdown | 282.000 | 1.15x |

## Builder decisions

- A2: after A1 (until src 25.50) jumps ahead to src 46.80 - narration order
- A3: after A2 (until src 51.40) jumps ahead to src 74.00 - narration order
- A4: after A3 (until src 76.90) jumps ahead to src 85.70 - narration order
- A5: after A4 (until src 89.50) jumps ahead to src 90.70 - narration order
- A6: after A5 (until src 93.00) jumps ahead to src 98.20 - narration order
- A7: after A6 (until src 107.30) jumps ahead to src 127.00 - narration order
- A9: after A8 (until src 132.40) jumps ahead to src 135.90 - narration order
- A11: after A10 (until src 150.00) jumps ahead to src 169.00 - narration order
- A12: after A11 (until src 180.50) jumps ahead to src 201.20 - narration order
- A15: after A12 (until src 203.40) jumps ahead to src 207.50 - narration order
- A16: after A15 (until src 210.00) jumps ahead to src 218.40 - narration order
- A18: after A16 (until src 220.50) jumps ahead to src 241.50 - narration order
- A19: after A18 (until src 250.30) jumps ahead to src 264.50 - narration order
- A20: after A19 (until src 269.50) jumps ahead to src 281.30 - narration order

## Judgment calls
- Narration order wins: 15 cross-faded jumps (the recording needs ~300 s for an 87 s narration), each landing on the footage of the step being narrated. No zooms (recorder already zooms), no ripples (would land wrong on zoomed frames, see lessons script-18).
- Anchors: A1 "presentation", A2 "circle", A3 "Duplicate", A4 "circle" (drag circle right), A5 "Duplicate", A6 "place" (drag page after page 2), A7 "first"/A8 "match" (first transition), A9 "second"/A10 "Match" (second transition), A11 "Preview" (play), A12 "Click" (Share), A15 "GIF", A16 "download", A18 "browser" (open GIF), A19 "Shorten" and A20 "MP4" from the second take at 250-297 s.
- Not anchored/skipped: A13 Download click and A14 dropdown (L15 says Share, download and GIF in 2 s; showing all would need >2x), A17 download wait (cut), the unnarrated recolour/trim steps.
- Intro starts at src 15.8 (1x) so the first 6.7 s play the Canva home page before the Create dialog; end at src 289 (1x).
- Pace: no `pace:` warnings. All speeds 0.77-1.5x, no holds.
- Remaining warnings: result-after-line for A6, A15, A18, A19 (result appears a second or two after its sentence; harmless) and A13/A14 not anchored (deliberate).
