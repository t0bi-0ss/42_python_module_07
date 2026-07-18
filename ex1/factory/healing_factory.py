"""Holds HealingCreatureFactory class"""

from .abstract_factory import CreatureFactory

from .families import sproutling


class HealingCreatureFactory(CreatureFactory):
    """HealingCreatureFactory class"""

    def create_base(self) -> sproutling.Sproutling:
        return sproutling.Sproutling

    def create_evolved(self) -> sproutling.Bloomelle:
        return sproutling.Bloomelle
