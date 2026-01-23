from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.Collections.Specialized

System_Collections_Specialized__EventContainer_Callable = typing.TypeVar("System_Collections_Specialized__EventContainer_Callable")
System_Collections_Specialized__EventContainer_ReturnType = typing.TypeVar("System_Collections_Specialized__EventContainer_ReturnType")


class NotifyCollectionChangedAction(IntEnum):
    """This class has no documentation."""

    ADD = 0

    REMOVE = 1

    REPLACE = 2

    MOVE = 3

    RESET = 4


class NotifyCollectionChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def action(self) -> System.Collections.Specialized.NotifyCollectionChangedAction:
        ...

    @property
    def new_items(self) -> typing.List[typing.Any]:
        ...

    @property
    def old_items(self) -> typing.List[typing.Any]:
        ...

    @property
    def new_starting_index(self) -> int:
        ...

    @property
    def old_starting_index(self) -> int:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any, index: int) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_item: typing.Any, old_item: typing.Any) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_item: typing.Any, old_item: typing.Any, index: int) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any, index: int, old_index: int) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList, starting_index: int) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_items: System.Collections.IList, old_items: System.Collections.IList) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_items: System.Collections.IList, old_items: System.Collections.IList, starting_index: int) -> None:
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList, index: int, old_index: int) -> None:
        ...


class INotifyCollectionChanged(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]:
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...


class _EventContainer(typing.Generic[System_Collections_Specialized__EventContainer_Callable, System_Collections_Specialized__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Collections_Specialized__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Collections_Specialized__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Collections_Specialized__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


