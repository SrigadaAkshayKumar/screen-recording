# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 4 | uploads | 18.900 | A1 Uploads in left sidebar | 18.550 | 0.98x |
| 5 | upload | 21.200 | A2 Upload files button | 30.550 | 1.04x |
| 5 | logo | 22.900 | A3 Open button in file picker | 34.300 | 1.21x |
| 7 | uploaded | 32.220 | A4 logo thumbnail in uploads | 41.600 | 0.78x |
| 8 | corner | 35.460 | A5 bottom-right corner handle | 46.200 | 1.42x |
| 8 | move | 37.140 | A8 logo | 90.000 | 1.19x |
| 10 | footage, | 45.960 | A6 chart image in uploads (footage) | 81.600 | 0.96x |
| 11 | logo | 51.540 | A9 logo layer in timeline | 100.300 | 1.11x |
| 16 | Preview | 73.700 | A10 playhead on timeline (previewing the video) | 154.900 | 1.00x |
| 17 | share, | 79.180 | A11 Share button | 177.600 | 1.13x |
| 17 | download | 80.100 | A12 Download in share menu | 180.200 | 1.09x |
| 17 | MP4 | 80.980 | A13 MP4 Video in file type list | 183.950 | 1.02x |
| 18 | downloaded | 82.700 | A14 Download button | 187.100 | 1.08x |

## Builder decisions

- A2: after A1 (until src 19.90) jumps ahead to src 29.50 - narration order
- A3: after A2 (until src 31.80) jumps ahead to src 33.50 - narration order
- A8: after A5 (until src 47.60) jumps ahead to src 89.40 - narration order
- A6: after A8 (until src 97.00) jumps back to src 80.10 - narration order
- A9: after A6 (until src 86.50) jumps ahead to src 99.00 - narration order
- A10: after A9 (until src 121.50) jumps ahead to src 153.90 - narration order
- A11: after A10 (until src 160.00) jumps ahead to src 176.50 - narration order
- A12: after A11 (until src 178.10) jumps ahead to src 179.70 - narration order
- A13: after A12 (until src 180.60) jumps ahead to src 183.45 - narration order
- A14: after A13 (until src 184.90) jumps ahead to src 186.20 - narration order

## Judgment calls
- Recording has the recorder's auto-zoom baked in -> no zooms, ripples only on the unzoomed clicks (Upload files, Share).
- Anchors: A1 "uploads", A2 "upload", A3 "logo" (+0.1), A4 "uploaded", A5 "corner" (resize), A8 "move" (move to corner, footage from 89.4), A6 "footage," (chart added, L10), A9 "logo" (L11, layer in timeline), A10 "Preview" (playhead scrub 154.9), A11 "share,", A12 "download", A13 "MP4", A14 "downloaded".
- Order changes (audio wins): resize/move-to-corner footage (88-92) is shown at L8 although the recording does it after the chart is added (81.6). The chart is then added at L10 "footage" -> continuity oddity: the chart is already on the canvas in the L8 shots.
- Cuts (cross-faded jumps) instead of fast-forward, because the narration leaves 2.3 s for 12 s of dead time: 20.2-29.5 (idle after Uploads), 32.1-33.5 (file picker browsing), 48-89 jump to the chart section, 97-80 back-jump, 86.5-99, 121.5-153.9, 160-176.5, 178.1-179.7, 180.6-183.45, 184.9-186.2.
- Unanchored: A7 (resize on chart, never shown), A15 wait (export). Hand edit to plan.json: last segment src_end 190.9 and wait:true (1.6x) so the closing frame shows the finished design instead of the open Download panel.
- No recording footage exists for "select position / open layers" (L10), "adjust start/end edges" (L12; timeline hover 100-121 played at 1x), "copy logo to scenes" (L13) or "separate scenes" - those lines play over related footage (timeline).
- Pace: no `pace:` warnings remain. Slowest 0.78x (A3->A4), fastest approach 1.42x (A4->A5).
