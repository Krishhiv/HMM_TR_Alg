from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Collections.Specialized
import System.ComponentModel

System_Collections_ObjectModel_ReadOnlyCollection_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyCollection_T")
System_Collections_ObjectModel_Collection_T = typing.TypeVar("System_Collections_ObjectModel_Collection_T")
System_Collections_ObjectModel_ReadOnlyDictionary_TKey = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyDictionary_TKey")
System_Collections_ObjectModel_ReadOnlyDictionary_TValue = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyDictionary_TValue")
System_Collections_ObjectModel_ReadOnlySet_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlySet_T")
System_Collections_ObjectModel_ObservableCollection_T = typing.TypeVar("System_Collections_ObjectModel_ObservableCollection_T")
System_Collections_ObjectModel_KeyedCollection_TItem = typing.TypeVar("System_Collections_ObjectModel_KeyedCollection_TItem")
System_Collections_ObjectModel_KeyedCollection_TKey = typing.TypeVar("System_Collections_ObjectModel_KeyedCollection_TKey")
System_Collections_ObjectModel_ReadOnlyObservableCollection_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyObservableCollection_T")
System_Collections_ObjectModel__EventContainer_Callable = typing.TypeVar("System_Collections_ObjectModel__EventContainer_Callable")
System_Collections_ObjectModel__EventContainer_ReturnType = typing.TypeVar("System_Collections_ObjectModel__EventContainer_ReturnType")


class ReadOnlyCollection(typing.Generic[System_Collections_ObjectModel_ReadOnlyCollection_T], System.Object, System.Collections.Generic.IList[System_Collections_ObjectModel_ReadOnlyCollection_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_ObjectModel_ReadOnlyCollection_T], typing.Iterable[System_Collections_ObjectModel_ReadOnlyCollection_T]):
    """This class has no documentation."""

    EMPTY: System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyCollection_T]

    @property
    def count(self) -> int:
        ...

    @property
    def items(self) -> typing.List[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        ...

    def __getitem__(self, index: int) -> System_Collections_ObjectModel_ReadOnlyCollection_T:
        ...

    def __init__(self, list: System.Collections.Generic.IList[System_Collections_ObjectModel_ReadOnlyCollection_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        ...

    def contains(self, value: System_Collections_ObjectModel_ReadOnlyCollection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyCollection_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        ...

    def index_of(self, value: System_Collections_ObjectModel_ReadOnlyCollection_T) -> int:
        ...


class Collection(typing.Generic[System_Collections_ObjectModel_Collection_T], System.Object, System.Collections.Generic.IList[System_Collections_ObjectModel_Collection_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_ObjectModel_Collection_T], typing.Iterable[System_Collections_ObjectModel_Collection_T]):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def items(self) -> typing.List[System_Collections_ObjectModel_Collection_T]:
        ...

    def __getitem__(self, index: int) -> System_Collections_ObjectModel_Collection_T:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.IList[System_Collections_ObjectModel_Collection_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_Collection_T]:
        ...

    def __setitem__(self, index: int, value: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def add(self, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def clear(self) -> None:
        ...

    def clear_items(self) -> None:
        ...

    def contains(self, item: System_Collections_ObjectModel_Collection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_ObjectModel_Collection_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_Collection_T]:
        ...

    def index_of(self, item: System_Collections_ObjectModel_Collection_T) -> int:
        ...

    def insert(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def remove(self, item: System_Collections_ObjectModel_Collection_T) -> bool:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def remove_item(self, index: int) -> None:
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...


class ReadOnlyDictionary(typing.Generic[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]):
    """This class has no documentation."""

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], typing.Iterable[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]:
            ...

        def contains(self, item: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], typing.Iterable[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
            ...

        def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
            ...

    EMPTY: System.Collections.ObjectModel.ReadOnlyDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]

    @property
    def dictionary(self) -> System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
        ...

    @property
    def keys(self) -> System.Collections.ObjectModel.ReadOnlyDictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.ObjectModel.ReadOnlyDictionary.ValueCollection:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> System_Collections_ObjectModel_ReadOnlyDictionary_TValue:
        ...

    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]:
        ...

    def try_get_value(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey, value: typing.Optional[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]) -> typing.Tuple[bool, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
        ...


class ReadOnlySet(typing.Generic[System_Collections_ObjectModel_ReadOnlySet_T], System.Object, System.Collections.Generic.IReadOnlySet[System_Collections_ObjectModel_ReadOnlySet_T], System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T], System.Collections.ICollection, typing.Iterable[System_Collections_ObjectModel_ReadOnlySet_T]):
    """This class has no documentation."""

    EMPTY: System.Collections.ObjectModel.ReadOnlySet[System_Collections_ObjectModel_ReadOnlySet_T]

    @property
    def set(self) -> System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T]:
        ...

    @property
    def count(self) -> int:
        ...

    def __init__(self, set: System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlySet_T]:
        ...

    def contains(self, item: System_Collections_ObjectModel_ReadOnlySet_T) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlySet_T]:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...


class ObservableCollection(typing.Generic[System_Collections_ObjectModel_ObservableCollection_T], System.Collections.ObjectModel.Collection[System_Collections_ObjectModel_ObservableCollection_T], System.Collections.Specialized.INotifyCollectionChanged, System.ComponentModel.INotifyPropertyChanged):
    """This class has no documentation."""

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]:
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]:
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ObservableCollection_T]) -> None:
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.List[System_Collections_ObjectModel_ObservableCollection_T]) -> None:
        ...

    def block_reentrancy(self) -> System.IDisposable:
        ...

    def check_reentrancy(self) -> None:
        ...

    def clear_items(self) -> None:
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_ObservableCollection_T) -> None:
        ...

    def move(self, old_index: int, new_index: int) -> None:
        ...

    def move_item(self, old_index: int, new_index: int) -> None:
        ...

    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        ...

    def on_property_changed(self, e: System.ComponentModel.PropertyChangedEventArgs) -> None:
        ...

    def remove_item(self, index: int) -> None:
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_ObservableCollection_T) -> None:
        ...


class KeyedCollection(typing.Generic[System_Collections_ObjectModel_KeyedCollection_TKey, System_Collections_ObjectModel_KeyedCollection_TItem], System.Collections.ObjectModel.Collection[System_Collections_ObjectModel_KeyedCollection_TItem], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey]:
        ...

    @property
    def dictionary(self) -> System.Collections.Generic.IDictionary[System_Collections_ObjectModel_KeyedCollection_TKey, System_Collections_ObjectModel_KeyedCollection_TItem]:
        ...

    def __getitem__(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> System_Collections_ObjectModel_KeyedCollection_TItem:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey]) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey], dictionary_creation_threshold: int) -> None:
        ...

    def change_item_key(self, item: System_Collections_ObjectModel_KeyedCollection_TItem, new_key: System_Collections_ObjectModel_KeyedCollection_TKey) -> None:
        ...

    def clear_items(self) -> None:
        ...

    def contains(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> bool:
        ...

    def get_key_for_item(self, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> System_Collections_ObjectModel_KeyedCollection_TKey:
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> None:
        ...

    def remove(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> bool:
        ...

    def remove_item(self, index: int) -> None:
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> None:
        ...

    def try_get_value(self, key: System_Collections_ObjectModel_KeyedCollection_TKey, item: typing.Optional[System_Collections_ObjectModel_KeyedCollection_TItem]) -> typing.Tuple[bool, System_Collections_ObjectModel_KeyedCollection_TItem]:
        ...


class ReadOnlyObservableCollection(typing.Generic[System_Collections_ObjectModel_ReadOnlyObservableCollection_T], System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T], System.Collections.Specialized.INotifyCollectionChanged, System.ComponentModel.INotifyPropertyChanged):
    """This class has no documentation."""

    EMPTY: System.Collections.ObjectModel.ReadOnlyObservableCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T]

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]:
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]:
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, list: System.Collections.ObjectModel.ObservableCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T]) -> None:
        ...

    def on_collection_changed(self, args: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        ...

    def on_property_changed(self, args: System.ComponentModel.PropertyChangedEventArgs) -> None:
        ...


class _EventContainer(typing.Generic[System_Collections_ObjectModel__EventContainer_Callable, System_Collections_ObjectModel__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Collections_ObjectModel__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Collections_ObjectModel__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Collections_ObjectModel__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


