# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | create | 7.180 | A1 Create button (sidebar) | 10.900 | 1.52x |
| 3 | vertical | 10.020 | A2 Instagram Reel (vertical) format card | 12.800 | 1.00x +0.9s hold |
| 4 | Uploads, | 14.260 | A3 Uploads tab in the sidebar | 27.200 | 0.97x |
| 5 | uploaded | 18.520 | A4 uploaded photo thumbnail | 31.600 | 1.03x |
| 5 | resize | 20.960 | A5 photo corner handle | 40.800 | 0.78x |
| 8 | Animate | 33.920 | A6 Animate button in the toolbar | 73.500 | 1.53x |
| 10 | pan, | 41.680 | A7 Pan effect | 98.000 | 1.35x |
| 10 | fade | 42.660 | A8 Fade effect | 105.000 | 1.63x |
| 11 | speed | 46.780 | A9 Fast speed button | 114.100 | 2.21x |
| 11 | play | 48.980 | A10 Play button under the canvas | 128.300 | 0.77x |
| 13 | extend | 56.440 | A11 end handle of the photo clip in the timeline | 139.800 | 1.54x |
| 17 | Share, | 72.280 | A12 Share button | 164.800 | 1.58x |
| 17 | download | 73.100 | A13 Download option in the Share panel | 166.600 | 2.20x |
| 17 | MP4 | 74.100 | A14 MP4 Video in the file type list | 177.900 | 2.30x |
| 18 | GIF | 76.140 | A15 GIF in the file type list | 179.500 | 0.78x |
| 19 | Download | 79.720 | A17 Download button in the dialog | 190.900 | 1.01x |
| 19 | check | 81.220 | A19 downloaded-file toast | 197.400 | 4.33x |

## Builder decisions

- A2->A3: cut src 16.60-26.90 - too long to fast-forward at <= 2.00x (junk: cursor idles/hovers in the empty editor)
- A4->A5: cut src 33.00-40.30 - too long to fast-forward at <= 2.00x (junk: hovering thumbnails/photo before resize)
- A5->A6: fast-forwarded src 56.20-72.80 instead of cutting it (junk: idle editor, cursor wandering)
- A6->A7: fast-forwarded src 75.20-80.50 instead of cutting it (junk: idle Animate panel)
- A6->A7: cut src 83.00-97.00 - too long to fast-forward at <= 2.00x (junk: hovering/scrolling effects list)
- A7->A8: cut src 99.00-104.40 - too long to fast-forward at <= 2.00x (junk: hovering Pan)
- A8->A9: fast-forwarded src 106.80-113.50 instead of cutting it (junk: scrolling to speed options)
- A9->A10: cut src 115.00-127.50 - too long to fast-forward at <= 2.00x (junk: idle / scrolling)
- A11->A12: fast-forwarded src 148.00-164.30 instead of cutting it (junk: idle editor)
- A13->A14: cut src 168.00-177.00 - too long to fast-forward at <= 2.00x (junk: browsing file types)
- A15->A17: cut src 181.00-188.80 - too long to fast-forward at <= 2.00x (junk: idle GIF panel)

## Judgment calls

- Recorder auto-zoom is baked into the footage: no plan zooms; ripples only on A7 (Pan, unzoomed at the click). All other clicks are `no_ripple` (recording-pixel coordinates are unreliable while zoomed).
- Anchors follow narration order. Source order already matches the narration except the timeline step: the clean take at 139.8 s (after the preview) is used for L13, which keeps the order forward. The first, messy timeline take (44-56 s: duplicate + delete) is cut.
- Anchor words: create (Create), vertical (Instagram Reel), Uploads, uploaded (thumbnail), resize, Animate, pan, fade, speed (Fast), play (preview), extend (timeline drag), Share, download, MP4, GIF, Download, check (open the downloaded file).
- Cuts (all cross-faded): 16.6-26.9, 33-40.3, 43-55.9, 83-97, 99-104.4, 115-127.5, 168-177, 181-188.8 (ff did not fit at 2x), 197.9-200.9 (media-player loading screen), 205+ (desktop). Fast-forwarded instead of cut: 56.2-72.8, 75.2-80.5, 106.8-113.5, 148-164.3, download wait 191.5-195.5.
- Not on screen: "Upload Files / choose your photo" (L4), L6-L7 (nothing to show), L12, L15-L16 (PNG/JPG file types were browsed at 169-176 s, cut because L16 comes before Share in the audio and L17 needs the Share click).
- A16 (second MP4 pick, 189.8) is unanchored; it plays inside the kept footage before A17.
- One 0.94 s hold at 8.63 s on the open Create-a-design menu (src 12.35), which shows the response.
