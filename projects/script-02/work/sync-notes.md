# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Open | 4.480 | A1 Home tab | 11.400 | 1.00x |
| 2 | slide | 6.180 | A2 Presentation card | 16.000 | 2.71x |
| 3 | Open | 8.080 | A3 Apps in side panel | 32.200 | 1.47x |
| 4 | Charts. | 12.880 | A4 Charts app | 38.800 | 1.37x |
| 5 | bar | 14.120 | A5 Bar chart | 44.300 | 2.50x |
| 5 | Edit | 15.860 | A6 Edit button (toolbar) | 58.400 | 2.87x |
| 6 | three | 20.120 | A7 HR row removed | 81.300 | 0.92x |
| 7 | colours | 24.040 | A8 chart colour swatch | 89.600 | 2.12x |
| 7 | motion. | 25.440 | A9 hex colour field | 92.500 | 2.07x |
| 9 | Animate. | 30.920 | A10 Animate button | 110.900 | 1.50x |
| 10 | animation, | 33.720 | A11 Rise animation tile | 133.500 | 2.43x |
| 12 | controls | 39.640 | A12 animation speed/timing controls | 137.800 | 1.00x +1.6s hold |
| 14 | chart | 48.260 | A19 Add page button | 188.900 | 1.82x |
| 15 | Download | 49.960 | A14 Download option | 167.600 | 1.94x |
| 15 | PNG, | 51.020 | A15 PNG file type | 171.000 | 3.21x |
| 15 | upload | 52.000 | A17 Uploads in side panel | 177.400 | 3.06x |
| 15 | animate | 54.180 | A20 Animate button (image toolbar) | 197.800 | 1.51x |
| 16 | original | 56.160 | A21 page 1 thumbnail | 254.700 | 2.17x |
| 20 | Preview | 74.060 | A22 chart on page 2 | 263.400 | 2.24x |
| 21 | To | 76.340 | A23 Share button | 277.000 | 2.15x |
| 21 | download | 78.100 | A24 MP4 Video file type | 282.500 | 3.13x |
| 21 | MP4 | 79.700 | A25 Download button | 286.600 | 2.56x |

## Builder decisions

- A2->A3: cut src 18.60-32.00 - too long to fast-forward at <= 2.20x (junk: waiting on the empty new slide with the Templates panel; idle)
- A4->A5: cut src 40.80-43.20 - too long to fast-forward at <= 2.20x (junk: idle on the Charts panel)
- A6->A7: cut src 60.00-79.00 - too long to fast-forward at <= 2.20x (junk: cursor moves through the data table (values unchanged))
- A7->A8: fast-forwarded src 82.30-88.40 instead of cutting it (junk: browsing Chart setup options after deleting HR)
- A9->A10: cut src 94.00-104.20 - too long to fast-forward at <= 2.20x (junk: idle on the Colour panel)
- A10->A11: cut src 116.00-131.80 - too long to fast-forward at <= 2.20x (cursor browses the animation tiles before choosing)
- A19: after A12 (until src 153.00) jumps ahead to src 188.40 - narration order
- A12->A19: fast-forwarded src 141.00-155.80 instead of cutting it (junk: cursor idle on the Animate panel)
- A14: after A19 (until src 191.20) jumps back to src 166.60 - narration order
- A17: after A15 (until src 172.80) jumps ahead to src 176.20 - narration order
- A20: after A17 (until src 179.50) jumps ahead to src 196.60 - narration order
- A21: after A20 (until src 201.40) jumps ahead to src 254.00 - narration order
- A20->A21: fast-forwarded src 201.00-233.00 instead of cutting it (junk: trying image animations in the Animate panel)
- A22: after A21 (until src 256.50) jumps back to src 201.50 - narration order
- A21->A22: fast-forwarded src 201.00-233.00 instead of cutting it (junk: trying image animations in the Animate panel)
- A23: after A22 (until src 267.50) jumps ahead to src 276.20 - narration order

## Judgment calls

- **Audio order followed.** Anchors are laid out by narration. Reorders: line 14 "own page" (Add page, src 188.9) is shown before
  line 15's download/upload steps (src 165-186), which the recording did earlier; line 16 "original chart on a separate page"
  uses the page-1 click at src 254.7. Continuity oddity: the new blank page appears *before* the PNG download is shown.
- **No zooms.** The recorder's auto-zoom is baked into the footage (lessons 2026-10-10 script-1), so the plan adds none.
  **No ripples either** (`no_ripple` on every action): click x/y were not verified with a crosshair and most clicks happen
  while the recorder is zoomed (lessons 2026-10-11 script-18).
- Anchors: A1 "Open"/A2 "slide" (Home -> new presentation); A3 "Open" and A4 "Charts" show Apps -> Charts icon over lines 3-4
  (the recording has no direct Charts click in the side panel and nothing is typed in a search box); A5 "bar", A6 "Edit";
  A7 "three" (HR row removed); A8 "colours", A9 "motion" (hex typed, chart turns navy); A10 "Animate"; A11 "animation" (tile chosen,
  preview auto-plays under line 10-11); A12 "controls"; A19 "chart" (Add page, a bit early for "page" to leave room);
  A14 "Download", A15 "PNG", A17 "upload", A20 "animate"; A21 "original"; A22 "Preview"; A23 "To", A24 "download", A25 "MP4".
- Narrated "Preview the slide in presentation mode": not recorded; the animation preview playing on page 2 (src 263-267) stands in.
- Cuts (too long to fast-forward at <= 2.2x, not off-topic): idle waiting 18.6-32.0, idle on Charts panel 40.8-43.2,
  data-table browsing 60-79 (values unchanged), idle on Colour panel 94-104, animation tile browsing 116-131.8.
  Cross-fade cuts: hovering bars 47.5-56.6, 236-253.8 and 256.6-262.4 (redundant animation tries / page clicks).
  Off-topic cut: chart drag-resize 155.9-162.5 (not narrated).
- Fast-forwarded instead of cut: 82.3-88.4, 141-155.8 (idle on Animate panel), 201-233 (image animation tries, ~2x).
- Intro starts at src 6.9 (the first 7 s are the old idle chart deck). Outro stops at 287.4, before the tray popup.
- A21 -> A22: the page-1 click (253.8-256.6) plays twice (once for line 16, again inside the line 17-19 stretch);
  the second pass is a short cross-faded replay.
- Fast approaches: A15 PNG 3.2x, A17 upload 3.1x, A24 download 3.1x (short stretches of dialogs).
- Warnings: results of A3, A4, A9, A10 appear a little after their line ends; A13, A16, A18 are unanchored (Share click, Download button, file dialog).
