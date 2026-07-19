"""Holds BattleStrategy abstract class"""

from abc import ABC, abstractmethod

from typing import Protocol


class InvalidCombination(Exception):
    """Dedicated exception for act() method in
    case of an invalid combination"""

    def __init__(self, creature_name: str, strategy_name: str) -> None:
        super().__init__(creature_name)
        self.creature_name = creature_name
        self.strategy_name = strategy_name

    def __str__(self) -> str:
        return f"Invalid Creature '{self.creature_name}' " \
            f"for this {self.strategy_name} strategy"


class Creature(Protocol):
    """Protocol class for every type of creature"""

    _name: str
    _type: str

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
