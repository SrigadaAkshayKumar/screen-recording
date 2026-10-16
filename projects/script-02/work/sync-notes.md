# Sync notes (script-02)
plan.json was built by `work/hand_plan.py`, not plan_builder (a 249 s recording for an 87 s voiceover; the builder's pace rules could not be met automatically, same as script-14-new). Each narration line gets its own source pieces (see the G list in the script).

## Judgment calls
- Anchors (click on word): A1 Uploads->"uploads", A2 Audio tab->"choose", A3 add voice-over->"add", A4 Play->"Play", A5 Audio tools->"lower", A6 Captions button->"captions" (L6), A7 Generate->"captions" (L9), A8 Share->"share". All within +-0.15 s (check.py).
- Intro: the first 7.9 s of the recording are idle; the video opens on 7.9-15.2 (cursor travelling to Uploads, recorder zoom) so nothing sits still.
- Speeds: all 0.78-1.3x except the caption-generation wait (2.8x, marked wait). No holds. Joins that jump in the source are cross-faded (21).
- Reorders: L8 (leave unrelated audio out) is shown on the Apply-captions-to area plus colour picker (96-100), which comes after the style click shown for L9 (93.6-94.9): a short jump back.
- L12/L13 (correct names / keep text away from faces): caption text being edited (150-158). No footage of moving captions away from faces.
- L14-L17 (timing tips): timeline zoom, clip trimming (207.9-211), captions transcript panel (183.5-186.4) and the selected caption (213-217). The 198-207 still (trim handle held) is skipped.
- L18: share -> download panel -> Download click; L19 ends on the download-in-progress toast (the file is never opened in the recording).
- No zooms, no ripples: the recorder's own zoom is baked into the footage.
- plan.json has no generated_hash, plan_builder would overwrite it only with --force.
