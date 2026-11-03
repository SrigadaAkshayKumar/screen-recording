# script-09 report — Canva bulk background remover (244 s take, 96.381 s voiceover, 17 lines)

## Result
- `projects/script-09/output/final.mp4` — 96.367 s, 2560x1440, **verify PASS** (duration, streams, resolution, frozen spans, 30 clean joins).
- `check.py --plan`: OK, no `pace:` warnings (first plan had one: 2.7 s still in L13, fixed). Groups play at 0.81-1.24x; the fixed static pieces play at <= 2x.
- Longest still in the *final* (freezedetect n=0.002, d=1.5): 2.13 s (L13, folder with the 4th photo, cursor only). Others 1.6-2.0 s.

## Stages
- probe / transcribe / align / scenes / frames: reused (already in work/). Gate B ok (17 lines).
- analyze + sync: not run as separate JSON stages. As in earlier runs of this repo (lessons.md), the plan is hand-built by `work/hand_plan.py`, one group per narration line, from 0.5-2.5 s contact sheets of the take. `actions.json` / `sync.json` therefore do not exist and `check.py --actions` was not run. No zooms/ripples (baked recorder zoom, no click log).
- preview rendered and reviewed (freezedetect + frames); final rendered and checked frame by frame; verify run.

## Judgment calls
- Audio order followed. Every line gets its own group starting at its lines.json start minus ~0.2 s.
- L1 (conceptual intro) opens on result footage (cutouts, src 123.8-127.9) and ends on the static Canva homepage as a 2.0 s fixed piece (src 0.6-4.1 at 1.75x), so the homepage is on screen when L2 says "homepage".
- Static (cursor-only) source is played as fixed pieces at <= 2x (L1 homepage, L9 src 86.0-88.6, L13 src 160.6-164.2) and the rest of those lines uses moving footage around them.
- The take barely moves between src 40-48, 73-81, 164-176 and 191-201; these spans are skipped, not stretched.
- Source jumps (all cross-faded) are only forward except L16, which returns to the profile-menu footage (181-184) for "check your plan access" and L13, which borrows the viewer/editor footage (119-122, 131-133).
- Mismatches between script and take: the take never shows a "50 image limit" or library-photo/design behaviour, so L14-L16 use the nearest panels (profile menu and Plans and pricing; All projects designs; the empty "Download designs (0)" dialog for "option unavailable"). The take also selects only one photo for the BG Remover toolbar step and then removes just that photo (4 photos result), which matches L12-L13.
- Cuts of src 150.1-153.3 (an accidental photo viewer opened from the folder) in L12.

## Per-line table (frames taken from final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-5.9 | 123.8-127.9, 0.6-4.1 | edited cutouts (folder/viewer), then Canva homepage | yes |
| 2 | 5.9-9.1 | 5.9-9.1 | homepage, sidebar Projects click (~8.2 src = out 8.2, word "Projects" 8.1), All projects loads | yes |
| 3 | 9.1-14.3 | 12.4-14.4, 16.9-18.9, 24.5-25.8 | Add new > New folder, Create-a-folder dialog with name, Add new > Upload files | yes |
| 4 | 14.3-16.5 | 30.6-32.8 | file picker with three images selected | yes |
| 5 | 16.5-22.3 | 34.2-40.0 | three uploaded portraits (uploading bars, then "3 items uploaded") | yes |
| 6 | 22.3-27.2 | 50.1-56.2 | folder -> All projects, folder hover, three-dot menu opens | yes |
| 7 | 27.2-29.1 | 66.9-69.2 | cursor on BG Remover in the menu, click (~out 27.95) | yes |
| 8 | 29.1-35.9 | 69.2-74.7 | "Removing 3 backgrounds", "Removed 3 of 3", bg-remover - Edited folder appears | yes |
| 9 | 35.9-40.4 | 84.2-89.4 | folders list: bg-remover - Edited and original bg-remover, zoom on the names | yes |
| 10 | 40.4-43.7 | 89.4-92.8 | edited folder clicked, opens to three cutouts | yes |
| 11 | 43.7-50.2 | 105.3-113.0 | cutout opened in viewer, zoom on hair edge | partly (zoom on one face only; no transparent objects/straps in the take) |
| 12 | 50.2-60.3 | 148.0-150.1, 153.3-160.6 | original folder, tick on third photo, bottom toolbar, BG Remover click (~out 58.2) | yes |
| 13 | 60.3-69.2 | 160.6-164.2, 175.8-177.2, 119.2-122.2, 131.0-133.3 | folder now has 4 photos (edited copy added), zoom on file names, open a cutout, Canva editor | partly (64-65 s a 1 s blank "loading" page while the viewer opens) |
| 14 | 69.2-76.9 | 177.4-181.0, 184.2-187.6 | profile menu, Plans and pricing page | partly (no 50-image limit shown in the take) |
| 15 | 76.9-83.7 | 202.9-209.0 | folder -> All projects with Folders and Designs sections | partly (illustrates folders vs designs, nothing is processed on screen) |
| 16 | 83.7-90.3 | 213.8-216.6, 181.0-184.2 | "Download designs (0)" dialog loading, profile menu hovering Plans and pricing | partly (nearest footage; no 50-image reduction in the take) |
| 17 | 90.3-96.4 | 230.0-235.8 | edited folder, three-dot menu, Download click (~out 93.0), browser download list | yes |

## Uncertain / Check these
- 64-65 s: blank loading page (partly). 83.8-85 s: dialog still loading skeleton. 
- 43.7-50 s (L11): static zoom on the face ~1.6 s twice.
- L14-L16 are illustrative footage, not the exact narrated limits.
- No analyze-notes.md / sync-notes.md (hand plan).

## Lessons added
- See docs/lessons.md (script-09 re-edit with the 96.381 s voiceover).
