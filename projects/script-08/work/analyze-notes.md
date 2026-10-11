# Analyze notes

- No clicks.json: every click time/position was read from frames (no logger). Most are medium confidence (+-0.2 s, +-30 px).
- The recorder has an auto-zoom (camera follows the cursor) baked in for most of the recording, so the plan uses ripples only, no zooms (lessons.md, script-1).
- Drags A9, A11, A12, A13 (move/trim the audio track) are low confidence: start/end pixels are estimates. They get no ripple.
- A23 (final Download click) is low confidence: the cursor shows a busy spinner by 188.7, the click is just before.
- First Explorer visit (18-38 s): file selected is shown as "script-15" at 21.8 and as "voice" at 37 (renamed/selected in between); not an action I could place.
- 144-176 s: a second Upload files dialog that is cancelled, then Explorer again. The script has no step for it; the narration over it (L13-17) talks about file formats, so it is used as illustration.
- Narration says "preview it with your visuals" (L12). The only playback in the recording (85-96 s) happens before the trimming; no second preview after trimming.
- Narration L10 "select the audio": no distinct click seen; the track is already selected when trimming starts.
