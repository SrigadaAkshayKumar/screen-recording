---
name: screencast-sync
description: Match every on-screen action in a screencast-editor project to the narration word that describes it and build work/plan.json (retiming segments, zooms, ripples) via tools/plan_builder.py. Use when plan.json is missing or must be redone, or when the screencast-edit orchestrator reaches the sync step.
---

# screencast-sync

You make the editorial decisions; `tools/plan_builder.py` does the arithmetic. You write
`work/sync.json`, run the builder, review its output, and write `work/sync-notes.md`.

## Inputs

`work/actions.json`, `work/lines.json` (sentences with their `words` and exact word times),
`work/words.json`, `work/scenes.json` (`stills`), `work/probe.json`, `work/analyze-notes.md`.

## 1. Pick the word for every action

For each action find the line that describes it and the exact word the click should land on:
the word that **names the control or the thing acted on**.

- "click **Open**" -> Open. "select **Uploads**" -> Uploads. "choose the **report** file" -> report.
- "press **Save** and close" -> Save (the next action gets "close").
- type actions -> the word that introduces the text ("type a **name**") or the first word of the
  typed text if it is read out. drags -> the verb or the object ("**drag** it into…").
- wait actions are not anchored; the builder speeds them up or you cut them.
- **The audio is the instruction.** Every step the narration describes must be shown at its
  words, even when the recording does it later, earlier or in another design ("find it under
  images, videos…" -> show the category tab clicks). Never drop a narrated step just to keep the
  recording's order. If the recording's order differs, anchor every step anyway: the builder
  lays anchors out in narration order and cross-fades to wherever the footage is (see
  `src_from` / `prev_until` below). Record each reorder in the notes, plus any continuity
  oddity it causes (e.g. something already on the page that is only added later).
- An action the narration never mentions: no anchor (it plays at whatever speed its interval
  gets); say so in the notes. A narrated step with no action: note it.

## 2. Write work/sync.json

```json
{
  "anchors": [
    {"action": "A1", "line": 2, "word": "Upload"},
    {"action": "A2", "line": 4, "word": "report"},
    {"action": "A3", "line": 5, "word": "Open", "occurrence": 2},
    {"action": "A5", "word_index": 57, "lead": 0.05},
    {"action": "A4", "line": 6, "word": "videos", "src_from": 110.0, "prev_until": 121.7}
  ],
  "zooms": [
    {"actions": ["A1"], "scale": 1.8},
    {"actions": ["A2", "A3"]},
    {"actions": ["A5"], "include": [[1050, 250]]}
  ],
  "no_ripple": [],
  "cuts": [{"src_start": 10.0, "src_end": 15.5, "reason": "upload wait; narration says we skip ahead", "xfade": true},
           {"src_start": 21.0, "src_end": 24.0, "reason": "cursor idles on the panel", "ff": true}],
  "ff_max": 2.0,
  "use_junk": true,
  "hold_at": {"A5": 16.7},
  "style": {"ripple_color": "#2F80ED"}
}
```

- **anchors**: `line` + `word` (matched case/punctuation-insensitively in that line's transcribed
  words; `occurrence` picks the 2nd, 3rd… hit), or `word_index` into words.json, or an explicit
  `out_t`. `lead` shifts the click after the word start (keep |lead| ≤ 0.1).
  - **Out of order** (narration order wins): anchors are laid out by their words, not by source
    time. Between anchor P and the next anchor N the plan plays P's footage from its click up to
    `prev_until` (default: P's result + 1 s), then cross-fades to `src_from` and plays up to N's
    click. A backward jump gets `src_from` = click − 1.5 s by default; set both explicitly when
    you know the right frames. Use `src_from` on a *forward* anchor too, whenever the plain
    stretch P→N would replay footage you already showed out of order.
  - Out-of-order footage must not be inside a cut/junk span; split the junk around it.
- **zooms** — zoom when the narration names a specific control. Not on every tiny click:
  - clicks less than 1.2 s apart (in the output) share one zoom that frames both (the builder
    also merges these automatically and says so);
  - keep scale 1.4-2.2 (default 1.8; smaller targets/dense UIs higher, wide areas lower);
  - when the result appears away from the click (a side panel, a dialog elsewhere), add
    `include: [[x, y], …]` so the zoom frames both, or leave the action unzoomed;
  - leave room to zoom out between steps so the viewer keeps their bearings.
- **cuts** — source spans to remove, cross-faded by default. Use them for long waits the
  narration skips ("…so we skip ahead"), dead time, and anything the builder cannot fit.
  `actions.junk` is cut automatically (`use_junk`).
  **Prefer fast-forward to cuts inside a scene**: a cut breaks the scene into jumps. Give a cut
  (or a junk span) `"ff": true` when it is in-scene dead time (idle, browsing, progress,
  scrolling); the builder keeps it and speeds its whole interval up instead, as long as the
  interval plays at ≤ `ff_max` (sync.json, default 2x). Spans that don't fit are still cut and
  listed in the builder notes with the reason. Off-topic material stays a plain cut.
- **hold_at** — where the slack before an action is held when the narration is longer than the
  footage. Default: just after the previous action's result appears (so the response stays on
  screen while it is described). Use a source time to hold a better frame (e.g. the "Upload
  complete" state), or `"before_click"`.
- **src_start / src_end** — trim the recording's head/tail if it starts or ends with junk.

## 3. Build and review

```
python tools/plan_builder.py --project P
```

It prints the sync table, its own decisions (merged zooms, auto-cuts of still spans, trimmed
intro) and runs the plan validator. Rules it enforces, which you must keep if you hand-edit:

- segments cover the output with no gaps/overlaps; a jump back in the source needs `xfade`
  (the builder sets it);
- each anchored click lands within ±0.15 s of its word;
- speed 0.75x-4x; slower -> hold the last frame; still spans/waits up to 8x (`"wait": true`)
- **Tutorial pacing (client rule, overrides "fits within the limits"):** a viewer must be able
  to follow every cursor move. Actions and cursor approaches 0.75-1.5x; in-scene dead time at most
  2x (`ff_max`); waits at most 3x, otherwise cut them with a cross-fade; no held frame over 1.5 s
  (closing hold up to 3 s); no stretch over 2.5 s where the screen does not move (holds plus
  `stills` footage played as is, e.g. only the cursor twitching: it looks frozen too); no piece
  shorter than 0.5 s. `check.py --plan` flags each of these as
  a `pace:` warning; fix them all before rendering (more narration time, a cut of dead time, or a
  supporting anchor unpinned), and list any you could not fix in the report.
  or cut with a cross-fade;
- zoom scale 1.4-2.2.

If it fails with "N s of source must fit in M s", add a cut or move the anchor. Read the table:
an approach speed near 4x means the viewer will see a rush — consider a cut instead. A long hold
(> 3 s) on one frame may look frozen — consider `hold_at` on a frame where something is happening
or holding in two places by anchoring an extra word.

plan.json keeps a hash: plan_builder refuses to overwrite hand edits (pass `--force` to replace them;
the edited copy is kept as plan.hand.json). Prefer putting every decision into sync.json.

## 4. work/sync-notes.md

The builder writes the table (line, word, out time, action, src time, speed) and its decisions.
Append a `## Judgment calls` section (the builder preserves it on re-runs) with: why each anchor
word, every cut and why, zoom choices (merged, skipped, `include`), order conflicts, unmentioned
actions, and anything from analyze-notes that affected the plan.

## Done when

`python tools/check.py --project P --plan` passes with no errors, and every warning is either fixed
or explained in sync-notes.md.
