# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Uploads | 7.520 | A1 Uploads icon in left sidebar | 15.100 | 1.76x |
| 3 | three | 12.040 | A2 three-dot menu on a thumbnail | 27.700 | 2.79x |
| 3 | Trash. | 14.480 | A3 Move to Trash in the menu | 37.300 | 3.93x |
| 4 | Projects, | 17.880 | A4 Projects in Canva home sidebar | 45.300 | 2.35x |
| 4 | All | 18.860 | A5 All projects | 53.900 | 2.35x |
| 4 | Uploads | 20.700 | A6 Uploads folder | 58.200 | 2.34x |
| 5 | three | 23.420 | A7 three-dot menu on Sample-Resume.Pdf - 1 | 69.200 | 1.69x |
| 5 | Trash. | 25.820 | A8 Move to Trash | 71.900 | 1.13x |
| 6 | thumbnail | 28.580 | A9 checkbox on New-canva-gif | 91.300 | 2.32x |
| 6 | tick | 29.320 | A10 checkbox on sample-resume.pdf (1) | 93.600 | 3.11x |
| 7 | trash | 32.920 | A11 trash icon in action bar | 99.600 | 1.67x |
| 7 | confirm | 34.840 | A12 Move to Trash confirm button | 100.800 | 1.00x +0.7s hold |
| 10 | selected | 46.380 | A13 design page | 116.000 | 1.32x |
| 12 | open | 54.100 | A14 All projects in sidebar | 142.200 | 3.39x |
| 12 | Trash, | 55.240 | A15 Trash in sidebar | 152.200 | 2.28x |
| 12 | item, | 56.320 | A16 checkbox on 'Copy of sample' in Trash | 165.800 | 2.78x |
| 12 | Restore | 57.340 | A17 Restore button | 169.500 | 1.76x |
| 13 | empty | 61.220 | A18 Empty Trash button | 179.400 | 2.55x |
| 15 | Return | 69.620 | A20 Untitled design tab | 190.900 | 1.37x |

## Builder decisions

- intro: fast-forwarded src 1.90-12.00 instead of cutting it (junk: idle design page before cursor moves)
- A4->A5: cut src 47.00-53.30 - too long to fast-forward at <= 2.00x (junk: cursor wandering / wrong 'Your projects' click)
- A6->A7: cut src 61.20-67.60 - too long to fast-forward at <= 2.00x (junk: cursor wandering over files)
- A8->A9: cut src 75.50-88.50 - too long to fast-forward at <= 2.00x (junk: idle after trash toast)
- A14->A15: cut src 143.40-150.80 - too long to fast-forward at <= 2.00x (junk: scrolling sidebar to find Trash)
- A15->A16: cut src 154.00-164.60 - too long to fast-forward at <= 2.00x (junk: cursor roaming Trash page)
- A16->A17: cut src 166.40-168.30 - too long to fast-forward at <= 2.00x (junk: cursor travel to Restore)

## Judgment calls
- Anchors: the word naming the control (Uploads, three-dot, Trash, Projects, All, tick, trash icon, confirm, selected, open, Restore, empty, Return). Repeated words use `occurrence` (line 4 "Uploads", line 12 "Trash").
- A9 on "thumbnail" and A10 on "tick" so the two checkbox clicks (2.3 s apart in the source) fit the 0.7 s of narration.
- A14 (All projects, home screen) anchored on "open", A15 Trash sidebar on the second "Trash"; A16 on "item" because "select" is only 0.66 s after "Trash".
- No zooms: the recorder already auto-zooms; ripples only.
- Cuts (junk that did not fit fast-forward at <= 2x): 47-53.3, 61.2-67.6, 75.5-88.5, 143.4-150.8, 154-164.6, 166.4-168.3. Intro 1.9-12.0 was fast-forwarded. Tail 196-202 (tab switch, desktop) trimmed.
- Narration L8-L11 (design-page delete vs uploads delete) has no matching footage action: design-page idle footage plays under it.
- A19 (Empty Trash confirm) has no anchor; it plays inside the A18->A20 interval.
- Warnings: A12's result (toast) shows after line 7 ends (acceptable); A19 unanchored.
