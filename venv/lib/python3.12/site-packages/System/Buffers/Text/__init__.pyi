from typing import overload
from enum import IntEnum
import datetime
import typing

import System
import System.Buffers
import System.Buffers.Text


class Base64(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(utf_8: System.ReadOnlySpan[int], bytes: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        ...

    @staticmethod
    def decode_from_utf_8_in_place(buffer: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], bytes_consumed: typing.Optional[int], chars_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str]) -> int:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int]) -> typing.List[str]:
        ...

    @staticmethod
    def encode_to_string(source: System.ReadOnlySpan[int]) -> str:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(bytes: System.ReadOnlySpan[int], utf_8: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        ...

    @staticmethod
    def encode_to_utf_8_in_place(buffer: System.Span[int], data_length: int, bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    def get_encoded_length(bytes_length: int) -> int:
        ...

    @staticmethod
    def get_max_decoded_from_utf_8_length(length: int) -> int:
        ...

    @staticmethod
    def get_max_decoded_length(base_64_length: int) -> int:
        ...

    @staticmethod
    def get_max_encoded_to_utf_8_length(length: int) -> int:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text: System.ReadOnlySpan[str], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text_utf_8: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text_utf_8: System.ReadOnlySpan[int], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_utf_8_in_place(buffer: System.Span[int], data_length: int, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Base64Url(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        ...

    @staticmethod
    def decode_from_utf_8_in_place(buffer: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], bytes_consumed: typing.Optional[int], chars_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str]) -> int:
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int]) -> typing.List[str]:
        ...

    @staticmethod
    def encode_to_string(source: System.ReadOnlySpan[int]) -> str:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        ...

    @staticmethod
    def get_encoded_length(bytes_length: int) -> int:
        ...

    @staticmethod
    def get_max_decoded_length(base_64_length: int) -> int:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_url_text: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(base_64_url_text: System.ReadOnlySpan[str], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def is_valid(utf_8_base_64_url_text: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(utf_8_base_64_url_text: System.ReadOnlySpan[int], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_encode_to_utf_8_in_place(buffer: System.Span[int], data_length: int, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Utf8Formatter(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def try_format(value: System.Guid, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: float, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: bool, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: datetime.timedelta, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: int, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: System.DateTimeOffset, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_format(value: typing.Union[datetime.datetime, datetime.date], destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        ...


class Utf8Parser(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[float], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, float, int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[datetime.timedelta], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, datetime.timedelta, int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[bool], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, int, int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[System.Guid], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, System.Guid, int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[typing.Union[datetime.datetime, datetime.date]], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date], int]:
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[System.DateTimeOffset], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, System.DateTimeOffset, int]:
        ...


