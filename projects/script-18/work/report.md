# script-18 report

## Result
- `projects/script-18/output/final.mp4`, 90.892 s, 2560x1440, **verify PASS** (duration, streams, resolution, frozen spans, black frames at 30 joins).
- `check.py --plan` clean: no pace warnings, no hold, 29 pieces at 0.73-2.0x. 2x only on static spans, all moving pieces 0.75-1.4x.
- Freezedetect on final.mp4 (n=0.003, d=1.5): longest still stretch 2.2 s (typing/cursor-only), none over 2.5 s.

## Stages
- probe, transcribe, align (19/19 lines ok), scenes, frames: reused (already current). Not re-transcribed.
- analyze/sync: no actions.json or sync.json; the plan was **hand-built** (`work/hand_plan.py`, per docs/lessons.md for long, mostly-static takes) from 1 s sheets and full-res freezedetect of the source. No zooms or ripples: the recording has baked-in recorder zoom (lessons: ripples would land wrong).
- preview: 2 rounds (first had a 4.1 s typing freeze in L9; fixed by mixing typing with a moving piece). Final render ~4 min, verify PASS.

## Judgment calls
- The take is 315 s with long static spans (generation wait 50-73 s, panels idle 91-105 s, etc.). Dead time is skipped with cross-faded jumps; static spans that stay are played at 2x and kept <= 2.4 s.
- The take has the whole flow twice (calm prompt, then a "rock" follow-up prompt) plus a Library audio search and a Video-design detour. Follow-up typing footage (src 239-255) is borrowed for L5, L9, L17 because the calm prompt was pasted instantly and then the screen sits still for 14 s. The text typed differs ("rock music...") from the narrated text.
- L1 intro uses b-roll of the second track being added (src 284-290) instead of the static home screen (0-11 s, cursor only).
- L16 "option is missing" uses the take's "Canva AI is coming to Video" screen (src 215.6-219.3), the closest real footage.
- Prompt paste (33.7) lands ~1.2 s after "Create" and the Submit click (48.4) ~0.6 s before "Submit"; kept to stay inside the pace rules.
- Unused: src 0-11 (static home), 50-72 generation wait, 91-105 idle, 119-160 duplicate positioning, 221-231 other-tab detour.

## Per-line table
| line | out window | source | what is shown | match |
|---|---|---|---|---|
| L1 intro | 0-5.1 | 284.3-289.8 | second track generated, added to the timeline | partly (b-roll) |
| L2 open design | 5.9-9.7 | 12.4-17.0 | click design on Home, editor loads (click ~6.7 s) | yes |
| L3 select Canva AI | 10.6-12.3 | 21.9-25.2 | cursor to Canva AI, panel opens (~11.4 s) | yes |
| L4 describe music | 12.9-16.5 | 25.2-31.3 | Canva AI panel, zoom to the prompt field | yes |
| L5 type the prompt | 17.2-24.9 | 31.3-34.3, 239.4-241.2, 47.3-48.4 | empty field, calm prompt pasted (~20.8 s), borrowed typing of the rock prompt, zoom on the full prompt | partly (text differs, paste late) |
| L6 submit | 25.6-27.9 | 48.4-50.6 | Submit click (~24.7 s), prompt bubble and "Working on it" | partly (click ~0.6 s early) |
| L7 preview generated track | 28.4-31.2 | 72.9-78.3 | "Tutorial Calm Bed" card appears | yes |
| L8 listen | 32.0-36.7 | 84.6-88.7 | card, page tiles, preview in design (no audio visible) | partly |
| L9 ask for fewer instruments | 37.5-41.1 | 243.0-245.0, 277.7-279.9 | follow-up prompt typing, new result arrives | partly (different text) |
| L10 add + position | 41.8-46.7 | 88.7-91.3, 109.0-112.6 | track added to timeline (~42.4 s), dragged on timeline | yes |
| L11 trim, volume | 47.4-50.7 | 114.0-116.8, 148.4-150.9 | trim handles, volume slider 100 to ~55 | yes |
| L12 fade | 51.6-55.8 | 160.6-165.0 | Fade menu, fade-in/out sliders | yes |
| L13 Elements + Audio | 55.8-61.7 | 174.5-177.6, 186.2-189.2 | Elements panel, Audio category, library list | yes |
| L14 Canva AI workflow | 62.5-66.3 | 233.2-237.0 | back in a design, Canva AI panel, prompt box focus | partly |
| L15 availability | 67.6-70.4 | 210.5-214.2 | Canva home and Create-a-design dialog | partly (conceptual) |
| L16 option missing | 71.0-74.5 | 215.6-219.3 | "Canva AI is coming to Video" message | yes |
| L17 musical direction | 75.3-79.6 | 246.5-248.5, 253.0-255.2 | typing a musical-direction prompt, send | yes |
| L18 terms | 80.1-87.2 | 293.7-301.0 | second track in project, timeline waveform | partly (conceptual) |
| L19 preview complete mix | 88.1-90.4 | 265.8-269.1 | Present clicked, full-screen preview | yes |

Verified from final.mp4 frames at 2.5, 8, 11.5, 15, 18, 22, 26, 30, 34, 39, 43, 46, 49.5, 53, 58, 61, 65, 69, 72.5, 76, 79, 84, 89, 90.5 s.

## Uncertain
- Rock-prompt typing used for L5/L9/L17 may look like a different prompt than the one narrated.
- L8, L15, L18 are conceptual lines with borrowed footage.

## Check these
- 20.8-23.3: paste of the calm prompt, then borrowed typing (cross-fade at 21.45).
- 24.7: Submit click, slightly before "Submit".
- 49.3: volume slider cross-fade; 53-56: fade slider area is near-static (2.2 s).
- 78.2-80.1 and 75.2-77.4: typing stretches (about 2 s each).

## Lessons added
- See docs/lessons.md (script-18 re-edit).
