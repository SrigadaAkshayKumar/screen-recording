# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | social | 6.900 | A1 Elements tab | 46.500 | 0.83x |
| 3 | arrow | 11.580 | A2 arrow in Lines | 55.350 | 1.89x |
| 4 | Place | 13.380 | A3 arrow | 56.600 | 1.00x +0.6s hold |
| 5 | Select | 15.940 | A4 arrow on canvas | 79.150 | 1.15x |
| 5 | Animate | 17.100 | A5 Animate button | 87.000 | 0.99x |
| 5 | Animation. | 19.180 | A6 Create an Animation | 92.100 | 1.01x |
| 6 | Click | 20.500 | A7 arrow | 95.600 | 1.14x |
| 10 | Preview | 35.480 | A8 Play preview | 154.200 | 1.40x |
| 11 | controls | 39.140 | A9 Movement Styles dropdown | 192.800 | 1.48x |
| 11 | recorded | 40.420 | A10 Smooth option | 194.100 | 1.02x |
| 12 | Change | 42.420 | A11 Speed slider | 205.600 | 1.10x |
| 14 | Done | 50.860 | A14 Done / close panel | 264.500 | 0.98x |
| 15 | Delete | 55.460 | A12 Delete path | 226.200 | 1.50x |
| 15 | new | 57.200 | A13 arrow | 229.800 | 1.49x |
| 20 | Play | 75.740 | A15 Play full design | 289.800 | 1.00x |
| 20 | timing | 77.380 | A16 Share button | 304.300 | 1.16x |
| 20 | download | 78.240 | A17 Download in share panel | 306.000 | 1.98x |
| 20 | Video. | 79.840 | A18 MP4 Video | 308.700 | 1.31x |

## Builder decisions

- A14: after A11 (until src 212.00) jumps ahead to src 262.60 - narration order
- A12: after A14 (until src 265.80) jumps back to src 220.60 - narration order
- A15: after A13 (until src 252.00) jumps ahead to src 287.00 - narration order

## Judgment calls
- Recording (315 s) is ~4x the voiceover (80.7 s): intro 0-40.8 s trimmed, 13 cross-faded cuts of idle/unnarrated footage (see sync.json reasons); no held frames.
- Anchors: A1 "social" (Elements click), A2 "arrow", A3 "Place", A4 "Select", A5 "Animate", A6 "Animation", A7 "Click" (drag), A8 "Preview", A9 "controls", A10 "recorded", A11 "Change"(speed slider), A14 Done "Done", A12 Delete path "Delete", A13 redraw "new", A15 "Play", A16 "timing" (Share), A17 "download", A18 "Video" (MP4).
- Order conflicts: Done (src 264.5) is narrated before Delete path (src 226) so the plan jumps ahead then back (xfade). Draw-new-route to Play skips 252-287.
- No zooms (recorder zoom is baked in); ripple only on A4, `no_ripple` elsewhere because of baked-in zoom.
- Orient-to-path toggle is narrated but never enabled in the recording: the toggle is shown while the speed slider plays out.
- Remaining check.py warnings (not fixable): A7, A11, A13 results (drag/slider durations of 2-5 s) appear 0.6-4 s after their lines end; playing them faster would break the 1.5x pace rule. Drag A13 ends in the unnarrated L16-17 area.
- Last Download click (src 310.3) is not shown; video ends on the MP4 selection.
