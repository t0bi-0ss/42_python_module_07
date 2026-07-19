"""Test new scenario"""

from factory import TransformCreatureFactory, HealingCreatureFactory

# Create healing Creature factory
healing_factory = HealingCreatureFactory()


def healing_factory_test(factory: HealingCreatureFactory) -> None:
    """Runs test"""

    # Create base creature
    base_form = factory.create_base()
    print("Testing Creature with healing capability")
    print(" base:")
    print(base_form.describe())
    print(base_form.attack())
    print(base_form.heal())

    # Create evolved creature
    evolved_form = factory.create_evolved()
    print(" evolved:")
    print(evolved_form.describe())
    print(evolved_form.attack())
    print(evolved_form.heal())


healing_factory_test(healing_factory)

print()

# Create transforming creature factory
transforming_factory = TransformCreatureFactory()


def transforming_factory_test(factory: TransformCreatureFactory) -> None:
    """Runs small test"""

    # Create base creature
    base_form = factory.create_base()
    print("Testing Creature with transform capability")
    print(" base:")
    print(base_form.describe())
    print(base_form.attack())
    print(base_form.transform())
    print(base_form.attack())
    print(base_form.revert())

    # Create evolved creature
    evolved_form = factory.create_evolved()
    print(" evolved:")
    print(evolved_form.describe())
    print(evolved_form.attack())
    print(evolved_form.transform())
    print(evolved_form.attack())
    print(evolved_form.revert())


transforming_factory_test(transforming_factory)
