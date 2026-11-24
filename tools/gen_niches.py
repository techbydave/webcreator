"""Builds the industry landing pages (websites-for-*.html) from one template.
Each page has its own wording, problems, features and FAQ so it isn't a copy of the others.
Run: python3 tools/gen_niches.py"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://webcreator.techbydave.com/"
SWOOSH = "M1 13c6-1 11-5 17-11 2 4 1 7-2 9 6-1 10-3 17-8-3 7-9 13-20 15-5 1-9-1-12-5z"
ARROW = '<span class="dot"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>'

PAGES = [
    {
        "slug": "websites-for-salons",
        "nav": "Salons",
        "word": "SALON",
        "title": "Salon & Barber Websites in Toronto with Online Booking | WebCreator",
        "desc": "Websites for salons, barbers and beauty studios in Toronto. Clients see your services and prices, request a time online and you approve it in one tap. Live in about 14 days, from $349.",
        "label": "Salons, barbers & beauty studios",
        "h1": 'A salon website that <em>fills your chair.</em>',
        "lead": "Clients find you on Instagram, then have to DM you to book. Give them a proper website with your services, prices and a booking button, and stop answering \"are you free Saturday?\" all day.",
        "say": "Your work speaks on Instagram. Your website should <em>turn that attention into bookings</em> while you're busy with a client.",
        "problems": [
            ("Booking by DM", "Clients message to ask about prices and times. You reply between appointments, and some never hear back in time."),
            ("No clear price list", "People want to know what a cut, colour or lineup costs before they ask. If they can't see it, they move on."),
            ("Hard to find on Google", "Someone searching \"salon near me\" sees the shops with a Google profile and photos first."),
        ],
        "features": [
            ("Service menu with prices", "Every service, how long it takes and what it costs, easy to update."),
            ("Online booking requests", "Clients pick a service and a time. You approve it from your dashboard and they get a confirmation email."),
            ("Your best work, front and centre", "A photo gallery of your cuts, colours and styles, linked to your Instagram."),
            ("Google Business Profile", "Show up on Google Maps with your photos, hours and a link to book."),
            ("Pro email", "you@yoursalon.ca instead of a Gmail address."),
            ("Flyers & business cards", "Designs with your booking link and QR code, ready to print."),
        ],
        "faq": [
            ("Can clients book when I'm closed?", "Yes. They can send a booking request any time. It waits in your dashboard and you approve it when you're free."),
            ("I already get clients from Instagram. Why do I need a website?", "Instagram gets attention. A website gives people one place to see your prices and book, shows up on Google, and belongs to you if the algorithm changes."),
            ("Can I show each stylist or barber?", "Yes. Each person can have their own photo, specialties and work on the site."),
            ("Can clients pay a deposit online?", "Online payments aren't part of the standard package. If you need deposits, tell me and I'll include it in your quote."),
        ],
    },
    {
        "slug": "websites-for-counsellors",
        "nav": "Counsellors",
        "word": "CALM",
        "title": "Websites for Counsellors & Therapists in Toronto | WebCreator",
        "desc": "Calm, trustworthy websites for counsellors, therapists and coaches in Toronto. Explain your approach, let clients request a consultation online and manage it all from a private dashboard. From $349.",
        "label": "Counsellors, therapists & coaches",
        "h1": 'A practice website that feels <em>safe to reach out to.</em>',
        "lead": "Reaching out for help is hard. Your website should make it easy: a calm design, a clear explanation of how you work, and a simple way to request a first session without making a phone call.",
        "say": "People decide whether to contact a counsellor in a few quiet minutes, often late at night. <em>Your website is the first conversation.</em>",
        "problems": [
            ("People don't want to call", "Many new clients would rather send a short request than phone a stranger. Without a form, they don't reach out at all."),
            ("Your approach isn't clear", "Visitors want to know who you help, how sessions work, and what it costs before they commit."),
            ("Booking is all back-and-forth", "Emails and voicemails to find a time eat into your day between sessions."),
        ],
        "features": [
            ("Calm, professional design", "Soft colours, clear writing and plenty of space, built to feel welcoming on a phone."),
            ("Consultation requests", "Clients choose in person or video and a time. You approve it from your dashboard and they get a confirmation email."),
            ("Private dashboard", "Requests and messages are behind your own login, not in a shared inbox."),
            ("Services & fees pages", "Explain individual, couple and family sessions, fees and what to expect."),
            ("Google Business Profile", "Show up when people nearby search for counselling, with your hours and a link to book."),
            ("Pro email", "you@yourpractice.ca for a trustworthy first impression."),
        ],
        "faq": [
            ("Is the information people send private?", "The site runs on a secure (HTTPS) connection and requests are only visible after you log in to your dashboard. I keep forms short and recommend not asking for personal health details in them."),
            ("Can clients request video sessions?", "Yes. You can offer in-person and video sessions, and clients choose when they request a time."),
            ("Have you built a site for a counselling practice before?", "Yes. My first client was a counselling practice: a new website, a booking dashboard, a Google Business Profile and professional email."),
            ("Can I offer a free first consultation?", "Yes. It can be its own option on the booking form, with its own length and description."),
        ],
    },
    {
        "slug": "websites-for-cleaning-services",
        "nav": "Cleaners",
        "word": "CLEAN",
        "title": "Websites for Cleaning Services in Toronto | WebCreator",
        "desc": "Websites for cleaning companies and cleaners in Toronto and the GTA. Get quote requests online, show up on Google Maps and hand out matching flyers and business cards. From $349.",
        "label": "Cleaning companies & cleaners",
        "h1": 'A cleaning website that <em>brings in quotes.</em>',
        "lead": "Most people pick a cleaner after a quick search on their phone. If you're not on Google with a clear way to ask for a quote, they call the next company on the list.",
        "say": "Homeowners don't compare cleaners for hours. They pick <em>the one that looks trustworthy</em> and makes it easy to get a price.",
        "problems": [
            ("Missed calls on the job", "You can't answer the phone with gloves on. Missed calls often turn into lost jobs."),
            ("No way to ask for a quote", "People want a rough price for their home size before they talk to anyone."),
            ("Hard to stand out", "Every cleaner says \"reliable and affordable\". Photos, reviews and a professional look are what win trust."),
        ],
        "features": [
            ("Quote request form", "Customers tell you the service, home size and area. It lands in your dashboard and your email."),
            ("Services & areas you cover", "Regular, deep, move-out and office cleaning, plus the neighbourhoods you serve."),
            ("Google Business Profile", "Show up on Google Maps when people search for cleaners nearby, with reviews and photos."),
            ("Before & after photos", "A simple gallery that shows the quality of your work."),
            ("Flyers & business cards", "Matching designs with a QR code to your quote form, ready for door-to-door."),
            ("Pro email", "bookings@yourcleaning.ca instead of a personal Gmail."),
        ],
        "faq": [
            ("Can customers book a regular clean?", "Yes. They can request a one-time or recurring clean, and you confirm the details and price before approving."),
            ("Can I show the areas I serve?", "Yes. Your site and Google profile can list the neighbourhoods and cities you cover, so you show up in those searches."),
            ("Do the flyers match the website?", "Yes. Flyers and business cards use the same colours and logo, with a QR code that opens your quote form."),
            ("I'm just starting out. Is the Starter Website enough?", "It's a good start: up to five pages, your Google profile and a contact form. You can upgrade to Business Online later."),
        ],
    },
    {
        "slug": "websites-for-contractors",
        "nav": "Contractors",
        "word": "BUILD",
        "title": "Websites for Contractors & Trades in Toronto | WebCreator",
        "desc": "Websites for contractors, renovators, plumbers, electricians and trades in Toronto and the GTA. Show your past projects, get quote requests online and show up on Google Maps. From $349.",
        "label": "Contractors, renovators & trades",
        "h1": 'Show your best jobs. <em>Win the next one.</em>',
        "lead": "Homeowners want to see your work before they let you in the door. A website with your past projects, the areas you cover and a quote form does the selling while you're on site.",
        "say": "Word of mouth gets people to search your name. <em>Your website decides</em> whether they call you or the next company.",
        "problems": [
            ("Your work isn't online", "Your best jobs live in your camera roll, where new customers can't see them."),
            ("Calls you can't take", "You're on a ladder or under a sink. Without a quote form, those leads go cold."),
            ("Not showing up nearby", "\"Contractor near me\" searches go to businesses with a Google profile, photos and reviews."),
        ],
        "features": [
            ("Project gallery", "Before and after photos of kitchens, bathrooms, decks or whatever you do best."),
            ("Quote request form", "Customers describe the job and their area. You get it in your dashboard and by email."),
            ("Services & areas", "A clear list of what you do and where you work across Toronto and the GTA."),
            ("Google Business Profile", "Show up on Google Maps with your photos, reviews and a call button."),
            ("Tap to call", "One tap from your website to your phone for customers who'd rather talk."),
            ("Business cards & flyers", "Matching designs for job sites, hardware store boards and neighbours."),
        ],
        "faq": [
            ("Can customers send photos of the job?", "The standard quote form lets them describe the job in detail. If you need photo uploads, tell me and I'll include it in your quote."),
            ("Can I list my licences and insurance?", "Yes. Showing licences, insurance and warranties is one of the best ways to build trust, and it goes right on your homepage."),
            ("Do I need to write everything myself?", "No. Tell me about your business on a short call and I'll write the pages. You just check them."),
            ("How do I add new projects later?", "Send me the photos and I'll add them, or add them yourself if you're on the Care Plan."),
        ],
    },
]


def nav_brand(href, label=None):
    a = f' aria-label="{label}"' if label else ""
    return f'<a class="brand" href="{href}"{a}><svg viewBox="0 0 34 20" aria-hidden="true"><path d="{SWOOSH}" fill="#1d2a38"/></svg>WebCreator</a>'


def other_links(cur):
    return " &nbsp;·&nbsp; ".join(f'<a href="{p["slug"]}.html">{p["nav"]}</a>' for p in PAGES if p["slug"] != cur)


def page(p):
    e = html.escape
    url = f"{BASE}{p['slug']}.html"
    plain_h1 = p["h1"].replace("<em>", "").replace("</em>", "")
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "name": plain_h1, "serviceType": "Website design", "url": url,
             "audience": {"@type": "BusinessAudience", "name": p["label"]},
             "areaServed": [{"@type": "City", "name": "Toronto"}, "Worldwide"],
             "provider": {"@id": f"{BASE}#business", "@type": "ProfessionalService", "name": "WebCreator by TechByDave", "url": BASE},
             "offers": [{"@type": "Offer", "name": "Starter Website", "price": "349", "priceCurrency": "USD"},
                        {"@type": "Offer", "name": "Business Online", "price": "899", "priceCurrency": "USD"}]},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]},
            {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "WebCreator", "item": BASE},
                                                             {"@type": "ListItem", "position": 2, "name": p["label"], "item": url}]},
        ],
    }
    probs = "".join(f'<div class="val glass rv"><span class="big">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(p["problems"]))
    feats = "".join(f'<div class="chap glass rv feat"><span class="k">0{i + 1}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(p["features"]))
    faq = "".join(f'<div class="q glass"><button type="button" aria-expanded="false" aria-controls="a{i}">{e(q)}<i aria-hidden="true"></i></button><div class="a" id="a{i}"><div><p>{e(a)}</p></div></div></div>' for i, (q, a) in enumerate(p["faq"]))
    checks = "".join(f'<li>{e(t)}</li>' for t, _ in p["features"][:5])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(p["title"])}">
<meta property="og:description" content="{e(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BASE}images/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta name="theme-color" content="#c9d9e5">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False)}
</script>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<nav class="pnav glass" aria-label="Page">
  {nav_brand("index.html")}
  <a class="l" href="#problems">Why</a><a class="l" href="#included">What you get</a><a class="l" href="#faq" data-opt>FAQ</a><a class="l" href="index.html#plans">Plans</a>
  <a class="btn btn-blue" href="index.html#contact" style="padding:0 16px">Get a quote</a>
</nav>

<header class="frame about niche" id="top">
  <nav class="nav" aria-label="Main">
    {nav_brand("index.html", "WebCreator home")}
    <ul><li><a href="index.html#included">What you get</a></li><li><a href="index.html#process">How it works</a></li><li><a href="index.html#plans">Plans</a></li><li><a href="index.html#work">Work</a></li><li><a href="about.html">About</a></li></ul>
    <a class="btn btn-white" href="index.html#contact">Get a quote</a>
  </nav>

  <div class="word" aria-hidden="true">{p["word"]}</div>

  <div class="ahero">
    <div>
      <nav class="crumbs reveal-up" aria-label="Breadcrumb"><a href="index.html">WebCreator</a> <span aria-hidden="true">›</span> <span>{e(p["label"])}</span></nav>
      <h1 class="reveal-up" style="transition-delay:.1s;margin-top:16px">{p["h1"]}</h1>
      <p class="lead reveal-up" style="transition-delay:.25s">{e(p["lead"])}</p>
      <div class="ctas reveal-up" style="transition-delay:.4s;display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn btn-blue" href="index.html#contact">Get a free quote {ARROW}</a>
        <a class="btn btn-white" href="index.html#plans">See plans</a>
      </div>
    </div>
    <aside class="nicard glass floaty reveal-up" style="transition-delay:.3s" aria-label="Business Online package">
      <span class="label">Most popular · Business Online</span>
      <div class="price">$899 <small>USD, one-time</small></div>
      <ul>{checks}</ul>
      <span class="live">Live in about 14 days</span>
    </aside>
  </div>
</header>

<section style="padding-bottom:30px"><div class="wrap">
  <p class="say">{p["say"]}</p>
</div></section>

<section id="problems"><div class="wrap">
  <div class="head rv"><span class="label">Sound familiar?</span><h2>What's costing you <em>customers.</em></h2></div>
  <div class="values four">{probs}
    <a class="val rv" href="index.html#contact" style="background:linear-gradient(160deg,var(--blue2),var(--blue));color:#fff;box-shadow:0 30px 60px rgba(26,92,255,.3)"><span class="big" style="color:#fff">→</span><h3>Let's fix it</h3><p style="color:rgba(255,255,255,.85)">Book a free 15-minute call and get a fixed quote the same day.</p></a>
  </div>
</div></section>

<section id="included" style="padding-top:30px"><div class="wrap">
  <div class="head rv"><span class="label">What you get</span><h2>Everything set up and <em>connected for you.</em></h2><p>Built for {e(p["label"].lower())}, run from one simple dashboard.</p></div>
  <div class="feats">{feats}</div>
</div></section>

<section style="padding-top:30px"><div class="wrap">
  <div class="mission">
    <div class="mcard glass rv"><span class="label">How it works</span><q>From first call to fully online in about 14 days.</q><p>Day 1: a free call and a fixed quote. Days 2–4: you approve your homepage. Days 5–12: I build and connect everything. Day 14: you're live and I walk you through it.</p></div>
    <div class="mcard dark rv"><span class="label">Plans</span><q>Starter $349 · Business Online $899 · Care Plan $39/month</q><p>Prices in USD, fixed before we start. Pay 50% to begin and 50% when you're happy. You own everything. <a href="index.html#plans" style="color:#fff;text-decoration:underline">Compare plans</a></p></div>
  </div>
</div></section>

<section id="faq" style="padding-top:30px"><div class="wrap">
  <div class="head c rv"><span class="label">FAQ</span><h2>Questions {e(p["nav"].lower())} <em>ask.</em></h2></div>
  <div class="faq rv">{faq}</div>
</div></section>

<section style="padding-top:60px"><div class="wrap">
  <div class="contact cta-row rv">
    <div class="bigword" aria-hidden="true">Let's talk</div>
    <div>
      <div class="head" style="margin:0"><span class="label">Free quote</span><h2>Ready to get your business <em>online?</em></h2></div>
      <p class="l">Tell me about your business. I'll reply within one business day with a fixed price and a timeline.</p>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap">
      <a class="btn btn-blue" href="index.html#contact">Get a free quote {ARROW}</a>
      <a class="btn btn-white" href="mailto:dave@techbydave.com">dave@techbydave.com</a>
    </div>
  </div>
</div></section>

<footer><div class="wrap">
  <span>© <span class="year">2026</span> TechByDave · Toronto, Canada</span>
  <span><a href="index.html">Home</a> &nbsp;·&nbsp; {other_links(p["slug"])} &nbsp;·&nbsp; <a href="about.html">About</a></span>
</div></footer>

<script src="assets/site.js"></script>
</body>
</html>
'''


for p in PAGES:
    (ROOT / f'{p["slug"]}.html').write_text(page(p))
    print("wrote", p["slug"])
