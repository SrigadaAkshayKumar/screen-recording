# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | landscape | 9.960 | A1 Landscape Video option | 11.900 | 1.19x |
| 4 | Open | 11.780 | A3 Elements tab | 35.500 | 1.00x |
| 4 | add | 12.840 | A4 black rectangle shape | 48.300 | 1.00x |
| 4 | stretch | 14.320 | A5 rectangle left handle | 50.800 | 1.00x |
| 4 | strip | 15.940 | A6 rectangle right handle | 53.600 | 1.02x |
| 5 | color | 20.020 | A2 grey background swatch | 32.300 | 1.00x |
| 6 | elements | 22.500 | A7 Elements tab | 71.000 | 1.00x |
| 6 | frames, | 23.820 | A8 Frames tab | 74.800 | 1.00x |
| 6 | photo | 26.000 | A9 photo frame | 83.400 | 1.00x |
| 7 | Resize | 27.460 | A10 frame corner handle | 85.500 | 1.44x |
| 7 | duplicate | 30.740 | A11 Duplicate button | 92.100 | 1.00x |
| 7 | three | 31.820 | A12 Duplicate button | 93.400 | 1.20x |
| 8 | Drag | 34.540 | A14 uploaded photo | 167.000 | 1.00x |
| 8 | each | 36.400 | A15 uploaded photo | 173.500 | 1.00x |
| 9 | Double | 37.740 | A17 photo (double-click) | 203.300 | 1.23x |
| 10 | white | 44.680 | A18 white square graphic | 238.500 | 1.00x |
| 11 | Duplicate | 47.440 | A19 Duplicate button | 256.200 | 1.00x |
| 11 | copy | 49.120 | A20 row of squares | 276.000 | 1.10x |
| 13 | click | 57.000 | A21 Group button | 291.000 | 1.00x |
| 15 | Move | 60.680 | A22 group | 297.600 | 1.00x |
| 16 | animate | 64.080 | A23 Animate button | 308.300 | 1.00x |
| 17 | Create | 66.120 | A24 Create an Animation card | 312.000 | 1.00x |
| 18 | Drag | 67.900 | A25 film strip | 316.000 | 1.00x |
| 19 | settings | 72.820 | A26 Done button | 342.700 | 1.00x |
| 19 | preview | 73.660 | A27 Play button | 347.000 | 1.13x |
| 23 | scene | 84.280 | A28 scene length handle | 361.800 | 1.39x |
| 24 | choose | 90.040 | A29 Share button | 375.300 | 1.30x |
| 24 | download, | 91.120 | A30 Download option | 377.600 | 1.00x |

## Builder decisions

- A3: after A1 (until src 13.12) jumps ahead to src 34.90 - narration order
- A4: after A3 (until src 36.56) jumps ahead to src 48.30 - narration order
- A5: after A4 (until src 49.78) jumps ahead to src 50.80 - narration order
- A6: after A5 (until src 52.45) jumps ahead to src 53.60 - narration order
- A2: after A6 (until src 56.85) jumps back to src 31.47 - narration order
- A7: after A2 (until src 34.03) jumps ahead to src 70.25 - narration order
- A8: after A7 (until src 72.32) jumps ahead to src 74.80 - narration order
- A9: after A8 (until src 76.38) jumps ahead to src 82.80 - narration order
- A11: after A10 (until src 88.11) jumps ahead to src 91.43 - narration order
- A14: after A12 (until src 95.27) jumps ahead to src 166.15 - narration order
- A15: after A14 (until src 168.86) jumps ahead to src 173.50 - narration order
- A17: after A15 (until src 175.15) jumps ahead to src 203.30 - narration order
- A18: after A17 (until src 209.04) jumps ahead to src 237.30 - narration order
- A19: after A18 (until src 240.60) jumps ahead to src 255.54 - narration order
- A20: after A19 (until src 258.05) jumps ahead to src 276.00 - narration order
- A21: after A20 (until src 282.68) jumps ahead to src 289.80 - narration order
- A22: after A21 (until src 293.48) jumps ahead to src 296.40 - narration order
- A23: after A22 (until src 300.24) jumps ahead to src 307.54 - narration order
- A24: after A23 (until src 310.34) jumps ahead to src 312.00 - narration order
- A25: after A24 (until src 313.78) jumps ahead to src 316.00 - narration order
- A26: after A25 (until src 320.92) jumps ahead to src 342.70 - narration order
- A27: after A26 (until src 343.65) jumps ahead to src 347.00 - narration order
- A29: after A28 (until src 366.00) jumps ahead to src 372.00 - narration order
- A30: after A29 (until src 376.38) jumps ahead to src 377.60 - narration order

## Judgment calls
- Audio order followed. Source order differs: background colour (A2, src 32) is shown at line 5 although recorded before Elements/rectangle; Elements again (A7) etc. jump forward. Every jump is a cross-fade (`src_from`/`prev_until` generated per pair so each piece is >= 0.5 s at ~1x).
- Anchors: A1 landscape, A3 Open, A4 add, A5 stretch, A6 strip, A2 color, A7 elements(again), A8 frames, A9 photo, A10 Resize, A11 duplicate, A12 three, A14 Drag, A15 each, A17 Double, A18 white, A19 Duplicate, A20 copy, A21 click(group), A22 Move, A23 animate, A24 Create, A25 Drag, A26 settings, A27 preview, A28 scene, A29 choose(share), A30 download.
- No zooms and no ripples: no click log, cursor coordinates are estimates and the recording already contains the recorder's own zoom/pan. A wrong ripple/zoom would be worse than none.
- A13 (Uploads tab) and A16 (third photo drop) have no anchor: narration gives three drags only ~3 s. Their footage is skipped (A16) / plays only as approach. Two of three photo drops are shown.
- Skipped source: typing/search for "black rectangle" (37-47), 60-70 browsing, 176-203 photo browsing, 209-237 white-square search, 322-342 path settings (cut, narration allows 1 s), 351-361 idle.
- Intro: recording opens with 7.8 s of a frozen home page. `work/intro_patch.py` (hand patch on plan.json, re-run after each builder run) shows the finished moving film strip (src 347.4-351.0) for the first 3.6 s, then cross-fades to the real start (src 5.2).
- Narrated but absent in the recording: choosing "MP4 video", playing the downloaded file; closing shot is the open Download dialog.
- Warnings left: results of A15/A20/A24/A25 land a little after their narration line ends (<= 1.2 s), harmless.
