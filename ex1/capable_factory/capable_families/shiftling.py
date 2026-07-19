"""Holds all classes for the 'Shiftling' creature family"""

from ex0.factory.families.abstract_creature import Creature

from .capabilities.transform import TransformCapability


class Shiftling(Creature, TransformCapability):
    """Shiftling Transformable Creature class"""

    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self._name: str = "Shiftling"
        self._type: str = "Normal"

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self._name} returns to normal"

    def attack(self) -> str:
        if not self._is_transformed:
            return f"{self._name} attacks normally"
        else:
            return f"{self._name} performs a boosted strike"


class Morphagon(Creature, TransformCapability):
    """Morphagon Transformable Creature class"""

    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self._name = "Morphagon"
        self._type = "Normal/Dragon"

    def transform(self) -> str:
        self._is_transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._is_transformed = False
        return f"{self._name} stabilizes its form"

    def attack(self) -> str:
        if self._is_transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        else:
            return f"{self._name} attacks normally"
