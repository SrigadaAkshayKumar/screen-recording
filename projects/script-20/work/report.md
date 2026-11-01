# script-20 re-edit report

## Result
`projects/script-20/output/final.mp4` - 95.200 s, 3420x1922, verify **PASS** (duration, streams, resolution, no freeze >3 s, no black frames at 20 joins). check.py --plan: OK with no pace warnings. Preview/final freezedetect (d=1.5): longest 1.9 s (static source spans and the one 1.4 s planned hold).

## Stages
- probe, transcribe, align, scenes, frames: reused (work files were current). New 1 s contact sheets (62 tiles) and 0.5 s sheets of 22-34 s and 39.5-55 s made for the analysis.
- analyze: redone from scratch; timeline in work/analyze-notes.md (no actions.json: no click log, baked zoom, no zooms/ripples planned).
- sync: work/hand_plan.py -> work/plan.json (19 segments, no zooms/ripples), notes in work/sync-notes.md.
- preview rendered and reviewed (frames at every line start and middle), final render (5.6 min), verify PASS.

## Judgment calls
- Order: L1-L11 follow the recording order; the only jump-backs are L12 (PDF first, then the image, matching the sentence) and the reused explanatory lines L13-L19, always cross-faded.
- L3 no longer jumps back; L8 and L9 use different footage (checklist opening / ranges vs. cleared and page 3 ticked).
- L4-L10 play src 19.7-41.6 at the 0.75x floor with one 1.4 s hold (page 3 ticked, Download enabled) so the Download click lands at out 43.1 on "click Download". Waiting for the download is 2.75x (wait footage).
- Speeds: 0.75-1.0x for actions, 2.75x only for the download wait; no segment under 0.75x.
- Cut: black browser frame (3.2-3.9) and src 12.1-19.7 (static page, pages-grid view, not narrated; not enough output time to fast-forward it).

## Per-line table (out window | source | what is shown | match)
| L | out | src | shown | match |
|---|---|---|---|---|
| 1 | 0-5.92 | 0-3.15, 3.9-5.5 | Canva home list, design opens/loads | yes |
| 2 | 5.92-8.76 | 5.5-8.4 | editor loads, page 1 appears, page strip | yes |
| 3 | 8.76-12.42 | 8.4-12.1 | page strip, "Page 2/3" tooltips, page 3 | yes |
| 4 | 12.42-16.82 | 19.7-23.1 | page 3 right-click menu opens, cursor goes to Download page | mostly: Share is not in the take; the Download page click lands at ~17.3 |
| 5 | 16.82-25.46 | 23.1-29.5 | download panel slides in, PDF panel, file type list opens ~22.3 (PNG/PDF/MP4 rows) | mostly: list appears at "MP4", not at "PNG or JPG" |
| 6 | 25.46-27.98 | 29.5-31.4 | PNG chosen, options with Select pages control | partly: no separate dropdown in the take |
| 7 | 27.98-31.3 | 31.4-33.9 | zoom on Select pages, cursor on "This page (3)", Custom clicked | yes |
| 8 | 31.3-36.8 | 33.9-36.2 | Custom page checklist, Select all, ranges | yes |
| 9 | 36.8-40.46 | 36.2-40.7 | pages cleared (error), page 3 ticked | yes |
| 10 | 40.46-44.4 | 40.7 hold, 40.7-41.6, 41.6-45.4 | only page 3 included, Download clicked at 43.1, download toast | yes |
| 11 | 44.4-47.18 | 45.4-48.0 | toast, star.png opens | yes |
| 12 | 47.18-53.54 | 55.5-58.3, 48.3-50.9 | PDF viewer (one page), then the PNG with only the artwork | yes |
| 13 | 53.54-56.32 | 22.4-24.5 (reuse) | Download page click, panel slides in | related |
| 14 | 56.32-61.82 | 9.6-12.2, 30.1-31.7 (reuse) | page thumbnail clicks in the editor, then download menu page selection | related |
| 15 | 61.82-65.22 | 35.6-38.2 (reuse) | Custom page selection before Download | related |
| 16 | 65.22-69.94 | 26.0-29.6 (reuse) | file type dropdown and list | related |
| 17 | 69.94-76.8 | 29.6-32.0, 24.2-27.0 (reuse) | PNG options, panel / type list | related |
| 18 | 76.8-82.9 | 15.1-19.9 (reuse) | pages view in the editor | related |
| 19 | 82.9-90.08 | 30.6-36.1 (reuse) | Select pages control, Custom pages | related |
| 20 | 90.08-95.2 | 58.5-62.4 | PDF page viewer, closing | yes |
Frames at each line's start and middle were checked in preview.mp4 and final.mp4 (same plan).

## Uncertain
See work/sync-notes.md: no Share click, no separate page-selection dropdown, the file type list opens later than "PNG or JPG" because the take has too little source at >=0.75x for L4-L10.

## Check these
- 12.4-17.5: page menu and Download page (no Share in the take).
- 22-24: file type list vs. "MP4 for animation".
- 40.4-43.1: hold on page 3 ticked, then the Download click at 43.1.
- 47.2-53.5: PDF then image (jump back, cross-fade at 50.4).
- 53.5-90: reused footage (L13-L19).

## Lessons added
One entry in docs/lessons.md.
