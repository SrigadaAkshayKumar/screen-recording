# script-07 report

## Result
`projects/script-07/output/final.mp4` — 97.756 s (= voiceover), delivered 2560x1440, **verify PASS**. `check.py --plan`: OK, no `pace:` warnings.

## Stages
- probe, transcribe, align (22 lines, all `ok`), scenes, frames: **reused** (new 311.067 s take, 97.756 s voiceover, no click log).
- analyze/sync: done as a **hand plan** (`work/hand_plan.py`, 22 per-line groups) instead of actions.json/sync.json — no click log, a typing-heavy take, and the repo's established practice for this project (see docs/lessons.md). No zooms/ripples. `work/actions.json` and `work/sync.json` were not written.
- preview: rendered, join frames reviewed (cross-fades only, no black/garbage frames); preview freezedetect (d=1.5) longest 2.47 s.
- final render + verify: PASS (0 freezes over 3 s, 31 joins clean).

## Judgment calls
- Followed audio order; each group starts exactly on its line and plays at one speed, 0.77-1.21x. Nothing faster than 1.21x, no holds.
- The recording is mostly static: home screen 3-12 s, loading, cursor-only 63-77 s, slow typing 104-150 s. Only moving windows (freezedetect n=0.002 d=0.5) were used; typing chunks inside scenes `stills` are ≤2.4 s each and separated by moving footage.
- Per-line footage: L1 opening; L2 static intro + editor (src 8.8-10.8, 12.1-15.6, borrowed: nothing narrated); L3 Apps panel + search (15.6-21.9); L4 AI voice list + tool open (24.8-27.1, 34.5-36.8); L5 language (48.1-52.3); L6 voice choice (56.9-63.1); L7 pasted text (40.6-42.9, borrowed); L8-L9 text editing (78.6-81.2, 98.3-104.3); L10-L11 typing numbers (126.8-129.2, 148.6-152.7, 131-132.7); L12-L13 generating AI voice (156.7-163.7); L14 rewrite typing + generate again (220.8-222.6, 205.8-208.8); L15 second generate (193.7-199.6, borrowed); L16 generate remaining (233.5-239.6); L17-L19 audio on timeline/playback (169.5-178.6); L20 timeline playback (242.2-246.8, borrowed); L21 music panel (271-275); L22 preview (290-295.3).
- Skipped dead spans: loading 27-34 s, voice-hover/cursor-only 63-77 s, long typing 104-148 s (partly), 166-169 s, 295-298 s, closing export dialog 298-311 s (not narrated).

## Uncertain
- Lines with no truly matching footage: L2 (intro), L7 (read aloud), L15 (rewording vs. regenerating), L20 (trim/move audio — the recording shows playback, not a trim), L21 (music-volume step is only the audio search panel), L22 (preview). Nearest panels used.
- The text edit steps (L8-L11) are small typing in a text box; at 1920 px they are legible but subtle.

## Check these
- 4.7-7.1 s: static-ish opening (cursor only), 2.5 s.
- 43.3-45.7 s, 50-52.2 s: slow typing, ≤2.4 s.
- 61-70 s (L14/L15): rewrite typing → generate; check the voice-generation footage matches the words.
- 80-82 s: playback of a still video frame, 2.1 s.
- 88-93 s: music panel / preview, borrowed.

## Lessons added
- script-07 entry appended to docs/lessons.md.
