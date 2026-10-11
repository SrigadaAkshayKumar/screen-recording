# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | title | 10.080 | A1 title field in the top toolbar | 22.200 | 2.20x |
| 4 | descriptive | 14.700 | A2 title field | 24.500 | 1.00x +2.3s hold |
| 5 | home | 22.080 | A3 Home tab in the browser tab strip | 52.000 | 3.73x |
| 6 | Open | 23.220 | A4 Projects in the left sidebar | 61.700 | 1.93x |
| 6 | find | 24.380 | A5 three-dots menu on the design card | 76.200 | 3.19x |
| 6 | title | 25.860 | A6 design title (beside pencil icon) in the card menu | 78.800 | 1.76x |
| 7 | Enter | 28.100 | A7 design title field | 80.900 | 0.94x |
| 8 | Uploads | 34.060 | A8 Uploads folder | 96.100 | 2.55x |
| 8 | file. | 35.820 | A9 three-dots menu on the duck gif card | 112.200 | 2.50x |
| 9 | preview | 37.240 | A10 duck gif thumbnail | 117.500 | 3.73x |
| 9 | Rename | 38.200 | A11 three-dots menu in the preview controls | 121.200 | 3.85x |
| 9 | controls. | 39.520 | A12 file name in the preview header | 123.300 | 1.59x |
| 10 | Enter | 40.840 | A13 file name field | 125.000 | 1.29x |
| 14 | repeat | 58.380 | A14 design title in the editor toolbar | 184.300 | 3.38x |
| 14 | version | 60.780 | A15 design title field | 187.000 | 1.12x |
| 16 | Projects | 69.560 | A16 Your projects in the left sidebar | 213.000 | 2.96x |

## Builder decisions

- intro: fast-forwarded src 5.30-16.90 instead of cutting it (junk: idle editor at start)
- A2->A3: fast-forwarded src 34.60-50.20 instead of cutting it (junk: frozen screen after rename)
- A3->A4: cut src 53.50-61.00 - too long to fast-forward at <= 3.00x (junk: browsing home page)
- A4->A5: cut src 65.00-75.80 - too long to fast-forward at <= 3.00x (junk: cursor wandering over recents)
- A7->A8: fast-forwarded src 88.90-95.80 instead of cutting it (junk: toast idle)
- A8->A9: cut src 98.80-100.00 - too long to fast-forward at <= 3.00x (junk: page loading)
- A8->A9: cut src 101.30-111.80 - too long to fast-forward at <= 3.00x (junk: scrolling uploads items)
- A13->A14: fast-forwarded src 130.70-153.00 instead of cutting it (junk: idle on renamed preview)
- A13->A14: fast-forwarded src 153.40-182.00 instead of cutting it (junk: closing preview, navigating back, idle on Uploads)
- A15->A16: fast-forwarded src 205.50-210.60 instead of cutting it (junk: idle on editor)

## Judgment calls
- Followed the audio order. The recording happens to match the narration order (editor rename, home-page rename, upload rename, version label, return to Projects), so no out-of-order jumps.
- Line 14 (Draft01/Final) is shown with the late editor rename (src 184-205); lines 11-13 play over the idle renamed preview (ff, 130-153) and the navigation back (ff, 153-182).
- No zooms: the recorder already baked in auto-zoom. Ripples only (type actions get none).
- Fast-forwarded (ff, up to 3x): idle start, frozen screen after first rename, toast idle, idle in preview, navigation, idle editor. Cut (cross-faded, too long to ff): home browsing 53.5-61, cursor wandering 65-75.8, page loading 98.8-100, scrolling 101.3-111.8.
- Anchors: clicks on the word naming the control; A2 (typing) anchored on "descriptive" so the name is typed while spoken; A4 on "Open" to leave time for the A5/A6 clicks.
- A card three-dots menu (A9) and preview menu (A11) are shown although the menu has no Rename entry; the real rename was the preview header name click (A12). Narration says "Rename action in the file controls", the footage differs.
- Results land after their lines end for A7, A13, A15, A16 (typing is slower than the narration), so the finished name is visible a few seconds late.
