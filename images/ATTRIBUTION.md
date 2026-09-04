# Image attribution

Grand Cayman Shore Excursion uses **local project image assets** already present under `images/`.
Do not scrape OTA or supplier galleries. The `npm run images` script only verifies that
active files exist; it does not download replacements.

## Active assets (referenced by the build)

| File | Provenance notes |
|------|------------------|
| `hero-grand-cayman.png` | Local project asset — Stingray City / sandbar scene |
| `best-grand-cayman-excursions.png` | Local project asset — underwater stingray scene |
| `grand-cayman-cruise-port.png` | Local project asset — George Town waterfront / tenders |
| `one-day-grand-cayman.png` | Local project asset — George Town street / harbour |
| `stingray-city-hero.png` | Local project asset — sandbar guests with stingrays |
| `seven-mile-beach-hero.png` | Local project asset — aerial west-coast beach (same binary as `grand-cayman-intro.png`; intentional within-site reuse) |
| `grand-cayman-intro.png` | Local project asset — aerial island / reef coastline |
| `grand-cayman-snorkelling.png` | Local project asset — reef snorkellers aerial |
| `starfish-point-hero.png` | Local project asset — starfish in shallow water |
| `grand-cayman-private-tours.png` | Local project asset — private boat / shallow water |
| `crystal-caves-hero.png` | Local project asset — cave interior |
| `glass-bottom-boat-hero.png` | Local project asset — glass-bottom reef view |
| `grand-cayman-family.png` | Local project asset — family sandbar scene |
| `horseback-riding-hero.png` | Local project asset — beach horseback ride |
| `fishing-charter-hero.png` | Local project asset — sport-fishing catch on deck |
| `catamaran-tour.jpg` | Local project asset — catamaran in turquoise water |

## Integrity audit (2026-09-04)

- **Cross-site contamination:** SHA-256 hashes of Cayman images were compared with Aruba, St Maarten and Cozumel `images/`. **No matches.** Cayman assets appear unique to this site.
- **Within-site duplicate binaries (kept intentionally or cleaned):**
  - `seven-mile-beach-hero.png` ≡ `grand-cayman-intro.png` (intentional reuse for intro/beach aerial)
  - Unused `.jpg` siblings that duplicated other stems or mismatched PNG heroes were removed to reduce confusion (`crystal-caves-hero.jpg`, `fishing-charter-hero.jpg`, `grand-cayman-cruise-port.jpg`, `grand-cayman-family.jpg`, `grand-cayman-private-tours.jpg`, `horseback-riding-hero.jpg`, `one-day-grand-cayman.jpg`, `starfish-point-hero.jpg`). Active pages use the `.png` heroes (plus `catamaran-tour.jpg`).

## Policy

- Prefer unique Cayman assets over copying other destinations.
- No AggregateRating, fabricated prices, or OTA scrapes.
- Re-run `npm run images` after adding or renaming active files.
