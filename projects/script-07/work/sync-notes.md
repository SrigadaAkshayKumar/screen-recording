# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | video | 6.000 | A1 Landscape Video design size | 17.400 | 1.22x |
| 2 | text | 7.440 | A2 Text tab in the sidebar | 24.700 | 2.22x |
| 3 | Add | 8.620 | A3 Add a heading | 26.300 | 1.36x |
| 3 | box | 10.920 | A6 Add a heading (second text box) | 47.900 | 3.48x |
| 4 | example, | 13.600 | A7 second text box | 50.300 | 0.90x |
| 4 | lines. | 15.020 | A8 Add a subheading (third text box) | 58.000 | 3.24x |
| 5 | font, | 16.620 | A9 third text box | 59.700 | 1.06x |
| 6 | sentences | 21.460 | A10 To Canva text box | 72.500 | 2.64x |
| 7 | Select | 25.340 | A11 To Canva text box | 98.200 | 0.82x |
| 7 | animate. | 27.100 | A12 Animate button | 99.700 | 0.85x |
| 8 | rise | 29.240 | A13 Pan entrance style | 110.200 | 3.41x |
| 9 | style | 32.400 | A14 Easy Editing For All text box | 121.000 | 3.42x |
| 9 | third | 33.560 | A15 Pan entrance style | 123.600 | 2.24x |
| 11 | begin | 40.820 | A16 To Canva timeline bar | 140.400 | 2.31x |
| 12 | Extend | 48.160 | A17 Welcome bar right edge | 145.900 | 1.00x +1.8s hold |
| 13 | Shorten | 54.000 | A18 To Canva bar edge | 152.000 | 1.04x |
| 14 | Play | 58.760 | A19 Play button | 156.800 | 1.01x |
| 20 | Download | 83.000 | A20 Share button | 249.900 | 3.46x |
| 20 | timed | 84.180 | A21 File type dropdown | 253.000 | 2.63x |
| 20 | mp4 | 85.020 | A22 MP4 Video option | 255.000 | 2.38x |

## Builder decisions

- A1->A2: cut src 19.90-24.00 - too long to fast-forward at <= 3.00x (junk: design loads, browsing template panel)
- A3->A6: cut src 26.80-30.40 - too long to fast-forward at <= 3.00x (junk: waiting before typing)
- A3->A6: cut src 37.30-47.30 - too long to fast-forward at <= 3.00x (junk: idle)
- A7->A8: cut src 54.50-57.60 - too long to fast-forward at <= 3.00x (junk: idle)
- A9->A10: fast-forwarded src 67.80-72.00 instead of cutting it (junk: idle / zoom camera moves)
- A10->A11: cut src 75.50-98.00 - too long to fast-forward at <= 3.00x (junk: idle with zoom camera moves)
- A12->A13: cut src 103.00-106.20 - too long to fast-forward at <= 3.00x (junk: browsing animation list)
- A13->A14: fast-forwarded src 113.30-119.50 instead of cutting it (junk: idle)
- A15->A16: fast-forwarded src 126.40-134.90 instead of cutting it (junk: idle)
- A19->A20: fast-forwarded src 174.20-177.70 instead of cutting it (junk: idle during playback)
- A19->A20: fast-forwarded src 185.60-190.80 instead of cutting it (junk: idle during playback)
- A19->A20: fast-forwarded src 198.20-204.80 instead of cutting it (junk: idle during playback)
- A19->A20: fast-forwarded src 214.90-223.20 instead of cutting it (junk: idle)
- A19->A20: cut src 230.67-239.80 - too long to fast-forward at <= 3.00x (junk: idle during playback)

## Judgment calls
- No zooms: the recording already has baked-in recorder zoom (lessons: double-zoom). All ripples disabled (`no_ripple` on A1-A22) because clicks happen during recorder zoom and coordinates are approximate.
- Anchors follow the audio order; the recording order already matches it, so no backward jumps.
- Cut 4.9-15.0 s: idle cursor on the pre-existing design (off-topic). Intro line 1 plays on the first static frames (0-4.8 s).
- In-scene dead time marked `ff` (idle, playback waits, browsing). The builder fast-forwarded those that fit under 3x and cut the rest (19.9-24.0, 26.8-30.4, 37.3-47.3, 54.5-57.6, 75.5-98.0, 103-106.2, 230.7-239.8) because the narration leaves too little time.
- L5 (font/size/alignment) is shown with the typing of the third box and the resize drag; no real font/alignment clicks exist in the footage. A9 anchored on "font" only to give the typing room.
- L3/L4: A6 anchored on "box", A7 "example", A8 "lines" so typing plays at ≤3.5x; A8's result lands just after line 4 ends.
- A4 (type Welcome) and A5 (resize) are unanchored; they play inside the A3->A6 interval.
- Lines 15-19 (slow down, line breaks, separate boxes, appear on click) have no matching actions: they play over timeline playback footage.
- Junk 19.9 start (not 18.0) so the blank design (A1 result at 19.7) stays.
