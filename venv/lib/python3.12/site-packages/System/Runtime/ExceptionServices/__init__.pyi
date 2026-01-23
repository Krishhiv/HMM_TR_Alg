from typing import overload
from enum import IntEnum
import typing

import System
import System.Runtime.ExceptionServices


class FirstChanceExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception(self) -> System.Exception:
        ...

    def __init__(self, exception: System.Exception) -> None:
        ...


class ExceptionDispatchInfo(System.Object):
    """This class has no documentation."""

    @property
    def source_exception(self) -> System.Exception:
        ...

    @staticmethod
    def capture(source: System.Exception) -> System.Runtime.ExceptionServices.ExceptionDispatchInfo:
        ...

    @staticmethod
    def set_current_stack_trace(source: System.Exception) -> System.Exception:
        ...

    @staticmethod
    def set_remote_stack_trace(source: System.Exception, stack_trace: str) -> System.Exception:
        ...

    @overload
    def throw(self) -> None:
        ...

    @staticmethod
    @overload
    def throw(source: System.Exception) -> None:
        ...


class ExceptionHandling(System.Object):
    """This class has no documentation."""

    @staticmethod
    def raise_app_domain_unhandled_exception_event(exception: typing.Any) -> None:
        ...

    @staticmethod
    def set_unhandled_exception_handler(handler: typing.Callable[[System.Exception], bool]) -> None:
        ...


class HandleProcessCorruptedStateExceptionsAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


