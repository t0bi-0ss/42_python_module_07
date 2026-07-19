"""Holds BattleStrategy abstract class"""

from abc import ABC, abstractmethod

from typing import Protocol


class InvalidCombination(Exception):
    """Dedicated exception for act() method in
    case of an invalid combination"""


class Creature(Protocol):
    """Protocol class for every type of creature"""

    def attack(self) -> str:
        ...

    def describe(self) -> str:
        ...


class BattleStrategy(ABC):
    """BattleStrategy abstract class"""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass
