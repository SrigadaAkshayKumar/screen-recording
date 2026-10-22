# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | segment | 10.720 | A1 Welcome caption segment on timeline | 16.400 | 0.82x |
| 3 | Captions | 13.780 | A2 Captions button in toolbar | 25.400 | 1.05x |
| 4 | Styles | 16.780 | A3 Styles tab | 29.950 | 1.52x |
| 7 | Select | 27.300 | A4 Momentum style pack tile | 87.000 | 1.18x |
| 9 | beginning, | 35.300 | A5 playhead on timeline | 117.500 | 1.05x |
| 13 | Review | 52.220 | A6 Captions button in toolbar | 139.000 | 1.15x |
| 14 | generated | 59.420 | A7 Transcript tab | 167.900 | 0.90x |
| 16 | individual | 72.000 | A8 Animate button in toolbar | 185.400 | 1.39x |
| 17 | Download | 75.180 | A9 Download in Share panel | 194.600 | 1.35x |
| 17 | video | 76.560 | A10 MP4 Video file type | 196.500 | 1.38x |

## Builder decisions

- A4: after A3 (until src 45.40) jumps ahead to src 86.60 - narration order

## Judgment calls
- Two takes in the recording; take 1 (0-31 s, 35-45 s) used for the intro, caption select (A1), Captions (A2), Styles tab (A3) and style browsing; take 2 from the Momentum tile click (A4, 87 s) on, because take 1 never applied a style.
- A4 jumps to src 86.6 (xfade); the 21 s spinner on the tile (87.9-110.0) is cut as a loading screen, so the applied style appears on "Canva applies...".
- Play button click (~115.8 s) not used; A5 (playhead scrub 117.5-135.5) carries "play the beginning, middle and end" and "check a short and a longer caption". A5 word = "beginning".
- A6 "Review", A7 "generated", A8 "individual" (later word so the 185-194 footage plays at 1.4x), A9 "Download", A10 "video".
- Cuts: idle stills 31.8-35.3, 124.3-126.3, 142.4-146.4, idle styles panel 149-167.4, animate hover 188-192.9. src_end 200 (the rest is the tray popup).
- No zooms (recorder auto-zoom baked in); ripple only on A4 (unzoomed), none on zoomed clicks.
- Lines 11-15 (tips) have no on-screen action; they play over scrub / styles panel / transcript footage.
