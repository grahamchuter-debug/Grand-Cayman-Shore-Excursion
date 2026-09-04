#!/usr/bin/env python3
"""World 2.0 content extensions for Grand Cayman Shore Excursion.

Runs after build-grand-cayman-site.py. Rewrites homepage decision architecture,
decision pages, legal pages, nav/footer, softens unsupported claims, and
merges schedule sitemap fragments. Does not modify Cozumel, Aruba, or St Maarten.
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://grandcaymanshoreexcursion.com"
SITE = "Grand Cayman Shore Excursion"
DATE = "2026-09-04"

_spec = importlib.util.spec_from_file_location(
    "build_cayman", ROOT / "scripts" / "build-grand-cayman-site.py"
)
_build = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_build)

page_shell = _build.page_shell
cruise_snapshot = _build.cruise_snapshot
_hero_inner = _build._hero_inner
write = _build.write
HOME_HERO = _build.HOME_HERO
HOME_HERO_ALT = _build.HOME_HERO_ALT
STINGRAY_IMG = _build.STINGRAY_IMG
STINGRAY_ALT = _build.STINGRAY_ALT
SEVEN_MILE_IMG = _build.SEVEN_MILE_IMG
SEVEN_MILE_ALT = _build.SEVEN_MILE_ALT
SNORKEL_IMG = _build.SNORKEL_IMG
SNORKEL_ALT = _build.SNORKEL_ALT
STARFISH_IMG = _build.STARFISH_IMG
STARFISH_ALT = _build.STARFISH_ALT
PORT_IMG = _build.PORT_IMG
PORT_ALT = _build.PORT_ALT
INTRO_IMG = _build.INTRO_IMG
INTRO_ALT = _build.INTRO_ALT
ONE_DAY_IMG = _build.ONE_DAY_IMG
ONE_DAY_ALT = _build.ONE_DAY_ALT
CRYSTAL_IMG = _build.CRYSTAL_IMG
CRYSTAL_ALT = _build.CRYSTAL_ALT
ACCENT = "text-teal-300"
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(7, 89, 133, 0.78) 0%, "
    "rgba(13, 148, 136, 0.55) 55%, rgba(0, 0, 0, 0.4) 100%)"
)
_hero_wave = _build._hero_wave


def soft_claims_in_text(html: str) -> str:
    replacements = [
        (
            r"Operators usually allow 60[–-]90 min buffer",
            "Build your own buffer; confirm operator return plan",
        ),
        (
            r"Ship tours guarantee the vessel waits if the operator is late\. Reputable Grand Cayman operators plan returns with buffer — confirm policies and read reviews\.",
            "Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.",
        ),
        (
            r"Ship tours guarantee wait-if-late; reputable locals plan buffer returns\.",
            "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer.",
        ),
        (
            r"with return buffer",
            "with a sensible return window",
        ),
        (
            r"Allow margin before published all-aboard\.",
            "Build your own buffer before published all-aboard — confirm times with your ship and operator.",
        ),
        (
            r"plan returns with buffer before all aboard",
            "plan returns with enough time before all aboard — confirm with the operator",
        ),
        (
            r"and a fixed return time to the pier",
            "and a timed return window to the pier — confirm details with the operator",
        ),
        (
            r"understand all-aboard deadlines",
            "usually plan around all-aboard — still confirm return timing in writing",
        ),
        (
            r"southern stingrays glide around guests",
            "guests may encounter southern stingrays — sightings vary",
        ),
        (
            r"Touch stingrays in waist-deep turquoise water",
            "Chance to meet stingrays in shallow turquoise water",
        ),
    ]
    out = html
    for pat, repl in replacements:
        out = re.sub(pat, repl, out)
    return out


def soft_all_content() -> None:
    content_dir = ROOT / "content"
    for path in content_dir.glob("*.html"):
        original = path.read_text(encoding="utf-8")
        updated = soft_claims_in_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"  softened claims in content/{path.name}")


def internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Grand Cayman guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your George Town port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="grand-cayman-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-grand-cayman-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="stingray-city-vs-seven-mile-beach.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Stingray vs Beach</a>
    <span class="text-gray-300">·</span>
    <a href="grand-cayman-tender-day-planning.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Tender Planning</a>
    <span class="text-gray-300">·</span>
    <a href="ship-schedule/" class="text-ocean-600 hover:text-ocean-800 font-medium">Ship Schedule</a>
    <span class="text-gray-300">·</span>
    <a href="grand-cayman-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def concierge_panel() -> str:
    return """<section class="py-14 bg-white" id="concierge" aria-labelledby="concierge-heading">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="concierge-panel">
      <h2 id="concierge-heading" class="font-display font-bold text-2xl sm:text-3xl mb-3">Need help shaping your Grand Cayman day?</h2>
      <p class="text-white/90 text-sm sm:text-base leading-relaxed mb-4">
        Tell us your ship, call date, and whether you lean Stingray City, Seven Mile Beach, reef snorkelling, or a quieter Starfish Point stop.
        We are an independent planning resource — not the cruise line and not a ticket marketplace.
      </p>
      <p class="text-white/80 text-sm leading-relaxed mb-5">
        Email <a href="mailto:hello@grandcaymanshoreexcursion.com">hello@grandcaymanshoreexcursion.com</a> with your ship, date and preferences.
        We do not promise instant replies or 24/7 staffing.
      </p>
      <div class="flex flex-col sm:flex-row gap-3">
        <a href="mailto:hello@grandcaymanshoreexcursion.com" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Email the Cayman concierge</a>
        <a href="best-grand-cayman-shore-excursions.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Compare excursion types</a>
      </div>
    </div>
  </div>
</section>"""


def snapshot(**overrides: str) -> str:
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


def write_nav() -> None:
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
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600 transition-colors">Ship Schedule</a>
        <a href="grand-cayman-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="contact.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Contact concierge
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sky-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )


def write_footer() -> None:
    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors calling at George Town, Grand Cayman. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-grand-cayman-shore-excursions.html" class="hover:text-white transition-colors">All Excursions</a></li>
            <li><a href="stingray-city-excursions.html" class="hover:text-white transition-colors">Stingray City</a></li>
            <li><a href="seven-mile-beach-excursions.html" class="hover:text-white transition-colors">Seven Mile Beach</a></li>
            <li><a href="grand-cayman-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="starfish-point-excursions.html" class="hover:text-white transition-colors">Starfish Point</a></li>
            <li><a href="crystal-caves-tours.html" class="hover:text-white transition-colors">Crystal Caves</a></li>
            <li><a href="stingray-city-vs-seven-mile-beach.html" class="hover:text-white transition-colors">Stingray vs Beach</a></li>
            <li><a href="grand-cayman-tender-day-planning.html" class="hover:text-white transition-colors">Tender Day Planning</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="grand-cayman-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="ship-schedule/" class="hover:text-white transition-colors">Ship Schedule</a></li>
            <li><a href="one-day-in-grand-cayman.html" class="hover:text-white transition-colors">One Day in Grand Cayman</a></li>
            <li><a href="grand-cayman-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="grand-cayman-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
            <li><a href="methodology.html" class="hover:text-white transition-colors">Methodology</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Legal</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="about.html" class="hover:text-white transition-colors">About</a></li>
            <li><a href="contact.html" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="privacy.html" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="terms.html" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Confirm times with your cruise line and operators. No fabricated prices or ratings on this site.</p>
      </div>
    </div>
  </footer>
""",
    )


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-teal-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">George Town · Tender-aware Cayman</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Grand Cayman Shore<br/><span class="{ACCENT}">Excursion</span>
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Ashore at George Town, choose your Cayman day: North Sound sandbar time, Seven Mile Beach calm, or a reef snorkel — with tender logistics factored in when your ship lands by boat.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="stingray-city-vs-seven-mile-beach.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Stingray or beach?</a>
          <a href="ship-schedule/" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Find your ship</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Stingray City</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Seven Mile Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Reef Snorkel</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">George Town</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def content_home() -> str:
    snap = snapshot()
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
  <p class="section-label mx-auto">George Town cruise call</p>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Grand Cayman is a decision port</h2>
  <p class="text-gray-600 text-sm sm:text-base leading-relaxed">Ships arrive at George Town — many calls tender ashore, though arrangements vary by vessel and day. Once you are on land, the classic trade-off is Stingray City energy versus Seven Mile Beach calm, with reef snorkelling as a strong third path.</p>
</div></section>
<section class="pb-10 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="decision-grid">
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Stingray City</h3><p>North Sound sandbar time with a chance to see southern stingrays — wildlife and conditions vary.</p><a href="stingray-city-excursions.html" class="text-ocean-600 font-semibold text-sm">Stingray City →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Seven Mile Beach</h3><p>White sand and calm swim west of town when you want lounger pace, not boat queues.</p><a href="seven-mile-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Seven Mile Beach →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Reef snorkel</h3><p>Barrier reef boat trips close to George Town — coral gardens without a full sandbar commitment.</p><a href="grand-cayman-snorkelling-tours.html" class="text-ocean-600 font-semibold text-sm">Snorkelling →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Stingray vs beach</h3><p>Honest trade-offs between the sandbar signature and a Seven Mile lounger day.</p><a href="stingray-city-vs-seven-mile-beach.html" class="text-ocean-600 font-semibold text-sm">Compare →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Tender logistics</h3><p>How to budget queue and boat time when your call lands by tender — without assuming every ship always does.</p><a href="grand-cayman-tender-day-planning.html" class="text-ocean-600 font-semibold text-sm">Tender planning →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Find your ship</h3><p>Search George Town call dates, then leave a sensible return window before all aboard.</p><a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></div>
  </div>
</div></section>
<section class="py-12 bg-sky-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Port orientation</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">George Town is the planning hub</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Whether you walk off a pier or ride a tender into the harbour, downtown George Town is where taxis, tour desks and marina transfers concentrate. Confirm landing arrangements with your cruise line that day — Cayman calls are famous for tendering, but not every ship on every call uses the same pattern.</p>
    <a href="grand-cayman-cruise-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg order-2 lg:order-1">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
  <div class="order-1 lg:order-2">
    <p class="section-label">Two moods, one island</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Sandbar drama or beach calm</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Stingray City is the headline North Sound experience. Seven Mile Beach is the classic west-coast unwind. Reef snorkelling sits between them. On a typical 7–10 hour call, pick one primary plan and protect your return window.</p>
    <a href="stingray-city-vs-seven-mile-beach.html" class="text-ocean-600 font-semibold text-sm">Stingray vs beach →</a>
    <span class="text-gray-300 mx-2">·</span>
    <a href="one-day-in-grand-cayman.html" class="text-ocean-600 font-semibold text-sm">One-day paths →</a>
  </div>
</div></div></section>
<section class="pb-4 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sky-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <p class="section-label mx-auto">Signature stops</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-3">Four Grand Cayman experiences cruise guests compare most</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sky-50 flex flex-col">
      <div class="card-media h-44"><img src="{STINGRAY_IMG}" alt="{STINGRAY_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Stingray City</h3><p class="text-sm text-gray-500 flex-1">North Sound sandbar — chance to see stingrays; conditions vary.</p><a href="stingray-city-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Stingray City →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sky-50 flex flex-col">
      <div class="card-media h-44"><img src="{SEVEN_MILE_IMG}" alt="{SEVEN_MILE_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Seven Mile Beach</h3><p class="text-sm text-gray-500 flex-1">White sand and calm Caribbean water west of George Town.</p><a href="seven-mile-beach-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Seven Mile →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sky-50 flex flex-col">
      <div class="card-media h-44"><img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Reef snorkel</h3><p class="text-sm text-gray-500 flex-1">Barrier reef boat trips with gear and guides from near town.</p><a href="grand-cayman-snorkelling-tours.html" class="mt-5 text-ocean-600 font-semibold text-sm">Snorkelling →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sky-50 flex flex-col">
      <div class="card-media h-44"><img src="{STARFISH_IMG}" alt="{STARFISH_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Starfish Point</h3><p class="text-sm text-gray-500 flex-1">Shallower east-end bay — a gentler alternative to a long sandbar day.</p><a href="starfish-point-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Starfish Point →</a></div>
    </div>
  </div>
  <p class="text-center mt-8"><a href="best-grand-cayman-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Full comparison →</a></p>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Ship planning</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Match the day to your George Town call</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Browse arrivals by month, note your all-aboard window, then choose sandbar, beach or reef. Schedules can change — treat published times as planning aids and build your own buffer.</p>
    <a href="ship-schedule/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm">Find your ship schedule</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{ONE_DAY_IMG}" alt="{ONE_DAY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Still deciding?</h2>
  <p class="text-white/85 text-sm mb-6">Compare Stingray City with Seven Mile Beach, or email the Cayman concierge with your ship and date.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="stingray-city-vs-seven-mile-beach.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Stingray vs beach</a>
    <a href="contact.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Contact concierge</a>
  </div>
</div></section>
{concierge_panel()}"""


def content_port() -> str:
    snap = snapshot(
        activity_level="Low at terminal; moderate on tours",
        popular="Pier or tender landing, taxis, organised pickups",
        best_for="Orienting at George Town before sandbar or beach plans",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">Cruise ships call at <strong>George Town</strong> on Grand Cayman. Many visits involve tendering ashore, but landing arrangements vary by ship, pier capacity and the day — always confirm with your cruise line. Typical calls run <strong>7–10 hours</strong>.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sky-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Where ships arrive</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sky-100"><h3 class="font-display font-bold text-lg mb-2">George Town waterfront</h3><p class="text-gray-600">Downtown shops, taxis and excursion meeting points concentrate near the harbour. Confirm your operator meeting point — multi-ship days get busy.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-sky-100"><h3 class="font-display font-bold text-lg mb-2">Tender logistics</h3><p class="text-gray-600">When your ship tenders, budget queue and boat time both ways. That is especially important before morning Stingray departures. See the tender planning guide for a careful checklist.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sky-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Cayman Islands dollar (KYD); <strong>US dollars</strong> widely accepted at excursions and taxis.</p></div>
    <div class="bg-teal-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English — straightforward for UK and North American cruise guests.</p></div>
    <div class="bg-sky-50 rounded-2xl p-6"><strong class="text-gray-900">Getting around</strong><p class="mt-2 text-gray-600">Licensed taxis at the landing; many Stingray and reef tours include boat transfer from marinas near town.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-grand-cayman.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a>
  <span class="text-gray-300 mx-2">·</span>
  <a href="grand-cayman-tender-day-planning.html" class="text-ocean-600 font-semibold text-sm">Tender planning →</a>
  <span class="text-gray-300 mx-2">·</span>
  <a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_stingray_vs_beach() -> str:
    snap = snapshot(
        best_for="Choosing Stingray City vs Seven Mile Beach",
        activity_level="Stingray low–moderate boat; beach low",
        popular="North Sound sandbar vs west-coast beach day",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">On a typical George Town call, Grand Cayman often comes down to <strong>Stingray City</strong> or a <strong>Seven Mile Beach</strong> day. Both are excellent. They spend your hours differently.</p>
  <p class="text-gray-600 leading-relaxed">Stingray City is a boat-led North Sound experience with a chance to see southern stingrays — not a wildlife guarantee. Seven Mile Beach maximises sand and swimming with simpler land transfers.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sky-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Stingray City vs Seven Mile Beach</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sky-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{STINGRAY_IMG}" alt="{STINGRAY_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Stingray City day</h3>
      <ul class="space-y-2 text-gray-600">
        <li>North Sound sandbar with a chance to encounter southern stingrays</li>
        <li>Wildlife and water conditions vary — no guaranteed sightings</li>
        <li>Often combined with a reef snorkel on the same boat</li>
        <li>More moving parts: marina transfer, boat time, tender queues on tender days</li>
      </ul>
      <p class="mt-4"><a href="stingray-city-excursions.html" class="text-ocean-600 font-semibold">Stingray City →</a> · <a href="grand-cayman-snorkelling-tours.html" class="text-ocean-600 font-semibold">Snorkelling →</a></p>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-sky-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{SEVEN_MILE_IMG}" alt="{SEVEN_MILE_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Seven Mile Beach day</h3>
      <ul class="space-y-2 text-gray-600">
        <li>White sand and calm swim west of George Town</li>
        <li>Public access is common; resort clubs may charge separately for chairs or facilities</li>
        <li>Shorter logistics than a North Sound boat day once you are ashore</li>
        <li>Best when shade, swimming and low intensity matter more than the sandbar</li>
      </ul>
      <p class="mt-4"><a href="seven-mile-beach-excursions.html" class="text-ocean-600 font-semibold">Seven Mile Beach →</a> · <a href="one-day-in-grand-cayman.html" class="text-ocean-600 font-semibold">One-day paths →</a></p>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Mixing both on a long call</h2>
      <p class="text-gray-600 leading-relaxed mb-3">On a longer George Town day, some guests do a morning sandbar combo and a short beach stop later — or the reverse. Two well-paced blocks beat three rushed attractions.</p>
      <p class="text-gray-600 leading-relaxed">Check your ship’s all-aboard time, confirm whether you tender or pier, and build your own buffer. Do not rely on a published “60–90 minutes” promise.</p>
      <p class="mt-4"><a href="grand-cayman-tender-day-planning.html" class="text-ocean-600 font-semibold">Tender planning →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{SNORKEL_IMG}" alt="{SNORKEL_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-4 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_tender_day() -> str:
    snap = snapshot(
        best_for="Planning when your Grand Cayman call may tender",
        activity_level="Low ashore; queue time varies",
        popular="Tender queues, marina transfers, return buffer",
        return_ship="Build your own buffer including tender time",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">Grand Cayman is widely known for <strong>tender operations</strong> into George Town. Many cruise calls land guests by tender boat — but arrangements vary by ship, pier capacity, weather and the day. This page helps you plan carefully <em>without</em> assuming every ship always tenders.</p>
  <p class="text-gray-600 leading-relaxed">Confirm landing method with your cruise line’s daily programme or app. Then budget time for queues, the tender ride, and the reverse journey before all aboard.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sky-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Tender-aware planning checklist</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sky-100">
      <h3 class="font-display font-bold text-lg mb-3">Before you leave the ship</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Confirm whether your call tends, uses a pier, or may switch on the day</li>
        <li>Note tender ticket / group numbers if your line uses them</li>
        <li>Pad morning Stingray or reef departures for queue and boat time</li>
        <li>Photograph meeting points and operator WhatsApp / phone contacts</li>
      </ul>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-sky-100">
      <h3 class="font-display font-bold text-lg mb-3">Coming back</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Leave earlier than a pier-port guest would — tender lines build late afternoon</li>
        <li>Confirm the operator’s last return drop near the tender landing, not only “downtown”</li>
        <li>Build your own buffer; do not treat any website’s minutes as a guarantee</li>
        <li>Keep ID and boarding documents on you while ashore</li>
      </ul>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">How tender time changes the day</h2>
      <p class="text-gray-600 leading-relaxed mb-3">A Stingray City combo that fits a walk-off pier call can feel tight when you also need tender time both ways. Beach transfers still need that same return cushion.</p>
      <p class="text-gray-600 leading-relaxed">If your ship announces a pier berth, you may reclaim that queue time — still confirm before you commit to a late afternoon stop.</p>
      <p class="mt-4"><a href="stingray-city-vs-seven-mile-beach.html" class="text-ocean-600 font-semibold">Stingray vs beach →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{PORT_IMG}" alt="{PORT_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-4 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_about() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">About Grand Cayman Shore Excursion</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Grand Cayman rewards water-first planning. Many cruise operations land guests in George Town by tender rather than a long pier walk, so the clock starts before you even choose Stingray City, Seven Mile Beach or a reef snorkel.</p>
  <p class="text-gray-600 leading-relaxed mb-4">This site helps passengers weigh those choices honestly — including tender variability and the fact that wildlife encounters are never guaranteed. We are not a cruise line, ticket marketplace or port authority.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedules here are synced from the Caribbean Shore Excursions authority import for Grand Cayman only. Confirm final timings with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-8">Network context: <a href="https://caribbeanshoreexcursion.com/" class="text-ocean-600 font-medium">Caribbean Shore Excursions</a>. Cayman detail lives here.</p>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_contact() -> str:
    return f"""<section class="pt-10 pb-8 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Contact</h2>
  <p class="text-gray-600 leading-relaxed mb-4">If you want help narrowing a Grand Cayman port day, include your ship name, call date, whether you expect to tender or pier, and whether you prefer Stingray City, Seven Mile Beach, reef snorkelling or a quieter stop.</p>
  <p class="text-gray-600 leading-relaxed mb-6">Email <a class="text-ocean-600 font-semibold" href="mailto:hello@grandcaymanshoreexcursion.com">hello@grandcaymanshoreexcursion.com</a>. Replies are handled when we can — this is a planning concierge, not a booking desk.</p>
  <ul class="space-y-2 text-sm text-gray-600 mb-8">
    <li><a class="text-ocean-600 font-semibold" href="ship-schedule/">Find your ship schedule</a></li>
    <li><a class="text-ocean-600 font-semibold" href="best-grand-cayman-shore-excursions.html">Compare excursion types</a></li>
    <li><a class="text-ocean-600 font-semibold" href="grand-cayman-cruise-port-guide.html">Read the port guide</a></li>
    <li><a class="text-ocean-600 font-semibold" href="stingray-city-vs-seven-mile-beach.html">Stingray vs beach decision</a></li>
    <li><a class="text-ocean-600 font-semibold" href="grand-cayman-tender-day-planning.html">Tender day planning</a></li>
  </ul>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_privacy() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Privacy</h2>
  <p class="text-gray-600 leading-relaxed mb-4">This is a static planning website. In this phase we do not operate a booking engine, payment system, or passenger account database.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Messages sent to hello@grandcaymanshoreexcursion.com are used only to respond about Grand Cayman port-day planning. We will not sell contact details.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Standard web server and CDN logs may record technical request data (such as IP address, user agent and requested URL) as part of delivering the site securely. We do not add analytics trackers in this build.</p>
  <p class="text-gray-600 leading-relaxed">If our contact or tooling practices change, this page will be updated before those features go live.</p>
</div></section>"""


def content_terms() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Terms of use</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Content on Grand Cayman Shore Excursion is provided for general information and planning. It is not a contract of carriage, not travel insurance, and not a guarantee of excursion availability, wildlife sightings, weather, tender operations or on-time return to your ship.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Cruise schedules, landing arrangements and excursion details can change. Confirm final arrangements with your cruise line and any operator you choose.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are independent of cruise lines and of Grand Cayman’s port operators. Mentions of beaches, sandbars or landmarks are for orientation and do not imply partnership unless we say so explicitly.</p>
  <p class="text-gray-600 leading-relaxed">You are responsible for leaving enough time to reboard, for following local rules, and for checking any medical or activity requirements before water activities.</p>
</div></section>"""


def content_methodology() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">How we assess Grand Cayman excursions</h2>
  <p class="text-gray-600 leading-relaxed mb-4">We judge options the way a cruise passenger has to: against the length of the George Town call, tender or pier logistics, transfer time, and how much return buffer you need before all aboard.</p>
  <div class="space-y-4 text-sm text-gray-600 mb-8">
    <div class="bg-sky-50 rounded-2xl p-5 border border-sky-100"><h3 class="font-display font-bold text-gray-900 mb-2">Cruise timing first</h3><p>A brilliant full-day mash-up is the wrong answer on a short or tender-heavy call. We favour options that leave a realistic return window.</p></div>
    <div class="bg-teal-50 rounded-2xl p-5 border border-teal-100"><h3 class="font-display font-bold text-gray-900 mb-2">Decision clarity</h3><p>Stingray City versus Seven Mile Beach, reef snorkel intensity, tender logistics — passengers need honest trade-offs, not marketplace noise.</p></div>
    <div class="bg-sky-50 rounded-2xl p-5 border border-sky-100"><h3 class="font-display font-bold text-gray-900 mb-2">No invented proof</h3><p>We do not invent star ratings, review counts, “places left” or fabricated prices. Wildlife sightings are never guaranteed. Trust comes from clear planning language and transparent limits.</p></div>
    <div class="bg-teal-50 rounded-2xl p-5 border border-teal-100"><h3 class="font-display font-bold text-gray-900 mb-2">Schedule integrity</h3><p>Call lists are generated from the Caribbean authority import for Grand Cayman, then checked for count and record-level match before pages are built.</p></div>
  </div>
  {internal_links()}
</div></section>
{concierge_panel()}"""


NEW_PAGES = [
    dict(
        file="stingray-city-vs-seven-mile-beach.html",
        title="Stingray City vs Seven Mile Beach | Grand Cayman Cruise Decision",
        description="Compare a Stingray City sandbar day with Seven Mile Beach on a Grand Cayman cruise call from George Town — honest trade-offs for boat time versus beach calm.",
        keywords="Stingray City vs Seven Mile Beach, Grand Cayman cruise decision, George Town shore day",
        path="stingray-city-vs-seven-mile-beach.html",
        data_page="excursions",
        hero="partials/hero-stingray-vs-beach.html",
        content="stingray-city-vs-seven-mile-beach.html",
        preload=STINGRAY_IMG,
    ),
    dict(
        file="grand-cayman-tender-day-planning.html",
        title="Grand Cayman Tender Day Planning | George Town Cruise Logistics",
        description="Plan a Grand Cayman cruise call when tendering may apply — queue time, marina transfers and return buffers without assuming every ship always tenders.",
        keywords="Grand Cayman tender, George Town tender cruise, Grand Cayman port logistics",
        path="grand-cayman-tender-day-planning.html",
        data_page="port",
        hero="partials/hero-tender-day.html",
        content="grand-cayman-tender-day-planning.html",
        preload=PORT_IMG,
    ),
    dict(
        file="about.html",
        title="About Grand Cayman Shore Excursion | Independent Port Planning",
        description="About Grand Cayman Shore Excursion — independent planning guidance for cruise passengers calling at George Town.",
        keywords="about Grand Cayman Shore Excursion, Grand Cayman cruise planning",
        path="about.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="about.html",
        preload=PORT_IMG,
    ),
    dict(
        file="contact.html",
        title="Contact Grand Cayman Shore Excursion | Concierge",
        description="Contact the Grand Cayman shore excursion concierge at hello@grandcaymanshoreexcursion.com for George Town port-day planning help.",
        keywords="contact Grand Cayman Shore Excursion, Grand Cayman cruise concierge",
        path="contact.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="contact.html",
        preload=PORT_IMG,
    ),
    dict(
        file="privacy.html",
        title="Privacy | Grand Cayman Shore Excursion",
        description="Privacy policy for Grand Cayman Shore Excursion — static planning site practices.",
        keywords="privacy Grand Cayman Shore Excursion",
        path="privacy.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="privacy.html",
        preload=PORT_IMG,
    ),
    dict(
        file="terms.html",
        title="Terms of Use | Grand Cayman Shore Excursion",
        description="Terms of use for Grand Cayman Shore Excursion planning content.",
        keywords="terms Grand Cayman Shore Excursion",
        path="terms.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="terms.html",
        preload=PORT_IMG,
    ),
    dict(
        file="methodology.html",
        title="How We Assess Grand Cayman Excursions | Methodology",
        description="How Grand Cayman Shore Excursion assesses cruise excursion options — timing, honest claims and schedule integrity.",
        keywords="Grand Cayman excursion methodology, how we choose Grand Cayman tours",
        path="methodology.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="methodology.html",
        preload=PORT_IMG,
    ),
]


def merge_sitemap(extra: list[tuple[str, str, str]]) -> None:
    sitemap_path = ROOT / "sitemap.xml"
    existing: list[tuple[str, str, str]] = []
    if sitemap_path.exists():
        text = sitemap_path.read_text(encoding="utf-8")
        locs = re.findall(r"<loc>(.*?)</loc>", text)
        freqs = re.findall(r"<changefreq>(.*?)</changefreq>", text)
        pris = re.findall(r"<priority>(.*?)</priority>", text)
        for i, loc in enumerate(locs):
            path = loc.replace(DOMAIN + "/", "").replace(DOMAIN, "")
            if path == "/":
                path = ""
            freq = freqs[i] if i < len(freqs) else "monthly"
            pri = pris[i] if i < len(pris) else "0.5"
            existing.append((path, pri, freq))

    by_path = {p: (pri, freq) for p, pri, freq in existing}
    for path, pri, freq in extra:
        by_path[path] = (pri, freq)

    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    if frag.exists():
        try:
            for path, pri, freq in json.loads(frag.read_text(encoding="utf-8")):
                by_path[path] = (pri, freq)
        except json.JSONDecodeError:
            pass

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, (pri, freq) in sorted(by_path.items(), key=lambda x: (x[0] != "", x[0])):
        url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")


def write_package_json() -> None:
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


def ensure_decision_css() -> None:
    css_path = ROOT / "css" / "site.css"
    css = css_path.read_text(encoding="utf-8")
    if ".decision-grid" not in css:
        css += """
.section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #0d9488;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
}
.decision-grid {
  display: grid;
  gap: 1rem;
}
@media (min-width: 640px) {
  .decision-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .decision-grid { grid-template-columns: repeat(3, 1fr); }
}
.decision-card {
  background: #fff;
  border: 1px solid #e0f2fe;
  border-radius: 1.25rem;
  padding: 1.25rem 1.35rem;
}
.decision-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
}
.decision-card p {
  font-size: 0.875rem;
  color: #4b5563;
  line-height: 1.55;
  margin-bottom: 0.75rem;
}
"""
        css_path.write_text(css, encoding="utf-8")
        print("  updated css/site.css with decision styles")


def main() -> None:
    print("World 2.0 extending Grand Cayman Shore Excursion…")
    ensure_decision_css()
    write_nav()
    write_footer()
    write("partials/hero-home.html", hero_home())
    write(
        "partials/hero-stingray-vs-beach.html",
        _hero_inner(
            "George Town decision",
            f"Stingray City vs<br/><span class=\"{ACCENT}\">Seven Mile Beach</span>",
            "North Sound sandbar time versus west-coast beach calm — choose how to spend a Grand Cayman cruise call.",
            STINGRAY_IMG,
            STINGRAY_ALT,
            breadcrumb="Stingray vs Beach",
        ),
    )
    write(
        "partials/hero-tender-day.html",
        _hero_inner(
            "Landing logistics",
            f"Grand Cayman<br/><span class=\"{ACCENT}\">Tender Day</span> Planning",
            "Many calls tender into George Town — arrangements vary. Budget queue and boat time without assuming every ship always tenders.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Tender Day Planning",
        ),
    )

    write("content/home.html", content_home())
    write("content/grand-cayman-cruise-port-guide.html", content_port())
    write("content/stingray-city-vs-seven-mile-beach.html", content_stingray_vs_beach())
    write("content/grand-cayman-tender-day-planning.html", content_tender_day())
    write("content/about.html", content_about())
    write("content/contact.html", content_contact())
    write("content/privacy.html", content_privacy())
    write("content/terms.html", content_terms())
    write("content/methodology.html", content_methodology())

    soft_all_content()

    for p in NEW_PAGES:
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
            ),
        )

    write(
        "index.html",
        page_shell(
            title=f"{SITE} | George Town — Stingray, Beach &amp; Tender-Aware Days",
            description="Independent Grand Cayman shore excursion planning from George Town — Stingray City, Seven Mile Beach, reef snorkelling and tender-aware cruise logistics.",
            keywords="Grand Cayman shore excursions, George Town cruise port, Stingray City, Seven Mile Beach, Grand Cayman tender",
            canonical_path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Grand Cayman cruise shore excursions from George Town",
            },
        ),
    )

    extra = [
        ("stingray-city-vs-seven-mile-beach.html", "0.8", "monthly"),
        ("grand-cayman-tender-day-planning.html", "0.8", "monthly"),
        ("about.html", "0.5", "yearly"),
        ("contact.html", "0.5", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("methodology.html", "0.5", "yearly"),
    ]
    merge_sitemap(extra)
    write_package_json()
    print("World 2.0 extend done.")


if __name__ == "__main__":
    main()
