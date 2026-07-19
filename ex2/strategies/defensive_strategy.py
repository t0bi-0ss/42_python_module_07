"""Holds DefensiveStrategy battle strategy class"""

from .battle_strategy import Creature, InvalidCombination, BattleStrategy

# from typing import Protocol


# class HealingCreature(Creature, Protocol):

#     def heal(self) -> str:
#         ...


class DefensiveStrategy(BattleStrategy):
    """DefensiveStrategy battle strategy class"""

    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.heal()
        except AttributeError:
            return False
        else:
            return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                creature._name,
                DefensiveStrategy.__name__.removesuffix("Strategy")
            )
        else:
            return f"{creature.attack()}\n{creature.heal()}"
