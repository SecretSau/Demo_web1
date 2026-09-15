"""
Render the Flask site to a static build for client preview and static hosting.

    python freeze.py

Writes into docs/:

  index.html     The page, CSS and JS inlined, asset paths rewritten to ./img/,
                 ./fonts/ and ./favicon.svg.
  404.html       The not-found page, same treatment.
  artifact.html  index.html without the <!doctype>/<html>/<head>/<body> wrapper,
                 for hosts that supply their own skeleton.
  .nojekyll      Stops GitHub Pages running the output through Jekyll.
  _headers       Security headers and image caching for Cloudflare Pages.
  img/, fonts/   Copied from static/.

The folder is called docs/ because GitHub Pages will serve a site from the repo
root or from /docs and nothing else — so this name is what lets Pages publish
straight from the main branch with no CI step.

Everything is generated from the live Flask templates, so the preview can never
drift from the real app.
"""

from __future__ import annotations

import pathlib
import re
import shutil

from app import app

ROOT = pathlib.Path(__file__).parent
BUILD = ROOT / "docs"          # see module docstring — the name is a Pages rule
STATIC = ROOT / "static"

LINK_RE = re.compile(r'\s*<link rel="stylesheet" href="/static/css/site\.css">')
SCRIPT_RE = re.compile(r'\s*<script src="/static/js/site\.js" defer></script>')

# Photographs are cached for a day rather than a year: the filenames are stable
# (caingin-1.webp and so on), so a year-long immutable cache would strand a
# replaced photo in visitors' browsers. Fonts never change, so they get a year.
HEADERS = """\
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), payment=()

/img/*
  Cache-Control: public, max-age=86400

/fonts/*
  Cache-Control: public, max-age=31536000, immutable
"""


def render(path: str) -> str:
    with app.test_client() as client:
        response = client.get(path)
        if response.status_code not in (200, 404):
            raise SystemExit(f"Render of {path} failed: HTTP {response.status_code}")
        return response.get_data(as_text=True)


def inline(html: str) -> str:
    """Replace the linked CSS/JS with their contents.

    The stylesheet reaches its fonts with ../fonts/, which is correct while the
    CSS sits in static/css/. Once inlined into a page at the build root, that
    relative path has to become fonts/ or every @font-face silently fails.
    """
    css = (STATIC / "css" / "site.css").read_text(encoding="utf-8")
    css = css.replace("../fonts/", "fonts/")
    js = (STATIC / "js" / "site.js").read_text(encoding="utf-8")

    # The replacement must be a function, not a string: re.sub expands escape
    # sequences in a string replacement, so a JS literal like lines.join("\n")
    # would arrive as a real newline inside the quotes and break the script.
    html, n_css = LINK_RE.subn(lambda _m: "\n<style>\n" + css + "\n</style>", html)

    # `defer` is ignored on an inline script, so the tag cannot simply be
    # replaced where it sits in <head> — it would run before the DOM exists and
    # every querySelector would return null. Drop it there, re-insert at the end
    # of <body>, which gives the same "after parsing" timing.
    # The 404 page deliberately ships no script, so a missing match is fine here.
    html, n_js = SCRIPT_RE.subn("", html)
    if n_js:
        html = html.replace("</body>", "<script>\n" + js + "\n</script>\n</body>", 1)

    if not n_css:
        raise SystemExit(
            "Could not find the stylesheet tag to inline. "
            "Did the asset paths in the templates change?"
        )

    # A broken inline script fails silently: the page still renders, but every
    # button is dead. Assert the assets survived verbatim rather than trusting it.
    if css not in html:
        raise SystemExit("Inlined CSS does not match static/css/site.css verbatim.")
    if n_js and js not in html:
        raise SystemExit("Inlined JS does not match static/js/site.js verbatim.")
    return html


def rewrite_assets(html: str) -> str:
    """Point the page at assets sitting beside it, so build/ is self-contained."""
    return (html
            .replace("/static/img/", "img/")
            .replace("/static/favicon.svg", "favicon.svg"))


def to_fragment(html: str, title: str = "Jesus Oneness Love Mission") -> str:
    """Strip the outer document so a host can supply its own skeleton.

    The live site's <title> carries the tagline for search results; a preview
    host shows the title as a short card name, so it is replaced here.
    """
    html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, count=1, flags=re.S)

    head = re.search(r"<head>(.*?)</head>", html, re.S)
    body = re.search(r"<body>(.*?)</body>", html, re.S)
    if not head or not body:
        raise SystemExit("Unexpected document shape — no <head>/<body> found.")

    keep = [tag.strip() for tag in
            re.findall(r"<title>.*?</title>|<style>.*?</style>", head.group(1), re.S)]
    return "\n".join(keep) + "\n" + body.group(1).strip() + "\n"


def copy_assets() -> tuple[int, int]:
    counts = []
    for name in ("img", "fonts"):
        dest = BUILD / name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(STATIC / name, dest)
        counts.append(len(list(dest.iterdir())))
    shutil.copy(STATIC / "favicon.svg", BUILD / "favicon.svg")
    return counts[0], counts[1]


def main() -> None:
    BUILD.mkdir(exist_ok=True)

    page = rewrite_assets(inline(render("/")))
    (BUILD / "index.html").write_text(page, encoding="utf-8")
    (BUILD / "404.html").write_text(
        rewrite_assets(inline(render("/no-such-page"))), encoding="utf-8")
    (BUILD / "artifact.html").write_text(to_fragment(page), encoding="utf-8")

    # Without this, GitHub Pages hands the output to Jekyll, which ignores
    # files and folders beginning with an underscore.
    (BUILD / ".nojekyll").write_text("", encoding="utf-8")
    # Cloudflare Pages / Netlify read this file from the output root.
    (BUILD / "_headers").write_text(HEADERS, encoding="utf-8")

    n_img, n_fonts = copy_assets()

    for name in ("index.html", "404.html", "artifact.html"):
        size = (BUILD / name).stat().st_size / 1024
        print(f"  docs/{name}  ({size:.0f} KB)")
    print(f"  docs/img/  ({n_img} files)   docs/fonts/  ({n_fonts} files)")


if __name__ == "__main__":
    main()
