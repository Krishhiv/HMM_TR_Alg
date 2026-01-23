from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable

System_Collections_Immutable_ImmutableHashSet_Enumerator = typing.Any
System_Collections_Immutable_ImmutableArray = typing.Any
System_Collections_Immutable_ImmutableList_Enumerator = typing.Any
System_Collections_Immutable_ImmutableSortedSet_Enumerator = typing.Any

System_Collections_Immutable_ImmutableHashSet_T = typing.TypeVar("System_Collections_Immutable_ImmutableHashSet_T")
System_Collections_Immutable_IImmutableList_T = typing.TypeVar("System_Collections_Immutable_IImmutableList_T")
System_Collections_Immutable_ImmutableArray_T = typing.TypeVar("System_Collections_Immutable_ImmutableArray_T")
System_Collections_Immutable_ImmutableDictionary_TValue = typing.TypeVar("System_Collections_Immutable_ImmutableDictionary_TValue")
System_Collections_Immutable_ImmutableDictionary_TKey = typing.TypeVar("System_Collections_Immutable_ImmutableDictionary_TKey")
System_Collections_Immutable_ImmutableList_T = typing.TypeVar("System_Collections_Immutable_ImmutableList_T")
System_Collections_Immutable_ImmutableStack_T = typing.TypeVar("System_Collections_Immutable_ImmutableStack_T")
System_Collections_Immutable_ImmutableSortedSet_T = typing.TypeVar("System_Collections_Immutable_ImmutableSortedSet_T")
System_Collections_Immutable_ImmutableSortedDictionary_TValue = typing.TypeVar("System_Collections_Immutable_ImmutableSortedDictionary_TValue")
System_Collections_Immutable_ImmutableSortedDictionary_TKey = typing.TypeVar("System_Collections_Immutable_ImmutableSortedDictionary_TKey")
System_Collections_Immutable_IImmutableQueue_T = typing.TypeVar("System_Collections_Immutable_IImmutableQueue_T")
System_Collections_Immutable_ImmutableQueue_T = typing.TypeVar("System_Collections_Immutable_ImmutableQueue_T")
System_Collections_Immutable_IImmutableDictionary_TKey = typing.TypeVar("System_Collections_Immutable_IImmutableDictionary_TKey")
System_Collections_Immutable_IImmutableDictionary_TValue = typing.TypeVar("System_Collections_Immutable_IImmutableDictionary_TValue")
System_Collections_Immutable_IImmutableStack_T = typing.TypeVar("System_Collections_Immutable_IImmutableStack_T")
System_Collections_Immutable_IImmutableSet_T = typing.TypeVar("System_Collections_Immutable_IImmutableSet_T")


class ImmutableHashSet(typing.Generic[System_Collections_Immutable_ImmutableHashSet_T], System.Object, System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.ICollection, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableHashSet_T, System_Collections_Immutable_ImmutableHashSet_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableHashSet_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableHashSet_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableHashSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    class Builder(System.Object, System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableHashSet_T], typing.Iterable[System_Collections_Immutable_ImmutableHashSet_T]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]:
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableHashSet_T]:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            ...

        def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableHashSet.Enumerator:
            ...

        def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

        def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def remove(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            ...

        def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            ...

        def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
            ...

        def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableHashSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableHashSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableHashSet_T]:
            ...

        def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

    EMPTY: System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T] = ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def add(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def contains(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableHashSet.Enumerator:
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def remove(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableHashSet.Builder:
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableHashSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableHashSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def with_comparer(self, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        ...


class IImmutableList(typing.Generic[System_Collections_Immutable_IImmutableList_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_IImmutableList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add(self, value: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def index_of(self, item: System_Collections_Immutable_IImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> int:
        ...

    def insert(self, index: int, element: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def last_index_of(self, item: System_Collections_Immutable_IImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> int:
        ...

    def remove(self, value: System_Collections_Immutable_IImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_IImmutableList_T], bool]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    @overload
    def remove_range(self, index: int, count: int) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def replace(self, old_value: System_Collections_Immutable_IImmutableList_T, new_value: System_Collections_Immutable_IImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...

    def set_item(self, index: int, value: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        ...


class ImmutableArray(typing.Generic[System_Collections_Immutable_ImmutableArray_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], System.IEquatable[System_Collections_Immutable_ImmutableArray], System.Collections.Immutable.IImmutableArray, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableArray_T], System.Collections.IList, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, System.Collections.Immutable.IImmutableList[System_Collections_Immutable_ImmutableArray_T], typing.Iterable[System_Collections_Immutable_ImmutableArray_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableArray_T:
            ...

        def move_next(self) -> bool:
            ...

    class Builder(System.Object, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableArray_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableArray_T], typing.Iterable[System_Collections_Immutable_ImmutableArray_T]):
        """This class has no documentation."""

        @property
        def capacity(self) -> int:
            ...

        @capacity.setter
        def capacity(self, value: int) -> None:
            ...

        @property
        def count(self) -> int:
            ...

        @count.setter
        def count(self, value: int) -> None:
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableArray_T:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableArray_T]:
            ...

        def __setitem__(self, index: int, value: System_Collections_Immutable_ImmutableArray_T) -> None:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableArray_T) -> None:
            ...

        @overload
        def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def add_range(self, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> None:
            ...

        @overload
        def add_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], length: int) -> None:
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], length: int) -> None:
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray.Builder) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableArray_T) -> bool:
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableArray_T], index: int) -> None:
            ...

        @overload
        def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def copy_to(self, source_index: int, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int, length: int) -> None:
            ...

        @overload
        def copy_to(self, destination: System.Span[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        def drain_to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableArray_T]:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            ...

        def insert(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> None:
            ...

        @overload
        def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def insert_range(self, index: int, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        def item_ref(self, index: int) -> typing.Any:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            ...

        def move_to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            ...

        @overload
        def remove(self, element: System_Collections_Immutable_ImmutableArray_T) -> bool:
            ...

        @overload
        def remove(self, element: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> bool:
            ...

        def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableArray_T], bool]) -> None:
            ...

        def remove_at(self, index: int) -> None:
            ...

        @overload
        def remove_range(self, index: int, length: int) -> None:
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T) -> None:
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        def reverse(self) -> None:
            ...

        @overload
        def sort(self) -> None:
            ...

        @overload
        def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableArray_T, System_Collections_Immutable_ImmutableArray_T], int]) -> None:
            ...

        @overload
        def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        @overload
        def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            ...

        def to_array(self) -> typing.List[System_Collections_Immutable_ImmutableArray_T]:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            ...

    EMPTY: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T] = ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def is_default(self) -> bool:
        ...

    @property
    def is_default_or_empty(self) -> bool:
        ...

    @overload
    def __eq__(self, right: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        ...

    @overload
    def __eq__(self, right: typing.Optional[System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableArray_T:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def __ne__(self, right: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        ...

    @overload
    def __ne__(self, right: typing.Optional[System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]]) -> bool:
        ...

    def add(self, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def add_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def add_range(self, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def as_memory(self) -> System.ReadOnlyMemory[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def as_span(self, range: System.Range) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def as_span(self) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def as_span(self, start: int, length: int) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def contains(self, item: System_Collections_Immutable_ImmutableArray_T) -> bool:
        ...

    @overload
    def contains(self, item: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int) -> None:
        ...

    @overload
    def copy_to(self, source_index: int, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int, length: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Collections_Immutable_ImmutableArray_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableArray.Enumerator:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def insert_range(self, index: int, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def insert_range(self, index: int, items: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def insert_range(self, index: int, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def item_ref(self, index: int) -> typing.Any:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        ...

    @overload
    def remove(self, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove(self, item: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableArray_T], bool]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, index: int, length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T] = None) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def remove_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T] = None) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def set_item(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def slice(self, start: int, length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def sort(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableArray_T, System_Collections_Immutable_ImmutableArray_T], int]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableArray.Builder:
        ...


class ImmutableDictionary(typing.Generic[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Object, System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Immutable.IImmutableDictionaryInternal[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
    """This class has no documentation."""

    class Builder(System.Object, System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
        """This class has no documentation."""

        @property
        def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]:
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]) -> None:
            ...

        @property
        def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]:
            ...

        @value_comparer.setter
        def value_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]) -> None:
            ...

        @property
        def count(self) -> int:
            ...

        @property
        def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TKey]:
            ...

        @property
        def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TValue]:
            ...

        def __contains__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            ...

        def __getitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            ...

        def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> None:
            ...

        @overload
        def add(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> None:
            ...

        @overload
        def add(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> None:
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
            ...

        def contains_key(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            ...

        def contains_value(self, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> bool:
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableDictionary.Enumerator:
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, default_value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            ...

        @overload
        def remove(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            ...

        @overload
        def remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
            ...

        def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableDictionary_TKey]) -> None:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
            ...

        def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TKey]:
            ...

        def try_get_value(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TValue]:
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    EMPTY: System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue] = ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]:
        ...

    @property
    def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    @property
    def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TKey]:
        ...

    @property
    def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def add_range(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
        ...

    def contains_key(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableDictionary.Enumerator:
        ...

    def remove(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableDictionary_TKey]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def set_item(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableDictionary.Builder:
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TKey]:
        ...

    def try_get_value(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey], value_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        ...


class ImmutableList(typing.Generic[System_Collections_Immutable_ImmutableList_T], System.Object, System.Collections.Immutable.IImmutableList[System_Collections_Immutable_ImmutableList_T], System.Collections.Generic.IList[System_Collections_Immutable_ImmutableList_T], System.Collections.IList, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableList_T]):
    """This class has no documentation."""

    class Builder(System.Object, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableList_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableList_T], typing.Iterable[System_Collections_Immutable_ImmutableList_T]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableList_T:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableList_T]:
            ...

        def __setitem__(self, index: int, value: System_Collections_Immutable_ImmutableList_T) -> None:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableList_T) -> None:
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def binary_search(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            ...

        @overload
        def binary_search(self, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            ...

        @overload
        def binary_search(self, index: int, count: int, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableList_T) -> bool:
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int) -> None:
            ...

        @overload
        def copy_to(self, index: int, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int, count: int) -> None:
            ...

        def exists(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
            ...

        def find(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
            ...

        def find_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            ...

        @overload
        def find_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        @overload
        def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        @overload
        def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        def find_last(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
            ...

        @overload
        def find_last_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        @overload
        def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        @overload
        def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        def for_each(self, action: typing.Callable[[System_Collections_Immutable_ImmutableList_T], typing.Any]) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableList.Enumerator:
            ...

        def get_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int) -> int:
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            ...

        def insert(self, index: int, item: System_Collections_Immutable_ImmutableList_T) -> None:
            ...

        def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        def item_ref(self, index: int) -> typing.Any:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int, count: int) -> int:
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            ...

        @overload
        def remove(self, item: System_Collections_Immutable_ImmutableList_T) -> bool:
            ...

        @overload
        def remove(self, item: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> bool:
            ...

        def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            ...

        def remove_at(self, index: int) -> None:
            ...

        @overload
        def remove_range(self, index: int, count: int) -> None:
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T) -> None:
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def reverse(self) -> None:
            ...

        @overload
        def reverse(self, index: int, count: int) -> None:
            ...

        @overload
        def sort(self) -> None:
            ...

        @overload
        def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_T], int]) -> None:
            ...

        @overload
        def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        @overload
        def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            ...

        def true_for_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableList_T], System.Collections.Immutable.ISecurePooledObjectUser, System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableList_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableList_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    EMPTY: System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T] = ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableList_T:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableList_T]:
        ...

    def add(self, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def binary_search(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
        ...

    @overload
    def binary_search(self, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        ...

    @overload
    def binary_search(self, index: int, count: int, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def contains(self, value: System_Collections_Immutable_ImmutableList_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int) -> None:
        ...

    @overload
    def copy_to(self, index: int, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int, count: int) -> None:
        ...

    def exists(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
        ...

    def find(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
        ...

    def find_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def find_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    def find_last(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
        ...

    @overload
    def find_last_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        ...

    def for_each(self, action: typing.Callable[[System_Collections_Immutable_ImmutableList_T], typing.Any]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableList.Enumerator:
        ...

    def get_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        ...

    @overload
    def index_of(self, value: System_Collections_Immutable_ImmutableList_T) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def item_ref(self, index: int) -> typing.Any:
        ...

    def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        ...

    @overload
    def remove(self, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def remove(self, value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def remove_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def reverse(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def reverse(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def set_item(self, index: int, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def sort(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_T], int]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableList.Builder:
        ...

    def true_for_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
        ...


class ImmutableStack(typing.Generic[System_Collections_Immutable_ImmutableStack_T], System.Object, System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_ImmutableStack_T], typing.Iterable[System_Collections_Immutable_ImmutableStack_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableStack_T:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]

    @property
    def is_empty(self) -> bool:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableStack_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableStack.Enumerator:
        ...

    def peek(self) -> System_Collections_Immutable_ImmutableStack_T:
        ...

    def peek_ref(self) -> typing.Any:
        ...

    @overload
    def pop(self) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        ...

    @overload
    def pop(self, value: typing.Optional[System_Collections_Immutable_ImmutableStack_T]) -> typing.Tuple[System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T], System_Collections_Immutable_ImmutableStack_T]:
        ...

    def push(self, value: System_Collections_Immutable_ImmutableStack_T) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        ...


class ImmutableSortedSet(typing.Generic[System_Collections_Immutable_ImmutableSortedSet_T], System.Object, System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.IList[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.IList, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableSortedSet_T, System_Collections_Immutable_ImmutableSortedSet_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableSortedSet_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Immutable.ISecurePooledObjectUser, System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableSortedSet_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    class Builder(System.Object, System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.ICollection, typing.Iterable[System_Collections_Immutable_ImmutableSortedSet_T]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def max(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            ...

        @property
        def min(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableSortedSet_T:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            ...

        def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedSet.Enumerator:
            ...

        def index_of(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> int:
            ...

        def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

        def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def item_ref(self, index: int) -> typing.Any:
            ...

        def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def remove(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            ...

        def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            ...

        def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableSortedSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableSortedSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

    EMPTY: System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T] = ...

    @property
    def max(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
        ...

    @property
    def min(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableSortedSet_T:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def add(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def contains(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedSet.Enumerator:
        ...

    def index_of(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> int:
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def item_ref(self, index: int) -> typing.Any:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def remove(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableSortedSet.Builder:
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableSortedSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableSortedSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def with_comparer(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...


class ImmutableSortedDictionary(typing.Generic[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Object, System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]], System.Collections.Immutable.ISecurePooledObjectUser):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    class Builder(System.Object, System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]):
        """This class has no documentation."""

        @property
        def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            ...

        @property
        def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            ...

        @property
        def count(self) -> int:
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> None:
            ...

        @property
        def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            ...

        @value_comparer.setter
        def value_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> None:
            ...

        def __contains__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            ...

        def __getitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            ...

        def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> None:
            ...

        @overload
        def add(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> None:
            ...

        @overload
        def add(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> None:
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
            ...

        def contains_key(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            ...

        def contains_value(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> bool:
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Enumerator:
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, default_value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            ...

        @overload
        def remove(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            ...

        @overload
        def remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
            ...

        def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> None:
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            ...

        def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            ...

        def try_get_value(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            ...

        def value_ref(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> typing.Any:
            ...

    EMPTY: System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue] = ...

    @property
    def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        ...

    @property
    def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        ...

    def __contains__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
        ...

    def contains_key(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Enumerator:
        ...

    def remove(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def set_item(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Builder:
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        ...

    def try_get_value(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    def value_ref(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> typing.Any:
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey], value_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        ...


class ImmutableInterlocked(System.Object):
    """This class has no documentation."""


class IImmutableQueue(typing.Generic[System_Collections_Immutable_IImmutableQueue_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableQueue_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_empty(self) -> bool:
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        ...

    def dequeue(self) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        ...

    def enqueue(self, value: System_Collections_Immutable_IImmutableQueue_T) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        ...

    def peek(self) -> System_Collections_Immutable_IImmutableQueue_T:
        ...


class ImmutableQueue(typing.Generic[System_Collections_Immutable_ImmutableQueue_T], System.Object, System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_ImmutableQueue_T], typing.Iterable[System_Collections_Immutable_ImmutableQueue_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableQueue_T:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def is_empty(self) -> bool:
        ...

    EMPTY: System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableQueue_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        ...

    @overload
    def dequeue(self) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        ...

    @overload
    def dequeue(self, value: typing.Optional[System_Collections_Immutable_ImmutableQueue_T]) -> typing.Tuple[System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T], System_Collections_Immutable_ImmutableQueue_T]:
        ...

    def enqueue(self, value: System_Collections_Immutable_ImmutableQueue_T) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableQueue.Enumerator:
        ...

    def peek(self) -> System_Collections_Immutable_ImmutableQueue_T:
        ...

    def peek_ref(self) -> typing.Any:
        ...


class IImmutableDictionary(typing.Generic[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add(self, key: System_Collections_Immutable_IImmutableDictionary_TKey, value: System_Collections_Immutable_IImmutableDictionary_TValue) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def add_range(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]) -> bool:
        ...

    def remove(self, key: System_Collections_Immutable_IImmutableDictionary_TKey) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableDictionary_TKey]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def set_item(self, key: System_Collections_Immutable_IImmutableDictionary_TKey, value: System_Collections_Immutable_IImmutableDictionary_TValue) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_IImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_IImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_IImmutableDictionary_TKey]:
        ...


class IImmutableStack(typing.Generic[System_Collections_Immutable_IImmutableStack_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableStack_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_empty(self) -> bool:
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        ...

    def peek(self) -> System_Collections_Immutable_IImmutableStack_T:
        ...

    def pop(self) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        ...

    def push(self, value: System_Collections_Immutable_IImmutableStack_T) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        ...


class IImmutableSet(typing.Generic[System_Collections_Immutable_IImmutableSet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_IImmutableSet_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add(self, value: System_Collections_Immutable_IImmutableSet_T) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def contains(self, value: System_Collections_Immutable_IImmutableSet_T) -> bool:
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def remove(self, value: System_Collections_Immutable_IImmutableSet_T) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_IImmutableSet_T, actual_value: typing.Optional[System_Collections_Immutable_IImmutableSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_IImmutableSet_T]:
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        ...


