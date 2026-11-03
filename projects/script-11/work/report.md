# script-11 — Canva Bulk Create from a Google Sheets CSV

## Result
- `projects/script-11/output/final.mp4`: 94.552 s, 2560x1440 (recording 1920x1080, delivered at 1440p), voiceover audio. **verify: PASS** (duration, streams, resolution, frozen spans, black frames at 40 joins).
- 22 narration lines, 40 pieces, all at 0.83-1.41x, no holds, no zooms (the recorder's own pan/zoom is already in the footage). `check.py --plan`: OK, no `pace:` warning.
- Longest still stretch in the final (freezedetect n=0.003, d=1.2): 2.07 s (src 49.9-53.0, column-width tweaks on the data rows, L3-L4 join); the others are 1.9 s (opening), 1.27 s, 1.7 s. All under 2.5 s.

## Stages
- probe, transcribe, align, scenes, frames: reused (already current; no re-transcribe). Voiceover is the cleaned one (94.552 s, 22 lines, all `ok`).
- analyze / sync: replaced by the hand plan `work/hand_plan.py` (the established recipe for these long recorder-zoomed takes; see lessons). Footage chosen from freezedetect (n=0.002, d=0.8) moving windows plus 1 s / 1.5 s contact sheets of every window, then checked on preview and final frames. No `actions.json`/`sync.json` was written.
- preview render + review sheets (every line start and middle): done, no fix round needed. Final render + verify: done.

## Judgment calls
- Follows the audio order; the take itself does everything in script order except that the result pages (opened after "Create 1 design") are shown earlier, at L15.
- Dead time is not cut: moving windows are played at 0.83-1.41x; the only jumps are cross-faded joins between windows of the same scene. Static source (the 1.0-2.8 s home screen, 3 s of column resizing) is used only as short runs at about 1x.
- Skipped on purpose: the blank Canva tab loading (src 95-97.4, 225.3-226.5), file-dialog loading, long idle stretches (e.g. 209-219 s, 303-310 s typing a new row, 332-351 s).
- No zooms, no ripples: baked recorder zoom (lessons rule).
- Frame size: output is 1920x1080 in plan, delivered 2560x1440 by the renderer.

## Per-line table (verified on preview and final frames)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0-6.74 | 1.0-2.8, 13.0-17.9 | Canva home, tab switch to Google Sheets, blank sheet | yes |
| 2 columns | 6.74-12.26 | 19.7-22.9, 27.3-29.6, 34.0-36.3 | Name, Offer, Website typed in row 1 (Name appears ~2 s before it is spoken) | yes |
| 3 one row per design | 12.26-15.18 | 44.7-46.6, 47.6-49.1 | cursor in row 2, data rows filled in | yes |
| 4 three rows | 15.18-18.92 | 49.9-53.0 | three rows (Glow Beauty Studio, Urban Cafe, Style Hub) with offers, columns widened | yes |
| 5 headings, no empty rows | 18.92-23.08 | 62.7-64.1, 70.1-71.6, 74.1-75.4 | table with headings in row 1, cursor on the empty rows below | partly (cursor only, nothing is removed in the take) |
| 6 File > Download > CSV | 23.08-28.84 | 82.9-85.0, 87.8-90.8 | File menu, Download submenu, Comma-separated values chosen (lands ~1 s after the words), download list | yes |
| 7 open template, text boxes | 28.84-34.04 | 92.6-94.9, 97.4-98.4, 101.8-104.9 | Canva home, template opens, text boxes Name/Offer/Website | yes |
| 8 shared items unconnected | 34.04-38.78 | 107.5-109.4, 112.7-115.0 | selecting the Website text, cursor over the template (no logos exist in this design) | partly |
| 9 Apps, Bulk Create | 38.78-41.30 | 129.5-130.7, 159.6-161.4 | Apps tab clicked, Bulk create in the app list, selected | yes |
| 10 Upload data, CSV | 41.30-45.34 | 167.0-171.6 | Upload data button, file picker, CSV selected | yes |
| 11 Match and fill | 45.34-49.30 | 171.6-173.6, 176.7-178.7 | Match and fill fields panel, fields placed on the text boxes | yes |
| 12 text box, Match data, column | 49.30-53.78 | 195.2-198.2, 200.3-202.6 | text box with Match data chip, Connect data list with the column ticked | yes |
| 13 repeat for remaining fields | 53.78-55.08 | 206.4-207.7 | Connect data list for the Website box | yes |
| 14 Name / Offer example | 55.08-61.86 | 178.9-185.0 | Match and fill panel with Name, Offer, Website chips on the matching text boxes (earlier in the take than L12-13) | partly |
| 15 preview, long entries | 61.86-65.32 | 233.6-237.0 | generated result pages (Urban Cafe, Style Hub with the long offer line) | partly (the take never clicks Preview; result pages are shown instead) |
| 16 adjust the template | 65.32-68.06 | 248.0-250.6 | result page 3 in the editor, then back to the template | partly |
| 17 creation options | 68.06-73.84 | 264.0-268.4, 270.0-271.3 | Advanced options panel with "1 design with multiple pages / 3 individual designs" | partly (take has "3 individual designs" selected) |
| 18 create, open result | 73.84-77.30 | 219.5-222.2, 224.0-225.2, 226.6-227.3 | Create 1 design clicked, "1 design created" toast, View design, result opens | yes |
| 19 CSV is a snapshot | 77.30-81.30 | 300.7-303.0, 310.3-312.3 | project folder, back to the Sheet, then the unchanged template tab | partly |
| 20 editing the sheet later | 81.30-86.76 | 324.7-330.8 | cells in the Sheet being edited (extra "mens club" row, offer changed) | yes |
| 21 download a new CSV | 86.76-90.76 | 351.6-355.6 | File menu, Download submenu, CSV, downloads list | yes |
| 22 plan requirement, desktop | 90.76-94.55 | 360.3-364.4 | downloads list, Canva home, editor with Bulk create template (no plan/desktop footage exists) | partly |

## Uncertain
- No footage for: removing empty rows, shared logos, a click on Preview, choosing "one design with multiple pages", a plan or desktop notice. Nearest steps are shown (marked partly above).
- L19 ends on the template, not the generated batch.

## Check these
- 15-16 s and 17-19 s: still stretch of about 2 s (column widths changing, cursor only).
- 25.5-27 s: CSV chosen about 1 s after "Comma-separated values".
- 76-77 s: cross-faded join from "View design" to the opened result (skips the blank loading page).
- 77.3 s: the L19 shot starts on the project folder with three designs (leftover from a second run in the take).

## Lessons added
- 2026-11-03 script-11 entry in docs/lessons.md.
