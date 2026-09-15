"""
Site content for Jesus Oneness Love Mission (JOLM) Inc.

Everything the client will ever want to reword lives in this file. Templates read
from it and never hardcode copy, so non-developers can be handed this single
module.

PLACEHOLDER markers flag values invented for the prototype. Every one of them
must be replaced with real JOLM data before this goes live.
"""

ORG = {
    "name": "Jesus Oneness Love Mission",
    "short": "JOLM",
    "legal": "Jesus Oneness Love Mission (JOLM) Inc.",
    "tagline": "Faith made visible in love.",
    "address_lines": [
        "PH3 BLK 9 LOT 8, Via Verde Subdivision, San Vicente",
        "Sto. Tomas, Batangas, Philippines 4234",
    ],
    "location": "Sto. Tomas, Batangas, Philippines",
    "email": "hello@jesusonenesslovemission.com",  # PLACEHOLDER
    "founded": 2023,
    "copyright_year": 2026,
    # While true, the page carries noindex and the giving section is labelled a
    # preview. Flip to False on the day the real details go in.
    "is_draft": True,
}

YOUTUBE = "https://www.youtube.com/channel/UC3sxLeCLK8hIf5qp5NFpSZw"
FACEBOOK = "https://www.facebook.com/profile.php?id=61550781354139"

NAV = [
    {"label": "Our heart", "href": "#heart"},
    {"label": "Our community", "href": "#events"},
    {"label": "Watch", "href": "#watch"},
    {"label": "Connect", "href": "#connect"},
]

HERO = {
    "eyebrow": "Rooted in Christ. Moved by love.",
    "title_lines": ["One faith.", "One mission.", "Boundless love."],
    "intro": "Transformation of the mind, body, and soul.<br>Sharing the love of "
             "Jesus with those in need.",
    "image": "hero.jpg",
    "image_alt": "Sunrise over a mountain valley, with a cross on a distant ridge",
    "caption": "Love that reaches beyond",
    "footnote": "Faith in our hearts. Love in our hands.",
    "verse": "Let all your things<br>be done with charity.",
    "verse_ref": "1 Corinthians 16:14 · KJV",
}

MISSION = (
    "Rooted in the Word of God and inspired by the life of Jesus Christ, we share "
    "love, compassion, and unity. As a non-profit organization, we are committed "
    "to making a positive difference in the lives of those in need in the "
    "Philippines."
)

VISION = (
    "Through the power of the Holy Spirit and the Word of God, we seek "
    "transformation of mind, body, and soul. We share the love and kindness of "
    "Jesus with all, offering support, hope, and dignity regardless of background "
    "or circumstance."
)

# An acrostic on the organisation's own name.
VALUES = [
    {"word": "Jesus", "gloss": "Our center"},
    {"word": "Oneness", "gloss": "Our fellowship"},
    {"word": "Love", "gloss": "Our response"},
    {"word": "Mission", "gloss": "Our calling"},
]

PATHWAYS = [
    {
        "icon": "✧",
        "title": "Grow in faith",
        "body": "Make space for prayer, Scripture, and a deeper relationship with Jesus.",
        "summary": "Begin with prayer",
        "detail": "Set aside a quiet moment. Give thanks, bring your needs to God, "
                  "and pray for someone in your community.",
    },
    {
        "icon": "♡",
        "title": "Walk together",
        "body": "Build connections rooted in care, encouragement, and shared faith.",
        "summary": "Make room for others",
        "detail": "Reach out to someone who needs encouragement. Listen with "
                  "patience and let them know they are remembered.",
    },
    {
        "icon": "↗",
        "title": "Love in action",
        "body": "Offer your time, your kindness, and your generosity to the needs around you.",
        "summary": "Take a small step",
        "detail": "Look for a practical way to help a neighbour. Small acts of care "
                  "can open the door to lasting connection.",
    },
]

# ---------------------------------------------------------------------------
# Our community — photo albums.
# Photographs are JOLM's own, carried over from the existing site.
# ---------------------------------------------------------------------------

EVENT_FILTERS = [
    {"key": "all", "label": "All moments"},
    {"key": "fellowship", "label": "Fellowship"},
    {"key": "celebration", "label": "Celebrations"},
    {"key": "bible-school", "label": "Bible school"},
    {"key": "outreach", "label": "Outreach"},
    {"key": "ministry", "label": "Ministry"},
    {"key": "milestones", "label": "Milestones"},
]

EVENTS = [
    {
        "id": "bible-study",
        "category": "fellowship",
        "label": "Fellowship",
        "title": "Together in the Word",
        "description": "Weekly gatherings in homes and barangay halls, opening "
                       "Scripture together.",
        "photos": [
            {"file": "bible-study-1.jpg", "alt": "Children and families gathered for a JOLM Bible study"},
            {"file": "bible-study-2.jpg", "alt": "Community members listening together during Bible study"},
            {"file": "bible-study-3.jpg", "alt": "A Bible study gathering at the mission"},
            {"file": "bible-1.webp", "alt": "A Bible study session held in a member's home"},
            {"file": "bible-2.webp", "alt": "Bible study with the youth ushers"},
        ],
    },
    {
        "id": "anniversary",
        "category": "celebration",
        "label": "Our first anniversary",
        "title": "A year of grace",
        "description": "Celebrating our first year as a mission family, with praise "
                       "and worship.",
        "photos": [
            {"file": "anniversary-1.jpg", "alt": "The mission family gathered for its first anniversary celebration"},
            {"file": "anniversary-2.jpg", "alt": "A volunteer with children at the anniversary celebration"},
            {"file": "anniversary-3.jpg", "alt": "JOLM members gathered at the anniversary event"},
        ],
    },
    {
        "id": "thanksgiving",
        "category": "celebration",
        "label": "Thanksgiving",
        "title": "Hearts full of thanks",
        "description": "A day of games, a hot meal and the gospel, for children who "
                       "rarely get a party of their own.",
        "photos": [
            {"file": "thanksgiving-1.jpg", "alt": "A child holding gifts at the Thanksgiving celebration"},
            {"file": "thanksgiving-2.jpg", "alt": "A young participant with gifts at Thanksgiving"},
            {"file": "thanksgiving-3.jpg", "alt": "Thanksgiving decorations at the celebration"},
            {"file": "kids-1.webp", "alt": "Children gathered at the JOLM Kids Thanksgiving party"},
        ],
    },
    {
        "id": "bible-school",
        "category": "bible-school",
        "label": "Daily Vacation Bible School",
        "title": "Little hearts. Growing faith.",
        "description": "Learning, creating and growing together across three days.",
        "photos": [
            {"file": "bible-school-1.jpg", "alt": "Day 1: children listening to teachers at Vacation Bible School"},
            {"file": "bible-school-2.jpg", "alt": "Day 1: members of the Vacation Bible School community"},
            {"file": "bible-school-3.jpg", "alt": "Day 2: children working on Bible school activities"},
            {"file": "bible-school-4.jpg", "alt": "Day 3: a volunteer arranging learning materials"},
            {"file": "kids-2.webp", "alt": "Children taking part in a Vacation Bible School session"},
            {"file": "kids-launch.webp", "alt": "The programme flow for the JOLM Kids Ministry launch"},
        ],
    },
    {
        "id": "caingin",
        "category": "outreach",
        "label": "Caingin, Sta. Rosa",
        "title": "A roof and a welcome",
        "description": "Food, shelter materials and prayer brought to families "
                       "living without a roof in Caingin, Sta. Rosa, Laguna.",
        "photos": [
            {"file": "caingin-1.webp", "alt": "JOLM volunteers with homeless families in Caingin, Sta. Rosa"},
            {"file": "caingin-2.webp", "alt": "Relief goods being handed to families in Caingin"},
        ],
    },
    {
        "id": "medical",
        "category": "outreach",
        "label": "Medical assistance",
        "title": "Sitting with the sick",
        "description": "Hospital bills covered and medicine delivered for families "
                       "facing a sudden stay.",
        "photos": [
            {"file": "medical-1.webp", "alt": "A JOLM member visiting a patient in hospital"},
            {"file": "medical-2.webp", "alt": "Medical assistance being delivered to a family"},
        ],
    },
    {
        "id": "wheelchair",
        "category": "ministry",
        "label": "Wheelchair sponsorship",
        "title": "Mobility restored",
        "description": "Each chair is matched to a named neighbour and handed over "
                       "in person by the board.",
        "photos": [
            {"file": "wheelchair-1.webp", "alt": "A sponsored wheelchair being presented to its recipient"},
            {"file": "wheelchair-2.webp", "alt": "A JOLM board member handing over a wheelchair"},
        ],
    },
    {
        "id": "jail",
        "category": "ministry",
        "label": "Jail ministry",
        "title": "Remembering the prisoner",
        "description": "Monthly visits, worship and counselling inside local "
                       "facilities.",
        "photos": [
            {"file": "jail-1.webp", "alt": "JOLM members during a jail ministry visit"},
        ],
    },
    {
        "id": "milestones",
        "category": "milestones",
        "label": "Registration & accreditation",
        "title": "Standing on record",
        "description": "Incorporated with the SEC, registered with the BIR, and "
                       "accredited by the Sto. Tomas local government.",
        "photos": [
            {"file": "sec.webp", "alt": "JOLM Securities and Exchange Commission registration document"},
            {"file": "bir.webp", "alt": "JOLM Bureau of Internal Revenue registration document"},
            {"file": "accreditation.webp", "alt": "JOLM accreditation at the Sto. Tomas Municipal Hall"},
        ],
    },
]

# ---------------------------------------------------------------------------
# Watch. Click-to-play: no request reaches YouTube until a visitor presses play,
# and the embed uses the no-cookie host.
# ---------------------------------------------------------------------------

VIDEOS = [
    {
        "id": "bRZFedDGoSc",
        "kind": "Trailer",
        "title": "Our 1st Anniversary Celebration",
        "blurb": "One year of ministry, marked with praise, worship and the launch "
                 "of our music team.",
        "poster": "video-anniversary.jpg",
        "poster_alt": "Title card for the JOLM first anniversary celebration video",
    },
    {
        "id": "DqaSYclxCFk",
        "kind": "Trailer",
        "title": "Thanksgiving Celebration",
        "blurb": "Giving thanks together with the families and children the mission "
                 "has walked alongside this year.",
        "poster": "video-thanksgiving.jpg",
        "poster_alt": "Title card for the JOLM Thanksgiving celebration video",
    },
]

# ---------------------------------------------------------------------------
# Giving. Bank transfer only — no payment gateway, by the client's instruction.
#
# Account details are withheld by app.py unless `verified` is True AND every
# required field is filled in. That makes it impossible to ship half-entered
# banking data by accident: set `verified` to True only once a JOLM officer has
# confirmed the numbers.
# ---------------------------------------------------------------------------

GIVE = {
    "eyebrow": "04 / Generosity with purpose",
    "title_lines": ["Let your love", "go further."],
    "body": "Giving is a personal expression of faith and love. Support the "
            "mission through a direct bank transfer.",
    "note": "Give directly through your banking app",
    "verse": "Every man according as he purposeth in his heart, so let him give.",
    "verse_ref": "2 Corinthians 9:7 · KJV",
}

GIVE_ACCOUNTS = [
    {
        "id": "local",
        "kind": "local",
        "label": "Philippine bank transfer",
        "description": "Give through your local bank, at your own pace.",
        "tag": "Within the Philippines",
        "verified": False,      # PLACEHOLDER — set True only with real details
        "bank_name": "",
        "account_name": "",
        "account_number": "",
        "currency": "",
        "reference": "",
        "swift_code": "",
        "bank_address": "",
    },
    {
        "id": "international",
        "kind": "international",
        "label": "Give from overseas",
        "description": "Let your generosity reach across borders.",
        "tag": "Across the world",
        "verified": False,      # PLACEHOLDER — set True only with real details
        "bank_name": "",
        "account_name": "",
        "account_number": "",
        "currency": "",
        "reference": "",
        "swift_code": "",
        "bank_address": "",
    },
]

GIVE_FAQ = [
    {
        "q": "How does a bank transfer work?",
        "a": "Once the mission's verified account details are available, open a "
             "donation card, copy the account information, and make the transfer "
             "through your own bank. This website does not process payments.",
    },
    {
        "q": "Can I give from another country?",
        "a": "Use the overseas card when verified international transfer "
             "instructions are available. Your bank can explain supported "
             "currencies, transfer fees, and the information it requires.",
    },
    {
        "q": "Will this page confirm my donation?",
        "a": "No. Copying or downloading account information does not send money. "
             "Your bank confirms the transfer. Keep your bank's receipt for your "
             "records.",
    },
    {
        "q": "Are these real bank details?",
        "a": "Not yet. The donation cards currently show generic examples. They "
             "demonstrate the transfer process and cannot be used to send money.",
    },
]

# ---------------------------------------------------------------------------
# The people. Officer names and portraits both come from the existing site,
# where each officer's name is carried in the photo's filename.
# ---------------------------------------------------------------------------

LEADERS = [
    {"name": "Cynthia J. Mendoza", "role": "President", "photo": "board-president.webp"},
    {"name": "Arlene G. Jose", "role": "Vice President", "photo": "board-vp.webp"},
    {"name": "Dolores J. Ocampo", "role": "Corporate Secretary", "photo": "board-secretary.webp"},
    {"name": "Rogelio P. Mendoza", "role": "Treasurer", "photo": "board-treasurer.webp"},
    {"name": "Rodel E. Reyes", "role": "Auditor", "photo": "board-auditor.webp"},
]

PASTOR = {
    "name": "Ptr. Nilo Buiser",
    "role": "Head Pastor · Local Overseer",
    "church": "Assembly of the Redeemed Church",
    "photo": "pastor.webp",
}

# A separate group on the existing site — supporters, not officers.
OVERSEERS = [
    "Mr. and Mrs. Maggieh Maxfield",
    "Mr. and Mrs. Deborah Phillips",
    "Mr. and Mrs. Rosemarie Abrigo",
    "Ms. Jenny Ancheta",
    "Mrs. Rose Fadrow",
    "Mrs. Clare Liebe",
]

CONNECT = {
    "eyebrow": "There is a place for you",
    "title_lines": ["The next chapter", "begins with love."],
    "body": "Follow our community, revisit our celebrations, and stay connected to "
            "the mission.",
}
