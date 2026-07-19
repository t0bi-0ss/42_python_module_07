"""Holds AggressiveStrategy battle strategy class"""

from .battle_strategy import BattleStrategy, InvalidCombination

from ex1.capable_factory.capable_families import Shiftling, Morphagon


class AggressiveStrategy(BattleStrategy[Shiftling | Morphagon]):
    """AggressiveStrategy battle strategy class"""

    def is_valid(
        self,
        creature: Shiftling | Morphagon
    ) -> bool:
        try:
            creature.transform()
            creature.revert()
        except AttributeError:
            return False
        else:
            return True

    def act(
        self,
        creature: Shiftling | Morphagon
    ) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                creature._name,
                AggressiveStrategy.__name__.removesuffix("Strategy")
            )
        else:
            return f"{creature.transform()}\n" \
                f"{creature.attack()}\n{creature.revert()}"
