#!/usr/bin/env python3
"""Generate Grand Cayman Shore Excursion static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://grandcaymanshoreexcursion.com"
SITE = "Grand Cayman Shore Excursion"
DATE = "2026-06-04"

HOME_HERO = "images/hero-grand-cayman.png"
HOME_HERO_ALT = (
    "Cruise passengers interacting with southern stingrays in crystal-clear turquoise water "
    "at Stingray City sandbar Grand Cayman with excursion catamarans under a blue sky"
)
BEST_IMG = "images/best-grand-cayman-excursions.png"
BEST_ALT = (
    "Underwater view of a southern stingray and silver fish in clear turquoise water "
    "at Stingray City sandbar Grand Cayman — best shore excursion experience"
)
PORT_IMG = "images/grand-cayman-cruise-port.png"
PORT_ALT = (
    "George Town Grand Cayman waterfront with cruise passenger tender boats in the harbour "
    "and colourful port buildings with blue roofs under a clear sky"
)
ONE_DAY_IMG = "images/one-day-grand-cayman.png"
ONE_DAY_ALT = (
    "Colourful George Town Grand Cayman waterfront street with turquoise harbour, "
    "colonial buildings and National Museum near the cruise port"
)
STINGRAY_IMG = "images/stingray-city-hero.png"
STINGRAY_ALT = (
    "Tourists with excursion guides interacting with stingrays in shallow turquoise water "
    "at Stingray City sandbar Grand Cayman with tour boats anchored nearby"
)
SEVEN_MILE_IMG = "images/seven-mile-beach-hero.png"
SEVEN_MILE_ALT = (
    "Aerial view of Seven Mile Beach Grand Cayman with white sand, turquoise reef water, "
    "resorts along the coast and excursion boats near shore"
)
SNORKEL_IMG = "images/grand-cayman-snorkelling.png"
SNORKEL_ALT = (
    "Aerial view of snorkellers in clear turquoise water over visible reef and seabed "
    "on a Grand Cayman barrier reef snorkelling tour"
)
STARFISH_IMG = "images/starfish-point-hero.png"
STARFISH_ALT = (
    "Hands gently holding a large starfish in shallow clear turquoise water "
    "at Starfish Point Grand Cayman"
)
PRIVATE_IMG = "images/grand-cayman-private-tours.png"
PRIVATE_ALT = (
    "Aerial view of a private motor yacht in turquoise shallow water off Grand Cayman "
    "with guests swimming near stingrays on a custom charter tour"
)
CRYSTAL_IMG = "images/crystal-caves-hero.png"
CRYSTAL_ALT = (
    "Stalactites and turquoise underground pool with reflections inside "
    "Crystal Caves Grand Cayman on a guided shore excursion tour"
)
GLASS_IMG = "images/glass-bottom-boat-hero.png"
GLASS_ALT = (
    "View through glass-bottom boat windows of tropical fish and reef seabed "
    "in clear turquoise Grand Cayman water on a cruise shore excursion"
)
FAMILY_IMG = "images/grand-cayman-family.png"
FAMILY_ALT = (
    "Child and adult interacting with stingrays in shallow turquoise water at Stingray City "
    "Grand Cayman on a family-friendly cruise shore excursion"
)
HORSE_IMG = "images/horseback-riding-hero.png"
HORSE_ALT = (
    "Three riders on horses trotting along a sandy beach beside turquoise ocean "
    "on a Grand Cayman horseback riding shore excursion"
)
FISH_IMG = "images/fishing-charter-hero.png"
FISH_ALT = (
    "Angler holding a large tuna on the deck of a sport fishing charter boat "
    "in blue ocean off Grand Cayman"
)
CATAMARAN_IMG = "images/catamaran-tour.jpg"
CATAMARAN_ALT = "Private catamaran sailing in turquoise water off Grand Cayman on a cruise port day"
INTRO_IMG = "images/grand-cayman-intro.png"
INTRO_ALT = (
    "Aerial view of Grand Cayman island showing Seven Mile Beach, turquoise reef water, "
    "resorts and boats along the coastline"
)


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: linear-gradient(135deg, rgba(7, 89, 133, 0.78) 0%, rgba(13, 148, 136, 0.55) 55%, rgba(0, 0, 0, 0.4) 100%), url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Grand Cayman guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="grand-cayman-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-grand-cayman-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="stingray-city-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Stingray City</a>
    <span class="text-gray-300">·</span>
    <a href="seven-mile-beach-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Seven Mile Beach</a>
    <span class="text-gray-300">·</span>
    <a href="grand-cayman-snorkelling-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Snorkelling</a>
    <span class="text-gray-300">·</span>
    <a href="starfish-point-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Starfish Point</a>
    <span class="text-gray-300">·</span>
    <a href="grand-cayman-private-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Private Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grand-cayman-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Stingray City", "2.5–3.5 hrs", "Iconic sandbar experience", "Low — standing in shallow water", "stingray-city-excursions.html"),
        ("Barrier Reef Snorkelling", "3–4 hrs", "Reef lovers &amp; swimmers", "Moderate — boat &amp; swim", "grand-cayman-snorkelling-tours.html"),
        ("Starfish Point", "3–4 hrs", "Calm shallow bay photos", "Low — wading optional", "starfish-point-excursions.html"),
        ("Seven Mile Beach", "4–6 hrs", "Beach &amp; resort clubs", "Low — sand &amp; swim", "seven-mile-beach-excursions.html"),
        ("Crystal Caves", "3–4 hrs", "Land adventure &amp; geology", "Moderate — cave walking", "crystal-caves-tours.html"),
        ("Glass Bottom Boats", "2–3 hrs", "Non-swimmers &amp; seniors", "Low — seated viewing", "glass-bottom-boat-tours-grand-cayman.html"),
        ("Horseback Riding", "2–3 hrs", "Scenic coastal rides", "Moderate — riding", "grand-cayman-horseback-riding.html"),
        ("Dolphin &amp; Turtle", "2–4 hrs", "Marine encounters", "Low to moderate", "grand-cayman-family-excursions.html"),
        ("Private Catamaran", "4–6 hrs", "Groups wanting flexibility", "Low to moderate", "grand-cayman-private-tours.html"),
        ("Fishing Charters", "4–6 hrs", "Anglers &amp; sport fish", "Moderate — boat", "grand-cayman-fishing-charters.html"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-sky-50 hover:bg-sky-50/50">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-teal-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sky-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Grand Cayman Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your port day to the experience that fits your time, mobility and interests — all timed for George Town cruise schedules.</p>
  <div class="overflow-x-auto rounded-3xl border border-sky-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-sky-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="7–10 hours (typical)",
        best_for="Stingray City, reef snorkel, beaches",
        activity_level="Varies by tour — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Build your own buffer; confirm operator return plan",
        popular="Stingray sandbar, snorkel boats, Seven Mile Beach",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


# --- Heroes ---

def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: linear-gradient(135deg, rgba(7, 89, 133, 0.78) 0%, rgba(13, 148, 136, 0.55) 55%, rgba(0, 0, 0, 0.4) 100%), url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Cayman Islands · George Town</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Grand Cayman Shore<br/><span class="text-teal-300">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Stingray City sandbar, barrier reef snorkelling, Seven Mile Beach and Starfish Point — the highest-intent experiences cruise passengers book in Grand Cayman.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-grand-cayman-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="stingray-city-excursions.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Stingray City</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Stingray City</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Turquoise Sandbar</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Seven Mile Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Snorkelling</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


# --- Content ---

def _content_home() -> str:
    cards = _card_grid([
        (STINGRAY_IMG, STINGRAY_ALT, "Stingray City", "Waist-deep turquoise sandbar with southern stingrays — Grand Cayman's signature cruise excursion.", "stingray-city-excursions.html", "Stingray City"),
        (SNORKEL_IMG, SNORKEL_ALT, "Reef Snorkelling", "Barrier reef boat trips with gear, guides and cruise-friendly return times.", "grand-cayman-snorkelling-tours.html", "Snorkelling"),
        (SEVEN_MILE_IMG, SEVEN_MILE_ALT, "Seven Mile Beach", "White sand, calm swim and resort beach clubs west of George Town.", "seven-mile-beach-excursions.html", "Beach Guide"),
        (STARFISH_IMG, STARFISH_ALT, "Starfish Point", "Shallow bay with starfish — short boat ride from the port.", "starfish-point-excursions.html", "Starfish Point"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>George Town Cruise Port</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Choose Grand Cayman</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Grand Cayman delivers clear shallow water at Stingray City, world-class reef snorkelling minutes from George Town, and postcard beaches — all on a typical <strong>7–10 hour</strong> port call.</p>
        <a href="best-grand-cayman-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-amber-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Grand Cayman Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 bg-ocean-800"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Grand Cayman Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="grand-cayman-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="grand-cayman-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (STINGRAY_IMG, STINGRAY_ALT, "Stingray City", "Chance to meet southern stingrays in shallow North Sound water — conditions and wildlife vary.", "stingray-city-excursions.html", "Stingray guide"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling", "Coral gardens, turtles and reef fish on barrier reef snorkel boats.", "grand-cayman-snorkelling-tours.html", "Reef Tours"),
        (SEVEN_MILE_IMG, SEVEN_MILE_ALT, "Seven Mile Beach", "Beach breaks with chairs, calm water and timed returns.", "seven-mile-beach-excursions.html", "Beach Day"),
        (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Catamarans, island drives and custom combos for your group.", "grand-cayman-private-tours.html", "Private Tours"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Grand Cayman Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Operators meet near <strong>George Town cruise terminals</strong> and typically plan returns with enough time before all aboard — confirm with the operator.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on tours",
        popular="Tender/walk port, taxis, organised pickups",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock or tender into <strong>George Town</strong> on Grand Cayman. Calls usually run <strong>7–10 hours</strong> — enough for Stingray City, a reef snorkel and a beach stop if you start early.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-gray-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-sky-100"><h3 class="font-display font-bold text-lg mb-2">George Town Piers</h3><p class="text-gray-600">Royal Watler and adjacent berths place you in downtown George Town — shopping, taxis and tour desks within minutes.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-sky-100"><h3 class="font-display font-bold text-lg mb-2">Tender Days</h3><p class="text-gray-600">Many Grand Cayman calls tender ashore, but arrangements vary by ship, pier capacity and the day. Confirm with your cruise line how you will land — and build tender queue time into morning Stingray or afternoon beach plans.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sky-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Cayman Islands dollar (KYD); <strong>US dollars</strong> widely accepted at excursions and taxis.</p></div>
        <div class="bg-teal-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English — straightforward for North American and UK cruise guests.</p></div>
        <div class="bg-sky-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Licensed taxis at the pier; most Stingray and reef tours include boat transfer from marinas near town.</p></div>
      </div>
      <p class="text-center mt-8"><a href="one-day-in-grand-cayman.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Stingray + snorkel or beach combo")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for a <strong>7–10 hour</strong> George Town call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sky-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Grand Cayman Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sky-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet Stingray City boat at marina — morning slots have calmer North Sound.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sky-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Stingray City sandbar</strong><p class="text-gray-600 mt-1">Waist-deep turquoise water with southern stingrays.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sky-100"><span class="font-bold text-ocean-600 shrink-0">11:30</span><div><strong>Barrier reef snorkel</strong><p class="text-gray-600 mt-1">Second stop on many combo tours — coral and tropical fish.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sky-100"><span class="font-bold text-ocean-600 shrink-0">14:00</span><div><strong>Seven Mile Beach or Starfish Point</strong><p class="text-gray-600 mt-1">If time allows — otherwise return early with buffer.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sky-100"><span class="font-bold text-ocean-600 shrink-0">16:30</span><div><strong>Back at pier</strong><p class="text-gray-600 mt-1">Build your own buffer before published all-aboard — confirm times with your ship and operator.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_stingray() -> str:
    return _content_excursion_page(
        "Stingray City is a shallow sandbar on Grand Cayman's North Sound where guests may encounter southern stingrays in typically waist-deep turquoise water. Wildlife sightings are never guaranteed — numbers and behaviour vary with conditions, boat traffic and the day. Many cruise visitors combine the sandbar with a reef snorkel stop on the same boat.",
        [
            "Morning departures often mean calmer water and smaller crowds — still confirm with the operator.",
            "Listen to the crew briefing — gentle interaction protects stingrays when they are present.",
            "Wear reef-safe sunscreen; water shoes optional on the boat.",
            "Combo tours can save time vs separate Stingray and snorkel bookings — confirm return timing in writing.",
        ],
        dict(
            best_for="First-time Grand Cayman visitors",
            activity_level="Low — standing in shallow water",
            popular="Stingray sandbar boats, snorkel combos",
        ),
        STINGRAY_IMG,
        STINGRAY_ALT,
    )


def _content_seven_mile() -> str:
    return _content_excursion_page(
        "Seven Mile Beach is Grand Cayman's famous white-sand strip west of George Town — calm Caribbean water, public access points and resort beach clubs. Organised cruise transfers typically include transport and a timed return window to the pier — confirm details with the operator.",
        [
            "Public beach access is common; resort clubs may charge separately for chairs or facilities — confirm on the day.",
            "Traffic from George Town can take roughly 15–25 minutes — confirm pickup time.",
            "Pair with morning Stingray City only if your ship stays late and you build a sensible return buffer.",
            "Reef-safe sunscreen and shade hats recommended.",
        ],
        dict(
            best_for="Beach lovers and relaxed port days",
            activity_level="Low — swimming and walking on sand",
            popular="Beach breaks, resort club days",
        ),
        SEVEN_MILE_IMG,
        SEVEN_MILE_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Grand Cayman's barrier reef sits close to George Town — snorkel boats reach coral gardens, sponges and tropical fish in clear water. Tours supply masks, fins and a guide; many bundle Stingray City on the same itinerary.",
        [
            "Half-day reef trips fit most 7–10 hour port calls.",
            "Beginners welcome — flotation aids often available.",
            "Avoid sunscreens that harm coral; rash guards work well.",
            "Glass-bottom boats suit guests who prefer not to swim.",
        ],
        dict(
            best_for="Reef enthusiasts and active swimmers",
            activity_level="Moderate — boat entry and snorkelling",
            popular="Two-stop snorkel, Stingray + reef combos",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_starfish() -> str:
    return _content_excursion_page(
        "Starfish Point (Starfish Beach) is a shallow bay on Grand Cayman's east end where starfish rest on the sandy bottom in calm turquoise water. Excursions are shorter than a full Stingray day and pair well with rum-cake stops or a condensed island drive.",
        [
            "Do not remove starfish from the water — observe gently for photos.",
            "Water is shallow — ideal for wading with kids under supervision.",
            "Allow extra drive time from George Town on traffic-heavy ship days.",
            "Often sold as a combo with Stingray City or beach time.",
        ],
        dict(
            best_for="Photographers and families with young children",
            activity_level="Low — optional wading",
            popular="Starfish Point boats, east-end island tours",
        ),
        STARFISH_IMG,
        STARFISH_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private catamarans, SUVs and charter boats let your group set the pace — Stingray City first, custom snorkel stops, Seven Mile Beach lunch, or a fishing run. Operators who serve cruise guests usually plan around all-aboard — still confirm return timing in writing.",
        [
            "Split cost across families to rival per-person coach pricing.",
            "Share your must-see list when booking — routes are flexible.",
            "Catamarans suit groups wanting shade, snorkel and sailing.",
            "Confirm return time in writing before payment.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private catamarans, custom island tours",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_crystal() -> str:
    return _content_excursion_page(
        "Crystal Caves on Grand Cayman offer guided walks through limestone caverns with stalactites and underground lakes — a land-based contrast to Stingray City and reef tours. Allow 3–4 hours including transfer from George Town.",
        [
            "Wear closed-toe shoes with grip — paths can be damp.",
            "Cooler underground temperatures — light layer helps.",
            "Less crowded than sandbar boats on heavy ship days.",
            "Combine with a short downtown stop if returning early.",
        ],
        dict(
            best_for="Guests who want a break from water activities",
            activity_level="Moderate — walking in caves",
            popular="Crystal Caves guided tours",
        ),
        CRYSTAL_IMG,
        CRYSTAL_ALT,
    )


def _content_glass() -> str:
    return _content_excursion_page(
        "Glass-bottom boats reveal Grand Cayman's reef without entering the water — coral, sponges and reef fish viewed from shaded seating. Shorter than full snorkel sails, leaving time for shopping or a quick Stingray combo on long port days.",
        [
            "Morning trips often have calmer water for viewing.",
            "Ideal for non-swimmers, seniors and mixed-age families.",
            "Still follow reef protection rules — no touching coral.",
            "Ask if tour includes narration and reef park fees.",
        ],
        dict(
            best_for="Non-swimmers and low-mobility guests",
            activity_level="Low — seated boat tour",
            popular="Glass-bottom reef tours",
        ),
        GLASS_IMG,
        GLASS_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in Grand Cayman focus on gentle Stingray City visits, shallow Starfish Point, dolphin and turtle encounters, and calm Seven Mile Beach time. Avoid over-packing the day — two stops beat three rushed attractions with kids.",
        [
            "Stingray sandbar suits school-age children with supervision.",
            "Marine encounter facilities publish age rules — check when booking.",
            "Private vans simplify nap timing and snack stops.",
            "Reef snorkel operators often offer junior gear.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Stingray combos, turtle centre, beach breaks",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_horseback() -> str:
    return _content_excursion_page(
        "Horseback riding along Grand Cayman's coastline and inland trails offers a scenic land adventure between water-based tours. Most rides run 2–3 hours with briefing and transfer — leaving afternoon time for beach or shopping if your ship stays late.",
        [
            "Wear long pants and closed-toe shoes where required.",
            "Check weight and age limits with the operator.",
            "Morning rides avoid afternoon heat and showers.",
            "Not ideal for guests with serious mobility limitations.",
        ],
        dict(
            best_for="Scenic adventure seekers",
            activity_level="Moderate — riding and mounting",
            popular="Coastal trail rides",
        ),
        HORSE_IMG,
        HORSE_ALT,
    )


def _content_fishing() -> str:
    return _content_excursion_page(
        "Sport fishing charters depart from George Town for blue water trolling and bottom fishing — mahi-mahi, tuna and reef species depending on season. Half-day and full-day trips are available; confirm duration against your ship's all-aboard.",
        [
            "Licences and gear usually included — ask what's provided.",
            "Motion-sensitive guests should take medication early.",
            "Catch-and-release vs keep policies vary — clarify ahead.",
            "Private charters let your group split cost.",
        ],
        dict(
            best_for="Anglers and sport-fishing enthusiasts",
            activity_level="Moderate — boat and fishing effort",
            popular="Half-day trolling, private charters",
        ),
        FISH_IMG,
        FISH_ALT,
    )


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-sky-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Grand Cayman?</summary>
        <p class="mt-4 text-sm text-gray-500">Most calls are 7 to 10 hours. Stingray City combos take roughly 3–4 hours; adding Seven Mile Beach needs an early start and a late all-aboard.</p></details>
      <details class="faq-item rounded-2xl border border-sky-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Stingray City safe for children?</summary>
        <p class="mt-4 text-sm text-gray-500">Yes, with crew supervision on organised tours. Water is shallow; follow briefing so kids interact gently with stingrays.</p></details>
      <details class="faq-item rounded-2xl border border-sky-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Do I need Cayman Islands cash?</summary>
        <p class="mt-4 text-sm text-gray-500">US dollars are widely accepted. Small vendors may prefer cash; ATMs are in George Town near the port.</p></details>
      <details class="faq-item rounded-2xl border border-sky-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Tender port or dock?</summary>
        <p class="mt-4 text-sm text-gray-500">Depends on the ship and pier assignment. Check your daily programme — add tender time when booking morning Stingray departures.</p></details>
      <details class="faq-item rounded-2xl border border-sky-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        ("How long do cruise ships stay in Grand Cayman?", "Most calls are 7 to 10 hours. Stingray combos take about 3–4 hours."),
        ("Is Stingray City safe for children?", "Yes on organised tours with crew supervision in shallow water."),
        ("Do I need Cayman Islands cash?", "US dollars are widely accepted; ATMs are in George Town."),
        ("Tender port or dock?", "Depends on ship and pier — add tender time to morning tour planning."),
        ("Ship excursion or book independently?", "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer."),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building Grand Cayman site…")

    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-sky-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Grand Cayman<br/><span class="text-[10px] font-body font-normal text-teal-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-grand-cayman-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="stingray-city-excursions.html" data-nav="stingray" class="text-gray-600 hover:text-ocean-600 transition-colors">Stingray City</a>
        <a href="seven-mile-beach-excursions.html" data-nav="beaches" class="text-gray-600 hover:text-ocean-600 transition-colors">Beaches</a>
        <a href="grand-cayman-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="grand-cayman-private-tours.html" data-nav="private" class="text-gray-600 hover:text-ocean-600 transition-colors">Private Tours</a>
        <a href="grand-cayman-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-grand-cayman-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sky-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Grand Cayman from George Town port. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-grand-cayman-shore-excursions.html" class="hover:text-white transition-colors">All Excursions</a></li>
            <li><a href="stingray-city-excursions.html" class="hover:text-white transition-colors">Stingray City</a></li>
            <li><a href="grand-cayman-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="seven-mile-beach-excursions.html" class="hover:text-white transition-colors">Seven Mile Beach</a></li>
            <li><a href="starfish-point-excursions.html" class="hover:text-white transition-colors">Starfish Point</a></li>
            <li><a href="crystal-caves-tours.html" class="hover:text-white transition-colors">Crystal Caves</a></li>
            <li><a href="glass-bottom-boat-tours-grand-cayman.html" class="hover:text-white transition-colors">Glass Bottom Boats</a></li>
            <li><a href="grand-cayman-private-tours.html" class="hover:text-white transition-colors">Private Tours</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="grand-cayman-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-grand-cayman.html" class="hover:text-white transition-colors">One Day in Grand Cayman</a></li>
            <li><a href="grand-cayman-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="grand-cayman-horseback-riding.html" class="hover:text-white transition-colors">Horseback Riding</a></li>
            <li><a href="grand-cayman-fishing-charters.html" class="hover:text-white transition-colors">Fishing Charters</a></li>
            <li><a href="grand-cayman-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        """<section class="trust-strip" aria-label="Grand Cayman shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Stingray City Sandbar</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Barrier Reef Snorkelling</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Seven Mile Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Tender-Aware Planning</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "George Town · Cayman Islands",
            "Best Grand Cayman<br/><span class=\"text-teal-300\">Shore Excursions</span>",
            "Compare Stingray City, reef snorkelling, beaches, caves, catamarans and fishing charters for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            "Grand Cayman<br/><span class=\"text-teal-300\">Cruise Port Guide</span>",
            "George Town piers, tenders, taxis, currency and how to plan shore time ashore.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-grand-cayman-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 George Town", "🐟 Stingray City", "🏖️ Seven Mile Beach", "🤿 Reef Snorkel"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            "One Day in<br/><span class=\"text-teal-300\">Grand Cayman</span>",
            "Hour-by-hour plan from gangway to departure — Stingray City, reef snorkel and beach with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in Grand Cayman",
        ),
        "hero-stingray.html": _hero_inner(
            "North Sound Sandbar",
            "Stingray City<br/><span class=\"text-teal-300\">Excursions</span>",
            "Shallow North Sound sandbar tours with a chance to meet southern stingrays — wildlife and conditions vary.",
            STINGRAY_IMG,
            STINGRAY_ALT,
            breadcrumb="Stingray City",
        ),
        "hero-seven-mile.html": _hero_inner(
            "Grand Cayman · Caribbean",
            "Seven Mile Beach<br/><span class=\"text-teal-300\">Excursions</span>",
            "White sand and calm turquoise water — organised beach days with a timed return window you confirm with the operator.",
            SEVEN_MILE_IMG,
            SEVEN_MILE_ALT,
            breadcrumb="Seven Mile Beach",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Barrier Reef · Grand Cayman",
            "Grand Cayman<br/><span class=\"text-teal-300\">Snorkelling</span> Tours",
            "Coral gardens and reef fish in clear water — boat trips from George Town with gear included.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-starfish.html": _hero_inner(
            "East End · Grand Cayman",
            "Starfish Point<br/><span class=\"text-teal-300\">Excursions</span>",
            "Shallow bay with starfish in calm turquoise water — a gentler alternative to long sandbar days.",
            STARFISH_IMG,
            STARFISH_ALT,
            breadcrumb="Starfish Point",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            "Grand Cayman<br/><span class=\"text-violet-300\">Private Tours</span>",
            "Private catamarans, island drives and charter boats at your group's pace.",
            PRIVATE_IMG,
            PRIVATE_ALT,
            breadcrumb="Private Tours",
        ),
        "hero-crystal.html": _hero_inner(
            "North Side · Grand Cayman",
            "Crystal Caves<br/><span class=\"text-teal-300\">Tours</span>",
            "Underground limestone caverns and guided walks — a land adventure between water tours.",
            CRYSTAL_IMG,
            CRYSTAL_ALT,
            breadcrumb="Crystal Caves",
        ),
        "hero-glass-bottom.html": _hero_inner(
            "Reef Without Diving",
            "Glass Bottom Boat<br/><span class=\"text-teal-300\">Tours</span>",
            "View coral and reef fish from a shaded boat — ideal for non-swimmers on a port day.",
            GLASS_IMG,
            GLASS_ALT,
            breadcrumb="Glass Bottom Boats",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            "Grand Cayman<br/><span class=\"text-teal-300\">Family</span> Excursions",
            "Stingray sandbar, turtle encounters, calm beaches and gentle snorkel for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-horseback.html": _hero_inner(
            "Coastal Trails",
            "Grand Cayman<br/><span class=\"text-teal-300\">Horseback</span> Riding",
            "Scenic rides along shoreline and inland paths — a land-based break from reef boats.",
            HORSE_IMG,
            HORSE_ALT,
            breadcrumb="Horseback Riding",
        ),
        "hero-fishing.html": _hero_inner(
            "George Town Marina",
            "Grand Cayman<br/><span class=\"text-teal-300\">Fishing</span> Charters",
            "Sport fishing from the cruise port — trolling and reef fishing with licensed captains.",
            FISH_IMG,
            FISH_ALT,
            breadcrumb="Fishing Charters",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            "Grand Cayman<br/><span class=\"text-teal-300\">Excursions FAQ</span>",
            "Port timing, Stingray City, currency, tenders and booking independent vs ship tours.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-grand-cayman-shore-excursions.html": _content_best(),
        "grand-cayman-cruise-port-guide.html": _content_port(),
        "one-day-in-grand-cayman.html": _content_one_day(),
        "stingray-city-excursions.html": _content_stingray(),
        "seven-mile-beach-excursions.html": _content_seven_mile(),
        "grand-cayman-snorkelling-tours.html": _content_snorkelling(),
        "starfish-point-excursions.html": _content_starfish(),
        "grand-cayman-private-tours.html": _content_private(),
        "crystal-caves-tours.html": _content_crystal(),
        "glass-bottom-boat-tours-grand-cayman.html": _content_glass(),
        "grand-cayman-family-excursions.html": _content_family(),
        "grand-cayman-horseback-riding.html": _content_horseback(),
        "grand-cayman-fishing-charters.html": _content_fishing(),
        "grand-cayman-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Stingray City, Reef Snorkel &amp; Beach Tours from George Town",
            description="Plan Grand Cayman shore excursions for cruise passengers — Stingray City sandbar, barrier reef snorkelling, Seven Mile Beach, Starfish Point and private catamarans from George Town port.",
            keywords="Grand Cayman shore excursions, Grand Cayman cruise excursions, Stingray City cruise tour, George Town cruise port tours, Seven Mile Beach excursion",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": f"{DOMAIN}/", "description": "Planning guide for Grand Cayman cruise shore excursions from George Town"},
        ),
        dict(
            file="best-grand-cayman-shore-excursions.html",
            title="Best Grand Cayman Shore Excursions | Compare Cruise Port Tours",
            description="Compare the best Grand Cayman shore excursions — Stingray City, reef snorkelling, Seven Mile Beach, Starfish Point, Crystal Caves, catamarans and fishing with cruise timing.",
            keywords="best Grand Cayman shore excursions, Grand Cayman cruise port tours, compare Grand Cayman excursions, George Town shore trips",
            path="best-grand-cayman-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-grand-cayman-shore-excursions.html",
            preload=BEST_IMG,
            schema={"@context": "https://schema.org", "@type": "WebPage", "name": "Best Grand Cayman Shore Excursions", "url": f"{DOMAIN}/best-grand-cayman-shore-excursions.html"},
        ),
        dict(
            file="grand-cayman-cruise-port-guide.html",
            title="Grand Cayman Cruise Port Guide | George Town for Cruise Passengers",
            description="Grand Cayman cruise port guide — George Town piers, tender tips, taxis, KYD and USD, and top shore excursions timed for your ship's schedule.",
            keywords="Grand Cayman cruise port guide, George Town cruise port, Royal Watler pier, Grand Cayman port day, cruise passenger guide Grand Cayman",
            path="grand-cayman-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="grand-cayman-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={"@context": "https://schema.org", "@type": "Article", "headline": "Grand Cayman Cruise Port Guide", "url": f"{DOMAIN}/grand-cayman-cruise-port-guide.html"},
        ),
        dict(
            file="one-day-in-grand-cayman.html",
            title="One Day in Grand Cayman from a Cruise Ship | Port Itinerary",
            description="How to spend one day in Grand Cayman on a cruise stop — Stingray City, barrier reef snorkel, Seven Mile Beach sample timeline with return-to-ship buffer.",
            keywords="one day in Grand Cayman cruise, Grand Cayman port day itinerary, George Town cruise stop planning",
            path="one-day-in-grand-cayman.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-grand-cayman.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="stingray-city-excursions.html",
            title="Stingray City Excursions | Grand Cayman Cruise Sandbar Tours",
            description="Stingray City excursions from George Town — waist-deep turquoise sandbar with southern stingrays, often combined with reef snorkel for cruise passengers.",
            keywords="Stingray City excursions, Stingray City cruise tour Grand Cayman, North Sound sandbar, George Town stingray tour",
            path="stingray-city-excursions.html",
            data_page="stingray",
            hero="partials/hero-stingray.html",
            content="stingray-city-excursions.html",
            preload=STINGRAY_IMG,
        ),
        dict(
            file="seven-mile-beach-excursions.html",
            title="Seven Mile Beach Excursions | Grand Cayman Cruise Beach Days",
            description="Seven Mile Beach excursions from Grand Cayman cruise port — transport, calm turquoise water, chair rental and timed returns to George Town.",
            keywords="Seven Mile Beach excursion Grand Cayman, Grand Cayman beach day cruise, Seven Mile Beach cruise port",
            path="seven-mile-beach-excursions.html",
            data_page="beaches",
            hero="partials/hero-seven-mile.html",
            content="seven-mile-beach-excursions.html",
            preload=SEVEN_MILE_IMG,
        ),
        dict(
            file="grand-cayman-snorkelling-tours.html",
            title="Grand Cayman Snorkelling Tours | Barrier Reef Cruise Excursions",
            description="Grand Cayman snorkelling tours on the barrier reef — boat trips, gear and guides with cruise-friendly returns from George Town; Stingray combos available.",
            keywords="Grand Cayman snorkelling tours, barrier reef snorkel cruise, George Town snorkel excursion, Grand Cayman reef tour",
            path="grand-cayman-snorkelling-tours.html",
            data_page="snorkelling",
            hero="partials/hero-snorkelling.html",
            content="grand-cayman-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="starfish-point-excursions.html",
            title="Starfish Point Excursions | Starfish Beach Grand Cayman Cruises",
            description="Starfish Point and Starfish Beach excursions — shallow turquoise bay with starfish, ideal for families and photographers on a George Town port day.",
            keywords="Starfish Point Grand Cayman, Starfish Beach excursion cruise, east end Grand Cayman tour",
            path="starfish-point-excursions.html",
            data_page="beaches",
            hero="partials/hero-starfish.html",
            content="starfish-point-excursions.html",
            preload=STARFISH_IMG,
        ),
        dict(
            file="grand-cayman-private-tours.html",
            title="Grand Cayman Private Tours | Catamaran &amp; Custom Cruise Excursions",
            description="Private Grand Cayman tours for cruise passengers — catamarans, charter boats and custom island itineraries with flexible timing from George Town.",
            keywords="Grand Cayman private tours, private catamaran Grand Cayman cruise, custom shore excursion Cayman Islands",
            path="grand-cayman-private-tours.html",
            data_page="private",
            hero="partials/hero-private.html",
            content="grand-cayman-private-tours.html",
            preload=PRIVATE_IMG,
        ),
        dict(
            file="crystal-caves-tours.html",
            title="Crystal Caves Tours Grand Cayman | Cruise Port Cave Excursions",
            description="Crystal Caves tours from George Town cruise port — guided underground limestone caverns, a land adventure between Stingray City and reef trips.",
            keywords="Crystal Caves Grand Cayman tour, Grand Cayman cave excursion cruise, north side Grand Cayman tour",
            path="crystal-caves-tours.html",
            data_page="excursions",
            hero="partials/hero-crystal.html",
            content="crystal-caves-tours.html",
            preload=CRYSTAL_IMG,
        ),
        dict(
            file="glass-bottom-boat-tours-grand-cayman.html",
            title="Glass Bottom Boat Tours Grand Cayman | Reef Views for Cruise Guests",
            description="Glass bottom boat tours in Grand Cayman — view barrier reef coral and fish without diving, ideal for non-swimmers on a George Town port day.",
            keywords="glass bottom boat Grand Cayman, reef boat tour cruise Grand Cayman, non swimmer Grand Cayman excursion",
            path="glass-bottom-boat-tours-grand-cayman.html",
            data_page="snorkelling",
            hero="partials/hero-glass-bottom.html",
            content="glass-bottom-boat-tours-grand-cayman.html",
            preload=GLASS_IMG,
        ),
        dict(
            file="grand-cayman-family-excursions.html",
            title="Grand Cayman Family Excursions | Kid-Friendly Cruise Port Tours",
            description="Family-friendly Grand Cayman excursions — Stingray City, turtle and dolphin encounters, Starfish Point and calm Seven Mile Beach for cruise guests.",
            keywords="Grand Cayman family excursions, kid friendly Grand Cayman cruise tours, family shore excursion Cayman",
            path="grand-cayman-family-excursions.html",
            data_page="stingray",
            hero="partials/hero-family.html",
            content="grand-cayman-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="grand-cayman-horseback-riding.html",
            title="Grand Cayman Horseback Riding | Cruise Shore Excursion Rides",
            description="Grand Cayman horseback riding excursions — coastal and trail rides with cruise-friendly timing and transfers from George Town port.",
            keywords="Grand Cayman horseback riding cruise, horse riding shore excursion Grand Cayman",
            path="grand-cayman-horseback-riding.html",
            data_page="excursions",
            hero="partials/hero-horseback.html",
            content="grand-cayman-horseback-riding.html",
            preload=HORSE_IMG,
        ),
        dict(
            file="grand-cayman-fishing-charters.html",
            title="Grand Cayman Fishing Charters | Sport Fishing from Cruise Port",
            description="Grand Cayman fishing charters for cruise passengers — half-day and private sport fishing from George Town with licensed captains.",
            keywords="Grand Cayman fishing charter cruise, sport fishing George Town, deep sea fishing Grand Cayman excursion",
            path="grand-cayman-fishing-charters.html",
            data_page="excursions",
            hero="partials/hero-fishing.html",
            content="grand-cayman-fishing-charters.html",
            preload=FISH_IMG,
        ),
        dict(
            file="grand-cayman-faq.html",
            title="Grand Cayman Shore Excursions FAQ | Cruise Port Planning",
            description="FAQ for Grand Cayman shore excursions — port hours, Stingray City, tenders, currency, Seven Mile Beach and independent vs ship booking.",
            keywords="Grand Cayman shore excursions FAQ, Grand Cayman cruise port questions, Stingray City FAQ cruise",
            path="grand-cayman-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="grand-cayman-faq.html",
            preload=ONE_DAY_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-grand-cayman-shore-excursions.html", "0.9", "monthly"),
        ("grand-cayman-cruise-port-guide.html", "0.8", "monthly"),
        ("one-day-in-grand-cayman.html", "0.8", "monthly"),
        ("stingray-city-excursions.html", "0.9", "monthly"),
        ("seven-mile-beach-excursions.html", "0.8", "monthly"),
        ("grand-cayman-snorkelling-tours.html", "0.8", "monthly"),
        ("starfish-point-excursions.html", "0.8", "monthly"),
        ("grand-cayman-private-tours.html", "0.8", "monthly"),
        ("crystal-caves-tours.html", "0.7", "monthly"),
        ("glass-bottom-boat-tours-grand-cayman.html", "0.7", "monthly"),
        ("grand-cayman-family-excursions.html", "0.8", "monthly"),
        ("grand-cayman-horseback-riding.html", "0.7", "monthly"),
        ("grand-cayman-fishing-charters.html", "0.7", "monthly"),
        ("grand-cayman-faq.html", "0.7", "monthly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += ["  <url>", f"    <loc>{url}</loc>", f"    <lastmod>{DATE}</lastmod>", f"    <changefreq>{freq}</changefreq>", f"    <priority>{priority}</priority>", "  </url>"]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write(
        "package.json",
        """{
  "name": "grand-cayman-shore-excursion",
  "private": true,
  "scripts": {
    "sync:schedules": "node scripts/sync-schedules.mjs",
    "qa:schedules": "node scripts/qa-schedules.mjs",
    "build": "python3 scripts/build-grand-cayman-site.py && python3 scripts/world2_extend_grand_cayman.py && python3 scripts/generate_schedule_pages.py",
    "build:all": "npm run sync:schedules && npm run qa:schedules && npm run build",
    "images": "python3 scripts/fetch-grand-cayman-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8901"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )

    # Domain may already be attached in Cloudflare; prefer workers_dev for local hygiene.
    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "grand-cayman-shore-excursion",
  "compatibility_date": "2026-06-04",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "workers_dev": true
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)
    print("Done.")


if __name__ == "__main__":
    main()
