"""
Jesus Oneness Love Mission — website.

Run locally:
    pip install -r requirements.txt
    python app.py
    open http://127.0.0.1:5000
"""

from __future__ import annotations

import copy
import datetime as _dt

from flask import Flask, render_template

import content

app = Flask(__name__)

# Fields an account must carry before it may be shown to a visitor.
_REQUIRED = ("bank_name", "account_name", "account_number", "currency")


def publishable_accounts() -> list[dict]:
    """Withhold banking details unless a human has confirmed them.

    An account is only rendered when `verified` is True *and* every required
    field is filled in. Anything short of that is blanked out, so half-entered
    details can never reach a donor by accident.
    """
    accounts = copy.deepcopy(content.GIVE_ACCOUNTS)
    for account in accounts:
        ready = account.get("verified") is True and all(
            isinstance(account.get(field), str) and account[field].strip()
            for field in _REQUIRED
        )
        if account.get("kind") == "international":
            ready = ready and bool(account.get("swift_code", "").strip())
        account["ready"] = ready
        if not ready:
            for field in (*_REQUIRED, "swift_code", "bank_address", "reference"):
                account[field] = ""
    return accounts


@app.context_processor
def inject_site():
    return {
        "org": content.ORG,
        "nav": content.NAV,
        "youtube": content.YOUTUBE,
        "facebook": content.FACEBOOK,
        "year": _dt.date.today().year,
    }


@app.route("/")
def index():
    return render_template(
        "index.html",
        hero=content.HERO,
        mission=content.MISSION,
        vision=content.VISION,
        values=content.VALUES,
        pathways=content.PATHWAYS,
        event_filters=content.EVENT_FILTERS,
        events=content.EVENTS,
        videos=content.VIDEOS,
        give=content.GIVE,
        accounts=publishable_accounts(),
        faq=content.GIVE_FAQ,
        leaders=content.LEADERS,
        pastor=content.PASTOR,
        overseers=content.OVERSEERS,
        connect=content.CONNECT,
    )


@app.route("/healthz")
def health():
    return {"status": "ok"}


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = (
        "camera=(), microphone=(), geolocation=(), payment=()"
    )
    # frame-src admits the YouTube no-cookie player, and only once a visitor
    # has pressed play — nothing is loaded from YouTube before that.
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; img-src 'self' data:; style-src 'self'; "
        "font-src 'self'; script-src 'self'; connect-src 'self'; "
        "frame-src https://www.youtube-nocookie.com; "
        "object-src 'none'; base-uri 'self'; frame-ancestors 'none'; "
        "form-action 'self'"
    )
    return response


if __name__ == "__main__":
    import os
    app.run(debug=True, port=int(os.environ.get("PORT", "5000")))
