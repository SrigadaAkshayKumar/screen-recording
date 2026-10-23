# Sync notes (script-01)
No sync.json / plan_builder run: the recording (586 s, recorder zoom baked in, no click log) was far longer than the
voiceover (122.7 s), so `work/hand_plan.py` builds plan.json: one group per narration line, pieces at 0.76-1.4x, no holds,
no zooms, no ripples, cross-faded jumps wherever the source skips.

## Judgment calls
- Pieces chosen from contact sheets where the UI changes; spans listed in scenes.json `stills` avoided (or kept under 2.5 s out).
- L8/L9 (element timing: right-click, Show Element Timing, drag handles) are NOT in the recording; page-timing popup footage (src 79-94) plays instead.
- L4 (eligible plan) has no matching footage; the deck plays.
- L13 uses the Clear table click (src 125-128) then typing of the column headers (189-196); the 128-189 sample-table/ChatGPT detour is cut.
- L17/L18 show the match-data correction from two takes (265-275 and 402-405); L19 preview data from 373-378.
- Rounds: first render had 3.4 s cursor-only stretches (out 34.4, 41.2, 72.9); re-cut L7, L8, L17 to footage where the picture changes.
