"""Holds NormalStrategy battle strategy class"""

from .battle_strategy import BattleStrategy, Creature, InvalidCombination


class NormalStrategy(BattleStrategy):
    """NormalStrategy battle strategy class"""

    def is_valid(self, creature: Creature) -> bool:
        try:
            creature.attack()
        except AttributeError:
            return False
        else:
            return True

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                creature._name,
                NormalStrategy.__name__.removesuffix("Strategy")
            )
        else:
            return creature.attack()
