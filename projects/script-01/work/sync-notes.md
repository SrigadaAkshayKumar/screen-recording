# Sync notes

| line | word | out time | action | src time | speed (approach) |
|---|---|---|---|---|---|
| 3 | Uploads, | 8.740 | A1 Uploads in the left sidebar | 48.400 | 1.08x |
| 3 | Files. | 10.500 | A2 Upload files button | 53.150 | 2.13x |
| 4 | select | 13.240 | A3 topmate_thumbnail file in the dialog | 77.000 | 1.37x |
| 4 | Open. | 14.320 | A4 Open button | 77.750 | 1.00x +0.3s hold |
| 7 | images, | 23.560 | A8 Images tab in the Uploads panel | 121.000 | 1.16x |
| 7 | videos, | 24.420 | A7 Videos tab in the Uploads panel | 110.750 | 1.69x |
| 8 | image | 26.860 | A6 uploaded image in the Uploads panel | 88.350 | 0.86x |
| 8 | video | 28.780 | A9 Videos tab in the Uploads panel | 184.150 | 1.46x |
| 8 | timeline. | 30.800 | A10 uploaded video | 187.850 | 1.83x |
| 9 | Explorer | 32.920 | A11 File Explorer icon in the taskbar | 200.950 | 1.23x |
| 9 | drag | 34.760 | A12 images (2) file in File Explorer | 205.750 | 2.61x |
| 14 | upload | 55.320 | A14 Upload in the Create a design list | 285.750 | 1.18x |
| 14 | finishes. | 59.340 | A18 open icon on the application.pdf upload toast | 308.300 | 2.72x |
| 15 | homepage, | 63.100 | A19 Home - Canva browser tab | 322.120 | 1.55x |
| 15 | Projects, | 64.100 | A20 Projects in the sidebar | 328.450 | 1.53x |
| 15 | Uploads. | 65.520 | A21 Uploads folder | 339.350 | 2.25x |

## Builder decisions

- A1->A2: cut src 50.30-51.30 - too long to fast-forward at <= 2.00x (cursor idles after the Uploads panel opens; makes room for 'then click Upload Files')
- A2->A3: cut src 55.00-75.10 - too long to fast-forward at <= 2.00x (junk: browsing folders in the file dialog looking for the file)
- A8: after A4 (until src 87.50) jumps ahead to src 119.80 - narration order
- A7: after A8 (until src 121.70) jumps back to src 110.00 - narration order
- A6: after A7 (until src 111.40) jumps back to src 86.90 - narration order
- A9: after A6 (until src 89.50) jumps ahead to src 182.50 - narration order
- A10->A11: cut src 189.50-200.00 - too long to fast-forward at <= 2.00x (junk: scrubbing the timeline after adding the video)
- A14->A18: cut src 288.60-294.60 - too long to fast-forward at <= 2.00x (junk: browsing folders in the file dialog for the PDF)
- A14->A18: cut src 297.00-302.60 - too long to fast-forward at <= 2.00x (PDF upload progress; narration says 'after processing finishes')
- A18->A19: cut src 312.50-320.50 - too long to fast-forward at <= 2.00x (idle on the imported PDF design)
- A19->A20: cut src 322.90-327.70 - too long to fast-forward at <= 2.00x (idle on the homepage before clicking Projects)
- A20->A21: cut src 330.60-338.30 - too long to fast-forward at <= 2.00x (hovering Recents and scrolling down to Folders (All projects page stays visible first))

## Judgment calls

- **No zooms.** The recorder already auto-zooms (padded window over a wallpaper, the camera pushes in on
  activity), so an added zoom would double-zoom (lessons.md, 2026-10-10). Ripples only.
- **Narration order wins (re-cut 2026-10-11 at the user's request).** L7's category tabs were clicked
  in the recording only after the image was placed (A6 88.35). The plan now plays A4's upload and the
  panel until src 87.5, then:
  - cross-fades ahead to src 120.0 for the Images tab (A8, "images");
  - jumps back to src 110.0 for the Videos tab (A7, "videos");
  - jumps back to src 86.9 for the image click (A6, "image");
  - jumps ahead to 182.5 for the Reel design (A9).

  Continuity side effect: during the tab clicks (about 23.0-25.2 s) the image is already on the page. It
  disappears at the jump back and is placed on "image" at 26.86.
- **Anchors.**
  - A1 "Uploads".
  - A2 "Files" with lead -0.1 (10.50) instead of "Upload" (10.12). Landing on "Upload" left 1.38 s for
    4.75 s of source (3.4x); with "Files" it runs about 2x.
  - A3 "select", A4 "Open", A8 "images", A7 "videos", A6 "image", A9 "video" (Videos tab in the Reel),
    A10 "timeline" (the click adds the video to the timeline), A11 "Explorer" (taskbar icon),
    A12 "drag", A14 "upload" (Upload in the Create menu).
  - A18 "finishes": the toast's open click comes after processing, so it lands on "finishes" and not on
    "open" (57.08). Anchoring it on "open" would need about 10x through the upload.
  - A19 "homepage", A20 "Projects", A21 "Uploads".
- **Unanchored:** A5 (upload wait), A13 (Create button), A15 (Upload files in the Create dialog), A16 (Open in
  the dialog) and A17 (PDF upload wait). They play inside their intervals at 1.2-2.7x. Canva has no Audio tab,
  so "audio" in L7 plays over the Videos tab's result.
- **Cuts** (junk from actions.json plus the cuts in sync.json):
  - wandering 6-45;
  - folder browsing in the dialog 55-75.1 and 288.6-294.6;
  - panel hover 89.5-109.8, the Designs/Folders tabs 111.5-120, the timer and switching designs 121.8-182.5;
  - timeline scrubbing 189.5-200;
  - a second .txt upload that opens as a Doc 225.5-281.3;
  - panel idle 50.3-51.3;
  - PDF upload progress 297.0-302.6 ("after processing finishes");
  - PDF design idle 312.5-320.5 and homepage idle 322.9-327.7;
  - scrolling Recents 330.6-338.3;
  - the tail from 347.6.
- **L10-L13** (no actions, about 17 s): the footage after the drag plays at about 1.2x. The dropped image sits in
  the Uploads panel and the page still shows the video, which illustrates "upload is not placement".
- **Hold:** 0.33 s at src 77.35 (file selected, before Open).
