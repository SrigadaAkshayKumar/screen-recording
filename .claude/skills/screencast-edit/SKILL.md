---
name: screencast-edit
description: Turn a silent screen recording plus a voiceover and its script into a finished tutorial video (actions retimed to the narration, smooth zoom and ripple on clicks). Runs the whole screencast-editor pipeline end to end and stops at quality gates. Use when the user asks to edit, build, render or re-render a screencast/tutorial video in this repo, or names a project under projects/.
---

# screencast-edit — orchestrator

You run every stage in order, without asking the user anything mid-run. Every judgment call goes
into `output/report.md`. The user reads that report, not the chat.

## 0. Before anything

1. Read `docs/lessons.md` (mistakes that already cost a render) and `CLAUDE.md`.
2. Work out the project: `projects/<name>`. If it does not exist and the user gave input files, run
   `python tools/new_project.py <name> --video … --audio … --script … [--clicks …]`.
   If it does not exist and there are no inputs, that is the one case where you stop and say so.
3. Start a run log in your head for report.md: stages run, stages reused, decisions, problems.

Below, `P=projects/<name>` and every command runs from the repo root.

## 1. Mechanical stages (reuse what is current)

Run a stage when its output is missing **or older than its inputs**; otherwise reuse it and note
"reused" in the report. Transcription takes minutes, so never re-run it needlessly.

| stage | command | output | inputs |
|---|---|---|---|
| probe | `python tools/probe.py --project P` | work/probe.json | input/* |
| transcribe | `python tools/transcribe.py --project P` | work/words.json | voiceover |
| align | `python tools/align_script.py --project P` | work/lines.json | words.json, script.md |
| scenes | `python tools/scenes.py --project P` | work/scenes.json (+ clicks_rec.json) | recording, clicks.json |
| frames | `python tools/frames.py --project P --sheets --event-sheets` | work/frames/sheet_*.jpg, events_*.jpg | recording, scenes.json |

**Gate A — inputs.** Stop if probe reports an odd frame size or a missing stream. Note VFR warnings.
**Gate B — alignment.** align_script exits 1 below 30 % overall match: stop (wrong script or
voiceover). Lines flagged `bad`/`missing` do not stop the run; list them in the report and treat
their times as approximate. If many words are misheard (product names), re-run transcribe with
`--prompt-from-script` once.
**Gate C — click sync** (only with clicks.json). If scenes prints few matched clicks, check the
offset by eye (the command it prints) and re-run with `--clicks-offset` if needed.

## 2. Judgment stages

- If `work/actions.json` exists, reuse it unless the user asked to re-analyze or the recording
  changed after it was written. Otherwise run the **screencast-analyze** skill.
  **Gate D:** `python tools/check.py --project P --actions` must pass.
- If `work/plan.json` exists and is newer than actions.json and lines.json, reuse it unless the
  user asked otherwise. Otherwise run the **screencast-sync** skill.
  **Gate E:** `python tools/check.py --project P --plan` must pass (render.py refuses otherwise).

## 3. Preview and review

1. `python tools/render.py --project P --preview` -> output/preview.mp4 (+ work/render.json).
2. Build one review sheet from the preview at every zoom peak and every segment join:
   take `zoom_peaks[].out_t` and `joins[].out_t` from work/render.json (add 0.05 s to joins so you
   see the incoming side) and run
   `python tools/frames.py --project P --video P/output/preview.mp4 --sheet-at t1,t2,… --name review`.
   Read every `work/frames/review_*.jpg`.
3. Look for: zoom framing the wrong place or cutting off the result; a hold frozen on a frame
   from before the UI responded; a jarring cut; ripple far from the cursor; black or garbage
   frames. For anything doubtful, export single frames with `--at` (add `--video`) and look again.
4. Fix the cause in `work/sync.json` and re-run `tools/plan_builder.py` (or, for a one-off tweak,
   edit plan.json by hand and note it). Re-render only the affected range with
   `--preview --from A --to B`. At most two fix rounds; after that, record the remaining issue.

## 4. Final render and verify

1. `python tools/render.py --project P` -> output/final.mp4.
2. `python tools/verify.py --project P` -> work/verify.json, output/checks/zoom_*.jpg.
   Read the zoom check images.
   **Gate F:** verify must pass. On failure: read the failing check, fix the plan, re-render,
   verify again (max two rounds). A `frozen spans` failure over a span that is static in the source
   (narrator talking over an idle screen) is a false alarm only if the source frames there really
   do not change; say so in the report rather than hiding it.
3. If any render had to be redone because of a mistake, append it to `docs/lessons.md`
   (date, symptom, cause, rule that prevents it).

## 5. output/report.md

Always write it, also when you stopped at a gate. Sections:

- **Result** — final.mp4 path, duration, verify PASS/FAIL, or the gate where the run stopped and why.
- **Stages** — each stage: ran / reused, with one line of notable output.
- **Judgment calls** — every decision you made without asking: anchors chosen, cuts, speed-ups,
  holds, zooms merged or skipped, alignment problems worked around, plan edits.
- **Uncertain** — copy the open items from analyze-notes.md and sync-notes.md.
- **Check these** — timestamps the user should eyeball, with what to look for.
- **Lessons added** — anything appended to docs/lessons.md.
