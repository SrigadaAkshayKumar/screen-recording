# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Create | 5.740 | A1 Create button (left sidebar of Canva home) | 17.500 | 0.92x |
| 3 | Open | 8.740 | A2 Instagram Reel / portrait video tile | 24.700 | 0.87x |
| 5 | Go | 19.780 | A3 Uploads tab in left sidebar | 38.800 | 0.95x |
| 5 | design. | 23.560 | A5 first uploaded clip dragged to the timeline | 50.600 | 1.24x |
| 6 | order | 26.120 | A6 second clip dragged to end of timeline | 58.400 | 1.29x |
| 7 | decide | 29.060 | A7 landscape clip (man) in Uploads | 86.600 | 1.36x |
| 9 | Double | 37.680 | A8 double-click on the video | 116.700 | 0.96x |
| 10 | add | 43.740 | A9 Text tab in left sidebar | 137.900 | 1.06x |
| 10 | graphics. | 44.640 | A10 Add a heading | 139.100 | 1.33x |
| 14 | Play | 67.980 | A11 Play button | 205.800 | 0.99x |
| 15 | crop | 70.640 | A12 double-click on the video again | 216.900 | 1.32x |
| 16 | Share, | 73.320 | A13 Share button (top right) | 228.000 | 1.46x |
| 16 | Download | 74.460 | A14 Download option in Share panel | 230.800 | 1.40x |
| 16 | Video. | 75.900 | A15 File type dropdown (MP4 Video) | 232.900 | 1.46x |
| 17 | quality | 77.600 | A16 1080p quality option | 237.800 | 1.24x |
| 17 | finished | 79.060 | A17 Download button | 245.900 | 0.75x |

## Builder decisions

- A7: after A6 (until src 61.40) jumps ahead to src 85.60 - narration order
- A11: after A10 (until src 169.00) jumps ahead to src 204.80 - narration order
- A12: after A11 (until src 207.80) jumps ahead to src 215.40 - narration order

## Judgment calls
- No zooms, no ripples: the recorder baked auto-zoom into the footage (docs/lessons.md), so click coordinates are rough and plan zooms would double-zoom.
- Anchors sit on the control's word, except: A3 "Go" (Uploads is 0.3 s later) and A5 "design" to give the upload/add steps enough footage; A7 "decide" and A15 "Video" and A17 "finished" to keep approach speeds <= 1.5x.
- Narration order followed: A7 (landscape clip, src 86.6), A11 (play, src 205.8), A12 (crop again, src 216.9) jump ahead in the recording, cross-faded.
- Cuts (cross-faded): Create dialog idle, file picker/upload progress, Videos tab browsing, clip browsing, clip loading/scrubbing 93-114.8, scrubbing 122-137, still heading 141.7-145, still 155.4-159.8, idle after crop, share panel loading, dropdown idle, other quality options 238.4-245.4. Still spans were cut rather than fast-forwarded (ff would have exceeded 2x).
- Unmentioned in the recording: no "search Mobile Video" (A2 picks the Instagram Reel tile); "Trim unnecessary footage" has no clear action (scrubbing 129-136 cut); lines 12-13 (resolution talk) play over text editing footage.
- A4 (Upload files) is unanchored; its footage is mostly cut. A17 result (download toast, src 248.0) is just past src_end.
- The 1080p click (A16) is followed by a cut to a frame where 4K is selected (the recording tried other options).
