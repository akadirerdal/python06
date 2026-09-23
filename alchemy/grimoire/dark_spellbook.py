from .dark_validator import validate_dark_ingredients

DARK_ALLOWED_INGREDIENTS: list[str] = ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_allowed_ingredients() -> list[str]:
    return list(DARK_ALLOWED_INGREDIENTS)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_dark_ingredients(ingredients)
    if validation.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
