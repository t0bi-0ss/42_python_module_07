"""Holds AquaFactory class"""

from .abstract_factory import CreatureFactory
from families import Aquabub, Torragon


class AquaFactory(CreatureFactory):
    """Aqua type creature factory"""

    def create_base(self) -> Aquabub:
        return Aquabub()

    def create_evolved(self) -> Torragon:
        return Torragon()
