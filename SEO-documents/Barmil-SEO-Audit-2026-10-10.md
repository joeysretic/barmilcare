# Barmil Care Services — SEO implementation audit

Audit date: 10 October 2026. Scope: the 18-page redesign, not the existing client-domain website.

**Result:** All 18 pages pass the available source/build checks after the improvements. The private preview remains deliberately non-indexable. A separate production build was checked and contains 18 indexable marketing pages; it has not been deployed to the client domain.

[Open the updated private preview](https://barmil-care-canberra.harrisandrew721.chatgpt.site)

## Reference and method

The reference is Barmil-Canberra-Keyword-Research.xlsx, including Keyword priorities, Page map, Excluded and held, and SEMrush data, plus the retained SEMrush reports dated 10 October 2026. Australian search-volume estimates have not been refreshed, invented or reassigned to a Canberra-only population. The original workbook remains unchanged.

The workbook mapped the homepage, ten services and coverage page. Six supporting pages now have editorial assignments suited to their own purpose. These are not new measured keyword opportunities. National service terms are used with Canberra context without inventing local search volume.

Each title, H1, introduction and meaningful body area was checked for the assigned topic. Natural grammar, singular/plural variants and reordered search phrases are allowed. Secondary-topic checks exclude global navigation, footer and repeated related-service cards. Content was also reviewed for service relevance and readable language; there is no keyword-density quota or arbitrary word-count target.

## Changes and technical findings

| Area | Change and result | Verification limit |
|---|---|---|
| Keyword assignments | Assigned distinct informational, branded or enquiry purposes to the other six pages. All 18 pages mapped. No additional search volumes claimed. | Ranking performance remains unverified. |
| Primary keyword placement | Aligned titles, H1s, introductions and relevant body copy with each topic using natural grammar. All 18 pages pass the topic-placement checks. | Word matching alone does not prove relevance or rankings; copy and intent were also reviewed. |
| Secondary keywords | Added relevant variants and practical explanations without repeating exact queries mechanically. All selected secondary topic checks pass. | Singular/plural and word-order variations are treated as the same topic. |
| Daily living / life skills | Daily Living focuses on assistance doing routines; Life Skills on learning and practice. Added reciprocal contextual links. Distinct page titles, H1s, introductions and service explanations. | Actual ranking cannibalization needs indexed URL/query data. |
| Community service overlap | Added innovative to metadata and differentiated tailored preparation, everyday community access and group sessions. All three genuine services remain on their existing URLs with distinct intent. | Actual ranking cannibalization needs Search Console or rank-tracking data. |
| Headings | Added a useful H2 above the service list. One H1 and no skipped heading levels in all 18 main-content areas. | Visual wrapping has not been checked in a browser. |
| Images | Replaced alt text with scene descriptions and corrected dimensions. Retained original imagery and layout. Descriptive alt text and explicit dimensions; decorative logos retain empty alt beside the brand name. | Photography does not establish staff identities, facilities or vehicle availability. |
| Titles and descriptions | Updated relevant titles and descriptions, including the innovative service and homepage description. 18 unique titles and descriptions; every marketing title is under 60 characters. | Google can choose different title links and snippets. |
| Internal links / calls to action | Added contextual links for overlapping services and retained phone, email and enquiry routes. 1,112 internal link and asset references pass the existing full-site validator. | External enquiry delivery was not tested. |
| Canonical URLs | Preserved all ten service URLs and checked one absolute canonical per page. All 18 canonical URLs match the intended live-domain page paths. | Public-host redirect behavior, preferred host and final response codes remain unverified. |
| Preview / production indexability | Preview now has an empty sitemap, noindex metadata/header and robots disallow. A separate production build creates the 18-URL sitemap. Preview blocked intentionally; 18 production marketing pages configured as indexable. | Production configuration was tested locally only. Nothing was deployed to the client domain. |
| Structured data | Added district service areas, enquiry contact point, publisher/about relationships and Service main-entity references. JSON and entity relationships pass checks; 10 Service entities match their pages. | Google Rich Results Test was not run; eligibility is not guaranteed. No invented LocalBusiness address or ratings. |
| Duplicate content | Rewrote focal content and used concise unique service-card summaries. No identical main-content bodies, duplicate H1s, titles or meta descriptions across the 18 pages. | Shared template elements and homepage FAQ excerpts remain intentionally. |
| Canberra coverage | Added appropriate local context, retained a single coverage page and district references. All 18 pages have relevant Canberra context; no thin suburb pages or invented offices. | Google Business Profile, citations and NAP across external directories were not audited. |
| Mobile source review | Preserved them and added narrow-layout guards for long text and grid children. Viewport and responsive CSS source checks pass. | Actual device layout, touch behavior, focus order and accessibility require browser testing. |
| Performance | Created Latin-subset WOFF versions of the same font families and weights; original TTF sources are not shipped. Fonts total 126,348 bytes: 83.8% smaller. Deferred JS is 2,728 bytes and CSS is 20,755 bytes. | These are file-size measurements, not network timings, Core Web Vitals or a PageSpeed score. |
| Enquiry behavior | Netlify form activation now requires FORM_BACKEND=netlify. Production defaults to phone/email if its enquiry URL would loop back to itself. Private preview retains the existing external enquiry form link. No fake local submission endpoint was introduced. | Backend configuration and actual receipt must be verified on the intended host. No message was sent. |
| Claims and scope | Kept content within the ten services; removed ambiguous extraordinary-needs wording and retained clear scope boundaries. No new registration, qualification, accreditation, housing vacancy, centre, 24/7 availability or review claims. | Client confirmation is still needed before adding such claims or approving operational/privacy details. |

## Keyword cannibalization review

The homepage introduces Barmil as a Canberra provider. The services hub helps compare ten options. The guide explains support types. FAQs answer practical arrangements, the coverage page addresses geography, and About, Contact and Privacy serve branded or utility needs. They do not all compete as generic provider landing pages.

| Page | Exclusive focus | Distinction retained |
|---|---|---|
| Daily Tasks / Shared Living | Assistance carrying out routines now | Shared living remains on this single page; no separate competing daily-living page or unconfirmed SIL offer. |
| Development of Life Skills | Learning and practising a practical skill | Its H1 no longer leads with daily living. Reciprocal links explain when each service is relevant. |
| Innovative Community Participation | Tailored preparation around a particular participation barrier | Metadata and copy retain the innovative focus rather than presenting a generic outings page. |
| Social & Community Participation | Assistance accessing the everyday activities and places a person chooses | Separated from group-session and tailored-preparation intent. |
| Group & Centre Activities | Shared group sessions and their arrangements | No permanent centre, timetable or specific activity availability is invented. |

This resolves avoidable on-site ambiguity. It does not prove the absence of ranking cannibalization: the redesign is private, and no Search Console query-to-URL data or live rank-tracking comparison is available. Shared navigation, related-service links and useful FAQ excerpts are not treated as duplicate landing pages.

## Page-by-page checklist

All rows below passed: topic placement in title/H1/introduction/body; selected secondary topics; unique title and description; one H1 and ordered headings; image alt/dimensions where relevant; internal links and calls to action; valid structured-data JSON; Canberra relevance; correct canonical; and indexability for the intended build profile. Images are not required on utility pages.

“Production eligible” means the checked static build permits indexing. It does not mean Google has indexed the page. Every current private-preview page remains noindex.

| Page | Primary keyword / topic | Secondary keywords | Result |
|---|---|---|---|
| Home (/) | ndis provider canberra | disability support services canberra; ndis providers canberra | Pass — source checks; production eligible |
| Daily Tasks & Shared Living (/services/daily-tasks-shared-living) | ndis daily living support canberra | ndis assistance with daily life; ndis daily tasks shared living | Pass — source checks; production eligible |
| Accommodation & Tenancy (/services/accommodation-tenancy) | ndis accommodation tenancy | ndis accommodation services canberra; ndis tenancy assistance canberra | Pass — source checks; production eligible |
| Household Tasks (/services/household-tasks) | ndis cleaning services canberra | domestic assistance ndis canberra; ndis cleaners canberra; ndis household tasks | Pass — source checks; production eligible |
| Life Stage & Transition Support (/services/assist-life-stage-transition) | ndis life transition support | ndis life stage transition; ndis life stage transition canberra | Pass — source checks; production eligible |
| Travel & Transport Assistance (/services/assist-travel-transport) | ndis transport support canberra | transport assistance ndis canberra; ndis travel and transport; ndis transport assistance | Pass — source checks; production eligible |
| Group & Centre Activities (/services/group-centre-activities) | ndis group activities | ndis group activities canberra; ndis group and centre activities | Pass — source checks; production eligible |
| Personal Activities & Care (/services/assist-personal-activities) | ndis personal care canberra | ndis personal care; ndis personal activities; ndis home care canberra | Pass — source checks; production eligible |
| Development of Life Skills (/services/development-life-skills) | ndis life skills | ndis development of life skills; ndis life skills canberra | Pass — source checks; production eligible |
| Innovative Community Participation (/services/innovative-community-participation) | ndis innovative community participation | innovative community participation; ndis innovative community participation canberra | Pass — source checks; production eligible |
| Social & Community Participation (/services/participate-community) | community participation ndis canberra | ndis community participation; ndis social and community participation; community access support | Pass — source checks; production eligible |
| Services hub (/services) | ndis services canberra | NDIS support services Canberra; Barmil care services | Pass — source checks; production eligible |
| About (/about) | About Barmil Care Services Canberra | Barmil disability support Canberra; person-centred support | Pass — source checks; production eligible |
| Canberra service areas (/service-areas) | Canberra NDIS service areas | Belconnen; Gungahlin; Woden Valley; Tuggeranong; Weston Creek; Molonglo Valley | Pass — source checks; production eligible |
| NDIS support guide (/ndis-supports) | understanding NDIS supports Canberra | NDIS support guide Canberra; choosing NDIS supports | Pass — source checks; production eligible |
| FAQs (/faqs) | NDIS support FAQs Canberra | Canberra NDIS questions; starting NDIS support | Pass — source checks; production eligible |
| Contact (/contact) | Contact Barmil Care Services Canberra | Barmil phone; Barmil email; NDIS enquiry Canberra | Pass — source checks; production eligible |
| Privacy (/privacy) | Barmil Care Services privacy | enquiry privacy Canberra; personal information | Pass — source checks; production eligible |

### 1. Home

URL: `/`

**Primary target:** ndis provider canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Choose a Canberra disability support provider

**SEO title:** NDIS Provider Canberra | Barmil Care Services
**H1:** Your NDIS provider in Canberra, with you at the centre.
**Meta description:** NDIS provider in Canberra offering personal care, household tasks, transport, community participation and life skills. Explore support with Barmil.
**Opening copy:** Barmil Care Services is an NDIS provider in Canberra, offering disability support services for daily routines, community life and learning new skills. Tell us what would make your day easier.

**Secondary keyword implementation:**

- disability support services canberra → disability support services in Canberra.
- ndis providers canberra → NDIS provider in Canberra (singular/plural variation). Singular/plural variation shares the homepage; no duplicate landing page.

**Content depth:** 567 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/
**Schema:** Organization, WebSite, WebPage
**Internal destinations in main content:** `/about`, `/contact`, `/faqs`, `/service-areas`, `/service-areas#belconnen`, `/service-areas#gungahlin`, `/service-areas#molonglo-valley`, `/service-areas#north-canberra`, `/service-areas#south-canberra`, `/service-areas#tuggeranong`, `/service-areas#weston-creek`, `/service-areas#woden-valley`, `/services`, `/services/accommodation-tenancy`, `/services/assist-life-stage-transition`, `/services/assist-personal-activities`, `/services/assist-travel-transport`, `/services/daily-tasks-shared-living`, `/services/development-life-skills`, `/services/group-centre-activities`, `/services/household-tasks`, `/services/innovative-community-participation`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 2. Daily Tasks & Shared Living

URL: `/services/daily-tasks-shared-living`

**Primary target:** ndis daily living support canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Practical assistance carrying out daily routines, including shared homes; no SIL offer

**SEO title:** NDIS Daily Living Support Canberra | Barmil Care
**H1:** NDIS daily living support in Canberra
**Meta description:** Everyday assistance with routines and shared living in Canberra. Talk to Barmil Care Services about NDIS daily living support shaped around your needs.
**Opening copy:** Barmil offers NDIS daily living support in Canberra, including help with daily tasks and shared living routines. Tell us where an extra pair of hands would make home life easier, while keeping your choices at the centre.

**Secondary keyword implementation:**

- ndis assistance with daily life → ndis assistance with daily life.
- ndis daily tasks shared living → daily tasks and shared living.

**Content depth:** 542 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/daily-tasks-shared-living
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-personal-activities`, `/services/development-life-skills`, `/services/household-tasks`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 3. Accommodation & Tenancy

URL: `/services/accommodation-tenancy`

**Primary target:** ndis accommodation tenancy
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Practical help accessing or maintaining a tenancy; no housing supply

**SEO title:** NDIS Accommodation & Tenancy Canberra | Barmil Care
**H1:** NDIS accommodation & tenancy assistance in Canberra
**Meta description:** Practical NDIS accommodation and tenancy assistance in Canberra. Discuss applications, tenancy routines and moving plans with Barmil Care Services.
**Opening copy:** Barmil provides practical NDIS accommodation and tenancy assistance in Canberra. We help you work through the documents, routines and decisions involved in accessing or maintaining a suitable home.

**Secondary keyword implementation:**

- ndis accommodation services canberra → NDIS accommodation services, scoped to Canberra tenancy assistance.
- ndis tenancy assistance canberra → NDIS accommodation and tenancy assistance in Canberra.

**Content depth:** 471 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/accommodation-tenancy
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-life-stage-transition`, `/services/daily-tasks-shared-living`, `/services/development-life-skills`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 4. Household Tasks

URL: `/services/household-tasks`

**Primary target:** ndis cleaning services canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Help completing essential household cleaning and domestic tasks

**SEO title:** NDIS Cleaning Services Canberra | Barmil Care
**H1:** NDIS cleaning services in Canberra
**Meta description:** NDIS household tasks, cleaning and domestic assistance across Canberra. Discuss help with laundry, kitchen routines and essential home tasks with Barmil.
**Opening copy:** Barmil offers NDIS cleaning services in Canberra as part of household task assistance. If disability makes essential cleaning or domestic routines difficult, we can discuss help with the tasks that matter in your home.

**Secondary keyword implementation:**

- domestic assistance ndis canberra → domestic assistance, within Canberra NDIS household support copy.
- ndis cleaners canberra → NDIS cleaners in Canberra.
- ndis household tasks → ndis household tasks.

**Content depth:** 481 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/household-tasks
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-personal-activities`, `/services/daily-tasks-shared-living`, `/services/development-life-skills`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 5. Life Stage & Transition Support

URL: `/services/assist-life-stage-transition`

**Primary target:** ndis life transition support
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Planning practical steps through a change in life circumstances

**SEO title:** NDIS Life Transition Support Canberra | Barmil Care
**H1:** NDIS life transition support in Canberra
**Meta description:** Practical NDIS life transition support in Canberra. Plan changes in living arrangements, routines and support needs with Barmil Care Services.
**Opening copy:** Barmil’s NDIS life transition support in Canberra helps you plan practical steps when life changes. Tell us about the move, new routine or changing support needs you are working through, and what would help you feel prepared.

**Secondary keyword implementation:**

- ndis life stage transition → life stage transition support.
- ndis life stage transition canberra → life stage transition support in Canberra.

**Content depth:** 484 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/assist-life-stage-transition
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/accommodation-tenancy`, `/services/development-life-skills`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 6. Travel & Transport Assistance

URL: `/services/assist-travel-transport`

**Primary target:** ndis transport support canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Plan and arrange journeys and the assistance required to travel

**SEO title:** NDIS Transport Support Canberra | Barmil Care Services
**H1:** NDIS transport support in Canberra
**Meta description:** Discuss NDIS transport support across Canberra for appointments, shopping and community activities. Plan your journey with Barmil Care Services.
**Opening copy:** Barmil offers NDIS transport support in Canberra for journeys such as appointments, shopping and community activities. Share your destination, timing and access requirements so we can discuss a suitable travel arrangement.

**Secondary keyword implementation:**

- transport assistance ndis canberra → NDIS transport assistance, within Canberra journey planning.
- ndis travel and transport → ndis travel and transport.
- ndis transport assistance → ndis transport assistance.

**Content depth:** 452 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/assist-travel-transport
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/development-life-skills`, `/services/group-centre-activities`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 7. Group & Centre Activities

URL: `/services/group-centre-activities`

**Primary target:** ndis group activities
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Ask about shared group activities and available program arrangements

**SEO title:** NDIS Group Activities Canberra | Barmil Care Services
**H1:** NDIS group activities in Canberra
**Meta description:** Explore NDIS group activities in Canberra with Barmil. Discuss shared activities, participation goals, access needs and current program availability.
**Opening copy:** Explore NDIS group activities in Canberra with Barmil. Discuss shared interests, the kind of group setting you prefer and the assistance you need, then ask about current options and arrangements.

**Secondary keyword implementation:**

- ndis group activities canberra → NDIS group activities in Canberra.
- ndis group and centre activities → ndis group and centre activities.

**Content depth:** 485 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/group-centre-activities
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-travel-transport`, `/services/innovative-community-participation`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 8. Personal Activities & Care

URL: `/services/assist-personal-activities`

**Primary target:** ndis personal care canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Assistance with personal routines, hygiene and dressing

**SEO title:** NDIS Personal Care Canberra | Barmil Care Services
**H1:** NDIS personal care in Canberra
**Meta description:** Respectful personal care assistance in Canberra. Discuss support with daily personal routines, hygiene and dressing with Barmil Care Services.
**Opening copy:** Barmil offers NDIS personal care in Canberra for everyday routines such as hygiene and getting dressed. We begin with your preferences, the assistance you need and what helps you feel comfortable.

**Secondary keyword implementation:**

- ndis personal care → ndis personal care.
- ndis personal activities → assistance with personal activities.
- ndis home care canberra → NDIS home care in Canberra. Scoped to everyday personal assistance, not nursing or aged care.

**Content depth:** 460 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/assist-personal-activities
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-travel-transport`, `/services/daily-tasks-shared-living`, `/services/household-tasks`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 9. Development of Life Skills

URL: `/services/development-life-skills`

**Primary target:** ndis life skills
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Learning and practising skills, rather than having daily tasks completed

**SEO title:** NDIS Life Skills Development Canberra | Barmil Care
**H1:** NDIS life skills development in Canberra
**Meta description:** Build everyday skills at your own pace in Canberra. Barmil offers NDIS life skills support around practical routines, confidence and independence.
**Opening copy:** Barmil supports NDIS life skills development in Canberra through learning and practice. Choose a practical skill you want to build, such as preparing a meal, planning shopping or organising your week, and we can discuss manageable steps.

**Secondary keyword implementation:**

- ndis development of life skills → development of life skills.
- ndis life skills canberra → NDIS life skills development in Canberra.

**Content depth:** 513 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/development-life-skills
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-life-stage-transition`, `/services/daily-tasks-shared-living`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 10. Innovative Community Participation

URL: `/services/innovative-community-participation`

**Primary target:** ndis innovative community participation
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Tailored preparation to address an individual participation barrier

**SEO title:** NDIS Innovative Community Participation Canberra | Barmil
**H1:** NDIS innovative community participation in Canberra
**Meta description:** NDIS innovative community participation in Canberra. Discuss individual barriers, preparation and tailored participation support with Barmil.
**Opening copy:** Barmil’s NDIS innovative community participation in Canberra starts with a particular barrier to taking part. We discuss your circumstances and goals, then explore a tailored approach where a standard activity arrangement may not fit.

**Secondary keyword implementation:**

- innovative community participation → innovative community participation.
- ndis innovative community participation canberra → NDIS innovative community participation in Canberra.

**Content depth:** 515 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/innovative-community-participation
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/development-life-skills`, `/services/group-centre-activities`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 11. Social & Community Participation

URL: `/services/participate-community`

**Primary target:** community participation ndis canberra
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Assistance accessing chosen everyday social and community activities

**SEO title:** NDIS Community Participation Canberra | Barmil Care
**H1:** NDIS social & community participation in Canberra
**Meta description:** Support to take part in social and community life across Canberra. Explore NDIS community participation shaped around your interests with Barmil.
**Opening copy:** Barmil offers NDIS community participation support in Canberra to help you access social activities and places you choose. Tell us who you want to spend time with, where you want to go and the assistance you need to take part.

**Secondary keyword implementation:**

- ndis community participation → ndis community participation.
- ndis social and community participation → ndis social and community participation.
- community access support → community access support.

**Content depth:** 494 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services/participate-community
**Schema:** Organization, WebSite, WebPage, BreadcrumbList, Service
**Internal destinations in main content:** `/`, `/contact`, `/faqs`, `/ndis-supports`, `/service-areas`, `/services`, `/services/assist-travel-transport`, `/services/group-centre-activities`, `/services/innovative-community-participation`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 12. Services hub

URL: `/services`

**Primary target:** ndis services canberra
**Assignment:** New editorial assignment for a previously unmapped hub; no new volume claimed
**Search intent:** Compare Barmil’s ten support options

**SEO title:** NDIS Services Canberra | Barmil Care Services
**H1:** NDIS services in Canberra, built around your life.
**Meta description:** Explore ten NDIS services in Canberra, including personal care, cleaning, transport, community participation, shared living assistance and life skills.
**Opening copy:** Explore ten NDIS services in Canberra with Barmil Care Services. Compare help at home, participation in the community and support to build skills, then talk to us about the arrangements.

**Secondary keyword implementation:**

- NDIS support services Canberra → NDIS support services in Canberra.
- Barmil care services → Barmil care services.

**Content depth:** 260 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/services
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`, `/services/accommodation-tenancy`, `/services/assist-life-stage-transition`, `/services/assist-personal-activities`, `/services/assist-travel-transport`, `/services/daily-tasks-shared-living`, `/services/development-life-skills`, `/services/group-centre-activities`, `/services/household-tasks`, `/services/innovative-community-participation`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 13. About

URL: `/about`

**Primary target:** About Barmil Care Services Canberra
**Assignment:** New branded assignment; no measured search volume claimed
**Search intent:** Branded information about Barmil’s approach

**SEO title:** About Barmil Care Services | Canberra Disability Support
**H1:** About Barmil Care Services in Canberra
**Meta description:** Get to know Barmil Care Services, supporting people with disability across Canberra with everyday assistance, community participation and life skills.
**Opening copy:** Barmil Care Services supports people with disability across Canberra. We focus on practical assistance that makes sense in your life, with your choices guiding the conversation.

**Secondary keyword implementation:**

- Barmil disability support Canberra → Barmil’s disability support in Canberra.
- person-centred support → support shaped around your preferences.

**Content depth:** 216 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/about
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`, `/contact`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 14. Canberra service areas

URL: `/service-areas`

**Primary target:** Canberra NDIS service areas
**Assignment:** Existing workbook target; local grammar is naturalised
**Search intent:** Check geographical coverage and suburb arrangements

**SEO title:** Canberra NDIS Service Areas | Barmil Care Services
**H1:** Canberra NDIS service areas
**Meta description:** NDIS support across Canberra: Belconnen, Gungahlin, Woden, Weston Creek, Tuggeranong, Molonglo Valley and North and South Canberra. Enquire with Barmil.
**Opening copy:** Barmil’s Canberra NDIS service areas cover the city’s districts, from Belconnen and Gungahlin to Woden Valley, Weston Creek and Tuggeranong. Share your suburb and the support you need so we can discuss availability.

**Secondary keyword implementation:**

- Belconnen → Belconnen.
- Gungahlin → Gungahlin.
- Woden Valley → Woden Valley.
- Tuggeranong → Tuggeranong.
- Weston Creek → Weston Creek.
- Molonglo Valley → Molonglo Valley.

**Content depth:** 335 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/service-areas
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`, `/contact`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 15. NDIS support guide

URL: `/ndis-supports`

**Primary target:** understanding NDIS supports Canberra
**Assignment:** New informational assignment; no measured search volume claimed
**Search intent:** Understand the differences between support types before choosing

**SEO title:** Understanding NDIS Supports Canberra | Barmil Care
**H1:** Understanding NDIS supports in Canberra
**Meta description:** A practical guide to Barmil’s Canberra support services. Understand everyday assistance, skill development, community participation and questions to ask.
**Opening copy:** Understanding NDIS supports in Canberra starts with what you need help doing. This guide explains the differences between Barmil’s services so you can prepare questions and choose the support to discuss.

**Secondary keyword implementation:**

- NDIS support guide Canberra → NDIS support guide, for comparing support options in Canberra.
- choosing NDIS supports → choose NDIS supports.

**Content depth:** 345 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/ndis-supports
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`, `/services/accommodation-tenancy`, `/services/assist-life-stage-transition`, `/services/assist-personal-activities`, `/services/assist-travel-transport`, `/services/daily-tasks-shared-living`, `/services/development-life-skills`, `/services/group-centre-activities`, `/services/household-tasks`, `/services/innovative-community-participation`, `/services/participate-community`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 16. FAQs

URL: `/faqs`

**Primary target:** NDIS support FAQs Canberra
**Assignment:** New informational assignment; no measured search volume claimed
**Search intent:** Practical questions about starting and arranging support

**SEO title:** NDIS Support FAQs Canberra | Barmil Care Services
**H1:** NDIS support FAQs for Canberra
**Meta description:** Questions about Barmil’s Canberra NDIS services? Read about service areas, starting support, funding arrangements, activities and making an enquiry.
**Opening copy:** These NDIS support FAQs cover starting services and making arrangements with Barmil in Canberra. Find practical answers, then contact us with questions about your own circumstances.

**Secondary keyword implementation:**

- Canberra NDIS questions → questions about NDIS support in Canberra.
- starting NDIS support → starting support.

**Content depth:** 471 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/faqs
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 17. Contact

URL: `/contact`

**Primary target:** Contact Barmil Care Services Canberra
**Assignment:** New branded enquiry assignment; no measured search volume claimed
**Search intent:** Branded contact and enquiry options

**SEO title:** Contact Barmil Care Services | NDIS Support Canberra
**H1:** Contact Barmil Care Services in Canberra
**Meta description:** Contact Barmil Care Services for NDIS and disability support across Canberra. Call 0449 644 722 or email Info@barmilcareservices.com.au.
**Opening copy:** Contact Barmil Care Services in Canberra with an NDIS support enquiry. Tell us about your routine, suburb and the assistance you need. You can contact us yourself or involve someone you trust.

**Secondary keyword implementation:**

- Barmil phone → call Barmil.
- Barmil email → email Barmil.
- NDIS enquiry Canberra → NDIS support enquiry in Canberra.

**Content depth:** 204 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/contact
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`, `/service-areas`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

### 18. Privacy

URL: `/privacy`

**Primary target:** Barmil Care Services privacy
**Assignment:** New branded utility assignment; not a competing commercial service target
**Search intent:** Privacy information for people contacting Barmil

**SEO title:** Barmil Care Services Privacy | Canberra
**H1:** Barmil Care Services privacy information
**Meta description:** Privacy information for contacting Barmil Care Services, including enquiries, personal information and how to ask questions about your details.
**Opening copy:** This Barmil Care Services privacy information explains the contact options for Canberra enquiries and how to ask about personal information you share.

**Secondary keyword implementation:**

- enquiry privacy Canberra → privacy information for Canberra enquiries.
- personal information → personal information.

**Content depth:** 199 visible main-content words; assessed for the page’s purpose, not a minimum length.
**Canonical:** https://barmilcareservices.com.au/privacy
**Schema:** Organization, WebSite, WebPage, BreadcrumbList
**Internal destinations in main content:** `/`

**Checklist:** Title ✓ · H1 ✓ · Opening ✓ · Body topic ✓ · Secondary topics ✓ · Heading hierarchy ✓ · Metadata uniqueness ✓ · Image handling ✓ · Internal links/CTA ✓ · Schema ✓ · Canberra relevance ✓ · Production configuration ✓.

**Unverified for this page:** actual browser/device rendering, public-host status/redirect behavior, Google indexing and field performance. Contact delivery is also unverified wherever an enquiry link is offered.

## Final build and technical verification

- Built the preview and a separate production-check directory from the updated source.
- Re-audited all 18 marketing pages in both build modes: no remaining source-check failures.
- Existing full-site validator passed 1,112 internal link and asset references, including auxiliary pages; the 18-page marketing audit checked 1,018 references.
- Verified 18 unique marketing titles, descriptions and H1s, with 10 service pages on the original URLs.
- Parsed structured-data JSON and checked entity IDs, provider relationships, canonical URLs and Service page URLs.
- Verified an empty private-preview sitemap and an 18-URL production sitemap. Thank-you, 404 and the form-detection endpoint stay noindex and outside the sitemap.
- Verified no global noindex header in the production build; the private preview keeps its noindex header and robots disallow rule.
- JavaScript syntax and Git whitespace checks passed. No runtime browser automation was available.
- The official NDIS participant and Commission links were retrievable. The existing Barmil contact page was checked earlier in this task; form receipt was not tested.

## Remaining verification before live deployment

1. Check desktop and mobile layouts, dropdowns, keyboard access, contrast and form navigation in a real browser. Responsive source rules are present, but this is not visual verification.
2. Run lab performance checks on a reachable deployment, then assess field Core Web Vitals when real visitor data exists. File-size reductions alone do not establish loading speed.
3. Configure the intended form backend and verify an authorised enquiry reaches the correct inbox. The private preview uses the current Barmil form; the production template does not silently assume Netlify support.
4. Check the public host’s 200/404 responses, HTTPS, www/non-www and trailing-slash behavior, sitemap access and canonical destinations before switching the domain. Do not enable indexing on the private preview.
5. Have the client verify operational details and privacy handling. No registration, qualifications, accreditations, permanent facilities, housing availability or 24-hour service should be added without evidence.
6. After the client site goes live, verify the correct Search Console property and sitemap, then monitor which queries lead to which URLs. Review Google Business Profile and external citations separately; neither was changed here.

## Guidance checked

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): readable content, relevant search terms, descriptive links and unique pages.
- [Google: block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing): indexability configuration. Private access is retained; robots disallow alone is not treated as a removal guarantee.
- [Google LocalBusiness structured data](https://developers.google.com/search/docs/appearance/structured-data/local-business): no physical address was invented to obtain a rich result. Organization markup is retained.
- [NDIS: supported independent living](https://www.ndis.gov.au/participants/home-and-living/types-home-and-living-supports/what-supported-independent-living-sil) and [specialist disability accommodation](https://www.ndis.gov.au/participants/home-and-living/types-home-and-living-supports/what-specialist-disability-accommodation-sda): these are separate concepts and are not advertised as confirmed Barmil services.
- [NDIS participant information](https://www.ndis.gov.au/participants) and [NDIS Quality and Safeguards Commission](https://www.ndiscommission.gov.au/): current official information for participants and provider registration.
