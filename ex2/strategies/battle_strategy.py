"""Holds BattleStrategy abstract class"""

from abc import ABC, abstractmethod

from typing import TypeVar, Generic

from ex0.factory.families.abstract_creature import Creature


T = TypeVar('T', bound=Creature)


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


class BattleStrategy(ABC, Generic[T]):
    """BattleStrategy abstract class"""

    @abstractmethod
    def is_valid(
        self,
        creature: T
    ) -> bool:
        pass

    @abstractmethod
    def act(
        self,
        creature: T
    ) -> str:
        pass
