# Analyze notes (script-10)
- No clicks.json: all click times/positions are read from frames. A1, A2, A9 positions are low/medium confidence (recorder auto-zoom is baked in at those moments, so the view is magnified).
- The recording has baked-in recorder zoom around most clicks -> plan uses no zooms and no ripples.
- A12 (final Download button, ~195.5 s) is never clearly clicked in the footage (cursor only hovers); not listed as an action.
- Recording starts with 5.3 s of frozen screen; used as junk by trimming src_start to 5.5 (plan starts at 5.3).
