# script-09 report

## Result
output/final.mp4 — 95.666 s, 2560x1440 (delivered height), verify PASS (0 freezes >3 s, 28 joins clean). check.py --plan clean, no pace warnings. Preview freezedetect (d=1.2): only the 2.4 s static opening.

## Stages
- probe, transcribe, align (all 20 lines ok), scenes, frames: reused (already current).
- analyze: skipped as actions.json — hand plan from freezedetect windows + contact sheets (check.py --actions not applicable).
- sync: work/hand_plan.py -> plan.json. Preview + final render + verify: ran.

## Judgment calls
- 20 per-line groups at 0.86-1.31x, audio order followed, no cuts of in-scene dead time except static spans >2.5 s (0-12.3, 28-35.5, 53-62, 68.8-72.3, 80.9-83.8, 195-202) which are skipped; no holds, zooms or ripples (recording has recorder zoom baked in, no click log).
- L1: 2.4 s static home screen, then the finished phone preview (208.8-214.3) as a topic match.
- L2-L6 follow the real steps: Preview, mobile toggle, publish panel/Settings, Resize on mobile, back to the design.
- L7-L17 matched by topic: text-box resize (123-133), grouping (84-94), preview again (96-99), replace image (109-115), buttons (155-159), large image (159-166).
- L18-L20: full-screen phone preview and scrolling (202-222).
- Footage 208-214 reused in L1 and L19 (cross-faded).

## Uncertain
- Steps with no dedicated footage: shortening headings, spacing, "avoid grouping all" and the approximation lines are illustrative matches.

## Check these
- 2.4-7.9 s: phone preview used as intro.
- 41-53 s: grouping/preview-again footage is by topic.
- 63.8-68 s: contact-button footage has some low-motion moments (<1.7 s).

## Lessons added
- script-09 entry appended to docs/lessons.md.
