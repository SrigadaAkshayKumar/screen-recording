---
name: screencast-analyze
description: Watch a screencast-editor recording through its contact sheets and frames and write work/actions.json (every meaningful UI action with time, cursor position, target and visible result) plus junk spans to cut. Use when actions.json is missing or must be redone, or when the screencast-edit orchestrator reaches the analyze step.
---

# screencast-analyze

Goal: an exact, honest list of what happens on screen. Times in seconds (3 decimals) on the
recording's own timeline; coordinates in **recording pixels**. Never guess a coordinate you have
not looked at.

## Inputs

- `work/probe.json` — size, fps, duration.
- `work/scenes.json` — `events` (visible UI changes: `t` onset, `bbox`), `minor_events` (cursor
  moves, hovers), `stills` (dead time, progress bars).
- `work/lines.json` — narration sentences with times and `notes` (the script's "(On screen: …)"
  directions). The notes tell you what the author expects to see.
- `work/clicks_rec.json` — present when the user ran click_logger: every click already converted
  to recording time and pixels. **This is the source of truth for click times and positions.**
- `work/frames/sheet_*.jpg` and `events_*.jpg` (from `tools/frames.py --sheets --event-sheets`).

## Method

1. Read every `sheet_*.jpg` for an overview of the whole recording, then `events_*.jpg`
   (one tile per change event, red box = changed region).
2. For each change event, run `python tools/frames.py --project P --around <t> --grid` and read the
   before/after pair. The click that caused a change happens shortly **before** its onset `t`
   (usually 0.03-0.3 s). Find the click frame: step back with `--at t-0.1,t-0.2,…`.
3. Find the cursor tip: `--at <t> --crop x,y,w,h --grid` shows a region at native resolution with
   gridlines labelled in recording pixels. Put `--mark x,y` on your estimate and check that the
   crosshair sits on the cursor tip before you write it down. Unsure → crop tighter and look again.
4. With clicks_rec.json: take `t`/`x`/`y` from the logged click and only confirm it visually (the
   first logged click is the sync click in an empty area: check the cursor sits on its mark with
   the command scenes.py printed). If the logged positions are consistently off, re-run scenes.py
   with `--clicks-offset` or `--click-region` instead of editing numbers by hand. Do not create
   actions for the sync click.
5. Without a log: changes caused by typing, scrolling and drags are also events; minor events show
   cursor travel. Long `stills` with a progress bar or spinner are `wait` actions.
6. Mark junk: mistakes and their undo, hesitations (cursor wandering with no purpose), retakes
   (the same step done twice — keep the clean take), dead time at start/end, the recorder's own
   stop button. Junk must not contain any action you keep. Give junk `"ff": true` when it is
   dead time *inside* the scene the viewer is watching (idle cursor, browsing a file dialog,
   a progress bar, scrolling): the plan then fast-forwards it instead of cutting it when the
   narration leaves room. Leave `ff` off for off-topic material (another design, a retake, a
   task the narration never mentions, the desktop); that is always cut.

## work/actions.json

```json
{
  "recording": {"width": 1920, "height": 1080, "fps": 30, "duration": 95.4},
  "sync": {"clicks_offset": -1.243, "source": "clicks.json | frames"},
  "actions": [
    {"id": "A1", "t_click": 3.557, "x": 100, "y": 60, "kind": "click",
     "target": "Upload files button", "result": "file picker opens",
     "t_result_visible": 3.6, "confidence": "high"},
    {"id": "A2", "t_click": 12.1, "x": 400, "y": 300, "kind": "drag", "x2": 900, "y2": 310, "t_end": 13.0,
     "target": "report.pdf", "result": "file dropped on the upload area", "t_result_visible": 13.1,
     "confidence": "medium"},
    {"id": "A3", "t_click": 15.0, "x": 640, "y": 412, "kind": "type", "text": "quarterly report",
     "target": "Name field", "result": "name filled in", "t_result_visible": 16.4, "confidence": "high"},
    {"id": "A4", "t_click": 16.6, "x": 960, "y": 900, "kind": "wait",
     "target": "upload progress bar", "result": "Upload complete banner", "t_result_visible": 31.2,
     "confidence": "high"}
  ],
  "junk": [{"start": 40.2, "end": 44.9, "reason": "opened the wrong menu and closed it"}]
}
```

- `kind`: click | drag | type | scroll | wait. For drags also `x2`, `y2`, `t_end`.
  For type, `t_click` = first keystroke, `x/y` = the field. For wait, `x/y` = the thing to watch.
- `t_result_visible`: first frame where the response is fully visible (after any animation).
- `target` names the control as the narration would ("Upload files button"), `result` describes
  what the viewer sees next. Sort by `t_click`; ids A1, A2, … in order.
- `confidence`: high (seen clearly / logged), medium, low. Every medium/low goes into the notes.

## work/analyze-notes.md

List everything uncertain: low-confidence positions or times, events you could not explain,
script notes ("On screen: …") that you could not find in the recording, actions the narration
mentions that are missing or in a different order, junk you were unsure about.

## Done when

`python tools/check.py --project P --actions` passes (fix every ERROR; read every warning —
with clicks.json, "no logged click near" usually means your t_click is wrong).
