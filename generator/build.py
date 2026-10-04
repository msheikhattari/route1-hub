# Builds route1-hub.html (artifact body) and index.html (standalone) from data below.
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote
import html as H

NY = ZoneInfo("America/New_York")
def gcal(title, start, hours, location="", details=""):
    s = datetime.fromisoformat(start).replace(tzinfo=NY)
    e = s + timedelta(hours=hours)
    fmt = lambda d: d.astimezone(ZoneInfo("UTC")).strftime("%Y%m%dT%H%M%SZ")
    return ("https://calendar.google.com/calendar/render?action=TEMPLATE&text=" + quote(title) +
            "&dates=" + fmt(s) + "/" + fmt(e) + "&location=" + quote(location) + "&details=" + quote(details))
def a(href, label, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{H.escape(href, quote=True)}">{label}</a>'
def tel(num, label=None):
    digits = "".join(ch for ch in num if ch.isdigit())
    if len(digits)==10: digits="1"+digits
    return f'<a class="tel" href="tel:+{digits}">{label or num}</a>'
def mail(addr): return f'<a class="mail" href="mailto:{addr}">{addr}</a>'

WILLIAMS = "Clarksville, MD (host home; address in the group email)"
GVM = "7280 Montgomery Rd, Elkridge, MD 21075"
GHB = "Banneker Room, George Howard Building, 3430 Court House Dr, Ellicott City, MD 21043"
PWD = "9830 Patuxent Woods Dr, Columbia, MD 21046"

# ---------------- CALENDAR ----------------
# cat: group | local | advocacy | online | money
CAL = [
 dict(d="Thu Oct 8", t="Coffee with a Cop, 9 AM", cat="local", why="Meet patrol officers before asking for a sextortion talk.", link=("Police events","https://www.howardcountymd.gov/events"), exp=False),
 dict(d="Tue Oct 13", t="Community Foundation of Howard County grant Q&A with Dee Athey, 4 PM", cat="money", why="Ask whether a church-sponsored project qualifies before Nov 2.", link=("Grant page","https://cfhoco.org/2026-community-grants/")),
 dict(d="Thu Oct 15", t="Group · Book ch. 2 · Study lesson 2, part 1 · 6–8 PM", cat="group", why="Write your 'poverty' words before reading.", g=("Impact Group: book ch. 2, lesson 2 pt 1","2026-10-15T18:00",2,WILLIAMS)),
 dict(d="Thu Oct 15", t="Unbound Now webinar on online exploitation, noon · Alliance to End Human Trafficking webinar on trafficking and domestic violence, 2 PM", cat="online", why="Two free lunchtime primers on the same day.", link=("Unbound series","https://unboundnow.org/trainings/connected-for-freedom/")),
 dict(d="Sat Oct 17", t="Route 1 prayer drive, 4 PM, Green Valley Marketplace", cat="group", why="Meet at the police substation.", g=("Route 1 Prayer Drive","2026-10-17T16:00",1,GVM,"Meet at the police substation in Green Valley Marketplace")),
 dict(d="Mon Oct 19", t="County Council public hearing, 7 PM, Ellicott City", cat="advocacy", why="Learn how three-minute testimony works before Route 1 items come up.", link=("Council legislation","https://apps.howardcountymd.gov/olis/")),
 dict(d="Thu Oct 22", t="HopeWorks candlelight vigil, 7–8 PM, Columbia", cat="local", why="Meet the county's victim-services staff; ask about their free trafficking workshop.", link=("Free tickets","https://www.eventbrite.com/e/domestic-violence-awareness-month-candlelight-vigil-2026-tickets-2001187684234"), g=("HopeWorks candlelight vigil","2026-10-22T19:00",1,"9770 Patuxent Woods Dr, Suite 100, Columbia, MD 21046")),
 dict(d="Mon Oct 26", t="Shared Hope \"JuST Faith\" pre-conference, 2–5 PM, Arlington VA, $45", cat="online", why="Nearest in-person faith training this fall; includes the Faith in Action book.", link=("Register","https://scurrystreet.swoogo.com/just2026")),
 dict(d="Oct 27–29", t="Shared Hope JuST Conference, Washington DC, $995", cat="online", why="Professional track only.", link=("Conference","https://www.justconference.org/")),
 dict(d="Thu Oct 29", t="Group · ch. 3 · lesson 2, part 2 · OnWatch training due", cat="group", why="Register the church as an OnWatch group first.", link=("OnWatch groups","https://www.iamonwatch.org/groups"), g=("Impact Group: book ch. 3, lesson 2 pt 2 (OnWatch due)","2026-10-29T18:00",2,WILLIAMS)),
 dict(d="Mon Nov 2", t="Community Foundation of Howard County community grants close, 11:59 PM", cat="money", why="Church as applicant; mini grants up to $5,000.", link=("Apply","https://cfhoco.org/2026-community-grants/")),
 dict(d="Thu Nov 5", t="Group · ch. 4 (relief, rehabilitation, development) · lesson 3", cat="group", why="Map local partners by stage, as the chapter asks.", g=("Impact Group: book ch. 4, lesson 3","2026-11-05T18:00",2,WILLIAMS)),
 dict(d="Sat Nov 7", t="Prayer drive, 4 PM · HopeWorks' Jewels for Hope sale, 8:30–2, Glen Mar Church, Ellicott City", cat="group", why="Mosaic's own first-Saturday prayer walk is the same morning.", link=("HopeWorks events","https://hopeworksofhc.org/events/list/"), g=("Route 1 Prayer Drive","2026-11-07T16:00",1,GVM)),
 dict(d="Thu Nov 12", t="Group · ch. 5 (asset-based) · lesson 4 · Unbound legislative webinar at noon", cat="group", why="Decide who attends Nov 19.", g=("Impact Group: book ch. 5, lesson 4","2026-11-12T18:00",2,WILLIAMS)),
 dict(d="Wed Nov 18", t="Montgomery County trafficking committee, noon–1:30, Rockville Library", cat="local", why="See how a mature county committee runs; confirm first.", link=("Committee","https://www.montgomerycountymd.gov/commission-women/human-trafficking")),
 dict(d="Thu Nov 19", t="Howard County trafficking council, public meeting, 1–3 PM", cat="local", why="Every local responder in one room. Introduce the group; offer the hotel audit.", link=("Council page","https://www.howardcountymd.gov/boards-commissions/human-trafficking-prevention-coordination-council"), g=("Howard County Human Trafficking Prevention Coordination Council (public)","2026-11-19T13:00",2,PWD,"Confirm location with the Office of Human Trafficking Prevention, 410-313-6558"), star=True),
 dict(d="Sun Nov 29", t="Advent begins · FAAST's free Advent guide for churches", cat="online", why="A ready-made way to put the topic in front of the whole church in December.", link=("Church toolkit","https://faastinternational.org/church-toolkit")),
 dict(d="Mon Nov 30", t="Walmart Spark Good local grant cycle closes", cat="money", why="$250 to $5,000; faith-based groups explicitly eligible.", link=("Guidelines","https://www.walmart.org/how-we-give/program-guidelines/spark-good-local-grants-guidelines")),
 dict(d="Tue Dec 1", t="HopeWorks volunteer applications open", cat="local", why="Spring 2027 season; six-month minimum; 18+.", link=("Volunteer","https://hopeworksofhc.org/volunteer/")),
 dict(d="Thu Dec 3", t="Group · ch. 6 · Indonesia Reconsidered · lesson 5", cat="group", why="Bring your Oct 1 answers.", g=("Impact Group: book ch. 6, lesson 5","2026-12-03T18:00",2,WILLIAMS)),
 dict(d="Sat Dec 5", t="Prayer drive, 4 PM", cat="group", why="", g=("Route 1 Prayer Drive","2026-12-05T16:00",1,GVM)),
 dict(d="Thu Dec 10", t="Group · ch. 7–9 · lesson 6 · Dressember for a Day · Unbound victim-services webinar at noon", cat="group", why="Dressember runs all month through IJM.", link=("Dressember","https://dressember.ijm.org/"), g=("Impact Group: book ch. 7–9, lesson 6","2026-12-10T18:00",2,WILLIAMS)),
 dict(d="Mon Dec 21", t="Howard County Delegation public hearing on 2027 local bills, 7 PM, Ellicott City", cat="advocacy", why="Every Howard County legislator in one room before session. Raise the hotel-training law.", link=("Delegation","https://www.howardcountymd.gov/state-delegation"), g=("Howard County Delegation public hearing on 2027 local bills","2026-12-21T19:00",2,GHB), star=True),
 dict(d="Thu Jan 7", t="Group · ch. 10 (how people change) · lesson 7 \"Mobilizing Your People\"", cat="group", why="Draft the pilot's proposal to church leadership.", g=("Impact Group: book ch. 10, lesson 7","2027-01-07T18:00",2,WILLIAMS)),
 dict(d="Sat Jan 9", t="Prayer drive, 4 PM · League of Women Voters legislative forum, Miller Branch library", cat="group", why="Forum date follows last year's pattern.", exp=True, g=("Route 1 Prayer Drive","2027-01-09T16:00",1,GVM)),
 dict(d="Mon Jan 11", t="National Human Trafficking Awareness Day · Wear Blue Day", cat="online", why="Two-minute announcement plus the hotline number.", link=("Blue Campaign","https://www.dhs.gov/blue-campaign/wear-blue-day")),
 dict(d="Wed Jan 13", t="Maryland General Assembly convenes, noon", cat="advocacy", why="Watch for re-filed bills: mandated-reporter, school curriculum, hotel-training penalties.", link=("Session dates","https://mgaleg.maryland.gov/Pubs/Other/2027rs-Session-dates.pdf")),
 dict(d="Thu Jan 21", t="Howard County trafficking council meeting, 1–3 PM", cat="local", why="January meeting sets the awareness event; volunteer the church as venue or table host.", exp=True, link=("Council page","https://www.howardcountymd.gov/boards-commissions/human-trafficking-prevention-coordination-council")),
 dict(d="Late Jan", t="Howard County awareness event and Red Sand ceremony", cat="local", why="2024: a panel in Columbia. 2025: a resource fair at the Elkridge 50+ Center. Bring ten or more members.", exp=True, link=("County page","https://www.howardcountymd.gov/human-trafficking-prevention")),
 dict(d="Thu Jan 28", t="Group · ch. 11 · lesson 8 · final session", cat="group", why="Decide what the pilot becomes.", g=("Impact Group: book ch. 11, lesson 8 (final)","2027-01-28T18:00",2,WILLIAMS)),
 dict(d="Late Jan–Feb", t="Maryland Human Trafficking Task Force Lobby Day, Annapolis", cat="advocacy", why="The statewide coalition meets Howard County's legislators.", exp=True, link=("Task Force","https://www.mdhumantrafficking.org/")),
 dict(d="Mon Feb 8", t="St. Josephine Bakhita Day of Prayer against Trafficking · Senate bill-introduction deadline", cat="online", why="Ecumenical prayer night; invite neighboring congregations. Toolkit is free.", link=("Bakhita toolkit","https://alliancetoendhumantrafficking.org/faith-resources/prayer-resources/")),
 dict(d="Feb", t="Mosaic Impact Weekend", cat="group", why="Last held Feb 26–28, 2026. Get an anti-trafficking partner on the roster.", exp=True, link=("Impact at Mosaic","https://mosaicchristian.org/impact/")),
 dict(d="~Feb 11", t="Maryland Catholic Conference virtual advocacy day", cat="advocacy", why="For Catholic members.", exp=True, link=("Advocacy day","https://www.mdcatholic.org/advocacyday/")),
 dict(d="Fri Feb 12", t="House bill-introduction deadline", cat="advocacy", why="If no hotel-penalty bill exists by now, it waits a year.", link=("Session dates","https://mgaleg.maryland.gov/Pubs/Other/2027rs-Session-dates.pdf")),
 dict(d="Feb–Mar", t="Committee hearings on trafficking bills", cat="advocacy", why="Written testimony needs a free MyMGA account and a PDF, in the window that opens two business days before each hearing.", link=("Witness sign-up","https://mgaleg.maryland.gov/mgawebsite/Committees/Testimony")),
 dict(d="Mar 11–12", t="Safe House Project Anti-Trafficking Alliance Conference, Charlotte NC", cat="online", why="Only if someone wants a deep dive with our study's authors.", link=("Conference","https://www.safehouseproject.org/events/atac-conference/")),
 dict(d="Thu Mar 18", t="Howard County trafficking council meeting", cat="local", why="Report back what the pilot did in January.", exp=True, link=("Council page","https://www.howardcountymd.gov/boards-commissions/human-trafficking-prevention-coordination-council")),
 dict(d="Mon Mar 22", t="Crossover Day in Annapolis", cat="advocacy", why="Last push of calls and emails on bills still alive.", link=("Session dates","https://mgaleg.maryland.gov/Pubs/Other/2027rs-Session-dates.pdf")),
 dict(d="Mon Apr 12", t="General Assembly adjourns", cat="advocacy", why="What passed, what to carry to 2028.", link=("Session dates","https://mgaleg.maryland.gov/Pubs/Other/2027rs-Session-dates.pdf")),
 dict(d="Sat May 16", t="United Methodist Peace with Justice grant deadline, up to $2,000", cat="money", why="Names trafficking explicitly; ecumenical groups qualify through a Methodist partner.", link=("Grant","https://www.bwcumc.org/ministries/love-like-jesus/peace-with-justice/")),
 dict(d="Sept 2027", t="Maryland Child Trafficking Awareness Conference, University of Maryland Baltimore", cat="online", why="Maryland's main statewide training day; send two or three next year.", exp=True, link=("Conference","https://www.marylandchildtraffickingconference.org/")),
]
ANYTIME = [
 ("A21 Global Freedom Summit", "Free, on demand since Oct 1, with a free host kit for a church watch night. This year's theme is online child sexual exploitation.", "https://www.a21.org/hostregistration"),
 ("Araminta \"Awaken\" training, part 1", "Free on Zoom; dates post on their Eventbrite page. The first step for any Araminta volunteer.", "https://www.eventbrite.com/o/araminta-63076676463"),
 ("HopeWorks \"Recognizing Human Trafficking\" workshop", "Free, at your location, for 8 to 30 people. Email chsevents@hopeworksofhc.org with two dates.", "https://hopeworksofhc.org/workshops/"),
 ("County presentation", "The Office of Human Trafficking Prevention presents to faith groups on request, in person or online.", "https://www.howardcountymd.gov/human-trafficking-prevention"),
 ("IJM Freedom Sunday", "Any Sunday; free sermon kit, kids' lesson, survivor stories.", "https://www.ijm.org/freedom-sunday"),
]

# ---------------- ACTIONS ----------------
# grp: now | project | long | give | avoid ; tags are stage labels
ACT = [
 dict(grp="now", t="Go to the county council meeting on November 19", tags=["Development"], body="1 to 3 PM, usually 9830 Patuxent Woods Dr. Introduce the group, ask what the January event needs, and ask the training-and-outreach subcommittee where volunteers fit. The highest-leverage hour on the calendar.", lead="Anyone free on a Thursday afternoon", cost="$0", links=[("Council page","https://www.howardcountymd.gov/boards-commissions/human-trafficking-prevention-coordination-council"),("Add to Google Calendar", gcal("Howard County Human Trafficking Prevention Coordination Council (public)","2026-11-19T13:00",2,PWD))]),
 dict(grp="now", t="Book a free county presentation for the whole church", tags=["Development"], body="The Office of Human Trafficking Prevention presents to faith groups on request. This is the pilot's first scaling step: it moves the topic from ten people to the congregation without us having to be the experts.", lead="Group facilitator with the church office", cost="$0", links=[("Request form","https://www.howardcountymd.gov/human-trafficking-prevention"),("Call", "tel:+14103136558")]),
 dict(grp="now", t="Book HopeWorks' free trafficking workshop at church", tags=["Development"], body="\"Recognizing Human Trafficking,\" taught by HopeWorks' community health team for 8 to 30 people at your location. Held in January it trains the pilot and recruits the next cohort in one evening.", lead="Group facilitator", cost="$0", links=[("Workshops","https://hopeworksofhc.org/workshops/"),("Email","mailto:chsevents@hopeworksofhc.org")]),
 dict(grp="now", t="Host Araminta's \"Awaken\" session", tags=["Development"], body="Free, on Zoom or in person. Araminta is the regional model for turning a congregation into trained, background-checked volunteers. Use their presentation form, not the general inbox.", lead="One host; invite neighboring churches", cost="$0", links=[("Request a presentation","https://form-usa.keela.co/request-a-presentation"),("Awaken dates","https://www.eventbrite.com/o/araminta-63076676463")]),
 dict(grp="now", t="Register the church as an OnWatch group", tags=["Prevention"], body="We are each taking the one-hour OnWatch training by Oct 29 anyway. Registering as a group earns \"OnWatch Advocate\" status when 90 percent complete, a concrete church-wide ask with a finish line.", lead="Whoever runs church communications", cost="$0", links=[("Group registration","https://www.iamonwatch.org/groups")]),
 dict(grp="now", t="Host an A21 Global Freedom Summit watch night", tags=["Prevention"], body="Free on demand with a free host kit. This year's theme is online child sexual exploitation, which pairs naturally with a parent night.", lead="Anyone with a screen and a room", cost="$0", links=[("Host kit","https://www.a21.org/hostregistration")]),
 dict(grp="now", t="Run the drives Araminta designed for church small groups", tags=["Relief"], body="Araminta's \"Serve On Purpose\" guide: a gift-card drive of 10 to 25 cards (rideshare, grocery, gas), \"Love Bags\" hygiene kits with handwritten notes, and a journal drive, dropped off by appointment. Also pantry items and holiday cards for HopeWorks and wish-list items for Catherine's Cottage. Confirm each list first.", lead="Rotates monthly", cost="Supplies", links=[("Serve On Purpose guide","https://aramintausa.org/wp-content/uploads/2026/03/Serve-On-Purpose.pdf"),("Email Araminta volunteers","mailto:volunteers@aramintausa.org"),("Email TurnAround","mailto:ksabater@turnaroundinc.org")]),
 dict(grp="now", t="Give the prayer drives a liturgy", tags=["Prayer"], body="Oct 17, Nov 7, Dec 5, Jan 9. Psalm 10:17–18, 12:5, 82:3–4; Proverbs 24:11–12; Isaiah 58:6. Send a courtesy note to the Elkridge Community Alliance, stay on public property, and do not approach motels. Mosaic's overseer David Ross already coordinates Route 1 prayer; loop him in.", lead="Prayer drive organizer", cost="$0", links=[("Scripture list","https://claude.ai/code/artifact/03868202-6b8d-4640-b968-d27ec289fefe#scripture")]),
 dict(grp="now", t="Wear Blue Day and a Bakhita prayer night", tags=["Prevention","Prayer"], body="January 11 is the national awareness day; a two-minute announcement with the hotline number is enough. February 8 is the international day of prayer against trafficking; the Catholic sisters' toolkit is free and ecumenical, and it is a natural night to invite neighboring congregations.", lead="Worship team", cost="$0", links=[("Blue Campaign","https://www.dhs.gov/blue-campaign/wear-blue-day"),("Bakhita toolkit","https://alliancetoendhumantrafficking.org/faith-resources/prayer-resources/")]),
 dict(grp="now", t="Put the topic in front of the church in Advent", tags=["Prevention"], body="FAAST's church toolkit includes a free Advent guide, a Lent guide, two Bible studies and a children's curriculum. Advent begins November 29.", lead="Worship or small-groups staff", cost="$0", links=[("FAAST church toolkit","https://faastinternational.org/church-toolkit")]),
 dict(grp="project", t="Audit hotel-training compliance in Howard County", tags=["Development"], body="Maryland requires every lodging employee to be trained and every property to certify yearly, yet 82 of 765 did in 2025 and nobody publishes a county breakdown. Request the Department of Labor's certification list under the Public Information Act, map every hotel and motel on the Route 1, I-95 and BWI corridor, hand the gap list to the county council, then offer non-compliant properties the free approved trainings through the county's Allied Business Program. Nobody else is doing this.", lead="Two or three people comfortable with spreadsheets", cost="$0", links=[("Baltimore Sun on compliance","https://www.baltimoresun.com/2026/09/01/human-trafficking-training-hotels/"),("The statute","https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?archived=False&article=gbr&enactments=False&section=15-210")]),
 dict(grp="project", t="Host a parent night on online safety and sextortion", tags=["Prevention"], body="The schools have nothing posted. Howard County Police's community outreach division presents on sextortion and internet safety on request, and the county's Family Institute offers \"Internet Safety 101 for Parents.\" Sextortion is the fastest-growing online threat to teenage boys.", lead="A parent in the group", cost="$0", links=[("Police outreach","tel:+14103132207"),("Email Family Institute","mailto:children@howardcountymd.gov"),("Police sextortion page","https://www.howardcountymd.gov/police/how-prevent-sextortion")]),
 dict(grp="project", t="Watch the 2027 legislative session", tags=["Advocacy"], body="Convenes Jan 13; bills must be introduced by Feb 8 (Senate) and Feb 12 (House); Crossover Day Mar 22; adjourns Apr 12. Likely re-files: the mandated-reporter bill that passed the House 133–0 and died in a Senate committee, and the grades 6–8 curriculum bill in its fifth year. Nobody has filed penalties for the hotel-training law; that is an open lane. Start with Delegate Pam Guzzone of District 13, who chairs the delegation and sponsored this year's law against illicit-massage advertising. The delegation's hearing on local bills is Dec 21 at 7 PM.", lead="One tracker; everyone for Lobby Day", cost="$0", links=[("Delegation office","tel:+14108413360"),("Bill index","https://mgaleg.maryland.gov/mgawebsite/Legislation/SubjectIndex/humant?ys=2026RS"),("Witness sign-up","https://mgaleg.maryland.gov/mgawebsite/Committees/Testimony")]),
 dict(grp="project", t="Maintain a dated local resource map", tags=["Rehabilitation"], body="Federal grant lapses in 2025 left referral lists stale. A living directory of housing, legal and record-relief, immigration, and language access (Spanish, Chinese, Korean, Vietnamese) would feed the county council's new data-collection tool.", lead="One owner, quarterly refresh", cost="$0", links=[("Maryland Task Force resource library","https://www.mdhumantrafficking.org/resource-library")]),
 dict(grp="project", t="Publish a rumor-response protocol for the congregation", tags=["Prevention"], body="A one-page \"we checked this\" process for viral claims (zip ties, Super Bowl, \"300,000 kids\"). Polaris says misinformation drowns real callers; a church that models restraint is itself a prevention tool.", lead="The group, using the checklist in Numbers", cost="$0", links=[("Polaris on rumors","https://polarisproject.org/human-trafficking-rumors/")]),
 dict(grp="project", t="Bring prevention education to The Children's Home", tags=["Prevention"], body="Mosaic already runs a Saturday flag-football group with teenagers placed in Catonsville after abuse or neglect, exactly the population traffickers recruit. HopeWorks or Araminta could deliver prevention education there. The most natural first project the church already has access to.", lead="The flag-football leaders with Mosaic's Local Impact Director", cost="$0", links=[("The Children's Home","https://www.thechildrenshome.net/"),("Email Impact at Mosaic","mailto:impact@mosaicchristian.org")]),
 dict(grp="project", t="Get an anti-trafficking partner onto Mosaic's Impact Weekend roster", tags=["Development"], body="Impact Weekend is billed as the best way for the congregation to meet local organizations and start year-round partnerships. The last one was late February 2026. Propose Araminta or HopeWorks for a table and a short stage slot.", lead="Group leader with the Local Impact Director", cost="$0", links=[("Impact at Mosaic","https://mosaicchristian.org/impact/"),("Email","mailto:impact@mosaicchristian.org")]),
 dict(grp="project", t="Apply for a faith seat, and for the new Interfaith Advisory Commission", tags=["Development"], body="The county trafficking council reserves two seats for the faith community; applications go through the county boards page. Separately, Howard County created an Interfaith Advisory Commission in April 2026 that meets quarterly starting this fall and is accepting inaugural members.", lead="One group member with time for bi-monthly meetings", cost="$0", links=[("Apply to serve","https://www.howardcountymd.gov/applybc"),("Interfaith Advisory Commission","https://www.howardcountymd.gov/boards-commissions/interfaith-advisory-commission")]),
 dict(grp="long", t="Araminta certified volunteer or mentor", tags=["Rehabilitation"], body="Awaken training first, then a fingerprint background check. Mentors commit one year, two outings a month, weekly contact. Survivor advocate and prayer-team roles also exist.", lead="Individuals", cost="$0", links=[("Volunteer form","https://form-usa.keela.co/volunteer-interest-form-vif"),("Prayer team","https://form-usa.keela.co/volunteer-for-our-prayer-team")]),
 dict(grp="long", t="HopeWorks volunteer", tags=["Rehabilitation"], body="Applications open December 1 for spring 2027. 18+, background check, orientation, six-month minimum. Group projects need five people and three weeks' notice; new group volunteers do not work directly with clients.", lead="Individuals", cost="$0", links=[("Volunteer","https://hopeworksofhc.org/volunteer/"),("Email Kate Kurlychek","mailto:kkurlychek@hopeworksofhc.org")]),
 dict(grp="long", t="TurnAround on-site roles, or a Human Trafficking 101 for the church", tags=["Rehabilitation"], body="Howard County's state-designated responder. On-site roles (helpline, pantry, front desk) need a background check and self-paced training. They also teach a \"Human Trafficking 101\" for churches on evenings and weekends.", lead="Individuals; facilitator for the 101", cost="$0", links=[("Volunteer","https://www.turnaroundinc.org/volunteer/"),("Email community engagement","mailto:communityengagement@turnaroundinc.org")]),
 dict(grp="long", t="Shared Hope Ambassador of Hope", tags=["Prevention"], body="Free online training, 16+, one reference letter; ambassadors present to churches, schools and civic groups. Shared Hope's DC office is on 16th Street.", lead="Individuals who like to present", cost="$0, optional $89 toolkit", links=[("Ambassadors of Hope","https://sharedhope.org/aoh/")]),
 dict(grp="long", t="Howard County resource parent", tags=["Prevention"], body="Foster care and running away are the pipeline into trafficking, and the county trains foster parents on it. Requires a home study and clearances.", lead="Families", cost="$0", links=[("Call DSS","tel:+14108728839")]),
 dict(grp="long", t="UMD SAFE Center volunteer", tags=["Rehabilitation"], body="Mentoring, tutoring, interpretation, court accompaniment for survivors in Prince George's and Montgomery; a faith-group training can be requested.", lead="Individuals; attorneys for pro bono", cost="$0", links=[("Get involved","https://umdsafecenter.org/get-involved/"),("Request a training","https://umdsafecenter.org/contact-us/request-a-training/")]),
 dict(grp="give", t="Community Foundation of Howard County", tags=["Money"], body="Community grants close Nov 2; mini grants up to $5,000 for nonprofits under five years old. Ask Dee Athey whether a church-sponsored project qualifies.", lead="Church as applicant", cost="", links=[("Grants","https://cfhoco.org/2026-community-grants/"),("Call","tel:+14107307840")]),
 dict(grp="give", t="Walmart Spark Good local grants", tags=["Money"], body="$250 to $5,000; faith-based groups explicitly eligible. Current cycle closes Nov 30; the next opens about Feb 1.", lead="Church as applicant", cost="", links=[("Guidelines","https://www.walmart.org/how-we-give/program-guidelines/spark-good-local-grants-guidelines")]),
 dict(grp="give", t="Thrivent Action Teams", tags=["Money"], body="$250 seed kits for member-led projects, any time, two weeks' notice. Ask whether anyone in the congregation is a Thrivent member.", lead="A Thrivent member", cost="", links=[("Action Teams","https://www.thrivent.com/about-us/membership/thrivent-action-teams")]),
 dict(grp="give", t="Howard County Community Service Partnership grants", tags=["Money"], body="Usually open in November or December and close in January; require a 501(c)(3) human-services nonprofit, so the church or HopeWorks would be the applicant. Join the notification list now.", lead="Church or a partner", cost="", links=[("Program","https://www.howardcountymd.gov/community-partnerships/community-service-partnership-grants-program"),("Notification list","https://lp.constantcontactpages.com/sl/yVDYkX6")]),
 dict(grp="give", t="United Methodist Peace with Justice grants", tags=["Money"], body="Up to $2,000, due May 16, names trafficking explicitly; ecumenical groups qualify through a Methodist partner such as Bethany or Glen Mar.", lead="With a Methodist partner", cost="", links=[("Grant","https://www.bwcumc.org/ministries/love-like-jesus/peace-with-justice/")]),
 dict(grp="give", t="Dressember and Freedom Partners", tags=["Money"], body="Dressember runs all of December through IJM and is a visible whole-church fundraiser. If the pilot wants to fund a local partner instead, pair it with a parallel ask for Araminta or HopeWorks.", lead="Anyone", cost="", links=[("Dressember","https://dressember.ijm.org/")]),
]
AVOID = ["Independent motel outreach or handing out hotline cards without TurnAround or the county.", "Untrained street outreach.", "Starting a shelter: the Nazarene church guide calls it \"the grandest of actions\" that \"may come from a place of pride.\"", "Showing Sound of Freedom without a correction.", "Quoting \"300,000 children.\"", "Any help conditioned on religious participation; survivors describe it as a second coercion."]

# ---------------- PARTNERS ----------------
PART = [
 ("Howard County government", [
  dict(n="Office of Human Trafficking Prevention", s="County · since 2017", w="County lead on sex and labor trafficking; staffs the council; multilingual fliers; Allied Business Program for hotels and shops.", p="Free presentations to faith groups. Ashton Petta, manager, is the gateway to everyone below.", c=[tel("410-313-6558"), mail("ohtp@howardcountymd.gov"), a("https://www.howardcountymd.gov/human-trafficking-prevention","County page")]),
  dict(n="Human Trafficking Prevention Coordination Council", s="County law CB 52-2019 · 19–23 members", w="Police, State's Attorney, social services, schools, HopeWorks, a survivor leader, HoCo AGAST, two faith seats. Vice chair Fr. Travis K. Smith.", p="Public meetings every other month, 1 to 3 PM; next Nov 19. Faith-seat applications through the county boards page.", c=[a("https://www.howardcountymd.gov/boards-commissions/human-trafficking-prevention-coordination-council","Council page"), a("https://www.howardcountymd.gov/applybc","Apply to serve")]),
  dict(n="Howard County Police community outreach", s="County", w="Presentations on trafficking, sextortion and internet safety, case by case; a free 12-week Citizens Police Academy includes a trafficking module.", p="Request a presentation for a parent night; ask about the next academy cohort.", c=[tel("410-313-2207"), mail("HCPDOutreach@howardcountymd.gov"), a("https://www.howardcountymd.gov/police/get-involved","Get involved")]),
  dict(n="Interfaith Advisory Commission", s="County · created April 2026", w="New quarterly commission under the Office of Human Rights and Equity.", p="Inaugural-member applications are open. A faith voice on trafficking belongs here.", c=[a("https://www.howardcountymd.gov/boards-commissions/interfaith-advisory-commission","Commission page")]),
  dict(n="Howard County Delegation", s="State legislators", w="Delegate Pam Guzzone (District 13) chairs it and sponsored this year's illicit-massage advertising law; Delegate Terri Hill co-sponsored several trafficking bills; Delegate Jessica Feldmark sits on the committee that hears the school-curriculum bill.", p="Public hearing on 2027 local bills Dec 21, 7 PM. Written testimony through a free MyMGA account.", c=[tel("410-841-3360"), a("https://www.howardcountymd.gov/state-delegation","Delegation page")]),
  dict(n="Maryland Human Trafficking Task Force", s="Statewide · led by the US Attorney", w="The statewide coalition; legislative committee runs an annual Lobby Day in Annapolis; resource library with recorded trainings.", p="Join a committee; attend Lobby Day; a recorded January 2026 session explains how local task forces work.", c=[a("https://www.mdhumantrafficking.org/","Task Force"), a("https://www.mdhumantrafficking.org/resource-library","Resource library")]),
 ]),
 ("Local responders", [
  dict(n="TurnAround, Inc.", s="Howard County's state-designated responder · Columbia office", w="Drop-in, street outreach, shelter, free trauma therapy, legal advocacy; regional navigator for anyone under 24 suspected of being trafficked (Julie Harrison).", p="Supply drives, event volunteers, on-site roles, and a \"Human Trafficking 101\" for churches. Hiring a Howard County outreach coordinator.", c=[tel("443-279-0379","24/7 443-279-0379"), mail("ksabater@turnaroundinc.org"), mail("communityengagement@turnaroundinc.org"), a("https://www.turnaroundinc.org","turnaroundinc.org")]),
  dict(n="HopeWorks of Howard County", s="Columbia · executive director Ngozi Obineme", w="Sexual and intimate-partner violence center that also serves trafficking survivors; monthly trafficking peer-support group; counseling.", p="Free \"Recognizing Human Trafficking\" workshop for 8 to 30 at your location; pantry and gift-card drives now; volunteer applications open Dec 1.", c=[tel("410-997-2272","24-hr 410-997-2272"), mail("chsevents@hopeworksofhc.org"), mail("kkurlychek@hopeworksofhc.org"), a("https://hopeworksofhc.org","hopeworksofhc.org")]),
  dict(n="Grassroots Crisis Intervention", s="Columbia · day resource center in Jessup on Route 1", w="Crisis center and homeless services; already on Mosaic's referral list; one of four partners the county names for volunteering.", p="Library drop-ins (Elkridge Branch, second Wednesdays 10 to 1); day-center shifts; drives.", c=[tel("410-531-6677","24-hr 410-531-6677"), mail("kathyp@grassrootscrisis.org"), a("https://grassrootscrisis.org/volunteer/","Volunteer")]),
  dict(n="Catherine's Cottage", s="Salvation Army · Baltimore", w="Maryland's only emergency shelter exclusively for adult trafficking survivors, since 2017. Program manager Jaleesa Thomas; a Salvation Army family-services office sits in Ellicott City (Sue Hunt).", p="Wish-list drives; a speaker; ask what they need this quarter. It is a secure house; do not ask to visit.", c=[tel("410-783-2920","410-783-2920 ext. 50110"), tel("443-656-3376","Ellicott City 443-656-3376"), a("https://sa-md.org/centralmaryland/anti-human-trafficking/","Program page")]),
  dict(n="Esperanza Center", s="Catholic Charities · Baltimore", w="Federally funded case management and legal help for immigrant trafficking victims.", p="Referral partner for labor-trafficking cases; victim-services line.", c=[tel("667-600-2906"), a("https://cc-md.org/programs/esperanza-center/","Esperanza Center")]),
  dict(n="UMD SAFE Center", s="College Park · serves Prince George's and Montgomery", w="Case management, legal, mental health, economic empowerment; research; wrote Prince George's contractor anti-trafficking ordinance.", p="Request a faith-group training; donation-drive toolkit; long-term volunteer roles.", c=[tel("301-314-7233"), a("https://umdsafecenter.org/contact-us/request-a-training/","Request a training")]),
 ]),
 ("Faith-based organizations", [
  dict(n="Araminta Freedom Initiative", s="Baltimore · Christian, church-mobilizing · executive director Rhonda Sanco", w="Prevents child sex trafficking; mentoring and clinical care; the region's model for turning congregations into trained volunteers. Volunteer manager Pascale Lebrun-Gay.", p="Free \"Awaken\" talk, then training, then fingerprinted volunteer roles. A drives guide written for church small groups. Zoom prayer team Mondays and Wednesdays at noon.", c=[a("https://form-usa.keela.co/request-a-presentation","Request a presentation"), tel("443-934-0003"), mail("contact@aramintafreedom.org"), mail("volunteers@aramintausa.org")]),
  dict(n="FAAST", s="Faith Alliance Against Slavery and Trafficking · Towson", w="Publishes Hands That Heal, the standard faith-based caregiver curriculum, plus a free church toolkit. Members include the Salvation Army and World Relief; no Maryland church yet.", p="$100-a-year church affiliate; Freedom Sunday any Sunday; host a caregiver training locally.", c=[mail("faast@faastinternational.org"), a("https://faastinternational.org/church-toolkit","Church toolkit")]),
  dict(n="Alliance to End Human Trafficking", s="Catholic sisters' network · national", w="Speaker's bureau, free parish study modules, Bakhita day toolkit. Advocacy director Marilyn Zigmund Luke is based in Maryland; program director Christine Commerce books speakers.", p="Request a speaker with four weeks' notice; use the free prayer and study resources.", c=[a("https://alliancetoendhumantrafficking.org/speaker-request/","Speaker request"), tel("267-332-7768")]),
  dict(n="Salvation Army Eastern Territory", s="Anti-trafficking program", w="Named contact for trained speakers on trauma-informed care: Arielle Curry, program coordinator.", p="Speaker or training request by email.", c=[mail("arielle.curry@use.salvationarmy.org"), a("https://www.salvationarmyusa.org/usa-eastern-territory/fight-for-justice/","Fight for Justice")]),
  dict(n="Safe House Project", s="Virginia Beach · authors of our study", w="OnWatch training, national safe-house certification, emergency response line; co-leads Frederick County's task force.", p="OnWatch group status at 90 percent completion; Ambassador and response-line volunteer roles; the study's lesson guides are behind a free login.", c=[tel("1-833-523-7233","1-833-5-BESAFE"), a("https://www.iamonwatch.org/groups","OnWatch groups"), a("https://www.safehouseproject.org/volunteer/ambassador/","Ambassadors")]),
  dict(n="International Justice Mission", s="Washington, DC", w="Global; Freedom Sunday kit; local prayer-gathering toolkit; Dressember; the best off-the-shelf church curriculum, God of Justice.", p="Church contact Stefani Johnson; speakers for sermons and workshops.", c=[mail("sjohnson@ijm.org"), a("https://www.ijm.org/get-involved/churches","Churches page")]),
  dict(n="Shared Hope International", s="Vancouver WA · DC office on 16th Street", w="State report cards (Maryland got an A overall, a C on protecting survivors from arrest); Faith in Action kit; Ambassadors of Hope.", p="Ambassador training is free; the $75 kit is the most church-ready single purchase.", c=[mail("awareness@sharedhope.org"), a("https://sharedhope.org/aoh/","Ambassadors of Hope"), a("https://store.sharedhope.org/product/faith-action-kit/","Faith in Action kit")]),
  dict(n="Set Free Movement", s="Free Methodist roots · open to any church", w="Starts church teams at no cost with a five-session onboarding cohort; free Freedom Sunday kit.", p="\"Start a Team\" if the pilot wants a national framework without fees.", c=[mail("team@setfreemovement.org"), a("https://setfreemovement.com/start-a-team","Start a Team")]),
  dict(n="Send Relief", s="Southern Baptist", w="Free 35-minute course \"How to Fight Human Trafficking,\" a 30-day prayer guide, a backpack-ministry guide; church speaker and materials request form.", p="The quickest free training for the whole congregation.", c=[a("https://courses.sendrelief.org/courses/how-to-fight-human-trafficking/","Free course"), a("https://sendrelief.formstack.com/forms/church_requests","Church request form")]),
  dict(n="Institute for Survivor Care", s="Formerly The Samaritan Women · now Kentucky", w="Trains faith-based ministries nationally; EquipU online courses, free to $35; a program for ministry founders.", p="Director of community engagement Linda Blackiston; online courses for anyone moving toward survivor care.", c=[mail("lblackiston@instituteforsurvivorcare.org"), a("https://equipu.learnupon.com/store","EquipU courses")]),
 ]),
 ("Churches and denominations nearby", [
  dict(n="HoCo AGAST", s="Volunteer faith coalition · founded 2011 · lead organizer Sara Cochran", w="Holds a seat on the county council; runs a \"Compassion Brigade\" that attends trafficking sentencings.", p="Ask how a church group plugs in and what they have learned churches should not do. Reach them through Ashton Petta or Facebook.", c=[a("https://www.facebook.com/HoCoAGAST/","Facebook")]),
  dict(n="Bethany UMC", s="Ellicott City", w="Lists \"rehabilitating living space for victims of human trafficking\" among its missions.", p="Ask who leads it; a Methodist partner also unlocks the Peace with Justice grant.", c=[tel("410-465-2919"), mail("bumc@bethanyum.org")]),
  dict(n="Glen Mar UMC", s="Ellicott City", w="Hosts HopeWorks' Jewels for Hope sale on Nov 7; partners with Grassroots, My Sister's Place and Bridges to Housing Stability.", p="Meet their missions people at the sale.", c=[tel("410-465-4995"), mail("office@glenmarumc.org")]),
  dict(n="Grace Episcopal Church", s="Elkridge", w="Fr. Travis K. Smith, vice chair of the county council, was rector here; the parish now has an interim rector.", p="An Elkridge neighbor on the corridor; reach Fr. Smith through the county office.", c=[tel("410-796-3270"), mail("graceoffice@graceelkridge.org")]),
  dict(n="St. Louis Catholic Church", s="Clarksville · pastor Rev. Michael DeAscanis", w="Hosted an Araminta presentation in 2017 through the Catholic Medical Association guild.", p="Ask the parish office who handles social ministry.", c=[tel("410-531-6668"), mail("parishoffice@slcmd.org")]),
  dict(n="Sisters of Bon Secours", s="Marriottsville, Howard County", w="Name trafficking a justice priority; members of the Alliance to End Human Trafficking. Their retreat center welcomes church groups.", p="A local retreat venue for the group; ask for the justice coordinator.", c=[tel("410-442-3120","Retreat center 410-442-3120"), mail("carol.jessee@bonsecoursusa.org")]),
  dict(n="Baltimore-Washington Conference, United Methodist", s="Fulton, Howard County", w="Justice ministries coordinator Courtney Morris; trafficking is a named Peace with Justice priority; grants up to $2,000 due May 16.", p="The nearest denominational justice desk, ten minutes from Clarksville.", c=[mail("cmorris@bwcumc.org"), tel("410-309-3423")]),
  dict(n="Maryland Catholic Conference", s="Annapolis", w="Testified for this year's navigator-reporting bill; virtual advocacy day each February; parish toolkit with hotline posters in several languages.", p="Legislative alerts; posters for church restrooms.", c=[tel("410-269-1155"), a("https://www.mdcatholic.org/parish-resources/respect-life/trafficking/","Parish toolkit")]),
 ]),
]

# ---------------- LEARN ----------------
LEARN = [
 ("60 min","OnWatch","Survivor-led, free, ten modules. Our Oct 29 assignment. Register the church as a group first.","https://www.iamonwatch.org/"),
 ("35 min","Send Relief: How to Fight Human Trafficking","Eight short videos, free registration, Spanish captions.","https://courses.sendrelief.org/courses/how-to-fight-human-trafficking/"),
 ("30 min","Truckers Against Trafficking","Free certificate course with a general-public track.","https://train.tatnonprofit.org/"),
 ("40 min","The Exodus Road TraffickWatch Academy","Two modules and a certificate, free.","https://theexodusroad.com/traffickwatch/"),
 ("Self-paced","Polaris Human Trafficking 101","Six modules; the county recommends it as a baseline.","https://polarisproject.org/human-trafficking-101/"),
 ("2 hrs","Araminta Awaken, part 1","Free on Zoom; required before any Araminta volunteer role.","https://www.eventbrite.com/o/araminta-63076676463"),
 ("Evening","HopeWorks Recognizing Human Trafficking","Free, at church, 8 to 30 people.","https://hopeworksofhc.org/workshops/"),
 ("13–16 hrs","Safe House Project Ally Training","$275, self-paced, certificate; lists faith leaders as an audience.","https://www.safehouseproject.org/trainings/ally/"),
 ("300+ episodes","Ending Human Trafficking podcast","Dr. Sandra Morgan at Vanguard University; the model of evidence-literate faith engagement.","https://endinghumantrafficking.org/"),
]
READ = [
 ("When Helping Hurts","Corbett and Fikkert. Our book. Free reflection questions and small-group videos from the Chalmers Center.","https://chalmers.org/resources/videos/series/when-helping-hurts-the-small-group-experience/"),
 ("God's Heart to Eradicate Trafficking","Safe House Project. Our study, free with a login.","https://training.safehouseproject.org/offers/e4LdGGz7/checkout"),
 ("Vulnerable: Rethinking Human Trafficking","Raleigh Sadler. The natural next book: churches already have access to the people traffickers target.","https://www.bhpublishinggroup.com/product/vulnerable-2/vulnerable-2/"),
 ("God of Justice","IJM's twelve-session church curriculum; the best spine for a second semester.","https://www.ivpress.com/god-of-justice"),
 ("Faith in Action kit","Shared Hope, $75: film, small-group guide, sermon notes, 30-day prayer guide.","https://store.sharedhope.org/product/faith-action-kit/"),
 ("Route 1 Briefing","The full background document behind this page: chart, scripture, discernment notes, sources.","https://claude.ai/code/artifact/03868202-6b8d-4640-b968-d27ec289fefe"),
]



# ---------------- BUILD (v3: mobile app UI, tabs, collapsible groups, button rows) ----------------
import re as _re
ICON = {
 "tel": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.5 15.5 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm1 2.4V18h16V7.4l-8 5.2-8-5.2zM4.8 7l7.2 4.7L19.2 7H4.8z"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 2h2v2h6V2h2v2h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3V2zm12 8H5v9h14v-9z"/></svg>',
 "link": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 3h7v7h-2V6.4l-9.3 9.3-1.4-1.4L17.6 5H14V3zM5 5h6v2H7v10h10v-4h2v6H5V5z"/></svg>',
}
def btn(href, label):
    h = href
    if h.startswith("tel:"): kind="tel"
    elif h.startswith("mailto:"): kind="mail"
    elif "calendar.google" in h: kind="cal"
    else: kind="link"
    return f'<a class="btn {kind}" href="{H.escape(h, quote=True)}">{ICON[kind]}<span>{label}</span></a>'
def btns_from_html(items):
    out=[]
    for it in items:
        m=_re.search(r'href="([^"]+)"[^>]*>(.*?)</a>', it)
        if m: out.append(btn(H.unescape(m.group(1)), m.group(2)))
    return "".join(out)

BY_T = {x["t"]: x for x in ACT}
ACT.append(dict(grp="now", t="Send two people to Shared Hope's faith pre-conference", tags=["Development"], body="Monday, Oct 26, 2 to 5 PM at Grace Community Church, Ballston Quarter, Arlington. $45, and it includes the Faith in Action book, the most church-ready kit on the market. The nearest in-person faith training this fall.", lead="Two volunteers", cost="$45 each", links=[("Register","https://scurrystreet.swoogo.com/just2026")]))
BY_T = {x["t"]: x for x in ACT}
BY_T["Book HopeWorks' free trafficking workshop at church"]["body"] += " Meet the staff first at their candlelight vigil on Thursday, Oct 22, 7 to 8 PM, 9770 Patuxent Woods Dr, Columbia."
BY_T["Book HopeWorks' free trafficking workshop at church"]["links"].insert(0, ("Oct 22 vigil tickets","https://www.eventbrite.com/e/domestic-violence-awareness-month-candlelight-vigil-2026-tickets-2001187684234"))

def act_card(t, date):
    x = BY_T[t]
    stage = x["tags"][0]
    buttons="".join(btn(h,l) for l,h in x["links"])
    meta=f'<div class="meta">{x["lead"]}' + (f' · {x["cost"]}' if x["cost"] else '') + '</div>'
    return f'<article class="card act"><div class="when">{date} <span class="stage">{stage}</span></div><h3>{x["t"]}</h3><p>{x["body"]}</p>{meta}<div class="btns">{buttons}</div></article>'

ORDER = [
 ("Do first", True, [
   ("Go to the county council meeting on November 19", "Thu Nov 19 · 1–3 PM"),
   ("Audit hotel-training compliance in Howard County", "First project · Nov–Jan"),
   ("Book a free county presentation for the whole church", "Ask this month"),
   ("Book HopeWorks' free trafficking workshop at church", "Vigil Oct 22 · workshop in January"),
   ("Host Araminta's \"Awaken\" session", "Ask this month"),
   ("Register the church as an OnWatch group", "Before Oct 29"),
 ]),
 ("Next", False, [
   ("Run the drives Araminta designed for church small groups", "Start in November"),
   ("Bring prevention education to The Children's Home", "Spring"),
   ("Get an anti-trafficking partner onto Mosaic's Impact Weekend roster", "Propose by December · event expected February"),
   ("Watch the 2027 legislative session", "Delegation hearing Mon Dec 21 · session Jan 13–Apr 12"),
   ("Host a parent night on online safety and sextortion", "Winter"),
   ("Apply for a faith seat, and for the new Interfaith Advisory Commission", "Applications open now"),
   ("Send two people to Shared Hope's faith pre-conference", "Mon Oct 26 · Arlington"),
   ("Host an A21 Global Freedom Summit watch night", "Any evening · free host kit"),
   ("Give the prayer drives a liturgy", "Oct 17 · Nov 7 · Dec 5 · Jan 9 · 4 PM"),
   ("Wear Blue Day and a Bakhita prayer night", "Jan 11 · Feb 8"),
   ("Put the topic in front of the church in Advent", "Advent begins Nov 29"),
   ("Maintain a dated local resource map", "Ongoing"),
   ("Publish a rumor-response protocol for the congregation", "Ongoing"),
 ]),
 ("Long-term, background-checked", False, [
   ("HopeWorks volunteer", "Applications open Dec 1"),
   ("Araminta certified volunteer or mentor", "One-year commitment"),
   ("TurnAround on-site roles, or a Human Trafficking 101 for the church", "Ongoing"),
   ("Shared Hope Ambassador of Hope", "Free online training"),
   ("Howard County resource parent", "Home study required"),
   ("UMD SAFE Center volunteer", "Prince George's and Montgomery"),
 ]),
 ("Money for the pilot", False, [
   ("Community Foundation of Howard County", "Closes Mon Nov 2"),
   ("Walmart Spark Good local grants", "Closes Mon Nov 30"),
   ("Thrivent Action Teams", "Any time · two weeks' notice"),
   ("Howard County Community Service Partnership grants", "Expected Nov–Jan"),
   ("United Methodist Peace with Justice grants", "Due May 16"),
   ("Dressember and Freedom Partners", "December"),
 ]),
]
def group(label, open_, inner, count):
    o = " open" if open_ else ""
    return f'<details class="grp"{o}><summary><span>{label}</span><span class="count">{count}</span></summary><div class="cards">{inner}</div></details>'
def actions_html():
    out=[]
    for label, open_, items in ORDER:
        out.append(group(label, open_, "".join(act_card(t,d) for t,d in items), len(items)))
    out.append(f'<details class="grp avoid"><summary><span>Avoid</span><span class="count">{len(AVOID)}</span></summary><ul class="avoid-list">{"".join(f"<li>{x}</li>" for x in AVOID)}</ul></details>')
    return "\n".join(out)

PART_ORDER = [
 ("Howard County government", False, ["Office of Human Trafficking Prevention","Human Trafficking Prevention Coordination Council","Howard County Delegation","Howard County Police community outreach","Interfaith Advisory Commission","Maryland Human Trafficking Task Force"]),
 ("Local responders", False, ["TurnAround, Inc.","HopeWorks of Howard County","Catherine's Cottage","Grassroots Crisis Intervention","Esperanza Center","UMD SAFE Center"]),
 ("Faith-based organizations", False, ["Araminta Freedom Initiative","FAAST","Alliance to End Human Trafficking","Safe House Project","Salvation Army Eastern Territory","International Justice Mission","Shared Hope International","Set Free Movement","Send Relief","Institute for Survivor Care"]),
 ("Churches and denominations nearby", False, ["HoCo AGAST","Bethany UMC","Baltimore-Washington Conference, United Methodist","Sisters of Bon Secours","Glen Mar UMC","Grace Episcopal Church","St. Louis Catholic Church","Maryland Catholic Conference"]),
]
PBY = {x["n"]: x for _,items in PART for x in items}
def org_card(n):
    x=PBY[n]
    return (f'<article class="card org"><h3>{x["n"]}</h3><div class="sub">{x["s"]}</div>'
            f'<p class="path"><strong>Open to us:</strong> {x["p"]}</p>'
            f'<div class="btns">{btns_from_html(x["c"])}</div>'
            f'<details class="more"><summary>About</summary><p>{x["w"]}</p></details></article>')
def partners_html():
    out=[]
    for label, open_, names in PART_ORDER:
        out.append(group(label, open_, "".join(org_card(n) for n in names), len(names)))
    return "\n".join(out)

CALLS = [
 ("Ashton Petta", "county Office of Human Trafficking Prevention, the gateway to everyone else. Ask for a presentation before Thanksgiving, introductions to the council's faith-seat members and HoCo AGAST, and how to be useful Nov 19.", [("mailto:apetta@howardcountymd.gov","apetta@howardcountymd.gov"),("tel:+14103136558","410-313-6558")]),
 ("Araminta", "Ask them to present, register six to ten of us for Awaken, and connect us with church partnerships and the prayer team.", [("https://form-usa.keela.co/request-a-presentation","Presentation form"),("tel:+14439340003","443-934-0003")]),
 ("Salvation Army Central Maryland", "Jaleesa Thomas and Nina Christian. Ask for Catherine's Cottage's top three needs this quarter and whether they take church teams. Extension 50110.", [("tel:+14107832920","410-783-2920")]),
 ("FAAST", "Ask to join as a $100 affiliate, which Maryland churches are members, and whether a caregiver training could be hosted here.", [("mailto:faast@faastinternational.org","faast@faastinternational.org")]),
 ("Sara Cochran, HoCo AGAST", "Ask how a church group plugs into the Compassion Brigade and what churches should not do. Reach her through Ashton Petta, or on Facebook.", [("https://www.facebook.com/HoCoAGAST/","Facebook")]),
]
def calls_html():
    return "".join(f'<article class="card call"><div class="when">Call {i}</div><h3>{n}</h3><p>{d}</p><div class="btns">{"".join(btn(h,l) for h,l in links)}</div></article>' for i,(n,d,links) in enumerate(CALLS,1))

CSS = open("hub.css").read()
BRIEF = "https://claude.ai/code/artifact/03868202-6b8d-4640-b968-d27ec289fefe"
page = f"""<title>Route 1 Hub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..600&amp;family=Source+Sans+3:wght@400;600;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<style>
{CSS}
</style>

<header class="top">
  <div class="wrap">
    <div class="eyebrow">Mosaic · Impact Group: HoCo Human Trafficking</div>
    <h1>Route 1 Hub</h1>
    <p class="dek">What we can do, who is already doing it, and where the church stands.</p>
  </div>
</header>
<nav class="tabs" aria-label="Sections">
  <a href="#actions" class="on">Actions</a><a href="#partners">Partners</a><a href="#mosaic">Mosaic</a>
</nav>

<main class="wrap">

<section id="actions">
  <div class="sec-head"><h2>What we can do</h2><p class="lede">Most important first. Each card says when, who could lead it, and has the button to start.</p></div>
{actions_html()}
</section>

<section id="partners">
  <div class="sec-head"><h2>Who is already doing this</h2><p class="lede">Start with the five calls. Every card ends with the door that is open to a church group.</p></div>
  <details class="grp" open><summary><span>Call first, in this order</span><span class="count">5</span></summary><div class="cards">{calls_html()}</div>
    <details class="more tpl"><summary>An introduction that works</summary>
      <p class="small">Subject: New Howard County church group, request for a conversation</p>
      <p>Hello [name]. I'm [name], coordinating a new small group at Mosaic Christian Church in Elkridge focused on human trafficking. We're [number] adults in Clarksville, Columbia and Elkridge who want to learn before we act, and to serve alongside organizations already doing the work rather than start something parallel. Would you have twenty minutes in the next few weeks to tell us how churches most usefully support [organization]: training, prayer, tangible needs, or advocacy? We're also glad to [host a presentation / register for your training / join as an affiliate]. Thank you for the work you're already doing.</p>
    </details>
  </details>
{partners_html()}
</section>

<section id="mosaic">
  <div class="sec-head"><h2>Where the church stands</h2><p class="lede">An outreach arm with a director and a budget, a Route 1 prayer practice owned by an elder, and a weekly presence with at-risk teens. None of it is labeled anti-trafficking. All of it is.</p></div>
  <details class="grp" open><summary><span>A path forward</span><span class="count">7</span></summary>
    <ol class="steps">
      <li><div class="when">October</div>Finish OnWatch as a registered church group. Book the county presentation. Loop overseer David Ross into the prayer drives.</li>
      <li><div class="when">November</div>Council meeting Nov 19; offer the hotel audit. Start the Araminta drives. Decide who applies to HopeWorks on Dec 1.</li>
      <li><div class="when">December</div>Delegation hearing Dec 21. Advent guide in front of the church. Dressember, or a parallel ask for a local partner.</li>
      <li><div class="when">January</div>HopeWorks workshop at church. Wear Blue Day. Staff the county's awareness event. Draft the pilot's proposal to leadership.</li>
      <li><div class="when">February</div>Put Araminta or HopeWorks on the Impact Weekend roster. Bakhita prayer night. Written testimony as bills are heard.</li>
      <li><div class="when">Spring</div>Prevention education at The Children's Home. Apply for a faith seat or the Interfaith Advisory Commission. Hand the hotel gap list to the council.</li>
      <li><div class="when">Summer</div>Report results to the church and launch a second group. Money moves to vetted Local Impact partners, so a project travels best as a partnership with HopeWorks or Araminta.</li>
    </ol>
  </details>
  <details class="grp"><summary><span>What Mosaic already brings</span><span class="count">7</span></summary>
    <ul class="bullets">
      <li><strong>Impact</strong>, the church's outreach arm: Local Impact Director Natasha Ramcharran; ten percent of all giving; about $814,000 in 2025, mostly grants to partners.</li>
      <li><strong>Route 1 prayer</strong>, already coordinated by overseer David Ross; an August 2026 self-guided drive named seven Route 1 hotels as "hidden places of exploitation and trafficking."</li>
      <li><strong>The Children's Home</strong> in Catonsville: a weekly Saturday flag-football group with teenagers placed there after abuse or neglect.</li>
      <li><strong>Celebrate Recovery</strong> on Thursdays, Sexual Integrity 101 and divorce support: the vulnerabilities traffickers use.</li>
      <li><strong>Partners today:</strong> Mount Clare Christian School, 10:12 Sports, Wellspring Life Ministry's pregnancy clinics, Operation Christmas Child, eleven church plants, five churches abroad. Mosaic's resource list already names Grassroots and HopeWorks.</li>
      <li><strong>Not yet connected:</strong> Araminta, TurnAround, the county office, Catherine's Cottage, FAAST, the SAFE Center.</li>
      <li><strong>Ask staff:</strong> an older public description says "for every first-time guest, we give money to fight sex trafficking." If it still exists, where does it go?</li>
    </ul>
    <div class="btns">{btn("mailto:impact@mosaicchristian.org","impact@mosaicchristian.org")}{btn("mailto:Overseers@mosaicchristian.org","Overseers@mosaicchristian.org")}{btn("https://mosaicchristian.org/impact/","Impact page")}</div>
  </details>
</section>

</main>

<footer class="wrap foot">
  <p class="small">If you see something: {tel("911")} · hotline {tel("1-888-373-7888")} · TurnAround {tel("443-279-0379")}. Don't confront anyone.</p>
  <p class="small">Built from county, state and federal reports and the organizations' own pages, October 2026. Background, numbers, scripture and sources are in the <a href="{BRIEF}">full briefing</a>. Confirm names and numbers before public use.</p>
</footer>

<script>
(function () {{
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".tabs a"));
  var secs = Array.prototype.slice.call(document.querySelectorAll("main > section"));
  var ids = secs.map(function (s) {{ return s.id; }});
  function show(id, scroll) {{
    if (ids.indexOf(id) < 0) id = ids[0];
    secs.forEach(function (s) {{ s.hidden = s.id !== id; }});
    tabs.forEach(function (t) {{ var on = t.getAttribute("href") === "#" + id; t.classList.toggle("on", on); t.setAttribute("aria-current", on ? "page" : "false"); }});
    if (scroll) window.scrollTo({{ top: 0 }});
  }}
  document.body.classList.add("js");
  show((location.hash || "#actions").slice(1), false);
  tabs.forEach(function (t) {{ t.addEventListener("click", function (e) {{ e.preventDefault(); var id = t.getAttribute("href").slice(1); history.replaceState(null, "", "#" + id); show(id, true); }}); }});
  window.addEventListener("hashchange", function () {{ show(location.hash.slice(1), true); }});
  window.addEventListener("beforeprint", function () {{ secs.forEach(function (s) {{ s.hidden = false; }}); document.querySelectorAll("details").forEach(function (d) {{ d.setAttribute("open", ""); }}); }});
  window.addEventListener("afterprint", function () {{ show((location.hash || "#actions").slice(1), false); }});
}})();
</script>
"""
page=_re.sub(r"&(?!amp;|nbsp;|lt;|gt;|quot;|#)", "&amp;", page)
open("route1-hub.html","w").write(page)
standalone = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F1F2F4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#13171F" media="(prefers-color-scheme: dark)">
<meta name="robots" content="noindex">
<meta name="description" content="Actions, partners and pathways for Mosaic's Howard County anti-trafficking Impact Group.">
<style>body{margin:0;font-size:14px;font-family:system-ui,sans-serif;background:#f6f6f4}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
""" + page + "\n</body>\n</html>\n"
open("index.html","w").write(standalone)
print("built v3:", len(page), "bytes")
