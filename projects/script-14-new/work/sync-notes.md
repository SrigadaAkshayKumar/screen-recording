# Sync notes (script-14-new)

plan.json is **hand-built** by `work/hand_plan.py` (groups of source pieces, each filling one narration interval at a uniform speed). `plan_builder.py` output had 15 pace warnings (holds up to 10.7 s, 7.9x piece, 3.2 s stills) that sync.json alone could not fix, so work/sync.json is only the first draft. Re-running plan_builder would overwrite the plan: do not.

## Judgment calls
- Anchors (word -> action src time): sound->A2 hover audio 10.4, video->A3 page hover 11.6, left->A5 drag 13.2, right->A6 drag 20.8, result->A9 play 55.3, trim->A7 42.0, shortened->A8 44.8, audio's->A10 menu 95.7, Adjust->A11 97.6, highlighted->A12 waveform drag 119.0, Listen->A13 play 131.6, Add->A14 Fade 179.3, smoothing->A15 slider 182.4, Preview->A16 play 189.6, download->A17 Share 191.2, soundtrack->A20 MP4 196.2.
- Footage is reordered to the narration (cross-faded jumps): lines 4-5 reuse hover footage 9.9-13.2; line 6 plays the Play click from 55 s; lines 7-9 jump between 40-48 s, 92-98 s, 116-121 s; lines 10-11 use the clip-drag footage at 143-148 s; line 12-13 plays 131.6-137.5 s; fade, share, download from 176-197 s.
- Cuts (cross-faded): idle 14.7-20.2 s (5.5 s still, would need 8x), 58.3-92 s, 125-129.9 s (still), 148-176 s, 193.0-194.3 s (share panel idle), desktop after 197.3 s.
- Fast-forward: still span 4.77-8.47 s plays at 1.7x (2.2 s). Everything else is 0.75-1.6x.
- MP4 click is anchored on "soundtrack" (0.2 s later than "MP4") because the share flow needs 5 s of footage in the last 3 s of narration.
- Unanchored: A1 (audio already selected), A4 (hover handle, part of A5 lead-in), A18/A19 (Download tile, file-type dropdown: shown as lead-in to A20).
- No zooms/ripples because of the recorder's baked-in zoom.
- Remaining check.py warnings: only the four "not tied to a narration word" notes above. No pace warnings.
