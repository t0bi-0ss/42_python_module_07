"""Test new scenario"""

from factory import TransformCreatureFactory, HealingCreatureFactory

# Create healing Creature factory
healing_factory = HealingCreatureFactory()


def healing_factory_test(factory: HealingCreatureFactory) -> None:
    """Runs test"""

    # Create base creature
    creature = factory.create_base()
    print("Testing Creature with healing capability")
    print(" base:")
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())

    # Create evolved creature
    creature = factory.create_evolved()
    print(" evolved:")
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


healing_factory_test(healing_factory)

print()

# Create transforming creature factory
transforming_factory = TransformCreatureFactory()


def transforming_factory_test(factory: TransformCreatureFactory) -> None:
    """Runs small test"""

    # Create base creature
    creature = factory.create_base()
    print("Testing Creature with transform capability")
    print(" base:")
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())

    # Create evolved creature
    creature = factory.create_evolved()
    print(" evolved:")
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


transforming_factory_test(transforming_factory)
