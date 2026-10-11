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
