from typing import overload
from enum import IntEnum
import typing

import Internal
import System


class Console(System.Object):
    """This class has no documentation."""

    class Error(System.Object):
        """This class has no documentation."""

        @staticmethod
        def write(s: str) -> None:
            ...

        @staticmethod
        def write_line() -> None:
            ...

    @staticmethod
    def write(s: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(s: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line() -> None:
        ...


