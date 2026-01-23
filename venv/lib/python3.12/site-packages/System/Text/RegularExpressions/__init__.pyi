from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.Reflection
import System.Reflection.Emit
import System.Runtime.Serialization
import System.Text.RegularExpressions


class RegexRunnerFactory(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class Capture(System.Object):
    """This class has no documentation."""

    @property
    def index(self) -> int:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def value(self) -> str:
        ...

    @property
    def value_span(self) -> System.ReadOnlySpan[str]:
        ...

    def to_string(self) -> str:
        ...


class CaptureCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Capture], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Capture], System.Collections.IList, typing.Iterable[System.Text.RegularExpressions.Capture]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    def __getitem__(self, i: int) -> System.Text.RegularExpressions.Capture:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.RegularExpressions.Capture]:
        ...

    @overload
    def copy_to(self, array: System.Array, array_index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System.Text.RegularExpressions.Capture], array_index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...


class Group(System.Text.RegularExpressions.Capture):
    """This class has no documentation."""

    @property
    def success(self) -> bool:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def captures(self) -> System.Text.RegularExpressions.CaptureCollection:
        ...

    @staticmethod
    def synchronized(inner: System.Text.RegularExpressions.Group) -> System.Text.RegularExpressions.Group:
        ...


class GroupCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Group], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Group], System.Collections.IList, System.Collections.Generic.IReadOnlyDictionary[str, System.Text.RegularExpressions.Group], typing.Iterable[System.Text.RegularExpressions.Group]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def keys(self) -> typing.Iterable[str]:
        ...

    @property
    def values(self) -> typing.Iterable[System.Text.RegularExpressions.Group]:
        ...

    def __contains__(self, key: str) -> bool:
        ...

    @overload
    def __getitem__(self, groupnum: int) -> System.Text.RegularExpressions.Group:
        ...

    @overload
    def __getitem__(self, groupname: str) -> System.Text.RegularExpressions.Group:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.RegularExpressions.Group]:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: str) -> bool:
        ...

    @overload
    def copy_to(self, array: System.Array, array_index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System.Text.RegularExpressions.Group], array_index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def try_get_value(self, key: str, value: typing.Optional[System.Text.RegularExpressions.Group]) -> typing.Tuple[bool, System.Text.RegularExpressions.Group]:
        ...


class Match(System.Text.RegularExpressions.Group):
    """This class has no documentation."""

    EMPTY: System.Text.RegularExpressions.Match

    @property
    def groups(self) -> System.Text.RegularExpressions.GroupCollection:
        ...

    def next_match(self) -> System.Text.RegularExpressions.Match:
        ...

    def result(self, replacement: str) -> str:
        ...

    @staticmethod
    def synchronized(inner: System.Text.RegularExpressions.Match) -> System.Text.RegularExpressions.Match:
        ...


class MatchCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Match], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Match], System.Collections.IList, typing.Iterable[System.Text.RegularExpressions.Match]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    def __getitem__(self, i: int) -> System.Text.RegularExpressions.Match:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.RegularExpressions.Match]:
        ...

    @overload
    def copy_to(self, array: System.Array, array_index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System.Text.RegularExpressions.Match], array_index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...


class RegexCompilationInfo(System.Object):
    """This class has no documentation."""

    @property
    def is_public(self) -> bool:
        ...

    @is_public.setter
    def is_public(self, value: bool) -> None:
        ...

    @property
    def match_timeout(self) -> datetime.timedelta:
        ...

    @match_timeout.setter
    def match_timeout(self, value: datetime.timedelta) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def namespace(self) -> str:
        ...

    @namespace.setter
    def namespace(self, value: str) -> None:
        ...

    @property
    def options(self) -> System.Text.RegularExpressions.RegexOptions:
        ...

    @options.setter
    def options(self, value: System.Text.RegularExpressions.RegexOptions) -> None:
        ...

    @property
    def pattern(self) -> str:
        ...

    @pattern.setter
    def pattern(self, value: str) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, name: str, fullnamespace: str, ispublic: bool) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, name: str, fullnamespace: str, ispublic: bool, match_timeout: datetime.timedelta) -> None:
        ...


class ValueMatch:
    """This class has no documentation."""

    @property
    def index(self) -> int:
        ...

    @property
    def length(self) -> int:
        ...


class Regex(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    class ValueSplitEnumerator(System.Collections.Generic.IEnumerator[System.Range]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Range:
            ...

        def get_enumerator(self) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
            ...

        def move_next(self) -> bool:
            ...

    class ValueMatchEnumerator(System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.ValueMatch]):
        """This class has no documentation."""

        @property
        def current(self) -> System.Text.RegularExpressions.ValueMatch:
            ...

        def get_enumerator(self) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
            ...

        def move_next(self) -> bool:
            ...

    cache_size: int

    @property
    def caps(self) -> System.Collections.IDictionary:
        ...

    @caps.setter
    def caps(self, value: System.Collections.IDictionary) -> None:
        ...

    @property
    def cap_names(self) -> System.Collections.IDictionary:
        ...

    @cap_names.setter
    def cap_names(self, value: System.Collections.IDictionary) -> None:
        ...

    @property
    def options(self) -> System.Text.RegularExpressions.RegexOptions:
        ...

    @property
    def right_to_left(self) -> bool:
        ...

    INFINITE_MATCH_TIMEOUT: datetime.timedelta = ...

    @property
    def match_timeout(self) -> datetime.timedelta:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, pattern: str) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    @overload
    def compile_to_assembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName) -> None:
        ...

    @staticmethod
    @overload
    def compile_to_assembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: typing.List[System.Reflection.Emit.CustomAttributeBuilder]) -> None:
        ...

    @staticmethod
    @overload
    def compile_to_assembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: typing.List[System.Reflection.Emit.CustomAttributeBuilder], resource_file: str) -> None:
        ...

    @overload
    def count(self, input: str) -> int:
        ...

    @overload
    def count(self, input: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def count(self, input: System.ReadOnlySpan[str], startat: int) -> int:
        ...

    @staticmethod
    @overload
    def count(input: str, pattern: str) -> int:
        ...

    @staticmethod
    @overload
    def count(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> int:
        ...

    @staticmethod
    @overload
    def count(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def count(input: System.ReadOnlySpan[str], pattern: str) -> int:
        ...

    @staticmethod
    @overload
    def count(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> int:
        ...

    @staticmethod
    @overload
    def count(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def enumerate_matches(input: System.ReadOnlySpan[str], pattern: str) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_matches(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_matches(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        ...

    @overload
    def enumerate_matches(self, input: System.ReadOnlySpan[str]) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        ...

    @overload
    def enumerate_matches(self, input: System.ReadOnlySpan[str], startat: int) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_splits(input: System.ReadOnlySpan[str], pattern: str) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_splits(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_splits(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @overload
    def enumerate_splits(self, input: System.ReadOnlySpan[str]) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @overload
    def enumerate_splits(self, input: System.ReadOnlySpan[str], count: int) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @overload
    def enumerate_splits(self, input: System.ReadOnlySpan[str], count: int, startat: int) -> System.Text.RegularExpressions.Regex.ValueSplitEnumerator:
        ...

    @staticmethod
    def escape(str: str) -> str:
        ...

    def get_group_names(self) -> typing.List[str]:
        ...

    def get_group_numbers(self) -> typing.List[int]:
        ...

    def group_name_from_number(self, i: int) -> str:
        ...

    def group_number_from_name(self, name: str) -> int:
        ...

    def initialize_references(self) -> None:
        warnings.warn("Obsoletions.RegexExtensibilityImplMessage", DeprecationWarning)

    @staticmethod
    @overload
    def is_match(input: str, pattern: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_match(input: System.ReadOnlySpan[str], pattern: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> bool:
        ...

    @staticmethod
    @overload
    def is_match(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> bool:
        ...

    @staticmethod
    @overload
    def is_match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def is_match(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def is_match(self, input: str) -> bool:
        ...

    @overload
    def is_match(self, input: str, startat: int) -> bool:
        ...

    @overload
    def is_match(self, input: System.ReadOnlySpan[str]) -> bool:
        ...

    @overload
    def is_match(self, input: System.ReadOnlySpan[str], startat: int) -> bool:
        ...

    @staticmethod
    @overload
    def match(input: str, pattern: str) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @overload
    def match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @overload
    def match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> System.Text.RegularExpressions.Match:
        ...

    @overload
    def match(self, input: str) -> System.Text.RegularExpressions.Match:
        ...

    @overload
    def match(self, input: str, startat: int) -> System.Text.RegularExpressions.Match:
        ...

    @overload
    def match(self, input: str, beginning: int, length: int) -> System.Text.RegularExpressions.Match:
        ...

    @staticmethod
    @overload
    def matches(input: str, pattern: str) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @overload
    def matches(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @overload
    def matches(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @overload
    def matches(self, input: str) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @overload
    def matches(self, input: str, startat: int) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, replacement: str) -> str:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, replacement: str, options: System.Text.RegularExpressions.RegexOptions) -> str:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, replacement: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> str:
        ...

    @overload
    def replace(self, input: str, replacement: str) -> str:
        ...

    @overload
    def replace(self, input: str, replacement: str, count: int) -> str:
        ...

    @overload
    def replace(self, input: str, replacement: str, count: int, startat: int) -> str:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str]) -> str:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], options: System.Text.RegularExpressions.RegexOptions) -> str:
        ...

    @staticmethod
    @overload
    def replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> str:
        ...

    @overload
    def replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str]) -> str:
        ...

    @overload
    def replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], count: int) -> str:
        ...

    @overload
    def replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], count: int, startat: int) -> str:
        ...

    @staticmethod
    @overload
    def split(input: str, pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def split(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def split(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout: datetime.timedelta) -> typing.List[str]:
        ...

    @overload
    def split(self, input: str) -> typing.List[str]:
        ...

    @overload
    def split(self, input: str, count: int) -> typing.List[str]:
        ...

    @overload
    def split(self, input: str, count: int, startat: int) -> typing.List[str]:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def unescape(str: str) -> str:
        ...

    def use_option_c(self) -> bool:
        warnings.warn("Obsoletions.RegexExtensibilityImplMessage", DeprecationWarning)

    def use_option_r(self) -> bool:
        warnings.warn("Obsoletions.RegexExtensibilityImplMessage", DeprecationWarning)


class GeneratedRegexAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def pattern(self) -> str:
        ...

    @property
    def options(self) -> System.Text.RegularExpressions.RegexOptions:
        ...

    @property
    def match_timeout_milliseconds(self) -> int:
        ...

    @property
    def culture_name(self) -> str:
        ...

    @overload
    def __init__(self, pattern: str) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, culture_name: str) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout_milliseconds: int) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, match_timeout_milliseconds: int, culture_name: str) -> None:
        ...


class RegexMatchTimeoutException(System.TimeoutException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def input(self) -> str:
        ...

    @property
    def pattern(self) -> str:
        ...

    @property
    def match_timeout(self) -> datetime.timedelta:
        ...

    @overload
    def __init__(self, regex_input: str, regex_pattern: str, match_timeout: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class RegexRunner(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def capture(self, capnum: int, start: int, end: int) -> None:
        ...

    @staticmethod
    def char_in_class(ch: str, char_class: str) -> bool:
        ...

    @staticmethod
    def char_in_set(ch: str, set: str, category: str) -> bool:
        warnings.warn("Obsoletions.RegexExtensibilityImplMessage", DeprecationWarning)

    def crawl(self, i: int) -> None:
        ...

    def crawlpos(self) -> int:
        ...

    def double_crawl(self) -> None:
        ...

    def double_stack(self) -> None:
        ...

    def double_track(self) -> None:
        ...

    def ensure_storage(self) -> None:
        ...

    def find_first_char(self) -> bool:
        ...

    def go(self) -> None:
        ...

    def init_track_count(self) -> None:
        ...

    def is_boundary(self, index: int, startpos: int, endpos: int) -> bool:
        ...

    def is_ecma_boundary(self, index: int, startpos: int, endpos: int) -> bool:
        ...

    def is_matched(self, cap: int) -> bool:
        ...

    def match_index(self, cap: int) -> int:
        ...

    def match_length(self, cap: int) -> int:
        ...

    def popcrawl(self) -> int:
        ...

    def scan(self, regex: System.Text.RegularExpressions.Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool) -> System.Text.RegularExpressions.Match:
        warnings.warn("Obsoletions.RegexExtensibilityImplMessage", DeprecationWarning)

    def transfer_capture(self, capnum: int, uncapnum: int, start: int, end: int) -> None:
        ...

    def uncapture(self) -> None:
        ...


