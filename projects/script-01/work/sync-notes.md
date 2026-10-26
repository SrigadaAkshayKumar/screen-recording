# Sync notes (script-01)
Hand plan (work/hand_plan.py -> plan.json): 21 per-line groups starting on each line's lines.json start, 0.79-1.23x, no holds,
no zooms/ripples (baked-in recorder zoom, no click log). check.py --plan: OK, no pace warnings.

## Judgment calls
- Pieces come from the moving windows of `freezedetect n=0.003 d=0.8` on the source.
- Audio order wins: Add Row (L7) uses src 68-75, Add Column (L8) uses 64-67; recording order is ambiguous there.
- Intro (L1) borrows the finished PDF table (src 133-136.6) because the recording has only ~4 s of moving footage before the editor opens.
- No footage exists for L16 (don't shrink table), L18 (paste from a spreadsheet), L19 (check result): topic-matched footage is
  reused (PDF viewer 136-144, cell filling 28-36 and 82-85), cross-faded.
