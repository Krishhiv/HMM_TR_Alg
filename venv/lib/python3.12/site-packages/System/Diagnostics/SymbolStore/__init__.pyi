from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Diagnostics.SymbolStore


class ISymbolDocumentWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def set_check_sum(self, algorithm_id: System.Guid, check_sum: typing.List[int]) -> None:
        ...

    def set_source(self, source: typing.List[int]) -> None:
        ...


