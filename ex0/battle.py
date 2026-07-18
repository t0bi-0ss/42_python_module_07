from factory import AquaFactory, FlameFactory, CreatureFactory


"""Test ex0 package"""

# Instatiate factories
flame_factory = FlameFactory()
aqua_factory = AquaFactory()


def factory_test(factory: CreatureFactory) -> None:
    """Verifies if factory can create base and evolved Creature"""

    print("Testing factory")
    base_form = factory.create_base()
    evolved_form = factory.create_evolved()

    print(base_form.describe())
    print(base_form.attack())
    print(evolved_form.describe())
    print(evolved_form.attack())


factory_test(flame_factory)
print()
factory_test(aqua_factory)

print()


def battle_test(
        factory_1: CreatureFactory,
        factory_2: CreatureFactory
) -> None:
    """Battle test between creatures created by two different factories"""

    print("Testing battle")
    creature_1 = factory_1.create_base()
    creature_2 = factory_2.create_base()

    print(creature_1.describe())
    print(" vs.")
    print(creature_2.describe())
    print(" fight!")
    print(creature_1.attack())
    print(creature_2.attack())


battle_test(flame_factory, aqua_factory)
