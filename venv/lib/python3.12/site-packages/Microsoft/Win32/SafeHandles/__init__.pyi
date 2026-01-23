from typing import overload
from enum import IntEnum
import abc
import typing

import Microsoft.Win32.SafeHandles
import System
import System.Runtime.InteropServices


class SafeHandleZeroOrMinusOneIsInvalid(System.Runtime.InteropServices.SafeHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self, owns_handle: bool) -> None:
        ...


class SafeFileHandle(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    """This class has no documentation."""

    @property
    def is_async(self) -> bool:
        ...

    @property
    def is_invalid(self) -> bool:
        ...

    @overload
    def __init__(self, preexisting_handle: System.IntPtr, owns_handle: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def release_handle(self) -> bool:
        ...


class SafeWaitHandle(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, existing_handle: System.IntPtr, owns_handle: bool) -> None:
        ...

    def release_handle(self) -> bool:
        ...


class CriticalHandleMinusOneIsInvalid(System.Runtime.InteropServices.CriticalHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self) -> None:
        ...


class SafeHandleMinusOneIsInvalid(System.Runtime.InteropServices.SafeHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self, owns_handle: bool) -> None:
        ...


class CriticalHandleZeroOrMinusOneIsInvalid(System.Runtime.InteropServices.CriticalHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self) -> None:
        ...


