"""Holds all classes for the 'Sproutling' creature family"""

from .abstract_creature import Creature

from .capabilities.heal import HealCapability


class Sproutling(Creature, HealCapability):
    """Class for Sproutling creature"""

    def __init__(self) -> None:
        Creature.__init__(self)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Class for Bloomelle creature"""

    def __init__(self) -> None:
        Creature.__init__(self)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and other for a large amount"
