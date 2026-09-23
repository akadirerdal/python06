"""Potions brewed from the four fundamental elements."""

from elements import create_fire, create_water

from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion from earth and air."""
    return (
        "Healing potion brewed with "
        f"'{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    """Brew a strength potion from fire and water."""
    return (
        "Strength potion brewed with "
        f"'{create_fire()}' and '{create_water()}'"
    )


def fundamental_elements() -> list[str]:
    """Return the creation of the four fundamental elements."""
    return [create_fire(), create_water(), create_earth(), create_air()]
