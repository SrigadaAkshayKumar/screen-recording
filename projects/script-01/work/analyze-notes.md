# analyze notes — script-01

Source: frames only (no clicks.json). Recording 361.6 s, voiceover 73.8 s, so about 80 % of the
recording is cut or sped up.

## Recording characteristics

- **Baked-in auto-zoom.** The recorder pads the window over a wallpaper and pushes the camera in
  on activity (e.g. 48.0, 52.3, 76.0, 95.0, 121.6, 136.8, 284.5, 306-307, 339.0). Coordinates were read
  on the zoomed frame at the click time. The plan must not add zooms (lessons.md).
- Several full-frame "events" in scenes.json are camera moves, not UI changes.

## Uncertain

- A3 (select the thumbnail, 77.0): the file-name box changes between 76.8 and 77.2; the click
  frame isn't sharp. Medium.
- A5 / A17 (waits): positions are the panel grid / upload toast, not a click.
- A11 (File Explorer taskbar icon, 200.95): the cursor is on the taskbar while the camera is zoomed
  out; the exact icon wasn't confirmed at native resolution. Medium.
- A12 (drag): the file is dropped at about (1467,595), over the editor's page area. The Explorer window
  covers the Uploads panel. The narration says "drag a file directly into the Uploads panel". The
  image does show up in the Uploads panel at 208.2, but the drop target on screen is the editor,
  not the panel.
- A13 (Create button, 284.45) and A19 (Home browser tab, 322.12): the click frames are blurred
  by camera motion. Medium.
- Unlogged click: Downloads in the File Explorer sidebar (~203.5) is not in the action list
  (unnarrated, position unclear), so it gets no ripple.

## Narration vs recording

- L2 "Open the design you want to work on": the design is already open when the recording starts. No action.
- L7 "Find it under the appropriate category, such as images, videos, or audio": in the recording,
  the category tabs are clicked only *after* the image is placed: Videos 110.75 (A7), Designs ~111.4,
  Folders ~111.85, Images 121.0 (A8). A7 and A8 were added on 2026-10-11 when the user asked for every
  narrated step to be shown. Canva has no Audio tab. The Designs and Folders clicks are not in the list
  (not narrated).
- L8 "...add a video or audio file to your video timeline": the recording does this in a
  *different* design (Instagram Reel, 182-189). The cut from the image design to the video
  design is a hard jump that a cross-fade smooths over.
- L10-L13 (37.5-52.2, talking points): no matching actions. The footage after the drag shows the
  dropped image sitting in the Uploads panel while the page still shows the video, which fits
  "uploading and placing are separate actions".
- Not narrated, so cut: a second upload of a .txt through the dialog that turns into a Doc design
  (226-281), the timer widget (136-148), and opening the .txt at the end (348+).
