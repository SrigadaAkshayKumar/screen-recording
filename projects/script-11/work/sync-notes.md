# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | box | 7.900 | A1 animated text box | 23.000 | 0.78x |
| 4 | animate | 12.740 | A2 Animate button in toolbar | 28.400 | 1.12x |
| 5 | remove | 16.040 | A3 Remove animation button | 31.700 | 1.00x |
| 6 | stay | 20.560 | A4 panel close X | 41.300 | 0.93x |
| 7 | Preview | 22.640 | A5 Play button | 43.500 | 1.06x |
| 8 | empty | 26.240 | A6 empty area of the page | 56.300 | 1.56x |
| 9 | animate | 28.220 | A7 Animate button in toolbar | 58.600 | 1.16x |
| 10 | text | 32.200 | A9 Animate button in toolbar | 70.900 | 1.31x |
| 11 | remove | 38.300 | A11 Done button | 76.000 | 0.84x |
| 13 | layer | 45.940 | A12 timeline playhead | 100.000 | 0.85x |
| 15 | Extend | 52.260 | A13 text layer end on timeline | 127.000 | 1.44x |
| 16 | turn | 57.500 | A14 Presentation tab | 134.500 | 0.80x |
| 16 | waiting | 61.140 | A15 Present button | 142.900 | 0.85x |
| 20 | Play | 74.740 | A16 Play button | 175.400 | 1.15x |

## Builder decisions

- A5->A6: cut src 47.30-54.50 - too long to fast-forward at <= 2.00x (junk: idle after preview)
- A7->A9: cut src 62.80-69.90 - too long to fast-forward at <= 2.00x (junk: idle with panel closed)
- A12->A13: cut src 102.00-113.00 - too long to fast-forward at <= 2.00x (junk: cursor idles on play button)

## Judgment calls
- Recording order matches the narration order, so no out-of-order jumps. 190 s of footage into 78 s of audio: idle spans were marked junk; the ones that fit at <= 2x were kept sped up, the rest cut (cross-faded): 34.5-39.9, 47.3-54.5, 62.8-69.9, 78-95.5, 102-113, 120.1-127, 130.3-133.6, 136.5-141.8, 150-158.9, 162.3-170.3.
- Trimmed head to 16.8 s and tail at 182.5 s (desktop at the end).
- Anchors: A1 box, A2 animate, A3 remove, A4 stay, A5 Preview, A6 empty, A7 animate, A9 text (L10), A11 remove (L11), A12 layer (L13), A13 Extend, A14 turn, A15 waiting, A16 Play. A8 (close X) and A10 (Create an animation) have no narration word; they play unanchored.
- No zooms, no ripples (baked-in recorder zoom, uncertain coordinates).
- All pace: warnings fixed; only the two "A8/A10 not tied to a word" info warnings remain (intentional).
