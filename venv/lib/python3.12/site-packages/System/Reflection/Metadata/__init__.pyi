from typing import overload
from enum import IntEnum
import typing

import System
import System.Reflection.Metadata


class MetadataUpdateHandlerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def handler_type(self) -> typing.Type:
        ...

    def __init__(self, handler_type: typing.Type) -> None:
        ...


