from typing import overload
from enum import IntEnum
import typing

import System
import System.Collections.Generic
import System.Net
import System.Net.NetworkInformation


class IPAddressCollection(System.Object, System.Collections.Generic.ICollection[System.Net.IPAddress], typing.Iterable[System.Net.IPAddress]):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    def __getitem__(self, index: int) -> System.Net.IPAddress:
        ...

    def __iter__(self) -> typing.Iterator[System.Net.IPAddress]:
        ...

    def add(self, address: System.Net.IPAddress) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, address: System.Net.IPAddress) -> bool:
        ...

    def copy_to(self, array: typing.List[System.Net.IPAddress], offset: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Net.IPAddress]:
        ...

    def remove(self, address: System.Net.IPAddress) -> bool:
        ...


