#!/usr/bin/env python3
"""Builds README.md and docs/ (GitHub Pages) from one offer list.
Every outbound Gumroad link gets the affiliate parameter a=154240979.
Edit OFFERS / UPDATED below, then run:  python3 build.py
"""
import html, json, pathlib
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

AFF_ID = "154240979"
UPDATED = "November 10, 2026"
MONTH = "November 2026"
SITE = "https://ussef-pro.github.io/gumroad-discount-codes/"
REPO = "https://github.com/ussef-pro/gumroad-discount-codes"
CTA = "Claim Your Discount Offer"

def aff(url):
    """Add ?a=AFF_ID (or &a=) to any Gumroad URL, replacing an existing a=."""
    p = urlsplit(url)
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k != "a"]
    q.append(("a", AFF_ID))
    return urlunsplit((p.scheme, p.netloc, p.path, urlencode(q), p.fragment))

MAIN = aff("https://gumroad.com/discover")

# (title, what you get, url)
OFFERS = [
    ("Gumroad Discover - all creator deals", "The main marketplace. Creator discounts that are set to auto-apply show the reduced price right on the listing - no code to type.", "https://gumroad.com/discover"),
    ("Free 3D assets", "Free and pay-what-you-want 3D assets, filtered by the free tag.", "https://gumroad.com/3d/3d-assets?tags=free"),
    ("VRChat avatars & assets", "Gumroad VRChat avatars, outfits and tutorials - one of the most searched Gumroad niches.", "https://gumroad.com/3d/vrchat"),
    ("Notion templates", "Planners, dashboards and second-brain templates from independent creators.", "https://gumroad.com/discover?query=notion%20template"),
    ("Procreate brushes", "Brush packs and stamp sets for iPad artists.", "https://gumroad.com/discover?query=procreate%20brushes"),
    ("Lightroom presets", "Photo presets and LUT bundles.", "https://gumroad.com/discover?query=lightroom%20presets"),
    ("Blender add-ons & courses", "Blender tools, add-ons and courses.", "https://gumroad.com/discover?query=blender"),
    ("AI & ChatGPT prompt packs", "Prompt libraries and AI workflow guides.", "https://gumroad.com/discover?query=chatgpt%20prompts"),
]

CATEGORIES = [
    ("3D", "3d"), ("Audio", "audio"), ("Business & Money", "business-and-money"),
    ("Comics & Graphic Novels", "comics-and-graphic-novels"), ("Design", "design"),
    ("Drawing & Painting", "drawing-and-painting"), ("Education", "education"),
    ("Fiction Books", "fiction-books"), ("Films", "films"), ("Fitness & Health", "fitness-and-health"),
    ("Gaming", "gaming"), ("Music & Sound Design", "music-and-sound-design"),
    ("Photography", "photography"), ("Recorded Music", "recorded-music"),
    ("Self Improvement", "self-improvement"), ("Software Development", "software-development"),
    ("Writing & Publishing", "writing-and-publishing"),
]

SELL_URL = aff("https://gumroad.com/")

FAQ = [
    ("Does Gumroad have a site-wide coupon code?",
     "No. Gumroad is a marketplace, so there is no single Gumroad promo code that works on every product. Each creator makes their own discount codes (Gumroad calls them offer codes) for their own products. Pages that list one \"80% off Gumroad\" code are usually showing a code from one creator's store that won't work anywhere else."),
    ("Where do I find working Gumroad discount codes?",
     "Start on Gumroad Discover: when a creator sets a discount to apply automatically, the lower price is shown on the listing and applied at checkout without a code. Beyond that, creators share codes on their profile posts, newsletters, YouTube and social accounts, and during sales such as Black Friday."),
    ("How do I use a discount code on Gumroad?",
     "Open the product, click the buy button, and enter the code in the \"Discount code\" field in the checkout panel, then apply it before paying. If a creator gave you a discount link, the code is already in the URL (gumroad.com/l/product/CODE) and is applied for you."),
    ("Why don't I see a discount code box at checkout?",
     "The box only appears if the creator has turned it on for that product. If it is off, the only way to apply a code is a discount link that has the code at the end of the URL. Ask the creator for the link."),
    ("Can I stack two Gumroad coupon codes?",
     "No. Only one code works per product. If purchasing power parity (PPP) pricing is on and gives you a bigger discount than your code, Gumroad applies the bigger one."),
    ("Why is my Gumroad promo code not working?",
     "The usual reasons: it belongs to a different creator's store, it only covers some products, it expired, it hit its usage limit, or there's a typo or space in it. Codes are not shared between creators."),
    ("Is there a Gumroad Black Friday sale?",
     "Gumroad featured creator Black Friday deals on Discover in 2025. Black Friday 2026 falls on November 27. Check the Discover page that week for discounted listings."),
    ("How much does Gumroad cost for sellers?",
     "Gumroad is free to join with no monthly fee. As of 2026 it takes about 10% + $0.50 per direct sale and 30% on sales that come through Discover, plus payment processing. Check Gumroad's pricing page for the current numbers before you sell."),
]

KEYWORDS = ("gumroad discount codes, gumroad coupons, gumroad coupon code, gumroad promo code, "
            "gumroad discount, discount code for gumroad, gumroad code promo, gumroad com discount code, "
            "gumroad discount code how to use, gumroad vrchat, gumroad pricing, sell on gumroad")

TITLE = f"Gumroad Discount Codes & Coupons ({MONTH}) - How to Get Real Gumroad Deals"
DESC = ("Working Gumroad discount codes, coupons and promo deals for "
        f"{MONTH}, plus how to use a Gumroad discount code at checkout. {CTA}.")

DISCLOSURE = ("Affiliate disclosure: links on this page are Gumroad affiliate links. If you buy through them, "
              "I may earn a commission at no extra cost to you. This page is not affiliated with or endorsed by Gumroad, Inc.")

# ---------------------------------------------------------------- README
def readme():
    L = []
    a = L.append
    a(f"# Gumroad Discount Codes & Coupons ({MONTH})\n")
    a(f"> **Last checked: {UPDATED}** - every deal below opens on gumroad.com.\n")
    a(f"## 🎁 [{CTA} →]({MAIN})\n")
    a(f"**[👉 {CTA} on Gumroad Discover]({MAIN})** - browse thousands of creator products, "
      "with automatic creator discounts shown right on the listing.\n")
    a(f"[![{CTA}](https://img.shields.io/badge/%F0%9F%8E%81%20{CTA.replace(' ', '%20')}-Gumroad%20Discover-ff90e8?style=for-the-badge)]({MAIN})\n")
    a("---\n")
    a("## Contents\n")
    for t in ["Gumroad coupons and offers available now", "Deals by category",
              "How to use a Gumroad discount code", "Why your Gumroad promo code isn't working",
              "Gumroad Black Friday 2026", "Selling on Gumroad: pricing", "FAQ"]:
        anchor = t.lower().replace(" ", "-").replace(":", "").replace("'", "")
        a(f"- [{t}](#{anchor})")
    a("")
    a("## Gumroad coupons and offers available now\n")
    a("| Offer | What you get | Link |")
    a("|---|---|---|")
    for title, what, url in OFFERS:
        a(f"| **{title}** | {what} | [{CTA} →]({aff(url)}) |")
    a("")
    a("> **Straight talk:** Gumroad has no single code that works across the whole site. "
      "Every Gumroad coupon belongs to one creator, so be careful with sites that list an \"80% off Gumroad\" code. "
      "The links above take you to the products and categories where creators are running discounts now.\n")
    a("## Deals by category\n")
    a("| Category | Deals |")
    a("|---|---|")
    for name, slug in CATEGORIES:
        a(f"| {name} | [Browse {name} deals →]({aff('https://gumroad.com/' + slug)}) |")
    a("")
    a(f"### [🎁 {CTA} →]({MAIN})\n")
    a("## How to use a Gumroad discount code\n")
    a("**Gumroad discount code: how to use it, step by step**\n")
    a(f"1. Open the product on Gumroad (start from [Gumroad Discover]({MAIN})).")
    a("2. Click the buy button (\"I want this!\" or \"Buy this\").")
    a("3. In the checkout panel, find the **Discount code** field.")
    a("4. Paste your code and apply it. The total updates before you pay.")
    a("5. Finish checkout. Your files or access go to your email and your Gumroad library.\n")
    a("**Have a discount link?** Creators can put the code in the URL: "
      "`gumroad.com/l/PRODUCT/CODE`. Opening that link applies the code automatically.\n")
    a("**Auto-applied discounts:** Since 2026, creators can set a discount to apply automatically. "
      "You'll see the lower price on the listing, with no code to enter. If you have your own code, it takes priority.\n")
    a("## Why your Gumroad promo code isn't working\n")
    a("- **Wrong store:** codes only work in the store of the creator who made them.")
    a("- **Wrong product:** the code may only cover certain products.")
    a("- **Expired or used up:** creators can set an end date and a usage limit.")
    a("- **No code box:** the creator turned off the discount field. Ask them for a discount link.")
    a("- **Stacking:** only one code per product. PPP pricing wins if it's the bigger discount.")
    a("- **Typo:** check for spaces and look-alike characters (O vs 0).\n")
    a("## Gumroad Black Friday 2026\n")
    a("Gumroad featured creator Black Friday deals on Discover in 2025. Black Friday 2026 is **Friday, November 27**, and Cyber Monday is **November 30**. "
      f"That week, [check Gumroad Discover]({MAIN}) for marked-down listings.\n")
    a("## Selling on Gumroad: pricing\n")
    a("Thinking of selling on Gumroad? Some things to know about Gumroad pricing:\n")
    a("- Free to start, with no monthly plan.")
    a("- About **10% + $0.50** per direct sale, and **30%** on sales made through Discover (as of 2026).")
    a("- You can create percentage or fixed-amount discount codes, limit how many times they're used, set expiry dates, and add codes to links.\n")
    a(f"[Start selling on Gumroad →]({SELL_URL})\n")
    a("## FAQ\n")
    for q, ans in FAQ:
        a(f"### {q}\n{ans}\n")
    a("---\n")
    a(f"## 🎁 [{CTA} →]({MAIN})\n")
    a(f"🌐 Web version: {SITE}\n")
    a(f"<sub>{DISCLOSURE}</sub>\n")
    a(f"<sub>Keywords: {KEYWORDS}</sub>")
    return "\n".join(L) + "\n"

# ---------------------------------------------------------------- HTML
def page():
    e = html.escape
    offers = "\n".join(
        f'<div class="offer"><h3>{e(t)}</h3><p>{e(w)}</p>'
        f'<a class="btn" href="{e(aff(u))}" rel="sponsored nofollow noopener" target="_blank">{CTA} &rarr;</a></div>'
        for t, w, u in OFFERS)
    cats = "\n".join(
        f'<a class="cat" href="{e(aff("https://gumroad.com/" + s))}" rel="sponsored nofollow noopener" target="_blank">{e(n)}</a>'
        for n, s in CATEGORIES)
    faq = "\n".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    schema = json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}, ensure_ascii=False)
    cta = lambda label=CTA: f'<a class="btn big" href="{e(MAIN)}" rel="sponsored nofollow noopener" target="_blank">{label} &rarr;</a>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<meta name="keywords" content="{e(KEYWORDS)}">
<link rel="canonical" href="{SITE}">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{SITE}">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{schema}</script>
<style>
:root{{--ink:#000;--paper:#fff;--pink:#ff90e8;--muted:#555}}
*{{box-sizing:border-box}}
body{{margin:0;font:17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--paper)}}
main{{max-width:900px;margin:0 auto;padding:32px 20px 64px}}
h1{{font-size:2.3rem;line-height:1.15;margin:.2em 0 .3em}}
h2{{font-size:1.6rem;margin:2.2em 0 .6em;border-bottom:2px solid var(--ink);padding-bottom:.2em}}
h3{{margin:.2em 0}}
.meta{{color:var(--muted);font-size:.95rem}}
.hero{{border:2px solid var(--ink);background:var(--pink);padding:28px;margin:24px 0;box-shadow:6px 6px 0 var(--ink)}}
.hero p{{margin:.4em 0 1.2em;font-size:1.1rem}}
.btn{{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:10px 18px;border:2px solid var(--ink)}}
.btn:hover{{background:var(--pink);color:var(--ink)}}
.btn.big{{font-size:1.2rem;padding:14px 26px}}
.offers{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}
.offer{{border:2px solid var(--ink);padding:18px;display:flex;flex-direction:column}}
.offer p{{flex:1;margin:.4em 0 1em}}
.note{{border-left:4px solid var(--ink);background:#f5f5f5;padding:12px 16px;margin:20px 0}}
.cats{{display:flex;flex-wrap:wrap;gap:8px}}
.cat{{border:2px solid var(--ink);padding:6px 12px;text-decoration:none;color:var(--ink);font-weight:600}}
.cat:hover{{background:var(--pink)}}
details{{border:2px solid var(--ink);padding:12px 16px;margin:10px 0}}
summary{{font-weight:700;cursor:pointer}}
code{{background:#f0f0f0;padding:2px 6px}}
footer{{font-size:.85rem;color:var(--muted);margin-top:48px;border-top:1px solid #ccc;padding-top:16px}}
</style>
</head>
<body>
<main>
<p class="meta">Last checked {UPDATED}</p>
<h1>Gumroad Discount Codes &amp; Coupons ({MONTH})</h1>
<p>Here are the working Gumroad coupons and deals, how to use a Gumroad discount code at checkout, and why a Gumroad promo code sometimes fails.</p>

<section class="hero">
<h2 style="border:0;margin:0">🎁 Our main Gumroad offer</h2>
<p>Browse Gumroad Discover. Creator discounts that apply automatically show the lower price right on the listing.</p>
{cta()}
</section>

<h2>Gumroad coupons and offers available now</h2>
<div class="offers">
{offers}
</div>
<div class="note"><strong>Straight talk:</strong> Gumroad has no single code that works across the whole site. Every Gumroad coupon code belongs to one creator, so be careful with sites that list an "80% off Gumroad" code. The links above take you to products and categories where creators are running discounts now.</div>

<h2>Gumroad deals by category</h2>
<div class="cats">
{cats}
</div>

<h2>How to use a Gumroad discount code</h2>
<ol>
<li>Open the product on Gumroad (start from <a href="{e(MAIN)}" rel="sponsored nofollow noopener" target="_blank">Gumroad Discover</a>).</li>
<li>Click the buy button ("I want this!" or "Buy this").</li>
<li>In the checkout panel, find the <strong>Discount code</strong> field.</li>
<li>Paste your code and apply it. The total updates before you pay.</li>
<li>Finish checkout. Your files or access go to your email and your Gumroad library.</li>
</ol>
<p><strong>Have a discount link?</strong> Creators can put the code in the URL: <code>gumroad.com/l/PRODUCT/CODE</code>. Opening that link applies the code for you.</p>
<p><strong>Auto-applied discounts:</strong> Since 2026, creators can set a discount to apply automatically. You'll see the lower price on the listing, with no code to enter.</p>

<h2>Why your Gumroad promo code isn't working</h2>
<ul>
<li><strong>Wrong store:</strong> codes only work in the store of the creator who made them.</li>
<li><strong>Wrong product:</strong> the code may only cover certain products.</li>
<li><strong>Expired or used up:</strong> creators can set an end date and a usage limit.</li>
<li><strong>No code box:</strong> the creator turned off the discount field. Ask them for a discount link.</li>
<li><strong>Stacking:</strong> only one code per product. PPP pricing wins if it's the bigger discount.</li>
<li><strong>Typo:</strong> check for spaces and look-alike characters (O vs 0).</li>
</ul>

<h2>Gumroad Black Friday 2026</h2>
<p>Gumroad featured creator Black Friday deals on Discover in 2025. Black Friday 2026 is <strong>Friday, November 27</strong>, and Cyber Monday is <strong>November 30</strong>. That week, check Discover for marked-down listings.</p>
{cta()}

<h2>Selling on Gumroad: pricing</h2>
<ul>
<li>Free to start, with no monthly plan.</li>
<li>About <strong>10% + $0.50</strong> per direct sale, and <strong>30%</strong> on sales made through Discover (as of 2026).</li>
<li>You can create percentage or fixed-amount discount codes, limit uses, set expiry dates, and add codes to links.</li>
</ul>
<p><a class="btn" href="{e(SELL_URL)}" rel="sponsored nofollow noopener" target="_blank">Start selling on Gumroad &rarr;</a></p>

<h2>Gumroad discount code FAQ</h2>
{faq}

<section class="hero" style="text-align:center">
<h2 style="border:0;margin:0 0 .5em">Ready to save?</h2>
{cta()}
</section>

<footer>
<p>{e(DISCLOSURE)}</p>
<p><a href="{REPO}">Source on GitHub</a></p>
</footer>
</main>
</body>
</html>
"""

def main():
    root = pathlib.Path(__file__).parent
    (root / "README.md").write_text(readme())
    d = root / "docs"; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page())
    (d / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    (d / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{SITE}</loc><lastmod>2026-11-10</lastmod><changefreq>weekly</changefreq></url>\n"
        "</urlset>\n")
    (d / ".nojekyll").write_text("")
    print("built README.md and docs/")

if __name__ == "__main__":
    main()
