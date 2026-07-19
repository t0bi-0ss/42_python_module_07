"""Holds abstract class for every type of Factory"""

from abc import ABC, abstractmethod
from ex0.factory.families.abstract_creature import Creature


class CreatureFactory(ABC):
    """Abstract class for every type of Factory"""

    @abstractmethod
    def create_base(self) -> Creature:
        """Creates creature base form"""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Creates creature evolved form"""
        pass
