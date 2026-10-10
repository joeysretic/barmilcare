# Barmil Care Services — website export

This ZIP contains the complete audited 18-page static website, editable source, local images and fonts, prebuilt HTML, keyword research and SEO audit documents.

## Start here

- `dist/` contains the prebuilt website in the same review/noindex configuration as the private preview.
- `content.json` and `build.py` contain editable content and templates; `styles.css` and `app.js` control styling and interactions.
- `SEO-documents/` contains the original keyword workbook and the final page-by-page audit.
- `README.md` explains rebuilding, production settings and remaining verification.

The website uses HTML, CSS and JavaScript with a Python 3 standard-library generator. It is not a React, Vite or Next.js project, and requires no npm packages.

To view locally, run `python3 -m http.server 8000 --directory dist` from the extracted project folder, then open http://localhost:8000. Use `python` instead of `python3` on systems where that is the Python 3 command. Opening individual HTML files directly will not correctly resolve root-relative assets and navigation.

To rebuild the review version, run `python3 build.py`. The included `dist/` intentionally has noindex rules and an empty sitemap. Follow the production instructions in README.md to build the intended 18-URL sitemap and enable indexing only when preparing the client's live site.

The enquiry page currently links to the existing Barmil form and offers phone/email contact. A Resend backend is not included or configured. Email delivery remains unverified.

This export does not deploy or modify any website. Git history, credentials, temporary files and the ChatGPT Sites project binding are excluded. The website content and assets are retained.

Source commit: 2eb95abf532175a3bd9141c31b4fc086ccdce303
