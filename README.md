# Jesus Oneness Love Mission — website rebuild

A Flask rebuild of [jesusonenesslovemission.com](https://jesusonenesslovemission.com),
redesigned as a client-facing prototype.

Repository: <https://github.com/SecretSau/Demo_web1> (private)

## Run it

```bash
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5000>. Set `PORT` to use a different port.

## Photographs

```bash
python fetch_assets.py
```

Downloads JOLM's own photographs from the existing site into `static/img/` —
board portraits, event photos, the official seal and the YouTube poster frames.
Run once; existing files are skipped.

The existing site is WordPress + Elementor, so these are its generated
thumbnails: event photos are **320×640**, board portraits **192×192**. If the
client can supply originals, drop them into `static/img/` under the same
filenames and nothing else needs to change.

## Build the static site

```bash
python freeze.py
```

Writes a complete, self-contained `docs/`:

```
docs/index.html     the page, CSS and JS inlined, assets at ./img/ and ./fonts/
docs/404.html       not-found page
docs/artifact.html  same page without the <html> wrapper, for embedding hosts
docs/_headers       security headers + caching (Cloudflare Pages / Netlify)
docs/img/, fonts/   copied from static/
```

Deploy `docs/` to any static host as-is. It is rendered from the live templates,
so the preview can never drift from the app.

## Layout

```
app.py            Routes, security headers, and the account-safety guard.
content.py        Every word on the site, as data. Edit here, never in templates.
fetch_assets.py   Pulls JOLM's photographs from the existing site.
freeze.py         Renders the site to a static build.
templates/        index.html + 404.html
static/css/       site.css — the design system
static/js/        site.js — no dependencies
static/fonts/     Manrope + Newsreader, self-hosted
static/img/       photographs
```

**`content.py` is the file to hand to whoever maintains the copy.** Nothing in
it requires knowing HTML.

## The design

Dark navy and gold, with **Newsreader** (display) and **Manrope** (body), both
self-hosted so the page makes no third-party font request and has no
render-blocking call to Google.

The recurring device is the **arch** — the hero image, the board portraits and
the pastor's photo are all cut to the same dome. It reads as sacred
architecture without a single literal church graphic.

The page is numbered 01–06 so a long scroll still has wayfinding, and the
`JESUS / ONENESS / LOVE / MISSION` strip is an acrostic on the organisation's
own name.

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
`youtube-nocookie.com`, which is the only host `frame-src` admits in the CSP in
`app.py` — if you ever change the player, change that header too or the frame
will silently fail to load.

Each card also carries a permanent *Watch on YouTube* link, so the video stays
reachable where embedded players are blocked.

## Giving — bank transfer, no gateway

By instruction, there is **no payment processor**.

`publishable_accounts()` in `app.py` withholds every banking field unless the
account is marked `verified: True` **and** every required field is filled in
(plus a SWIFT code for the overseas account). Anything short of that is blanked
out and the page shows example details clearly labelled as examples. This makes
it impossible to ship half-entered banking data by accident — so the way to go
live is to fill in `GIVE_ACCOUNTS` in `content.py` and flip `verified`, and not
to touch the template at all.

### Before this goes live

- [ ] **Fill in `GIVE_ACCOUNTS` in `content.py` and set `verified: True`.** Until
      then the giving section shows examples, which is the correct behaviour for
      a demo.
- [ ] Set `ORG["is_draft"] = False`. That removes the `noindex` tag and the
      "Design preview" footer label — so do it only when the details are real.
- [ ] Confirm the contact email (currently `PLACEHOLDER`).
- [ ] Ask JOLM for a higher-resolution logo and original photographs.

Board names and portraits, the pastor, the overseers, all nine photo albums and
both YouTube videos are real, taken from the existing site.

## Hosting and HTTPS

### Deploying — Cloudflare Pages

The repo is private, and GitHub Pages will not serve a private repo on a free
plan. Cloudflare Pages will, for free, and it is also the path to the real
domain later.

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

To publish updates:

```bash
python freeze.py && git add -A && git commit -m "Update site" && git push
```

When JOLM is ready to move the real domain, add
`jesusonenesslovemission.com` under the project's **Custom domains** tab. Let
the certificate issue *before* cutting DNS over, so there is no window where
visitors hit a certificate warning.

### The static trade-off

Deploying `docs/` means there is no server, so the security headers set in
`app.py` do not apply — `docs/_headers` carries the equivalents for Cloudflare
Pages and Netlify. If you later need server-side behaviour (a contact form, a
donation reference log for the treasurer), host the Flask app instead:

```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

Put Caddy in front for TLS — it obtains and renews Let's Encrypt certificates
on its own from a two-line config.

## Credits

The visual design originates from a Codex-generated concept, kept and extended
here: the photo albums, the full board, the video section and the build/deploy
pipeline were added on top.
