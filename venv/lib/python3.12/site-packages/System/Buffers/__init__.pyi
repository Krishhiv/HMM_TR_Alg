from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Buffers
import System.Runtime.InteropServices

System_Buffers_StandardFormat = typing.Any

System_Buffers_ArrayPool_T = typing.TypeVar("System_Buffers_ArrayPool_T")
System_Buffers_MemoryManager_T = typing.TypeVar("System_Buffers_MemoryManager_T")
System_Buffers_IMemoryOwner_T = typing.TypeVar("System_Buffers_IMemoryOwner_T")
System_Buffers_SearchValues_T = typing.TypeVar("System_Buffers_SearchValues_T")


class StandardFormat(System.IEquatable[System_Buffers_StandardFormat]):
    """This class has no documentation."""

    NO_PRECISION: int = ...

    MAX_PRECISION: int = 99

    @property
    def symbol(self) -> str:
        ...

    @property
    def precision(self) -> int:
        ...

    @property
    def has_precision(self) -> bool:
        ...

    @property
    def is_default(self) -> bool:
        ...

    def __eq__(self, right: System.Buffers.StandardFormat) -> bool:
        ...

    def __init__(self, symbol: str, precision: int = ...) -> None:
        ...

    def __ne__(self, right: System.Buffers.StandardFormat) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Buffers.StandardFormat) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(format: System.ReadOnlySpan[str]) -> System.Buffers.StandardFormat:
        ...

    @staticmethod
    @overload
    def parse(format: str) -> System.Buffers.StandardFormat:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def try_parse(format: System.ReadOnlySpan[str], result: typing.Optional[System.Buffers.StandardFormat]) -> typing.Tuple[bool, System.Buffers.StandardFormat]:
        ...


class OperationStatus(IntEnum):
    """This class has no documentation."""

    DONE = 0

    DESTINATION_TOO_SMALL = 1

    NEED_MORE_DATA = 2

    INVALID_DATA = 3


class ArrayPool(typing.Generic[System_Buffers_ArrayPool_T], System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    SHARED: System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]

    @staticmethod
    @overload
    def create() -> System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]:
        ...

    @staticmethod
    @overload
    def create(max_array_length: int, max_arrays_per_bucket: int) -> System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]:
        ...

    def rent(self, minimum_length: int) -> typing.List[System_Buffers_ArrayPool_T]:
        ...

    def Return(self, array: typing.List[System_Buffers_ArrayPool_T], clearArray: bool = False) -> None:
        ...


class MemoryHandle(System.IDisposable):
    """This class has no documentation."""

    @property
    def pointer(self) -> typing.Any:
        ...

    def __init__(self, pointer: typing.Any, handle: System.Runtime.InteropServices.GCHandle = ..., pinnable: System.Buffers.IPinnable = ...) -> None:
        ...

    def dispose(self) -> None:
        ...


class IPinnable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def pin(self, element_index: int) -> System.Buffers.MemoryHandle:
        ...

    def unpin(self) -> None:
        ...


class MemoryManager(typing.Generic[System_Buffers_MemoryManager_T], System.Object, System.Buffers.IMemoryOwner[System_Buffers_MemoryManager_T], System.Buffers.IPinnable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def memory(self) -> System.Memory[System_Buffers_MemoryManager_T]:
        ...

    @overload
    def create_memory(self, length: int) -> System.Memory[System_Buffers_MemoryManager_T]:
        ...

    @overload
    def create_memory(self, start: int, length: int) -> System.Memory[System_Buffers_MemoryManager_T]:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def get_span(self) -> System.Span[System_Buffers_MemoryManager_T]:
        ...

    def pin(self, element_index: int = 0) -> System.Buffers.MemoryHandle:
        ...

    def unpin(self) -> None:
        ...


class IMemoryOwner(typing.Generic[System_Buffers_IMemoryOwner_T], System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def memory(self) -> System.Memory[System_Buffers_IMemoryOwner_T]:
        ...


class SearchValues(typing.Generic[System_Buffers_SearchValues_T], System.Object):
    """This class has no documentation."""

    def contains(self, value: System_Buffers_SearchValues_T) -> bool:
        ...

    @staticmethod
    @overload
    def create(*values: typing.Union[int, typing.Iterable[int]]) -> System.Buffers.SearchValues[int]:
        ...

    @staticmethod
    @overload
    def create(*values: typing.Union[str, typing.Iterable[str]]) -> System.Buffers.SearchValues[str]:
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> System.Buffers.SearchValues[str]:
        ...


