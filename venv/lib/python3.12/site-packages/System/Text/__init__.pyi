from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Buffers
import System.Collections.Generic
import System.IO
import System.Runtime.Serialization
import System.Text

System_Text_RunePosition = typing.Any


class StringBuilderRuneEnumerator(System.Collections.Generic.IEnumerable[System.Text.Rune], System.Collections.Generic.IEnumerator[System.Text.Rune], typing.Iterable[System.Text.Rune]):
    """This class has no documentation."""

    @property
    def current(self) -> System.Text.Rune:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.Rune]:
        ...

    def get_enumerator(self) -> System.Text.StringBuilderRuneEnumerator:
        ...

    def move_next(self) -> bool:
        ...


class CompositeFormat(System.Object):
    """This class has no documentation."""

    @property
    def format(self) -> str:
        ...

    @property
    def minimum_argument_count(self) -> int:
        ...

    @staticmethod
    def parse(format: str) -> System.Text.CompositeFormat:
        ...


class StringBuilder(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    class ChunkEnumerator:
        """This class has no documentation."""

        @property
        def current(self) -> System.ReadOnlyMemory[str]:
            ...

        def get_enumerator(self) -> System.Text.StringBuilder.ChunkEnumerator:
            ...

        def move_next(self) -> bool:
            ...

    class AppendInterpolatedStringHandler:
        """This class has no documentation."""

        @overload
        def __init__(self, literal_length: int, formatted_count: int, string_builder: System.Text.StringBuilder) -> None:
            ...

        @overload
        def __init__(self, literal_length: int, formatted_count: int, string_builder: System.Text.StringBuilder, provider: System.IFormatProvider) -> None:
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> None:
            ...

        @overload
        def append_formatted(self, value: str) -> None:
            ...

        @overload
        def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> None:
            ...

        def append_literal(self, value: str) -> None:
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def max_capacity(self) -> int:
        ...

    @property
    def length(self) -> int:
        ...

    @length.setter
    def length(self, value: int) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    @overload
    def __init__(self, value: str, capacity: int) -> None:
        ...

    @overload
    def __init__(self, value: str, start_index: int, length: int, capacity: int) -> None:
        ...

    @overload
    def __init__(self, capacity: int, max_capacity: int) -> None:
        ...

    def __setitem__(self, index: int, value: str) -> None:
        ...

    @overload
    def append(self, value: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: typing.Any, value_count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: str, repeat_count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: typing.List[str], start_index: int, char_count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: str, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.Text.StringBuilder) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.Text.StringBuilder, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: bool) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.Text.Rune) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: float) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: typing.List[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.ReadOnlyMemory[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, provider: System.IFormatProvider, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: System.Text.CompositeFormat, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_join(self, separator: str, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_join(self, separator: str, *values: typing.Union[str, typing.Iterable[str]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self, value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self, provider: System.IFormatProvider, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        ...

    def clear(self) -> System.Text.StringBuilder:
        ...

    @overload
    def copy_to(self, source_index: int, destination: typing.List[str], destination_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, source_index: int, destination: System.Span[str], count: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        ...

    def enumerate_runes(self) -> System.Text.StringBuilderRuneEnumerator:
        ...

    @overload
    def equals(self, sb: System.Text.StringBuilder) -> bool:
        ...

    @overload
    def equals(self, span: System.ReadOnlySpan[str]) -> bool:
        ...

    def get_chunks(self) -> System.Text.StringBuilder.ChunkEnumerator:
        ...

    def get_rune_at(self, index: int) -> System.Text.Rune:
        ...

    @overload
    def insert(self, index: int, value: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: str, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: bool) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: int) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: System.Text.Rune) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: typing.List[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: typing.List[str], start_index: int, char_count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: float) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        ...

    def remove(self, start_index: int, length: int) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_value: str, new_value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_value: System.ReadOnlySpan[str], new_value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_value: str, new_value: str, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_value: System.ReadOnlySpan[str], new_value: System.ReadOnlySpan[str], start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_char: str, new_char: str) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_char: str, new_char: str, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_rune: System.Text.Rune, new_rune: System.Text.Rune) -> System.Text.StringBuilder:
        ...

    @overload
    def replace(self, old_rune: System.Text.Rune, new_rune: System.Text.Rune, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, start_index: int, length: int) -> str:
        ...

    def try_get_rune_at(self, index: int, value: typing.Optional[System.Text.Rune]) -> typing.Tuple[bool, System.Text.Rune]:
        ...


class EncoderFallbackBuffer(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def remaining(self) -> int:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class EncoderFallback(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    REPLACEMENT_FALLBACK: System.Text.EncoderFallback

    EXCEPTION_FALLBACK: System.Text.EncoderFallback

    @property
    @abc.abstractmethod
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...


class DecoderFallbackBuffer(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def remaining(self) -> int:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DecoderFallback(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    REPLACEMENT_FALLBACK: System.Text.DecoderFallback

    EXCEPTION_FALLBACK: System.Text.DecoderFallback

    @property
    @abc.abstractmethod
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...


class EncodingProvider(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def get_encoding(self, name: str) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, codepage: int) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, name: str, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, codepage: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    def get_encodings(self) -> System.Collections.Generic.IEnumerable[System.Text.EncodingInfo]:
        ...


class NormalizationForm(IntEnum):
    """This class has no documentation."""

    FORM_C = 1

    FORM_D = 2

    FORM_KC = 5

    FORM_KD = 6


class Decoder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def fallback(self) -> System.Text.DecoderFallback:
        ...

    @fallback.setter
    def fallback(self, value: System.Text.DecoderFallback) -> None:
        ...

    @property
    def fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def convert(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int, flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int, char_count: int, flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int, flush: bool) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int, flush: bool) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int], flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int, flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int, flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool) -> int:
        ...

    def reset(self) -> None:
        ...


class Encoder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def fallback(self) -> System.Text.EncoderFallback:
        ...

    @fallback.setter
    def fallback(self, value: System.Text.EncoderFallback) -> None:
        ...

    @property
    def fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def convert(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int, flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int, byte_count: int, flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int, flush: bool) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int, flush: bool) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str], flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int, flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int, flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool) -> int:
        ...

    def reset(self) -> None:
        ...


class Encoding(System.Object, System.ICloneable):
    """This class has no documentation."""

    DEFAULT: System.Text.Encoding

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def body_name(self) -> str:
        ...

    @property
    def encoding_name(self) -> str:
        ...

    @property
    def header_name(self) -> str:
        ...

    @property
    def web_name(self) -> str:
        ...

    @property
    def windows_code_page(self) -> int:
        ...

    @property
    def is_browser_display(self) -> bool:
        ...

    @property
    def is_browser_save(self) -> bool:
        ...

    @property
    def is_mail_news_display(self) -> bool:
        ...

    @property
    def is_mail_news_save(self) -> bool:
        ...

    @property
    def is_single_byte(self) -> bool:
        ...

    @property
    def encoder_fallback(self) -> System.Text.EncoderFallback:
        ...

    @encoder_fallback.setter
    def encoder_fallback(self, value: System.Text.EncoderFallback) -> None:
        ...

    @property
    def decoder_fallback(self) -> System.Text.DecoderFallback:
        ...

    @decoder_fallback.setter
    def decoder_fallback(self, value: System.Text.DecoderFallback) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    ASCII: System.Text.Encoding

    LATIN_1: System.Text.Encoding

    @property
    def code_page(self) -> int:
        ...

    UNICODE: System.Text.Encoding

    BIG_ENDIAN_UNICODE: System.Text.Encoding

    UTF_7: System.Text.Encoding

    UTF_8: System.Text.Encoding

    UTF_32: System.Text.Encoding

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, code_page: int) -> None:
        ...

    @overload
    def __init__(self, code_page: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def convert(src_encoding: System.Text.Encoding, dst_encoding: System.Text.Encoding, bytes: typing.List[int]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def convert(src_encoding: System.Text.Encoding, dst_encoding: System.Text.Encoding, bytes: typing.List[int], index: int, count: int) -> typing.List[int]:
        ...

    @staticmethod
    def create_transcoding_stream(inner_stream: System.IO.Stream, inner_stream_encoding: System.Text.Encoding, outer_stream_encoding: System.Text.Encoding, leave_open: bool = False) -> System.IO.Stream:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str]) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str, index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str]) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], index: int, count: int) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, s: str, index: int, count: int) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int]) -> typing.List[str]:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], index: int, count: int) -> typing.List[str]:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    @staticmethod
    @overload
    def get_encoding(codepage: int) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(codepage: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(name: str) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(name: str, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @staticmethod
    def get_encodings() -> typing.List[System.Text.EncodingInfo]:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    @overload
    def get_string(self, bytes: typing.Any, byte_count: int) -> str:
        ...

    @overload
    def get_string(self, bytes: System.ReadOnlySpan[int]) -> str:
        ...

    @overload
    def get_string(self, bytes: typing.List[int]) -> str:
        ...

    @overload
    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...

    @overload
    def is_always_normalized(self) -> bool:
        ...

    @overload
    def is_always_normalized(self, form: System.Text.NormalizationForm) -> bool:
        ...

    @staticmethod
    def register_provider(provider: System.Text.EncodingProvider) -> None:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class UTF7Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, allow_optionals: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class EncodingInfo(System.Object):
    """This class has no documentation."""

    @property
    def code_page(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def display_name(self) -> str:
        ...

    def __init__(self, provider: System.Text.EncodingProvider, code_page: int, name: str, display_name: str) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_encoding(self) -> System.Text.Encoding:
        ...

    def get_hash_code(self) -> int:
        ...


class UTF8Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, encoder_should_emit_utf_8_identifier: bool) -> None:
        ...

    @overload
    def __init__(self, encoder_should_emit_utf_8_identifier: bool, throw_on_invalid_bytes: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class RunePosition(System.IEquatable[System_Text_RunePosition]):
    """This class has no documentation."""

    class Utf16Enumerator(System.Collections.Generic.IEnumerator[System_Text_RunePosition]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Text.RunePosition:
            ...

        def get_enumerator(self) -> System.Text.RunePosition.Utf16Enumerator:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    class Utf8Enumerator(System.Collections.Generic.IEnumerator[System_Text_RunePosition]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Text.RunePosition:
            ...

        def get_enumerator(self) -> System.Text.RunePosition.Utf8Enumerator:
            ...

        def move_next(self) -> bool:
            ...

        def reset(self) -> None:
            ...

    @property
    def rune(self) -> System.Text.Rune:
        ...

    @property
    def start_index(self) -> int:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def was_replaced(self) -> bool:
        ...

    def __eq__(self, right: System.Text.RunePosition) -> bool:
        ...

    def __init__(self, rune: System.Text.Rune, start_index: int, length: int, was_replaced: bool) -> None:
        ...

    def __ne__(self, right: System.Text.RunePosition) -> bool:
        ...

    @overload
    def deconstruct(self, rune: typing.Optional[System.Text.Rune], start_index: typing.Optional[int]) -> typing.Tuple[None, System.Text.Rune, int]:
        ...

    @overload
    def deconstruct(self, rune: typing.Optional[System.Text.Rune], start_index: typing.Optional[int], length: typing.Optional[int]) -> typing.Tuple[None, System.Text.Rune, int, int]:
        ...

    @staticmethod
    def enumerate_utf_16(span: System.ReadOnlySpan[str]) -> System.Text.RunePosition.Utf16Enumerator:
        ...

    @staticmethod
    def enumerate_utf_8(span: System.ReadOnlySpan[int]) -> System.Text.RunePosition.Utf8Enumerator:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Text.RunePosition) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class Ascii(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    def from_utf_16(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def is_valid(value: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(value: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(value: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_lower_in_place(value: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_lower_in_place(value: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper_in_place(value: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def to_upper_in_place(value: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    def to_utf_16(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        ...

    @staticmethod
    @overload
    def trim(value: System.ReadOnlySpan[int]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim(value: System.ReadOnlySpan[str]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_end(value: System.ReadOnlySpan[int]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_end(value: System.ReadOnlySpan[str]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_start(value: System.ReadOnlySpan[int]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_start(value: System.ReadOnlySpan[str]) -> System.Range:
        ...


class SpanRuneEnumerator(System.Collections.Generic.IEnumerator[System.Text.Rune]):
    """This class has no documentation."""

    @property
    def current(self) -> System.Text.Rune:
        ...

    def get_enumerator(self) -> System.Text.SpanRuneEnumerator:
        ...

    def move_next(self) -> bool:
        ...


class StringRuneEnumerator(System.Collections.Generic.IEnumerable[System.Text.Rune], System.Collections.Generic.IEnumerator[System.Text.Rune], typing.Iterable[System.Text.Rune]):
    """This class has no documentation."""

    @property
    def current(self) -> System.Text.Rune:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.Rune]:
        ...

    def get_enumerator(self) -> System.Text.StringRuneEnumerator:
        ...

    def move_next(self) -> bool:
        ...


class EncoderExceptionFallback(System.Text.EncoderFallback):
    """This class has no documentation."""

    @property
    def max_char_count(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class EncoderExceptionFallbackBuffer(System.Text.EncoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...


class EncoderFallbackException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def char_unknown(self) -> str:
        ...

    @property
    def char_unknown_high(self) -> str:
        ...

    @property
    def char_unknown_low(self) -> str:
        ...

    @property
    def index(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    def is_unknown_surrogate(self) -> bool:
        ...


class UnicodeEncoding(System.Text.Encoding):
    """This class has no documentation."""

    CHAR_SIZE: int = 2

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool, throw_on_invalid_bytes: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class UTF32Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool, throw_on_invalid_characters: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class ASCIIEncoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def is_single_byte(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_string(self, bytes: typing.List[int], byte_index: int, byte_count: int) -> str:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class DecoderReplacementFallback(System.Text.DecoderFallback):
    """This class has no documentation."""

    @property
    def default_string(self) -> str:
        ...

    @property
    def max_char_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, replacement: str) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DecoderReplacementFallbackBuffer(System.Text.DecoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self, fallback: System.Text.DecoderReplacementFallback) -> None:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class EncoderReplacementFallback(System.Text.EncoderFallback):
    """This class has no documentation."""

    @property
    def default_string(self) -> str:
        ...

    @property
    def max_char_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, replacement: str) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class EncoderReplacementFallbackBuffer(System.Text.EncoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self, fallback: System.Text.EncoderReplacementFallback) -> None:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DecoderExceptionFallback(System.Text.DecoderFallback):
    """This class has no documentation."""

    @property
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DecoderExceptionFallbackBuffer(System.Text.DecoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...


class DecoderFallbackException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def bytes_unknown(self) -> typing.List[int]:
        ...

    @property
    def index(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, bytes_unknown: typing.List[int], index: int) -> None:
        ...


class SpanLineEnumerator(System.Collections.Generic.IEnumerator[System.ReadOnlySpan[str]]):
    """This class has no documentation."""

    @property
    def current(self) -> System.ReadOnlySpan[str]:
        ...

    def get_enumerator(self) -> System.Text.SpanLineEnumerator:
        ...

    def move_next(self) -> bool:
        ...


