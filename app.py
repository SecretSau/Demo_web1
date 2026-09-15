"""
Jesus Oneness Love Mission — website.

Run locally:
    pip install -r requirements.txt
    python app.py
    open http://127.0.0.1:5000
"""

from __future__ import annotations

import datetime as _dt
import random
import string

from flask import Flask, jsonify, render_template

import content

app = Flask(__name__)


def _site_context() -> dict:
    """Everything every page needs. Injected into all templates."""
    return {
        "org": content.ORG,
        "nav": content.NAV,
        "socials": content.SOCIALS,
        "scripture": content.SCRIPTURE,
        "credentials": content.CREDENTIALS,
        "youtube_channel": content.YOUTUBE_CHANNEL,
        "year": _dt.date.today().year,
    }


@app.context_processor
def inject_site():
    return _site_context()


@app.route("/")
def index():
    return render_template(
        "index.html",
        hero=content.HERO,
        impact=content.IMPACT,
        mission=content.MISSION,
        vision=content.VISION,
        ministries=content.MINISTRIES,
        work=content.WORK,
        work_filters=content.WORK_FILTERS,
        give=content.GIVE,
        give_amounts=content.GIVE_AMOUNTS,
        give_accounts=content.GIVE_ACCOUNTS,
        give_steps=content.GIVE_STEPS,
        join=content.JOIN,
        videos=content.VIDEOS,
        board=content.BOARD,
        overseers=content.OVERSEERS,
        pastor=content.PASTOR,
    )


@app.route("/api/reference-code")
def reference_code():
    """
    Issue a short code the donor pastes into their bank transfer notes, so the
    treasurer can reconcile an incoming transfer against a specific donor.

    Prototype only: codes are generated, not persisted. For production, write
    these to a table with a timestamp and the intended amount, and expose them
    to the treasurer in a simple admin view.
    """
    stamp = _dt.datetime.now().strftime("%y%m")
    tail = "".join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return jsonify({"code": f"JOLM-{stamp}-{tail}"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
