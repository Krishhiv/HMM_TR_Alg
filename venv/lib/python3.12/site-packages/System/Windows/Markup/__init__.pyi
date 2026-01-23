from typing import overload
from enum import IntEnum
import typing

import System
import System.Windows.Markup


class ValueSerializerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value_serializer_type(self) -> typing.Type:
        ...

    @property
    def value_serializer_type_name(self) -> str:
        ...

    @overload
    def __init__(self, value_serializer_type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, value_serializer_type_name: str) -> None:
        ...


