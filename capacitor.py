"""Test new scenario"""

from ex1 import TransformCreatureFactory, HealingCreatureFactory

# Create healing Creature factory
healing_factory = HealingCreatureFactory()


def healing_factory_test(factory: HealingCreatureFactory) -> None:
    """Runs test"""

    # Create base creature
    base_form = factory.create_base()
    print("Testing Creature with healing capability")

    print(f"\n Go!\n{base_form._name}!!!\n")

    print(base_form.describe())
    print(base_form.attack())
    print(base_form.heal())

    # Create evolved creature
    evolved_form = factory.create_evolved()

    print(f"\nWhat?\n{base_form._name} is evolving!")
    print(
        f"\nCongratulations!\nYour {base_form._name} "
        f"evolved into {evolved_form._name}\n"
    )

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

    print(f"\n Go!\n{base_form._name}!!!\n")

    print(base_form.describe())
    print(base_form.attack())
    print(base_form.transform())
    print(base_form.attack())
    print(base_form.revert())

    # Create evolved creature
    evolved_form = factory.create_evolved()

    print(f"\nWhat?\n{base_form._name} is evolving!")
    print(
        f"\nCongratulations!\nYour {base_form._name} "
        f"evolved into {evolved_form._name}\n"
    )

    print(evolved_form.describe())
    print(evolved_form.attack())
    print(evolved_form.transform())
    print(evolved_form.attack())
    print(evolved_form.revert())


transforming_factory_test(transforming_factory)
