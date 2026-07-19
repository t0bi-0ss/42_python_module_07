"""Holds TransformCreatureFactory class"""

from .abstract_factory import CreatureFactory

from .capable_families import shiftling


class TransformCreatureFactory(CreatureFactory):
    """TransformCreatureFactory class"""

    def create_base(self) -> shiftling.Shiftling:
        return shiftling.Shiftling()

    def create_evolved(self) -> shiftling.Morphagon:
        return shiftling.Morphagon()
