from typing import overload
from enum import IntEnum
import typing

import System
import System.Buffers
import System.Text.Unicode


class Utf8(System.Object):
    """This class has no documentation."""

    @staticmethod
    def from_utf_16(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_read: typing.Optional[int], bytes_written: typing.Optional[int], replace_invalid_sequences: bool = True, is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    def is_valid(value: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    def to_utf_16(source: System.ReadOnlySpan[int], destination: System.Span[str], bytes_read: typing.Optional[int], chars_written: typing.Optional[int], replace_invalid_sequences: bool = True, is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...


