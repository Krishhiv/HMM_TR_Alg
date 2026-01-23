from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Threading.Tasks.Sources

System_Threading_Tasks_Sources_IValueTaskSource_TResult = typing.TypeVar("System_Threading_Tasks_Sources_IValueTaskSource_TResult")
System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult = typing.TypeVar("System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult")


class ValueTaskSourceOnCompletedFlags(IntEnum):
    """This class has no documentation."""

    NONE = 0

    USE_SCHEDULING_CONTEXT = ...

    FLOW_EXECUTION_CONTEXT = ...


class ValueTaskSourceStatus(IntEnum):
    """This class has no documentation."""

    PENDING = 0

    SUCCEEDED = 1

    FAULTED = 2

    CANCELED = 3


class IValueTaskSource(typing.Generic[System_Threading_Tasks_Sources_IValueTaskSource_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_result(self, token: int) -> None:
        ...

    def get_status(self, token: int) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        ...

    def on_completed(self, continuation: typing.Callable[[System.Object], typing.Any], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        ...


class ManualResetValueTaskSourceCore(typing.Generic[System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult]):
    """This class has no documentation."""

    @property
    def run_continuations_asynchronously(self) -> bool:
        ...

    @run_continuations_asynchronously.setter
    def run_continuations_asynchronously(self, value: bool) -> None:
        ...

    @property
    def version(self) -> int:
        ...

    def get_result(self, token: int) -> System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult:
        ...

    def get_status(self, token: int) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        ...

    def on_completed(self, continuation: typing.Callable[[System.Object], typing.Any], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        ...

    def reset(self) -> None:
        ...

    def set_exception(self, error: System.Exception) -> None:
        ...

    def set_result(self, result: System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult) -> None:
        ...


