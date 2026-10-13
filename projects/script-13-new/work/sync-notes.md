# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads. | 8.660 | A1 Uploads tab in sidebar | 10.450 | 1.09x |
| 3 | file | 10.660 | A2 Upload files button | 13.200 | 1.38x |
| 4 | should | 14.180 | A4 voice-over.mp3 in Uploads > Audio | 21.800 | 1.42x |
| 5 | Audio | 16.720 | A6 Audio category tile in Elements | 50.300 | 1.97x |
| 5 | track, | 18.760 | A7 Way You Make Me Feel track | 55.400 | 1.13x |
| 6 | layering | 22.540 | A8 track in audio list (adds to timeline) | 74.400 | 0.95x |
| 7 | sound | 27.600 | A9 that feeling track in audio list | 84.000 | 1.01x |
| 8 | moment | 29.980 | A10 sound effect clip on timeline | 87.200 | 1.34x |
| 8 | title | 31.800 | A11 Add a heading in Text panel | 123.900 | 1.26x |
| 9 | Listen | 34.540 | A12 Play button under preview | 145.800 | 1.68x |
| 10 | Select | 38.460 | A13 narration audio track in timeline | 182.900 | 1.07x |
| 11 | loud | 46.120 | A14 music track in timeline then volume slider | 192.600 | 1.27x |
| 13 | Trim | 55.320 | A15 clip edge in timeline | 207.200 | 0.90x |
| 14 | place | 60.340 | A16 second clip in timeline | 219.000 | 1.53x |
| 16 | part | 65.920 | A17 clip in timeline | 229.500 | 1.39x |
| 17 | Preview | 71.500 | A18 Play button | 239.700 | 1.09x |
| 17 | covering | 75.700 | A19 Share button / Download | 248.300 | 1.52x |
| 18 | MP4 | 78.100 | A20 MP4 Video file type | 254.000 | 1.54x |

## Builder decisions

- A6: after A4 (until src 25.50) jumps ahead to src 49.00 - narration order
- A8: after A7 (until src 57.80) jumps ahead to src 73.20 - narration order
- A9: after A8 (until src 78.50) jumps ahead to src 83.00 - narration order
- A11: after A10 (until src 88.60) jumps ahead to src 123.00 - narration order
- A12: after A11 (until src 127.50) jumps ahead to src 144.80 - narration order
- A13: after A12 (until src 149.00) jumps ahead to src 181.90 - narration order

## Judgment calls
- Recording has baked-in recorder zoom, so no zooms and no ripples (lessons: double zoom, misplaced ripples). All actions are `no_ripple`.
- Cursor x/y in actions.json are rough estimates (low confidence); harmless since nothing uses them.
- Narration order followed: A6, A8, A9, A11, A12, A13 jump forward with cross-fades (`src_from`/`prev_until`).
- Cuts (cross-faded): upload processing wait 15.4-19.0, audio list browsing 51.8-54.6, idle stills 198.5-204.8, 214.9-219.0, 226.77-229.5, 235.57-239.7, 246.1-248.3, share panel dwell 249.5-251.5. Source 27-46 (adding a video clip, not narrated) and 90-122 (retakes/trim of the second track) are skipped.
- Anchors moved to later words to keep speeds <= 2x: A4 "should", A10 "moment", A14 "loud", A17 "part" (L16, no action there), A19 "covering".
- A3 (Open in dialog) and A5 (positioning drag) are unanchored; they play inside the A2->A4 interval.
- Sound effect (L7) is shown with the "that feeling" track, the only second audio in the recording; the "title appearing" is the Text > heading step (A11).
