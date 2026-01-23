from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Windows.Input

System_Windows_Input__EventContainer_Callable = typing.TypeVar("System_Windows_Input__EventContainer_Callable")
System_Windows_Input__EventContainer_ReturnType = typing.TypeVar("System_Windows_Input__EventContainer_ReturnType")


class ICommand(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def can_execute_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @can_execute_changed.setter
    def can_execute_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    def can_execute(self, parameter: typing.Any) -> bool:
        ...

    def execute(self, parameter: typing.Any) -> None:
        ...


class _EventContainer(typing.Generic[System_Windows_Input__EventContainer_Callable, System_Windows_Input__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Windows_Input__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Windows_Input__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Windows_Input__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


