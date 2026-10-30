# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Search | 5.960 | A1 Create button (homepage) | 11.000 | 0.77x |
| 2 | choose | 8.440 | A2 TikTok Video tile | 19.400 | 1.01x |
| 4 | Upload | 16.020 | A3 Uploads sidebar tab | 34.800 | 1.06x |
| 4 | order | 17.620 | A5 uploaded clip | 39.300 | 1.19x |
| 5 | Trim | 18.920 | A6 clip trim handle | 56.600 | 1.38x |
| 6 | Replace | 25.680 | A8 Add a heading | 97.000 | 1.17x |
| 6 | opening | 28.020 | A9 heading text field | 108.300 | 1.07x |
| 8 | timeline | 36.520 | A10 text bar end handle on timeline | 172.600 | 0.98x |
| 9 | captions | 40.880 | A11 Captions toolbar button | 176.300 | 0.85x |
| 10 | Preview | 45.760 | A13 Play button | 216.800 | 1.15x |
| 11 | include | 49.280 | A14 Add audio | 221.700 | 0.94x |
| 11 | audio | 50.400 | A15 Uploads in audio menu | 223.400 | 1.52x |
| 12 | narration | 57.020 | A16 voice-over.mp3 | 230.500 | 1.07x |
| 15 | edit, | 73.480 | A18 Share button | 309.300 | 0.97x |
| 15 | download | 74.260 | A19 Download in share panel | 314.400 | 1.03x |
| 16 | TikTok | 77.580 | A21 TikTok icon | 326.000 | 1.14x |

## Builder decisions

- A2: after A1 (until src 12.50) jumps ahead to src 18.40 - narration order
- A3: after A2 (until src 26.50) jumps ahead to src 33.90 - narration order
- A5: after A3 (until src 35.80) jumps ahead to src 38.40 - narration order
- A6: after A5 (until src 40.40) jumps ahead to src 55.90 - narration order
- A8: after A6 (until src 59.00) jumps ahead to src 91.50 - narration order
- A9: after A8 (until src 98.50) jumps ahead to src 107.30 - narration order
- A10: after A9 (until src 115.60) jumps ahead to src 171.60 - narration order
- A13: after A11 (until src 189.30) jumps ahead to src 216.00 - narration order
- A14: after A13 (until src 218.00) jumps ahead to src 219.60 - narration order
- A18: after A16 (until src 245.80) jumps ahead to src 308.70 - narration order
- A19: after A18 (until src 309.30) jumps ahead to src 313.60 - narration order
- A21: after A19 (until src 317.20) jumps ahead to src 325.00 - narration order

## Judgment calls
- Recording (334 s) is 4x the voiceover (82 s) with many retakes; every anchor jumps (cross-faded) to a clean take via `src_from`/`prev_until`. Narration order followed.
- Intro (L1) plays 5.6-11.0 (editor before the homepage); the frozen 0-5.6 s is skipped via src_start.
- A4 (Videos tab), A7 (Text tab), A17 (Play click), A20 (file-type dropdown) are not anchored: the narration is too dense (0.1-1 s between steps). A4/A7 are jumped over; A20 plays inside A19's footage; the play click is not shown, the preview is already playing at "Play".
- A18 (Share) result is cut out; the share panel is already open at the next jump (313.6).
- Cut 180.5-188.7: captions progress bar (kept start and end).
- No plan zooms: recorder auto-zoom is baked into the footage. Ripple only on A19 (unzoomed); the rest `no_ripple`.
- L5 "adjust each crop", L13/L14 (TikTok safe zones) have no matching footage; L12-L14 play the voice-over added to the timeline (230-246).
- A9 result (typed text) completes at 35 s of output, after L6: typing plays across L7.
