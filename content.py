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
    "tagline": "Transformation of the Mind, Body, and Soul.",
    "address_lines": [
        "PH3 BLK 9 LOT 8 Via Verde Subd.",
        "San Vicente, Sto. Tomas, Batangas 4234",
    ],
    "email": "hello@jesusonenesslovemission.com",  # PLACEHOLDER
    "phone": "+63 900 000 0000",                   # PLACEHOLDER
    "founded": 2023,
    "copyright_year": 2026,
}

SOCIALS = [
    {"label": "Facebook", "handle": "/jesusonenesslovemission", "url": "#", "icon": "facebook"},
    {"label": "Instagram", "handle": "@jolm.inc", "url": "#", "icon": "instagram"},
    {"label": "YouTube", "handle": "Jesus Oneness Love Mission",
     "url": "https://www.youtube.com/channel/UC3sxLeCLK8hIf5qp5NFpSZw", "icon": "youtube"},
    {"label": "X", "handle": "@jolm_inc", "url": "#", "icon": "x"},
]

NAV = [
    {"label": "Mission", "href": "#mission"},
    {"label": "Ministries", "href": "#ministries"},
    {"label": "Our Work", "href": "#work"},
    {"label": "Watch", "href": "#watch"},
    {"label": "Leadership", "href": "#leadership"},
    {"label": "Join Us", "href": "#join"},
]

# The two verses the current site leads with, kept verbatim.
SCRIPTURE = [
    {
        "text": "But seek first his kingdom and his righteousness, "
                "and all these things will be given to you as well.",
        "ref": "Matthew 6:33",
    },
    {
        "text": "But as for me and my house, we will serve the Lord.",
        "ref": "Joshua 24:15",
    },
]

HERO = {
    "eyebrow": "Non-profit ministry · Sto. Tomas, Batangas",
    "title_lines": ["Transformation of the", "Mind, Body", "and Soul."],
    "lede": "A Filipino non-profit carrying the love of Jesus Christ to the "
            "hungry, the sick, the imprisoned and the forgotten — one household "
            "at a time.",
    "primary_cta": {"label": "Support the mission", "href": "#give"},
    "secondary_cta": {"label": "See our work", "href": "#work"},
}

# PLACEHOLDER — swap for figures JOLM can actually stand behind.
IMPACT = [
    {"value": 1200, "suffix": "+", "label": "Meals served", "note": "Community feeding"},
    {"value": 48, "suffix": "", "label": "Wheelchairs sponsored", "note": "Mobility program"},
    {"value": 26, "suffix": "", "label": "Families rehoused", "note": "Caingin, Sta. Rosa"},
    {"value": 140, "suffix": "+", "label": "Bible studies held", "note": "Since 2023"},
]

MISSION = {
    "eyebrow": "Our Mission",
    "title": "Love, compassion and unity — shown, not just spoken.",
    "body": "Our mission is rooted in the core teachings of the Word of God, "
            "where love, compassion and unity are shown, inspired by the "
            "teachings and life of our loving Lord Jesus Christ. We are a "
            "dedicated non-profit organization committed to making a positive "
            "impact on the lives of those in need in the Philippines.",
}

VISION = {
    "eyebrow": "Our Vision",
    "title": "Hope, dignity and a bright future for all.",
    "body": "At Jesus Oneness Love Mission, we believe in the power of the Holy "
            "Spirit by spreading the Word of God to transform mind, body and "
            "soul. Our charity is driven by a singular purpose: to spread the "
            "love and kindness of our Lord Jesus Christ to all, regardless of "
            "their background or circumstances. We aim to provide support and "
            "resources to the less fortunate, helping them find hope, dignity "
            "and a bright future.",
}

# Derived from the event categories already on the live site.
MINISTRIES = [
    {
        "slug": "bible-study",
        "name": "Bible Study",
        "pane": "gold",
        "summary": "Weekly gatherings in homes and barangay halls, opening the "
                   "Word together for youth, ushers and families.",
        "meta": "Weekly · Sto. Tomas",
    },
    {
        "slug": "kids",
        "name": "Kids Ministry & DVBS",
        "pane": "rose",
        "summary": "Daily Vacation Bible School, thanksgiving parties and "
                   "programs built so a child is treated as a beam of sunlight.",
        "meta": "Seasonal · Ages 4–12",
    },
    {
        "slug": "medical",
        "name": "Medical Assistance",
        "pane": "azure",
        "summary": "Hospitalization support and medicine for families who would "
                   "otherwise go without care.",
        "meta": "On request · Batangas",
    },
    {
        "slug": "wheelchair",
        "name": "Wheelchair Sponsorship",
        "pane": "gold",
        "summary": "Mobility restored to neighbours living with disability, "
                   "sponsored chair by chair.",
        "meta": "Ongoing · Nationwide",
    },
    {
        "slug": "jail",
        "name": "Jail Ministry",
        "pane": "azure",
        "summary": "Visiting those inside, because the Lord remembers the "
                   "prisoner as surely as the free.",
        "meta": "Monthly · Local facilities",
    },
    {
        "slug": "outreach",
        "name": "Community Outreach",
        "pane": "rose",
        "summary": "Relief and rebuilding for homeless families, including our "
                   "ongoing work in Caingin, Sta. Rosa, Laguna.",
        "meta": "As needed · Luzon",
    },
]

WORK_FILTERS = ["All", "Outreach", "Kids", "Bible Study", "Ministry", "Milestones"]

# Photographs are JOLM's own, pulled from the existing site by fetch_assets.py.
# Sources are 320x640 portrait, so the grid is built for portrait tiles.
# Set `image` to None on any entry to fall back to a designed glass tile.
WORK = [
    {
        "title": "Helping homeless families in Caingin",
        "place": "Sta. Rosa, Laguna",
        "date": "2023",
        "cat": "Outreach",
        "pane": "rose",
        "image": "caingin-1.webp",
        "blurb": "Our largest relief effort to date — food, shelter materials "
                 "and prayer brought to families living without a roof.",
    },
    {
        "title": "JOLM Kids Thanksgiving Party",
        "place": "Sto. Tomas, Batangas",
        "date": "2024",
        "cat": "Kids",
        "pane": "gold",
        "image": "kids-1.webp",
        "blurb": "A full day of games, a hot meal and the gospel, for children "
                 "who rarely get a party of their own.",
    },
    {
        "title": "Medical assistance & hospitalization",
        "place": "Batangas",
        "date": "2024",
        "cat": "Outreach",
        "pane": "azure",
        "image": "medical-1.webp",
        "blurb": "Bills covered and medicine delivered for families facing a "
                 "sudden hospital stay.",
    },
    {
        "title": "Guard Your Heart Bible Study",
        "place": "Sto. Tomas, Batangas",
        "date": "August 2024",
        "cat": "Bible Study",
        "pane": "gold",
        "image": "bible-1.webp",
        "blurb": "A season of teaching on Proverbs 4:23, held across homes in "
                 "the barangay.",
    },
    {
        "title": "Wheelchair sponsorship",
        "place": "Ongoing",
        "date": "2024",
        "cat": "Ministry",
        "pane": "azure",
        "image": "wheelchair-1.webp",
        "blurb": "Each chair is matched to a named neighbour and handed over in "
                 "person by the board.",
    },
    {
        "title": "Jail Ministry",
        "place": "Local facilities",
        "date": "2024",
        "cat": "Ministry",
        "pane": "rose",
        "image": "jail-1.webp",
        "blurb": "Monthly visits, worship and counselling inside.",
    },
    {
        "title": "JOLM Kids Ministry launch",
        "place": "Sto. Tomas, Batangas",
        "date": "2024",
        "cat": "Kids",
        "pane": "rose",
        "image": "kids-launch.webp",
        "blurb": "The programme flow for our children's ministry, launched with "
                 "the local church.",
    },
    {
        "title": "SEC registration completed",
        "place": "Republic of the Philippines",
        "date": "2024",
        "cat": "Milestones",
        "pane": "azure",
        "image": "sec.webp",
        "blurb": "JOLM formally incorporated as a non-stock, non-profit "
                 "organization.",
    },
    {
        "title": "Sto. Tomas Municipal Hall accreditation",
        "place": "Sto. Tomas, Batangas",
        "date": "2024",
        "cat": "Milestones",
        "pane": "gold",
        "image": "accreditation.webp",
        "blurb": "Recognised by the local government as an accredited "
                 "civil-society partner.",
    },
    {
        "title": "Rebuilding after the rain",
        "place": "Caingin, Sta. Rosa, Laguna",
        "date": "2023",
        "cat": "Outreach",
        "pane": "rose",
        "image": "caingin-2.webp",
        "blurb": "Returning to the same families with materials to rebuild, not "
                 "just relief to get through the week.",
    },
    {
        "title": "Bible Study with Youth Ushers",
        "place": "Sto. Tomas, Batangas",
        "date": "2024",
        "cat": "Bible Study",
        "pane": "gold",
        "image": "bible-2.webp",
        "blurb": "Teaching the young people who serve every week — so those who "
                 "usher also get fed.",
    },
    {
        "title": "Daily Vacation Bible School",
        "place": "Three-day programme",
        "date": "2024",
        "cat": "Kids",
        "pane": "gold",
        "image": "kids-2.webp",
        "blurb": "Three days of teaching, music and play — with a recap "
                 "published for parents each evening.",
    },
    {
        "title": "A chair handed over in person",
        "place": "Batangas",
        "date": "2024",
        "cat": "Ministry",
        "pane": "azure",
        "image": "wheelchair-2.webp",
        "blurb": "Mobility restored to a neighbour living with disability, "
                 "delivered by the board themselves.",
    },
    {
        "title": "Hospital visitation",
        "place": "Batangas",
        "date": "2024",
        "cat": "Outreach",
        "pane": "azure",
        "image": "medical-2.webp",
        "blurb": "Sitting with patients and their families through the long "
                 "days of a hospital stay.",
    },
    {
        "title": "BIR registration",
        "place": "Republic of the Philippines",
        "date": "2024",
        "cat": "Milestones",
        "pane": "gold",
        "image": "bir.webp",
        "blurb": "Registered with the Bureau of Internal Revenue, so official "
                 "receipts can be issued for every gift.",
    },
]

# ---------------------------------------------------------------------------
# Giving. Bank transfer only — no payment gateway, by the client's instruction.
# EVERY account detail below is PLACEHOLDER and must be replaced with JOLM's
# real treasury accounts before launch.
# ---------------------------------------------------------------------------

GIVE = {
    "eyebrow": "Support Our Mission",
    "title": "Give directly. Every peso goes to the work.",
    "body": "JOLM receives gifts by bank transfer and e-wallet only — there is "
            "no processing fee and no middleman taking a cut. Pick an amount, "
            "copy the details, and send your proof of transfer so our treasurer "
            "can acknowledge it.",
    "note": "JOLM Inc. is a registered non-stock, non-profit organization. "
            "Official receipts are issued for every gift on request.",
}

# `impact` copy is PLACEHOLDER — JOLM should supply real unit costs.
GIVE_AMOUNTS = [
    {"amount": 500, "impact": "Feeds a family of five for two days."},
    {"amount": 1000, "impact": "Covers one week of medicine for a patient in our care."},
    {"amount": 2500, "impact": "Sends one child through the full Vacation Bible School."},
    {"amount": 5000, "impact": "Sponsors one wheelchair, handed over in person."},
]

# PLACEHOLDER accounts.
GIVE_ACCOUNTS = [
    {
        "id": "bdo",
        "kind": "Bank transfer",
        "bank": "BDO Unibank",
        "pane": "gold",
        "account_name": "Jesus Oneness Love Mission Inc.",
        "account_number": "0000 1234 5678",
        "extra_label": "Swift code",
        "extra_value": "BNORPHMM",
    },
    {
        "id": "bpi",
        "kind": "Bank transfer",
        "bank": "Bank of the Philippine Islands",
        "pane": "azure",
        "account_name": "Jesus Oneness Love Mission Inc.",
        "account_number": "0000 9876 5432",
        "extra_label": "Swift code",
        "extra_value": "BOPIPHMM",
    },
    {
        "id": "gcash",
        "kind": "E-wallet",
        "bank": "GCash",
        "pane": "rose",
        "account_name": "Jesus Oneness Love Mission Inc.",
        "account_number": "0917 000 0000",
        "extra_label": "Account name shown as",
        "extra_value": "JE**S O****SS L**E M****ON",
    },
]

GIVE_STEPS = [
    {
        "n": 1,
        "title": "Choose your gift",
        "body": "Pick an amount, or enter your own. We will show you what it "
                "covers on the ground.",
    },
    {
        "n": 2,
        "title": "Transfer with your reference code",
        "body": "Copy the account details and paste your code into the notes or "
                "message field of the transfer.",
    },
    {
        "n": 3,
        "title": "Send your proof",
        "body": "Message the screenshot to our Facebook page or email the "
                "treasurer. We acknowledge every gift within 48 hours.",
    },
]

JOIN = [
    {
        "kind": "Calendar",
        "title": "Come to what's next",
        "body": "Bible studies, outreaches and kids' programs — our year, open "
                "for you to join.",
        "cta": "Get the calendar",
        "href": "#",
        "pane": "gold",
    },
    {
        "kind": "YouTube",
        "title": "Watch the ministry",
        "body": "Anniversary services, DVBS recaps and praise nights, posted as "
                "they happen.",
        "cta": "Subscribe on YouTube",
        "href": "#",
        "pane": "rose",
    },
    {
        "kind": "Volunteer",
        "title": "Serve with us",
        "body": "Drivers, cooks, teachers, musicians and prayer warriors — there "
                "is a place for you.",
        "cta": "Tell us you're in",
        "href": "#",
        "pane": "azure",
    },
]

# Officers of the corporation. Names and portraits both come from the existing
# site, where each officer's name is carried in the photo's filename.
BOARD = [
    {"name": "Cynthia J. Mendoza", "role": "President", "image": "board-president.webp"},
    {"name": "Arlene G. Jose", "role": "Vice President", "image": "board-vp.webp"},
    {"name": "Dolores J. Ocampo", "role": "Corporate Secretary", "image": "board-secretary.webp"},
    {"name": "Rogelio P. Mendoza", "role": "Treasurer", "image": "board-treasurer.webp"},
    {"name": "Rodel E. Reyes", "role": "Auditor", "image": "board-auditor.webp"},
]

# A separate group on the existing site — not officers.
OVERSEERS = [
    {"name": "Maggieh Maxfield", "note": "Mr. and Mrs."},
    {"name": "Deborah Phillips", "note": "Mr. and Mrs."},
    {"name": "Rosemarie Abrigo", "note": "Mr. and Mrs."},
    {"name": "Jenny Ancheta", "note": "Ms."},
    {"name": "Rose Fadrow", "note": "Mrs."},
    {"name": "Clare Liebe", "note": "Mrs."},
]

PASTOR = {
    "name": "Ptr. Nilo Buiser",
    "role": "Head Pastor · Local Overseer",
    "church": "Assembly of the Redeemed Church",
    "image": "pastor.webp",
    # Scripture, not a personal quote — JOLM has not published one, and an
    # invented quote attributed to a real pastor would be a fabrication.
    "verse": "Give thanks to the Lord, for He is good; His love endures forever.",
    "verse_ref": "Psalm 107:1",
}

# ---------------------------------------------------------------------------
# Video. Click-to-play: no YouTube request is made until a visitor presses play,
# and the embed uses the no-cookie host.
# ---------------------------------------------------------------------------

YOUTUBE_CHANNEL = "https://www.youtube.com/channel/UC3sxLeCLK8hIf5qp5NFpSZw"

VIDEOS = [
    {
        "id": "bRZFedDGoSc",
        "title": "Our 1st Anniversary Celebration",
        "kind": "Trailer",
        "blurb": "One year of ministry, marked with praise, worship and the "
                 "launch of our music team.",
        "poster": "video-anniversary.jpg",
        "pane": "gold",
    },
    {
        "id": "DqaSYclxCFk",
        "title": "Thanksgiving Celebration",
        "kind": "Trailer",
        "blurb": "Giving thanks together with the families and children the "
                 "mission has walked alongside this year.",
        "poster": "video-thanksgiving.jpg",
        "pane": "rose",
    },
]

CREDENTIALS = [
    {"label": "SEC registered", "detail": "Non-stock, non-profit"},
    {"label": "BIR registered", "detail": "Official receipts issued"},
    {"label": "LGU accredited", "detail": "Sto. Tomas, Batangas"},
]
