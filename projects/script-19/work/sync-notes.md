# Sync notes (hand plan: work/hand_plan.py -> plan.json)
No click log and baked recorder zoom, so no anchors/zooms/ripples; each narration line gets the moving window (freezedetect n=0.003 d=0.8) that shows its step. 22 groups, 0.82-1.20x, no holds.

| line | out | source | what is seen |
|---|---|---|---|
| 1 | 0-7.2 | 11.2-13.7, 17.5-21 | Canva home zoom, Word manuscript |
| 2 | 7.2-10.9 | 21-24 | Word doc scrolls |
| 3 | 10.9-17.9 | 24-26.6, 31.9-35.5 | Word doc (headings/body) |
| 4 | 17.9-21.4 | 42.8-46.3 | Canva home + file explorer |
| 5 | 21.4-23.4 | 46.3-49.4 | Downloads folder with .docx |
| 6 | 23.4-27.1 | 94.9-100.9 | upload done toast, Open |
| 7-8 | 27.1-36.2 | 100.9-111.3 | imported doc in editor (check content) |
| 9 | 36.2-39.1 | 113.4-115.9 | imported doc, title being edited |
| 10 | 39.1-44.8 | 168.3-175 | Uploads/projects page, Create a design (no e-book template search in take) |
| 11 | 44.8-48.2 | 122.6-127.4 | retyping the title text (stands in for cover title) |
| 12 | 48.2-55.6 | 232-240 | text selected in imported doc to copy |
| 13 | 55.6-60.2 | 243-251.5 | doc text/scroll |
| 14 | 60.2-64.6 | 251.5-256.2, 228.3-229.6 | page/image scroll |
| 15-17 | 64.6-77.8 | 263-278.6 | uploads page, Create a design, upload files, file dialog |
| 18 | 77.8-83.1 | 286.5-290.7, 309.6-311 | doc page zoom |
| 19 | 83.1-88.1 | 204.2-207.3, 240-241.4 | doc text paste |
| 20 | 88.1-96.4 | 318.8-323.4, 333.7-339.8 | Download panel, PDF type |
| 21 | 96.4-99.7 | 366.7-369.9 | PDF downloaded, opens |
| 22 | 99.7-106 | 369.9-377.4 | PDF pages scroll |

## Judgment calls
- Skipped (static, cursor only): 0-11.2, 51-94.9 (upload wait, cut with cross-fade), 138-168, 195-204, 207-228, 290-309.6, 351-361.6. Skipped 115.9-120.9 (black box glitch).
- Footage order differs from the script in several places (audio order wins; jumps are cross-faded).
- No footage for: e-book template search/choose, cover title/author/image, chapter opening pages and page numbers, duplicate-a-page. Nearest steps borrowed (lines 10, 11, 14, 15-17).
- check.py --plan: OK; the 14 warnings are only "action not tied to a narration word" (no sync in a hand plan).
