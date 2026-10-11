# Analyze notes (script-11)

- No click log: all click times/positions were read from frames. Positions are only approximate because the
  recorder zooms the footage (baked-in camera moves), so the same control sits at different pixels depending on
  the zoom state. Ripples may be off by tens of pixels. Low confidence: A9, A10 (resize/move drags), A14 (timeline drag).
- The recorder has baked-in auto-zoom -> plan uses ripples only, no zooms (lessons: script-1).
- Recording is 152.6 s, voiceover 79.1 s. Dead time: 34.8-47.8 (cursor rests by Play), 68-95.4 (idle timeline,
  Images tab browsing), 110-121 and 129-133.5 (idle Download panel), 135-141 (download toast).
- The Share -> Download -> format flow is recorded twice (95.9-118 and 122.8-135). Pass 1 is used for the narration of
  "download formats" (L13-15), pass 2 for "Select Share, Download..." (L17).
- 121.0-122.3: browser context menu flashes (unintended) -> junk, cut.
- Unnarrated actions left out of actions.json: closing the image viewer (14.6), second timeline click (60.3),
  opening the format dropdown in pass 2 (~127.2).
- Narration L11 "Preview the full section" has no distinct action in the recording.
- Script directions (On screen: ...) are absent.
