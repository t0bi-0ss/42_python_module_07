"""Holds all classes for the 'flameling' family"""

from .abstract_creature import Creature


class Flameling(Creature):

    def attack(self) -> str:
        return f"{self._name} uses Ember"


class Pyrodon(Creature):

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower"
