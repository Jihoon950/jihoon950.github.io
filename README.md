# Jihoon Lee — Academic portfolio

An English research portfolio for Jihoon Lee, Ph.D. student at Yonsei University.

**Live site:** https://jihoon950.github.io/

## Site

Static HTML, CSS, and JavaScript. GitHub Pages serves the committed files directly.
No Node build, theme runtime, database, or paid hosting is required.

- Editable Figma research illustrations exported as outlined SVG
- Demonstration record and a native video player with English-subtitled footage
- Postdoctoral availability statement and institutional contact link
- Publication filters, BibTeX citations, and citation download
- Responsive navigation and reduced-motion support
- Public English CV as a three-page PDF
- Shareable QR assets once the final Pages URL is configured

## Update content

Edit `content.json`, then run:

    python scripts/build_cv.py
    python scripts/build_site.py
    python scripts/check_site.py

The website build uses the Python standard library. PDF generation requires
ReportLab and the Arial font files in `C:/Windows/Fonts`; adjust the font paths
when building on another operating system. The PDF and generated HTML are
committed, so visitors and GitHub Pages do not need Python.

For QR generation, set `site_url` to the confirmed HTTPS Pages address in
`content.json`, install `requirements.txt`, and run:

    python scripts/build_qr.py
    python scripts/build_cv.py
    python scripts/build_site.py

QR generation verifies the PNG with an independent decoder.

## Preview

    python -m http.server 8000 --bind 127.0.0.1

Open `http://127.0.0.1:8000/`. Stop the server with Ctrl+C.

## Publish

Use the public repository `Jihoon950/jihoon950.github.io`. In Settings → Pages,
select **Deploy from a branch**, **main**, and **/ (root)**. The `.nojekyll` file
keeps the static files unchanged.

## Content notes

Professional content is adapted from the supplied CV and research portfolio.
Korean domestic-conference and patent titles are labeled as English translations.
Published, accepted, and submitted international papers share one publication
list, with accepted and submitted work explicitly marked. Manuscripts in
preparation have a subsection under Publications. Submission status follows
the author's confirmation in November 2026.
The planned MobiCom 2027 manuscript is not listed as submitted or accepted.
The AI-RAN Alliance All-Member Meeting demonstration is listed as scheduled for
November 11-12, 2026. Its authors follow the event flyer, independently of the
planned manuscript's author list. Update the demo status after presentation is
confirmed. The supplied 90-second MP4 is served unchanged, with its English
subtitles already visible in the footage; it loads only when the visitor plays it.
Stylesheet and downloadable CV URLs include content versions to refresh caches.
The public CV contains institutional contact details; the original application
documents are not part of this repository.

## Design references

Original implementation informed by these academic website structures:

- [Hugo Blox Academic CV](https://hugoblox.com/templates/academic-cv)
- [al-folio](https://alshedivat.github.io/al-folio/)
- [Academic Pages](https://academicpages.github.io/)

No theme source code is copied. Web typography uses Manrope and IBM Plex Mono
from Google Fonts, with local system fallbacks.

Research illustrations are editable in [Figma](https://www.figma.com/design/LtWOK0zR7GdSeaKhLr0zi7?node-id=2-2).
The four `assets/research-*.svg` files are exported directly from those frames,
with text outlined for consistent rendering. They are conceptual schematics,
not experimental result plots.
