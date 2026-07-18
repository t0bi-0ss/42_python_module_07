"""Holds FlameFactory class"""

from .abstract_factory import CreatureFactory
from families import Flameling, Pyrodon


class FlameFactory(CreatureFactory):
    """Flame type creature factory"""

    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()
