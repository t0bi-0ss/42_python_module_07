"""Holds TransformCapability abstract class"""

from abc import ABC, abstractmethod


class TransformCapability(ABC):
    """Transform capability abstract class"""

    def __init__(self) -> None:
        self._is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
