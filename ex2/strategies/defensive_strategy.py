"""Holds DefensiveStrategy battle strategy class"""

from .battle_strategy import Creature, InvalidCombination, BattleStrategy


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
            raise InvalidCombination
        else:
            return f"{creature.attack()}\n{creature.heal()}"
