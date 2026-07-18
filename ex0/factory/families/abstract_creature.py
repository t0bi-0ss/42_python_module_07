"""Holds abstract class for every type of creature"""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract class for every type of creature"""

    def __init__(self, name: str, type: str) -> None:
        self._name = name
        self._type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self._name} is {self._type} type Creature"
