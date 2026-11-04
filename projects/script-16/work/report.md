# script-16 — Canva Brand Kit tutorial

## Result
- `projects/script-16/output/final.mp4`, 93.089 s (= voiceover), 2560x1440, 30 fps. **verify: PASS** (duration, streams, resolution, frozen spans, black frames at joins).
- 21 groups (one per narration line, plus a few multi-piece lines), 0.82x–1.28x, no `pace:` warning from `check.py --plan`.
- Longest still stretch in the final (freezedetect d=1.7): 2.1 s at 44.5 s (colour picker, blue being chosen) and 1.77 s at 82.6 s. Both under the 2.5 s limit.
- Final frames checked at 12 points (sheet `fin_01`); the other lines were checked on the preview, which uses the identical plan.

## Stages
- probe, transcribe, align, scenes, frames: **reused** (alignment from the earlier run; transcription not repeated).
- analyze: as in script-03/05/15, a hand plan from 1 s contact sheets (`work/hand_plan.py`) plus `freezedetect` on the source (`work/freeze_src.txt`). `actions.json` is a stub with no actions (no click log, recorder zoom is baked into the take), so `check.py --actions` reports "needs a non-empty actions list". This is expected; no zooms or ripples are planned.
- sync: `hand_plan.py` -> `plan.json`; `check.py --plan` OK.
- preview (40 s) reviewed; final render ~5 min; verify PASS.

## Judgment calls
- Audio order is followed. Pieces are cross-faded wherever the source jumps.
- The take is 249 s; every static source window (home screen 0-9 s, brand kit 11-15 s, colour suggestions 59-67 s, fonts list 137-143 s, 223-235 s) was left out, so nothing is cut inside a moving step.
- L1 (intro) uses logos->colours and fonts footage instead of the 9 s static homepage.
- L7 (filenames) re-uses the file-picker footage (43-45 s) because that is the only place filenames are visible.
- L11: take shows yellow and blue (green was a discarded first pick at 79-82 s, skipped); no dark-text or light-background colour exists in the take.
- L16: "open a design" = home -> new design (149 s) + editor Brand click (158 s). L17 uses four short pieces (kit, logo, colours, fonts) because the take adds logo/colours/fonts in separate stretches.
- L18/L19/L20 have no dedicated footage (plan/role limits, older designs): borrowed Brand Controls menu, Publish Brand Template dialog, and the plain design.
- No zooms, no ripples (recorder zoom already baked in; no click log).

## Per-line table
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0–5.89 | 57.0–59.6, 106.9–109.4 | logos page -> Colours click; Fonts page | yes |
| 2 open Brand | 5.89–8.23 | 9.0–11.4 | home, sidebar Brand click, Brand Kit page loads | yes |
| 3 dropdown / create kit | 8.23–14.55 | 17.3–20.9, 22.4–26.9 | dropdown, Create new Brand Kit, name "test", Create | yes |
| 4 Logos | 14.55–16.15 | 36.5–38.3 | click Logos, empty Logos page | yes |
| 5 Add to category / upload | 16.15–22.01 | 39.8–46.6 | Add brand assets, menu, Upload files, file dialog, logo uploaded | yes |
| 6 main/light/dark logos | 22.01–26.25 | 47.0–52.2 | second upload, file dialog, two logos | yes |
| 7 filenames | 26.25–28.69 | 43.0–45.2 | file picker with filenames (re-used) | partly |
| 8 open Colors | 28.69–32.35 | 56.8–59.8 | Colours click, Colours page | yes |
| 9 add palette | 32.35–35.37 | 68.4–71.5 | Add new colour, picker opens | yes |
| 10 hex codes | 35.37–39.65 | 71.5–75.8 | picker with hex field, first colour set, second added | yes |
| 11 blue/dark/light colours | 39.65–45.53 | 82.4–88.0 | yellow then blue chosen | partly (no dark/light colour in take) |
| 12 name palette | 45.53–48.23 | 88.0–90.5 | finished palette, hex labels | partly (no naming action) |
| 13 open Fonts | 48.23–51.63 | 101.8–105.0 | Fonts click, Fonts page | yes |
| 14 typefaces/sizes/save | 51.63–56.93 | 106.8–113.0 | font dropdown, Title/Subtitle type + size | yes (save tick not shown) |
| 15 custom font upload | 56.93–63.51 | 128.4–134.0 | Manage uploaded fonts, Uploaded fonts dialog, file picker | yes |
| 16 open design, Brand | 63.51–67.41 | 149.0–151.2, 158.3–160.6 | home -> new design; Brand in editor panel | yes |
| 17 kit/logo/colours/styles | 67.41–72.75 | 166.8–168.6, 196.0–197.4, 207.4–208.8, 214.8–216.2 | kit dropdown; logo placed; colours panel; fonts panel | yes |
| 18 plan/role limits | 72.75–79.13 | 168.4–171.3, 172.9–175.2 | kit dropdown with Brand Controls, Brand panel | partly |
| 19 team admin | 79.13–84.31 | 181.4–186.6 | Brand templates, Publish Brand Template dialog | partly |
| 20 older designs | 84.31–89.95 | 188.0–193.6 | plain existing design, no brand styling | partly |
| 21 apply assets | 89.95–93.09 | 200.4–203.5 | Brand panel in design, Colours | yes |

## Uncertain
- Lines 7, 11, 12, 18–20: take lacks the exact gesture (see table).
- The recording has two Brand Kits ("test" and "nike"); kit names appear mid-video.

## Check these
- 26.25–28.7 s (file picker re-used for "filenames").
- 44–46 s (colour picker nearly static, 2.1 s).
- 82.5–84 s (borrowed old-design footage).

## Lessons added
None; first preview and final passed without redo.
