# Jesus Oneness Love Mission — website rebuild

A Flask rebuild of [jesusonenesslovemission.com](https://jesusonenesslovemission.com),
redesigned as a client-facing prototype.

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5000>.

## Photographs

```bash
python fetch_assets.py
```

Downloads JOLM's own photographs from the existing site into `static/img/` —
board portraits, event photos, the official seal and the YouTube poster frames.
Run once; existing files are skipped.

The existing site is WordPress + Elementor, so these are its generated
thumbnails: event photos are **320×640 portrait** and board portraits **192×192**.
The gallery is built for portrait tiles because of this. If the client can
supply originals, drop them into `static/img/` under the same filenames and
nothing else needs to change.

## Build the static site

```bash
python freeze.py
```

Writes a complete, self-contained `build/`:

```
build/index.html     the page, CSS and JS inlined, images at ./img/
build/artifact.html  same page without the <html> wrapper, for embedding hosts
build/img/           copied from static/img/
```

Deploy `build/` to any static host as-is. It is rendered from the live
templates, so the preview can never drift from the app.

## Layout

```
app.py            Routes. Two: the page, and the reference-code endpoint.
content.py        Every word on the site, as data. Edit here, never in templates.
fetch_assets.py   Pulls JOLM's photographs from the existing site.
freeze.py         Renders the site to a static build.
templates/        base.html + index.html + partials/ (one file per section)
static/css/       site.css — the whole design system, tokenised
static/js/        site.js — no dependencies
static/img/       photographs (populated by fetch_assets.py)
```

**`content.py` is the file to hand to whoever maintains the copy.** Nothing in
it requires knowing HTML.

## The design

The brief was "futuristic" *and* "missionary/religious" — two directions that
usually fight. They are resolved here through one material: **stained glass**.

- Panels are **chamfered**, not rounded — cut glass, not a UI card.
- A hairline gold **"came" line** traces every panel edge, the way lead traces
  a window. It is the signature detail; it is why panels use `clip-path` plus a
  masked gradient border rather than `border-radius`.
- Light is **transmitted, not reflected**: gradient panes behind the hero, a
  faint diagonal lattice, and dust motes drifting in a light shaft (canvas).
- Three glass hues carry meaning across the page — gold, rose, azure — assigned
  per ministry and per event in `content.py`.

Type is **Fraunces** (display), **Plus Jakarta Sans** (body), **JetBrains Mono**
(labels and, functionally, bank account numbers — tabular digits).

Both light and dark themes are fully designed, with a toggle in the header. Dark
is the default world; light is "morning light through the window". The theme
respects the visitor's OS setting until they choose otherwise.

## Giving — bank transfer, no gateway

By instruction, there is **no payment processor**. The section is built around
making a manual transfer as frictionless as a gateway would be:

1. **Amount picker** with a live readout of what that amount covers on the
   ground. Custom amounts are tiered in `site.js` (`customInput` handler) and
   those tiers mirror `GIVE_AMOUNTS` in `content.py` — change both together.
2. **Reference code** (`JOLM-YYMM-XXXX`), issued by `/api/reference-code`. The
   donor pastes it into the transfer notes so the treasurer can match an
   incoming deposit to a specific giver. Today codes are generated and thrown
   away — see below.
3. **Account cards** with one-tap copy on the account name and number.

### Before this goes live

- [ ] **Replace every bank and GCash detail in `GIVE_ACCOUNTS`.** They are
      invented. This is the one item that must not reach a real donor.
- [ ] Replace the impact figures in `IMPACT` and the unit costs in
      `GIVE_AMOUNTS` with numbers JOLM can stand behind. The custom-amount
      tiers in `site.js` mirror `GIVE_AMOUNTS` — change both together.
- [ ] Fill in the real Facebook, Instagram and X URLs, the calendar link, and
      the contact email and phone (currently `#` / `PLACEHOLDER`).
- [ ] Persist reference codes if you want reconciliation to actually work:
      write `{code, amount, issued_at}` to a table and give the treasurer a
      simple list view. As written the endpoint is display-only.
- [ ] Ask JOLM for a higher-resolution logo. The seal on the existing site is
      113×124, which is large enough for the footer but not for a header mark.

Done: board names and portraits, the pastor, overseers, event photographs, and
both YouTube videos are all real, taken from the existing site.

## Video

Two videos and the channel are wired in from the existing site:

| Video | ID |
| --- | --- |
| Our 1st Anniversary Celebration | `bRZFedDGoSc` |
| Thanksgiving Celebration | `DqaSYclxCFk` |

They use a **click-to-play facade**: the card shows a locally stored poster
frame, and the YouTube iframe is only created when a visitor presses play. So
the page makes no third-party request and sets no YouTube cookies for the
majority of visitors who never watch, and it loads faster. The embed uses
`youtube-nocookie.com`.

Each card also carries a permanent *Watch on YouTube* link, so the video stays
reachable where embedded players are blocked (strict CSP, some school and
office networks).

## Hosting and HTTPS

Repository: <https://github.com/SecretSau/Demo_web1> (private)

### Deploying — Cloudflare Pages

The repo is private, and GitHub Pages will not serve a private repo on a free
plan. Cloudflare Pages will, for free, and it is also the path to the real
domain later — so the prototype and the eventual cutover use the same setup.

In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect to
Git**, pick `Demo_web1`, then:

| Setting | Value |
| --- | --- |
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `docs` |
| Root directory | `/` |

No build command is needed because `docs/` is committed. Every push to `main`
redeploys automatically, and HTTPS is issued for you.

To publish updates: edit, then

```bash
python freeze.py && git add -A && git commit -m "Update site" && git push
```

When JOLM is ready to move the real domain, add
`jesusonenesslovemission.com` under the project's **Custom domains** tab.
Let the certificate issue *before* cutting DNS over, so there is no window
where visitors hit a certificate warning.

`docs/_headers` carries the security headers and image caching; Cloudflare
Pages and Netlify both read it, and it is regenerated by `freeze.py`.

### The static trade-off

Deploying `docs/` means there is no server, so `/api/reference-code` is not
available. The page already falls back to generating the code in the browser,
which is fine for a prototype — but the server never sees the code, so nothing
is recorded for the treasurer. Move to the hosted option below when you want
that.

**Flask hosted.** Any small VPS or a platform like Render/Fly/PythonAnywhere.
Needed the moment you want reference codes persisted, a contact form, or an
admin view for the treasurer. Serve with a real WSGI server, not `app.run()`:

```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

Put nginx or Caddy in front for TLS. Caddy is the shorter path — it obtains and
renews Let's Encrypt certificates on its own from a two-line config.

Either way, point the existing domain at the new host and let the certificate
issue **before** cutting DNS over, so there is no window where visitors hit a
certificate warning.
