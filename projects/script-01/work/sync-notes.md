# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | create | 7.180 | A1 Create button in sidebar | 11.200 | 1.00x +4.8s hold |
| 3 | vertical | 10.020 | A2 Instagram Reel (vertical video) design | 12.700 | 1.00x +1.3s hold |
| 4 | Uploads, | 14.260 | A3 Uploads in sidebar | 26.600 | 3.28x |
| 4 | Files, | 15.740 | A4 Upload files button | 28.800 | 1.49x |
| 5 | uploaded | 18.520 | A5 uploaded photo in panel | 31.600 | 1.01x |
| 5 | resize | 20.960 | A6 photo corner handle (resize) | 41.000 | 1.39x |
| 8 | Animate | 33.920 | A8 Animate button in toolbar | 74.300 | 1.00x +6.7s hold |
| 10 | pan, | 41.680 | A9 Pan effect | 97.800 | 2.51x |
| 10 | fade | 42.660 | A10 Fade effect | 105.000 | 1.73x |
| 11 | speed | 46.780 | A11 Fast speed option | 114.200 | 2.23x |
| 11 | play | 48.980 | A12 Play button under canvas | 126.900 | 1.27x |
| 13 | extend | 56.440 | A7 image layer end in timeline | 47.800 | 1.00x +5.4s hold |
| 16 | PNG | 67.820 | A16 PNG in list | 169.600 | 1.00x +6.3s hold |
| 16 | JPG | 68.740 | A17 JPG in list | 170.400 | 0.87x |
| 17 | Share, | 72.280 | A13 Share button | 165.100 | 1.00x +2.4s hold |
| 17 | download | 73.100 | A14 Download in share panel | 167.000 | 2.32x |
| 17 | MP4 | 74.100 | A18 MP4 Video in list | 178.200 | 1.80x |
| 18 | GIF | 76.140 | A19 GIF in list | 180.500 | 1.13x |
| 19 | Download | 79.720 | A21 Download button | 190.900 | 0.95x |
| 19 | play | 80.660 | A22 downloaded file toast | 196.700 | 3.30x |

## Builder decisions

- A6: after A5 (until src 33.50) jumps ahead to src 39.50 - narration order
- A8: after A6 (until src 46.00) jumps ahead to src 73.00 - narration order
- A8->A9: fast-forwarded src 85.00-92.00 instead of cutting it (junk: cursor idle, effect preview)
- A8->A9: cut src 76.00-80.00 - too long to fast-forward at <= 2.00x (junk: cursor idle on effects panel)
- A9->A10: cut src 99.00-104.50 - too long to fast-forward at <= 2.00x (junk: scrolling effects list)
- A12: after A11 (until src 115.60) jumps ahead to src 125.50 - narration order
- A7: after A12 (until src 128.00) jumps back to src 46.80 - narration order
- A16: after A7 (until src 51.50) jumps ahead to src 168.20 - narration order
- A13: after A17 (until src 170.40) jumps back to src 164.00 - narration order
- A18: after A14 (until src 167.60) jumps ahead to src 177.00 - narration order
- A21: after A19 (until src 189.50) jumps ahead to src 189.50 - narration order
- A19->A21: cut src 182.00-189.00 - too long to fast-forward at <= 2.00x (junk: GIF selected, cursor idle)
- A22: after A21 (until src 192.60) jumps ahead to src 195.30 - narration order

## Judgment calls
- Recorder baked-in auto-zoom: no zooms; ripple only for A9 (Pan, unzoomed); all other clicks `no_ripple` (lessons, script-18).
- src_start 8.8: the first 8.8 s are a finished design from another take; L1 plays over a hold of the Canva home page.
- Follow the audio: Animate (rec 74) is narrated before the timeline step (rec 47-50), so A8-A12 come first, then a cross-faded jump back to the timeline (A7, L13). PNG/JPG (rec 169-171) is narrated before Share (rec 165), so jumps back again (A13, hard cut: the builder emitted a hold with no xfade there, warned; left as is). MP4 jumps forward to 177.
- Anchor words: create/vertical (A1/A2), Uploads/Files, uploaded (photo), resize, Animate, pan, fade, speed (Fast), play (preview), extend (timeline), PNG/JPG, Share, download, MP4, GIF, Download, play.
- Fast-forward kept for 85-92 s idle (2x). Too long to fast-forward, so cut: 76-80 idle, 99-104.5 scrolling, 182-189 GIF idle. Wallpaper 205+ trimmed.
- Long holds (narration longer than footage): ~6.7 s on resized photo (L6-L7, no matching action), ~5.4 s at 127.5 (L12), ~6.3 s on 5.0 s layer (L14-15), 2.4 s before Share.
- Unnarrated: A15 (file type dropdown), A20 (MP4 reselect). A17 result partly cut. A22 result lands just after L19 ends.
- A4/A6/A7/A12/A14/A19 positions and times are low confidence (no click log).
