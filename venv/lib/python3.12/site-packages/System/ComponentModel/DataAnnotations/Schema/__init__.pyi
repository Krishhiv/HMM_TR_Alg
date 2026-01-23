from typing import overload
from enum import IntEnum
import typing

import System
import System.ComponentModel.DataAnnotations.Schema


class InversePropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def property(self) -> str:
        ...

    def __init__(self, property: str) -> None:
        ...


class ForeignKeyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    def __init__(self, name: str) -> None:
        ...


class ComplexTypeAttribute(System.Attribute):
    """This class has no documentation."""


class DatabaseGeneratedOption(IntEnum):
    """This class has no documentation."""

    NONE = 0

    IDENTITY = 1

    COMPUTED = 2


class DatabaseGeneratedAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def database_generated_option(self) -> System.ComponentModel.DataAnnotations.Schema.DatabaseGeneratedOption:
        ...

    def __init__(self, database_generated_option: System.ComponentModel.DataAnnotations.Schema.DatabaseGeneratedOption) -> None:
        ...


class ColumnAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def order(self) -> int:
        ...

    @order.setter
    def order(self, value: int) -> None:
        ...

    @property
    def type_name(self) -> str:
        ...

    @type_name.setter
    def type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...


class NotMappedAttribute(System.Attribute):
    """This class has no documentation."""


class TableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def schema(self) -> str:
        ...

    @schema.setter
    def schema(self, value: str) -> None:
        ...

    def __init__(self, name: str) -> None:
        ...


