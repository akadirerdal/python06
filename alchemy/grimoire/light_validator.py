"""Validator for light magic ingredients.

light_spellbook imports this module at load time, so importing the
spellbook back at module level would create a circular import. The
cycle is broken with a deferred import inside the function.
"""


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID.

    Ingredients are valid when they contain at least one of the
    ingredients allowed by the light spellbook (case insensitive).
    """
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    is_valid = any(ingredient in lowered for ingredient in allowed)
    verdict = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {verdict}"
