# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | format | 6.940 | A1 Instagram Reel format | 16.700 | 1.15x |
| 3 | Uploads, | 9.240 | A2 Uploads in the sidebar | 23.400 | 1.09x |
| 3 | Upload | 10.280 | A3 Upload files button | 24.800 | 1.35x |
| 3 | select | 11.620 | A4 Open in the file dialog (select footage) | 26.800 | 1.49x |
| 4 | Drag | 13.100 | A6 first uploaded video | 34.700 | 1.28x |
| 5 | Add | 16.040 | A7 second uploaded video | 46.300 | 1.16x |
| 6 | Select | 19.180 | A8 left edge of the clip | 59.500 | 1.27x |
| 6 | inward | 21.620 | A9 right edge of the clip | 62.700 | 1.31x |
| 7 | playhead | 27.480 | A10 timeline at the section start | 77.600 | 1.01x |
| 8 | Select | 29.760 | A11 clip on the timeline | 88.600 | 1.23x |
| 8 | More | 31.260 | A12 More (...) button | 90.800 | 1.47x |
| 8 | Split. | 32.420 | A13 Split | 94.600 | 1.21x |
| 9 | another | 33.680 | A14 timeline at the section end | 107.700 | 1.43x |
| 9 | section's | 34.640 | A15 Split | 112.600 | 1.46x |
| 9 | delete | 35.760 | A16 Delete (trash) button | 120.600 | 1.43x |
| 10 | Reorder | 38.460 | A17 clip on main track | 132.500 | 1.07x |
| 11 | Preview | 41.820 | A18 Play button | 147.400 | 1.31x |
| 14 | Add | 53.620 | A19 Add audio | 153.300 | 1.22x |
| 14 | voiceover | 55.100 | A20 Uploads in the audio menu | 157.000 | 1.28x |
| 14 | audio | 56.320 | A21 voiceover file | 161.700 | 1.39x |
| 15 | adjust | 58.620 | A22 Volume button | 173.300 | 1.13x |
| 15 | sure | 60.440 | A23 Play button | 184.300 | 1.10x |
| 17 | Add | 66.020 | A24 transition icon between the clips | 219.800 | 0.99x |
| 17 | clips | 67.400 | A25 Dissolve | 221.400 | 1.16x |
| 20 | pencil | 80.180 | A26 Editing (pencil) menu | 266.200 | 0.85x |
| 21 | Preview | 84.940 | A27 Play button | 295.200 | 1.11x |
| 21 | Share, | 87.040 | A28 Share button | 306.500 | 1.33x |
| 21 | Download | 88.120 | A29 Download option | 309.300 | 1.48x |
| 21 | Video. | 89.760 | A30 MP4 Video file type | 311.200 | 1.16x |
| 22 | Play | 90.780 | A31 downloaded file notification | 335.000 | 1.27x |

## Builder decisions

- A2: after A1 (until src 17.30) jumps ahead to src 21.50 - narration order
- A6: after A4 (until src 28.00) jumps ahead to src 34.00 - narration order
- A7: after A6 (until src 37.40) jumps ahead to src 45.60 - narration order
- A8: after A7 (until src 49.80) jumps ahead to src 59.00 - narration order
- A10: after A9 (until src 66.00) jumps ahead to src 75.00 - narration order
- A11: after A10 (until src 79.00) jumps ahead to src 87.20 - narration order
- A13: after A12 (until src 91.50) jumps ahead to src 93.90 - narration order
- A14: after A13 (until src 95.50) jumps ahead to src 106.80 - narration order
- A15: after A14 (until src 108.50) jumps ahead to src 112.00 - narration order
- A16: after A15 (until src 113.40) jumps ahead to src 119.80 - narration order
- A17: after A16 (until src 122.00) jumps ahead to src 131.00 - narration order
- A18: after A17 (until src 136.40) jumps ahead to src 146.90 - narration order
- A19: after A18 (until src 151.50) jumps back to src 143.00 - narration order
- A20: after A19 (until src 154.60) jumps ahead to src 156.40 - narration order
- A21: after A20 (until src 158.00) jumps ahead to src 161.00 - narration order
- A22: after A21 (until src 163.40) jumps ahead to src 172.40 - narration order
- A23: after A22 (until src 174.50) jumps ahead to src 183.50 - narration order
- A24: after A23 (until src 188.00) jumps ahead to src 218.00 - narration order
- A23->A24: fast-forwarded src 187.00-203.00 instead of cutting it (junk: listening to the preview; idle)
- A26: after A25 (until src 228.00) jumps ahead to src 262.00 - narration order
- A25->A26: fast-forwarded src 228.50-265.00 instead of cutting it (junk: idle in the editor)
- A27: after A26 (until src 270.50) jumps ahead to src 294.20 - narration order
- A28: after A27 (until src 297.00) jumps ahead to src 305.50 - narration order
- A29: after A28 (until src 307.50) jumps ahead to src 308.70 - narration order
- A31: after A30 (until src 312.00) jumps ahead to src 334.50 - narration order

## Judgment calls

- No zooms and no ripples: the recording has baked-in recorder auto-zoom (docs/lessons.md, script-18/script-01) and no click log, so ripple positions would be unreliable.
- Narration order = recording order, so each step is a forward jump. Every gap between steps is cut with a cross-fade via `prev_until`/`src_from` (24 jumps) instead of speeding the gap up, because the narration is 3.7x shorter than the recording and actions must stay at 0.75-1.5x. Every segment is 0.85-1.49x; no holds, no `pace:` warnings.
- Anchors: A9 on "inward" (not "right") and A20 on "voiceover", A23 on "sure", A30 on "Video." so clicks sit >= 1 s apart; A5 (Videos tab) is unanchored (never narrated).
- Cut off-topic/junk: leftover finished design (5.2-13.9), mistaken browser context menu (109.8-111.7), Editing-mode menu detour (271-292), post-playback tail.
- Intro line 1 plays src 0-5.2 (the old editor view) because nothing else fits before "Create a video design".
- L12-L13 (Text) and L16 (Crop): not in the recording. L12-13 plays the preview footage again (src 143-153) at 1.2x; L16 plays the listening footage (184-188) and the end-of-clip trim. The video does not show text or crop.
- L18-L19 and L20: no page-thumbnail view exists; L18-19 plays the transition panel and idle footage (221-228) at 0.85x, L20 shows the draw tool / Editing menu.
- Preview of the audio (A23 play) and the exported preview (A27 play) are shown for 1.8-3.7 s only.
- "Result is cut out" warnings (A1, A6, A7, A12, A13, A15, A17, A19, A20, A28, A30, A31) are deliberate: the next step is shown right after the click instead of waiting for the response (loading screens, menus). A21: result 0.3 s after line 14 ends.
