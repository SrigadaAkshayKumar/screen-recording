# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | animation | 12.060 | A1 Animate button | 38.900 | 1.08x |
| 4 | audio | 16.380 | A2 Audio category | 43.600 | 1.09x |
| 6 | Uploads, | 23.940 | A3 Uploads tab | 61.000 | 1.07x |
| 6 | audio | 25.300 | A4 Audio filter in Uploads | 66.300 | 1.25x |
| 6 | add | 26.380 | A5 uploaded audio file | 68.100 | 1.67x |
| 7 | duration | 29.260 | A6 Duration/timing control | 76.900 | 1.32x |
| 8 | 15 | 33.920 | A7 timing slider | 83.000 | 1.31x |
| 9 | copy | 41.440 | A8 select-all design contents | 111.900 | 1.06x |
| 9 | layout. | 43.740 | A9 new video design | 120.400 | 1.35x |
| 10 | length. | 46.400 | A10 audio clip edge | 150.500 | 0.94x |
| 11 | opening | 47.780 | A11 play button | 156.000 | 1.52x |
| 11 | volume | 49.640 | A12 Volume control | 162.200 | 1.18x |
| 13 | Here's | 57.220 | A13 Share button | 188.900 | 1.02x |
| 13 | printed | 59.960 | A14 Download option | 191.900 | 1.09x |
| 13 | JPG | 62.120 | A15 File type dropdown | 194.900 | 1.39x |
| 14 | MP4 | 67.600 | A16 MP4 Video option | 201.900 | 1.28x |
| 14 | music | 69.500 | A17 Download button | 210.400 | 1.26x |
| 15 | exported | 72.020 | A18 Download button (export toast) | 245.900 | 1.59x |

## Judgment calls
- Every anchor is low confidence (no click log; times estimated from event onsets). Words: A1 "animation", A2 "Audio", A3 "Uploads", A4 "audio", A5 "add", A6 "Duration", A7 "fifteen", A8 "copy", A9 "layout", A10 "length", A11 "opening", A12 "volume", A13 "Here's", A14 "printed", A15 "JPG", A16 "MP4", A17 "music", A18 "exported". Several are later words than the natural one so each interval has enough time to keep 0.75-1.5x pace.
- 16 cross-faded cuts remove idle/un-narrated footage (text editing 17-36 s, idle audio panel, idle timeline, new-design setup 121-149 s, print-promo page 213-245 s). 251 s of footage for 79 s of voiceover left no room for fast-forward alone.
- No zooms and no ripples: the recorder baked auto-zoom into most of the footage (see lessons) so ripples would land off the cursor.
- Narrated but without matching action: "choose a licensed track" (L5), "fade at the end" (L12), "send through messaging app" (L16, shows the download toast).
- Remaining warnings: results of A5-A7, A9, A10 appear slightly after their line ends (0.5-2.8 s; the slider drag to 15 s finishes at 39.8 s though line 8 ends 36.9 s).
