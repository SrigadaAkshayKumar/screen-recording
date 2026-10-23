# Sync notes (script-08)
Plan built by hand (`work/hand_plan.py`, not plan_builder): the recording has baked-in recorder zoom, no click log, 281.8 s of footage for a 91.8 s voiceover.
## Judgment calls
- One source piece (or two cross-faded) per narration line, all 0.8-1.18x, no holds, no zooms/ripples (baked-in zoom), no `sync` entries (click times are +-0.5 s from sheets, so they are not pinned to words).
- Order follows the audio: lines 4-8 (Elements, Mockups, products, add mock-up) use 30-46 s + 54-71 s; lines 9-13 (uploads/drag, fit, controls, crop, apply) use 92-143 s; lines 14-15 (text) use 172-187 s; lines 16-19 (proportions, wide artwork in tall frame, crop) use 205-240 s; line 20 zoom 247-251 s; lines 21-22 share/download/final 256-277 s.
- Avoided scenes.json stills; cut the idle 35.6-43.6 (panel static), 136-140, 161-172, 222-231. Dead time was skipped via cross-fades because the footage is much longer than the voiceover, not sped up.
- Line 6 ("through apps") and "download artwork as PNG" have no matching footage: panel browsing / uploads panel stand in.
- Line 4-5 clicks (Elements ~31.8 s, Mockups ~33.7 s) land ~2 s before their words (play at 0.8x, the slowest allowed).
- check.py --plan: no pace warnings.
