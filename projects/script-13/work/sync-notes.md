# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | select | 5.960 | A1 Welcome text object | 15.500 | 1.01x |
| 3 | Animate | 8.360 | A2 Animate button in toolbar | 24.400 | 1.04x |
| 3 | applied | 10.520 | A3 applied Typewriter animation | 32.000 | 1.30x |
| 4 | Slow, | 16.180 | A4 Slow speed preset | 62.200 | 0.87x |
| 5 | Fast | 21.380 | A6 Fast speed preset | 68.600 | 1.23x |
| 5 | play | 23.300 | A7 Play button | 83.300 | 1.25x |
| 6 | intro | 26.260 | A8 On enter | 96.400 | 1.15x |
| 6 | duration | 27.460 | A9 On exit | 97.550 | 0.96x |
| 7 | duration | 30.260 | A10 On enter | 111.600 | 0.95x |
| 8 | longer | 33.100 | A11 On enter | 113.800 | 0.77x |
| 9 | adjust | 41.020 | A12 Typewriter speed slider | 129.400 | 0.83x |
| 12 | choose | 54.840 | A13 Tectonic effect | 174.300 | 1.15x |
| 14 | Extending | 63.720 | A14 timeline layer end | 194.100 | 0.97x |
| 17 | text, | 75.580 | A15 Welcome text | 211.700 | 0.89x |
| 18 | images, | 79.640 | A16 bird image | 246.200 | 1.23x |
| 19 | Preview | 82.660 | A17 Play button | 260.700 | 1.23x |
| 19 | export | 85.020 | A18 Download in share panel | 264.800 | 1.19x |
| 19 | GIF | 87.240 | A20 GIF option | 274.000 | 1.13x |

## Judgment calls

- **Anchors**: A1 "select", A2 "Animate", A3 "applied", A4 Slow@"Slow", A6 Fast@"Fast", A7 "play", A8 "intro", A9 "duration" (outro is only 0.5 s earlier, anchoring it on "outro" made 1.6x), A10 "duration" (L7), A11 "longer", A12 "adjust", A13 "choose", A14 "Extending", A15 "text", A16 "images", A17 "Preview", A18 "export", A20 "GIF".
- **Unanchored**: A5 Medium (plays between Slow and Fast, L5 says "Choose Slow" while Medium is on screen), A19 file-type dropdown (cut: its click would have needed 2x+; the dropdown is already open on the frame where the cut resumes).
- **No zooms**: the recorder's own auto-zoom is baked in. Ripples only on clicks made while unzoomed (A5, A8, A9).
- **Cuts (all cross-faded)**: 14 spans, listed with reasons in sync.json. Dead time inside a scene could not be fast-forwarded within 2x (the narration is much shorter than the 287 s recording), so it was cut. Only the pieces that fit were kept at 0.77-1.53x.
- Slowest piece 0.77x (L7-L8, A10 -> A11); fastest 1.53x was reduced to 1.13x by merging the MP4 dropdown cut.
- Order conflicts: none, source order follows the narration. Continuity: the first design (typewriter text) is used for L3, the bird image from L4 on, and the text again for L9/L17, as in the recording.
- L10 "Preview ... path": no click anchor; the slider drag's own preview (typewriter replay) plays there.
