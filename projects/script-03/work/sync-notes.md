# Sync notes
Anchors (click at word): A1 Uploads(L2 "Open"-0.1) 6.88 | A2 Upload Files 9.74 | A3 Open in dialog 16.68 | A4 Audio tab 19.64 | A5 add clip 21.26 | A7 trim 31.36 | A8 Play 33.88 | A9 Shorten 35.86 | A10 add scene 42.6 | A11 Audio tools 48.68 | A12 voiceover track 53.04 | A13 Uploads 59.06 | A14 drag to timeline 63.72 | A15 check timeline end 68.9 | A16 Share 71.94 | A17 Download 73.78. See `hand_plan.py` for source pieces and speeds.

## Judgment calls
- plan.json is hand-built (as for script-14-new): each narration interval between two anchors is filled with 1-3 source pieces at one uniform speed (0.75-1.5x), cross-faded where the source jumps. No pace warnings.
- Cut with cross-fades (not fast-forwarded): the upload wait (31-43 s, > 3x needed), play-button buffering (73-77 s), the unnarrated middle of the recording, the idle spells (96-101, 120-126, 176-187 s) and the Download panel loading (176-187 s).
- Intro: the recording starts with ~1.5 s of idle canvas then the recorder zoom animation; A1's click had to land 1.1 s before "select Uploads" (at "Open") because only 4.9 s of footage precede it and the 0.75x floor leaves no room; a 0.3 s hold at the very start.
- Narration order: footage jumps forward/back as needed; L13 ("part many tutorials skip", no action) plays the volume-slider footage.
- No zooms, no ripples: recorder baked-in zoom.
- Warnings accepted: A4 result (the Audio list) and A8 result (playback after buffering) are cut out; the viewer sees the next step after a cross-fade.
