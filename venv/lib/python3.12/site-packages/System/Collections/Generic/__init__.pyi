from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks

System_Collections_Generic_IAsyncEnumerable_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerable_T")
System_Collections_Generic_IReadOnlySet_T = typing.TypeVar("System_Collections_Generic_IReadOnlySet_T")
System_Collections_Generic_IReadOnlyDictionary_TKey = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TKey")
System_Collections_Generic_IReadOnlyDictionary_TValue = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TValue")
System_Collections_Generic_Comparer_T = typing.TypeVar("System_Collections_Generic_Comparer_T")
System_Collections_Generic_GenericComparer_T = typing.TypeVar("System_Collections_Generic_GenericComparer_T")
System_Collections_Generic_NullableComparer_T = typing.TypeVar("System_Collections_Generic_NullableComparer_T")
System_Collections_Generic_ObjectComparer_T = typing.TypeVar("System_Collections_Generic_ObjectComparer_T")
System_Collections_Generic_ICollection_T = typing.TypeVar("System_Collections_Generic_ICollection_T")
System_Collections_Generic_IReadOnlyList_T = typing.TypeVar("System_Collections_Generic_IReadOnlyList_T")
System_Collections_Generic_EqualityComparer_T = typing.TypeVar("System_Collections_Generic_EqualityComparer_T")
System_Collections_Generic_GenericEqualityComparer_T = typing.TypeVar("System_Collections_Generic_GenericEqualityComparer_T")
System_Collections_Generic_NullableEqualityComparer_T = typing.TypeVar("System_Collections_Generic_NullableEqualityComparer_T")
System_Collections_Generic_ObjectEqualityComparer_T = typing.TypeVar("System_Collections_Generic_ObjectEqualityComparer_T")
System_Collections_Generic_EnumEqualityComparer_T = typing.TypeVar("System_Collections_Generic_EnumEqualityComparer_T")
System_Collections_Generic_HashSet_T = typing.TypeVar("System_Collections_Generic_HashSet_T")
System_Collections_Generic_HashSet_AlternateLookup_TAlternate = typing.TypeVar("System_Collections_Generic_HashSet_AlternateLookup_TAlternate")
System_Collections_Generic_Dictionary_TValue = typing.TypeVar("System_Collections_Generic_Dictionary_TValue")
System_Collections_Generic_Dictionary_TKey = typing.TypeVar("System_Collections_Generic_Dictionary_TKey")
System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey = typing.TypeVar("System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey")
System_Collections_Generic_List_T = typing.TypeVar("System_Collections_Generic_List_T")
System_Collections_Generic_IComparer_T = typing.TypeVar("System_Collections_Generic_IComparer_T")
System_Collections_Generic_KeyValuePair_TKey = typing.TypeVar("System_Collections_Generic_KeyValuePair_TKey")
System_Collections_Generic_KeyValuePair_TValue = typing.TypeVar("System_Collections_Generic_KeyValuePair_TValue")
System_Collections_Generic_IList_T = typing.TypeVar("System_Collections_Generic_IList_T")
System_Collections_Generic_IEqualityComparer_T = typing.TypeVar("System_Collections_Generic_IEqualityComparer_T")
System_Collections_Generic_IEnumerable_T = typing.TypeVar("System_Collections_Generic_IEnumerable_T")
System_Collections_Generic_Queue_T = typing.TypeVar("System_Collections_Generic_Queue_T")
System_Collections_Generic_IAsyncEnumerator_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerator_T")
System_Collections_Generic_ISet_T = typing.TypeVar("System_Collections_Generic_ISet_T")
System_Collections_Generic_IEnumerator_T = typing.TypeVar("System_Collections_Generic_IEnumerator_T")
System_Collections_Generic_IReadOnlyCollection_T = typing.TypeVar("System_Collections_Generic_IReadOnlyCollection_T")
System_Collections_Generic_IDictionary_TValue = typing.TypeVar("System_Collections_Generic_IDictionary_TValue")
System_Collections_Generic_IDictionary_TKey = typing.TypeVar("System_Collections_Generic_IDictionary_TKey")
System_Collections_Generic_IAlternateEqualityComparer_TAlternate = typing.TypeVar("System_Collections_Generic_IAlternateEqualityComparer_TAlternate")
System_Collections_Generic_IAlternateEqualityComparer_T = typing.TypeVar("System_Collections_Generic_IAlternateEqualityComparer_T")
System_Collections_Generic_LinkedList_T = typing.TypeVar("System_Collections_Generic_LinkedList_T")
System_Collections_Generic_LinkedListNode_T = typing.TypeVar("System_Collections_Generic_LinkedListNode_T")
System_Collections_Generic_SortedList_TKey = typing.TypeVar("System_Collections_Generic_SortedList_TKey")
System_Collections_Generic_SortedList_TValue = typing.TypeVar("System_Collections_Generic_SortedList_TValue")
System_Collections_Generic_SortedDictionary_TValue = typing.TypeVar("System_Collections_Generic_SortedDictionary_TValue")
System_Collections_Generic_SortedDictionary_TKey = typing.TypeVar("System_Collections_Generic_SortedDictionary_TKey")
System_Collections_Generic_TreeSet_T = typing.TypeVar("System_Collections_Generic_TreeSet_T")
System_Collections_Generic_Stack_T = typing.TypeVar("System_Collections_Generic_Stack_T")
System_Collections_Generic_SortedSet_T = typing.TypeVar("System_Collections_Generic_SortedSet_T")
System_Collections_Generic_PriorityQueue_TElement = typing.TypeVar("System_Collections_Generic_PriorityQueue_TElement")
System_Collections_Generic_PriorityQueue_TPriority = typing.TypeVar("System_Collections_Generic_PriorityQueue_TPriority")


class CollectionExtensions(System.Object):
    """This class has no documentation."""


class IAsyncEnumerable(typing.Generic[System_Collections_Generic_IAsyncEnumerable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_async_enumerator(self, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerator[System_Collections_Generic_IAsyncEnumerable_T]:
        ...


class IReadOnlySet(typing.Generic[System_Collections_Generic_IReadOnlySet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlySet_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __contains__(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def contains(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        ...


class IReadOnlyDictionary(typing.Generic[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def keys(self) -> typing.Iterable[System_Collections_Generic_IReadOnlyDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def values(self) -> typing.Iterable[System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> System_Collections_Generic_IReadOnlyDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey, value: typing.Optional[System_Collections_Generic_IReadOnlyDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...


class Comparer(typing.Generic[System_Collections_Generic_Comparer_T], System.Object, System.Collections.IComparer, System.Collections.Generic.IComparer[System_Collections_Generic_Comparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    DEFAULT: System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]

    def compare(self, x: System_Collections_Generic_Comparer_T, y: System_Collections_Generic_Comparer_T) -> int:
        ...

    @staticmethod
    def create(comparison: typing.Callable[[System_Collections_Generic_Comparer_T, System_Collections_Generic_Comparer_T], int]) -> System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]:
        ...


class GenericComparer(typing.Generic[System_Collections_Generic_GenericComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_GenericComparer_T]):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_GenericComparer_T, y: System_Collections_Generic_GenericComparer_T) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class NullableComparer(typing.Generic[System_Collections_Generic_NullableComparer_T], System.Collections.Generic.Comparer[typing.Optional[System_Collections_Generic_NullableComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def compare(self, x: typing.Optional[System_Collections_Generic_NullableComparer_T], y: typing.Optional[System_Collections_Generic_NullableComparer_T]) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectComparer(typing.Generic[System_Collections_Generic_ObjectComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_ObjectComparer_T]):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_ObjectComparer_T, y: System_Collections_Generic_ObjectComparer_T) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ICollection(typing.Generic[System_Collections_Generic_ICollection_T], System.Collections.Generic.IEnumerable[System_Collections_Generic_ICollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        ...

    def __contains__(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_ICollection_T) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_ICollection_T], array_index: int) -> None:
        ...

    def remove(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...


class IReadOnlyList(typing.Generic[System_Collections_Generic_IReadOnlyList_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlyList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IReadOnlyList_T:
        ...


class EqualityComparer(typing.Generic[System_Collections_Generic_EqualityComparer_T], System.Object, System.Collections.IEqualityComparer, System.Collections.Generic.IEqualityComparer[System_Collections_Generic_EqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    DEFAULT: System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]

    @staticmethod
    def create(equals: typing.Callable[[System_Collections_Generic_EqualityComparer_T, System_Collections_Generic_EqualityComparer_T], bool], get_hash_code: typing.Callable[[System_Collections_Generic_EqualityComparer_T], int] = None) -> System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]:
        ...

    def equals(self, x: System_Collections_Generic_EqualityComparer_T, y: System_Collections_Generic_EqualityComparer_T) -> bool:
        ...

    def get_hash_code(self, obj: System_Collections_Generic_EqualityComparer_T) -> int:
        ...


class GenericEqualityComparer(typing.Generic[System_Collections_Generic_GenericEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_GenericEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_GenericEqualityComparer_T, y: System_Collections_Generic_GenericEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_GenericEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class NullableEqualityComparer(typing.Generic[System_Collections_Generic_NullableEqualityComparer_T], System.Collections.Generic.EqualityComparer[typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T], y: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectEqualityComparer(typing.Generic[System_Collections_Generic_ObjectEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_ObjectEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_ObjectEqualityComparer_T, y: System_Collections_Generic_ObjectEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_ObjectEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class ByteEqualityComparer(System.Collections.Generic.EqualityComparer[int]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: int, y: int) -> bool:
        ...

    @overload
    def get_hash_code(self, b: int) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class EnumEqualityComparer(typing.Generic[System_Collections_Generic_EnumEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_EnumEqualityComparer_T], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_EnumEqualityComparer_T, y: System_Collections_Generic_EnumEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_EnumEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class HashSet(typing.Generic[System_Collections_Generic_HashSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_HashSet_T], System.Collections.Generic.IReadOnlySet[System_Collections_Generic_HashSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_HashSet_T]):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Generic_HashSet_AlternateLookup_TAlternate]):
        """This class has no documentation."""

        @property
        def set(self) -> System.Collections.Generic.HashSet[System_Collections_Generic_HashSet_T]:
            ...

        def __contains__(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            ...

        def __len__(self) -> int:
            ...

        def add(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            ...

        def contains(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            ...

        def remove(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            ...

        def try_get_value(self, equal_value: System_Collections_Generic_HashSet_AlternateLookup_TAlternate, actual_value: typing.Optional[System_Collections_Generic_HashSet_T]) -> typing.Tuple[bool, System_Collections_Generic_HashSet_T]:
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_HashSet_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_HashSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]:
        ...

    def __contains__(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_HashSet_T]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T], array_index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T], array_index: int, count: int) -> None:
        ...

    @staticmethod
    def create_set_comparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.HashSet[System_Collections_Generic_HashSet_T]]:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.HashSet.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def remove(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    def remove_where(self, match: typing.Callable[[System_Collections_Generic_HashSet_T], bool]) -> int:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        ...

    def try_get_value(self, equal_value: System_Collections_Generic_HashSet_T, actual_value: typing.Optional[System_Collections_Generic_HashSet_T]) -> typing.Tuple[bool, System_Collections_Generic_HashSet_T]:
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...


class Dictionary(typing.Generic[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey]):
        """This class has no documentation."""

        @property
        def dictionary(self) -> System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

        def __contains__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            ...

        def __getitem__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> System_Collections_Generic_Dictionary_TValue:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
            ...

        def contains_key(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            ...

        @overload
        def remove(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            ...

        @overload
        def remove(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Generic_Dictionary_TKey], value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

        def try_add(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: System_Collections_Generic_Dictionary_TValue) -> bool:
            ...

        @overload
        def try_get_value(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
            ...

        @overload
        def try_get_value(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Generic_Dictionary_TKey], value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TKey], typing.Iterable[System_Collections_Generic_Dictionary_TKey]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TKey]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_Dictionary_TKey:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __contains__(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_Dictionary_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def contains(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_Dictionary_TKey], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.Dictionary.KeyCollection.Enumerator:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TValue], typing.Iterable[System_Collections_Generic_Dictionary_TValue]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TValue]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_Dictionary_TValue:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_Dictionary_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_Dictionary_TValue], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.Dictionary.ValueCollection.Enumerator:
            ...

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    @property
    def keys(self) -> System.Collections.Generic.Dictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.Generic.Dictionary.ValueCollection:
        ...

    def __contains__(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_Dictionary_TKey) -> System_Collections_Generic_Dictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def get_enumerator(self) -> System.Collections.Generic.Dictionary.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def remove(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    @overload
    def remove(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        ...

    def try_add(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
        ...


class List(typing.Generic[System_Collections_Generic_List_T], System.Object, System.Collections.Generic.IList[System_Collections_Generic_List_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_Generic_List_T], typing.Iterable[System_Collections_Generic_List_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_List_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_List_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Collections_Generic_List_T:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_List_T]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, index: int, value: System_Collections_Generic_List_T) -> None:
        ...

    def add(self, item: System_Collections_Generic_List_T) -> None:
        ...

    def add_range(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def as_read_only(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_Generic_List_T]:
        ...

    @overload
    def binary_search(self, index: int, count: int, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    @overload
    def binary_search(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def binary_search(self, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def copy_to(self, index: int, array: typing.List[System_Collections_Generic_List_T], array_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_List_T], array_index: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def exists(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...

    def find(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    def find_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def find_index(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def find_last(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    @overload
    def find_last_index(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def for_each(self, action: typing.Callable[[System_Collections_Generic_List_T], typing.Any]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.List.Enumerator:
        ...

    def get_range(self, index: int, count: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Generic_List_T) -> None:
        ...

    def insert_range(self, index: int, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    def remove(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def remove_range(self, index: int, count: int) -> None:
        ...

    @overload
    def reverse(self) -> None:
        ...

    @overload
    def reverse(self, index: int, count: int) -> None:
        ...

    def slice(self, start: int, length: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def sort(self) -> None:
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Generic_List_T, System_Collections_Generic_List_T], int]) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_List_T]:
        ...

    def trim_excess(self) -> None:
        ...

    def true_for_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...


class IComparer(typing.Generic[System_Collections_Generic_IComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_IComparer_T, y: System_Collections_Generic_IComparer_T) -> int:
        ...


class KeyNotFoundException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class KeyValuePair(typing.Generic[System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]):
    """This class has no documentation."""

    @property
    def key(self) -> System_Collections_Generic_KeyValuePair_TKey:
        ...

    @property
    def value(self) -> System_Collections_Generic_KeyValuePair_TValue:
        ...

    def __init__(self, key: System_Collections_Generic_KeyValuePair_TKey, value: System_Collections_Generic_KeyValuePair_TValue) -> None:
        ...

    def deconstruct(self, key: typing.Optional[System_Collections_Generic_KeyValuePair_TKey], value: typing.Optional[System_Collections_Generic_KeyValuePair_TValue]) -> typing.Tuple[None, System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]:
        ...

    def to_string(self) -> str:
        ...


class IList(typing.Generic[System_Collections_Generic_IList_T], System.Collections.Generic.ICollection[System_Collections_Generic_IList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IList_T:
        ...

    def __setitem__(self, index: int, value: System_Collections_Generic_IList_T) -> None:
        ...

    def index_of(self, item: System_Collections_Generic_IList_T) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Generic_IList_T) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...


class IEqualityComparer(typing.Generic[System_Collections_Generic_IEqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, x: System_Collections_Generic_IEqualityComparer_T, y: System_Collections_Generic_IEqualityComparer_T) -> bool:
        ...

    def get_hash_code(self, obj: System_Collections_Generic_IEqualityComparer_T) -> int:
        ...


class IEnumerable(typing.Generic[System_Collections_Generic_IEnumerable_T], System.Collections.IEnumerable, typing.Iterable[System_Collections_Generic_IEnumerable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_IEnumerable_T]:
        ...


class Queue(typing.Generic[System_Collections_Generic_Queue_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Queue_T], typing.Iterable[System_Collections_Generic_Queue_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Queue_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_Queue_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    def __contains__(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Queue_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_Queue_T]:
        ...

    def __len__(self) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_Queue_T], array_index: int) -> None:
        ...

    def dequeue(self) -> System_Collections_Generic_Queue_T:
        ...

    def enqueue(self, item: System_Collections_Generic_Queue_T) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def get_enumerator(self) -> System.Collections.Generic.Queue.Enumerator:
        ...

    def peek(self) -> System_Collections_Generic_Queue_T:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_Queue_T]:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        ...

    def try_dequeue(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Tuple[bool, System_Collections_Generic_Queue_T]:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Tuple[bool, System_Collections_Generic_Queue_T]:
        ...


class IAsyncEnumerator(typing.Generic[System_Collections_Generic_IAsyncEnumerator_T], System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def current(self) -> System_Collections_Generic_IAsyncEnumerator_T:
        ...

    def move_next_async(self) -> System.Threading.Tasks.ValueTask[bool]:
        ...


class ISet(typing.Generic[System_Collections_Generic_ISet_T], System.Collections.Generic.ICollection[System_Collections_Generic_ISet_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...


class IEnumerator(typing.Generic[System_Collections_Generic_IEnumerator_T], System.IDisposable, System.Collections.IEnumerator, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class NonRandomizedStringEqualityComparer(System.Object, System.Collections.Generic.IInternalStringEqualityComparer, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self, information: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def equals(self, x: str, y: str) -> bool:
        ...

    def get_hash_code(self, obj: str) -> int:
        ...

    @staticmethod
    def get_string_comparer(comparer: typing.Any) -> System.Collections.Generic.IEqualityComparer[str]:
        ...

    def get_underlying_equality_comparer(self) -> System.Collections.Generic.IEqualityComparer[str]:
        ...


class IReadOnlyCollection(typing.Generic[System_Collections_Generic_IReadOnlyCollection_T], System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlyCollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...


class IDictionary(typing.Generic[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def keys(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def values(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IDictionary_TKey) -> System_Collections_Generic_IDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def remove(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_IDictionary_TKey, value: typing.Optional[System_Collections_Generic_IDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_IDictionary_TValue]:
        ...


class IAlternateEqualityComparer(typing.Generic[System_Collections_Generic_IAlternateEqualityComparer_TAlternate, System_Collections_Generic_IAlternateEqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate) -> System_Collections_Generic_IAlternateEqualityComparer_T:
        ...

    def equals(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate, other: System_Collections_Generic_IAlternateEqualityComparer_T) -> bool:
        ...

    def get_hash_code(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate) -> int:
        ...


class LinkedList(typing.Generic[System_Collections_Generic_LinkedList_T], System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_LinkedList_T], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_LinkedList_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_LinkedList_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_LinkedList_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_LinkedList_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def first(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @property
    def last(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def __contains__(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_LinkedList_T]:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def add_after(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_after(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], new_node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_before(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_before(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], new_node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_first(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_first(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_last(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_last(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_LinkedList_T], index: int) -> None:
        ...

    def find(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def find_last(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def get_enumerator(self) -> System.Collections.Generic.LinkedList.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def remove(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def remove(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def remove_first(self) -> None:
        ...

    def remove_last(self) -> None:
        ...


class LinkedListNode(typing.Generic[System_Collections_Generic_LinkedListNode_T], System.Object):
    """This class has no documentation."""

    @property
    def list(self) -> System.Collections.Generic.LinkedList[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def next(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def previous(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def value(self) -> System_Collections_Generic_LinkedListNode_T:
        ...

    @value.setter
    def value(self, value: System_Collections_Generic_LinkedListNode_T) -> None:
        ...

    @property
    def value_ref(self) -> typing.Any:
        ...

    def __init__(self, value: System_Collections_Generic_LinkedListNode_T) -> None:
        ...


class SortedList(typing.Generic[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]):
    """This class has no documentation."""

    class KeyList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TKey], System.Collections.ICollection, typing.Iterable[System_Collections_Generic_SortedList_TKey]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def is_read_only(self) -> bool:
            ...

        def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TKey:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedList_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def add(self, key: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedList_TKey], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TKey]:
            ...

        def index_of(self, key: System_Collections_Generic_SortedList_TKey) -> int:
            ...

        def insert(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def remove_at(self, index: int) -> None:
            ...

    class ValueList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TValue], System.Collections.ICollection, typing.Iterable[System_Collections_Generic_SortedList_TValue]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def is_read_only(self) -> bool:
            ...

        def __contains__(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TValue:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedList_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def add(self, key: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedList_TValue], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TValue]:
            ...

        def index_of(self, value: System_Collections_Generic_SortedList_TValue) -> int:
            ...

        def insert(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def remove(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def remove_at(self, index: int) -> None:
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def keys(self) -> typing.List[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def values(self) -> typing.List[System_Collections_Generic_SortedList_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_SortedList_TKey) -> System_Collections_Generic_SortedList_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    def get_key_at_index(self, index: int) -> System_Collections_Generic_SortedList_TKey:
        ...

    def get_value_at_index(self, index: int) -> System_Collections_Generic_SortedList_TValue:
        ...

    def index_of_key(self, key: System_Collections_Generic_SortedList_TKey) -> int:
        ...

    def index_of_value(self, value: System_Collections_Generic_SortedList_TValue) -> int:
        ...

    def remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def set_value_at_index(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    def trim_excess(self) -> None:
        ...

    def try_get_value(self, key: System_Collections_Generic_SortedList_TKey, value: typing.Optional[System_Collections_Generic_SortedList_TValue]) -> typing.Tuple[bool, System_Collections_Generic_SortedList_TValue]:
        ...


class SortedDictionary(typing.Generic[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]], System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TKey], typing.Iterable[System_Collections_Generic_SortedDictionary_TKey]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TKey]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_SortedDictionary_TKey:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __contains__(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedDictionary_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def contains(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedDictionary_TKey], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.KeyCollection.Enumerator:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System_Collections_Generic_SortedDictionary_TValue]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TValue]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_SortedDictionary_TValue:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedDictionary_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedDictionary_TValue], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.ValueCollection.Enumerator:
            ...

    class KeyValuePairComparer(System.Collections.Generic.Comparer[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
        """This class has no documentation."""

        def __init__(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
            ...

        def compare(self, x: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], y: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> int:
            ...

        def equals(self, obj: typing.Any) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]:
        ...

    @property
    def keys(self) -> System.Collections.Generic.SortedDictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.Generic.SortedDictionary.ValueCollection:
        ...

    def __contains__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> System_Collections_Generic_SortedDictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_SortedDictionary_TValue) -> bool:
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.Enumerator:
        ...

    def remove(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_SortedDictionary_TKey, value: typing.Optional[System_Collections_Generic_SortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_SortedDictionary_TValue]:
        ...


class TreeSet(typing.Generic[System_Collections_Generic_TreeSet_T], System.Collections.Generic.SortedSet[System_Collections_Generic_TreeSet_T]):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_TreeSet_T]) -> None:
        ...


class Stack(typing.Generic[System_Collections_Generic_Stack_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Stack_T], typing.Iterable[System_Collections_Generic_Stack_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Stack_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_Stack_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    def __contains__(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Stack_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_Stack_T]:
        ...

    def __len__(self) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_Stack_T], array_index: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def get_enumerator(self) -> System.Collections.Generic.Stack.Enumerator:
        ...

    def peek(self) -> System_Collections_Generic_Stack_T:
        ...

    def pop(self) -> System_Collections_Generic_Stack_T:
        ...

    def push(self, item: System_Collections_Generic_Stack_T) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_Stack_T]:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Tuple[bool, System_Collections_Generic_Stack_T]:
        ...

    def try_pop(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Tuple[bool, System_Collections_Generic_Stack_T]:
        ...


class SortedSet(typing.Generic[System_Collections_Generic_SortedSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_SortedSet_T], System.Collections.ICollection, System.Collections.Generic.IReadOnlySet[System_Collections_Generic_SortedSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_SortedSet_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_SortedSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]:
        ...

    @property
    def min(self) -> System_Collections_Generic_SortedSet_T:
        ...

    @property
    def max(self) -> System_Collections_Generic_SortedSet_T:
        ...

    def __contains__(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedSet_T]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def create_set_comparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        ...

    @staticmethod
    @overload
    def create_set_comparer(member_equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_SortedSet_T]) -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        ...

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.SortedSet.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_view_between(self, lower_value: System_Collections_Generic_SortedSet_T, upper_value: System_Collections_Generic_SortedSet_T) -> System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]:
        ...

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def remove(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    def remove_where(self, match: typing.Callable[[System_Collections_Generic_SortedSet_T], bool]) -> int:
        ...

    def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def try_get_value(self, equal_value: System_Collections_Generic_SortedSet_T, actual_value: typing.Optional[System_Collections_Generic_SortedSet_T]) -> typing.Tuple[bool, System_Collections_Generic_SortedSet_T]:
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...


class PriorityQueue(typing.Generic[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority], System.Object):
    """This class has no documentation."""

    class UnorderedItemsCollection(System.Object, System.Collections.Generic.IReadOnlyCollection[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], System.Collections.ICollection, typing.Iterable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]):
            """This class has no documentation."""

            @property
            def current(self) -> System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]:
            ...

        def get_enumerator(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection.Enumerator:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]:
        ...

    @property
    def unordered_items(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initial_capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        ...

    @overload
    def __init__(self, initial_capacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        ...

    def clear(self) -> None:
        ...

    def dequeue(self) -> System_Collections_Generic_PriorityQueue_TElement:
        ...

    def dequeue_enqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        ...

    def enqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        ...

    def enqueue_dequeue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        ...

    @overload
    def enqueue_range(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        ...

    @overload
    def enqueue_range(self, elements: System.Collections.Generic.IEnumerable[System_Collections_Generic_PriorityQueue_TElement], priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def peek(self) -> System_Collections_Generic_PriorityQueue_TElement:
        ...

    def remove(self, element: System_Collections_Generic_PriorityQueue_TElement, removed_element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_PriorityQueue_TElement] = None) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        ...

    def trim_excess(self) -> None:
        ...

    def try_dequeue(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        ...

    def try_peek(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        ...


