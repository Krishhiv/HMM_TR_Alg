from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections.Generic
import System.Linq

System_Linq_IGrouping_TKey = typing.TypeVar("System_Linq_IGrouping_TKey")
System_Linq_IGrouping_TElement = typing.TypeVar("System_Linq_IGrouping_TElement")
System_Linq_IOrderedEnumerable_TElement = typing.TypeVar("System_Linq_IOrderedEnumerable_TElement")
System_Linq_Lookup_TKey = typing.TypeVar("System_Linq_Lookup_TKey")
System_Linq_Lookup_TElement = typing.TypeVar("System_Linq_Lookup_TElement")
System_Linq_ILookup_TKey = typing.TypeVar("System_Linq_ILookup_TKey")
System_Linq_ILookup_TElement = typing.TypeVar("System_Linq_ILookup_TElement")


class ImmutableArrayExtensions(System.Object):
    """This class has no documentation."""


class Enumerable(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def average(source: System.Collections.Generic.IEnumerable[int]) -> float:
        ...

    @staticmethod
    @overload
    def average(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def average(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def average(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def max(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def max(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def max(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def max(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def min(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def min(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def min(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def min(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    def range(start: int, count: int) -> System.Collections.Generic.IEnumerable[int]:
        ...

    @staticmethod
    @overload
    def sum(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def sum(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def sum(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def sum(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...


class IGrouping(typing.Generic[System_Linq_IGrouping_TKey, System_Linq_IGrouping_TElement], System.Collections.Generic.IEnumerable[System_Linq_IGrouping_TElement], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def key(self) -> System_Linq_IGrouping_TKey:
        ...


class IOrderedEnumerable(typing.Generic[System_Linq_IOrderedEnumerable_TElement], System.Collections.Generic.IEnumerable[System_Linq_IOrderedEnumerable_TElement], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class Lookup(typing.Generic[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement], System.Object, System.Linq.ILookup[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement], typing.Iterable[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    def __getitem__(self, key: System_Linq_Lookup_TKey) -> System.Collections.Generic.IEnumerable[System_Linq_Lookup_TElement]:
        ...

    def __iter__(self) -> typing.Iterator[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]:
        ...

    def contains(self, key: System_Linq_Lookup_TKey) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]:
        ...


class ILookup(typing.Generic[System_Linq_ILookup_TKey, System_Linq_ILookup_TElement], System.Collections.Generic.IEnumerable[System.Linq.IGrouping[System_Linq_ILookup_TKey, System_Linq_ILookup_TElement]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...

    def __getitem__(self, key: System_Linq_ILookup_TKey) -> System.Collections.Generic.IEnumerable[System_Linq_ILookup_TElement]:
        ...

    def contains(self, key: System_Linq_ILookup_TKey) -> bool:
        ...


