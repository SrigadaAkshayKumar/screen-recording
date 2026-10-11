# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | Projects, | 7.280 | A1 Projects sidebar icon | 17.600 | 2.42x |
| 2 | Projects. | 8.700 | A2 All projects sidebar item | 21.000 | 2.39x |
| 3 | Add | 10.260 | A3 Add new (+) button | 24.750 | 2.40x |
| 3 | Folder, | 11.860 | A4 New folder menu item | 26.000 | 0.78x |
| 3 | Create | 13.760 | A6 Create folder button | 36.100 | 2.95x |
| 5 | Open | 21.680 | A7 class-1 folder card | 56.200 | 2.54x |
| 5 | create | 22.960 | A9 Folder menu item | 62.000 | 2.81x |
| 5 | thumbnails, | 25.320 | A11 Create folder button | 67.900 | 2.50x |
| 5 | designs. | 27.740 | A15 Create folder button | 79.800 | 3.51x |
| 7 | Projects | 34.060 | A16 All projects sidebar item | 93.800 | 2.22x |
| 7 | organize | 36.520 | A17 thumbnail checkbox of Copy of sample | 98.400 | 1.87x |
| 8 | Choose | 39.680 | A18 Move icon in selection toolbar | 115.900 | 1.00x +1.5s hold |
| 8 | destination | 41.020 | A19 destination folder (class-1 then images) | 120.100 | 3.13x |
| 8 | confirm. | 42.440 | A20 Move button | 123.950 | 2.71x |
| 9 | folder, | 44.580 | A21 class-1 / images folder | 130.400 | 3.01x |
| 9 | Add | 45.680 | A12 Add new button (second time) | 73.000 | 2.45x |
| 11 | Remove | 53.980 | A22 three-dots menu on the item | 154.900 | 1.14x |
| 12 | Removing | 57.120 | A23 Remove from folder menu item | 160.000 | 1.62x |
| 13 | Trash | 62.080 | A24 Move to Trash menu item (hover only, not clicked) | 167.800 | 1.57x |
| 16 | Open | 75.020 | A25 class-1 folder | 194.900 | 2.09x |
| 16 | inside | 78.200 | A26 images folder | 197.200 | 1.00x +0.9s hold |

## Builder decisions

- intro: fast-forwarded src 0.00-10.80 instead of cutting it (junk: idle start on All projects)
- A6->A7: fast-forwarded src 40.00-55.50 instead of cutting it (junk: idle after folder created)
- A7->A9: cut src 57.00-59.20 - too long to fast-forward at <= 3.00x (junk: folder page loading)
- A11->A15: cut src 69.30-72.70 - too long to fast-forward at <= 3.00x (junk: waiting after thumbnails created)
- A15->A16: fast-forwarded src 81.00-93.00 instead of cutting it (junk: idle in class-1)
- A17->A18: cut src 99.50-115.30 - too long to fast-forward at <= 3.00x (junk: item selected, idle cursor)
- A12: after A21 (until src 131.60) jumps back to src 71.50 - narration order
- A21->A12: fast-forwarded src 69.30-72.70 instead of cutting it (junk: waiting after thumbnails created)
- A22: after A12 (until src 75.60) jumps ahead to src 148.00 - narration order
- A24->A25: fast-forwarded src 172.50-194.00 instead of cutting it (junk: unnarrated second move and idle)
