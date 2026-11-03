# script-09 report (re-edit)

## Result
- `projects/script-09/output/final.mp4`, 101.6 s, 2560x1440, **verify PASS** (duration, streams, resolution, frozen spans, black frames at 36 joins).
- freezedetect (n=0.003, d=1.2) on final.mp4: longest still **2.33 s (the opening)**, next 2.27, 2.13, 2.1, 2.1, 2.03 s. Nothing over 2.5 s. No held frames, no zooms, no ripples. check.py --plan: no `pace:` warnings.
- Speeds 0.82-1.31x (every group; no static piece above ~2x).

## Stages
- probe, transcribe, align (21 lines), scenes, frames: reused (already current).
- analyze: redone by hand. Looked at the take on 2.5 s sheets, then 0.5-1 s sheets at every step; moving spans and what each shows are in `work/analyze-notes.md`; landmark actions in `work/actions.json` (approximate coordinates, no click log).
- sync: hand plan `work/hand_plan.py` -> `work/plan.json`, built per line from the table below (not from recording order).
- Preview rendered 4 times, final 4 times (3 re-renders from frame review); each time frames at every line start/middle were read (final.mp4 frames, `work/frames/v*.jpg`).

## Judgment calls
- Opening trimmed: static home 2.9-5.13 played as one 2.3 s piece (was 2.5+ s), then the home zoom 5.13-7.9, so nothing at the start is still for more than 2.33 s.
- Every line starts exactly on its lines.json start; footage chosen by what it SHOWS. The take was recorded in a different order than narrated at several points (cutouts folder, inspect, selected-photo method, limits), so source jumps back/forward with 6-frame cross-fades on 30 of the 34 joins.
- Typing in the Create-folder name field is invisible to freezedetect (2.6 s "still" in the first final): removed 1 s of typing (15.2-16.2).
- Dead time fast-forwarded or skipped, not held: upload progress (34-39), toast waits (37-48.7, 73.5-84.2), menu hover (56.6-66.2), long cursor-only spans.
- Blank "loading" frames cut: editor loading (130.6-131.0), PNG viewer loading and white flash (238.0-238.35, after 239.3).
- Lines with no matching footage (see table): L3 (concept), L17-L20 (limits; the recording never shows a 50-image limit or a library photo). Nearest real UI is used and marked "partly".

## Per-line table (verified on final.mp4 frames at line start and middle)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1-2 "Script 9 / How to remove backgrounds in bulk" | 0.00-5.48 | 2.9-5.13 (2.3 s), 5.13-7.9 | Canva home, then zoom to the design categories / cursor to Projects | yes |
| 3 "This tutorial shows you how to remove several photo backgrounds" | 5.48-11.38 | 91.7-94.3, 105.1-108.3 | Edited folder with three cutouts, first cutout opened in the viewer | partly (conceptual, shows the result) |
| 4 "Start from the homepage and open projects" | 11.38-14.54 | 8.0-9.17, 10.6-12.4 | Projects click, All projects page, Add new menu opening | yes |
| 5 "Create a folder ... upload your images" | 14.54-19.78 | 12.6-15.2, 16.2-19.5 | New folder, "Create a folder" dialog, name "bg-remover" typed, Create folder | yes (upload shown in L6-L7) |
| 6 "Use a small test batch first" | 19.78-22.12 | 21.0-22.3, 24.2-25.5 | Folder created, opens empty, Add new > Upload files | partly (concept line, upload step shown) |
| 7 "Product photos with clear edges..." | 22.12-27.74 | 28.6-34.2 | File picker, Gallery with the portrait photos, 3 selected, Open, upload starts | yes |
| 8 "Return to the folder listing, hover, three-dot menu" | 27.74-32.64 | 50.0-56.6 | Back to All projects, folder row, hover, three-dot menu opens (menu lands ~30.7 on "three-dot menu") | yes |
| 9 "Select remove background" | 32.64-35.02 | 66.35-68.5 | Cursor on BG Remover in the menu at ~33.3 ("remove background"), click | yes |
| 10 "Canva processes ... creates a separate folder" | 35.02-41.34 | 68.5-73.5 | "Removing 3 backgrounds" toast, "bg-remover - Edited" folder appears, "Removed 3 of 3" | yes |
| 11 "The new folder name includes edited ... original stays" | 41.34-45.78 | 73.5-75.7, 84.23-85.0, 86.6-88.4 | Folder list with both bg-remover - Edited and bg-remover, cursor to the Edited folder | yes |
| 12 "Open the edited folder and check each cutout" | 45.78-49.1 | 88.4-91.7 | Zoom on Edited folder, click, folder opens with three cutouts | yes |
| 13 "Look closely around hair, transparent objects, thin straps" | 49.1-56.32 | 108.3-111.2, 123.0-128.0 | Close-up of a cutout's hair, then the cutouts folder and the second cutout (phone, strap) | yes |
| 14 "open the original folder, tick, BG remover from the toolbar" | 56.32-65.7 | 149.8-150.6, 152.1-153.57, 155.1-160.5 | Original folder, photo ticked (~60.2), bottom toolbar, BG Remover clicked (~62.6), toast | yes |
| 15 "adds the edited copies to the same folder" | 65.7-69.9 | 160.5-163.8, 176.2-178.0 | Same folder now with a fourth (edited) photo and toast, zoom on the photos | yes |
| 16 "check which versions you are opening before placing into a design" | 69.9-74.58 | 129.0-130.6, 131.0-133.5 | Cutout preview with "Open in editor", editor opens with the cutout | yes |
| 17 "Here's the important limit" | 74.58-76.38 | 178.0-179.8 | Profile menu open | partly (nearest real UI) |
| 18 "up to 50 images ... eligible paid plan" | 76.38-82.7 | 181.4-186.6 | Plans and pricing in the menu, pricing page (~81.3 on "paid plan") | partly |
| 19 "library photos or complete designs ... not processed" | 82.7-89.1 | 202.0-208.3 | Folder with photos, All projects with Recents / Designs | partly (no footage of the limit itself) |
| 20 "If the folder option is unavailable, reduce to 50 images" | 89.1-95.7 | 210.97-214.4, 190.2-192.7 | Folder three-dot menu with BG Remover option, folder with the photos | partly |
| 21 "Use the cutouts in a new design or download as transparent PNGs" | 95.7-101.61 | 133.5-135.7, 231.2-233.0, 234.0-235.8, 238.35-239.3 | Editor with the cutout, three-dot > Download, browser download list, transparent PNG viewer (~100.5) | yes |

## Uncertain
- Click coordinates in actions.json are approximate; check.py reports 16 "not tied to a narration word" warnings because plan.sync is empty (clicks are not frame-exact and no ripples/zooms are planned).
- L17-L20: the recording has no footage of the 50-image limit, library photos or reducing the folder; nearest UI used.

## Check these
- 0:00-0:05 opening (2.3 s still on the home screen, then zoom).
- 0:14-0:20 typing is slow to see (only the name field changes).
- 0:33 BG Remover click lands on "remove background".
- 1:14-1:29 limits lines use topic-matched footage (profile menu, pricing, All projects).
- 1:36-1:41 download menu, list, PNG viewer.

## Lessons added
- script-09 re-edit entry in docs/lessons.md.
