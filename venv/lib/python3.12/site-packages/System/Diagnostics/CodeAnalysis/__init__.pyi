from typing import overload
from enum import IntEnum
import System
import System.Diagnostics.CodeAnalysis


class ConstantExpectedAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def min(self) -> System.Object:
        ...

    @min.setter
    def min(self, value: System.Object) -> None:
        ...

    @property
    def max(self) -> System.Object:
        ...

    @max.setter
    def max(self, value: System.Object) -> None:
        ...


class ExcludeFromCodeCoverageAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def justification(self) -> str:
        ...

    @justification.setter
    def justification(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...


class SuppressMessageAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def category(self) -> str:
        ...

    @property
    def check_id(self) -> str:
        ...

    @property
    def scope(self) -> str:
        ...

    @scope.setter
    def scope(self, value: str) -> None:
        ...

    @property
    def target(self) -> str:
        ...

    @target.setter
    def target(self, value: str) -> None:
        ...

    @property
    def message_id(self) -> str:
        ...

    @message_id.setter
    def message_id(self, value: str) -> None:
        ...

    @property
    def justification(self) -> str:
        ...

    @justification.setter
    def justification(self, value: str) -> None:
        ...

    def __init__(self, category: str, check_id: str) -> None:
        ...


class UnscopedRefAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


