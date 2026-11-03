# script-08 report (foldable business card, 230.6 s take, 96.316 s voiceover, 1920x1080)

## Result
`projects/script-08/output/final.mp4` (2560x1440, 96.3 s). verify: **PASS** (duration, streams, resolution, no freeze over 3 s, clean joins). `check.py --plan`: OK, no `pace:` warnings. Preview freezedetect (d=1.5): longest 2.2 s, below the 2.5 s limit.

## Stages
- probe, transcribe, align (23 lines, all `ok`), scenes, frames: reused (already current).
- analyze / sync skills: replaced by `work/hand_plan.py` (the repo's established approach for these takes: freezedetect n=0.002 d=0.8 windows plus 8 contact sheets). No actions.json or sync.json was written. There is no click log, so no zooms or ripples (the recording has a baked recorder zoom).
- preview: rendered twice, 1 fix. Final render: ~3.6 min. verify: PASS.

## Judgment calls
- 23 per-line groups in narration order, speeds 0.80-1.24x, no holds. The whole video is fast-forwarded or slowed within 0.8-1.24x, never cut inside a scene. Jumps in the source carry cross-fades.
- Lines 1-6: the home screen is static for 0-3.2 s, so the opening uses only 1.2 s of it. Then Create a design > Custom size > 85 / 55 typing > blank sheet.
- L7-L9 (File > Rulers and guides, Add guides panel): src 43-57. L10: guides added and locked (62-65). L11/L12: selecting the lower and upper halves and the rotate handle (src 89-112).
- L13/L14: page two (src 137.8-146). L15-L16 (essential check, mock-up): conceptual, borrowed zoomed-out design footage (112-116).
- L17-L19 (print spreads, duplex, provider layout): no footage of printing exists. Borrowed the Share > Download panel (File type list, PDF settings, src 158-168.5).
- L20/L21 (remove fold line, guides do not print): File > Rulers and guides menu with Clear guides (src 67-74).
- L22: Share > Download, PDF, Print preset (src 204-212). L23: "File downloaded" notification (src 184-187).
- Fix round 1: the first preview had a 2.7 s frozen stretch in L3 (src 13.03-15.27 is static and was played at 0.83x). It is now a fixed 2.24 s piece at 1x and the moving source before it is spread over L1-L3 at 0.80x.

## Uncertain
- The take is 85x55 typed in the Custom size form, while the script says 85x110; the recording does not show 110 explicitly.
- The recording has no real footage of the printed mock-up, duplex settings or removing a drawn fold line; borrowed footage is the nearest panel (see above).

## Check these
- 10.7-14.5 s: Custom-size form with a 2.2 s near-still (cursor only).
- 31-35 s: template picked in the design (cross-fade before the File menu).
- 62.8-74 s and 74-82 s: borrowed footage for "essential check" and "print/duplex"; the visuals are an approximation.
- 91-96 s: the final cross-fades into the downloaded-file notification.

## Lessons added
None; no render had to be redone for a mistake, apart from the one preview fix recorded in the run log.
