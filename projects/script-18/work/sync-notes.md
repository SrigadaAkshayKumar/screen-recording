# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 1 | shortcuts. | 6.120 | A1 Home button in the sidebar | 13.800 | 2.25x |
| 2 | projects | 7.840 | A2 Projects button in the sidebar | 17.000 | 1.86x |
| 3 | design | 10.180 | A3 three-dot menu on the first design | 24.300 | 3.12x |
| 3 | title | 12.700 | A4 title beside the pencil icon | 29.800 | 2.18x |
| 4 | pattern | 15.960 | A5 title field | 30.600 | 1.00x +2.5s hold |
| 7 | checkboxes, | 32.060 | A12 three-dot menu on the design | 165.800 | 1.00x +4.2s hold |
| 7 | move, | 33.560 | A13 Move menu item | 167.200 | 0.93x |
| 7 | folder, | 34.840 | A14 thumbnails folder in the dialog | 170.200 | 2.34x |
| 7 | confirm. | 35.680 | A15 Move confirm button | 172.400 | 2.62x |
| 8 | subfolder | 39.100 | A11 class-1 breadcrumb | 143.500 | 0.99x |
| 9 | star | 46.760 | A6 star icon on the design card | 84.200 | 1.00x +4.0s hold |
| 10 | sidebar. | 51.240 | A7 starred design in the sidebar | 98.000 | 1.18x |
| 12 | Recent | 54.240 | A8 Recents heading | 108.000 | 3.33x |
| 13 | retrieve | 61.860 | A9 class-1 folder | 112.400 | 1.00x +3.2s hold |
| 13 | folder | 63.020 | A10 images folder | 114.000 | 1.38x |

## Builder decisions

- A12: after A5 (until src 40.70) jumps ahead to src 164.00 - narration order
- A11: after A15 (until src 174.30) jumps back to src 142.00 - narration order
- A6: after A11 (until src 145.50) jumps back to src 82.50 - narration order
- A6->A7: cut src 88.00-96.50 - too long to fast-forward at <= 2.00x (idle after starring (toast))
- A7->A8: fast-forwarded src 100.00-106.50 instead of cutting it (idle cursor on the page)

## Judgment calls

- **No zooms**: the recorder's auto-zoom is baked into the footage; adding zooms would double-zoom (lessons.md, script-1). Ripples only; A7/A8 are hovers, no ripple.
- **Audio order wins.** Footage order is rename -> star -> Recents -> folder nav -> move. Narration is rename -> move -> subfolder -> star -> sidebar -> Recents -> folder. Jumps (cross-faded): A5 -> A12 (src 164), A15 -> A11 (src 142), A11 -> A6 (src 82.5). Continuity oddity: the move footage (164-175) shows the design already named "New-canva-design-version-1" (second rename at 59-70 s is not shown) and already starred.
- Anchor words: Home on "shortcuts" (end of L1, so Home then Projects reads before "Open projects"), Projects on "projects", 3-dot on "design", title click on "title", typing from "pattern" (runs through L5, Enter/toast at the end of L5). Move flow on checkboxes/move/folder/confirm of L7. Class-1 breadcrumb on "subfolder" (L8). Star on "star". Sidebar item on "sidebar". Recents on "Recent". class-1 folder on "retrieve" and images folder on "folder" (L13; earlier words made the approach > 4x).
- Missing in recording, so the narration plays over a held/idle frame: creating a folder (L6, holds the renamed list), checkbox selection (only hover), creating a finished/archived folder (L15), search (L16), alternate versions (L14). L14-L17 play the idle images-folder page (src 116-142, ~1x) and the video ends there (src_end 142).
- 88-96.5 (post-star idle) is cut (too long to fast-forward); 100-106.5 fast-forwarded. 146.5-160.5 (design opened in the editor) and 175.6+ (desktop) are junk. Second rename (59-70) and thumbnail flicker (40-83) are simply unused.
- Warnings explained: A5 result lands after L4 ends (typing spans L4-L5); A15/A6 results a fraction of a second after their lines end.
- **Ripples off for clicks made while the recorder's own zoom was active** (A1, A2, A4, A9, A10, A12, A13, A14): the plan's ripple coordinates are in recording pixels and land in the wrong place on the recorder-zoomed footage (seen in the first preview at 12.8 s). Ripples remain on A3, A6, A11, A15 (and A5 is typing).
