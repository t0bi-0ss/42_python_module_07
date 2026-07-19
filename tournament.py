from ex2 import NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, BattleStrategy

from ex0 import FlameFactory, AquaFactory, CreatureFactory

# Create creature factories
flame_factory = FlameFactory()
aqua_factory = AquaFactory()

# Create strategies
normal_strategy = NormalStrategy()
aggressive_strategy = AggressiveStrategy()
defensive_strategy = DefensiveStrategy()


# Single battle function
def singe_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")

    print("* Battle *")
    for i, opponent in enumerate(opponents):
        since = i + 1
        for enemy in opponents[since:]:
            print(opponent[0].create_base().describe())
            print(" vs.")
            print(enemy[0].create_base().describe())


singe_battle([(flame_factory, normal_strategy), (aqua_factory, normal_strategy)])
