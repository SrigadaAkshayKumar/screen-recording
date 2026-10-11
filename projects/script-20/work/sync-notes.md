# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | heading | 6.600 | A1 Welcome heading | 12.000 | 1.82x |
| 2 | animate | 8.580 | A2 Animate button in toolbar | 20.500 | 4.29x |
| 3 | rise | 14.580 | A3 Rise style | 37.400 | 2.82x |
| 4 | photo | 21.860 | A4 photo | 53.500 | 2.21x |
| 4 | animate | 23.640 | A5 Animate button (image toolbar) | 56.600 | 1.74x |
| 4 | element. | 26.060 | A6 Whip Slide animation | 73.100 | 2.48x |
| 9 | Preview | 50.640 | A7 Play preview | 134.600 | 2.50x |
| 14 | remove | 72.960 | A8 Remove animation button | 196.900 | 2.79x |
| 15 | share, | 77.040 | A9 Share button | 202.200 | 1.30x |
| 15 | download | 77.820 | A10 Download in share panel | 203.900 | 2.18x |
| 15 | video. | 79.280 | A11 File type dropdown | 207.300 | 2.33x |
| 16 | GIF | 80.600 | A12 GIF option | 214.300 | 1.36x |
| 17 | PNG | 83.300 | A14 PNG option | 222.200 | 2.93x |
| 17 | JPG | 84.140 | A13 JPG option | 220.700 | 3.45x |
| 18 | export. | 89.560 | A15 Download button | 231.800 | 2.05x |

## Builder decisions

- intro: fast-forwarded src 0.00-11.00 instead of cutting it (junk: idle before first action)
- A3->A4: fast-forwarded src 40.40-51.50 instead of cutting it (junk: idle, nothing changes)
- A6->A7: fast-forwarded src 75.50-125.00 instead of cutting it (waiting/replaying whip slide preview; tweaking speed/direction settings, narration moves on; junk: idle cursor)
- A7->A8: fast-forwarded src 135.50-196.00 instead of cutting it (repeated settings experiments and idle; junk: frozen, nothing changes)
- A13: after A14 (until src 223.60) jumps back to src 219.20 - narration order

## Judgment calls
- No plan zooms: the recorder already zooms the footage (double-zoom lesson); ripples only.
- Anchors: heading, animate (2nd), rise, photo, animate, element (Whip Slide; "animation" gave only 1.5 s), Preview (Play), remove (2nd), share, download, video (mp4 was 0.7 s after download), GIF, PNG, JPG, export (final Download).
- PNG/JPG: narration order PNG then JPG, recording JPG then PNG: builder jumps back with a cross-fade.
- Fast-forwarded (ff, up to 4x): intro idle, frozen 40-51 s, 75-125 s and 135-196 s. Plain cross-faded cuts: 59.5-70.0 (hovering tiles), 208.3-213.5 (open dropdown wait); tail 236+ cut (desktop).
- Missing in the recording: narration of page tab, create an animation, drag path/done, timeline handles (L5-L8, L10-L13); those lines play over fast-forwarded footage of the settings panel.
- Warnings: A6 result and A15 result appear slightly after their lines end (<0.8 s).
