# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | template | 9.080 | A1 Video category on the Canva home screen | 12.550 | 0.79x |
| 2 | design. | 10.520 | A2 Instagram Reel tile | 14.300 | 1.22x |
| 4 | uploads | 19.260 | A3 Uploads tab in the left rail | 31.100 | 1.35x |
| 4 | library. | 20.760 | A4 Videos tab in Uploads | 34.800 | 1.13x |
| 5 | slow | 22.080 | A5 background video thumbnail | 36.100 | 0.98x |
| 6 | length | 26.480 | A6 end of the video clip in the timeline | 62.000 | 1.11x |
| 7 | text, | 30.160 | A7 Text tab in the left rail | 73.500 | 1.44x |
| 7 | text | 31.300 | A8 Add a heading | 74.750 | 1.10x |
| 7 | quote. | 32.680 | A9 text box | 77.900 | 1.05x |
| 9 | Add | 36.760 | A11 Add a subheading | 108.000 | 0.98x |
| 9 | crediting | 38.460 | A12 subheading box | 111.100 | 0.94x |
| 10 | shape | 43.400 | A15 square shape | 131.900 | 1.38x |
| 10 | reduce | 44.700 | A17 Transparency button | 172.000 | 1.15x |
| 10 | opacity. | 45.600 | A18 transparency slider | 172.600 | 1.00x +0.3s hold |
| 11 | add | 47.880 | A20 Animate | 215.000 | 1.18x |
| 11 | enter | 49.880 | A21 Typewriter animation | 217.300 | 1.15x |
| 12 | Set | 51.120 | A19 text clip end in the timeline | 190.200 | 1.13x |
| 14 | becomes | 66.620 | A22 Play | 227.100 | 0.95x |
| 16 | phone | 72.140 | A23 Share | 231.500 | 0.80x |
| 16 | MP4 | 73.840 | A24 Download | 232.800 | 0.76x |

## Builder decisions

- A20: after A18 (until src 179.70) jumps ahead to src 214.40 - narration order
- A19: after A21 (until src 218.40) jumps back to src 189.90 - narration order
- A22: after A19 (until src 202.80) jumps ahead to src 224.90 - narration order

## Judgment calls
- Footage is 247 s for 77 s of narration: 17 plain cross-faded cuts of idle/loading/scrubbing/typing-middle spans were unavoidable (see sync.json `cuts`); everything kept plays at 0.75-1.7x.
- Anchors: A1 "template", A2 "design", A3 "uploads", A4 "library", A5 "slow", A6 "length", A7/A8 "text", A9 "quote", A11 "Add", A12 "crediting", A15 "shape", A17 "reduce", A18 "opacity", A20 "add", A21 "enter", A19 "Set", A22 "becomes", A23 "phone", A24 "MP4".
- Order conflict: the recording sets the text duration (190-203 s) before the animation (215-218 s); the narration says animation first, so the plan follows the audio with cross-faded jumps (A20 jumps ahead, A19 back, A22 ahead).
- No zooms/ripples: recorder baked-in zoom (lessons 2026-10-10, 2026-10-11) and no click log.
- Not anchored (unnarrated or no spare time): A10 resize, A13 move author, A14 Elements tab, A16 resize shape; shape layering/colour (143-171 s) cut. Music (L13) has no footage: the timeline footage plays under it.
- A22/A23: Share is on "phone" and Download on "MP4", the nearest words with enough time for the footage; the Preview step itself is the playback at A22.
