# script-02 report

## Result
- `projects/script-02/output/final.mp4`, 92.322 s (= voiceover), 2560x1440, **verify PASS** (duration, streams, resolution, 0 freezes >3 s, 36 join boundaries clean).
- `check.py --actions` OK, `check.py --plan` OK with **no pace warnings** (groups 0.83-1.29x, one 2.0x opening piece, all pieces >= 0.56 s, no holds).
- Preview freezedetect (n=0.002, d=1.0): opening 2.2 s (static home screen at 2x), 55.9-58.0 s 2.07 s (typing the cube prompt: only the text box changes), 19.8 s 1.3 s, 80.6 s 1.3 s. All under 2.5 s. Static spans in the source are never played slower than 1x.

## Stages
- probe, transcribe, align (all 18 lines ok, match 0.94-1.0), scenes, frames: **reused** (already current).
- analyze: ran by hand from 8 sheets plus 14 finer 0.5-1.5 s sheets -> `work/actions.json` (13 click actions, placeholder coordinates because the take has baked recorder zoom), `work/analyze-notes.md`.
- sync: no plan_builder run. Hand plan `work/hand_plan.py` (per-line groups starting on each lines.json start, slack only inside a group), as in earlier baked-zoom takes. No zooms or ripples (baked zoom).
- preview render, final render (4 m 45 s), verify: ran once each; no fix round on the render itself. The plan needed 3 tuning iterations in check.py (click-to-word within +-0.15 s).

## Judgment calls
- Audio order followed. Dead time fast-forwarded (at most 2x), never held; long still stretches (static home 1.3-6.2, idle 121-134, 135-147, 192-205 etc.) were skipped, not played.
- The take has only ~100 s of motion for a 92 s voiceover, so several lines borrow the closest footage (marked partly below).
- Skipped: the Shapes detour (28-32 s), the duplicate-sphere mess (60-66 s), the sphere-prompt generation wait, the idle waits.
- Clicks tied to words: Create 5.9 (Open), Elements 9.0, 3D category 12.1, sphere add ~17.9 ("add"), colour swatch 28.4 ("click"), blue chosen ~30.3, heading ~38, Magic Media 48.9, 3D tab 50.2, Generate 54.1, cube Generate ~59.0, Share 72.8, Download 73.8.

## Per-line table (frames from final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0-5.82 | 0-5.1 (2x), 7.0-9.9 | Canva home, cursor to Create, zoom to sidebar | yes |
| 2 | 5.82-10.24 | 10.0-13.8, 18.4-20.3 | Create a design menu, blank design opens, Elements clicked, categories panel | yes |
| 3 | 10.24-15.1 | 25.5-26.1, 32.0-34.6, 44.4-46.4 | Browse categories, cursor to 3D, 3D panel opens, search box clicked | yes |
| 4 | 15.1-19.44 | 47.5-50.2, 51.8-54.0 | "sphere" typed, results, yellow sphere added to page | yes |
| 5 | 19.44-22.52 | 56.2-58.3, 59.1-60.9 | red sphere selected, dragged on page | partly (a move-drag; no clean viewing-angle drag on this sphere) |
| 6 | 22.52-25.8 | 67.0-70.4 | sphere enlarged/resized | partly (resize yes, positioning beside text not shown) |
| 7 | 25.8-31.72 | 94.26-100.0 | toolbar colour swatch, Colour panel, blue chosen | yes |
| 8 | 31.72-36.6 | 97.2-99.6, 99.8-101.0, 105.2-106.8 | 3D colours panel again (reuse, cross-faded), blue sphere | partly (no footage of "keep original materials") |
| 9 | 36.6-41.14 | 109.0-113.0 | Text tab, Add a heading, heading on page | yes |
| 10 | 41.14-45.68 | 113.0-114.3, 116.3-120.4 | heading typed "Sphere" below the blue sphere | yes |
| 11 | 45.68-48.3 | 148.4-151.0 | Apps panel opens | yes |
| 12 | 48.3-55.54 | 153.9-155.3, 163.8-165.0, 168.2-170.9, 172.9-175.0 | search Magic Media, 3D tab, describe field, Generate 3D | yes |
| 13 | 55.54-60.38 | 202.4-205.0, 207.2-209.2 | orange cube prompt typed, Generate 3D clicked | yes |
| 14 | 60.38-66.62 | 233.5-236.2, 237.4-241.0 | generated cube results, cube added to page | partly (concept line) |
| 15 | 66.62-71.78 | 263.9-269.0 | 3D tab panel with cube, cursor on page | partly (no footage of returning to 3D category after a flat item) |
| 16 | 71.78-75.42 | 290.0-293.5 | Share, share panel, Download | yes |
| 17 | 75.42-85.6 | 293.5-294.5, 295.3-298.0, 302.2-307.0 | Download panel, file type list (MP4/GIF/PNG), Download button | partly (no footage of interactive presentations/websites) |
| 18 | 85.6-92.32 | 246.2-252.8 | Play pressed on the cube, preview, drag | yes |

## Uncertain
- Lines 5, 6, 8, 14, 15, 17 borrow nearest footage (see table). Line 5 shows a move-drag, not a rotation; rotation footage exists only for the blue sphere (105-108) and cube (250-262).
- The 2.07 s near-freeze at 55.9 s is typing (cursor-free, small text change).
- actions.json coordinates are placeholders; no zoom/ripple uses them.

## Check these
- 12.1 s: 3D category click, 17.9 s sphere added, 28.4 s colour click, 54.1 s Generate, 59.0 s cube Generate.
- 19.4-22.5 s (drag, not rotate), 31.7-36.6 s (reused colour panel).
- 46-48 s: taskbar visible in the Apps sidebar click.

## Lessons added
- None (no render was redone because of a mistake).
