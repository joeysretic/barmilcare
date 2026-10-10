# Barmil Care Services — Canberra redesign

This project contains 18 marketing/support pages, preserving all ten existing service URLs. It is a portable static site with editable content in `content.json`, reusable templates in `build.py`, CSS and a small amount of progressive JavaScript. There is no frontend framework or package dependency.

## Preview

Run `python3 build.py`. The default is a review build: `SITE_PREVIEW=1`, meta noindex, an X-Robots-Tag header and a robots disallow rule. The preview sitemap is intentionally empty because none of its pages should be indexed. Serve `dist/` through a static web server. Every route has complete initial HTML, rather than relying on JavaScript for search content.

The private preview uses phone and email links and directs online enquiries to the existing Barmil website. It does not submit enquiries through a new backend.

## Production migration

1. Review the service descriptions, contact hours and privacy information with the client. Confirm NDIS registration separately before making a registered-provider claim. SIL, SDA, respite, formal support coordination and plan management are not advertised as confirmed services.
2. Preserve the existing contact-form backend. The current site posts to `/netlify-forms.html` using Netlify Forms with form-name `contact`. The Netlify form template is enabled only with `FORM_BACKEND=netlify`; a production build otherwise uses phone/email contact options when the external enquiry link would point back to itself. Server acceptance and email delivery must be tested on the actual host. Netlify processing is not available automatically on Cloudflare Pages, Sites or other hosts. Implement a real server endpoint on another host and update the form action before switching the domain. Do not deploy a production form without a working backend.
3. Build for the live domain with `SITE_PREVIEW=0 SITE_URL=https://barmilcareservices.com.au python3 build.py`. This removes the review noindex settings from the 18 marketing pages and creates their 18-URL sitemap. Enabling the Netlify form also requires `FORM_BACKEND=netlify` on a properly configured Netlify host. `/thank-you` and `/404` remain noindex. The production contact form is an integration template, not a verified email delivery service.
4. Upload the resulting `dist/` contents to the current hosting project. Keep all existing page paths. The new routes are `/service-areas` and `/privacy`; no service-URL redirects are needed because existing paths are retained. Set the host's error route to `404.html` and ensure unknown paths return HTTP 404.
5. Verify the form on the actual host with an authorised test and confirm receipt. Check the 18 pages on desktop and mobile, canonical URLs, HTTPS, host redirects and the HTTP response codes. Submit `https://barmilcareservices.com.au/sitemap.xml` to the correct Search Console property once live.

## What is included

- Ten distinct service pages plus homepage, services hub, about, Canberra coverage, NDIS guide, FAQs, contact and privacy information.
- Unique page titles and meta descriptions, one H1 per page, clean internal links, breadcrumbs, absolute canonical tags and an absolute-URL sitemap.
- Organization, WebSite and WebPage structured data, plus Service and BreadcrumbList on the relevant pages. No invented office address, ratings, registration number or reviews.
- Canberra-only geography, covering Belconnen, Gungahlin, North and South Canberra, Woden Valley, Weston Creek, Tuggeranong and Molonglo Valley. Districts are not represented as physical offices.
- Existing logo and four existing photos, with responsive local assets, descriptive alternative text, branded favicon and current social metadata.
- Keyboard-accessible navigation, service filtering, native expandable FAQs, mobile layouts, reduced-motion handling, click-to-call and email links.

## Verification limits

Content, metadata, links, structured-data JSON, sitemap and asset references are checked by `validate.py` and `audit_seo.py`. `seo-targets.json` records all 18 page assignments, the original workbook targets, natural keyword forms and distinct page intent. These source checks are not ranking predictions or visual browser tests. Browser rendering could not be verified in this environment because the supported browser QA capability is unavailable. No contact-form submission or email delivery test has been performed. The private preview does not change the existing live domain.

## Asset sources

The logo and images were reused from the client's current website, inspected 10 October 2026. Treat photography as illustrative; identities of depicted staff/participants were not independently verified.

- `/barmil-logo.png`
- `/assets/hero-CYthspQg.jpg`
- `/assets/about-WIHCcg00.jpg`
- `/assets/gallery-1-Bj-Y0Q5N.jpg`
- `/assets/gallery-3-CfYc5-q3.jpg`

Source origin: https://barmilcareservices.com.au/

Fonts are Plus Jakarta Sans and Inter, locally hosted from Google Fonts. Font licence information: https://fonts.google.com/specimen/Plus+Jakarta+Sans/license and https://fonts.google.com/specimen/Inter/license.

## SEO implementation audit, 10 October 2026

The ten service URLs and the premium layout are retained. Titles, H1s and introductory copy now express each page’s topic naturally. Contextual links distinguish daily assistance from learning life skills, and separate innovative preparation, everyday community access and shared group activities. Supporting pages have their own informational or branded purpose; the privacy page is not a commercial landing page.

The original SEMrush research has not been altered or re-measured. Localised wording for national service terms and six newly assigned supporting pages does not imply measured local volume.

Fonts use Latin-subset WOFF files with the same families and weights. Original TTF source files remain in `assets/` but are omitted from deployment output. The subset includes basic and extended Latin, general punctuation and currency characters.

To check production indexability without overwriting the safe preview:

```bash
SITE_PREVIEW=0 BUILD_OUTPUT_NAME=.audit-production python3 build.py
python3 audit_seo.py --directory .audit-production --production --output /tmp/barmil-production-audit.json
```

To rebuild and audit the private preview:

```bash
python3 build.py
python3 validate.py
python3 audit_seo.py
node --check app.js
```

`.audit-production/` is ignored and is not the Sites deployment directory. No live-domain deployment, Search Console submission, Google Business Profile change or email test is performed by these commands. Production redirects, response codes, actual mobile rendering, lab/field performance and contact delivery must be checked on the intended public host before migration.
