"""Holds DefensiveStrategy battle strategy class"""

from ex1.capable_factory.capable_families import Sproutling, \
    Bloomelle

from .battle_strategy import InvalidCombination, BattleStrategy


class DefensiveStrategy(BattleStrategy[Sproutling | Bloomelle]):
    """DefensiveStrategy battle strategy class"""

    def is_valid(
        self,
        creature: Sproutling | Bloomelle
    ) -> bool:
        try:
            creature.heal()
        except AttributeError:
            return False
        else:
            return True

    def act(
        self,
        creature: Sproutling | Bloomelle
    ) -> str:
        if not self.is_valid(creature):
            raise InvalidCombination(
                creature._name,
                DefensiveStrategy.__name__.removesuffix("Strategy")
            )
        else:
            return f"{creature.attack()}\n{creature.heal()}"
