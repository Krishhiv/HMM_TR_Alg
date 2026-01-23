from typing import overload
from enum import IntEnum
import typing

import System.Runtime.InteropServices.Swift

System_Runtime_InteropServices_Swift_SwiftSelf_T = typing.TypeVar("System_Runtime_InteropServices_Swift_SwiftSelf_T")


class SwiftSelf(typing.Generic[System_Runtime_InteropServices_Swift_SwiftSelf_T]):
    """This class has no documentation."""

    @property
    def value(self) -> typing.Any:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: System_Runtime_InteropServices_Swift_SwiftSelf_T) -> None:
        ...


class SwiftError:
    """This class has no documentation."""

    @property
    def value(self) -> typing.Any:
        ...

    def __init__(self, value: typing.Any) -> None:
        ...


class SwiftIndirectResult:
    """This class has no documentation."""

    @property
    def value(self) -> typing.Any:
        ...

    def __init__(self, value: typing.Any) -> None:
        ...


