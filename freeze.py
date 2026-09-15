"""
Render the Flask site to a static build for client preview and static hosting.

    python freeze.py

Writes into docs/:

  index.html     The complete page, CSS and JS inlined, image paths rewritten
                 to ./img/. Deploy docs/ to any static host as-is.
  artifact.html  The same page without the <!doctype>/<html>/<head>/<body>
                 wrapper, for hosts that supply their own skeleton.
  .nojekyll      Stops GitHub Pages running the output through Jekyll.
  img/           Copied from static/img/.

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
IMG_SRC = ROOT / "static" / "img"

LINK_RE = re.compile(r'\s*<link rel="stylesheet" href="/static/css/site\.css">')
SCRIPT_RE = re.compile(r'\s*<script src="/static/js/site\.js"></script>')


def render() -> str:
    with app.test_client() as client:
        response = client.get("/")
        if response.status_code != 200:
            raise SystemExit(f"Render failed: HTTP {response.status_code}")
        return response.get_data(as_text=True)


def inline(html: str) -> str:
    """Replace the linked CSS/JS with their contents."""
    css = (ROOT / "static" / "css" / "site.css").read_text(encoding="utf-8")
    js = (ROOT / "static" / "js" / "site.js").read_text(encoding="utf-8")

    html, n_css = LINK_RE.subn("\n<style>\n" + css + "\n</style>", html)
    html, n_js = SCRIPT_RE.subn("\n<script>\n" + js + "\n</script>", html)

    if not n_css or not n_js:
        raise SystemExit(
            "Could not find the stylesheet/script tags to inline. "
            "Did the asset paths in base.html change?"
        )
    return html


def rewrite_images(html: str) -> str:
    """/static/img/foo.webp -> img/foo.webp, so build/ is self-contained."""
    return html.replace("/static/img/", "img/")


def copy_images() -> int:
    dest = BUILD / "img"
    if dest.exists():
        shutil.rmtree(dest)
    if not IMG_SRC.exists():
        return 0
    shutil.copytree(IMG_SRC, dest)
    return len(list(dest.iterdir()))


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

    keep = []
    for tag in re.findall(r"<title>.*?</title>|<link[^>]*>|<style>.*?</style>",
                          head.group(1), re.S):
        # The host skeleton already supplies charset/viewport.
        if 'rel="preconnect"' in tag or "fonts.googleapis" in tag or \
           tag.startswith("<title") or tag.startswith("<style"):
            keep.append(tag.strip())

    return "\n".join(keep) + "\n" + body.group(1).strip() + "\n"


def main() -> None:
    BUILD.mkdir(exist_ok=True)
    full = rewrite_images(inline(render()))

    page = BUILD / "index.html"
    page.write_text(full, encoding="utf-8")

    fragment = BUILD / "artifact.html"
    fragment.write_text(to_fragment(full), encoding="utf-8")

    # Without this, Pages hands the output to Jekyll, which ignores files and
    # folders beginning with an underscore.
    (BUILD / ".nojekyll").write_text("", encoding="utf-8")

    n_img = copy_images()

    for path in (page, fragment):
        print(f"  {path.relative_to(ROOT)}  ({path.stat().st_size / 1024:.0f} KB)")
    print(f"  {BUILD.name}/img/  ({n_img} files)")


if __name__ == "__main__":
    main()
