# Lyto Studio · lytostudio.com

Static marketing website for Erica Torta and Abderrahman Lyassi, Turin. Hosted on the existing Cloudflare Pages project; this change does not move hosting or change DNS.

## Pages

- `/` and `/it/`: Italian homepage (root canonical points to `/it/`).
- `/en/`: English homepage.
- `/it/siti/` and `/en/websites/`: website packages and Up Collection case study.
- `/it/automazioni/` and `/en/automations/`: automations and AI assistants.
- `/it/lyto-caller/` and `/en/lyto-caller/`: real estate voice assistant.
- `/privacy.html?lang=it` or `en`: existing bilingual privacy notice.

Each marketing URL contains its own localized HTML, title, description, canonical and hreflang links. The language switch preserves the current service page. Legacy `/?lang=en` and `/?lang=it` links are supported; `/it` and `/en` redirect to the corresponding directories. Legacy homepage `#pricing` and `#work` anchors remain available.

## Editing and building

Copy, templates and prices live in `scripts/build.py`. Shared design is in `assets/site.css`; contact interaction is in `assets/site.js`. Run with Python 3, no dependencies:

```sh
python3 scripts/build.py
python3 scripts/check.py
node --check assets/site.js
python3 -m http.server 8765 --bind 127.0.0.1
```

Commit the generated HTML and sitemap: Cloudflare can serve this repository directly, with no install or runtime build step. Preserve the existing Cloudflare project build and output settings.

## Contact behavior

The calendar links to the existing `https://cal.com/lyto-studio/20min` booking page. No embedded calendar or third-party scripts load on the marketing pages. The form explicitly prepares a `mailto:` email and asks visitors to finish sending it in their email app. It does not claim a successful server submission. No contact backend, new provider account or WhatsApp number has been invented. Add a real backend and update the technical privacy disclosure together if direct submission is needed.

## Commercial review before production

The implemented prices are the proposed list, not a verified profitability model:

- Essential website €590; Business website €1,290; optional care €49/month.
- Automation from €1,490 plus required management from €99/month; month one included. First 12 months from €2,579.
- Caller €149/month plus €290 setup; 300 minutes; extra €0.30/min; one office and number. First month €439; 450-minute recurring month €194.

Confirm actual AI, telephony, infrastructure and support costs before production. Confirm VAT wording, domain renewal costs, care allowance, cancellation notice and billing rules in the commercial proposal. Caller monthly usage roll-over, rounding and overage notifications are not asserted: define them operationally and in the proposal.

Only Up Collection is presented as client work. Automation workflows and the written Caller conversation are labelled illustrative. No invented reviews, measured savings or audio demos. Add authorized recordings and testimonials when available. A business WhatsApp number has not been supplied; contact uses the existing email/calendar.

No analytics provider is configured. Use existing hosting statistics if available; a measurement integration and consent requirements need a separate choice of provider and implementation.

© 2026 Erica Torta & Abderrahman Lyassi. All rights reserved.
