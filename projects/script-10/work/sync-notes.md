# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 5.040 | A1 welcome presentation thumbnail on Canva home | 9.100 | 1.81x |
| 3 | animate | 10.040 | A3 Animate button in toolbar | 28.300 | 2.84x |
| 3 | remove | 11.040 | A4 animation style / remove in Page Animations panel | 31.700 | 3.40x |
| 4 | select | 15.900 | A5 welcome text box | 49.000 | 2.04x |
| 4 | shapes | 19.000 | A6 To Canva text box | 64.900 | 2.77x |
| 5 | animation | 21.240 | A8 Animate button in toolbar (slide 2) | 71.400 | 2.90x |
| 5 | remove | 22.320 | A9 Remove all animations button | 73.600 | 2.04x |
| 9 | thumbnails | 40.900 | A10 slide 3 thumbnail | 75.300 | 1.00x +16.9s hold |
| 10 | clears | 44.500 | A11 Remove all animations button (slide 3) | 80.800 | 1.53x |
| 11 | transitions | 50.520 | A12 transition icon between slides 1 and 2 | 110.300 | 1.28x |
| 12 | each | 52.820 | A14 transition icon between slides 2 and 3 | 122.000 | 3.22x |
| 12 | remove | 54.740 | A15 None in Transitions panel | 124.500 | 1.30x |
| 13 | Run | 56.820 | A16 Present button | 139.400 | 1.88x |
| 13 | changes | 59.380 | A17 slide (advance) | 141.700 | 0.90x |
| 13 | plain | 61.000 | A18 slide (advance) | 143.000 | 0.80x |
| 15 | animation | 66.660 | A20 Animate button in toolbar | 159.800 | 2.97x |
| 15 | text, | 69.220 | A22 To Canva text box | 166.600 | 2.66x |
| 16 | uploaded | 73.920 | A23 Uploads in the sidebar | 178.300 | 1.17x |
| 16 | GIF | 75.060 | A24 Videos tab in Uploads | 188.000 | 3.25x |
| 18 | text | 83.500 | A25 Effects in toolbar | 203.700 | 1.86x |
| 19 | Preview | 88.320 | A26 Present dropdown arrow | 215.000 | 2.34x |
| 20 | movement | 93.520 | A29 close X of presenter window | 226.400 | 2.19x |

## Builder decisions

- A1->A3: cut src 14.50-19.50 - too long to fast-forward at <= 2.00x (junk: idle cursor hovering over thumbnails)
- A4->A5: cut src 40.50-47.90 - too long to fast-forward at <= 2.00x (junk: idle, nothing happens)
- A5->A6: cut src 51.10-58.40 - too long to fast-forward at <= 2.00x (junk: idle on selected text)
- A12->A14: cut src 113.60-117.90 - too long to fast-forward at <= 2.00x (junk: cursor idle on transitions panel)
- A18->A20: fast-forwarded src 148.60-156.70 instead of cutting it (junk: frozen editor after presenting)
- A23->A24: cut src 180.50-186.50 - too long to fast-forward at <= 2.00x (browsing uploads panel before Videos tab)
- A24->A25: fast-forwarded src 194.20-201.70 instead of cutting it (junk: idle cursor)

## Judgment calls
- **Baked-in recorder zoom** (see analyze-notes): no zooms, and `no_ripple` for every action, since positions were read off zoomed frames and would put ripples in the wrong place.
- Anchors: A1 "Open" (L2); A3 "animate", A4 "remove" (L3); A5 "select", A6 "shapes" (L4); A8 "animation", A9 "remove" (L5, slide 2 page animations, the only remove-effects footage); A10 "thumbnails" (L9); A11 "clears" (L10); A12 "transitions" (L11); A14 "each", A15 "remove" (L12); A16 "Run", A17 "changes", A18 "plain" (L13); A20 "animation", A22 "text" (L15); A23 "uploaded", A24 "GIF" (L16); A25 "text" (L18); A26 "Preview" (L19); A29 "movement" (L20).
- Unanchored: A2, A7, A13, A19, A21, A27, A28 (supporting clicks, they play in the approach to the next anchor; A27 too close to A26 for 4x).
- **Long hold, L5-L8 (out ~24-41 s, 16.9 s):** the narration describes object-level removal and group selection, but the recording has no footage for it. The plan holds on slide 3 after the page-animation removal. Narration order was followed; no footage was dropped.
- Cuts: 126-137 s (unnarrated first present run, xfade); 90-106 s (idle on slide 2, the rest of 86.5-108.3 is fast-forwarded); 180.5-186.5 (uploads browsing). Junk idle spans 14.5-19.5, 40.5-47.9, 51.1-58.4, 113.6-117.9 did not fit at 2x and were cut. 148.6-156.7 and 194.2-201.7 were fast-forwarded. Junk bounds 51.1 / 113.6 were widened to avoid tiny 8x slivers at still-span edges.
- Cut: 167.5-173.7 (accidental rotate + tray popup), tail after 235.0.
- L5-L8 / L14 / L17 have no matching distinct footage; L17 "replace moving assets" plays over uploads / idle frames.
