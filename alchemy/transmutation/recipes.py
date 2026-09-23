"""Transmutation recipes mixing absolute and relative imports."""

from alchemy.elements import create_air  # absolute import
from elements import create_fire  # absolute import

from ..potions import strength_potion  # relative import


def lead_to_gold() -> str:
    """Transmute lead into gold with air, a potion and fire."""
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
