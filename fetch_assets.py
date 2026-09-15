"""
Download JOLM's own photographs from the existing site into static/img/.

    python fetch_assets.py

The current site is WordPress + Elementor; these are the Elementor-generated
thumbnails it already serves, re-saved under readable filenames. Run once —
files are skipped if they already exist.

If the client later supplies original-resolution photographs, drop them into
static/img/ under the same names and nothing else has to change.
"""

from __future__ import annotations

import pathlib
import urllib.request

BASE = "https://jesusonenesslovemission.com/wp-content/uploads/"
THUMBS = BASE + "elementor/thumbs/"
OUT = pathlib.Path(__file__).parent / "static" / "img"

# local name -> remote path
ASSETS: dict[str, str] = {
    # --- Logo -------------------------------------------------------------
    "logo.webp": BASE + "2024/08/JOLM-1.webp",

    # --- Board portraits (names come from the source filenames) -----------
    "board-president.webp":  THUMBS + "Cynthia-J.-Mendoza-qty8z2brtle74iofhokm4qj7ibuqls05nat0zkdaps.webp",
    "board-vp.webp":         THUMBS + "Arlene-G.-Jose-qty9bfv9t2c3zop9815rym3p2yupyb4xck16gq0osg.webp",
    "board-secretary.webp":  THUMBS + "Dolores-J.-Ocampo-qty8z39m0ffhg4n2c6z8p8ao3pq3th3vzfgigubwjk.webp",
    "board-treasurer.webp":  THUMBS + "Rogelio-P.-Mendoza-qty8z2brtle74iofhokm4qj7ibuqls05nat0zkdaps.webp",
    "board-auditor.webp":    THUMBS + "Rodel-E.-Reyes-qty8z2brtle74iofhokm4qj7ibuqls05nat0zkdaps.webp",
    "pastor.webp":           THUMBS + "Ptr.-Nilo-Buiser-qty8pejhkw63ssplwi8ni6anprgxhrngzhfdf6oyo0.webp",

    # --- Work / events ----------------------------------------------------
    "caingin-1.webp":    THUMBS + "IMG20231209163927-scaled-qtxknp6oq3zj9vbxby4j2r5hll8xtlb2lp39jazb40.webp",
    "caingin-2.webp":    THUMBS + "IMG20231209171429-qtxkonypqzb57fxeov5q50djkuhiqe552h88ajjqps.webp",
    "kids-1.webp":       THUMBS + "received_317466904059636-qtxld7j078wocw9zdh318tetz1ijpvktrygnen5o8w.webp",
    "kids-2.webp":       THUMBS + "received_756815113038246-qtxldfzjwr899dxp02qod99zbicun5iet4c0q4t4ow.webp",
    "medical-1.webp":    THUMBS + "IMG20240807095738-scaled-qtxlm344qx260bdrjb86skrjy1rceytkbw9qkpzthc.webp",
    "medical-2.webp":    THUMBS + "IMG20240821155008-scaled-qtxlop3zqcmu9bl8afuvpx1nckw1sp6q0tiake4g74.webp",
    "bible-1.webp":      THUMBS + "20240910_134636-qtxlsxduhifai5g1l9ofxumbl01ifnz8lr6yb7uo74.webp",
    "bible-2.webp":      THUMBS + "IMG20240511160705-scaled-qtxltkvt8dbgkehws1u466oufmtos3kj0zi3b4vtvk.webp",
    "wheelchair-1.webp": THUMBS + "20240910_134050-qtxm1ym066si38bmu69cwkjt4biiexud6gwycygge8.webp",
    "wheelchair-2.webp": THUMBS + "IMG20240126110806-scaled-qtxm264pov2so40pm9idginhvehg4io7vi4u765b0g.webp",
    "jail-1.webp":       THUMBS + "IMG_20240129_115524-scaled-qtxkfyygj5entak2gluykpd1rjcaj6mivfzjhefu9s.webp",
    "sec.webp":          THUMBS + "SEC-DOCUMENTATION-1-qtxm3j0bk8xpfu1poumz26bgrfsj8s29e8235k4u0w.webp",
    "bir.webp":          THUMBS + "BIR-DOCUMENTATION-1-qtxm3cfg8eop6kb9r9sl2pz8lqoyqwc51bhosmel8g.webp",
    "accreditation.webp": THUMBS + "received_3551203795118818-qtxm0x0gktd16tu8xq0a4u1dcwntv1p3patj5w07b4.webp",
    "kids-launch.webp":  THUMBS + "PROGRAM-FLOW-JOLM-KIDS-MINISTRY-LAUNCH-1-qtxm3f8yswsk5e76at0gs79mdwb2dznc1pg58gaeps.webp",

    # --- YouTube poster frames --------------------------------------------
    # Stored locally so the page makes no third-party request until a visitor
    # actually presses play.
    "video-anniversary.jpg": "https://i.ytimg.com/vi/bRZFedDGoSc/maxresdefault.jpg",
    "video-thanksgiving.jpg": "https://i.ytimg.com/vi/DqaSYclxCFk/maxresdefault.jpg",
}

UA = {"User-Agent": "Mozilla/5.0 (JOLM site rebuild asset fetch)"}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    got = skipped = failed = 0

    for name, url in ASSETS.items():
        dest = OUT / name
        if dest.exists():
            skipped += 1
            continue
        try:
            request = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(request, timeout=30) as response:
                dest.write_bytes(response.read())
            print(f"  {name}  {dest.stat().st_size / 1024:.0f} KB")
            got += 1
        except Exception as exc:  # noqa: BLE001 - report and continue
            print(f"  FAILED {name}: {exc}")
            failed += 1

    print(f"\n{got} downloaded, {skipped} already present, {failed} failed")


if __name__ == "__main__":
    main()
