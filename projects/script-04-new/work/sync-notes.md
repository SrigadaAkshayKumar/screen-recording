# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | apps | 8.460 | A1 Apps in the left sidebar | 15.400 | 1.22x |
| 4 | check | 17.860 | A2 Face Blur in Video app | 29.700 | 0.88x |
| 6 | Upload | 25.060 | A3 Choose file button | 41.600 | 0.78x |
| 6 | strength. | 28.940 | A5 Intensity slider | 58.267 | 1.44x |
| 7 | use. | 32.960 | A6 Gaussian blur style | 71.200 | 1.33x |
| 8 | Blurring | 34.500 | A7 Process your video button | 79.500 | 0.91x |

## Judgment calls
- Narration lines 9-16 (add to design, check faces, tracking caveat, website fallback, export) have no footage: the recording ends while face detection is still running. Lines 8-16 (34.5-84.3 s) play the processing screen. Real progress-bar footage with the recorder's own zoom pops (112-130, 137-160, 163-171) is used; the static stretches (81.2-112.1, 129.9-137.3, 160.1-163.2) are cut with cross-fades. No stretch over 2.5 s without movement remains.
- Anchors: A1 "apps"; A2 (Face Blur app click) on "check" (17.9 s) instead of "Open the Face Blur integration" (13.7 s): the panel is idle for 8 s after it opens and A2 earlier would need long stills; A3 Choose file on "Upload"; A5 slider drag on "strength"; A6 style click on "use" (the narration says "select the one you want to use" ~1 s earlier); A7 Process click on "Blurring" (0.5 s after "Run"), because footage between actions is dead and cannot be played faster than 1.5x.
- Narration is faster than the footage for upload -> strength -> style -> run (9 s of narration, ~25 s of footage), so idle spans between actions are cut with cross-fades (47.2-58.3, 62.8-70.4, 72-78.9) rather than fast-forwarded (>2x needed). Result: 7 cross-fade cuts in 84 s.
- A4 (Open in file dialog) has no anchor; it plays at ~1.4x within the A3->A5 interval.
- No zooms and no ripples: the recorder baked its own zoom into the footage (see lessons 2026-10-10 / 2026-10-11).
- A5's click time was moved to 58.27 (end of a still span where only the cursor rests on the slider) so the builder does not treat the approach as a still at 8x.
