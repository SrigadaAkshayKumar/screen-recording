# Sync notes (script-05)
plan.json is built by work/hand_plan.py (not plan_builder): the recording is 259.6 s for a 90.1 s voiceover,
has baked-in recorder zoom and no click log, so each narration line got source pieces chosen by hand.
No zooms, no ripples, empty `sync` (clicks are not word-pinned; the footage follows each line's step).
## Judgment calls
- Follows the audio order; all pieces play at 0.91-1.44x, no holds. Source order is kept except where the narration needs
  an earlier/later step (cross-faded jumps, 23 of them; unavoidable with 170 s of dead time to skip).
- L2 packs Create / Uploads / Videos tab into 4.3 s at 1.43x (three pieces).
- Idle/cursor-only spans (45-53, 59.5-65.7, 73.9-79.2, 134-141, 145.6-148.3, 190-198, 209.9-213.6) are skipped.
- Player loading (240-246.5) and the download progress (229-237) are cut. Closing line plays the downloaded video.
- L17-18 ("Here's the part. Many tutorials skip.") has no matching on-screen step; shows the audio track being added.
- L19/L20 reuse the audio panel and the speed slider returning to 0.5 as visuals.
## Uncertain
- Piece boundaries chosen from sheet tiles, not single frames; see report "Check these".
