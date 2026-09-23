"""The alchemy package: elements, potions and transmutation.

Only part of the laboratory is exposed through this interface:
``create_air`` is reachable with ``import alchemy`` while
``create_earth`` is not (see ft_alembic_4.py).
"""

from . import transmutation
from .elements import create_air
from .potions import healing_potion as heal
from .potions import strength_potion

__all__ = ["create_air", "heal", "strength_potion", "transmutation"]
