# script-06 — Canva watermark tutorial

## Result
`projects/script-06/output/final.mp4` — 93.316 s (voiceover 93.317 s), 2560x1440 delivered, 30 fps.
**verify: PASS** (duration, streams, resolution, frozen spans, black frames at joins). `check.py --plan`: OK, no `pace:` warning.
Final freezedetect (n=0.002, d=1.5): 1.8-3.6 s (1.8 s, faded logo, cursor-only), 3.8-5.9 s (2.1 s, static opening of the take), 11.2-13.4 s (2.2 s, typing in the text box and slow panel). All under 2.5 s.

## Stages
- probe / transcribe / align (19 lines, all `ok`, L10 match 0.8, L17 0.923) / scenes / frames: **reused** (not re-run).
- analyze: no actions.json — footage was mapped by hand from 1 s contact sheets (project's hand-plan workflow, `work/hand_plan.py` regenerates plan.json). The old hand_plan.py/plan.json were for a different 96.967 s voiceover and were rewritten.
- sync: `work/hand_plan.py` -> `work/plan.json` (19 groups, one per line, 0.79-1.41x, no zooms/ripples: the recording already carries its own zoom moves).
- preview: 2 renders (first had a 2.6 s opening freeze and a 2.0 s typing freeze; shortened). Final render ~4 min, verify PASS.

## Judgment calls
- Audio order followed. Source jumps (cross-faded) wherever the take did things in another order: L8 position (src 96-101) comes before L9 transparency (src 80-85), L12 uses text footage (src 116-120).
- Dead time fast-forwarded, not cut, where short: uploads panel loading (L6 1.41x), download panel loading (L15 B2 1.7x). Cut with cross-fade (>3x): static page 3 (src 167.8-174.4), panel hovering (src 181-191), add-heading wait (src 10.2-13.5, 15.3-19.8), font panel idle (src 36.6-52).
- L1 intro opens on the faded-logo result (src 109.6-113.4) so the first seconds are not a 4+ s blank page; then the real blank opening (2.1 s) leads into the page click at src 6.3 -> out 5.9 ("Open the ... design").
- No zooms/ripples (the take has its own recorder zoom; extra zoom made movement harder to follow).
- The recording has no photo (blank square page, logo/“Crack IT” text only) — script says "photo"; the footage cannot show one.

## Per-line table (frames checked in final.mp4)
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 intro | 0.0-5.4 | 109.6-113.4, 3.9-5.8 | faded logo watermark on page, then blank design | yes (concept) |
| 2 open design | 5.4-8.0 | 5.8-8.3 | blank design page gets selected (src 6.3 -> out 5.9), toolbar appears | yes |
| 3 press T, type | 8.0-13.4 | 8.3-10.2, 13.5-15.3, 19.8-22.8 | T clicked, text panel, "Add a heading" placed, typing "Crack IT" | yes (typing ends ~12 s, "type your name" is 10.3-12.5) |
| 4 font | 13.4-17.4 | 31.5-36.6 | font dropdown, Archivo Black picked | partly (colour not yet shown at word "colour") |
| 5 white / dark gray | 17.4-21.9 | 52.6-58.4 | text selected, colour panel, picker light -> dark grey | yes |
| 6 Uploads | 21.9-25.8 | 68.0-73.5 | Uploads panel opens, images list | yes |
| 7 transparent logo | 25.8-33.1 | 73.6-81.0 | logo clicked in Uploads, placed, centred on the page | yes |
| 8 position | 33.1-37.7 | 96.2-101.5 | logo (already faded) dragged with centre guides | yes (logo faded, not black: take did transparency first) |
| 9 select, Transparency | 37.7-43.5 | 80.6-85.4 | logo selected, Transparency slider opens (100) and is reduced to ~31 | yes |
| 10 ~30 % | 43.5-47.0 | 103.2-107.2 | slider adjusted around 22-50 on faded logo | yes |
| 11 rotation | 47.0-51.3 | 120.8-125.0 | text rotated with the handle | yes |
| 12 signature near corner | 51.3-55.1 | 116.0-119.8 | small grey "Crack IT" text with its Transparency slider | partly (no take footage of a small signature in a corner) |
| 13 copy to another design | 55.1-60.0 | 145.6-151.8 | logo selected, "..." menu, scroll to new page | partly (copy/paste itself is only a menu hover) |
| 14 separate design, light/dark | 60.0-66.1 | 152.0-153.8, 157.7-161.3 | new page with logo, then the text version / design title | partly |
| 15 separate page, Share, Download, PNG, transparent bg | 66.1-75.9 | 164.4-167.8, 175.4-177.0, 178.4-181.0, 191.2-194.7 | rotated text -> page 3 with logo only, Share, Download panel, Transparent background toggled on (~75.4 out) | yes (toggle lands ~0.4 s after the words) |
| 16 paid plan | 75.9-78.7 | 194.7-196.9 | download panel with transparent background on and a quality tip | partly (take shows no paid-plan notice) |
| 17 element transparency | 78.7-84.8 | 216.0-221.0 | logo selected, Transparency slider moved (50 -> 60) | yes |
| 18 transparent background | 84.8-87.6 | 228.5-230.9 | Download panel, Transparent background on | yes |
| 19 download PNG/JPG | 87.6-93.3 | 204.2-206.6, 229.7-231.8 | Download clicked, then file-type list with JPG/PNG | yes |

## Uncertain
- L4/L12/L13/L14/L16: take lacks exact footage (see "partly").
- The static opening (2.1 s) is real source (take starts idle 0-6.3 s).

## Check these
- 11.2-13.4 s: typing; text change is small, freezedetect counts it as still but it is real typing.
- 33.1-37.7 s vs 37.7-43.5 s: logo is faded in L8 and opaque in L9 (take order differs from narration).
- 75-76 s: transparent-background toggle timing.
- 66-68 s: starts on rotated text page, page 3 logo-only page appears about 69 s.

## Lessons added
- 2026-11-03 script-06 entry in docs/lessons.md (new voiceover for an existing take: rebuild the table).
