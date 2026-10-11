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
