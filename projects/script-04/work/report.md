# script-04 report — Canva invoice PDF tutorial

## Result
- `projects/script-04/output/final.mp4`, 86.723 s (= voiceover), 3420x1922, 19 lines. **verify.py: PASS** (duration, streams, resolution, frozen spans, black frames at 32 joins).
- `check.py --plan`: OK, no `pace:` warnings. Speeds 0.76x–1.68x (1.68x only on the in-scene Settings -> Invite page -> Orders cursor travel/page load; all footage that shows a click is 0.76–1.13x).
- freezedetect on the final (d=1.5): 3.2 s 2.0 s (opening PDF idle), 21.7 s 2.3 s (orders list), 29.3 s 2.3 s (orders list), 65.5 s 1.9 s (rename typing), 79.8 s 1.7 s, closing hold 84.6-86.7 s (2.1 s). Longest hold 1.44 s, closing hold 2.1 s. No stretch over 2.5 s.

## Stages
- probe, transcribe, align (all 19 lines `ok`), scenes, frames: **reused** (done before this run). voiceover-cleanup had cut the 4.8 s title line.
- analyze/sync: no click log and the recorder bakes in its own zooms, so (as in earlier hand-plan projects) I looked at 0.5–1 s contact sheets over the whole take and wrote `work/hand_plan.py` (per-line pieces) instead of actions.json/sync.json. Plan: `work/plan.json`, no plan-level zooms/ripples (recorder zoom is already in the footage).
- preview rendered twice, final rendered twice, verify PASS on the second final.

## Judgment calls
- Recording order: it starts with the finished invoice open in Preview (0-13 s, static / jiggling window, not used), then Canva home 14 s, profile menu 16-24, Settings/Invite people 24-30, Orders and invoices 30-36, type filter 37-40, date filter 40-44, View invoice click 45.65 (new tab, downloading 46-50, dock 50, PDF opens 51), PDF read 52-58, rename 59-68, PDF idle/scroll 62-87, "Your invoice has downloaded" banner 88-93 (static), back to Orders 94-96.7.
- The recording has **no** three-dot menu, no search typing, no Apple/Google/app-store content, no email, no team switching. Those lines borrow the closest real footage (see table); this is stated per line.
- Profile menu: the take opens it before "Open your profile menu" is narrated, so L3 shows the open menu (teams/account list) and L4 jumps back (cross-fade) to the click that opens it, then on to the Settings click (out 16.8 s, "choose" is at 17.0).
- Orders click lands at out 20.26 s ("orders" 19.92 / "invoices" 20.76). View invoice click lands ~38.8 s (narration "Download invoice" 37.4-38.3): ~0.5-1 s late, because the click needs 1.35 s of approach footage at 0.84x and the line has only 2.9 s.
- Static downloading screen (46.3-49.8) is shown for ~2.3 s total (rest cut with cross-fade) to stay under the 2.5 s frozen rule; the loading dark flash at 45.8-46.2 is cut.
- Holds (<=1.5 s): L2 1.44, L9 1.4, L11 1.0, L12 1.4, L16 1.0, L17 1.0; closing hold 2.1 s on the PDF.
- Reused footage (explanatory lines only): L17 homepage 14.3-16.2 (also L2), L15/L16 PDF details, L16/L19 PDF overlap a little (83.0-83.4, 84.8).
- Cut/jumps (cross-fade): 14 joins; none inside a single step except the downloading-screen skip.

## Per-line table (checked on frames from final.mp4 at each line's start and middle)
| L | out window | source | what is shown | match |
|---|---|---|---|---|
| 1 | 0.0-6.8 | 71.8-77.4 | finished PDF invoice in Preview (scroll/zoom to the invoice) | partly (intro: result, not the download) |
| 2 | 6.8-11.6 | 13.6-16.25 + hold | Preview -> Canva home page, home page held | yes |
| 3 | 11.6-15.6 | 16.7-21.0 | profile menu open with account + team list | partly (no team switching exists in the take) |
| 4 | 15.6-19.3 | 15.9-16.9, 23.7-28.2 | menu opens (click at out 15.9, "profile"), cursor to Settings, click (out 16.8), Invite people page loads | yes |
| 5 | 19.3-22.1 | 28.2-31.5 | cursor to Orders and invoices, click (out 20.3), page loads | yes |
| 6 | 22.1-24.0 | 31.3-33.0 | Orders and invoices list with the transaction row | yes |
| 7 | 24.0-29.1 | 36.2-40.1 | Any item type filter opened, options (Credit, Licence, Print order, Subscription…) | partly (purchase-type filter only; no date filter, no search typing) |
| 8 | 29.1-32.6 | 33.0-35.9 | list row with date, status, total payable columns, cursor on the row | yes |
| 9 | 32.6-37.2 | 41.8-44.3 + hold | date filter list (Last 30/90/120 days) then table zoomed on the row | partly (filters standing in for "avoid wrong invoice") |
| 10 | 37.2-40.1 | 44.3-45.75, 46.3-47.3 | cursor on View invoice link, click (~38.8), new tab "We're downloading your invoice" | yes (click ~0.5-1 s after the words) |
| 11 | 40.1-43.2 | 40.1-41.8 + hold | date dropdown menu opening | **no** (no three-dot menu in the recording; a dropdown stands in) |
| 12 | 43.2-47.8 | 47.3-48.4, 49.8-51.2 + hold | "We're downloading your invoice", then dock shows the downloaded PDF | yes |
| 13 | 47.8-53.2 | 51.2-57.3 | PDF opens, cursor on invoice no. (~49.8, "number"), total/amount selected (~51.7, "total") | yes |
| 14 | 53.2-57.3 | 58.4-62.6 | Preview rename field with the file name | yes |
| 15 | 57.3-65.3 | 77.2-83.4 | PDF invoice, cursor selects invoice date/number/subscription | **no** (borrowed; recording has no Apple/Google content) |
| 16 | 65.3-70.7 | 62.6-64.2, 83.0-84.8 + hold | PDF (rename typing, then selected Subscriptions block) | **no** (borrowed) |
| 17 | 70.7-77.9 | 14.3-16.2, 93.4-96.7 + hold | Canva home, then back on Orders and invoices | partly (account/transaction list; no email in the take) |
| 18 | 77.9-81.5 | 25.0-28.0 | Invite people page (team members) | partly |
| 19 | 81.5-86.7 | 84.8-87.3 + closing hold | PDF invoice, closing hold | partly (end on the invoice) |

## Uncertain
- L11 (three-dot menu), L15/L16 (Apple/Google), L17 (email), L7 (date filter/search) have no matching footage; they show stand-in footage as listed.
- L10 click lands up to ~1 s after "Download invoice".
- L3 shows the open menu before L4 opens it.

## Check these
- 15.6-22.1 s: menu -> Settings -> Orders chain at 1.68x for the Invite people page.
- 38-40 s: new tab dark -> downloading cross-fade; 44-47 s hold + click.
- 40-43 s (L11) stand-in dropdown.
- 57-70 s (L15/L16) borrowed PDF footage; 65 s rename typing.

## Lessons added
- Yes, see docs/lessons.md (2026-11-03 script-04).
