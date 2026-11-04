# script-04 report — Canva invoice PDF tutorial

## Result
- `projects/script-04/output/final.mp4`, 86.623 s (= voiceover), 3420x1922, 19 lines. **verify.py: PASS** (duration, streams, resolution, frozen spans, black frames at 32 joins).
- `check.py --plan`: OK, no `pace:` warnings. Speeds 0.76x–2.0x: the only 2.0x piece is in-scene dead time (Invite people page loading, 17.6–19.15 s); all footage that shows a click plays at 0.76–1.45x.
- freezedetect on the full-res final (n=0.003, d=1.4): longest 2.43 s (21.6 s, Orders list, cursor only), others 1.4–2.4 s. Nothing over 2.5 s. Longest hold 1.47 s (L2 and L12 1.4); closing hold 1.45 s.

## Stages
- probe, transcribe, align (19/19 lines `ok`), scenes, frames: **reused** (current; the voiceover was re-exported, 86.623 s, title line already cut).
- analyze/sync: no click log, recorder bakes in its own zooms -> (as in the earlier script-04 runs) a per-line hand plan `work/hand_plan.py` written from 0.5–1 s contact sheets and freezedetect on source and final, instead of actions.json/sync.json. No plan-level zooms/ripples. Same recording as the previous run (same hash), new voiceover timings, so the old plan was re-timed and then improved (below).
- preview rendered once, final rendered three times (final 1 had a 3.4 s cursor-only freeze in L7, final 2 a 4.6 s one when L7's static piece merged with L8's static start). verify PASS each time.

## Judgment calls
- Recording order: finished invoice open in Preview (0–13 s), Canva home 14 s, profile menu 16–24, Settings/Invite people 24–30, Orders and invoices 30–36, type filter 35–40, date filter 40–44, View invoice click 45.6 (new tab, downloading 46–50, dock 50, PDF opens 51), PDF 52–87, rename 59–68, "Your invoice has downloaded" 88–93 (static), Orders again 94–96.7.
- The take has **no** three-dot menu, no search typing, no Apple/Google/app-store, no email, no team switching. Those lines borrow the nearest real footage (marked no/partly).
- Fixed vs the previous plan: (a) L2 was 0.74x (below floor) -> footage starts 13.55 s, hold 1.47 s; (b) Settings->Orders chain was one 1.68x piece: now the approach to each click plays at 1.43–1.45x and only the Invite-people page load is 2.0x; (c) **View invoice click now lands at out 37.7 s on "Invoice"** (was ~1 s late): L9 and L10 were merged into one group so the approach plays through L9 and the click lands on the words, then the dark loading flash is cut (cross-fade) to the "downloading" screen; (d) L7 had a 3.3 s cursor-only freeze (open dropdown) -> pieces re-cut so the static part is ≤1.1 s and moving footage (dropdown opening, type -> date dropdown) surrounds it; (e) L12 now begins after the downloading screen so that screen is shown only ~2.1 s in L9/L10, then the dock appearing.
- Click landings: Settings click out ~17.05 ("Settings" 17.28), Orders click ~20.15 ("Orders" 19.82 / "Invoices" 20.66), View invoice click ~37.7 ("Invoice" 37.72).
- L3 shows the open profile menu before L4 opens it (the take opens the menu once); L4 cross-fades back to the click that opens it.
- Reused footage: homepage 14.3–16.2 (L2, L17), PDF details (L15/L16/L19), dropdown opening (L7, L8 end, L11) — out of order cross-fades, not frozen.
- 31 cross-fade joins; none inside a single click-to-result step.

## Per-line table (frames read from final.mp4 at each line start+0.3 s and middle)
| L | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0.0–6.54 | 71.8–77.4 | finished invoice PDF in Preview | partly (the result, an intro) |
| 2 | 6.54–11.54 | 13.55–16.25 + hold | Preview -> Canva home page, then menu opening, held | yes |
| 3 | 11.54–15.5 | 16.7–21.0 | profile menu open with account + team list | partly (no team switching in take) |
| 4 | 15.5–20.2 | 15.9–16.9, 23.7–29.9 | menu opens on "profile", click Settings ~17.05, Invite people page, cursor to Orders and invoices | yes |
| 5 | 19.22–22.0 | 28.4–31.5 | Orders and invoices click ~20.15, page loads | yes |
| 6 | 22.0–23.88 | 31.3–33.0 | Orders and invoices list, transaction row | yes |
| 7 | 23.88–29.0 | 35.0–38.4, 39.9–41.0 | "Any item type" filter opens, option list, moves on to the date filter | partly (no search typing) |
| 8 | 29.0–32.5 | 33.0–35.9 | list row: date, status, total payable; filter dropdown starts | yes |
| 9 | 32.5–36.1 | 41.6–45.65 | date filter list, cursor to the row, View invoice link | partly (filters stand in for "avoid wrong invoice") |
| 10 | 37.08–40.0 | 45.65, 46.3–48.0 | cursor on View invoice, click lands on "Invoice" (37.7), new tab "We're downloading your invoice" | yes |
| 11 | 40.0–43.06 | 39.8–42.3 | type dropdown -> date dropdown opening | **no** (no three-dot menu in take; dropdown stands in) |
| 12 | 43.06–47.7 | 48.4–51.2 + hold 1.4 | downloading screen, dock shows the downloaded PDF | yes |
| 13 | 47.7–53.1 | 51.2–57.3 | PDF opens, cursor on invoice no., selects total | yes |
| 14 | 53.1–57.38 | 58.4–62.6 | Preview title bar / file name field | yes |
| 15 | 57.38–65.22 | 77.2–83.4 | PDF invoice, cursor selects date/number/subscription | **no** (borrowed; no Apple/Google content) |
| 16 | 65.22–70.0 | 62.6–64.2, 83.0–84.8 + hold | PDF, selected Subscriptions block | **no** (borrowed) |
| 17 | 70.6–76.78 | 14.3–16.2, 93.4–96.7 + hold | Canva home, "Your invoice has downloaded", back on Orders | partly (no email in take) |
| 18 | 77.8–80.9 | 25.0–28.0 | Invite people page (team members) | partly |
| 19 | 81.42–86.14 | 84.4–87.3 + hold 1.45 | PDF invoice, closing hold | partly |

## Uncertain
- L11 (three-dot menu), L15/L16 (Apple/Google), L17 (email), L7 (search) have no matching footage; stand-ins as listed.
- L3 shows the open menu before L4 opens it; L7's dropdown opening repeats at the end of L8.
- Frames at 21.6–24 and 29.2–31.6 s are cursor-only (2.4 s each, just under the 2.5 s limit): that is the source's idle Orders list.

## Check these
- 15.5–22 s: menu -> Settings -> Orders chain (2.0x only on the page load).
- 23.9–29 s: filter pieces (cross-fades), 37–40 s: click on "Invoice" then dark-flash cut.
- 40–43 s (L11) stand-in dropdown; 57–70 s (L15/L16) borrowed PDF footage.

## Lessons added
- Yes, docs/lessons.md (2026-11-04 script-04).
