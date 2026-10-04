# Generator

`build.py` holds the page's data (actions, partners, calls, Mosaic steps) and writes `route1-hub.html` (artifact body) and `index.html` (standalone page). `hub.css` is the stylesheet it inlines.

Rebuild: `python3 build.py` (Python 3.9+, no dependencies), then copy `index.html` to the repository root and push. GitHub Pages redeploys in about a minute.

Earlier versions of the generator (long-scroll briefing-style v1, three-section v2) are kept in the group's local folder, not here.
