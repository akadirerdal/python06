"""The dark validator: the import that closes the fatal loop."""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID.

    Ingredients are valid when they contain at least one of the
    ingredients allowed by the dark spellbook (case insensitive).
    """
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()
    is_valid = any(ingredient in lowered for ingredient in allowed)
    verdict = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {verdict}"
