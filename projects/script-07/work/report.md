# script-07 report

## Result
- `projects/script-07/output/final.mp4`, 93.500 s (voiceover 93.506 s), 2560x1440, **verify PASS** (duration, streams, resolution, frozen spans, 29 join boundaries without black frames).
- `check.py --plan`: OK, **no `pace:` warnings**. 20 line groups at 0.81-1.20x (no hold, no cut, no segment under 1.3 s).
- Freeze check on the *final* (freezedetect n=0.002, d=1.7): longest still 2.33 s (the static editor right after the intro zoom-out, 3.5-5.9 s); the others are 1.7-2.2 s (typing / loading). Nothing over 2.5 s.

## Stages
- probe, transcribe, align (lines 1-20, all match >= 0.93), scenes, frames: **reused** (already current; transcription not re-run).
- analyze: done by hand from the 9 contact sheets plus ~14 extra 12-tile sheets (0.5-1.5 s steps). No `actions.json` was written; as in the earlier script-07/-06/-09 runs this take is planned with `work/hand_plan.py` (per-line groups, no clicks log, no zooms). Notes below replace analyze-notes/sync-notes.
- sync/plan: `work/hand_plan.py` -> `work/plan.json` (segments only, no zooms/ripples: the recording already carries the recorder's own zoom).
- preview rendered 4 times (freeze fixes), final rendered once. verify PASS.

## Judgment calls
- Audio order is followed; every group starts on its line's start. The take is mostly slow typing (src 100-150 and 218-232 are almost static), so only ~60 s of it really moves; typing-only stretches were replaced by the places where the text changes.
- Source jumps (all cross-faded, no cuts of in-scene dead time that were not static): L1 skips the static home screen (3.7-10 s, cursor only); L2 jumps Apps click -> search typing (skips panel loading 16-20.9 s); L3 jumps AI Voice click -> paste (skips 36-40.4 s idle voice list); L4 uses 36.6-38.4 (first voice pick, Ralph) for "voice style"; L7-L9 skip static text spans (81.5-84.4, 88.2-93.6); L10 jumps to the "200 -> two hundred" edit.
- Footage borrowed or approximate (see table): L5 (Richard's sample playing, "clear conversational voice") is the nearest real footage; L6 "read the text aloud" is the cursor entering the text box; L9 shows number typing ("200" at 127-128 s) as the "numbers in the form you want spoken" step; L14 shows the 2nd generated sample appearing (the take has no side-by-side comparison); L17 (room to breathe) shows the clip being dragged to leave a gap.
- No zooms/ripples (hand plan; the recorder zoom is baked into the take at several places, e.g. 14.7, 17.1 s).

## Per-line table (frames read from final.mp4 at each line start and middle)
| # | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0.00-7.40 | 0-2.7, 10-13.4 | editor with the portrait video open, then cursor travelling toward the Apps sidebar | yes (intro) |
| 2 | 7.40-12.50 | 13.6-16.0, 20.9-24.6 | cursor on Apps, panel opens (Apps on "Apps" 9.4 s); "AI voice" typed in the search box with the dropdown (on "search" 10.6 s) | yes |
| 3 | 12.50-17.00 | 33.0-35.9, 40.4-42.5 | AI Voice icon clicked in results (~13.5 s), AI Voice panel opens, text pasted in the box (~16 s) | yes |
| 4 | 17.00-20.68 | 48.4-50.9, 36.6-38.4 | language dropdown with English (United States) ticked; then the voice tiles, Ralph picked | yes |
| 5 | 20.68-26.08 | 58.0-59.8, 60.4-63.6 | Ralph selected, then Richard picked and previewed (ring around the tile) | partly (nearest footage to "conversational voice") |
| 6 | 26.08-28.34 | 75.0-77.3 | cursor into the text box, text being edited at the start | partly (no literal read-aloud on screen) |
| 7 | 28.34-35.26 | 77.3-81.5, 84.4-85.8 | text box zoomed by the recorder, "Welcome to the masterclass." inserted, sentences edited | yes |
| 8 | 35.26-38.80 | 86.5-88.2, 93.6-95.0 | cursor moving along the text, punctuation edits | partly (edits visible, small) |
| 9 | 38.80-42.70 | 94.3-96.8, 127.4-128.7 | text edits, then the number being typed into the text | partly |
| 10 | 42.70-48.02 | 148.9-154.3 | zoomed text; "200" selected and replaced by "two hundred" | yes |
| 11 | 48.02-50.90 | 159.4-162.3 | Generate AI voice clicked (~48.5 s), "Generating AI voice" bar | yes |
| 12 | 50.90-54.16 | 170.8-174.1 | clip on timeline playing back with captions ("This ...") | yes |
| 13 | 54.16-59.70 | 200.0-205.8 | the line selected and rewritten ("...completed in two hundred countries"), Richard still selected | yes |
| 14 | 59.70-65.72 | 205.8-211.8 | Generating AI voice, new clip appears on the timeline | yes |
| 15 | 65.72-70.48 | 231.0-235.8 | new text typed, Generate clicked, third clip added | yes |
| 16 | 70.48-74.36 | 235.8-239.7 | the new clip on the timeline after the first, zoomed timeline | yes |
| 17 | 74.36-79.60 | 243.2-248.4 | playhead over timeline, second clip dragged right leaving a gap | yes |
| 18 | 79.60-83.56 | 249.0-253.0 | clip trimmed / moved on the timeline, video playing | yes |
| 19 | 83.56-88.30 | 276.5-281.3 | Audio panel, Energy Trend Logo music added below the narration, preview plays | yes |
| 20 | 88.30-93.51 | 299.9-305.1 | volume slider on the music clip, then the timeline; Share click at the end (~93.1 s on "exporting") | yes |

## Uncertain
- Lines 5, 6, 8, 9 only partly match: the take has no footage of the narrated step itself (no read-aloud, no comparison of voices, typing of abbreviations).
- The take's voiceover steps differ from the script in places (e.g. there is no separate "full stops and commas" typing); text edits are the closest footage.
- Output is 2560x1440 (upscaled from 1920x1080 by the pipeline default, as in earlier runs).

## Check these
- 3.3-7.4 s: cursor travel before Apps; static for ~2.3 s after the intro zoom-out.
- 20.7-26 s: Richard sample ring (nearest footage for "conversational voice").
- 33.5 s, 35.3 s, 37.2 s, 38.8 s, 41.4 s: cross-fades between text edits (L7-L9); small changes only.
- 59.7-65.7 s: the second sample appears in the timeline (L14).
- 88.3 s: volume popup at the start of L20.

## Lessons added
- 2026-11-03 script-07 re-edit (new script, 93.506 s voiceover) entry in docs/lessons.md.
