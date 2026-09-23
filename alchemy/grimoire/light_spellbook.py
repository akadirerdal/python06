"""The light spellbook: safe magic, no circular import."""

from .light_validator import validate_ingredients

LIGHT_ALLOWED_INGREDIENTS: list[str] = ["earth", "air", "fire", "water"]


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed for light magic."""
    return list(LIGHT_ALLOWED_INGREDIENTS)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell, or reject it if ingredients are invalid."""
    validation = validate_ingredients(ingredients)
    if validation.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
