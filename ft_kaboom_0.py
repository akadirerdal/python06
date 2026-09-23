#!/usr/bin/env python3
"""Kaboom 0: record a light spell through the grimoire module."""

from alchemy import grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")

spell = grimoire.light_spellbook.light_spell_record(
    "Fantasy", "Earth, wind and fire"
)
print(f"Testing record light spell: {spell}")
