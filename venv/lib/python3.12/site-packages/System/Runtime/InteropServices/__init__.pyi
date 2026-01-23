from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections
import System.Globalization
import System.Numerics
import System.Reflection
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ComTypes
import System.Runtime.Serialization
import System.Security

System_Runtime_InteropServices_GCHandle = typing.Any
System_Runtime_InteropServices_ArrayWithOffset = typing.Any
System_Runtime_InteropServices_CULong = typing.Any
System_Runtime_InteropServices_PinnedGCHandle = typing.Any
System_Runtime_InteropServices_WeakGCHandle = typing.Any
System_Runtime_InteropServices_OSPlatform = typing.Any
System_Runtime_InteropServices_NFloat = typing.Any
System_Runtime_InteropServices_CLong = typing.Any

System_Runtime_InteropServices_GCHandle_T = typing.TypeVar("System_Runtime_InteropServices_GCHandle_T")
System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup")
System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup")
System_Runtime_InteropServices_PinnedGCHandle_T = typing.TypeVar("System_Runtime_InteropServices_PinnedGCHandle_T")
System_Runtime_InteropServices_WeakGCHandle_T = typing.TypeVar("System_Runtime_InteropServices_WeakGCHandle_T")
System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup")


class GCHandleType(IntEnum):
    """This class has no documentation."""

    WEAK = 0

    WEAK_TRACK_RESURRECTION = 1

    NORMAL = 2

    PINNED = 3


class GCHandle(typing.Generic[System_Runtime_InteropServices_GCHandle_T], System.IEquatable[System_Runtime_InteropServices_GCHandle], System.IDisposable):
    """This class has no documentation."""

    @property
    def is_allocated(self) -> bool:
        ...

    @property
    def target(self) -> System_Runtime_InteropServices_GCHandle_T:
        ...

    @target.setter
    def target(self, value: System_Runtime_InteropServices_GCHandle_T) -> None:
        ...

    def __eq__(self, b: System.Runtime.InteropServices.GCHandle) -> bool:
        ...

    def __init__(self, target: System_Runtime_InteropServices_GCHandle_T) -> None:
        ...

    def __ne__(self, b: System.Runtime.InteropServices.GCHandle) -> bool:
        ...

    def addr_of_pinned_object(self) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def alloc(value: typing.Any) -> System.Runtime.InteropServices.GCHandle:
        ...

    @staticmethod
    @overload
    def alloc(value: typing.Any, type: System.Runtime.InteropServices.GCHandleType) -> System.Runtime.InteropServices.GCHandle:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.GCHandle) -> bool:
        ...

    def free(self) -> None:
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def to_int_ptr(value: System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def to_int_ptr(value: System.Runtime.InteropServices.GCHandle) -> System.IntPtr:
        ...


class LCIDConversionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, lcid: int) -> None:
        ...


class VariantWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class TypeMapAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup], System.Attribute):
    """This class has no documentation."""

    @overload
    def __init__(self, value: str, target: typing.Type) -> None:
        ...

    @overload
    def __init__(self, value: str, target: typing.Type, trim_target: typing.Type) -> None:
        ...


class ComVisibleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> bool:
        ...

    def __init__(self, visibility: bool) -> None:
        ...


class ExtendedLayoutKind(IntEnum):
    """This class has no documentation."""

    C_STRUCT = 0

    C_UNION = 1


class PosixSignal(IntEnum):
    """This class has no documentation."""

    SIGHUP = -1

    SIGINT = -2

    SIGQUIT = -3

    SIGTERM = -4

    SIGCHLD = -5

    SIGCONT = -6

    SIGWINCH = -7

    SIGTTIN = -8

    SIGTTOU = -9

    SIGTSTP = -10


class PosixSignalContext(System.Object):
    """This class has no documentation."""

    @property
    def signal(self) -> System.Runtime.InteropServices.PosixSignal:
        ...

    @property
    def cancel(self) -> bool:
        ...

    @cancel.setter
    def cancel(self, value: bool) -> None:
        ...

    def __init__(self, signal: System.Runtime.InteropServices.PosixSignal) -> None:
        ...


class PosixSignalRegistration(System.Object, System.IDisposable):
    """This class has no documentation."""

    @staticmethod
    def create(signal: System.Runtime.InteropServices.PosixSignal, handler: typing.Callable[[System.Runtime.InteropServices.PosixSignalContext], typing.Any]) -> System.Runtime.InteropServices.PosixSignalRegistration:
        ...

    def dispose(self) -> None:
        ...


class DefaultParameterValueAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    def __init__(self, value: typing.Any) -> None:
        ...


class CharSet(IntEnum):
    """This class has no documentation."""

    NONE = 1

    ANSI = 2

    UNICODE = 3

    AUTO = 4


class DefaultCharSetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    def __init__(self, char_set: System.Runtime.InteropServices.CharSet) -> None:
        ...


class ArrayWithOffset(System.IEquatable[System_Runtime_InteropServices_ArrayWithOffset]):
    """This class has no documentation."""

    def __eq__(self, b: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    def __init__(self, array: typing.Any, offset: int) -> None:
        ...

    def __ne__(self, b: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    def get_array(self) -> System.Object:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_offset(self) -> int:
        ...


class CustomQueryInterfaceResult(IntEnum):
    """This class has no documentation."""

    HANDLED = 0

    NOT_HANDLED = 1

    FAILED = 2


class TypeIdentifierAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def scope(self) -> str:
        ...

    @property
    def identifier(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, scope: str, identifier: str) -> None:
        ...


class CriticalHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        ...

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        ...

    @property
    def is_closed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_invalid(self) -> bool:
        ...

    def __init__(self, invalid_handle_value: System.IntPtr) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def release_handle(self) -> bool:
        ...

    def set_handle(self, handle: System.IntPtr) -> None:
        ...

    def set_handle_as_invalid(self) -> None:
        ...


class ExternalException(System.SystemException):
    """This class has no documentation."""

    @property
    def error_code(self) -> int:
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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def to_string(self) -> str:
        ...


class SEHException(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

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

    def can_resume(self) -> bool:
        ...


class LayoutKind(IntEnum):
    """This class has no documentation."""

    SEQUENTIAL = 0

    EXTENDED = 1

    EXPLICIT = 2

    AUTO = 3


class ComMemberType(IntEnum):
    """This class has no documentation."""

    METHOD = 0

    PROP_GET = 1

    PROP_SET = 2


class NativeMemory(System.Object):
    """This class has no documentation."""

    @staticmethod
    def aligned_alloc(byte_count: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    def aligned_free(ptr: typing.Any) -> None:
        ...

    @staticmethod
    def aligned_realloc(ptr: typing.Any, byte_count: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    @overload
    def alloc(byte_count: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    @overload
    def alloc(element_count: System.UIntPtr, element_size: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    @overload
    def alloc_zeroed(element_count: System.UIntPtr, element_size: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    @overload
    def alloc_zeroed(byte_count: System.UIntPtr) -> typing.Any:
        ...

    @staticmethod
    def clear(ptr: typing.Any, byte_count: System.UIntPtr) -> None:
        ...

    @staticmethod
    def copy(source: typing.Any, destination: typing.Any, byte_count: System.UIntPtr) -> None:
        ...

    @staticmethod
    def fill(ptr: typing.Any, byte_count: System.UIntPtr, value: int) -> None:
        ...

    @staticmethod
    def free(ptr: typing.Any) -> None:
        ...

    @staticmethod
    def realloc(ptr: typing.Any, byte_count: System.UIntPtr) -> typing.Any:
        ...


class CreateComInterfaceFlags(IntEnum):
    """This class has no documentation."""

    NONE = 0

    CALLER_DEFINED_I_UNKNOWN = 1

    TRACKER_SUPPORT = 2


class CreateObjectFlags(IntEnum):
    """This class has no documentation."""

    NONE = 0

    TRACKER_OBJECT = 1

    UNIQUE_INSTANCE = 2

    AGGREGATION = 4

    UNWRAP = 8


class CreatedWrapperFlags(IntEnum):
    """This class has no documentation."""

    NONE = 0

    TRACKER_OBJECT = 1

    NON_WRAPPING = ...


class ComWrappers(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class ComInterfaceEntry:
        """This class has no documentation."""

        @property
        def iid(self) -> System.Guid:
            ...

        @iid.setter
        def iid(self, value: System.Guid) -> None:
            ...

        @property
        def vtable(self) -> System.IntPtr:
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

        @property
        def iid(self) -> System.Guid:
            ...

        @iid.setter
        def iid(self, value: System.Guid) -> None:
            ...

        @property
        def vtable(self) -> System.IntPtr:
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

    class ComInterfaceDispatch:
        """This class has no documentation."""

        @property
        def vtable(self) -> System.IntPtr:
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

        @property
        def vtable(self) -> System.IntPtr:
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

    def compute_vtables(self, obj: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags, count: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        ...

    @overload
    def create_object(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, user_state: typing.Any, wrapper_flags: typing.Optional[System.Runtime.InteropServices.CreatedWrapperFlags]) -> typing.Tuple[System.Object, System.Runtime.InteropServices.CreatedWrapperFlags]:
        ...

    @overload
    def create_object(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        ...

    @staticmethod
    def get_i_unknown_impl(fp_query_interface: typing.Optional[System.IntPtr], fp_add_ref: typing.Optional[System.IntPtr], fp_release: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr, System.IntPtr, System.IntPtr]:
        ...

    def get_or_create_com_interface_for_object(self, instance: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags) -> System.IntPtr:
        ...

    @overload
    def get_or_create_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, user_state: typing.Any) -> System.Object:
        ...

    @overload
    def get_or_create_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        ...

    @overload
    def get_or_register_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any) -> System.Object:
        ...

    @overload
    def get_or_register_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any, inner: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def register_for_marshalling(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    @staticmethod
    def register_for_tracker_support(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    @staticmethod
    def try_get_com_instance(obj: typing.Any, unknown: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    def try_get_object(unknown: System.IntPtr, obj: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...


class CustomQueryInterfaceMode(IntEnum):
    """This class has no documentation."""

    IGNORE = 0

    ALLOW = 1


class SafeHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        ...

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        ...

    @property
    def is_closed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_invalid(self) -> bool:
        ...

    def __init__(self, invalid_handle_value: System.IntPtr, owns_handle: bool) -> None:
        ...

    def close(self) -> None:
        ...

    def dangerous_add_ref(self, success: bool) -> None:
        ...

    def dangerous_get_handle(self) -> System.IntPtr:
        ...

    def dangerous_release(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def release_handle(self) -> bool:
        ...

    def set_handle_as_invalid(self) -> None:
        ...


class Marshal(System.Object):
    """This class has no documentation."""

    SYSTEM_DEFAULT_CHAR_SIZE: int = 2

    SYSTEM_MAX_DBCS_CHAR_SIZE: int = ...

    @staticmethod
    def add_ref(p_unk: System.IntPtr) -> int:
        ...

    @staticmethod
    def alloc_co_task_mem(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def alloc_h_global(cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def alloc_h_global(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    def are_com_objects_available_for_cleanup() -> bool:
        ...

    @staticmethod
    def bind_to_moniker(moniker_name: str) -> System.Object:
        ...

    @staticmethod
    def change_wrapper_handle_strength(otp: typing.Any, f_is_weak: bool) -> None:
        ...

    @staticmethod
    def cleanup_unused_objects_in_current_context() -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[int], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[str], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[float], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[System.IntPtr], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[int], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[str], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[float], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[System.IntPtr], start_index: int, length: int) -> None:
        ...

    @staticmethod
    def create_aggregated_object(p_outer: System.IntPtr, o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def create_wrapper_of_type(o: typing.Any, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    def destroy_structure(ptr: System.IntPtr, structuretype: typing.Type) -> None:
        ...

    @staticmethod
    def final_release_com_object(o: typing.Any) -> int:
        ...

    @staticmethod
    def free_bstr(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    def free_co_task_mem(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    def free_h_global(hglobal: System.IntPtr) -> None:
        ...

    @staticmethod
    def generate_guid_for_type(type: typing.Type) -> System.Guid:
        ...

    @staticmethod
    def generate_prog_id_for_type(type: typing.Type) -> str:
        ...

    @staticmethod
    @overload
    def get_com_interface_for_object(o: typing.Any, t: typing.Type) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def get_com_interface_for_object(o: typing.Any, t: typing.Type, mode: System.Runtime.InteropServices.CustomQueryInterfaceMode) -> System.IntPtr:
        ...

    @staticmethod
    def get_com_object_data(obj: typing.Any, key: typing.Any) -> System.Object:
        ...

    @staticmethod
    def get_delegate_for_function_pointer(ptr: System.IntPtr, t: typing.Type) -> System.Delegate:
        ...

    @staticmethod
    def get_end_com_slot(t: typing.Type) -> int:
        ...

    @staticmethod
    def get_exception_code() -> int:
        warnings.warn("GetExceptionCode() may be unavailable in future releases.", DeprecationWarning)

    @staticmethod
    @overload
    def get_exception_for_hr(error_code: int) -> System.Exception:
        ...

    @staticmethod
    @overload
    def get_exception_for_hr(error_code: int, error_info: System.IntPtr) -> System.Exception:
        ...

    @staticmethod
    @overload
    def get_exception_for_hr(error_code: int, iid: System.Guid, p_unk: System.IntPtr) -> System.Exception:
        ...

    @staticmethod
    def get_exception_pointers() -> System.IntPtr:
        ...

    @staticmethod
    def get_function_pointer_for_delegate(d: System.Delegate) -> System.IntPtr:
        ...

    @staticmethod
    def get_hinstance(m: System.Reflection.Module) -> System.IntPtr:
        ...

    @staticmethod
    def get_hr_for_exception(e: System.Exception) -> int:
        ...

    @staticmethod
    def get_hr_for_last_win_32_error() -> int:
        ...

    @staticmethod
    def get_i_dispatch_for_object(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def get_i_unknown_for_object(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def get_last_p_invoke_error() -> int:
        ...

    @staticmethod
    def get_last_p_invoke_error_message() -> str:
        ...

    @staticmethod
    def get_last_system_error() -> int:
        ...

    @staticmethod
    def get_last_win_32_error() -> int:
        ...

    @staticmethod
    def get_native_variant_for_object(obj: typing.Any, p_dst_native_variant: System.IntPtr) -> None:
        ...

    @staticmethod
    def get_object_for_i_unknown(p_unk: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def get_object_for_native_variant(p_src_native_variant: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def get_objects_for_native_variants(a_src_native_variant: System.IntPtr, c_vars: int) -> typing.List[System.Object]:
        ...

    @staticmethod
    def get_p_invoke_error_message(error: int) -> str:
        ...

    @staticmethod
    def get_start_com_slot(t: typing.Type) -> int:
        ...

    @staticmethod
    def get_typed_object_for_i_unknown(p_unk: System.IntPtr, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_type_from_clsid(clsid: System.Guid) -> typing.Type:
        ...

    @staticmethod
    def get_type_info_name(type_info: System.Runtime.InteropServices.ComTypes.ITypeInfo) -> str:
        ...

    @staticmethod
    def get_unique_object_for_i_unknown(unknown: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def init_handle(safe_handle: System.Runtime.InteropServices.SafeHandle, handle: System.IntPtr) -> None:
        ...

    @staticmethod
    def is_com_object(o: typing.Any) -> bool:
        ...

    @staticmethod
    def is_type_visible_from_com(t: typing.Type) -> bool:
        ...

    @staticmethod
    def offset_of(t: typing.Type, field_name: str) -> System.IntPtr:
        ...

    @staticmethod
    def prelink(m: System.Reflection.MethodInfo) -> None:
        ...

    @staticmethod
    def prelink_all(c: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def ptr_to_string_ansi(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_ansi(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_auto(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_auto(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    def ptr_to_string_bstr(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_uni(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_uni(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_utf_8(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_utf_8(ptr: System.IntPtr, byte_len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_structure(ptr: System.IntPtr, structure: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def ptr_to_structure(ptr: System.IntPtr, structure_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def query_interface(p_unk: System.IntPtr, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Tuple[int, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: typing.Any, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: typing.Any, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: typing.Any, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: typing.Any, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: System.IntPtr, ofs: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: typing.Any, ofs: int) -> System.IntPtr:
        ...

    @staticmethod
    def re_alloc_co_task_mem(pv: System.IntPtr, cb: int) -> System.IntPtr:
        ...

    @staticmethod
    def re_alloc_h_global(pv: System.IntPtr, cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def release(p_unk: System.IntPtr) -> int:
        ...

    @staticmethod
    def release_com_object(o: typing.Any) -> int:
        ...

    @staticmethod
    def secure_string_to_bstr(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_co_task_mem_ansi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_co_task_mem_unicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_global_alloc_ansi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_global_alloc_unicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def set_com_object_data(obj: typing.Any, key: typing.Any, data: typing.Any) -> bool:
        ...

    @staticmethod
    def set_last_p_invoke_error(error: int) -> None:
        ...

    @staticmethod
    def set_last_system_error(error: int) -> None:
        ...

    @staticmethod
    @overload
    def size_of(structure: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def size_of(t: typing.Type) -> int:
        ...

    @staticmethod
    def string_to_bstr(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_ansi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_auto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_uni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_utf_8(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_ansi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_auto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_uni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def structure_to_ptr(structure: typing.Any, ptr: System.IntPtr, f_delete_old: bool) -> None:
        ...

    @staticmethod
    @overload
    def throw_exception_for_hr(error_code: int) -> None:
        ...

    @staticmethod
    @overload
    def throw_exception_for_hr(error_code: int, error_info: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def throw_exception_for_hr(error_code: int, iid: System.Guid, p_unk: System.IntPtr) -> None:
        ...

    @staticmethod
    def unsafe_addr_of_pinned_array_element(arr: System.Array, index: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def write_byte(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_byte(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_byte(ptr: typing.Any, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, ofs: int, val: str) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, val: str) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: typing.Any, ofs: int, val: str) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: typing.Any, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: typing.Any, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: typing.Any, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: System.IntPtr, ofs: int, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: System.IntPtr, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: typing.Any, ofs: int, val: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_bstr(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_ansi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_unicode(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_utf_8(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_global_alloc_ansi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_global_alloc_unicode(s: System.IntPtr) -> None:
        ...


class ClassInterfaceType(IntEnum):
    """This class has no documentation."""

    NONE = 0

    AUTO_DISPATCH = 1

    AUTO_DUAL = 2


class ClassInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.ClassInterfaceType:
        ...

    @overload
    def __init__(self, class_interface_type: System.Runtime.InteropServices.ClassInterfaceType) -> None:
        ...

    @overload
    def __init__(self, class_interface_type: int) -> None:
        ...


class VarEnum(IntEnum):
    """This class has no documentation."""

    VT_EMPTY = 0

    VT_NULL = 1

    VT_I_2 = 2

    VT_I_4 = 3

    VT_R_4 = 4

    VT_R_8 = 5

    VT_CY = 6

    VT_DATE = 7

    VT_BSTR = 8

    VT_DISPATCH = 9

    VT_ERROR = 10

    VT_BOOL = 11

    VT_VARIANT = 12

    VT_UNKNOWN = 13

    VT_DECIMAL = 14

    VT_I_1 = 16

    VT_UI_1 = 17

    VT_UI_2 = 18

    VT_UI_4 = 19

    VT_I_8 = 20

    VT_UI_8 = 21

    VT_INT = 22

    VT_UINT = 23

    VT_VOID = 24

    VT_HRESULT = 25

    VT_PTR = 26

    VT_SAFEARRAY = 27

    VT_CARRAY = 28

    VT_USERDEFINED = 29

    VT_LPSTR = 30

    VT_LPWSTR = 31

    VT_RECORD = 36

    VT_FILETIME = 64

    VT_BLOB = 65

    VT_STREAM = 66

    VT_STORAGE = 67

    VT_STREAMED_OBJECT = 68

    VT_STORED_OBJECT = 69

    VT_BLOB_OBJECT = 70

    VT_CF = 71

    VT_CLSID = 72

    VT_VECTOR = ...

    VT_ARRAY = ...

    VT_BYREF = ...


class CallingConvention(IntEnum):
    """This class has no documentation."""

    WINAPI = 1

    CDECL = 2

    STD_CALL = 3

    THIS_CALL = 4

    FAST_CALL = 5


class DllImportAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @property
    def entry_point(self) -> str:
        ...

    @entry_point.setter
    def entry_point(self, value: str) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    @property
    def set_last_error(self) -> bool:
        ...

    @set_last_error.setter
    def set_last_error(self, value: bool) -> None:
        ...

    @property
    def exact_spelling(self) -> bool:
        ...

    @exact_spelling.setter
    def exact_spelling(self, value: bool) -> None:
        ...

    @property
    def calling_convention(self) -> System.Runtime.InteropServices.CallingConvention:
        ...

    @calling_convention.setter
    def calling_convention(self, value: System.Runtime.InteropServices.CallingConvention) -> None:
        ...

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @best_fit_mapping.setter
    def best_fit_mapping(self, value: bool) -> None:
        ...

    @property
    def preserve_sig(self) -> bool:
        ...

    @preserve_sig.setter
    def preserve_sig(self, value: bool) -> None:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    def __init__(self, dll_name: str) -> None:
        ...


class OutAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CULong(System.IEquatable[System_Runtime_InteropServices_CULong]):
    """This class has no documentation."""

    @property
    def value(self) -> System.UIntPtr:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: System.UIntPtr) -> None:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.CULong) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class StandardOleMarshalObject(System.MarshalByRefObject, System.Runtime.InteropServices.IMarshal):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class BestFitMappingAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    def __init__(self, best_fit_mapping: bool) -> None:
        ...


class ICustomAdapter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_underlying_object(self) -> System.Object:
        ...


class ExtendedLayoutAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self, layout_kind: System.Runtime.InteropServices.ExtendedLayoutKind) -> None:
        ...


class ICustomFactory(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create_instance(self, server_type: typing.Type) -> System.MarshalByRefObject:
        ...


class StructLayoutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.LayoutKind:
        ...

    @property
    def pack(self) -> int:
        ...

    @pack.setter
    def pack(self, value: int) -> None:
        ...

    @property
    def size(self) -> int:
        ...

    @size.setter
    def size(self, value: int) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    @overload
    def __init__(self, layout_kind: System.Runtime.InteropServices.LayoutKind) -> None:
        ...

    @overload
    def __init__(self, layout_kind: int) -> None:
        ...


class ComEventsHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def combine(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> None:
        ...

    @staticmethod
    def remove(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> System.Delegate:
        ...


class DllImportSearchPath(IntEnum):
    """This class has no documentation."""

    USE_DLL_DIRECTORY_FOR_DEPENDENCIES = ...

    APPLICATION_DIRECTORY = ...

    USER_DIRECTORIES = ...

    SYSTEM_32 = ...

    SAFE_DIRECTORIES = ...

    ASSEMBLY_DIRECTORY = ...

    LEGACY_BEHAVIOR = ...


class NativeLibrary(System.Object):
    """This class has no documentation."""

    @staticmethod
    def free(handle: System.IntPtr) -> None:
        ...

    @staticmethod
    def get_export(handle: System.IntPtr, name: str) -> System.IntPtr:
        ...

    @staticmethod
    def get_main_program_handle() -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def load(library_path: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def load(library_name: str, assembly: System.Reflection.Assembly, search_path: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]) -> System.IntPtr:
        ...

    @staticmethod
    def set_dll_import_resolver(assembly: System.Reflection.Assembly, resolver: typing.Callable[[str, System.Reflection.Assembly, typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]], System.IntPtr]) -> None:
        ...

    @staticmethod
    def try_get_export(handle: System.IntPtr, name: str, address: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_load(library_path: str, handle: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_load(library_name: str, assembly: System.Reflection.Assembly, search_path: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath], handle: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...


class ComEventInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def source_interface(self) -> typing.Type:
        ...

    @property
    def event_provider(self) -> typing.Type:
        ...

    def __init__(self, source_interface: typing.Type, event_provider: typing.Type) -> None:
        ...


class WasmImportLinkageAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class TypeMapAssociationAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup], System.Attribute):
    """This class has no documentation."""

    def __init__(self, source: typing.Type, proxy: typing.Type) -> None:
        ...


class ComInterfaceType(IntEnum):
    """This class has no documentation."""

    INTERFACE_IS_DUAL = 0

    INTERFACE_IS_I_UNKNOWN = 1

    INTERFACE_IS_I_DISPATCH = 2

    INTERFACE_IS_I_INSPECTABLE = 3


class CurrencyWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> float:
        ...

    @overload
    def __init__(self, obj: typing.Any) -> None:
        ...

    @overload
    def __init__(self, obj: float) -> None:
        ...


class TypeMapping(System.Object):
    """This class has no documentation."""


class DefaultDllImportSearchPathsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def paths(self) -> System.Runtime.InteropServices.DllImportSearchPath:
        ...

    def __init__(self, paths: System.Runtime.InteropServices.DllImportSearchPath) -> None:
        ...


class Architecture(IntEnum):
    """This class has no documentation."""

    X_86 = 0

    X_64 = 1

    ARM = 2

    ARM_64 = 3

    WASM = 4

    S_390X = 5

    LOONG_ARCH_64 = 6

    ARMV_6 = 7

    PPC_64_LE = 8

    RISC_V_64 = 9


class OSPlatform(System.IEquatable[System_Runtime_InteropServices_OSPlatform]):
    """This class has no documentation."""

    FREE_BSD: System.Runtime.InteropServices.OSPlatform

    LINUX: System.Runtime.InteropServices.OSPlatform

    OSX: System.Runtime.InteropServices.OSPlatform

    WINDOWS: System.Runtime.InteropServices.OSPlatform

    def __eq__(self, right: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    def __ne__(self, right: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    @staticmethod
    def create(os_platform: str) -> System.Runtime.InteropServices.OSPlatform:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class RuntimeInformation(System.Object):
    """This class has no documentation."""

    RUNTIME_IDENTIFIER: str

    process_architecture: System.Runtime.InteropServices.Architecture

    OS_DESCRIPTION: str

    OS_ARCHITECTURE: System.Runtime.InteropServices.Architecture

    @staticmethod
    def is_os_platform(os_platform: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...


class ComDefaultInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> typing.Type:
        ...

    def __init__(self, default_interface: typing.Type) -> None:
        ...


class MemoryMarshal(System.Object):
    """This class has no documentation."""

    @staticmethod
    def create_read_only_span_from_null_terminated(value: typing.Any) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def get_array_data_reference(array: System.Array) -> typing.Any:
        ...

    @staticmethod
    def try_get_string(memory: System.ReadOnlyMemory[str], text: typing.Optional[str], start: typing.Optional[int], length: typing.Optional[int]) -> typing.Tuple[bool, str, int, int]:
        ...


class PinnedGCHandle(typing.Generic[System_Runtime_InteropServices_PinnedGCHandle_T], System.IEquatable[System_Runtime_InteropServices_PinnedGCHandle], System.IDisposable):
    """This class has no documentation."""

    @property
    def is_allocated(self) -> bool:
        ...

    @property
    def target(self) -> System_Runtime_InteropServices_PinnedGCHandle_T:
        ...

    @target.setter
    def target(self, value: System_Runtime_InteropServices_PinnedGCHandle_T) -> None:
        ...

    def __init__(self, target: System_Runtime_InteropServices_PinnedGCHandle_T) -> None:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]) -> bool:
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]:
        ...

    def get_address_of_object_data(self) -> typing.Any:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]) -> System.IntPtr:
        ...


class UnmanagedCallConvAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def call_convs(self) -> typing.List[typing.Type]:
        ...

    @call_convs.setter
    def call_convs(self, value: typing.List[typing.Type]) -> None:
        ...

    def __init__(self) -> None:
        ...


class WeakGCHandle(typing.Generic[System_Runtime_InteropServices_WeakGCHandle_T], System.IEquatable[System_Runtime_InteropServices_WeakGCHandle], System.IDisposable):
    """This class has no documentation."""

    @property
    def is_allocated(self) -> bool:
        ...

    def __init__(self, target: System_Runtime_InteropServices_WeakGCHandle_T, track_resurrection: bool = False) -> None:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]) -> bool:
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]:
        ...

    def get_hash_code(self) -> int:
        ...

    def set_target(self, target: System_Runtime_InteropServices_WeakGCHandle_T) -> None:
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]) -> System.IntPtr:
        ...

    def try_get_target(self, target: typing.Optional[System_Runtime_InteropServices_WeakGCHandle_T]) -> typing.Tuple[bool, System_Runtime_InteropServices_WeakGCHandle_T]:
        ...


class FieldOffsetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, offset: int) -> None:
        ...


class InAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class UnmanagedCallersOnlyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def call_convs(self) -> typing.List[typing.Type]:
        ...

    @call_convs.setter
    def call_convs(self, value: typing.List[typing.Type]) -> None:
        ...

    @property
    def entry_point(self) -> str:
        ...

    @entry_point.setter
    def entry_point(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...


class NFloat(System.Numerics.IBinaryFloatingPointIeee754[System_Runtime_InteropServices_NFloat], System.Numerics.IMinMaxValue[System_Runtime_InteropServices_NFloat], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    EPSILON: System.Runtime.InteropServices.NFloat

    MAX_VALUE: System.Runtime.InteropServices.NFloat

    MIN_VALUE: System.Runtime.InteropServices.NFloat

    NA_N: System.Runtime.InteropServices.NFloat

    NEGATIVE_INFINITY: System.Runtime.InteropServices.NFloat

    POSITIVE_INFINITY: System.Runtime.InteropServices.NFloat

    SIZE: int

    @property
    def value(self) -> float:
        ...

    E: System.Runtime.InteropServices.NFloat

    PI: System.Runtime.InteropServices.NFloat

    TAU: System.Runtime.InteropServices.NFloat

    NEGATIVE_ZERO: System.Runtime.InteropServices.NFloat

    def __add__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __eq__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    def __iadd__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __imod__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __imul__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __init__(self, value: float) -> None:
        ...

    def __isub__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __itruediv__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __le__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    def __mod__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __mul__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __ne__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    def __neg__(self) -> System.Runtime.InteropServices.NFloat:
        ...

    def __pos__(self) -> System.Runtime.InteropServices.NFloat:
        ...

    def __sub__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def __truediv__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def abs(value: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acos(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acosh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acos_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asin(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asinh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asin_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_2(y: System.Runtime.InteropServices.NFloat, x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_2_pi(y: System.Runtime.InteropServices.NFloat, x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atanh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def bit_decrement(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def bit_increment(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cbrt(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def ceiling(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def clamp(value: System.Runtime.InteropServices.NFloat, min: System.Runtime.InteropServices.NFloat, max: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def clamp_native(value: System.Runtime.InteropServices.NFloat, min: System.Runtime.InteropServices.NFloat, max: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, other: System.Runtime.InteropServices.NFloat) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.Runtime.InteropServices.NFloat, sign: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cos(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cosh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cos_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def exp(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_10(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_10_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_2(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_2_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def floor(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat, addend: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def hypot(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def ieee_754_remainder(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def i_log_b(x: System.Runtime.InteropServices.NFloat) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_finite(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_na_n(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_negative_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_normal(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_real_number(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_subnormal(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def lerp(value_1: System.Runtime.InteropServices.NFloat, value_2: System.Runtime.InteropServices.NFloat, amount: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def log(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def log(x: System.Runtime.InteropServices.NFloat, new_base: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_10(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_10_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_2(value: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_2_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_magnitude(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_magnitude_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_native(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_magnitude(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_magnitude_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_native(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat, addend: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def pow(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def reciprocal_estimate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def root_n(x: System.Runtime.InteropServices.NFloat, n: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, digits: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, mode: System.MidpointRounding) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, digits: int, mode: System.MidpointRounding) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def scale_b(x: System.Runtime.InteropServices.NFloat, n: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sign(value: System.Runtime.InteropServices.NFloat) -> int:
        ...

    @staticmethod
    def sin(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sin_cos(x: System.Runtime.InteropServices.NFloat) -> System.ValueTuple[System.Runtime.InteropServices.NFloat, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    def sin_cos_pi(x: System.Runtime.InteropServices.NFloat) -> System.ValueTuple[System.Runtime.InteropServices.NFloat, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    def sinh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sin_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sqrt(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tan(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tanh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tan_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def truncate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...


class CoClassAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def co_class(self) -> typing.Type:
        ...

    def __init__(self, co_class: typing.Type) -> None:
        ...


class ICustomMarshaler(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clean_up_managed_data(self, managed_obj: typing.Any) -> None:
        ...

    def clean_up_native_data(self, p_native_data: System.IntPtr) -> None:
        ...

    def get_native_data_size(self) -> int:
        ...

    def marshal_managed_to_native(self, managed_obj: typing.Any) -> System.IntPtr:
        ...

    def marshal_native_to_managed(self, p_native_data: System.IntPtr) -> System.Object:
        ...


class GCHandleExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_address_of_string_data(handle: System.Runtime.InteropServices.PinnedGCHandle[str]) -> typing.Any:
        ...


class InvalidOleVariantTypeException(System.SystemException):
    """This class has no documentation."""

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


class ComImportAttribute(System.Attribute):
    """This class has no documentation."""


class GuidAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    def __init__(self, guid: str) -> None:
        ...


class SafeBuffer(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def byte_length(self) -> int:
        ...

    def __init__(self, owns_handle: bool) -> None:
        ...

    def acquire_pointer(self, pointer: typing.Any) -> None:
        ...

    @overload
    def initialize(self, num_bytes: int) -> None:
        ...

    @overload
    def initialize(self, num_elements: int, size_of_each_element: int) -> None:
        ...

    def release_pointer(self) -> None:
        ...


class PreserveSigAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class HandleRef:
    """This class has no documentation."""

    @property
    def wrapper(self) -> System.Object:
        ...

    @property
    def handle(self) -> System.IntPtr:
        ...

    def __init__(self, wrapper: typing.Any, handle: System.IntPtr) -> None:
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.HandleRef) -> System.IntPtr:
        ...


class ProgIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    def __init__(self, prog_id: str) -> None:
        ...


class SafeArrayTypeMismatchException(System.SystemException):
    """This class has no documentation."""

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


class IDynamicInterfaceCastable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_interface_implementation(self, interface_type: System.RuntimeTypeHandle) -> System.RuntimeTypeHandle:
        ...

    def is_interface_implemented(self, interface_type: System.RuntimeTypeHandle, throw_if_not_implemented: bool) -> bool:
        ...


class DynamicInterfaceCastableImplementationAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DispatchWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class ComSourceInterfacesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @overload
    def __init__(self, source_interfaces: str) -> None:
        ...

    @overload
    def __init__(self, source_interface: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type, source_interface_3: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type, source_interface_3: typing.Type, source_interface_4: typing.Type) -> None:
        ...


class TypeMapAssemblyTargetAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup], System.Attribute):
    """This class has no documentation."""

    def __init__(self, assembly_name: str) -> None:
        ...


class CLong(System.IEquatable[System_Runtime_InteropServices_CLong]):
    """This class has no documentation."""

    @property
    def value(self) -> System.IntPtr:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: System.IntPtr) -> None:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.CLong) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class UnknownWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class UnmanagedType(IntEnum):
    """This class has no documentation."""

    BOOL = ...

    I_1 = ...

    U_1 = ...

    I_2 = ...

    U_2 = ...

    I_4 = ...

    U_4 = ...

    I_8 = ...

    U_8 = ...

    R_4 = ...

    R_8 = ...

    CURRENCY = ...

    B_STR = ...

    LP_STR = ...

    LPW_STR = ...

    LPT_STR = ...

    BY_VAL_T_STR = ...

    I_UNKNOWN = ...

    I_DISPATCH = ...

    STRUCT = ...

    INTERFACE = ...

    SAFE_ARRAY = ...

    BY_VAL_ARRAY = ...

    SYS_INT = ...

    SYS_U_INT = ...

    VB_BY_REF_STR = ...

    ANSI_B_STR = ...

    TB_STR = ...

    VARIANT_BOOL = ...

    FUNCTION_PTR = ...

    AS_ANY = ...

    LP_ARRAY = ...

    LP_STRUCT = ...

    CUSTOM_MARSHALER = ...

    ERROR = ...

    I_INSPECTABLE = ...

    H_STRING = ...

    LPUTF_8_STR = ...


class MarshalAsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.UnmanagedType:
        ...

    @property
    def safe_array_sub_type(self) -> System.Runtime.InteropServices.VarEnum:
        ...

    @safe_array_sub_type.setter
    def safe_array_sub_type(self, value: System.Runtime.InteropServices.VarEnum) -> None:
        ...

    @property
    def safe_array_user_defined_sub_type(self) -> typing.Type:
        ...

    @safe_array_user_defined_sub_type.setter
    def safe_array_user_defined_sub_type(self, value: typing.Type) -> None:
        ...

    @property
    def iid_parameter_index(self) -> int:
        ...

    @iid_parameter_index.setter
    def iid_parameter_index(self, value: int) -> None:
        ...

    @property
    def array_sub_type(self) -> System.Runtime.InteropServices.UnmanagedType:
        ...

    @array_sub_type.setter
    def array_sub_type(self, value: System.Runtime.InteropServices.UnmanagedType) -> None:
        ...

    @property
    def size_param_index(self) -> int:
        ...

    @size_param_index.setter
    def size_param_index(self, value: int) -> None:
        ...

    @property
    def size_const(self) -> int:
        ...

    @size_const.setter
    def size_const(self, value: int) -> None:
        ...

    @property
    def marshal_type(self) -> str:
        ...

    @marshal_type.setter
    def marshal_type(self, value: str) -> None:
        ...

    @property
    def marshal_type_ref(self) -> typing.Type:
        ...

    @marshal_type_ref.setter
    def marshal_type_ref(self, value: typing.Type) -> None:
        ...

    @property
    def marshal_cookie(self) -> str:
        ...

    @marshal_cookie.setter
    def marshal_cookie(self, value: str) -> None:
        ...

    @overload
    def __init__(self, unmanaged_type: System.Runtime.InteropServices.UnmanagedType) -> None:
        ...

    @overload
    def __init__(self, unmanaged_type: int) -> None:
        ...


class UnmanagedFunctionPointerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def calling_convention(self) -> System.Runtime.InteropServices.CallingConvention:
        ...

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @best_fit_mapping.setter
    def best_fit_mapping(self, value: bool) -> None:
        ...

    @property
    def set_last_error(self) -> bool:
        ...

    @set_last_error.setter
    def set_last_error(self, value: bool) -> None:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    def __init__(self, calling_convention: System.Runtime.InteropServices.CallingConvention) -> None:
        ...


class COMException(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def to_string(self) -> str:
        ...


class OptionalAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CollectionsMarshal(System.Object):
    """This class has no documentation."""

    @staticmethod
    def as_bytes(array: System.Collections.BitArray) -> System.Span[int]:
        ...


class SafeArrayRankMismatchException(System.SystemException):
    """This class has no documentation."""

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


class InvalidComObjectException(System.SystemException):
    """This class has no documentation."""

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


class InterfaceTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.ComInterfaceType:
        ...

    @overload
    def __init__(self, interface_type: System.Runtime.InteropServices.ComInterfaceType) -> None:
        ...

    @overload
    def __init__(self, interface_type: int) -> None:
        ...


class BStrWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> str:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...


class ErrorWrapper(System.Object):
    """This class has no documentation."""

    @property
    def error_code(self) -> int:
        ...

    @overload
    def __init__(self, error_code: typing.Any) -> None:
        ...

    @overload
    def __init__(self, error_code: int) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception) -> None:
        ...


class AllowReversePInvokeCallsAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class MarshalDirectiveException(System.SystemException):
    """This class has no documentation."""

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


class ICustomQueryInterface(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_interface(self, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Tuple[System.Runtime.InteropServices.CustomQueryInterfaceResult, System.IntPtr]:
        ...


class DispIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, disp_id: int) -> None:
        ...


class ImmutableCollectionsMarshal(System.Object):
    """This class has no documentation."""


