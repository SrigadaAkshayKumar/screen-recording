# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | First, | 6.300 | A1 File Explorer icon on the taskbar | 6.800 | 1.08x |
| 2 | confirm | 8.120 | A2 GIF file in the folder (double-click) | 9.950 | 1.73x |
| 4 | Uploads. | 15.480 | A3 Uploads in the Canva sidebar | 19.000 | 1.23x |
| 5 | Upload | 16.880 | A4 Upload files button | 20.900 | 1.36x |
| 5 | choose | 18.040 | A5 GIF file in the picker | 21.750 | 1.00x +0.3s hold |
| 5 | Open. | 19.400 | A6 Open button in the picker | 22.900 | 0.85x |
| 7 | click | 24.120 | A8 uploaded GIF thumbnail | 28.600 | 1.21x |
| 8 | Drag | 26.180 | A9 corner handle of the GIF | 32.000 | 1.65x |
| 8 | then | 28.080 | A10 GIF on the page | 33.500 | 0.79x |
| 9 | Play | 30.060 | A12 Play button | 48.500 | 1.28x |
| 10 | inspect | 36.260 | A13 GIF clip on the timeline | 56.050 | 1.22x |
| 10 | adjust | 38.320 | A14 end of the GIF clip on the timeline | 62.500 | 3.13x |
| 13 | download | 50.280 | A15 Share button | 95.950 | 2.80x |
| 13 | preserve | 51.340 | A16 Download in the Share panel | 98.000 | 1.93x |
| 14 | PNG | 53.380 | A17 File type dropdown | 100.000 | 0.98x |
| 15 | GIF | 56.880 | A18 GIF in the format list | 104.800 | 1.37x |
| 15 | MP4 | 58.540 | A19 MP4 Video in the format list | 108.950 | 2.50x |
| 17 | Share, | 69.520 | A20 Share button (second pass) | 122.850 | 1.15x |
| 17 | Download | 70.300 | A21 Download in the Share panel | 124.850 | 2.56x |
| 17 | format. | 72.020 | A22 GIF in the format list | 128.200 | 1.95x |
| 18 | Open | 73.260 | A23 Download button | 133.900 | 4.60x |
| 18 | movement. | 75.040 | A26 downloaded GIF in the folder (double-click) | 144.350 | 3.79x |

## Builder decisions

- A10->A12: auto-cut still span src 35.20-47.67 with a cross-fade
- A14->A15: fast-forwarded src 68.00-95.40 instead of cutting it (junk: idle timeline, browsing Images tab; nothing narrated)
- A19->A20: fast-forwarded src 110.00-120.90 instead of cutting it (junk: idle on the Download panel)
- A22->A23: fast-forwarded src 129.00-133.50 instead of cutting it (junk: idle on the Download panel)
- A23->A26: auto-cut still span src 135.40-139.10 with a cross-fade

## Judgment calls

- Order: the recording follows the narration, so no `src_from` jumps. The Share -> Download -> format flow was recorded twice;
  pass 1 (src 95.9-109.4) is used for L13-15 (formats), pass 2 (src 122.8-144) for L17-18.
- Anchors: A1 "First" / A2 "confirm" (open explorer, open the GIF); A3 "Uploads"; A4 "Upload"; A5 "choose"; A6 "Open"; A8 "click";
  A9 "Drag"; A10 "then" (move); A12 "Play"; A13 "inspect" / A14 "adjust" (timeline); A15 "download" / A16 "preserve" (Share, Download:
  the narration never says "Share" in L13); A17 "PNG" (format list opens), A18 "GIF", A19 "MP4"; A20 "Share", A21 "Download",
  A22 "format" (GIF chosen), A23 "Open" (Download button; the narration moves on to opening the file), A26 "movement" (opens downloaded GIF).
- Zooms: none, the recorder already zooms (baked-in camera moves); ripples only.
- Cuts: no manual cuts. Junk: context menu flash 121.0-122.3 and the tail after 149.5 are cut. Idle spans 68-95.4, 110-120.9, 129-133.5
  were marked ff and fast-forwarded. The builder cut two spans because they did not fit: 35.2-47.67 (cursor resting by Play, 12 s)
  and 135.4-139.1 (download toast). Both cross-faded.
- Tight windows: A23 approaches at 4.6x and A26 at 3.8x (download -> open the file is described in 2 s of narration, the recording took 10 s).
- Unnarrated actions without anchors: A7 (upload wait), A11 (idle by Play), A24 (download toast), A25 (explorer click).
- Narrated but without a distinct action: L11 "Preview the full section" (the clip extension and idle screen play there).
- A14 warning: its result appears at 40.1 s, after L10 ends (39.4 s); acceptable.
