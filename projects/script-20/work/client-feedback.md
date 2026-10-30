Quality re-edit of script-20 (the client flagged the same problem on script-17: "visuals are not matching").
The previous version mapped footage to lines purely by recording order, without checking any line.
Redo it properly:
- Watch the recording first (contact sheets, then single frames with frames.py --at/--around at every
  scene change) and write a real actions.json: what is on screen and what changes at each moment.
  Baked-in recorder zoom is fine - just do not use the coordinates for zooms/ripples.
- For each narration line, show the footage of THAT step, starting on the line's lines.json start.
  Verify every line's piece with a frame export at its start and middle before rendering, and list in the
  report, per line, what the viewer sees.
- Where the recording truly has no footage for a line, say so in the report and use the closest step,
  never an unrelated one. Keep 0.75-1.5x and no freezes.
