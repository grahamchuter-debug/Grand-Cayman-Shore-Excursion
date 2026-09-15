#!/usr/bin/env python3
"""Bake Grand Cayman pages: inline nav/hero/content/footer so first HTML is server-visible.

Run after build-grand-cayman-site.py, world2_extend_grand_cayman.py, generate_schedule_pages.py.
Produces extensionless apex canonicals; does not ship content/ or partials/ (see .assetsignore).
Phase 32B — do not modify other destinations.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://grandcaymanshoreexcursion.com"
SITE = "Grand Cayman Shore Excursion"
EMAIL = "hello@grandcaymanshoreexcursion.com"
TODAY = date.today().isoformat()
FONTS = (
    "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700"
    "&family=Inter:wght@300;400;500;600&display=swap"
)

# filename -> meta. Output stays flat slug.html (CF drop-trailing-slash → /slug).
PAGES: dict[str, dict] = {
    "index.html": {
        "slug": "",
        "page": "home",
        "hero": "partials/hero-home.html",
        "trust": "partials/trust-strip.html",
        "content": "content/home.html",
        "og_image": "images/hero-grand-cayman.png",
        "keep_schema": True,
    },
    "best-grand-cayman-shore-excursions.html": {
        "slug": "best-grand-cayman-shore-excursions",
        "page": "excursions",
        "hero": "partials/hero-excursions.html",
        "trust": "partials/trust-strip.html",
        "content": "content/best-grand-cayman-shore-excursions.html",
        "og_image": "images/best-grand-cayman-excursions.png",
        "keep_schema": True,
    },
    "grand-cayman-cruise-port-guide.html": {
        "slug": "grand-cayman-cruise-port-guide",
        "page": "port",
        "hero": "partials/hero-port-guide.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-cruise-port-guide.html",
        "og_image": "images/grand-cayman-cruise-port.png",
        "keep_schema": True,
    },
    "one-day-in-grand-cayman.html": {
        "slug": "one-day-in-grand-cayman",
        "page": "port",
        "hero": "partials/hero-one-day.html",
        "trust": "partials/trust-strip.html",
        "content": "content/one-day-in-grand-cayman.html",
        "og_image": "images/one-day-grand-cayman.png",
    },
    "stingray-city-excursions.html": {
        "slug": "stingray-city-excursions",
        "page": "stingray",
        "hero": "partials/hero-stingray.html",
        "trust": "partials/trust-strip.html",
        "content": "content/stingray-city-excursions.html",
        "og_image": "images/stingray-city-hero.png",
    },
    "seven-mile-beach-excursions.html": {
        "slug": "seven-mile-beach-excursions",
        "page": "beaches",
        "hero": "partials/hero-seven-mile.html",
        "trust": "partials/trust-strip.html",
        "content": "content/seven-mile-beach-excursions.html",
        "og_image": "images/seven-mile-beach-hero.png",
    },
    "grand-cayman-snorkelling-tours.html": {
        "slug": "grand-cayman-snorkelling-tours",
        "page": "snorkelling",
        "hero": "partials/hero-snorkelling.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-snorkelling-tours.html",
        "og_image": "images/grand-cayman-snorkelling.png",
    },
    "starfish-point-excursions.html": {
        "slug": "starfish-point-excursions",
        "page": "beaches",
        "hero": "partials/hero-starfish.html",
        "trust": "partials/trust-strip.html",
        "content": "content/starfish-point-excursions.html",
        "og_image": "images/starfish-point-hero.png",
    },
    "crystal-caves-tours.html": {
        "slug": "crystal-caves-tours",
        "page": "excursions",
        "hero": "partials/hero-crystal.html",
        "trust": "partials/trust-strip.html",
        "content": "content/crystal-caves-tours.html",
        "og_image": "images/crystal-caves-hero.png",
    },
    "glass-bottom-boat-tours-grand-cayman.html": {
        "slug": "glass-bottom-boat-tours-grand-cayman",
        "page": "snorkelling",
        "hero": "partials/hero-glass-bottom.html",
        "trust": "partials/trust-strip.html",
        "content": "content/glass-bottom-boat-tours-grand-cayman.html",
        "og_image": "images/glass-bottom-boat-hero.png",
    },
    "grand-cayman-private-tours.html": {
        "slug": "grand-cayman-private-tours",
        "page": "private",
        "hero": "partials/hero-private.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-private-tours.html",
        "og_image": "images/grand-cayman-private-tours.png",
    },
    "grand-cayman-family-excursions.html": {
        "slug": "grand-cayman-family-excursions",
        "page": "stingray",
        "hero": "partials/hero-family.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-family-excursions.html",
        "og_image": "images/grand-cayman-family.png",
    },
    "grand-cayman-fishing-charters.html": {
        "slug": "grand-cayman-fishing-charters",
        "page": "excursions",
        "hero": "partials/hero-fishing.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-fishing-charters.html",
        "og_image": "images/fishing-charter-hero.png",
    },
    "grand-cayman-horseback-riding.html": {
        "slug": "grand-cayman-horseback-riding",
        "page": "excursions",
        "hero": "partials/hero-horseback.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-horseback-riding.html",
        "og_image": "images/seven-mile-beach-hero.png",
    },
    "grand-cayman-faq.html": {
        "slug": "grand-cayman-faq",
        "page": "port",
        "hero": "partials/hero-faq.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-faq.html",
        "og_image": "images/one-day-grand-cayman.png",
        "schema": "faq",
    },
    "stingray-city-vs-seven-mile-beach.html": {
        "slug": "stingray-city-vs-seven-mile-beach",
        "page": "excursions",
        "hero": "partials/hero-stingray-vs-beach.html",
        "trust": "partials/trust-strip.html",
        "content": "content/stingray-city-vs-seven-mile-beach.html",
        "og_image": "images/stingray-city-hero.png",
    },
    "grand-cayman-tender-day-planning.html": {
        "slug": "grand-cayman-tender-day-planning",
        "page": "port",
        "hero": "partials/hero-tender-day.html",
        "trust": "partials/trust-strip.html",
        "content": "content/grand-cayman-tender-day-planning.html",
        "og_image": "images/grand-cayman-cruise-port.png",
    },
    "about.html": {
        "slug": "about",
        "page": "about",
        "hero": "partials/hero-about.html",
        "content": "content/about.html",
        "og_image": "images/grand-cayman-intro.png",
        "main_class": "pt-16",
    },
    "contact.html": {
        "slug": "contact",
        "page": "contact",
        "hero": "partials/hero-contact.html",
        "content": "content/contact.html",
        "og_image": "images/grand-cayman-intro.png",
        "main_class": "pt-16",
    },
    "methodology.html": {
        "slug": "methodology",
        "page": "methodology",
        "hero": "partials/hero-methodology.html",
        "content": "content/methodology.html",
        "og_image": "images/grand-cayman-intro.png",
        "main_class": "pt-16",
    },
    "privacy.html": {
        "slug": "privacy",
        "page": "privacy",
        "hero": "partials/hero-privacy.html",
        "content": "content/privacy.html",
        "og_image": "images/grand-cayman-intro.png",
        "main_class": "pt-16",
    },
    "terms.html": {
        "slug": "terms",
        "page": "terms",
        "hero": "partials/hero-terms.html",
        "content": "content/terms.html",
        "og_image": "images/grand-cayman-intro.png",
        "main_class": "pt-16",
    },
    "404.html": {
        "slug": "404",
        "page": "404",
        "content": "content/404.html",
        "og_image": "images/hero-grand-cayman.png",
        "main_class": "pt-16",
        "noindex": True,
        "canonical_override": f"{DOMAIN}/404",
    },
}

PRIORITY = {
    "": 1.0,
    "best-grand-cayman-shore-excursions": 0.9,
    "stingray-city-excursions": 0.9,
    "grand-cayman-snorkelling-tours": 0.8,
    "starfish-point-excursions": 0.8,
    "seven-mile-beach-excursions": 0.8,
    "grand-cayman-cruise-port-guide": 0.8,
    "grand-cayman-tender-day-planning": 0.8,
    "stingray-city-vs-seven-mile-beach": 0.8,
    "one-day-in-grand-cayman": 0.8,
    "grand-cayman-family-excursions": 0.8,
    "grand-cayman-private-tours": 0.8,
    "glass-bottom-boat-tours-grand-cayman": 0.7,
    "crystal-caves-tours": 0.7,
    "grand-cayman-fishing-charters": 0.7,
    "grand-cayman-horseback-riding": 0.7,
    "grand-cayman-faq": 0.7,
}


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def canon_url(slug: str) -> str:
    if slug == "404":
        return f"{DOMAIN}/404"
    if not slug:
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{slug}"


def extensionlessify_html(html: str) -> str:
    def repl(m: re.Match) -> str:
        attr, quote, url = m.group(1), m.group(2), m.group(3)
        if url.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
            return m.group(0)
        if url.startswith(("images/", "/images/", "css/", "/css/", "js/", "/js/")):
            if not url.startswith("/") and not url.startswith("http"):
                return f"{attr}={quote}/{url}{quote}"
            return m.group(0)
        parts = urlsplit(url)
        path = parts.path
        if path.endswith(".html"):
            if path.endswith("index.html"):
                path = path[: -len("index.html")] or "/"
            else:
                path = path[: -len(".html")]
            if path in ("", "index") or path.endswith("/index"):
                path = "/"
        if path == "index" or path == "":
            path = "/"
        if not path.startswith("/"):
            path = "/" + path
        if len(path) > 1 and path.endswith("/"):
            path = path.rstrip("/") or "/"
        rebuilt = path
        if parts.query:
            rebuilt += "?" + parts.query
        if parts.fragment:
            rebuilt += "#" + parts.fragment
        return f"{attr}={quote}{rebuilt}{quote}"

    html = re.sub(r'(href|action)=([\'"])([^\'"]+)\2', repl, html)
    html = re.sub(
        r"""(\b(?:src|href)=)(['"])(?!/|https?:|mailto:|tel:|#|data:)(images/|css/|js/)([^'"]+)\2""",
        lambda m: f"{m.group(1)}{m.group(2)}/{m.group(3)}{m.group(4)}{m.group(2)}",
        html,
    )
    html = re.sub(
        r"""url\((['"]?)(?!/|https?:)(images/[^)'"]+)\1\)""",
        lambda m: f"url({m.group(1)}/{m.group(2)}{m.group(1)})",
        html,
    )
    return html


def extract_existing_schema(shell_path: Path) -> str | None:
    if not shell_path.exists():
        return None
    text = shell_path.read_text(encoding="utf-8")
    m = re.search(
        r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
        text,
        re.S,
    )
    return m.group(1).strip() if m else None


def faq_schema_from_content(content_html: str) -> dict:
    entities = []
    for m in re.finditer(
        r"<details[^>]*>\s*<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>",
        content_html,
        re.S | re.I,
    ):
        q = re.sub(r"<[^>]+>", "", m.group(1))
        a = re.sub(r"<[^>]+>", "", m.group(2))
        q = re.sub(r"\s+", " ", q).strip()
        a = re.sub(r"\s+", " ", a).strip()
        if q and a:
            entities.append(
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
            )
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}


def rewrite_schema_urls(schema_text: str, canon: str) -> str:
    try:
        data = json.loads(schema_text)
    except json.JSONDecodeError:
        return schema_text
    if isinstance(data, dict):
        if "url" in data and isinstance(data["url"], str) and "grandcaymanshoreexcursion.com" in data["url"]:
            if data.get("@type") in ("WebPage", "Article"):
                data["url"] = canon
            elif data.get("@type") == "WebSite":
                data["url"] = f"{DOMAIN}/"

        def fix(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k in ("url", "item") and isinstance(v, str) and v.endswith(".html"):
                        if v.endswith("/index.html"):
                            obj[k] = v[: -len("index.html")] or f"{DOMAIN}/"
                        else:
                            obj[k] = v[: -len(".html")]
                    else:
                        fix(v)
            elif isinstance(obj, list):
                for i in obj:
                    fix(i)

        fix(data)
        return json.dumps(data, ensure_ascii=False, indent=2)
    return schema_text


def build_head(meta: dict, title: str, description: str, schema_json: str | None) -> str:
    if meta.get("canonical_override"):
        url = meta["canonical_override"]
    else:
        url = canon_url(meta["slug"])
    og = f"{DOMAIN}/{meta['og_image']}"
    robots = '  <meta name="robots" content="noindex, follow" />\n' if meta.get("noindex") else ""
    preload = ""
    if meta.get("hero") or meta["slug"] == "":
        preload = f'  <link rel="preload" as="image" href="/{meta["og_image"]}" fetchpriority="high" />\n'
    schema_block = ""
    if schema_json:
        schema_block = f'  <script type="application/ld+json">\n{schema_json}\n  </script>\n'
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
{robots}  <link rel="canonical" href="{url}" />
{preload}  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{og}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
{schema_block}  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
"""


def title_desc_from_shell(filename: str, meta: dict) -> tuple[str, str]:
    shell = ROOT / filename
    if shell.exists():
        text = shell.read_text(encoding="utf-8")
        t = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
        d = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', text, re.I
        )
        title = re.sub(r"\s+", " ", t.group(1)).strip() if t else meta["slug"] or SITE
        desc = d.group(1) if d else ""
        return title, desc
    defaults = {
        "404": (
            "Page not found | Grand Cayman Shore Excursion",
            "The requested Grand Cayman Shore Excursion page was not found.",
        ),
    }
    return defaults.get(meta["slug"], (SITE, ""))


def ensure_utility_heroes() -> None:
    heroes = {
        "partials/hero-about.html": ("About", "Independent George Town cruise planning"),
        "partials/hero-contact.html": ("Contact", "Planning concierge for Grand Cayman port days"),
        "partials/hero-methodology.html": ("Methodology", "How we assess Grand Cayman excursion options"),
        "partials/hero-privacy.html": ("Privacy", "How this planning site handles information"),
        "partials/hero-terms.html": ("Terms of use", "Planning content — not a booking contract"),
    }
    for path, (h1, lead) in heroes.items():
        html = f"""<section class="site-hero site-hero--compact">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: linear-gradient(135deg, rgba(7, 89, 133, 0.78) 0%, rgba(13, 148, 136, 0.55) 55%, rgba(0, 0, 0, 0.4) 100%), url('/images/grand-cayman-intro.png');" role="img" aria-label="Aerial view of Grand Cayman coastline with turquoise reef water"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl pt-8 pb-4">
      <h1 class="site-hero__title text-4xl sm:text-5xl font-display font-bold text-white leading-tight mb-3">{h1}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed max-w-2xl">{lead}</p>
    </div>
  </div>
  <div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>
</section>
"""
        (ROOT / path).write_text(html, encoding="utf-8")
        print(f"  wrote {path}")


def ensure_404_content() -> None:
    path = ROOT / "content" / "404.html"
    path.write_text(
        """<section class="pt-10 pb-20 bg-white">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label mx-auto mb-3">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">That URL is not part of the Grand Cayman shore excursion planning guide. Try the home page, best excursions list, or ship schedule.</p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Grand Cayman home</a>
      <a href="/best-grand-cayman-shore-excursions" class="btn-outline inline-flex items-center justify-center font-semibold px-6 py-3 rounded-full text-sm no-underline border border-ocean-600 text-ocean-700">Best excursions</a>
      <a href="/ship-schedule" class="btn-outline inline-flex items-center justify-center font-semibold px-6 py-3 rounded-full text-sm no-underline border border-ocean-600 text-ocean-700">Ship schedule</a>
    </div>
  </div>
</section>
""",
        encoding="utf-8",
    )
    print("  wrote content/404.html")


def ensure_nav_mobile() -> None:
    """Ensure nav has mobile menu hooks (extensionlessified later)."""
    nav_path = ROOT / "partials" / "nav.html"
    nav = nav_path.read_text(encoding="utf-8")
    if 'id="menu-toggle"' in nav:
        return
    nav = nav.replace(
        '<button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sky-50" aria-label="Open menu">',
        '<button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sky-50" id="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">',
    )
    if 'id="mobile-menu"' not in nav:
        mobile = """
    <div id="mobile-menu" class="hidden lg:hidden pb-4 border-t border-sky-100">
      <div class="flex flex-col gap-3 pt-3 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600">Home</a>
        <a href="best-grand-cayman-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600">Excursions</a>
        <a href="stingray-city-excursions.html" data-nav="stingray" class="text-gray-600 hover:text-ocean-600">Stingray City</a>
        <a href="seven-mile-beach-excursions.html" data-nav="beaches" class="text-gray-600 hover:text-ocean-600">Beaches</a>
        <a href="grand-cayman-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600">Snorkelling</a>
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600">Ship Schedule</a>
        <a href="grand-cayman-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600">Port Guide</a>
        <a href="contact.html" data-nav="contact" class="text-gray-600 hover:text-ocean-600">Contact</a>
      </div>
    </div>
"""
        nav = nav.replace("    </div>\n  </div>\n</nav>", f"    </div>{mobile}  </div>\n</nav>")
    nav_path.write_text(nav, encoding="utf-8")
    print("  patched partials/nav.html mobile menu")


def assemble_page(filename: str, meta: dict) -> str:
    nav = extensionlessify_html(read("partials/nav.html"))
    footer = extensionlessify_html(read("partials/footer.html"))
    hero = extensionlessify_html(read(meta["hero"])) if meta.get("hero") else ""
    trust = extensionlessify_html(read(meta["trust"])) if meta.get("trust") else ""
    content = extensionlessify_html(read(meta["content"]))
    title, description = title_desc_from_shell(filename, meta)
    if meta["slug"] == "404":
        title, description = (
            "Page not found | Grand Cayman Shore Excursion",
            "The requested Grand Cayman Shore Excursion page was not found.",
        )

    schema_json = None
    if meta.get("schema") == "faq":
        schema_json = json.dumps(faq_schema_from_content(content), ensure_ascii=False, indent=2)
    elif meta.get("keep_schema"):
        raw = extract_existing_schema(ROOT / filename)
        if raw:
            schema_json = rewrite_schema_urls(raw, canon_url(meta["slug"]))

    main_class = meta.get("main_class", "")
    main_attr = f' class="{main_class}"' if main_class else ""
    body = f"""<body class="bg-white text-gray-800 antialiased" data-page="{meta["page"]}" data-static="1">
  <div id="site-nav" data-inlined="true">{nav}</div>
  <div id="page-hero" data-inlined="true">{hero}</div>
  <div id="page-trust-strip" data-inlined="true">{trust}</div>
  <main id="page-content"{main_attr}>{content}</main>
  <div id="site-footer" data-inlined="true">{footer}</div>
  <script src="/js/site.js" defer></script>
</body>
</html>
"""
    return build_head(meta, title, description, schema_json) + body


def bake_schedule_pages() -> None:
    """Inline nav/footer into ship-schedule pages; keep schedule body + search JS."""
    nav = extensionlessify_html(read("partials/nav.html"))
    footer = extensionlessify_html(read("partials/footer.html"))
    for path in (ROOT / "ship-schedule").rglob("index.html"):
        text = path.read_text(encoding="utf-8")
        m_body = re.search(r'<main id="page-content">(.*?)</main>', text, re.S)
        if not m_body:
            continue
        body_html = m_body.group(1)
        title_m = re.search(r"<title[^>]*>(.*?)</title>", text, re.S | re.I)
        desc_m = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', text, re.I
        )
        canon_m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', text, re.I)
        title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else "Ship schedule"
        description = desc_m.group(1) if desc_m else ""
        canon = canon_m.group(1) if canon_m else f"{DOMAIN}/ship-schedule"
        if ".html" in canon:
            canon = canon.replace(".html", "")
        if not canon.startswith(DOMAIN):
            canon = DOMAIN + (canon if canon.startswith("/") else "/" + canon)
        if canon.endswith("/") and canon != f"{DOMAIN}/":
            canon = canon.rstrip("/")
        html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="{canon}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="/js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="/css/site.css" />
</head>
<body class="bg-white text-gray-800 antialiased" data-page="schedule" data-static="1">
  <div id="site-nav" data-inlined="true">{nav}</div>
  <main id="page-content">{body_html}</main>
  <div id="site-footer" data-inlined="true">{footer}</div>
  <script src="/js/site.js" defer></script>
  <script src="/js/schedule-search.js" defer></script>
</body>
</html>
"""
        html = extensionlessify_html(html)
        path.write_text(html, encoding="utf-8")
        print(f"  baked {path.relative_to(ROOT)}")


def write_sitemap() -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for _, meta in PAGES.items():
        if meta.get("noindex") or meta["slug"] == "404":
            continue
        slug = meta["slug"]
        pri = PRIORITY.get(slug, 0.6)
        loc = canon_url(slug)
        freq = "weekly" if pri >= 0.9 else "monthly"
        if slug in ("about", "contact", "methodology", "privacy", "terms"):
            freq = "yearly"
            pri = 0.5 if slug in ("about", "contact", "methodology") else 0.3
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri:.1f}</priority>",
            "  </url>",
        ]

    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    schedule_paths: list[str] = []
    if frag.exists():
        try:
            for path, _pri, _freq in json.loads(frag.read_text(encoding="utf-8")):
                schedule_paths.append(path)
        except json.JSONDecodeError:
            pass
    if not schedule_paths:
        schedule_paths = ["ship-schedule"]
        for p in sorted((ROOT / "ship-schedule").rglob("index.html")):
            rel = p.relative_to(ROOT).as_posix().replace("/index.html", "").replace("index.html", "")
            schedule_paths.append(rel)

    seen = set()
    for path in schedule_paths:
        path = path.strip("/")
        if not path:
            continue
        if path in seen:
            continue
        seen.add(path)
        pri = 0.8 if path == "ship-schedule" else 0.6
        lines += [
            "  <url>",
            f"    <loc>{DOMAIN}/{path}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{'weekly' if path == 'ship-schedule' else 'monthly'}</changefreq>",
            f"    <priority>{pri:.1f}</priority>",
            "  </url>",
        ]

    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("  wrote sitemap.xml")


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n",
        encoding="utf-8",
    )
    print("  wrote robots.txt")


def patch_image_refs_in_sources() -> None:
    """Replace RED horseback asset; soften uncertain alts; drop unused catamaran."""
    replacements = {
        "images/horseback-riding-hero.png": "images/seven-mile-beach-hero.png",
        "Three riders on horses trotting along a sandy beach beside turquoise ocean on a Grand Cayman horseback riding shore excursion":
            "Aerial view of Seven Mile Beach Grand Cayman coastline — context for land-based shore excursions including horseback rides",
        "Angler holding a large tuna on the deck of a sport fishing charter boat in blue ocean off Grand Cayman":
            "Angler holding a large tuna on the deck of a sport fishing charter boat in open ocean",
        "View through glass-bottom boat windows of tropical fish and reef seabed in clear turquoise Grand Cayman water on a cruise shore excursion":
            "View through glass-bottom boat windows of tropical fish and reef seabed in clear turquoise water",
    }
    for folder in ("partials", "content"):
        for path in (ROOT / folder).rglob("*.html"):
            text = path.read_text(encoding="utf-8")
            orig = text
            for old, new in replacements.items():
                text = text.replace(old, new)
            if text != orig:
                path.write_text(text, encoding="utf-8")
                print(f"  patched images/alts in {path.relative_to(ROOT)}")


def remove_bad_images() -> None:
    for name in ("horseback-riding-hero.png", "catamaran-tour.jpg"):
        p = ROOT / "images" / name
        if p.exists():
            p.unlink()
            print(f"  removed images/{name}")


def update_attribution() -> None:
    attr = ROOT / "images" / "ATTRIBUTION.md"
    attr.write_text(
        """# Image attribution

Grand Cayman Shore Excursion uses **local project image assets** under `images/`.
Do not scrape OTA or supplier galleries.

## Active assets (referenced by the build)

| File | Provenance notes |
|------|------------------|
| `hero-grand-cayman.png` | Local — Stingray City / sandbar scene |
| `best-grand-cayman-excursions.png` | Local — underwater stingray scene |
| `grand-cayman-cruise-port.png` | Local — George Town waterfront / tenders |
| `one-day-grand-cayman.png` | Local — George Town street / harbour |
| `stingray-city-hero.png` | Local — sandbar guests with stingrays |
| `seven-mile-beach-hero.png` | Local — aerial west-coast beach (same binary as `grand-cayman-intro.png`) |
| `grand-cayman-intro.png` | Local — aerial island / reef coastline |
| `grand-cayman-snorkelling.png` | Local — reef snorkellers aerial |
| `starfish-point-hero.png` | Local — starfish in shallow water |
| `grand-cayman-private-tours.png` | Local — private boat / shallow water (generic marine; alt softened) |
| `crystal-caves-hero.png` | Local — cave interior |
| `glass-bottom-boat-hero.png` | Local — glass-bottom reef view (generic marine; alt softened) |
| `grand-cayman-family.png` | Local — family sandbar scene |
| `fishing-charter-hero.png` | Local — sport-fishing catch (generic offshore; alt softened) |

## Phase 32B hygiene

- Removed `horseback-riding-hero.png` (wrong-geography RED). Horseback page uses Seven Mile Beach aerial as coastal context.
- Removed unused `catamaran-tour.jpg`.
- No AggregateRating, fabricated prices, or OTA scrapes.
""",
        encoding="utf-8",
    )
    print("  wrote images/ATTRIBUTION.md")


def main() -> None:
    print("Assembling Grand Cayman server-visible pages…")
    ensure_nav_mobile()
    ensure_utility_heroes()
    ensure_404_content()
    patch_image_refs_in_sources()
    remove_bad_images()

    for filename, meta in PAGES.items():
        out = ROOT / filename
        html = assemble_page(filename, meta)
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {filename}")

    bake_schedule_pages()
    write_sitemap()
    write_robots()
    update_attribution()
    print("Done.")


if __name__ == "__main__":
    main()
