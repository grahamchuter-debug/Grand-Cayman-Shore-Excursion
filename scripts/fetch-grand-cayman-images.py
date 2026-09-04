#!/usr/bin/env python3
"""Verify Grand Cayman site images are present.

Active assets are local project files documented in images/ATTRIBUTION.md.
This script does not download from OTAs or scrape supplier galleries.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

ACTIVE = [
    "hero-grand-cayman.png",
    "best-grand-cayman-excursions.png",
    "grand-cayman-cruise-port.png",
    "one-day-grand-cayman.png",
    "stingray-city-hero.png",
    "seven-mile-beach-hero.png",
    "grand-cayman-snorkelling.png",
    "starfish-point-hero.png",
    "grand-cayman-private-tours.png",
    "crystal-caves-hero.png",
    "glass-bottom-boat-hero.png",
    "grand-cayman-family.png",
    "horseback-riding-hero.png",
    "fishing-charter-hero.png",
    "catamaran-tour.jpg",
    "grand-cayman-intro.png",
]


def main() -> int:
    print("Checking Grand Cayman active images…")
    missing = []
    for name in ACTIVE:
        path = IMAGES / name
        if path.is_file():
            print(f"  ok  {name} ({path.stat().st_size} bytes)")
        else:
            print(f"  MISSING  {name}")
            missing.append(name)
    if missing:
        print(f"Missing {len(missing)} active image(s). See images/ATTRIBUTION.md.")
        return 1
    print("All active images present. No remote fetch performed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
