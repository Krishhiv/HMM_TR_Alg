from typing import overload
from enum import IntEnum
import typing

import System
import System.CodeDom.Compiler
import System.IO
import System.Text
import System.Threading
import System.Threading.Tasks


class GeneratedCodeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def tool(self) -> str:
        ...

    @property
    def version(self) -> str:
        ...

    def __init__(self, tool: str, version: str) -> None:
        ...


class IndentedTextWriter(System.IO.TextWriter):
    """This class has no documentation."""

    DEFAULT_TAB_STRING: str = "    "

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @property
    def new_line(self) -> str:
        ...

    @new_line.setter
    def new_line(self, value: str) -> None:
        ...

    @property
    def indent(self) -> int:
        ...

    @indent.setter
    def indent(self, value: int) -> None:
        ...

    @property
    def inner_writer(self) -> System.IO.TextWriter:
        ...

    @overload
    def __init__(self, writer: System.IO.TextWriter) -> None:
        ...

    @overload
    def __init__(self, writer: System.IO.TextWriter, tab_string: str) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def output_tabs(self) -> None:
        ...

    def output_tabs_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write(self, value: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, s: str) -> None:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, value: System.Text.Rune) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.Rune) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, value: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, s: str) -> None:
        ...

    @overload
    def write_line(self) -> None:
        ...

    @overload
    def write_line(self, value: bool) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.Rune) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write_line(self, value: float) -> None:
        ...

    @overload
    def write_line(self, value: int) -> None:
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.Rune) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    def write_line_no_tabs(self, s: str) -> None:
        ...

    def write_line_no_tabs_async(self, s: str) -> System.Threading.Tasks.Task:
        ...


