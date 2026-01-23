from typing import overload
from enum import IntEnum
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.Java


class JavaMarshal(System.Object):
    """This class has no documentation."""

    @staticmethod
    def create_reference_tracking_handle(obj: typing.Any, context: typing.Any) -> System.Runtime.InteropServices.GCHandle:
        ...

    @staticmethod
    def finish_cross_reference_processing(cross_references: typing.Any, unreachable_object_handles: System.ReadOnlySpan[System.Runtime.InteropServices.GCHandle]) -> None:
        ...

    @staticmethod
    def get_context(obj: System.Runtime.InteropServices.GCHandle) -> typing.Any:
        ...

    @staticmethod
    def initialize(mark_cross_references: typing.Any) -> None:
        ...


class StronglyConnectedComponent:
    """This class has no documentation."""

    @property
    def count(self) -> System.UIntPtr:
        ...

    @count.setter
    def count(self, value: System.UIntPtr) -> None:
        ...

    @property
    def contexts(self) -> typing.Any:
        ...

    @contexts.setter
    def contexts(self, value: typing.Any) -> None:
        ...


class MarkCrossReferencesArgs:
    """This class has no documentation."""

    @property
    def component_count(self) -> System.UIntPtr:
        ...

    @component_count.setter
    def component_count(self, value: System.UIntPtr) -> None:
        ...

    @property
    def components(self) -> typing.Any:
        ...

    @components.setter
    def components(self, value: typing.Any) -> None:
        ...

    @property
    def cross_reference_count(self) -> System.UIntPtr:
        ...

    @cross_reference_count.setter
    def cross_reference_count(self, value: System.UIntPtr) -> None:
        ...

    @property
    def cross_references(self) -> typing.Any:
        ...

    @cross_references.setter
    def cross_references(self, value: typing.Any) -> None:
        ...


class ComponentCrossReference:
    """This class has no documentation."""

    @property
    def source_group_index(self) -> System.UIntPtr:
        ...

    @source_group_index.setter
    def source_group_index(self, value: System.UIntPtr) -> None:
        ...

    @property
    def destination_group_index(self) -> System.UIntPtr:
        ...

    @destination_group_index.setter
    def destination_group_index(self, value: System.UIntPtr) -> None:
        ...


