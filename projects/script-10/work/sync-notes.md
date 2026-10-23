# sync notes (script-10)
plan.json is HAND-BUILT by `work/hand_plan.py` (recording 346 s vs voiceover 98 s, long idle spells; plan_builder cannot
slow footage below 1x). No sync.json was written; plan.sync is empty, so check.py lists A1-A14 as "not tied to a word".
Pieces (src -> out), all cross-faded except continuous joins:
| line(s) | src | out | speed |
|---|---|---|---|
| L1-2 intro | 2.2-7.9, 9.8-13.5 | 0-11.0 | 0.84-0.88x |
| L3 | 334.9-339.0 (Gemini new chat) | 11.0-15.98 | 0.82x |
| L4-6 Settings > PI > Connected apps > scroll > Canva | 26.1-33.0, 35.0-38.0, 42.3-44.0 | 15.98-24.94 | 1.45 / 1.27 / 0.92x |
| L7 connect | 44.0-46.8, 49.2-53.2 (loading 46.8-49.2 cut) | 24.94-30.78 | 1.0 / 1.3x |
| L8 authorize | 58.3-62.9 | 30.78-34.66 | 1.19x |
| L9 confirm enabled | 87.0-91.8 (second take) | 34.66-38.76 | 1.17x |
| L10 new chat + @ + pick Canva | 98.0-99.8, 103.7-109.6 | 38.76-45.5 | 1.0-1.2x |
| L11 typing prompt | 134-140, 142-146, 161-163, 190-193 | 45.5-58.0 | 1.0-1.8x |
| L12 result + open design | 223-227, 236-238.6 | 58.0-62.84 | 1.4 / 1.3x |
| L13 edit in Canva | 241.5-248.0 | 62.84-69.08 | 1.04x |
| L14-15 account | 277.2-280.8, 285.2-288.5 | 69.08-75.4 | 1.2 / 0.97x |
| L16-17 check account, back to Connected apps | 294.4-300.0, 300.0-302.0, 311.0-315.2 | 75.4-88.0 | 0.88-1.0x |
| L18 unlink | 324.2-327.8 | 88.0-91.62 | 1.0x |
| L19 sign in again | 332.4-334.5 (Connect to Canva? dialog) | 91.62-93.78 | 1.0x |
| L20 closing | 227.6-232.0 (Gemini result with Canva design) | 93.78-98.22 | 1.0x |

## Judgment calls
- Audio order followed. Jumps (cross-faded): the intro skips the idle Gemini screen (13.5-26 s); the long wait for the
  Canva design (191-223 s) and the loading screens (46.8-49.2, 238.6-241.5) are cut (loading screens: lessons).
- L9 uses the second Settings take (84-93 s) because it ends on Canva listed as Active; L4-6 use the first take.
- L11 typing is built from 4 pieces straddling the layout changes (143.5, 161.6, 190.5-191 s) so no static run exceeds ~2.9 s
  in output (verify's -60 dB freezedetect), at up to 1.8x. Text visibly grows in each piece but jumps between pieces.
- "off and back on" (L17) has no literal toggle in the recording: shows Canva's options menu (Use now / Unlink / Disconnect).
- No zooms and no ripples: the recorder baked zoom into the footage (lessons 2026-10-10 / 2026-10-11).
