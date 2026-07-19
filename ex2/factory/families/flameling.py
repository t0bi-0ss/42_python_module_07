"""Holds all classes for the 'flameling' family"""

from .abstract_creature import Creature


class Flameling(Creature):

    def __init__(self) -> None:
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return f"{self._name} uses Ember"


class Pyrodon(Creature):

    def __init__(self) -> None:
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower"
