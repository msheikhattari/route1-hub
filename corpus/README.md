# Corpus: Howard County anti-trafficking Impact Group

Research behind the Route 1 Hub (the page served from this repo's root) and the Route 1 Briefing. The page does not link here; this folder is the knowledge base that future updates build on.

## Layout
- `CONTEXT.md` — the synthesis: group, curriculum, local landscape, numbers, impact menu, scripture, presentation guidance, events, grants, Mosaic, legislative session, contacts. Read this first.
- `impact-group-schedule.md` — the group's original schedule (Oct 2026 – Jan 2027).
- `research/01–15` — the full reports, one per thread:
  01 *When Helping Hurts* chapter by chapter · 02 Safe House Project study and OnWatch · 03 Howard County / Maryland landscape · 04 evidence and data · 05 scripture and Christian studies · 06 presenting to a mixed-tech group · 07 upcoming events and actions · 08 grants and funding · 09 Mosaic Christian Church · 10 2027 legislative session and regional events · 11 faith-space contacts · 12 Baltimore-region partners · 13 survivor-care orgs and corrections · 14 denominational contacts · 15 national faith-org contacts.
- `sources/` — text extracts and small PDFs of the public documents cited; `SOURCES.md` indexes them with URLs, including items kept online only.
- `CHANGELOG.md` — what was added when.

## Conventions
- Every report carries its compile date at the top. Treat names, phone numbers and event dates as true *as of that date*; re-verify before public use.
- Reports flag confidence inline: **verified** (seen on an official page or filing), **expected / pattern** (prior-year date, not confirmed), **unverified** (secondary or stale). Keep that habit when adding.
- Statistics: cite the primary source and say what was counted (hotline signals, police detections, modeled estimate, at-risk population).
- Privacy: this repo is public. No private home addresses, no personal phone numbers or emails; organizational contacts only.

## Adding to the corpus
1. New thread → new numbered file in `research/` with a date and a one-line scope at the top.
2. Corrections → edit the affected report *and* add a dated note under "Corrections" in `CHANGELOG.md`; do not silently overwrite findings.
3. Update `CONTEXT.md` with anything that changes a recommendation.
4. If the page should change, edit `generator/build.py` (data lists), rebuild, copy `index.html` to the repo root, commit, push.
