from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import System
import System.Collections
import System.Collections.Concurrent
import System.Collections.Generic
import System.Threading

System_Collections_Concurrent_ConcurrentQueue_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentQueue_T")
System_Collections_Concurrent_IProducerConsumerCollection_T = typing.TypeVar("System_Collections_Concurrent_IProducerConsumerCollection_T")
System_Collections_Concurrent_ConcurrentDictionary_TKey = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_TKey")
System_Collections_Concurrent_ConcurrentDictionary_TValue = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_TValue")
System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey")
System_Collections_Concurrent_Partitioner_TSource = typing.TypeVar("System_Collections_Concurrent_Partitioner_TSource")
System_Collections_Concurrent_ConcurrentStack_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentStack_T")
System_Collections_Concurrent_OrderablePartitioner_TSource = typing.TypeVar("System_Collections_Concurrent_OrderablePartitioner_TSource")
System_Collections_Concurrent_ConcurrentBag_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentBag_T")
System_Collections_Concurrent_BlockingCollection_T = typing.TypeVar("System_Collections_Concurrent_BlockingCollection_T")


class ConcurrentQueue(typing.Generic[System_Collections_Concurrent_ConcurrentQueue_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentQueue_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentQueue_T], typing.Iterable[System_Collections_Concurrent_ConcurrentQueue_T]):
    """This class has no documentation."""

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentQueue_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Concurrent_ConcurrentQueue_T]:
        ...

    def clear(self) -> None:
        ...

    def copy_to(self, array: typing.List[System_Collections_Concurrent_ConcurrentQueue_T], index: int) -> None:
        ...

    def enqueue(self, item: System_Collections_Concurrent_ConcurrentQueue_T) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentQueue_T]:
        ...

    def to_array(self) -> typing.List[System_Collections_Concurrent_ConcurrentQueue_T]:
        ...

    def try_dequeue(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentQueue_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentQueue_T]:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentQueue_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentQueue_T]:
        ...


class IProducerConsumerCollection(typing.Generic[System_Collections_Concurrent_IProducerConsumerCollection_T], System.Collections.Generic.IEnumerable[System_Collections_Concurrent_IProducerConsumerCollection_T], System.Collections.ICollection, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def copy_to(self, array: typing.List[System_Collections_Concurrent_IProducerConsumerCollection_T], index: int) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Concurrent_IProducerConsumerCollection_T]:
        ...

    def try_add(self, item: System_Collections_Concurrent_IProducerConsumerCollection_T) -> bool:
        ...

    def try_take(self, item: typing.Optional[System_Collections_Concurrent_IProducerConsumerCollection_T]) -> typing.Tuple[bool, System_Collections_Concurrent_IProducerConsumerCollection_T]:
        ...


class ConcurrentDictionary(typing.Generic[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey]):
        """This class has no documentation."""

        @property
        def dictionary(self) -> System.Collections.Concurrent.ConcurrentDictionary[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
            ...

        def __getitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
            ...

        def __setitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> None:
            ...

        def contains_key(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey) -> bool:
            ...

        def try_add(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> bool:
            ...

        @overload
        def try_get_value(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
            ...

        @overload
        def try_get_value(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TKey], value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
            ...

        @overload
        def try_remove(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
            ...

        @overload
        def try_remove(self, key: System_Collections_Concurrent_ConcurrentDictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TKey], value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
            ...

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def keys(self) -> System.Collections.Generic.ICollection[System_Collections_Concurrent_ConcurrentDictionary_TKey]:
        ...

    @property
    def values(self) -> System.Collections.Generic.ICollection[System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, concurrency_level: int, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, concurrency_level: int, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, concurrency_level: int, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> None:
        ...

    @overload
    def add_or_update(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, add_value_factory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey], System_Collections_Concurrent_ConcurrentDictionary_TValue], update_value_factory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        ...

    @overload
    def add_or_update(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, add_value: System_Collections_Concurrent_ConcurrentDictionary_TValue, update_value_factory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]:
        ...

    @overload
    def get_or_add(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value_factory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        ...

    @overload
    def get_or_add(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        ...

    def to_array(self) -> typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]:
        ...

    def try_add(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        ...

    @overload
    def try_remove(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        ...

    @overload
    def try_remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> bool:
        ...

    def try_update(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, new_value: System_Collections_Concurrent_ConcurrentDictionary_TValue, comparison_value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> bool:
        ...


class EnumerablePartitionerOptions(IntEnum):
    """This class has no documentation."""

    NONE = ...

    NO_BUFFERING = ...


class Partitioner(typing.Generic[System_Collections_Concurrent_Partitioner_TSource], System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def supports_dynamic_partitions(self) -> bool:
        ...

    @staticmethod
    @overload
    def create(from_inclusive: int, to_exclusive: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        ...

    @staticmethod
    @overload
    def create(from_inclusive: int, to_exclusive: int, range_size: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        ...

    def get_dynamic_partitions(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_Partitioner_TSource]:
        ...

    def get_partitions(self, partition_count: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System_Collections_Concurrent_Partitioner_TSource]]:
        ...


class ConcurrentStack(typing.Generic[System_Collections_Concurrent_ConcurrentStack_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentStack_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentStack_T], typing.Iterable[System_Collections_Concurrent_ConcurrentStack_T]):
    """This class has no documentation."""

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentStack_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Concurrent_ConcurrentStack_T]:
        ...

    def clear(self) -> None:
        ...

    def copy_to(self, array: typing.List[System_Collections_Concurrent_ConcurrentStack_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentStack_T]:
        ...

    def push(self, item: System_Collections_Concurrent_ConcurrentStack_T) -> None:
        ...

    @overload
    def push_range(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T]) -> None:
        ...

    @overload
    def push_range(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T], start_index: int, count: int) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Concurrent_ConcurrentStack_T]:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentStack_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentStack_T]:
        ...

    def try_pop(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentStack_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentStack_T]:
        ...

    @overload
    def try_pop_range(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T]) -> int:
        ...

    @overload
    def try_pop_range(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T], start_index: int, count: int) -> int:
        ...


class OrderablePartitioner(typing.Generic[System_Collections_Concurrent_OrderablePartitioner_TSource], System.Collections.Concurrent.Partitioner[System_Collections_Concurrent_OrderablePartitioner_TSource], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def keys_ordered_in_each_partition(self) -> bool:
        ...

    @property
    def keys_ordered_across_partitions(self) -> bool:
        ...

    @property
    def keys_normalized(self) -> bool:
        ...

    def __init__(self, keys_ordered_in_each_partition: bool, keys_ordered_across_partitions: bool, keys_normalized: bool) -> None:
        ...

    def get_dynamic_partitions(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_OrderablePartitioner_TSource]:
        ...

    def get_orderable_dynamic_partitions(self) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[int, System_Collections_Concurrent_OrderablePartitioner_TSource]]:
        ...

    def get_orderable_partitions(self, partition_count: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[int, System_Collections_Concurrent_OrderablePartitioner_TSource]]]:
        ...

    def get_partitions(self, partition_count: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System_Collections_Concurrent_OrderablePartitioner_TSource]]:
        ...


class ConcurrentBag(typing.Generic[System_Collections_Concurrent_ConcurrentBag_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentBag_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentBag_T], typing.Iterable[System_Collections_Concurrent_ConcurrentBag_T]):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentBag_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Concurrent_ConcurrentBag_T]:
        ...

    def add(self, item: System_Collections_Concurrent_ConcurrentBag_T) -> None:
        ...

    def clear(self) -> None:
        ...

    def copy_to(self, array: typing.List[System_Collections_Concurrent_ConcurrentBag_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentBag_T]:
        ...

    def to_array(self) -> typing.List[System_Collections_Concurrent_ConcurrentBag_T]:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentBag_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentBag_T]:
        ...

    def try_take(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentBag_T]) -> typing.Tuple[bool, System_Collections_Concurrent_ConcurrentBag_T]:
        ...


class BlockingCollection(typing.Generic[System_Collections_Concurrent_BlockingCollection_T], System.Object, System.Collections.ICollection, System.IDisposable, System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_BlockingCollection_T], typing.Iterable[System_Collections_Concurrent_BlockingCollection_T]):
    """This class has no documentation."""

    @property
    def bounded_capacity(self) -> int:
        ...

    @property
    def is_adding_completed(self) -> bool:
        ...

    @property
    def is_completed(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, bounded_capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_BlockingCollection_T], bounded_capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_BlockingCollection_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def add(self, item: System_Collections_Concurrent_BlockingCollection_T) -> None:
        ...

    @overload
    def add(self, item: System_Collections_Concurrent_BlockingCollection_T, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @staticmethod
    @overload
    def add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T) -> int:
        ...

    @staticmethod
    @overload
    def add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, cancellation_token: System.Threading.CancellationToken) -> int:
        ...

    def complete_adding(self) -> None:
        ...

    def copy_to(self, array: typing.List[System_Collections_Concurrent_BlockingCollection_T], index: int) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def get_consuming_enumerable(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def get_consuming_enumerable(self, cancellation_token: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def take(self) -> System_Collections_Concurrent_BlockingCollection_T:
        ...

    @overload
    def take(self, cancellation_token: System.Threading.CancellationToken) -> System_Collections_Concurrent_BlockingCollection_T:
        ...

    @staticmethod
    @overload
    def take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @staticmethod
    @overload
    def take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], cancellation_token: System.Threading.CancellationToken) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    def to_array(self) -> typing.List[System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def try_add(self, item: System_Collections_Concurrent_BlockingCollection_T) -> bool:
        ...

    @overload
    def try_add(self, item: System_Collections_Concurrent_BlockingCollection_T, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_add(self, item: System_Collections_Concurrent_BlockingCollection_T, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_add(self, item: System_Collections_Concurrent_BlockingCollection_T, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @staticmethod
    @overload
    def try_add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T) -> int:
        ...

    @staticmethod
    @overload
    def try_add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def try_add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    @overload
    def try_add_to_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> int:
        ...

    @overload
    def try_take(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Tuple[bool, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def try_take(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], timeout: datetime.timedelta) -> typing.Tuple[bool, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def try_take(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], milliseconds_timeout: int) -> typing.Tuple[bool, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @overload
    def try_take(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> typing.Tuple[bool, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @staticmethod
    @overload
    def try_take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @staticmethod
    @overload
    def try_take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], timeout: datetime.timedelta) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @staticmethod
    @overload
    def try_take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], milliseconds_timeout: int) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...

    @staticmethod
    @overload
    def try_take_from_any(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> typing.Tuple[int, System_Collections_Concurrent_BlockingCollection_T]:
        ...


