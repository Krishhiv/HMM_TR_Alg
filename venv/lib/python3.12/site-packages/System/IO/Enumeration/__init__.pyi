from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections.Generic
import System.IO
import System.IO.Enumeration
import System.Runtime.ConstrainedExecution

System_IO_Enumeration_FileSystemEnumerator_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerator_TResult")
System_IO_Enumeration_FileSystemEnumerable_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerable_TResult")


class FileSystemEntry:
    """This class has no documentation."""

    @property
    def file_name(self) -> System.ReadOnlySpan[str]:
        ...

    @property
    def directory(self) -> System.ReadOnlySpan[str]:
        ...

    @property
    def root_directory(self) -> System.ReadOnlySpan[str]:
        ...

    @property
    def original_root_directory(self) -> System.ReadOnlySpan[str]:
        ...

    @property
    def attributes(self) -> System.IO.FileAttributes:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def creation_time_utc(self) -> System.DateTimeOffset:
        ...

    @property
    def last_access_time_utc(self) -> System.DateTimeOffset:
        ...

    @property
    def last_write_time_utc(self) -> System.DateTimeOffset:
        ...

    @property
    def is_hidden(self) -> bool:
        ...

    @property
    def is_directory(self) -> bool:
        ...

    def to_file_system_info(self) -> System.IO.FileSystemInfo:
        ...

    def to_full_path(self) -> str:
        ...

    def to_specified_full_path(self) -> str:
        ...


class FileSystemName(System.Object):
    """This class has no documentation."""

    @staticmethod
    def matches_simple_expression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignore_case: bool = True) -> bool:
        ...

    @staticmethod
    def matches_win_32_expression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignore_case: bool = True) -> bool:
        ...

    @staticmethod
    def translate_win_32_expression(expression: str) -> str:
        ...


class FileSystemEnumerator(typing.Generic[System_IO_Enumeration_FileSystemEnumerator_TResult], System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.Collections.Generic.IEnumerator[System_IO_Enumeration_FileSystemEnumerator_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def current(self) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        ...

    def __init__(self, directory: str, options: System.IO.EnumerationOptions = None) -> None:
        ...

    def continue_on_error(self, error: int) -> bool:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def move_next(self) -> bool:
        ...

    def on_directory_finished(self, directory: System.ReadOnlySpan[str]) -> None:
        ...

    def reset(self) -> None:
        ...

    def should_include_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        ...

    def should_recurse_into_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        ...

    def transform_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        ...


class FileSystemEnumerable(typing.Generic[System_IO_Enumeration_FileSystemEnumerable_TResult], System.Object, System.Collections.Generic.IEnumerable[System_IO_Enumeration_FileSystemEnumerable_TResult], typing.Iterable[System_IO_Enumeration_FileSystemEnumerable_TResult]):
    """This class has no documentation."""

    @property
    def should_include_predicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @should_include_predicate.setter
    def should_include_predicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]) -> None:
        ...

    @property
    def should_recurse_predicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @should_recurse_predicate.setter
    def should_recurse_predicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]) -> None:
        ...

    def __init__(self, directory: str, transform: typing.Callable[[System.IO.Enumeration.FileSystemEntry], System_IO_Enumeration_FileSystemEnumerable_TResult], options: System.IO.EnumerationOptions = None) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_IO_Enumeration_FileSystemEnumerable_TResult]:
        ...

    def find_predicate(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        ...

    def find_transform(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerable_TResult:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_IO_Enumeration_FileSystemEnumerable_TResult]:
        ...


