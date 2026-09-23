#!/usr/bin/env python3
"""Kaboom 1: the dark spellbook explodes on import."""

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

spell = dark_spell_record("Doom", "bats, frogs, arsenic")
print(f"Testing record dark spell: {spell}")
