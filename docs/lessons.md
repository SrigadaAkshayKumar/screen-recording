# Lessons

Read before every run. Add an entry whenever a mistake cost a render (or would have).
Format: date, symptom, cause, rule.

## Known pitfalls (found while building the pipeline)

- **2026-10-10. A hold froze on the frame *before* the UI responded.** Cause: the hold point was
  snapped back to the click when `t_result_visible` was within a frame of it. Rule: hold only at or
  after `t_result_visible` (plan_builder holds `--settle` 0.15 s after it and only snaps forward).
  When reviewing a preview, check that every long hold shows the response.
- **2026-10-10. A zoom hid the result.** The Settings panel opened outside the zoomed frame, so the
  zoom peak showed the button but not what it did. Rule: when the result appears away from the
  click, give the zoom `include: [[x, y]]` for the result, or don't zoom.
- **freezedetect ignores cursor-only motion.** A stretch where only the cursor moves counts as
  "frozen". verify.py doesn't count frozen spans inside planned holds and scenes.py still spans,
  but if you change scenes.py thresholds, re-run scenes.py before verify.
- **cv2.imwrite fails silently on non-ASCII Windows paths.** Always use `common.save_jpg`.
- **Logged click times can be 1-2 frames late.** scenes.py estimates the logger offset from UI
  responses, which follow clicks by a variable latency. If ripples look early or late, check the
  sync click by eye and pass `--clicks-offset`.

## Run log

- **2026-10-10 script-1. A plan failed validation at 8.01x.** A still span planned at exactly 8x
  became 8.01x after rounding to 3 decimals. Rule: plan_builder plans at 99 % of the 4x/8x limits.
- **2026-10-10 script-1. verify failed a freeze that was in the source.** The opening shot was a static
  Canva home screen, with the cursor too small for freezedetect to count. Rule: verify now treats a
  freeze as a failure only if the matching source frames actually change.
- **2026-10-10 script-1. The recorder had already zoomed the footage.** Screen recorders with
  auto-zoom (padded window over a wallpaper, camera moves on every click) double-zoom if the plan
  adds zooms. Rule: check the contact sheets for baked-in zooms; if present, use no zooms (ripples only).
- **2026-10-11 script-01. A narrated step was left out.** L7 "find it under the appropriate
  category, such as images, videos, or audio": the category-tab clicks were in the recording but
  happened after the image was placed, so they were cut to keep source order, and the line played over an
  idle panel. The client flagged it. Rule: follow the audio. Every step the narration describes
  must appear on its words; reorder the footage (cross-faded jump) instead of dropping it.
  plan_builder now lays anchors out in narration order (`src_from` / `prev_until` on an anchor,
  see the screencast-sync skill); script-01 was re-cut this way.
- **2026-10-11 client feedback. Too many cuts break the scenes.** script-01 had 16 cross-faded
  jumps in 74 s and the client asked for fast-forward (1.5-2x) instead. Rule: mark in-scene dead
  time (idle, browsing, progress, scrolling) `"ff": true` so plan_builder keeps it and speeds it up
  (≤ `ff_max`); wait actions now fast-forward up to 8x like stills. Cut only off-topic material or
  mistakes. script-02 was built this way: 1 cut in 79 s.
- **2026-10-11 script-02. The closing hold froze on a half-started action.** src_end was 166.0 but
  the next (unnarrated) filter pass had begun at 164.2: the recorder was already zooming and the
  dropdown was open on the held frame. Rule: before setting src_end (or any hold point), look at
  the 2 s before it and stop at the last frame with nothing starting.
- **2026-10-11 script-18. Ripples landed in the wrong place on recorder-zoomed footage.** The recording had baked-in auto-zoom; the plan's ripple (recording pixels) assumes the unzoomed frame, so clicks during a recorder zoom got a ripple far from the cursor (preview at 12.8 s). Rule: with baked-in zoom, use `no_ripple` for every click that happens while the recorder is zoomed (check the contact sheet at the click time); keep ripples only on unzoomed clicks.
- **2026-10-11 script-09. A hold froze before the panel opened.** A4's result time was read from a contact-sheet tile (36.0 s) of footage with baked-in recorder zoom; the sheet tile showed an unzoomed panel but the real frames at 36.0-36.35 still showed the toolbar (panel at ~36.6). Cause: trusted a sheet tile instead of single frames. Rule: for every action that gets a hold, export `--at` frames around `t_result_visible` and confirm the response is on screen before building; the preview review of the hold frame caught it.
- **2026-10-12 client review. Long holds read as a frozen/stuck video.** script-01 (holds of 4.8-6.7 s), script-04 (2.6 s at 0:40), script-10 (16.9 s), script-14 (7.8 s) and script-19 (8.4 s ending) were all flagged as "the screen is stuck". Rule: no hold longer than 1.5 s, except a closing hold of at most 3 s on the last line. When the narration runs longer than its footage, first play the neighbouring real footage slower (down to 0.75x), then reuse unused footage of the same screen (cross-faded), and unpin a supporting anchor from its word if that is what it takes; a click a second off its word is better than a frozen frame. Check every hold in plan.json before rendering.
- **2026-10-12 script-08. Loading screens look broken.** After the downloaded MP4 was clicked, the ending played ~4 s of the browser's video player loading before the video appeared; the client asked to cut it. Rule: cut loading/buffering/spinner/progress screens (player loading, editor loading, export progress) with a cross-faded jump to the first frame that shows the result, unless the narration is about the wait itself.
- **2026-10-12 client rule. Tutorials must be smooth and easy to follow.** The videos teach people, so screen movement has to be readable: speed the screen up only where it lags behind the voice, never so much that the cursor jumps, and keep the screen following the script. Rule: actions and cursor approaches 0.75-1.5x, in-scene dead time at most 2x, waits at most 3x (cut longer waits with a cross-fade instead of 8x), no held frame over 1.5 s (closing hold 3 s), no piece under 0.5 s (script-01 had 0.02 s pieces at 8x). `check.py --plan` now prints a `pace:` warning for each; a plan with pace warnings is not done.
- **2026-10-12 script-12. `prev_until` put on the wrong anchor.** `prev_until`/`src_from` describe the jump *into* the anchor they sit on (prev_until = how long the previous anchor's footage plays), so a trailing hold after A4 had to be set on A5, not A4. Also: the builder holds (at 1x) instead of slowing when an interval needs < 0.75x, so give each interval at least T x 0.75 of source (reuse neighbouring footage via prev_until) and end `prev_until` before a `stills` span (it would be sped up 8x).
- **2026-10-13 script-01-new. A motionless screen looks frozen even when it is real footage.** The plan had no long holds, but it played 3.8 s and 7.9 s of footage where the recording itself sat still (scenes.json `stills`: only the cursor twitching), which looks exactly like a frozen video (the same thing the client flagged in script-18's first 4 s). Rule: no output stretch over 2.5 s where the screen does not move (holds and `stills` footage together; 3 s at the very end). Cut most of the still, show moving footage of the same step (reuse it cross-faded), or fast-forward it (<= 2x) so something visibly changes. `check.py --plan` prints a `pace: the screen does not move` warning for each.
- **2026-10-13 script-04-new. verify failed on idle panels (3.0 s at 15.6 s) and the static opening.** The app panel sat idle for 4 s after loading and the chosen opening (18-21 s source) only had the cursor moving. Rule: scenes.py `stills` only list spans with zero cursor-sized activity; after building, look for loaded panels left idle (cut them) and start the video on footage that moves (here the clip in the timeline) rather than an idle empty design.
- **2026-10-13 script-10-new. A 334 s recording for an 82 s voiceover has no room for pace rules at the start.** The first 5.6 s of the recording are frozen and the next 4 s only have cursor motion, so the intro cannot satisfy "no still over 2.5 s" and 0.75x. Rule: when the recording is much longer than the voiceover, look for the intro footage first (what moving footage exists before the first anchor) and start the plan there; a leading hold of 2 s is worse than slow cursor-only footage. Also: freezedetect flags typing as static; check the frames before calling it a freeze.
- **2026-10-13 script-14-new. plan_builder could not meet the pace rules on a recording with long idle spells and few actions.** A first draft had holds up to 10.7 s, an 8x piece and 3 s stills. Rule: when sync.json iterations keep leaving holds, budget each narration interval by hand (source pieces per anchor gap, stills at <= 2x, idle > 2x cut, reuse moving footage of the same step cross-faded) and generate plan.json from that list (see `projects/script-14-new/work/hand_plan.py`). Also verify the click time of a Play/toggle action on single frames: A9 was first logged 1 s before the cursor reached the button.
- **2026-10-16 script-02. A cursor-only stretch passed check.py but failed verify.** The first L17 draft played 4.5 s of source (215-219.5) where only the cursor moved; `check.py --plan` printed nothing but verify reported a 4.8 s freeze. Rule: when hand-building a plan, choose pieces where the UI changes (zoom, panel, drag), not only the cursor, and check the verify frozen-spans line before accepting a render. Also: render.py ran after a failed `check.py --plan` in one chained command; run check first and read its result.
- **2026-10-16 script-05. plan_builder never plays a segment slower than 1x; it holds instead.** The recording has only ~2 s of cursor motion before the first click (src 7.9-10.5) against 6.3 s of intro narration, so the builder produced a 4 s lead hold plus a 1.9 s hold. Rule: for intros/gaps where moving footage is short, hand-patch plan.json with 0.75x speed pieces and a hold <= 1.5 s (script: `projects/script-05/work/patch_intro.py`, re-apply after any `plan_builder --force`). Also: freezedetect-static spans where only the cursor moves (here 26.9-34.8 s, the idle timeline) cannot be fixed without moving footage; list them in the report.
- **2026-10-19 script-08. 287 s of recorder-zoomed footage for a 79 s voiceover: hand plan again.** The committed work files were from an older script-08 and were stale (new transcript), so actions had to be re-read. Rule: check `work/transcript.txt` against the committed sync/actions before reusing them; for long zoom-baked recordings build the plan with `work/hand_plan.py` (pieces per narration interval at 0.8-1.5x, loading screens cut) and anchor on whichever word keeps speed <= 1.5x. Result: check.py clean, verify PASS on the first render.
