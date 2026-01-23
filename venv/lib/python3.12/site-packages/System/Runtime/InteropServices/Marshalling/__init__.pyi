from typing import overload
from enum import IntEnum
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.Marshalling

System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T")
System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T")
System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_SpanMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SpanMarshaller_T")
System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T")
System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T")


class AnsiStringMarshaller(System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...


class MarshalMode(IntEnum):
    """This class has no documentation."""

    DEFAULT = 0

    MANAGED_TO_UNMANAGED_IN = 1

    MANAGED_TO_UNMANAGED_REF = 2

    MANAGED_TO_UNMANAGED_OUT = 3

    UNMANAGED_TO_MANAGED_IN = 4

    UNMANAGED_TO_MANAGED_REF = 5

    UNMANAGED_TO_MANAGED_OUT = 6

    ELEMENT_IN = 7

    ELEMENT_REF = 8

    ELEMENT_OUT = 9


class ReadOnlySpanMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T, System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement], System.Object):
    """This class has no documentation."""

    class UnmanagedToManagedOut(System.Object):
        """This class has no documentation."""

        @staticmethod
        def allocate_container_for_unmanaged_elements(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
            ...

        @staticmethod
        def get_managed_values_source(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            ...

        @staticmethod
        def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            ...

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]) -> None:
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]) -> typing.Any:
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    class ManagedToUnmanagedOut:
        """This class has no documentation."""

        def free(self) -> None:
            ...

        def from_unmanaged(self, unmanaged: typing.Any) -> None:
            ...

        def get_managed_values_destination(self, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            ...

        def get_unmanaged_values_source(self, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            ...

        def to_managed(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            ...


class ComVariant(System.IDisposable):
    """This class has no documentation."""

    NULL: System.Runtime.InteropServices.Marshalling.ComVariant

    @property
    def var_type(self) -> System.Runtime.InteropServices.VarEnum:
        ...

    def dispose(self) -> None:
        ...


class ArrayMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T, System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement], System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, array: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]) -> None:
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(array: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> typing.Any:
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...

    @staticmethod
    def get_managed_values_destination(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        ...

    @staticmethod
    def get_managed_values_source(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged_value: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
        ...


class CustomMarshallerAttribute(System.Attribute):
    """This class has no documentation."""

    class GenericPlaceholder:
        """This class has no documentation."""

    @property
    def managed_type(self) -> typing.Type:
        ...

    @property
    def marshal_mode(self) -> System.Runtime.InteropServices.Marshalling.MarshalMode:
        ...

    @property
    def marshaller_type(self) -> typing.Type:
        ...

    def __init__(self, managed_type: typing.Type, marshal_mode: System.Runtime.InteropServices.Marshalling.MarshalMode, marshaller_type: typing.Type) -> None:
        ...


class SpanMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T, System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement], System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]) -> None:
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> typing.Any:
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...

    @staticmethod
    def get_managed_values_destination(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        ...

    @staticmethod
    def get_managed_values_source(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
        ...


class NativeMarshallingAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def native_type(self) -> typing.Type:
        ...

    def __init__(self, native_type: typing.Type) -> None:
        ...


class BStrStringMarshaller(System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...


class PointerArrayMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T, System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement], System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, array: typing.List[typing.Any], buffer: System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]) -> None:
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System.IntPtr]:
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(array: typing.List[typing.Any]) -> typing.Any:
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> typing.List[typing.Any]:
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: typing.List[typing.Any], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...

    @staticmethod
    def get_managed_values_destination(managed: typing.List[typing.Any]) -> System.Span[System.IntPtr]:
        ...

    @staticmethod
    def get_managed_values_source(managed: typing.List[typing.Any]) -> System.ReadOnlySpan[System.IntPtr]:
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged_value: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
        ...


class SafeHandleMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T], System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        def free(self) -> None:
            ...

        def from_managed(self, handle: System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T) -> None:
            ...

        def to_unmanaged(self) -> System.IntPtr:
            ...

    class ManagedToUnmanagedRef:
        """This class has no documentation."""

        def __init__(self) -> None:
            ...

        def free(self) -> None:
            ...

        def from_managed(self, handle: System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T) -> None:
            ...

        def from_unmanaged(self, value: System.IntPtr) -> None:
            ...

        def on_invoked(self) -> None:
            ...

        def to_managed_finally(self) -> System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T:
            ...

        def to_unmanaged(self) -> System.IntPtr:
            ...

    class ManagedToUnmanagedOut:
        """This class has no documentation."""

        def __init__(self) -> None:
            ...

        def free(self) -> None:
            ...

        def from_unmanaged(self, value: System.IntPtr) -> None:
            ...

        def to_managed(self) -> System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T:
            ...


class Utf8StringMarshaller(System.Object):
    """This class has no documentation."""

    class ManagedToUnmanagedIn:
        """This class has no documentation."""

        BUFFER_SIZE: int

        def free(self) -> None:
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            ...

        def to_unmanaged(self) -> typing.Any:
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...


class MarshalUsingAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def native_type(self) -> typing.Type:
        ...

    @property
    def count_element_name(self) -> str:
        ...

    @count_element_name.setter
    def count_element_name(self, value: str) -> None:
        ...

    @property
    def constant_element_count(self) -> int:
        ...

    @constant_element_count.setter
    def constant_element_count(self, value: int) -> None:
        ...

    @property
    def element_indirection_depth(self) -> int:
        ...

    @element_indirection_depth.setter
    def element_indirection_depth(self, value: int) -> None:
        ...

    RETURNS_COUNT_VALUE: str = "return-value"

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, native_type: typing.Type) -> None:
        ...


class ContiguousCollectionMarshallerAttribute(System.Attribute):
    """This class has no documentation."""


class Utf16StringMarshaller(System.Object):
    """This class has no documentation."""

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        ...

    @staticmethod
    def get_pinnable_reference(str: str) -> typing.Any:
        ...


