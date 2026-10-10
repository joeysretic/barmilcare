# Barmil contact form: Cloudflare Pages + Resend

The form is implemented in `build.py`, `app.js` and `functions/api/enquiries.js`. It uses server-side Resend, Cloudflare Turnstile verification, honeypot, validation, and an optional Cloudflare rate limiting binding. **No credentials are included; delivery is not yet tested.**

## 1. Verify the sender domain in Resend

Verify `barmilcareservices.com.au` in Resend and add its required DNS records in Cloudflare. Use a verified `from` address such as `Barmil Care Services <enquiries@barmilcareservices.com.au>` (only after domain verification). Set the recipient to the actual Barmil inbox.

## 2. Create Cloudflare Turnstile keys

Create a Turnstile widget for the final hostname `barmilcareservices.com.au` and `www.barmilcareservices.com.au` if used. For staging, add the actual staging hostname to the widget as appropriate. The **site key** is public; the **secret key** is a Cloudflare secret.

## 3. Configure Cloudflare Pages environment

In the Pages project settings, add the following server-side variables/secrets:

- `RESEND_API_KEY` — secret, from Resend
- `TURNSTILE_SECRET_KEY` — secret, from Cloudflare Turnstile
- `RESEND_FROM` — verified sender, e.g. `Barmil Care Services <enquiries@barmilcareservices.com.au>`
- `ENQUIRY_TO` — Barmil's receiving email address
- `TURNSTILE_ALLOWED_HOSTNAMES` — comma-separated production hostnames (recommended)

Never put secret values in the ZIP, GitHub, client JavaScript, or chat.

## 4. Build and deploy

Build the production site with the **public** Turnstile site key:

```bash
SITE_PREVIEW=0 FORM_BACKEND=resend TURNSTILE_SITE_KEY=YOUR_PUBLIC_SITE_KEY SITE_URL=https://barmilcareservices.com.au python3 build.py
```

Commit/upload the root `functions/` directory **and** source files. For Cloudflare Pages with a Git-connected project, set the build command to the command above (using dashboard environment variables instead of inline values), and output directory to `dist`. Cloudflare Pages Functions are discovered from the **repository-root** `functions/` directory; do not upload only `dist/` without the functions. Avoid a Cloudflare Workers static-assets-only deployment unless you explicitly configure its API routing.

The included `dist/` was rebuilt in preview mode with the form, and remains intentionally `noindex`. **Do not deploy the preview build to the live domain.**

## 5. Rate limiting

Optionally configure a Cloudflare rate limiting binding named `ENQUIRY_RATE_LIMIT` (for example 5 requests per 60 seconds per IP). The function checks this binding after Turnstile verification and before sending. Without the binding, Turnstile + honeypot + server validation still work, **but rate limiting is not active**. Add a Cloudflare WAF rate-limit rule for `/api/enquiries` if the binding is unavailable. Do not assume rate limiting is enabled until verified.

## 6. Test on the deployed hostname

1. Open `/contact`, confirm the form and Turnstile load, and send one authorised test enquiry.
2. Verify Resend's Logs and delivery to the recipient inbox; Reply-To should be the visitor's email.
3. Test missing fields, invalid email, invalid Turnstile token, honeypot and repeated submissions.
4. Verify the Pages Functions route `/api/enquiries` is deployed and the request doesn't return HTML or 404.
5. Check mobile layout, privacy wording and success/error messaging.

If you see **Security verification is temporarily unavailable**, check the secret key, site key/hostname configuration, deployment variables and Pages Functions logs. The endpoint deliberately fails closed rather than sending unverified spam.
