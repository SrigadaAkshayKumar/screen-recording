# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 8.540 | A1 Uploads in the left sidebar | 18.600 | 1.01x |
| 3 | Upload | 10.840 | A2 Upload files button | 32.000 | 0.91x |
| 5 | logo | 22.220 | A4 uploaded logo thumbnail | 41.300 | 0.82x |
| 6 | handle | 25.300 | A5 corner handle of the logo | 45.600 | 1.40x |
| 6 | corner | 27.360 | A8 logo | 89.500 | 1.21x |
| 8 | behind | 34.980 | A6 Uploads in the left sidebar (again) | 78.400 | 1.10x |
| 8 | Layers | 37.740 | A7 chart image in the library | 82.300 | 1.41x |
| 9 | layer | 42.080 | A9 logo (select it) | 99.400 | 1.24x |
| 10 | end | 45.000 | A11 logo layer edge in the timeline | 107.800 | 1.20x |
| 13 | Preview | 63.260 | A12 Play button under the canvas | 164.400 | 1.18x |
| 14 | Share, | 68.800 | A13 Share button | 178.800 | 1.14x |
| 14 | Download | 69.860 | A14 Download in the share menu | 180.200 | 1.32x |
| 14 | Video. | 71.220 | A16 MP4 Video option | 183.600 | 1.18x |

## Builder decisions

- A2: after A1 (until src 19.60) jumps ahead to src 30.90 - narration order
- A8: after A5 (until src 47.40) jumps ahead to src 88.80 - narration order
- A6: after A8 (until src 95.50) jumps back to src 76.00 - narration order
- A9: after A7 (until src 85.30) jumps ahead to src 97.00 - narration order
- A11: after A9 (until src 102.00) jumps ahead to src 106.90 - narration order
- A12: after A11 (until src 127.00) jumps ahead to src 162.00 - narration order
- A13: after A12 (until src 169.50) jumps ahead to src 177.60 - narration order
- A16: after A14 (until src 181.20) jumps ahead to src 183.00 - narration order

## Judgment calls

- Audio order followed. Source jumps (cross-fades, 8 in 74 s): intro idle -> Upload files (11 s of idle at 19.6-30.9 s cannot play at <= 2x in the 2.3 s the narration leaves), resize -> move to corner (45 -> 89 s), corner move -> Uploads reopened (back to 76 s), chart -> logo layer, layer -> second edge drag, edge drag -> Preview (~127 -> 162 s), Preview -> Share, Download -> MP4.
- Everything else plays at 0.82-1.41x; nothing is cut inside a scene, idle stretches just play at about 1x. No `pace:` warnings.
- Anchors: A1 "Uploads", A2 "Upload", A4 "logo" (A3, closing the picker, plays inside the "select your logo / wait for it to appear" stretch), A5 "handle", A8 "corner" (2nd), A6 "behind" + A7 "Layers" (see below), A9 "layer", A11 "end", A12 "Preview", A13 "Share", A14 "Download" (+0.1 lead), A16 "Video" (MP4 selection).
- Line 8 ("select Position, open Layers, move the logo above the video") has no footage. It plays over reopening Uploads and adding the chart as footage, ending with the logo shown above the chart. The words do not match the clicks; the viewer sees the logo above the footage but not the Position/Layers menus.
- Line 9: the logo-layer row appears in the timeline at 99.4 s; the click is anchored on "layer" (42.08 s) rather than "logo" because the footage after it needed more narration time.
- A15 (file type dropdown) is cut by the jump to the MP4 selection (narration says "Download, and MP4 Video" in 2 s); A10 is shown but not tied to a word.
- A8 result (logo in corner) finishes at 28.72 s, 0.6 s after line 6 ends, intentionally: line 7 talks about spacing next to it.
- No zooms (baked-in recorder zoom) and no ripples (coordinates would be wrong in zoomed frames, lessons 2026-10-10 / 2026-10-11).
- Intro starts at src 10.0 s (frozen canvas 10-11.9 s plays under "This tutorial shows you...").
