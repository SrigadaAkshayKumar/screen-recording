# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | Elements | 9.740 | A1 Elements sidebar button | 16.450 | 0.89x |
| 3 | category, | 11.340 | A2 Audio category tile | 18.850 | 1.50x |
| 4 | Search | 14.520 | A4 Search field (mood) | 31.000 | 1.12x |
| 4 | such | 15.820 | A5 Search field (genre) | 34.300 | 1.23x |
| 5 | three | 21.060 | A6 three-dot info button of a track | 58.900 | 1.45x |
| 10 | playhead | 41.900 | A7 timeline start (playhead) | 95.800 | 0.81x |
| 10 | click | 43.880 | A8 track row | 98.600 | 1.41x |
| 11 | Adjust | 45.620 | A9 end of audio track on timeline | 117.000 | 1.26x |
| 12 | your | 49.400 | A10 volume button | 126.600 | 1.30x |
| 12 | speech. | 50.720 | A11 volume slider | 128.000 | 1.06x |
| 13 | uploads. | 54.060 | A12 Uploads sidebar button | 132.200 | 1.26x |
| 14 | license | 55.900 | A13 Audio tab in Uploads | 157.800 | 1.14x |
| 14 | attribution | 58.340 | A14 Upload files button | 160.600 | 1.15x |
| 15 | part | 60.780 | A15 three-dot info button of Corporate Music | 188.600 | 1.43x |
| 16 | guidance | 68.740 | A16 Commercial use info link | 209.600 | 1.17x |
| 17 | Preview | 75.020 | A19 Share button | 226.000 | 1.11x |
| 17 | download | 76.220 | A20 Download in share menu | 228.300 | 1.50x |
| 17 | video | 77.400 | A21 File type dropdown (MP4 Video) | 230.500 | 1.27x |
| 17 | intended. | 80.100 | A22 Download button | 238.300 | 1.41x |

## Builder decisions

- A2->A4: cut src 20.20-28.80 - too long to fast-forward at <= 2.00x (idle cursor on Audio panel)
- A4->A5: cut src 32.20-33.90 - too long to fast-forward at <= 2.00x (suggestion dropdown idle)
- A5->A6: cut src 40.00-57.00 - too long to fast-forward at <= 2.00x (cursor browsing results)
- A9->A10: fast-forwarded src 125.00-126.00 instead of cutting it (idle between trim and volume)

## Judgment calls
- Recorder auto-zoom is baked into the footage and there is no click log, so **no zooms and no ripples** (every action in `no_ripple`); a plan-added zoom would double-zoom and ripples would land on the wrong spot (docs/lessons.md, script-18).
- Opening: src_start 7.8 (0-7.8 s of the recording is a frozen screen). Ends at src 241.5 (desktop after the recording is cut).
- Anchor words: A1 Elements, A2 category (Audio click), A4 "Search" (typing "mood"), A5 "such" (typing "genre"; the 0.3 s drift is needed to keep <=1.5x), A6 "three" (three-dot), A7 playhead, A8 "click", A9 "Adjust" (trim drag), A10 "your" / A11 "speech" (volume), A12 uploads, A13 license / A14 attribution (Uploads Audio tab / Upload files), A15 "part" (Corporate Music three-dot), A16 "guidance" (licensing dialog), A19 "Preview" (Share), A20 download, A21 "video" (file-type), A22 "intended" (Download button).
- Unanchored: A3 (search field click, right before A4), A17 (close licensing dialog), A18 (Play; the preview is shown before the word "Preview" because there is no room for it after).
- Cuts (all are dead time or off-topic; the builder could not fast-forward them at <= 2x, so they are cross-faded): 20.2-28.8 idle cursor; 32.2-33.9; 40-57 cursor browsing results; 72-92 static popover (cursor only); 99.8-116 and 118.6-123.3 timeline fiddling around the trim drag; 133.5-157 off-topic (a talking-head video is added); 163-187.5 retake of opening the Audio panel; 192.17-203.87 static popover; 211-214 static dialog; 216-220 cursor travel; 222.8-225.2 playback; 227.4-227.9, 229.2-229.9, 233-237 menu/idle moments. 125-126 is fast-forwarded.
- Narration order is the footage order, so there are no out-of-order jumps. The recording shows "Search for a mood" -> "genre" and the 3-dot info popover the same way the script describes.
- Narrated but not shown: "find Audio through Apps" (L3), a real preview of a track (L5).
- Licensing dialog (src 209.6-211 and 214-215) is the "Content ID / account verification" visual: it is the closest footage, not an exact match.
