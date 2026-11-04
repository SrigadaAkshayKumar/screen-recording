# script-17 report

## Result
- `projects/script-17/output/final.mp4`, 92.553 s (matches voiceover), 2560x1440, verify **PASS** (no frozen span over 3 s, 30 join boundaries clean).
- Longest near-static piece in the preview (freezedetect d=1.2): 2.2 s (L10/L11 boundary and L14); the rest are <= 1.7 s. No held frames.

## Stages
- probe, transcribe, align, scenes, frames: reused (already current).
- analyze: ran by hand from the 1 s contact sheets; `work/actions.json` is an empty action list (no click log, baked recorder zoom), see analyze-notes.md.
- sync: hand plan (`work/hand_plan.py`, one piece group per narration line). `check.py --plan`: OK, no `pace:` warnings.
- preview render, final render, verify: ran once each, no fix round needed.

## Judgment calls
- The take (275.7 s) is longer than the narration and in script order, but the recorder zoom is baked in; no extra zooms or ripples were added.
- Each line group starts at its line start; pieces play at one speed per line: 0.77-1.41x (all within 0.75-1.5x). Nothing was fast-forwarded above 1.3x; dead time (home page idle, glow static 81-91 s, slider idle 106-113 s, 160-210 s shape/text fiddling, 242-254 s toast wait, 260-269 s viewer) is skipped by cross-faded jumps rather than played.
- Click landing: BG Remover click lands on "BG" (14.8 s); Edit on "open Edit"; Glow, colour, blur, intensity, Share, Download within about 0.7 s of their words.
- Lines with no matching footage use the closest real footage (marked partly): L1 (opening), L6 (cutout while eligibility is spoken), L17 (outline on black, then download preparing), L20 (Share panel "Print with Canva" and final artwork), L21 (outline closeup).
- The take uses a black square, narration says "coloured shape".
- Footage re-used: 218.6-219.9 appears in L15 and L21; 228.0-230.0 region in L16 and L20.

## Per-line table (checked on frames of final.mp4 at line start + 0.3 s and mid-line)
| line | out window | source (s) | what is shown | match |
|---|---|---|---|---|
| 1 | 0.00-5.00 | 6.9-10.9 | Canva home, then zoom to search bar and Templates | partly (opening shot, no photo yet) |
| 2 | 5.00-8.76 | 12.8-16.5 | 'logo' results, click Create a blank logo, empty square canvas opens | yes |
| 3 | 8.76-13.82 | 20.6-24.4, 28.0-30.4 | Uploads tab, image list scroll, photo clicked and placed on the canvas | yes |
| 4 | 13.82-17.54 | 45.2-49.9 | Photo selected, BG Remover clicked (click on 'BG'), processing, cutout appears | yes |
| 5 | 17.54-22.40 | 61.5-66.0 | Zoom into the cutout edges (hair, shoulders) | yes |
| 6 | 22.40-25.96 | 52.0-56.0 | Cutout overview (borrowed; no footage for the eligibility note) | partly |
| 7 | 25.96-29.60 | 65.2-67.6, 72.0-73.6 | Edit clicked, Edit image panel, scrolled to the Shadows row | yes |
| 8 | 29.60-33.06 | 78.7-82.0 | Glow thumbnail clicked, glow applied | yes |
| 9 | 33.06-39.70 | 96.9-99.2, 104.6-106.4, 115.0-118.0 | Colour picker set to white, Blur dragged to 0, Intensity dragged to 60 | yes |
| 10 | 39.70-44.10 | 118.8-123.0 | Size slider dragged, white edge grows | yes |
| 11 | 44.10-47.84 | 139.8-143.5 | Black square placed on the page and enlarged (black, not coloured) | yes |
| 12 | 47.84-51.04 | 147.6-151.0 | Layer > Send to back, sticker visible over the shape | yes |
| 13 | 51.04-54.08 | 171.8-174.8 | Text tab, Add a text box / Title clicked | yes |
| 14 | 54.08-57.06 | 182.0-186.2 | Caption 'Just Do It!' typed in bold font, zoom out | yes |
| 15 | 57.06-60.70 | 218.8-221.6 | Shape selected and deleted, white page with sticker remains | yes |
| 16 | 60.70-67.24 | 227.1-228.0, 230.0-231.6, 234.9-238.6 | Share, Download panel, PNG, Transparent background toggle, Download clicked | yes |
| 17 | 67.24-74.84 | 155.9-159.2, 239.0-242.4 | White outline around the cutout on black (borrowed), then the download preparing toast | partly |
| 18 | 74.84-77.94 | 269.3-272.2 | Back on the plain white Canva page, sticker with white edge | yes |
| 19 | 77.94-80.74 | 255.6-258.8 | Download history popup, then the PNG opened on a dark checkerboard viewer | yes |
| 20 | 80.74-88.14 | 227.6-230.6, 272.2-275.0 | Share panel with 'Print with Canva' (borrowed), then the artwork zoomed | partly (no printing footage) |
| 21 | 88.14-92.55 | 215.0-218.8 | Sticker with white outline, zoomed on black (borrowed) | partly |

## Uncertain
- analyze-notes.md / sync-notes.md: no click log, so click times were read from 1 s frames (about +-0.3 s).
- Glow click time (~79.2 s) and the Share/Download clicks were not measured frame by frame.

## Check these
- 5.0-8.8 s (L2): the Create a blank logo click and the canvas opening.
- 29.6-33 s (L8) and 33-39.7 s (L9): glow click and the colour/blur/intensity moves against the words.
- 60.7-67 s (L16): Share, Download, PNG, Transparent, Download clicks are close together.
- 67-74 s (L17), 80.7-92 s (L20/L21): borrowed footage.

## Lessons added
- One line in docs/lessons.md (run log).
