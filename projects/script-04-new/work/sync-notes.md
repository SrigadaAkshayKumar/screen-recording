# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 2 | apps | 8.440 | A1 Apps in the left sidebar | 22.800 | 1.28x |
| 2 | BG | 10.760 | A2 Apps search field | 26.300 | 1.51x |
| 3 | Face | 13.680 | A3 Face Blur in Video app icon | 33.600 | 1.82x |
| 6 | Upload | 25.040 | A4 Choose file button | 50.600 | 1.09x |
| 6 | control, | 27.100 | A5 Open button in file dialog | 57.000 | 1.17x |
| 6 | strength. | 28.980 | A6 Intensity slider | 69.800 | 1.60x |
| 7 | select | 32.020 | A7 Gaussian blur style | 73.400 | 1.18x |
| 8 | Run | 33.960 | A8 Process your video button | 79.000 | 1.65x |
| 9 | Add | 37.540 | A10 Add to design button | 124.600 | 0.92x |
| 10 | Play | 42.900 | A11 Play button | 163.300 | 1.19x |
| 13 | blur | 61.520 | A14 Elements search field | 217.400 | 0.89x |
| 13 | frame | 63.480 | A15 blur graphic | 222.400 | 1.17x |
| 16 | Finish | 79.460 | A17 Add a heading | 277.600 | 1.10x |
| 16 | export | 81.120 | A19 Share button | 295.200 | 1.20x |
| 16 | MP4 | 82.940 | A20 MP4 Video file type | 298.900 | 1.10x |

## Judgment calls
- No zooms, no ripples: the recorder bakes in auto-zoom (many full-screen events) and there is no click log, so cursor positions are not reliable in recording pixels.
- Audio order followed. Anchors: apps/BG/Face on lines 2-3; Upload/control/strength (A4-A6) all in line 6, so the file dialog is shortened (folder browsing 52-56 s cut).
- Source 0-16.3 s (setup) is junk; the opening plays 16.4-22.8 s at 0.76x with no hold.
- Cuts (all cross-faded, reasons in sync.json): processing wait 80.6-114.6 (narration says wait for the result), Add to design spinner 126-136.8, idle 139.5-161 and 176.8-214.3, unmentioned transparency tweaks 232.5-258.5, idle Start-over hover 262.4-274, heading typing 278.8-294.4, still 46.3-48.1.
- A3 and A6 warnings: the app panel loads ~2.5 s after the click / the slider drag finishes after the word; accepted.
- Narration lines 11-12 (check faces, increase blur strength) have no matching footage: the timeline scrub (170-176 s) plays under them. Line 15 (BGBlur website) has no footage; it plays the 'Start over' panel (258-262 s) and the blur-graphic footage. A12, A13, A16, A18 are not anchored (extra clicks inside the played footage).
- Lines 13-14 (blur-shaped graphic): shown by searching Elements for blur and adding the graphic (214-232 s).
