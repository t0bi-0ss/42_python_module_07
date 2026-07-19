from ex2 import NormalStrategy, AggressiveStrategy, \
    DefensiveStrategy, BattleStrategy, InvalidCombination

from ex0 import FlameFactory, AquaFactory, CreatureFactory

from ex1 import HealingCreatureFactory, TransformCreatureFactory

# Create creature factories
flame_factory = FlameFactory()
aqua_factory = AquaFactory()
healing_factory = HealingCreatureFactory()
transforming_factory = TransformCreatureFactory()

# Create strategies
normal_strategy = NormalStrategy()
aggressive_strategy = AggressiveStrategy()
defensive_strategy = DefensiveStrategy()


# Single battle function
def singe_battle(
        opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i, opponent in enumerate(opponents):
        since = i + 1
        for enemy in opponents[since:]:
            print("\n* Battle *")
            # Create creatures
            creature_1 = opponent[0].create_base()
            creature_2 = enemy[0].create_base()
            print(creature_1.describe())
            print(" vs.")
            print(creature_2.describe())
            print(" now fight!")
            try:
                first_act = opponent[1].act(creature_1)
                second_act = enemy[1].act(creature_2)
            except InvalidCombination as msg:
                print("Battle error, aborting tournament:", msg)
            else:
                print(first_act)
                print(second_act)


print("\t\t\t\t>>>>>>>>>>>>>>>> Tournament 0 (basic) <<<<<<<<<<<<<<<<")
print("\t\t\t\t\t[ (Flameling+Normal), (Healing+Defensive) ]\n")

singe_battle(
    [(flame_factory, normal_strategy), (healing_factory, defensive_strategy)]
)

print("\n\t\t\t\t>>>>>>>>>>>>>>>> Tournament 1 (error) <<<<<<<<<<<<<<<<")
print("\t\t\t\t\t[ (Flameling+Aggressive), (Healing+Defensive) ]\n")

singe_battle(
    [
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy)
    ]
)

print("\n\t\t\t\t>>>>>>>>>>>>>>>> Tournament 2 (multiple) <<<<<<<<<<<<<<<<")
print(
    "\t\t\t\t\t[ (Aquabub+Normal), (Healing+Defensive) "
    ", (Transform+Aggressive)]\n"
)

singe_battle(
    [
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transforming_factory, aggressive_strategy)
    ]
)
