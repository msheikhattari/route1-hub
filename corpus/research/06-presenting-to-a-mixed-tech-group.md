# Presenting the briefing to a mixed-tech church group — research summary (Oct 2026)
(compiled by Claude research agent; URLs inline)

## 1. Device reality
- Pew Mobile Fact Sheet (Nov 2025; fielded 2025): smartphone ownership 97% (18–29), 96% (30–49), 90% (50–64), **78% (65+)**; 17% of 65+ are smartphone-dependent (no home broadband). https://www.pewresearch.org/internet/fact-sheet/mobile/
- Pew (Jan 2026): 70% of 65+ have home broadband; only 14% of 65+ are online "almost constantly." https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/
- AARP 2026 Tech Trends (fielded fall 2025): 90% of 50+ own smartphones; **texting is now the lead communication method among 50+**; 3 in 5 say tech isn't designed with their age in mind. https://www.aarp.org/pri/topics/technology/internet-media-devices/2026-technology-trends-older-adults/
- Pew Religious Landscape Study (Feb 2025): median age of US Christians is 54; 50+ are a majority of evangelicals (54%), mainline (64%), Catholics (57%). https://www.pewresearch.org/religion/2025/02/26/age-race-education-and-other-demographic-traits-of-us-religious-groups/
- Takeaway: in a group of 8–15 with several 65+, expect 1–3 people with no smartphone or no home internet; most of the rest are comfortable texting.

## 2. Format choice
- Web page beats PDF on phones (NNG 2020, "PDF: Still Unfit for Human Consumption"): offer HTML first, PDF only as an optional printable. https://www.nngroup.com/articles/pdf-unfit-for-human-consumption/
- **Print retains better for informational text**: Delgado et al. 2018 meta-analysis (54 studies, n=171,055) paper advantage g=0.21, larger for expository text; Clinton 2019 replicated (g=−0.25 screens). https://eric.ed.gov/?id=EJ1212958
- Offer two formats when any member lacks a smartphone, the content is meant to be retained, and you want action later. All three apply here.
- Church practitioners: keep paper for those who want it; use QR signage + a volunteer helper (Church Communications Group). Channels churches actually use: GroupMe, Messenger, WhatsApp, SMS group chats, email (Subsplash 2026).
- **GroupMe ended SMS mode Aug 17, 2026** → no longer inclusive for app-averse members. A plain SMS/iMessage group text reaches everyone. https://groupme.com/blog/goodbye-sms-mode

## 3. Readability/accessibility on mobile
- No WCAG minimum font size, but never disable zoom (1.4.4). Practical target **18px body, 1.5 line-height** (NNG seniors study: "small type" the most persistent complaint). https://www.nngroup.com/articles/usability-for-senior-citizens/
- Line length 50–75 characters (Baymard); contrast 4.5:1 (WCAG 1.4.3); tap targets 24px min (WCAG 2.5.8), **44px preferred** (Apple; WCAG 2.5.5).
- **No sideways scrolling** at 320px (WCAG 1.4.10); only tables/charts/maps may scroll in their own box.
- Plain language: ≤2–3 abbreviations per document, spell out the rest (digital.gov). Write "Howard County Police," not "HCPD."
- Progressive disclosure: keep summary, actions, hotline numbers always visible; collapse stats detail/sources (NNG mobile accordions).
- tel: links dial after a confirmation alert on iOS; digits-only href, human formatting visible.
- Reading depth: users read ~20% of words; 57% of viewing time is above the fold, 74% within two screenfuls → summary + first action must fit in ~150–200 words.

## 4. Information architecture
- Inverted pyramid / BLUF / "what–so what–now what." Top summary 3–5 bullets, <100 words, headed "Start here."
- Contacts as cards with fixed field order: name, one-line role, phone (tel:), website, "call when…".
- Calendar: Google Calendar "add event" links work everywhere; .ics downloads are blocked inside a claude.ai artifact unless a downloads capability is declared (work fine on GitHub Pages).
- QR codes: 20% of 65+ find them difficult (YouGov 2021); in a 2025 HRS screener, 38% typed the URL rather than scan → **print both QR and a short typeable URL**.

## 5. Sharing mechanics
- **Claude Code artifacts**: private by default; switching to Public gives a link anyone can open with **no sign-in**. Logged-out viewers see a "Content is user-generated and unverified" label, cannot comment, and the page is served from a sandboxed *.claudeusercontent.com origin; self-initiated downloads are blocked. https://code.claude.com/docs/en/artifacts
- GitHub Pages: free, repo must be public, URL `https://<user>.github.io/<repo>/`, no banner, downloads work, shorter to type from print.
- Netlify Drop now effectively requires an account (anonymous drops are password-protected until claimed).

## 6. Recommendation for this group
1. One mobile-first HTML page, BLUF structure, no login (GitHub Pages for a short bannerless URL, or a public Claude artifact for speed).
2. One printed one-pager per person (Start here + actions + contacts in 14pt+), with QR **and** a short typed URL.
3. A plain SMS group text the morning after, with the link and the top three actions in the message body.
4. Optional print-styled PDF linked from the page.
Thursday delivery: hand out the one-pager as people sit; walk "Start here" aloud (2 min); have a younger member help neighbors scan/type; tap one tel: link together; everyone circles one action; send the group text Friday.
Page checklist: 18px/1.5 body, ≤75 cpl, 4.5:1 contrast, zoom on · tel: links in 44px targets · reflows at 320px · Start here + first action in two screens, ≤2 acronyms · calendar as Google Calendar links; printed short URL matches the live page.
