# Report: script-12 (Canva logo -> favicon)

## Result
- `projects/script-12/output/final.mp4`, 3420x1922, 91.933 s (voiceover 91.95 s). **verify PASS** (duration, streams, resolution, frozen spans, black frames at 30 joins).
- Strict freezedetect on the final (n=0.003, d=1.7): 1.27-3.17 s, 3.73-5.6 s, 20.83-22.7 s (each <= 1.9 s, cursor-only/loading) and the closing 89.4-91.95 s (2.55 s, last line, <= 3 s allowed). Nothing over 2.5 s except that closing.
- check.py --plan: no `pace:` warning. Pieces run 0.75-1.9x (the 1.9x piece is a static download toast), no holds, no pieces under 0.5 s.

## Stages
- probe, transcribe, align, scenes, frames: reused (already current). Alignment 21/21 lines ok (L3 fuzzy for "512").
- analyze: done by hand from 1 s sheets (work/frames/a*, b*); actions.json has coarse landmarks only. `check.py --actions` OK.
- sync: hand plan (work/hand_plan.py), because the take does not follow the script. `check.py --plan` OK.
- preview: rendered twice (first freezes of 2.1-2.2 s in L1/L9 fixed). Review sheets of all 27 joins read: only the expected cross-fade blends.
- final render 335 s; verify PASS.

## Judgment calls
- **The recording is a Canva sticker/"Sparkles" take**, not a favicon one: no favicon, Site tab, Settings or ICO footage exists. Lines are matched by topic where no real step exists (see table).
- Followed audio order: L10 (small zoom) before L11 (inspection) although the take zooms in first (cross-faded jump back).
- Cut loading screens (editor load 24.3-25.5, dark browser 124.5-127.5), the idle share-panel time and the 11 s cat opening; fast-forwarded only the static download toast (1.9x).
- No zooms/ripples: the recording has baked recorder zoom (lessons 2026-10-10/11).
- Each group starts on its line's start from lines.json; Share click lands on "Share" (46.2), Download click ~47.0, file type list on "PNG" (48.0), Transparent toggle on "Transparent/Background" (~50.4), Download click ~58.6, Publish click ~72.2.

## Per-line table (verified on final.mp4 frames)
| L | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-5.6 | 128.3-130.9, 12.4-14.3 | published page with the sticker loading, then Canva home | partly (result + start of workflow) |
| 2 | 5.6-8.1 | 14.3-16.6 | Create a design dialog, Custom size | yes |
| 3 | 8.1-13.16 | 16.6-22.2 | Custom size, 512 x 512 typed | yes |
| 4 | 13.16-15.06 | 22.2-23.4, 27.2-27.9 | Create new design click, blank square canvas | partly (no logo paste in the take) |
| 5 | 15.06-20.02 | 31.4-35.4 | Elements panel, search for a symbol ("sticker") | partly |
| 6 | 20.02-24.92 | 35.4-38.6 | results, sticker placed on the square | partly (take has no browser-tab shot) |
| 7 | 24.92-29.32 | 38.6-42.1 | sticker resized with the handle (size tooltip) | yes |
| 8 | 29.32-30.96 | 42.1-44.0 | sticker settled on the page, cursor to Text | partly |
| 9 | 30.96-37.7 | 44.0-46.8, 48.2-51.5 | Text panel, subheading added, "Sparkles" typed | partly (bold letter in circle not in take) |
| 10 | 37.7-40.04 | 71.0-73.2 | zoom out until the design is tiny | yes |
| 11 | 40.04-45.8 | 59.8-66.0 | zoomed in on the artwork and the lettering | yes |
| 12 | 45.8-49.4 | 76.4-77.4, 79.7-80.6, 82.9-84.7 | Share click, Download click + panel, file type list with PNG | yes |
| 13 | 49.4-55.46 | 88.4-91.2, 98.2-100.5 | Transparent background toggled on, PNG on dark in Preview | yes |
| 14 | 55.46-58.14 | 81.0-83.0 | download panel, transparency off (solid background) | partly (no colour picker in take) |
| 15 | 58.14-64.02 | 92.3-98.2, 100.5-102.3 | Download click, file toast, file opened in Preview | partly (no favicon upload) |
| 16 | 64.02-68.24 | 105.4-109.4 | Share > More ways to publish | partly (not the Publish dropdown; no Settings click) |
| 17 | 68.24-73.98 | 112.0-117.2 | Website panel with Publish / Settings, Publish click ~72.2 | partly (no Site tab / favicon upload) |
| 18 | 73.98-83.02 | 120.7-122.9, 85.0-88.3, 102.3-104.2 | "website published" toast, file type list/size, PNG preview closing | partly (conceptual line, reused footage) |
| 19 | 83.02-84.44 | 104.2-105.4 | back in Canva | no (conceptual, no matching footage) |
| 20 | 84.44-88.52 | 123.0-124.7, 127.5-129.9 | Website panel, browser opens the published page | yes |
| 21 | 88.52-91.95 | 129.9-133.3 | published page with the sticker, browser tab | partly (no refresh shown) |

## Uncertain
- Favicon-specific steps (Settings > Site tab > favicon upload > Done, tab icon, ICO, cache refresh) are not in the recording; L16-L19, L21 are topic matches, not the step itself.
- Take shows a sticker + "Sparkles" text, not "a bold letter in a coloured circle" (L9).
- Pre-hand-plan analysis is coarse: actions.json has 7 landmarks only.

## Check these
- 3.4-5.6 (home piece after the cross-fade from the result page), 13-15 (Create click -> blank canvas jump), 45.8-50.5 (three cuts across Share/Download/PNG/Transparent), 53-55.5 (PNG preview as "transparent background"), 64-68 and 76-84 (reused/conceptual footage), closing 89.4-91.95 (2.55 s near-still page, only the loading dot moves).
- Source recording is ~2.8 Mbps (387 MB / 136 s): soft source.

## Lessons added
- One entry in docs/lessons.md.
