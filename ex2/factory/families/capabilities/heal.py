"""Holds HealCapability abstract class"""

from abc import ABC, abstractmethod

from typing import Protocol


class Creature(Protocol):
    """Protocol class for any creature"""
    _name: str
    _type: str


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass
