# Sync notes (script-19)
Plan built by work/hand_plan.py (234 s recording, 83.4 s voiceover): one footage piece per narration interval at 0.92-1.1x (all 0.75-1.5x), no holds, no zooms, no ripples (recorder zoom baked in), 15 cross-fades at line boundaries.

## Judgment calls
- Since the screen has no language-setting UI, each line got the closest-themed moving footage: L2 captions panel opening (60.6-64.3); L3 selecting the clip/timeline (150-155.6); L4 clip toolbar Captions button / panel with "Delete all captions" (106-110.2); L5 toolbar zoom on Captions (88-94); L6-L7 Styles tab (76.5-84.9); L8 font/captions panel (164-167.6); L9-L10 video playing, compare captions with audio (126.2-138.2); L11-L12 typing/editing transcript text (71-73.3, 67-70.3); L13-L14 captions panel, text styles (160.6-172); L15-L16 reviewing/editing caption "Edmeades" (191.8-203.3); L17 Share > Download panel (217-222.2).
- Skipped still spans (scenes.json stills: 9.1-14.4, 18-24.3, 46.4-56.2, 84.9-88.4, 96.4-103.6, 122.1-126.8, 140.97-148.7, 172-181, 184.7-190.9) and the idle opening hold; no span longer than 2.5 s of cursor-only footage is used.
- Audio order followed; source order is not (jumps are cross-faded).
- check.py --plan: no pace warnings. Remaining warnings: A1-A5 "not tied to a narration word" - intentional, the footage does not match the narrated steps closely enough to pin a click to a word.
- Not shown: the Download click itself (L17 ends on the download panel before the click).
