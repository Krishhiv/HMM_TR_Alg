from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.Collections.Frozen
import System.Collections.Generic
import System.Collections.Immutable

System_Collections_Frozen_FrozenSet_T = typing.TypeVar("System_Collections_Frozen_FrozenSet_T")
System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate = typing.TypeVar("System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate")
System_Collections_Frozen_FrozenDictionary_TKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TKey")
System_Collections_Frozen_FrozenDictionary_TValue = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TValue")
System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey")


class FrozenSet(typing.Generic[System_Collections_Frozen_FrozenSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Frozen_FrozenSet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Frozen_FrozenSet_T], System.Collections.ICollection, typing.Iterable[System_Collections_Frozen_FrozenSet_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Frozen_FrozenSet_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Frozen_FrozenSet_T:
            ...

        def move_next(self) -> bool:
            ...

    class AlternateLookup(typing.Generic[System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate]):
        """This class has no documentation."""

        @property
        def set(self) -> System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_T]:
            ...

        def contains(self, item: System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate) -> bool:
            ...

        def try_get_value(self, equal_value: System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate, actual_value: typing.Optional[System_Collections_Frozen_FrozenSet_T]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenSet_T]:
            ...

    EMPTY: System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_T]

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenSet_T]:
        ...

    @property
    def items(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenSet_T]:
        ...

    @property
    def count(self) -> int:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Frozen_FrozenSet_T]:
        ...

    def contains(self, item: System_Collections_Frozen_FrozenSet_T) -> bool:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Frozen_FrozenSet_T], destination_index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Collections_Frozen_FrozenSet_T]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Frozen.FrozenSet.Enumerator:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def try_get_value(self, equal_value: System_Collections_Frozen_FrozenSet_T, actual_value: typing.Optional[System_Collections_Frozen_FrozenSet_T]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenSet_T]:
        ...


class FrozenDictionary(typing.Generic[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey]):
        """This class has no documentation."""

        @property
        def dictionary(self) -> System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]:
            ...

        def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey) -> System_Collections_Frozen_FrozenDictionary_TValue:
            ...

        def contains_key(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey) -> bool:
            ...

        def try_get_value(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Frozen_FrozenDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenDictionary_TValue]:
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_TKey]:
        ...

    @property
    def keys(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TKey]:
        ...

    @property
    def values(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TValue]:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        ...

    @overload
    def copy_to(self, destination: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], destination_index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Frozen.FrozenDictionary.Enumerator:
        ...

    def get_value_ref_or_null_ref(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        ...

    def try_get_value(self, key: System_Collections_Frozen_FrozenDictionary_TKey, value: typing.Optional[System_Collections_Frozen_FrozenDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenDictionary_TValue]:
        ...


