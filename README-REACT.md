# Barmil Care Services — React + Vite + TypeScript

This is a **Bolt-importable React + Vite + TypeScript project** converted from the original audited 18-page Barmil site. It retains all original imagery, logo, fonts, URL paths, metadata, schema, and Cloudflare Pages Resend backend.

## Start in Bolt or locally

1. Upload this ZIP to a GitHub repository and import the repository into Bolt.new.
2. Install dependencies: `npm install`.
3. Run `npm run dev` for the React development preview.
4. Build production: `npm run build`.

**Cloudflare Pages:** Framework preset Vite, build command `npm run build`, output directory `dist`. Keep repository-root `functions/api/enquiries.js` for Resend. Use a **Pages** project, not a static-only Worker. Python 3 and `beautifulsoup4` are needed by the prerender build scripts. Cloudflare build command: `pip3 install -r requirements-build.txt && npm run build`.

Set `TURNSTILE_SITE_KEY` as a **public build-time variable**. Set `RESEND_API_KEY`, `TURNSTILE_SECRET_KEY`, `RESEND_FROM`, `ENQUIRY_TO`, and `TURNSTILE_ALLOWED_HOSTNAMES` as **Cloudflare Pages runtime variables/secrets**. `ENQUIRY_TO=info@barmilcareservices.com.au`. Do not commit secrets.

## How the React conversion preserves SEO

- `src/main.tsx` is the React entry point.
- `src/pages.json` holds each page's editable HTML content, with React rendering it inside `SitePage`. This is a **React shell with migrated HTML content**, not a complete rewrite into separate JSX components. It can be progressively componentized in Bolt.
- `build.py` remains the authoritative content/SEO generator. `scripts/prepare.py` regenerates all page content from the audited `content.json` and `seo-targets.json`.
- `scripts/finalize.py` embeds the production page HTML and per-page metadata into the Vite build, so crawlers receive content without JavaScript.
- `/sitemap.xml` includes 18 indexable marketing pages; `/robots.txt` is production-ready.
- `functions/api/enquiries.js` implements server-side Resend, Turnstile, honeypot, and optional rate limiting.

**Important:** Edits to `src/pages.json` will be overwritten on `npm run build`. For lasting copy/SEO changes, edit `content.json`, `seo-targets.json` and/or `build.py`. You can ask Bolt to refactor the HTML content into editable React components without changing its design or SEO.

**Testing:** This package was converted and statically inspected, but actual npm install/Vite compilation, desktop/mobile rendering, and Resend delivery require testing in an environment with package access and configured credentials.
