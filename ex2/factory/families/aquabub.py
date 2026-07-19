"""Holds all classes for the 'Aquabub' family"""

from .abstract_creature import Creature


class Aquabub(Creature):

    def __init__(self) -> None:
        self._name = "Aquabub"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):

    def __init__(self) -> None:
        self._name = "Torragon"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"
