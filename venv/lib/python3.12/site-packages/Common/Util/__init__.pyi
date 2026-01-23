from typing import overload
from enum import IntEnum
import typing

import Common.Util
import QuantConnect
import System.Collections.Generic

Common_Util_ReadOnlyExtendedDictionary_TValue = typing.TypeVar("Common_Util_ReadOnlyExtendedDictionary_TValue")
Common_Util_ReadOnlyExtendedDictionary_TKey = typing.TypeVar("Common_Util_ReadOnlyExtendedDictionary_TKey")
Common_Util_BaseExtendedDictionary_TDictionary = typing.TypeVar("Common_Util_BaseExtendedDictionary_TDictionary")
Common_Util_BaseExtendedDictionary_TKey = typing.TypeVar("Common_Util_BaseExtendedDictionary_TKey")
Common_Util_BaseExtendedDictionary_TValue = typing.TypeVar("Common_Util_BaseExtendedDictionary_TValue")


class ReadOnlyExtendedDictionary(typing.Generic[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue], Common.Util.BaseExtendedDictionary[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    def __getitem__(self, key: Common_Util_ReadOnlyExtendedDictionary_TKey) -> Common_Util_ReadOnlyExtendedDictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, data: System.Collections.Generic.IEnumerable[Common_Util_ReadOnlyExtendedDictionary_TValue], key_selector: typing.Callable[[Common_Util_ReadOnlyExtendedDictionary_TValue], Common_Util_ReadOnlyExtendedDictionary_TKey]) -> None:
        ...

    def __setitem__(self, key: Common_Util_ReadOnlyExtendedDictionary_TKey, value: Common_Util_ReadOnlyExtendedDictionary_TValue) -> None:
        ...

    @overload
    def add(self, key: Common_Util_ReadOnlyExtendedDictionary_TKey, value: Common_Util_ReadOnlyExtendedDictionary_TValue) -> None:
        ...

    @overload
    def add(self, item: System.Collections.Generic.KeyValuePair[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue]) -> None:
        ...

    def clear(self) -> None:
        ...

    @overload
    def remove(self, key: Common_Util_ReadOnlyExtendedDictionary_TKey) -> bool:
        ...

    @overload
    def remove(self, item: System.Collections.Generic.KeyValuePair[Common_Util_ReadOnlyExtendedDictionary_TKey, Common_Util_ReadOnlyExtendedDictionary_TValue]) -> bool:
        ...


class BaseExtendedDictionary(typing.Generic[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue, Common_Util_BaseExtendedDictionary_TDictionary], QuantConnect.ExtendedDictionary[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue], System.Collections.Generic.IDictionary[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]]):
    """This class has no documentation."""

    @property
    def dictionary(self) -> Common_Util_BaseExtendedDictionary_TDictionary:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def get_keys(self) -> typing.Iterable[Common_Util_BaseExtendedDictionary_TKey]:
        ...

    @property
    def get_values(self) -> typing.Iterable[Common_Util_BaseExtendedDictionary_TValue]:
        ...

    def __contains__(self, key: Common_Util_BaseExtendedDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: Common_Util_BaseExtendedDictionary_TKey) -> Common_Util_BaseExtendedDictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, dictionary: Common_Util_BaseExtendedDictionary_TDictionary) -> None:
        ...

    @overload
    def __init__(self, data: System.Collections.Generic.IEnumerable[Common_Util_BaseExtendedDictionary_TValue], key_selector: typing.Callable[[Common_Util_BaseExtendedDictionary_TValue], Common_Util_BaseExtendedDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: Common_Util_BaseExtendedDictionary_TKey, value: Common_Util_BaseExtendedDictionary_TValue) -> None:
        ...

    @overload
    def add(self, key: Common_Util_BaseExtendedDictionary_TKey, value: Common_Util_BaseExtendedDictionary_TValue) -> None:
        ...

    @overload
    def add(self, item: System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]) -> bool:
        ...

    def contains_key(self, key: Common_Util_BaseExtendedDictionary_TKey) -> bool:
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]], array_index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]]:
        ...

    def get_items(self) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]]:
        ...

    @overload
    def remove(self, key: Common_Util_BaseExtendedDictionary_TKey) -> bool:
        ...

    @overload
    def remove(self, item: System.Collections.Generic.KeyValuePair[Common_Util_BaseExtendedDictionary_TKey, Common_Util_BaseExtendedDictionary_TValue]) -> bool:
        ...

    def try_get_value(self, key: Common_Util_BaseExtendedDictionary_TKey, value: typing.Optional[Common_Util_BaseExtendedDictionary_TValue]) -> typing.Tuple[bool, Common_Util_BaseExtendedDictionary_TValue]:
        ...


