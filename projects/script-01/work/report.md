# script-01 report

## Result
`projects/script-01/output/final.mp4` - 96.167 s (voiceover 96.177 s), 2560x1440 (verify's expected size; probe.json lists the recording as 1920x1080 - not investigated), **verify PASS** (duration, streams, resolution, no frozen spans, no black frames at 35 joins).
`check.py --plan`: 0 errors, 6 warnings, none of them `pace:` (all pace warnings fixed, see below).

## Stages
- probe, transcribe, align (25/25 lines ok), scenes, frames: **reused** (already current).
- analyze: ran (no click log: times read from contact sheets, ±0.3 s). `check.py --actions` OK.
- sync: ran -> `plan_builder.py`, then `work/intro_patch.py` (hand patch, see below). `check.py --plan` OK.
- preview: rendered and reviewed on a 33-frame join sheet (cross-fades clean, no garbage/black frames, no wrong zoom since there are none).
- final render + verify: PASS.

## Judgment calls
- **Audio order followed.** The background colour (src ~32 s) is shown at line 5 although it was recorded before Elements/rectangle; every other step is shown at the words that name it. Each reorder/skip is a cross-fade whose pieces are >= 0.5 s at ~1x.
- Pacing: all footage plays at 0.8-1.5x (one stretch 1.39x on the finished preview, the rest ~1.0x), no speed over 2x, no hold at all, no piece under 0.5 s. In-scene dead time was skipped by cross-fade jumps rather than fast-forwarded above 2x.
- **Intro**: the recording opens with 7.8 s of a frozen home page (would be a 6.5 s frozen stretch). `work/intro_patch.py` replaces the first 3.6 s with the finished film strip moving (src 347.4-351.0), then cross-fades to the real start (src 5.2). plan.json therefore carries a hand edit; re-run the patch after every `plan_builder.py` run (use `--force`).
- **No zooms, no ripples**: no click log, cursor coordinates are estimates (and the recording already contains the screen recorder's own zoom/pan), so a zoom or ripple could land in the wrong place.
- Two of the three photo drops are shown (A14, A15); A16 (third drop) and A13 (Uploads tab) are unanchored because the narration covers all three drops in ~3 s.
- Skipped source: typing "black rectangle" (38-47), browsing 60-70, 176-203 photo browsing, 209-237 white-square search, 322-342 path settings, 351-361 idle.
- Cut-ish junk 156-166 (photo dropped on the page, undone) was flagged ff; builder skipped it.

## Uncertain
- All action times are from contact sheets, not a click log; x/y are rough (low/medium). Photo drop times (A14-A16), square duplicate/row copy (A19, A20), path drawing/Done (A25, A26) and scene-length drag (A28) are low confidence.
- Recording has no click on Download/MP4 and no playback of the downloaded file; those narrated steps have no footage (the closing shot is the Download dialog, static ~5 s at the end - verify did not flag it).
- Results of A15/A20/A24/A25 appear up to ~1.2 s after their narration line ends.

## Check these
- 0.00-3.6 s: finished film strip intro really moving, then fade to the home page.
- 19.2 s: background colour step (grey swatch) matches "different color".
- 33.7-37.7 s: the two photo drops; photos in the frames afterwards.
- 43-47 s and 49-56 s: white square, duplicates, perforation rows.
- 63-73 s: Animate -> Create an Animation -> path drawing.
- 90-96 s: Share / Download dialog.

## Lessons added
None (no render had to be redone for a mistake).
