# Re-edit (standing client rules not met by the first pass)

The first pass mapped pieces by freezedetect windows and recording order and did not verify each narration line
against frames (the report has no per-line table) - the client has rejected edits like that before
(docs/lessons.md: "mapped by recording order, not verified per line" is not a finished edit). Also the static
opening is 2.53 s still (limit 2.5 s).
Redo the analysis: look at the take second by second, note what each moving span shows, then map every
narration line to the footage that SHOWS that step, starting exactly on its lines.json start; make the visible
UI change (click / panel / result) land on the words describing it. Trim the static opening so nothing is still
for more than 2.5 s. Verify each line with frames from the final render and put a per-line table
(out window | source | what is shown | match yes/partly/no) in the report.
