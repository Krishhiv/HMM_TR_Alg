from typing import overload
from enum import IntEnum
import datetime
import typing

import System
import System.ComponentModel
import System.Timers

System_Timers__EventContainer_Callable = typing.TypeVar("System_Timers__EventContainer_Callable")
System_Timers__EventContainer_ReturnType = typing.TypeVar("System_Timers__EventContainer_ReturnType")


class ElapsedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def signal_time(self) -> datetime.datetime:
        ...

    def __init__(self, signal_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...


class Timer(System.ComponentModel.Component, System.ComponentModel.ISupportInitialize):
    """This class has no documentation."""

    @property
    def auto_reset(self) -> bool:
        ...

    @auto_reset.setter
    def auto_reset(self, value: bool) -> None:
        ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...

    @property
    def interval(self) -> float:
        ...

    @interval.setter
    def interval(self, value: float) -> None:
        ...

    @property
    def elapsed(self) -> _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], typing.Any], typing.Any]:
        ...

    @elapsed.setter
    def elapsed(self, value: _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def site(self) -> System.ComponentModel.ISite:
        ...

    @site.setter
    def site(self, value: System.ComponentModel.ISite) -> None:
        ...

    @property
    def synchronizing_object(self) -> System.ComponentModel.ISynchronizeInvoke:
        ...

    @synchronizing_object.setter
    def synchronizing_object(self, value: System.ComponentModel.ISynchronizeInvoke) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, interval: float) -> None:
        ...

    @overload
    def __init__(self, interval: datetime.timedelta) -> None:
        ...

    def begin_init(self) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def end_init(self) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...


class TimersDescriptionAttribute(System.ComponentModel.DescriptionAttribute):
    """This class has no documentation."""

    @property
    def description(self) -> str:
        ...

    def __init__(self, description: str) -> None:
        ...


class _EventContainer(typing.Generic[System_Timers__EventContainer_Callable, System_Timers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Timers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Timers__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Timers__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


