# script-10 report

## Result
output/final.mp4, 97.83 s (voiceover 97.849 s), 2560x1440 delivered. verify.py: PASS. `check.py --plan`: OK, no pace warnings.

## Stages
- probe, transcribe, align, scenes, frames: reused (already current). Recording 243.1 s, 1920x1080, no clicks log.
- analyze/sync: replaced by `work/hand_plan.py` (long take, no click log, same recipe as other projects); actions.json is a stub, so `check.py --actions` reports "empty actions" (expected).
- preview: freezedetect (d=1.5) only the 2.4 s static opening. Review sheet read at all 29 joins: cross-fades only, no black/garbage frames.
- final render + verify: PASS.

## Judgment calls
- One group per narration line, starting on the line's start; 17 groups at 0.76-1.35x; no holds, zooms or ripples.
- Pieces taken only from freezedetect moving windows; the 78-95 s download progress bar and 166-196 s processing wait are skipped (static), not sped up.
- Opening: 2.4 s static home screen (1x), then the Projects page appearing.
- Order follows the audio: Projects/select (L2), toolbar Download/file type (L3), download + extract (L6), explorer (L7), open design, Share>Download>pages toggle (L9), download (L10).

## Uncertain
- Lines with no matching footage use the nearest steps: L4 (plan requirement) and L5 (25 limit) show selecting designs; L11-L13 (video design timeline) show the Canva design page; L14 (new separate design) uses the design page and the end screen; L15 (Music/VoiceOver) and L16 show Explorer folder browsing; L17 shows Explorer.
- Recording has no MP4-selected dialog step visible long enough for L3 "select MP4"; the file-type list is shown at 23.2 s.

## Check these
- 16-17 s and 20-23 s (selection and download dialog cross-fades).
- 75-91 s (lines 14-16): footage is illustrative, not matching the words.

## Lessons added
- script-10 entry in docs/lessons.md.
