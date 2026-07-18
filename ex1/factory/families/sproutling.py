"""Holds all classes for the 'Spoutling' creature family"""

from .abstract_creature import Creature

from .capabilities.heal import HealCapability


class Sproutling(Creature, HealCapability):
    """Class for Sproutling creature"""

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Class for Bloomelle creature"""

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self._name} heals itself and other for a large amount"
