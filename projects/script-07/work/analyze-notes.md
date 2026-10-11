# Analyze notes (script-07)

- The recorder has baked-in auto-zoom (frames alternate between the padded full window and zoomed views). Coordinates are the pixels of the frame at the click time, estimated from contact-sheet tiles (±25 px); none checked with --grid crops. Confidence is medium/low everywhere.
- Low confidence: A9/A10 (track move / edge trim, 80-87 s), A13 (volume slider), A19 (video volume slider), A20 (video clip end drag). Exact click times are +-0.3 s.
- 88.4-96.8 s: track held mid-drag with tooltip 14.8-15.6 s; 97-98.5 s the track is moved again. Treated as hesitation (junk, ff), not an action.
- 48-52 s: drag of script-15 towards the timeline did not add anything (junk). The track was added later by clicking the file (A8, 59.75 s) after using the Add audio button.
- 65-79 s: unnarrated playback test (junk). 112-121 s: playback (junk).
- 128-153 s: video clip resized and idle (unnarrated, junk). 157-192 s: cursor idles, Uploads panel browsed (junk).
- Not in the script's order: the recording clicks Add audio -> Uploads -> file (54-60 s) *after* the first idle/failed drag; narration says click the file first (L6) and the Add Audio button second (L7).
- The recording has no click log; clicks were found by eye.
