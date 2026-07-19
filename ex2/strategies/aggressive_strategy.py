"""Holds AggressiveStrategy battle strategy class"""

from .battle_strategy import BattleStrategy, Creature, InvalidCombination


class AggressiveStrategy(BattleStrategy):
    """AggressiveStrategy battle strategy class"""

    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.transform()
            creature.revert()
        except AttributeError:
            return False
        else:
            return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination
        else:
            return f"{creature.transform()}\n" \
                f"{creature.attack()}\n{creature.revert()}"
