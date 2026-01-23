from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import System
import System.Buffers
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.ComponentModel
import System.Configuration.Assemblies
import System.Globalization
import System.IO
import System.Numerics
import System.Reflection
import System.Runtime.CompilerServices
import System.Runtime.ExceptionServices
import System.Runtime.InteropServices
import System.Runtime.Remoting
import System.Runtime.Serialization
import System.Security
import System.Security.Principal
import System.Text
import System.Threading
import System.Threading.Tasks

System_TimeZoneInfo = typing.Any
System_TimeZoneInfo_AdjustmentRule = typing.Any
System_TimeZoneInfo_TransitionTime = typing.Any
System_DateTimeOffset = typing.Any
System_Lazy = typing.Any
System_UIntPtr = typing.Any
System_Memory = typing.Any
System_Int128 = typing.Any
System_Half = typing.Any
System_UInt128 = typing.Any
System_DateOnly = typing.Any
System_Guid = typing.Any
System_IntPtr = typing.Any
System_ReadOnlyMemory = typing.Any
System_ValueTuple = typing.Any
System_Version = typing.Any
System_TimeOnly = typing.Any
System_ConsoleKeyInfo = typing.Any

System_ISpanParsable_TSelf = typing.TypeVar("System_ISpanParsable_TSelf")
System_Span_T = typing.TypeVar("System_Span_T")
System_IObserver_T = typing.TypeVar("System_IObserver_T")
System_IParsable_TSelf = typing.TypeVar("System_IParsable_TSelf")
System_IProgress_T = typing.TypeVar("System_IProgress_T")
System_Lazy_T = typing.TypeVar("System_Lazy_T")
System_Lazy_TMetadata = typing.TypeVar("System_Lazy_TMetadata")
System_Delegate_InvocationListEnumerator_TDelegate = typing.TypeVar("System_Delegate_InvocationListEnumerator_TDelegate")
System_Nullable_T = typing.TypeVar("System_Nullable_T")
System_ReadOnlySpan_T = typing.TypeVar("System_ReadOnlySpan_T")
System_MemoryExtensions_SpanSplitEnumerator_T = typing.TypeVar("System_MemoryExtensions_SpanSplitEnumerator_T")
System_WeakReference_T = typing.TypeVar("System_WeakReference_T")
System_Memory_T = typing.TypeVar("System_Memory_T")
System_Progress_T = typing.TypeVar("System_Progress_T")
System_ReadOnlyMemory_T = typing.TypeVar("System_ReadOnlyMemory_T")
System_IObservable_T = typing.TypeVar("System_IObservable_T")
System_Tuple_T1 = typing.TypeVar("System_Tuple_T1")
System_Tuple_T2 = typing.TypeVar("System_Tuple_T2")
System_Tuple_T3 = typing.TypeVar("System_Tuple_T3")
System_Tuple_T4 = typing.TypeVar("System_Tuple_T4")
System_Tuple_T5 = typing.TypeVar("System_Tuple_T5")
System_Tuple_T6 = typing.TypeVar("System_Tuple_T6")
System_Tuple_T7 = typing.TypeVar("System_Tuple_T7")
System_Tuple_TRest = typing.TypeVar("System_Tuple_TRest")
System_ValueTuple_T1 = typing.TypeVar("System_ValueTuple_T1")
System_ValueTuple_T2 = typing.TypeVar("System_ValueTuple_T2")
System_ValueTuple_T3 = typing.TypeVar("System_ValueTuple_T3")
System_ValueTuple_T4 = typing.TypeVar("System_ValueTuple_T4")
System_ValueTuple_T5 = typing.TypeVar("System_ValueTuple_T5")
System_ValueTuple_T6 = typing.TypeVar("System_ValueTuple_T6")
System_ValueTuple_T7 = typing.TypeVar("System_ValueTuple_T7")
System_ValueTuple_TRest = typing.TypeVar("System_ValueTuple_TRest")
System_IUtf8SpanParsable_TSelf = typing.TypeVar("System_IUtf8SpanParsable_TSelf")
System_IEquatable_T = typing.TypeVar("System_IEquatable_T")
System_ArraySegment_T = typing.TypeVar("System_ArraySegment_T")
System_IComparable_T = typing.TypeVar("System_IComparable_T")
System__EventContainer_Callable = typing.TypeVar("System__EventContainer_Callable")
System__EventContainer_ReturnType = typing.TypeVar("System__EventContainer_ReturnType")


class Object:
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def equals(obj_a: typing.Any, obj_b: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type(self) -> typing.Type:
        ...

    def memberwise_clone(self) -> System.Object:
        ...

    @staticmethod
    def reference_equals(obj_a: typing.Any, obj_b: typing.Any) -> bool:
        ...

    def to_string(self) -> str:
        ...


class Exception(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def data(self) -> System.Collections.IDictionary:
        ...

    @property
    def inner_exception(self) -> System.Exception:
        ...

    @property
    def help_link(self) -> str:
        ...

    @help_link.setter
    def help_link(self, value: str) -> None:
        ...

    @property
    def source(self) -> str:
        ...

    @source.setter
    def source(self, value: str) -> None:
        ...

    @property
    def serialize_object_state(self) -> _EventContainer[typing.Callable[[System.Object, System.Runtime.Serialization.SafeSerializationEventArgs], typing.Any], typing.Any]:
        warnings.warn("Obsoletions.BinaryFormatterMessage", DeprecationWarning)

    @serialize_object_state.setter
    def serialize_object_state(self, value: _EventContainer[typing.Callable[[System.Object, System.Runtime.Serialization.SafeSerializationEventArgs], typing.Any], typing.Any]) -> None:
        warnings.warn("Obsoletions.BinaryFormatterMessage", DeprecationWarning)

    @property
    def h_result(self) -> int:
        ...

    @h_result.setter
    def h_result(self, value: int) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        ...

    @property
    def target_site(self) -> System.Reflection.MethodBase:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_base_exception(self) -> System.Exception:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_type(self) -> typing.Type:
        ...

    def to_string(self) -> str:
        ...


class SystemException(System.Exception):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class InvalidOperationException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectDisposedException(System.InvalidOperationException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def object_name(self) -> str:
        ...

    @overload
    def __init__(self, object_name: str) -> None:
        ...

    @overload
    def __init__(self, object_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    @overload
    def throw_if(condition: bool, instance: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def throw_if(condition: bool, type: typing.Type) -> None:
        ...


class ISpanParsable(typing.Generic[System_ISpanParsable_TSelf], System.IParsable[System_ISpanParsable_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IFormatProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...


class IFormattable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...


class ISpanFormattable(System.IFormattable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        ...


class IUtf8SpanFormattable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        ...


class TypeCode(IntEnum):
    """This class has no documentation."""

    EMPTY = 0

    OBJECT = 1

    DB_NULL = 2

    BOOLEAN = 3

    CHAR = 4

    S_BYTE = 5

    BYTE = 6

    INT_16 = 7

    U_INT_16 = 8

    INT_32 = 9

    U_INT_32 = 10

    INT_64 = 11

    U_INT_64 = 12

    SINGLE = 13

    DOUBLE = 14

    DECIMAL = 15

    DATE_TIME = 16

    STRING = 18


class IConvertible(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_type_code(self) -> System.TypeCode:
        ...

    def to_boolean(self, provider: System.IFormatProvider) -> bool:
        ...

    def to_byte(self, provider: System.IFormatProvider) -> int:
        ...

    def to_char(self, provider: System.IFormatProvider) -> str:
        ...

    def to_date_time(self, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    def to_decimal(self, provider: System.IFormatProvider) -> float:
        ...

    def to_double(self, provider: System.IFormatProvider) -> float:
        ...

    def to_int_16(self, provider: System.IFormatProvider) -> int:
        ...

    def to_int_32(self, provider: System.IFormatProvider) -> int:
        ...

    def to_int_64(self, provider: System.IFormatProvider) -> int:
        ...

    def to_s_byte(self, provider: System.IFormatProvider) -> int:
        ...

    def to_single(self, provider: System.IFormatProvider) -> float:
        ...

    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    def to_type(self, conversion_type: typing.Type, provider: System.IFormatProvider) -> System.Object:
        ...

    def to_u_int_16(self, provider: System.IFormatProvider) -> int:
        ...

    def to_u_int_32(self, provider: System.IFormatProvider) -> int:
        ...

    def to_u_int_64(self, provider: System.IFormatProvider) -> int:
        ...


class ICloneable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self) -> System.Object:
        ...


class Array(System.Object, System.ICloneable, System.Collections.IList, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def is_fixed_size(self) -> bool:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    MAX_LENGTH: int

    @property
    def length(self) -> int:
        ...

    @property
    def long_length(self) -> int:
        ...

    @property
    def rank(self) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, index: int, length: int, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, index: int, length: int, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    @staticmethod
    @overload
    def clear(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def clear(array: System.Array, index: int, length: int) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    def constrained_copy(source_array: System.Array, source_index: int, destination_array: System.Array, destination_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source_array: System.Array, destination_array: System.Array, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source_array: System.Array, source_index: int, destination_array: System.Array, destination_index: int, length: int) -> None:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length_1: int, length_2: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length_1: int, length_2: int, length_3: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, *lengths: typing.Union[int, typing.Iterable[int]]) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, lengths: typing.List[int], lower_bounds: typing.List[int]) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, length: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, *lengths: typing.Union[int, typing.Iterable[int]]) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, lengths: typing.List[int], lower_bounds: typing.List[int]) -> System.Array:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_length(self, dimension: int) -> int:
        ...

    def get_long_length(self, dimension: int) -> int:
        ...

    def get_lower_bound(self, dimension: int) -> int:
        ...

    def get_upper_bound(self, dimension: int) -> int:
        ...

    @overload
    def get_value(self, *indices: typing.Union[int, typing.Iterable[int]]) -> System.Object:
        ...

    @overload
    def get_value(self, index: int) -> System.Object:
        ...

    @overload
    def get_value(self, index_1: int, index_2: int) -> System.Object:
        ...

    @overload
    def get_value(self, index_1: int, index_2: int, index_3: int) -> System.Object:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any, start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any, start_index: int, count: int) -> int:
        ...

    def initialize(self) -> None:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any, start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any, start_index: int, count: int) -> int:
        ...

    @staticmethod
    @overload
    def reverse(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def reverse(array: System.Array, index: int, length: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index_1: int, index_2: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index_1: int, index_2: int, index_3: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, *indices: typing.Union[int, typing.Iterable[int]]) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, index: int, length: int, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, index: int, length: int, comparer: System.Collections.IComparer) -> None:
        ...


class Enum(System.Object, System.IComparable, System.ISpanFormattable, System.IConvertible, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __ge__(self, other: typing.Any) -> bool:
        ...

    def __gt__(self, other: typing.Any) -> bool:
        ...

    def __le__(self, other: typing.Any) -> bool:
        ...

    def __lt__(self, other: typing.Any) -> bool:
        ...

    def compare_to(self, target: typing.Any) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    def format(enum_type: typing.Type, value: typing.Any, format: str) -> str:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_name(enum_type: typing.Type, value: typing.Any) -> str:
        ...

    @staticmethod
    def get_names(enum_type: typing.Type) -> typing.List[str]:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def get_underlying_type(enum_type: typing.Type) -> typing.Type:
        ...

    @staticmethod
    def get_values(enum_type: typing.Type) -> System.Array:
        ...

    @staticmethod
    def get_values_as_underlying_type(enum_type: typing.Type) -> System.Array:
        ...

    def has_flag(self, flag: System.Enum) -> bool:
        ...

    @staticmethod
    def is_defined(enum_type: typing.Type, value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: str) -> System.Object:
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: System.ReadOnlySpan[str]) -> System.Object:
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: str, ignore_case: bool) -> System.Object:
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], ignore_case: bool) -> System.Object:
        ...

    @staticmethod
    @overload
    def to_object(enum_type: typing.Type, value: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def to_object(enum_type: typing.Type, value: int) -> System.Object:
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
    @overload
    def try_parse(enum_type: typing.Type, value: str, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: str, ignore_case: bool, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], ignore_case: bool, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...


class DayOfWeek(IntEnum):
    """This class has no documentation."""

    SUNDAY = 0

    MONDAY = 1

    TUESDAY = 2

    WEDNESDAY = 3

    THURSDAY = 4

    FRIDAY = 5

    SATURDAY = 6


class TimeOnly(System.IComparable[System_TimeOnly], System.IEquatable[System_TimeOnly], System.ISpanFormattable, System.ISpanParsable[System_TimeOnly], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    MIN_VALUE: System.TimeOnly

    MAX_VALUE: System.TimeOnly

    @property
    def hour(self) -> int:
        ...

    @property
    def minute(self) -> int:
        ...

    @property
    def second(self) -> int:
        ...

    @property
    def millisecond(self) -> int:
        ...

    @property
    def microsecond(self) -> int:
        ...

    @property
    def nanosecond(self) -> int:
        ...

    @property
    def ticks(self) -> int:
        ...

    def __eq__(self, right: System.TimeOnly) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.TimeOnly) -> bool:
        ...

    @overload
    def __ge__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.TimeOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __init__(self, hour: int, minute: int) -> None:
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int) -> None:
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int, millisecond: int) -> None:
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int, millisecond: int, microsecond: int) -> None:
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        ...

    def __isub__(self, t_2: System.TimeOnly) -> datetime.timedelta:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.TimeOnly) -> bool:
        ...

    @overload
    def __le__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.TimeOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: System.TimeOnly) -> bool:
        ...

    def __ne__(self, right: System.TimeOnly) -> bool:
        ...

    def __sub__(self, t_2: System.TimeOnly) -> datetime.timedelta:
        ...

    @overload
    def add(self, value: datetime.timedelta) -> System.TimeOnly:
        ...

    @overload
    def add(self, value: datetime.timedelta, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        ...

    @overload
    def add_hours(self, value: float) -> System.TimeOnly:
        ...

    @overload
    def add_hours(self, value: float, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        ...

    @overload
    def add_minutes(self, value: float) -> System.TimeOnly:
        ...

    @overload
    def add_minutes(self, value: float, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.TimeOnly) -> int:
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int], millisecond: typing.Optional[int]) -> typing.Tuple[None, int, int, int, int]:
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int], millisecond: typing.Optional[int], microsecond: typing.Optional[int]) -> typing.Tuple[None, int, int, int, int, int]:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: System.TimeOnly) -> bool:
        ...

    @staticmethod
    def from_date_time(date_time: typing.Union[datetime.datetime, datetime.date]) -> System.TimeOnly:
        ...

    @staticmethod
    def from_time_span(time_span: datetime.timedelta) -> System.TimeOnly:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_between(self, start: System.TimeOnly, end: System.TimeOnly) -> bool:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str]) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str]) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        ...

    def to_long_time_string(self) -> str:
        ...

    def to_short_time_string(self) -> str:
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

    def to_time_span(self) -> datetime.timedelta:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...


class DateTimeKind(IntEnum):
    """This class has no documentation."""

    UNSPECIFIED = 0

    UTC = 1

    LOCAL = 2


class DateOnly(System.IComparable[System_DateOnly], System.IEquatable[System_DateOnly], System.ISpanFormattable, System.ISpanParsable[System_DateOnly], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    MIN_VALUE: System.DateOnly

    MAX_VALUE: System.DateOnly

    @property
    def year(self) -> int:
        ...

    @property
    def month(self) -> int:
        ...

    @property
    def day(self) -> int:
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        ...

    @property
    def day_of_year(self) -> int:
        ...

    @property
    def day_number(self) -> int:
        ...

    def __eq__(self, right: System.DateOnly) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.DateOnly) -> bool:
        ...

    @overload
    def __ge__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.DateOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.DateOnly) -> bool:
        ...

    @overload
    def __le__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.DateOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: System.DateOnly) -> bool:
        ...

    def __ne__(self, right: System.DateOnly) -> bool:
        ...

    def add_days(self, value: int) -> System.DateOnly:
        ...

    def add_months(self, value: int) -> System.DateOnly:
        ...

    def add_years(self, value: int) -> System.DateOnly:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.DateOnly) -> int:
        ...

    def deconstruct(self, year: typing.Optional[int], month: typing.Optional[int], day: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: System.DateOnly) -> bool:
        ...

    @staticmethod
    def from_date_time(date_time: typing.Union[datetime.datetime, datetime.date]) -> System.DateOnly:
        ...

    @staticmethod
    def from_day_number(day_number: int) -> System.DateOnly:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str]) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str]) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        ...

    @overload
    def to_date_time(self, time: System.TimeOnly) -> datetime.datetime:
        ...

    @overload
    def to_date_time(self, time: System.TimeOnly, kind: System.DateTimeKind) -> datetime.datetime:
        ...

    def to_long_date_string(self) -> str:
        ...

    def to_short_date_string(self) -> str:
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

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...


class DateTimeOffset(System.IComparable[System_DateTimeOffset], System.ISpanFormattable, System.IEquatable[System_DateTimeOffset], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ISpanParsable[System_DateTimeOffset], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    MIN_VALUE: System.DateTimeOffset

    MAX_VALUE: System.DateTimeOffset = ...

    UNIX_EPOCH: System.DateTimeOffset = ...

    UTC_NOW: System.DateTimeOffset

    @property
    def date_time(self) -> datetime.datetime:
        ...

    @property
    def utc_date_time(self) -> datetime.datetime:
        ...

    @property
    def local_date_time(self) -> datetime.datetime:
        ...

    @property
    def date(self) -> datetime.datetime:
        ...

    @property
    def day(self) -> int:
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        ...

    @property
    def day_of_year(self) -> int:
        ...

    @property
    def hour(self) -> int:
        ...

    @property
    def millisecond(self) -> int:
        ...

    @property
    def microsecond(self) -> int:
        ...

    @property
    def nanosecond(self) -> int:
        ...

    @property
    def minute(self) -> int:
        ...

    @property
    def month(self) -> int:
        ...

    @property
    def offset(self) -> datetime.timedelta:
        ...

    @property
    def total_offset_minutes(self) -> int:
        ...

    @property
    def second(self) -> int:
        ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def utc_ticks(self) -> int:
        ...

    @property
    def time_of_day(self) -> datetime.timedelta:
        ...

    @property
    def year(self) -> int:
        ...

    NOW: System.DateTimeOffset

    def __add__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def __eq__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __ge__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __ge__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __gt__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __gt__(self, right: System.DateTimeOffset) -> bool:
        ...

    def __iadd__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __init__(self, ticks: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @overload
    def __init__(self, date_time: typing.Union[datetime.datetime, datetime.date], offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __isub__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __isub__(self, right: System.DateTimeOffset) -> datetime.timedelta:
        ...

    @overload
    def __le__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __le__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __lt__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __lt__(self, right: System.DateTimeOffset) -> bool:
        ...

    def __ne__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __sub__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __sub__(self, right: System.DateTimeOffset) -> datetime.timedelta:
        ...

    def add(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def add_days(self, days: float) -> System.DateTimeOffset:
        ...

    def add_hours(self, hours: float) -> System.DateTimeOffset:
        ...

    def add_microseconds(self, microseconds: float) -> System.DateTimeOffset:
        ...

    def add_milliseconds(self, milliseconds: float) -> System.DateTimeOffset:
        ...

    def add_minutes(self, minutes: float) -> System.DateTimeOffset:
        ...

    def add_months(self, months: int) -> System.DateTimeOffset:
        ...

    def add_seconds(self, seconds: float) -> System.DateTimeOffset:
        ...

    def add_ticks(self, ticks: int) -> System.DateTimeOffset:
        ...

    def add_years(self, years: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def compare(first: System.DateTimeOffset, second: System.DateTimeOffset) -> int:
        ...

    def compare_to(self, other: System.DateTimeOffset) -> int:
        ...

    def deconstruct(self, date: typing.Optional[System.DateOnly], time: typing.Optional[System.TimeOnly], offset: typing.Optional[datetime.timedelta]) -> typing.Tuple[None, System.DateOnly, System.TimeOnly, datetime.timedelta]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.DateTimeOffset) -> bool:
        ...

    @staticmethod
    @overload
    def equals(first: System.DateTimeOffset, second: System.DateTimeOffset) -> bool:
        ...

    def equals_exact(self, other: System.DateTimeOffset) -> bool:
        ...

    @staticmethod
    def from_file_time(file_time: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def from_unix_time_milliseconds(milliseconds: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def from_unix_time_seconds(seconds: int) -> System.DateTimeOffset:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider = None, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @overload
    def subtract(self, value: System.DateTimeOffset) -> datetime.timedelta:
        ...

    @overload
    def subtract(self, value: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def to_file_time(self) -> int:
        ...

    def to_local_time(self) -> System.DateTimeOffset:
        ...

    def to_offset(self, offset: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    def to_universal_time(self) -> System.DateTimeOffset:
        ...

    def to_unix_time_milliseconds(self) -> int:
        ...

    def to_unix_time_seconds(self) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...


class Guid(System.ISpanFormattable, System.IComparable[System_Guid], System.IEquatable[System_Guid], System.ISpanParsable[System_Guid], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Guid]):
    """This class has no documentation."""

    EMPTY: System.Guid

    ALL_BITS_SET: System.Guid

    @property
    def variant(self) -> int:
        ...

    @property
    def version(self) -> int:
        ...

    def __eq__(self, b: System.Guid) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __init__(self, b: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, b: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def __init__(self, b: System.ReadOnlySpan[int], big_endian: bool) -> None:
        ...

    @overload
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int) -> None:
        ...

    @overload
    def __init__(self, a: int, b: int, c: int, d: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, g: str) -> None:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __le__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Guid) -> bool:
        ...

    def __ne__(self, b: System.Guid) -> bool:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Guid) -> int:
        ...

    @staticmethod
    @overload
    def create_version_7() -> System.Guid:
        ...

    @staticmethod
    @overload
    def create_version_7(timestamp: System.DateTimeOffset) -> System.Guid:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, g: System.Guid) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def new_guid() -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str]) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str]) -> System.Guid:
        ...

    @overload
    def to_byte_array(self) -> typing.List[int]:
        ...

    @overload
    def to_byte_array(self, big_endian: bool) -> typing.List[int]:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ...) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @overload
    def try_write_bytes(self, destination: System.Span[int]) -> bool:
        ...

    @overload
    def try_write_bytes(self, destination: System.Span[int], big_endian: bool, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Type(System.Reflection.MemberInfo, System.Reflection.IReflect, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_serializable(self) -> bool:
        warnings.warn("Obsoletions.LegacyFormatterMessage", DeprecationWarning)

    @property
    def contains_generic_parameters(self) -> bool:
        ...

    @property
    def is_visible(self) -> bool:
        ...

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def namespace(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def assembly_qualified_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def full_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    @abc.abstractmethod
    def module(self) -> System.Reflection.Module:
        ...

    @property
    def is_interface(self) -> bool:
        ...

    @property
    def is_nested(self) -> bool:
        ...

    @property
    def declaring_type(self) -> typing.Type:
        ...

    @property
    def declaring_method(self) -> System.Reflection.MethodBase:
        ...

    @property
    def reflected_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def underlying_system_type(self) -> typing.Type:
        ...

    @property
    def is_type_definition(self) -> bool:
        ...

    @property
    def is_array(self) -> bool:
        ...

    @property
    def is_by_ref(self) -> bool:
        ...

    @property
    def is_pointer(self) -> bool:
        ...

    @property
    def is_constructed_generic_type(self) -> bool:
        ...

    @property
    def is_generic_parameter(self) -> bool:
        ...

    @property
    def is_generic_type_parameter(self) -> bool:
        ...

    @property
    def is_generic_method_parameter(self) -> bool:
        ...

    @property
    def is_generic_type(self) -> bool:
        ...

    @property
    def is_generic_type_definition(self) -> bool:
        ...

    @property
    def is_sz_array(self) -> bool:
        ...

    @property
    def is_variable_bound_array(self) -> bool:
        ...

    @property
    def is_by_ref_like(self) -> bool:
        ...

    @property
    def is_function_pointer(self) -> bool:
        ...

    @property
    def is_unmanaged_function_pointer(self) -> bool:
        ...

    @property
    def has_element_type(self) -> bool:
        ...

    @property
    def generic_type_arguments(self) -> typing.List[typing.Type]:
        ...

    @property
    def generic_parameter_position(self) -> int:
        ...

    @property
    def generic_parameter_attributes(self) -> System.Reflection.GenericParameterAttributes:
        ...

    @property
    def attributes(self) -> System.Reflection.TypeAttributes:
        ...

    @property
    def is_abstract(self) -> bool:
        ...

    @property
    def is_import(self) -> bool:
        ...

    @property
    def is_sealed(self) -> bool:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    def is_class(self) -> bool:
        ...

    @property
    def is_nested_assembly(self) -> bool:
        ...

    @property
    def is_nested_fam_and_assem(self) -> bool:
        ...

    @property
    def is_nested_family(self) -> bool:
        ...

    @property
    def is_nested_fam_or_assem(self) -> bool:
        ...

    @property
    def is_nested_private(self) -> bool:
        ...

    @property
    def is_nested_public(self) -> bool:
        ...

    @property
    def is_not_public(self) -> bool:
        ...

    @property
    def is_public(self) -> bool:
        ...

    @property
    def is_auto_layout(self) -> bool:
        ...

    @property
    def is_explicit_layout(self) -> bool:
        ...

    @property
    def is_layout_sequential(self) -> bool:
        ...

    @property
    def is_ansi_class(self) -> bool:
        ...

    @property
    def is_auto_class(self) -> bool:
        ...

    @property
    def is_unicode_class(self) -> bool:
        ...

    @property
    def is_com_object(self) -> bool:
        ...

    @property
    def is_contextful(self) -> bool:
        ...

    @property
    def is_enum(self) -> bool:
        ...

    @property
    def is_marshal_by_ref(self) -> bool:
        ...

    @property
    def is_primitive(self) -> bool:
        ...

    @property
    def is_value_type(self) -> bool:
        ...

    @property
    def is_signature_type(self) -> bool:
        ...

    @property
    def is_security_critical(self) -> bool:
        ...

    @property
    def is_security_safe_critical(self) -> bool:
        ...

    @property
    def is_security_transparent(self) -> bool:
        ...

    @property
    def struct_layout_attribute(self) -> System.Runtime.InteropServices.StructLayoutAttribute:
        ...

    @property
    def type_initializer(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def type_handle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    @abc.abstractmethod
    def guid(self) -> System.Guid:
        ...

    @property
    @abc.abstractmethod
    def base_type(self) -> typing.Type:
        ...

    DEFAULT_BINDER: System.Reflection.Binder

    DELIMITER: str = ...

    EMPTY_TYPES: typing.List[typing.Type] = ...

    MISSING: System.Object = ...

    FILTER_ATTRIBUTE: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    FILTER_NAME: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    FILTER_NAME_IGNORE_CASE: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    def __eq__(self, right: typing.Type) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: typing.Type) -> bool:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, o: typing.Type) -> bool:
        ...

    def find_interfaces(self, filter: typing.Callable[[typing.Type, System.Object], bool], filter_criteria: typing.Any) -> typing.List[typing.Type]:
        ...

    def find_members(self, member_type: System.Reflection.MemberTypes, binding_attr: System.Reflection.BindingFlags, filter: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool], filter_criteria: typing.Any) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_array_rank(self) -> int:
        ...

    def get_attribute_flags_impl(self) -> System.Reflection.TypeAttributes:
        ...

    @overload
    def get_constructor(self, types: typing.List[typing.Type]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    def get_constructor_impl(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructors(self) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    @overload
    def get_constructors(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    def get_default_members(self) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_element_type(self) -> typing.Type:
        ...

    def get_enum_name(self, value: typing.Any) -> str:
        ...

    def get_enum_names(self) -> typing.List[str]:
        ...

    def get_enum_underlying_type(self) -> typing.Type:
        ...

    def get_enum_values(self) -> System.Array:
        ...

    def get_enum_values_as_underlying_type(self) -> System.Array:
        ...

    @overload
    def get_event(self, name: str) -> System.Reflection.EventInfo:
        ...

    @overload
    def get_event(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.EventInfo:
        ...

    @overload
    def get_events(self) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def get_events(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def get_field(self, name: str) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_field(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_fields(self) -> typing.List[System.Reflection.FieldInfo]:
        ...

    @overload
    def get_fields(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def get_function_pointer_calling_conventions(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_parameter_types(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_return_type(self) -> typing.Type:
        ...

    def get_generic_arguments(self) -> typing.List[typing.Type]:
        ...

    def get_generic_parameter_constraints(self) -> typing.List[typing.Type]:
        ...

    def get_generic_type_definition(self) -> typing.Type:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_interface(self, name: str) -> typing.Type:
        ...

    @overload
    def get_interface(self, name: str, ignore_case: bool) -> typing.Type:
        ...

    def get_interface_map(self, interface_type: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    def get_interfaces(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_member(self, name: str) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_member(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_member(self, name: str, type: System.Reflection.MemberTypes, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_members(self) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_members(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_member_with_same_metadata_definition_as(self, member: System.Reflection.MemberInfo) -> System.Reflection.MemberInfo:
        ...

    @overload
    def get_method(self, name: str) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method_impl(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_methods(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_nested_type(self, name: str) -> typing.Type:
        ...

    @overload
    def get_nested_type(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.Type:
        ...

    @overload
    def get_nested_types(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_nested_types(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[typing.Type]:
        ...

    def get_optional_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_properties(self) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def get_properties(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def get_property(self, name: str) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type, types: typing.List[typing.Type]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def get_property_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def get_required_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_type(self) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type]) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type], throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type], throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_array(args: typing.List[System.Object]) -> typing.List[typing.Type]:
        ...

    @staticmethod
    def get_type_code(type: typing.Type) -> System.TypeCode:
        ...

    def get_type_code_impl(self) -> System.TypeCode:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, server: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, server: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_from_handle(handle: System.RuntimeTypeHandle) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, server: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, server: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_handle(o: typing.Any) -> System.RuntimeTypeHandle:
        ...

    def has_element_type_impl(self) -> bool:
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, named_parameters: typing.List[str]) -> System.Object:
        ...

    def is_array_impl(self) -> bool:
        ...

    def is_assignable_from(self, c: typing.Type) -> bool:
        ...

    def is_assignable_to(self, target_type: typing.Type) -> bool:
        ...

    def is_by_ref_impl(self) -> bool:
        ...

    def is_com_object_impl(self) -> bool:
        ...

    def is_contextful_impl(self) -> bool:
        ...

    def is_enum_defined(self, value: typing.Any) -> bool:
        ...

    def is_equivalent_to(self, other: typing.Type) -> bool:
        ...

    def is_instance_of_type(self, o: typing.Any) -> bool:
        ...

    def is_marshal_by_ref_impl(self) -> bool:
        ...

    def is_pointer_impl(self) -> bool:
        ...

    def is_primitive_impl(self) -> bool:
        ...

    def is_subclass_of(self, c: typing.Type) -> bool:
        ...

    def is_value_type_impl(self) -> bool:
        ...

    @overload
    def make_array_type(self) -> typing.Type:
        ...

    @overload
    def make_array_type(self, rank: int) -> typing.Type:
        ...

    def make_by_ref_type(self) -> typing.Type:
        ...

    @staticmethod
    def make_generic_method_parameter(position: int) -> typing.Type:
        ...

    @staticmethod
    def make_generic_signature_type(generic_type_definition: typing.Type, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> typing.Type:
        ...

    def make_generic_type(self, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> typing.Type:
        ...

    def make_pointer_type(self) -> typing.Type:
        ...

    @staticmethod
    def reflection_only_get_type(type_name: str, throw_if_not_found: bool, ignore_case: bool) -> typing.Type:
        warnings.warn("Obsoletions.ReflectionOnlyLoadingMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class DateTime(System.IComparable[datetime.datetime], System.ISpanFormattable, System.IConvertible, System.IEquatable[datetime.datetime], System.Runtime.Serialization.ISerializable, System.ISpanParsable[datetime.datetime], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    MIN_VALUE: datetime.datetime

    MAX_VALUE: datetime.datetime = ...

    UNIX_EPOCH: datetime.datetime = ...

    @property
    def date(self) -> datetime.datetime:
        ...

    @property
    def day(self) -> int:
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        ...

    @property
    def day_of_year(self) -> int:
        ...

    @property
    def hour(self) -> int:
        ...

    @property
    def kind(self) -> System.DateTimeKind:
        ...

    @property
    def millisecond(self) -> int:
        ...

    @property
    def microsecond(self) -> int:
        ...

    @property
    def nanosecond(self) -> int:
        ...

    @property
    def minute(self) -> int:
        ...

    @property
    def month(self) -> int:
        ...

    NOW: datetime.datetime

    @property
    def second(self) -> int:
        ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def time_of_day(self) -> datetime.timedelta:
        ...

    TODAY: datetime.datetime

    @property
    def year(self) -> int:
        ...

    UTC_NOW: datetime.datetime

    def __add__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    def __eq__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __ge__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __gt__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def __iadd__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        ...

    @overload
    def __init__(self, ticks: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly) -> None:
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __isub__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __isub__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __le__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __lt__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def __ne__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __sub__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __sub__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    def add(self, value: datetime.timedelta) -> datetime.datetime:
        ...

    def add_days(self, value: float) -> datetime.datetime:
        ...

    def add_hours(self, value: float) -> datetime.datetime:
        ...

    def add_microseconds(self, value: float) -> datetime.datetime:
        ...

    def add_milliseconds(self, value: float) -> datetime.datetime:
        ...

    def add_minutes(self, value: float) -> datetime.datetime:
        ...

    def add_months(self, months: int) -> datetime.datetime:
        ...

    def add_seconds(self, value: float) -> datetime.datetime:
        ...

    def add_ticks(self, value: int) -> datetime.datetime:
        ...

    def add_years(self, value: int) -> datetime.datetime:
        ...

    @staticmethod
    def compare(t_1: typing.Union[datetime.datetime, datetime.date], t_2: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        ...

    @overload
    def deconstruct(self, date: typing.Optional[System.DateOnly], time: typing.Optional[System.TimeOnly]) -> typing.Tuple[None, System.DateOnly, System.TimeOnly]:
        ...

    @overload
    def deconstruct(self, year: typing.Optional[int], month: typing.Optional[int], day: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(t_1: typing.Union[datetime.datetime, datetime.date], t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    def from_binary(date_data: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_file_time(file_time: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_file_time_utc(file_time: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_oa_date(d: float) -> datetime.datetime:
        ...

    @overload
    def get_date_time_formats(self) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, provider: System.IFormatProvider) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, format: str) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, format: str, provider: System.IFormatProvider) -> typing.List[str]:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    def is_daylight_saving_time(self) -> bool:
        ...

    @staticmethod
    def is_leap_year(year: int) -> bool:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = None, styles: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    def specify_kind(value: typing.Union[datetime.datetime, datetime.date], kind: System.DateTimeKind) -> datetime.datetime:
        ...

    @overload
    def subtract(self, value: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def subtract(self, value: datetime.timedelta) -> datetime.datetime:
        ...

    def to_binary(self) -> int:
        ...

    def to_file_time(self) -> int:
        ...

    def to_file_time_utc(self) -> int:
        ...

    def to_local_time(self) -> datetime.datetime:
        ...

    def to_long_date_string(self) -> str:
        ...

    def to_long_time_string(self) -> str:
        ...

    def to_oa_date(self) -> float:
        ...

    def to_short_date_string(self) -> str:
        ...

    def to_short_time_string(self) -> str:
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

    def to_universal_time(self) -> datetime.datetime:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...


class InvalidProgramException(System.SystemException):
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


class Byte(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IUtfChar[int], System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = 0

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
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
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class TimeZoneInfo(System.Object, System.IEquatable[System_TimeZoneInfo], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
    """This class has no documentation."""

    class AdjustmentRule(System.Object, System.IEquatable[System_TimeZoneInfo_AdjustmentRule], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def date_start(self) -> datetime.datetime:
            ...

        @property
        def date_end(self) -> datetime.datetime:
            ...

        @property
        def daylight_delta(self) -> datetime.timedelta:
            ...

        @property
        def daylight_transition_start(self) -> System.TimeZoneInfo.TransitionTime:
            ...

        @property
        def daylight_transition_end(self) -> System.TimeZoneInfo.TransitionTime:
            ...

        @property
        def base_utc_offset_delta(self) -> datetime.timedelta:
            ...

        @staticmethod
        @overload
        def create_adjustment_rule(date_start: typing.Union[datetime.datetime, datetime.date], date_end: typing.Union[datetime.datetime, datetime.date], daylight_delta: datetime.timedelta, daylight_transition_start: System.TimeZoneInfo.TransitionTime, daylight_transition_end: System.TimeZoneInfo.TransitionTime, base_utc_offset_delta: datetime.timedelta) -> System.TimeZoneInfo.AdjustmentRule:
            ...

        @staticmethod
        @overload
        def create_adjustment_rule(date_start: typing.Union[datetime.datetime, datetime.date], date_end: typing.Union[datetime.datetime, datetime.date], daylight_delta: datetime.timedelta, daylight_transition_start: System.TimeZoneInfo.TransitionTime, daylight_transition_end: System.TimeZoneInfo.TransitionTime) -> System.TimeZoneInfo.AdjustmentRule:
            ...

        @overload
        def equals(self, obj: typing.Any) -> bool:
            ...

        @overload
        def equals(self, other: System.TimeZoneInfo.AdjustmentRule) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    class TransitionTime(System.IEquatable[System_TimeZoneInfo_TransitionTime], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def time_of_day(self) -> datetime.datetime:
            ...

        @property
        def month(self) -> int:
            ...

        @property
        def week(self) -> int:
            ...

        @property
        def day(self) -> int:
            ...

        @property
        def day_of_week(self) -> System.DayOfWeek:
            ...

        @property
        def is_fixed_date_rule(self) -> bool:
            ...

        def __eq__(self, t_2: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        def __ne__(self, t_2: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        @staticmethod
        def create_fixed_date_rule(time_of_day: typing.Union[datetime.datetime, datetime.date], month: int, day: int) -> System.TimeZoneInfo.TransitionTime:
            ...

        @staticmethod
        def create_floating_date_rule(time_of_day: typing.Union[datetime.datetime, datetime.date], month: int, week: int, day_of_week: System.DayOfWeek) -> System.TimeZoneInfo.TransitionTime:
            ...

        @overload
        def equals(self, obj: typing.Any) -> bool:
            ...

        @overload
        def equals(self, other: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    @property
    def id(self) -> str:
        ...

    @property
    def has_iana_id(self) -> bool:
        ...

    @property
    def display_name(self) -> str:
        ...

    @property
    def standard_name(self) -> str:
        ...

    @property
    def daylight_name(self) -> str:
        ...

    @property
    def base_utc_offset(self) -> datetime.timedelta:
        ...

    @property
    def supports_daylight_saving_time(self) -> bool:
        ...

    LOCAL: System.TimeZoneInfo

    UTC: System.TimeZoneInfo

    @staticmethod
    def clear_cached_data() -> None:
        ...

    @staticmethod
    @overload
    def convert_time(date_time_offset: System.DateTimeOffset, destination_time_zone: System.TimeZoneInfo) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def convert_time(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def convert_time(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone: System.TimeZoneInfo, destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time_offset: System.DateTimeOffset, destination_time_zone_id: str) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone_id: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone_id: str, destination_time_zone_id: str) -> datetime.datetime:
        ...

    @staticmethod
    def convert_time_from_utc(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def convert_time_to_utc(date_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def convert_time_to_utc(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str) -> System.TimeZoneInfo:
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str, daylight_display_name: str, adjustment_rules: typing.List[System.TimeZoneInfo.AdjustmentRule]) -> System.TimeZoneInfo:
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str, daylight_display_name: str, adjustment_rules: typing.List[System.TimeZoneInfo.AdjustmentRule], disable_daylight_saving_time: bool) -> System.TimeZoneInfo:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.TimeZoneInfo) -> bool:
        ...

    @staticmethod
    def find_system_time_zone_by_id(id: str) -> System.TimeZoneInfo:
        ...

    @staticmethod
    def from_serialized_string(source: str) -> System.TimeZoneInfo:
        ...

    def get_adjustment_rules(self) -> typing.List[System.TimeZoneInfo.AdjustmentRule]:
        ...

    @overload
    def get_ambiguous_time_offsets(self, date_time_offset: System.DateTimeOffset) -> typing.List[datetime.timedelta]:
        ...

    @overload
    def get_ambiguous_time_offsets(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> typing.List[datetime.timedelta]:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_system_time_zones() -> System.Collections.ObjectModel.ReadOnlyCollection[System.TimeZoneInfo]:
        ...

    @staticmethod
    @overload
    def get_system_time_zones(skip_sorting: bool) -> System.Collections.ObjectModel.ReadOnlyCollection[System.TimeZoneInfo]:
        ...

    @overload
    def get_utc_offset(self, date_time_offset: System.DateTimeOffset) -> datetime.timedelta:
        ...

    @overload
    def get_utc_offset(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    def has_same_rules(self, other: System.TimeZoneInfo) -> bool:
        ...

    @overload
    def is_ambiguous_time(self, date_time_offset: System.DateTimeOffset) -> bool:
        ...

    @overload
    def is_ambiguous_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def is_daylight_saving_time(self, date_time_offset: System.DateTimeOffset) -> bool:
        ...

    @overload
    def is_daylight_saving_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def is_invalid_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def to_serialized_string(self) -> str:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def try_convert_iana_id_to_windows_id(iana_id: str, windows_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        ...

    @staticmethod
    @overload
    def try_convert_windows_id_to_iana_id(windows_id: str, iana_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        ...

    @staticmethod
    @overload
    def try_convert_windows_id_to_iana_id(windows_id: str, region: str, iana_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        ...

    @staticmethod
    def try_find_system_time_zone_by_id(id: str, time_zone_info: typing.Optional[System.TimeZoneInfo]) -> typing.Tuple[bool, System.TimeZoneInfo]:
        ...


class Base64FormattingOptions(IntEnum):
    """This class has no documentation."""

    NONE = 0

    INSERT_LINE_BREAKS = 1


class Convert(System.Object):
    """This class has no documentation."""

    DB_NULL: System.Object = ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, type_code: System.TypeCode) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, type_code: System.TypeCode, provider: System.IFormatProvider) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, conversion_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, conversion_type: typing.Type, provider: System.IFormatProvider) -> System.Object:
        ...

    @staticmethod
    def from_base_64_char_array(in_array: typing.List[str], offset: int, length: int) -> typing.List[int]:
        ...

    @staticmethod
    def from_base_64_string(s: str) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(s: str) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(chars: System.ReadOnlySpan[str]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(utf_8_source: System.ReadOnlySpan[int]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(source: str, destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    @overload
    def from_hex_string(utf_8_source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        ...

    @staticmethod
    def get_type_code(value: typing.Any) -> System.TypeCode:
        ...

    @staticmethod
    def is_db_null(value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def to_base_64_char_array(in_array: typing.List[int], offset_in: int, length: int, out_array: typing.List[str], offset_out: int) -> int:
        ...

    @staticmethod
    @overload
    def to_base_64_char_array(in_array: typing.List[int], offset_in: int, length: int, out_array: typing.List[str], offset_out: int, options: System.Base64FormattingOptions) -> int:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], options: System.Base64FormattingOptions) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], offset: int, length: int) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], offset: int, length: int, options: System.Base64FormattingOptions) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(bytes: System.ReadOnlySpan[int], options: System.Base64FormattingOptions = ...) -> str:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Any, provider: System.IFormatProvider) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: bool) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: int) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: str, provider: System.IFormatProvider) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: float) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Any, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: bool) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: str) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: int) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: float) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Union[datetime.datetime, datetime.date]) -> str:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Any) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Any, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: int) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: bool) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: float) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_hex_string(in_array: typing.List[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_hex_string(in_array: typing.List[int], offset: int, length: int) -> str:
        ...

    @staticmethod
    @overload
    def to_hex_string(bytes: System.ReadOnlySpan[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(in_array: typing.List[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(in_array: typing.List[int], offset: int, length: int) -> str:
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(bytes: System.ReadOnlySpan[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Any, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: bool) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: bool, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: str) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: float) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: float, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Union[datetime.datetime, datetime.date]) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Union[datetime.datetime, datetime.date], provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int, to_base: int) -> str:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str, from_base: int) -> int:
        ...

    @staticmethod
    def try_from_base_64_chars(chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_from_base_64_string(s: str, bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_to_base_64_chars(bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int], options: System.Base64FormattingOptions = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_to_hex_string(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_to_hex_string(source: System.ReadOnlySpan[int], utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_to_hex_string_lower(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_to_hex_string_lower(source: System.ReadOnlySpan[int], utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class UInt128(System.Numerics.IUnsignedNumber[System_UInt128], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[System_UInt128]):
    """This class has no documentation."""

    MIN_VALUE: System.UInt128

    MAX_VALUE: System.UInt128

    ONE: System.UInt128

    ZERO: System.UInt128

    @overload
    def __add__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __add__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __and__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __eq__(self, right: System.UInt128) -> bool:
        ...

    def __ge__(self, right: System.UInt128) -> bool:
        ...

    def __gt__(self, right: System.UInt128) -> bool:
        ...

    @overload
    def __iadd__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __iadd__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __iand__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ilshift__(self, shift_amount: int) -> System.UInt128:
        ...

    def __imod__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __imul__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __imul__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __init__(self, upper: int, lower: int) -> None:
        ...

    def __invert__(self) -> System.UInt128:
        ...

    def __ior__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __irshift__(self, shift_amount: int) -> System.UInt128:
        ...

    @overload
    def __isub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __isub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __itruediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __itruediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ixor__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __le__(self, right: System.UInt128) -> bool:
        ...

    def __lshift__(self, shift_amount: int) -> System.UInt128:
        ...

    def __lt__(self, right: System.UInt128) -> bool:
        ...

    def __mod__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __mul__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __mul__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ne__(self, right: System.UInt128) -> bool:
        ...

    @overload
    def __neg__(self) -> System.UInt128:
        ...

    @overload
    def __neg__(self) -> System.UInt128:
        ...

    def __or__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __pos__(self) -> System.UInt128:
        ...

    def __rshift__(self, shift_amount: int) -> System.UInt128:
        ...

    @overload
    def __sub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __sub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __truediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __truediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __xor__(self, right: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def big_mul(left: System.UInt128, right: System.UInt128, lower: typing.Optional[System.UInt128]) -> typing.Tuple[System.UInt128, System.UInt128]:
        ...

    @staticmethod
    def clamp(value: System.UInt128, min: System.UInt128, max: System.UInt128) -> System.UInt128:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.UInt128) -> int:
        ...

    @staticmethod
    def div_rem(left: System.UInt128, right: System.UInt128) -> System.ValueTuple[System.UInt128, System.UInt128]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.UInt128) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def log_2(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def max(x: System.UInt128, y: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def min(x: System.UInt128, y: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    def pop_count(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def rotate_left(value: System.UInt128, rotate_amount: int) -> System.UInt128:
        ...

    @staticmethod
    def rotate_right(value: System.UInt128, rotate_amount: int) -> System.UInt128:
        ...

    @staticmethod
    def sign(value: System.UInt128) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: System.UInt128) -> System.UInt128:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...


class UInt64(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> System.UInt128:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Span(typing.Generic[System_Span_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Span_T]):
        """This class has no documentation."""

        @property
        def current(self) -> typing.Any:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def length(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    EMPTY: System.Span[System_Span_T]

    def __eq__(self, right: System.Span[System_Span_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_Span_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_Span_T], start: int, length: int) -> None:
        ...

    @overload
    def __init__(self, reference: System_Span_T) -> None:
        ...

    def __ne__(self, right: System.Span[System_Span_T]) -> bool:
        ...

    def clear(self) -> None:
        ...

    def copy_to(self, destination: System.Span[System_Span_T]) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        warnings.warn("Equals() on Span will always throw an exception. Use the equality operator instead.", DeprecationWarning)

    def fill(self, value: System_Span_T) -> None:
        ...

    def get_enumerator(self) -> System.Span.Enumerator:
        ...

    def get_hash_code(self) -> int:
        warnings.warn("GetHashCode() on Span will always throw an exception.", DeprecationWarning)

    def get_pinnable_reference(self) -> typing.Any:
        ...

    @overload
    def slice(self, start: int) -> System.Span[System_Span_T]:
        ...

    @overload
    def slice(self, start: int, length: int) -> System.Span[System_Span_T]:
        ...

    def to_array(self) -> typing.List[System_Span_T]:
        ...

    def to_string(self) -> str:
        ...

    def try_copy_to(self, destination: System.Span[System_Span_T]) -> bool:
        ...


class Attribute(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def type_id(self) -> System.Object:
        ...

    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Assembly, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Module, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Assembly, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Module, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...


class SerializableAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IObserver(typing.Generic[System_IObserver_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def on_completed(self) -> None:
        ...

    def on_error(self, error: System.Exception) -> None:
        ...

    def on_next(self, value: System_IObserver_T) -> None:
        ...


class PlatformID(IntEnum):
    """This class has no documentation."""

    WIN_32S = 0

    WIN_32_WINDOWS = 1

    WIN_32_NT = 2

    WIN_CE = 3

    UNIX = 4

    XBOX = 5

    MAC_OSX = 6

    OTHER = 7


class Version(System.Object, System.ICloneable, System.IComparable[System_Version], System.IEquatable[System_Version], System.ISpanFormattable, System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Version]):
    """This class has no documentation."""

    @property
    def major(self) -> int:
        ...

    @property
    def minor(self) -> int:
        ...

    @property
    def build(self) -> int:
        ...

    @property
    def revision(self) -> int:
        ...

    @property
    def major_revision(self) -> int:
        ...

    @property
    def minor_revision(self) -> int:
        ...

    def __eq__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Version) -> bool:
        ...

    @overload
    def __ge__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Version) -> bool:
        ...

    @overload
    def __gt__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __init__(self, major: int, minor: int, build: int, revision: int) -> None:
        ...

    @overload
    def __init__(self, major: int, minor: int, build: int) -> None:
        ...

    @overload
    def __init__(self, major: int, minor: int) -> None:
        ...

    @overload
    def __init__(self, version: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.Version) -> bool:
        ...

    @overload
    def __le__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Version) -> bool:
        ...

    @overload
    def __lt__(self, v_2: System.Version) -> bool:
        ...

    def __ne__(self, v_2: System.Version) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @overload
    def compare_to(self, version: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Version) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Version) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.Version:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str]) -> System.Version:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Version:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, field_count: int) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, destination: System.Span[str], field_count: int, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], field_count: int, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        ...


class OperatingSystem(System.Object, System.Runtime.Serialization.ISerializable, System.ICloneable):
    """This class has no documentation."""

    @property
    def platform(self) -> System.PlatformID:
        ...

    @property
    def service_pack(self) -> str:
        ...

    @property
    def version(self) -> System.Version:
        ...

    @property
    def version_string(self) -> str:
        ...

    def __init__(self, platform: System.PlatformID, version: System.Version) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def is_android() -> bool:
        ...

    @staticmethod
    def is_android_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        ...

    @staticmethod
    def is_browser() -> bool:
        ...

    @staticmethod
    def is_free_bsd() -> bool:
        ...

    @staticmethod
    def is_free_bsd_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        ...

    @staticmethod
    def is_ios() -> bool:
        ...

    @staticmethod
    def is_ios_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        ...

    @staticmethod
    def is_linux() -> bool:
        ...

    @staticmethod
    def is_mac_catalyst() -> bool:
        ...

    @staticmethod
    def is_mac_catalyst_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        ...

    @staticmethod
    def is_mac_os() -> bool:
        ...

    @staticmethod
    def is_mac_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        ...

    @staticmethod
    def is_os_platform(platform: str) -> bool:
        ...

    @staticmethod
    def is_os_platform_version_at_least(platform: str, major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        ...

    @staticmethod
    def is_tv_os() -> bool:
        ...

    @staticmethod
    def is_tv_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        ...

    @staticmethod
    def is_wasi() -> bool:
        ...

    @staticmethod
    def is_watch_os() -> bool:
        ...

    @staticmethod
    def is_watch_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        ...

    @staticmethod
    def is_windows() -> bool:
        ...

    @staticmethod
    def is_windows_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        ...

    def to_string(self) -> str:
        ...


class EnvironmentVariableTarget(IntEnum):
    """This class has no documentation."""

    PROCESS = 0

    USER = 1

    MACHINE = 2


class Environment(System.Object):
    """This class has no documentation."""

    class ProcessCpuUsage:
        """This class has no documentation."""

        @property
        def user_time(self) -> datetime.timedelta:
            ...

        @property
        def privileged_time(self) -> datetime.timedelta:
            ...

        @property
        def total_time(self) -> datetime.timedelta:
            ...

    class SpecialFolder(IntEnum):
        """This class has no documentation."""

        APPLICATION_DATA = ...

        COMMON_APPLICATION_DATA = ...

        LOCAL_APPLICATION_DATA = ...

        COOKIES = ...

        DESKTOP = ...

        FAVORITES = ...

        HISTORY = ...

        INTERNET_CACHE = ...

        PROGRAMS = ...

        MY_COMPUTER = ...

        MY_MUSIC = ...

        MY_PICTURES = ...

        MY_VIDEOS = ...

        RECENT = ...

        SEND_TO = ...

        START_MENU = ...

        STARTUP = ...

        SYSTEM = ...

        TEMPLATES = ...

        DESKTOP_DIRECTORY = ...

        PERSONAL = ...

        MY_DOCUMENTS = ...

        PROGRAM_FILES = ...

        COMMON_PROGRAM_FILES = ...

        ADMIN_TOOLS = ...

        CD_BURNING = ...

        COMMON_ADMIN_TOOLS = ...

        COMMON_DOCUMENTS = ...

        COMMON_MUSIC = ...

        COMMON_OEM_LINKS = ...

        COMMON_PICTURES = ...

        COMMON_START_MENU = ...

        COMMON_PROGRAMS = ...

        COMMON_STARTUP = ...

        COMMON_DESKTOP_DIRECTORY = ...

        COMMON_TEMPLATES = ...

        COMMON_VIDEOS = ...

        FONTS = ...

        NETWORK_SHORTCUTS = ...

        PRINTER_SHORTCUTS = ...

        USER_PROFILE = ...

        COMMON_PROGRAM_FILES_X_86 = ...

        PROGRAM_FILES_X_86 = ...

        RESOURCES = ...

        LOCALIZED_RESOURCES = ...

        SYSTEM_X_86 = ...

        WINDOWS = ...

    class SpecialFolderOption(IntEnum):
        """This class has no documentation."""

        NONE = 0

        CREATE = ...

        DO_NOT_VERIFY = ...

    MACHINE_NAME: str

    USER_NAME: str

    WORKING_SET: int

    USER_DOMAIN_NAME: str

    SYSTEM_DIRECTORY: str

    USER_INTERACTIVE: bool

    CPU_USAGE: System.Environment.ProcessCpuUsage

    TICK_COUNT_64: int

    PROCESSOR_COUNT: int

    IS_PRIVILEGED_PROCESS: bool

    HAS_SHUTDOWN_STARTED: bool

    COMMAND_LINE: str

    current_directory: str

    PROCESS_ID: int

    PROCESS_PATH: str

    IS_64_BIT_PROCESS: bool

    IS_64_BIT_OPERATING_SYSTEM: bool

    NEW_LINE: str

    OS_VERSION: System.OperatingSystem

    STACK_TRACE: str

    SYSTEM_PAGE_SIZE: int

    TICK_COUNT: int

    CURRENT_MANAGED_THREAD_ID: int

    exit_code: int

    @staticmethod
    def exit(exit_code: int) -> None:
        ...

    @staticmethod
    def expand_environment_variables(name: str) -> str:
        ...

    @staticmethod
    @overload
    def fail_fast(message: str) -> None:
        ...

    @staticmethod
    @overload
    def fail_fast(message: str, exception: System.Exception) -> None:
        ...

    @staticmethod
    def get_command_line_args() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_environment_variable(variable: str) -> str:
        ...

    @staticmethod
    @overload
    def get_environment_variable(variable: str, target: System.EnvironmentVariableTarget) -> str:
        ...

    @staticmethod
    @overload
    def get_environment_variables() -> System.Collections.IDictionary:
        ...

    @staticmethod
    @overload
    def get_environment_variables(target: System.EnvironmentVariableTarget) -> System.Collections.IDictionary:
        ...

    @staticmethod
    @overload
    def get_folder_path(folder: System.Environment.SpecialFolder) -> str:
        ...

    @staticmethod
    @overload
    def get_folder_path(folder: System.Environment.SpecialFolder, option: System.Environment.SpecialFolderOption) -> str:
        ...

    @staticmethod
    def get_logical_drives() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def set_environment_variable(variable: str, value: str) -> None:
        ...

    @staticmethod
    @overload
    def set_environment_variable(variable: str, value: str, target: System.EnvironmentVariableTarget) -> None:
        ...


class IParsable(typing.Generic[System_IParsable_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class MidpointRounding(IntEnum):
    """This class has no documentation."""

    TO_EVEN = 0

    AWAY_FROM_ZERO = 1

    TO_ZERO = 2

    TO_NEGATIVE_INFINITY = 3

    TO_POSITIVE_INFINITY = 4


class MathF(System.Object):
    """This class has no documentation."""

    E: float = ...

    PI: float = ...

    TAU: float = ...

    @staticmethod
    def abs(x: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def copy_sign(x: float, y: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(x: float, y: float, z: float) -> float:
        ...

    @staticmethod
    def ieee_remainder(x: float, y: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    @overload
    def log(x: float, y: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_2(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(x: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def truncate(x: float) -> float:
        ...


class TypeUnloadedException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class MemberAccessException(System.SystemException):
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


class MethodAccessException(System.MemberAccessException):
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


class OperationCanceledException(System.SystemException):
    """This class has no documentation."""

    @property
    def cancellation_token(self) -> System.Threading.CancellationToken:
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
    def __init__(self, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, message: str, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class FieldAccessException(System.MemberAccessException):
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


class MarshalByRefObject(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def get_lifetime_service(self) -> System.Object:
        warnings.warn("Obsoletions.RemotingApisMessage", DeprecationWarning)

    def initialize_lifetime_service(self) -> System.Object:
        warnings.warn("Obsoletions.RemotingApisMessage", DeprecationWarning)

    def memberwise_clone(self, clone_identity: bool) -> System.MarshalByRefObject:
        ...


class AppDomainSetup(System.Object):
    """This class has no documentation."""

    @property
    def application_base(self) -> str:
        ...

    @property
    def target_framework_name(self) -> str:
        ...


class EventArgs(System.Object):
    """This class has no documentation."""

    EMPTY: System.EventArgs = ...

    def __init__(self) -> None:
        ...


class UnhandledExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception_object(self) -> System.Object:
        ...

    @property
    def is_terminating(self) -> bool:
        ...

    def __init__(self, exception: typing.Any, is_terminating: bool) -> None:
        ...


class AssemblyLoadEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def loaded_assembly(self) -> System.Reflection.Assembly:
        ...

    def __init__(self, loaded_assembly: System.Reflection.Assembly) -> None:
        ...


class ResolveEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def requesting_assembly(self) -> System.Reflection.Assembly:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, requesting_assembly: System.Reflection.Assembly) -> None:
        ...


class AppDomain(System.MarshalByRefObject):
    """This class has no documentation."""

    CURRENT_DOMAIN: System.AppDomain

    @property
    def base_directory(self) -> str:
        ...

    @property
    def relative_search_path(self) -> str:
        ...

    @property
    def setup_information(self) -> System.AppDomainSetup:
        ...

    @property
    def permission_set(self) -> System.Security.PermissionSet:
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @property
    def unhandled_exception(self) -> _EventContainer[typing.Callable[[System.Object, System.UnhandledExceptionEventArgs], typing.Any], typing.Any]:
        ...

    @unhandled_exception.setter
    def unhandled_exception(self, value: _EventContainer[typing.Callable[[System.Object, System.UnhandledExceptionEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def dynamic_directory(self) -> str:
        ...

    @property
    def friendly_name(self) -> str:
        ...

    @property
    def id(self) -> int:
        ...

    @property
    def is_fully_trusted(self) -> bool:
        ...

    @property
    def is_homogenous(self) -> bool:
        ...

    @property
    def domain_unload(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @domain_unload.setter
    def domain_unload(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def first_chance_exception(self) -> _EventContainer[typing.Callable[[System.Object, System.Runtime.ExceptionServices.FirstChanceExceptionEventArgs], typing.Any], typing.Any]:
        ...

    @first_chance_exception.setter
    def first_chance_exception(self, value: _EventContainer[typing.Callable[[System.Object, System.Runtime.ExceptionServices.FirstChanceExceptionEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def process_exit(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @process_exit.setter
    def process_exit(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    monitoring_is_enabled: bool

    @property
    def monitoring_survived_memory_size(self) -> int:
        ...

    MONITORING_SURVIVED_PROCESS_MEMORY_SIZE: int

    @property
    def monitoring_total_allocated_memory_size(self) -> int:
        ...

    @property
    def shadow_copy_files(self) -> bool:
        ...

    @property
    def assembly_load(self) -> _EventContainer[typing.Callable[[System.Object, System.AssemblyLoadEventArgs], typing.Any], typing.Any]:
        ...

    @assembly_load.setter
    def assembly_load(self, value: _EventContainer[typing.Callable[[System.Object, System.AssemblyLoadEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def assembly_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @assembly_resolve.setter
    def assembly_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def reflection_only_assembly_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @reflection_only_assembly_resolve.setter
    def reflection_only_assembly_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def type_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @type_resolve.setter
    def type_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def resource_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @resource_resolve.setter
    def resource_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def monitoring_total_processor_time(self) -> datetime.timedelta:
        ...

    def append_private_path(self, path: str) -> None:
        warnings.warn("AppDomain.AppendPrivatePath has been deprecated and is not supported.", DeprecationWarning)

    def apply_policy(self, assembly_name: str) -> str:
        ...

    def clear_private_path(self) -> None:
        warnings.warn("AppDomain.ClearPrivatePath has been deprecated and is not supported.", DeprecationWarning)

    def clear_shadow_copy_path(self) -> None:
        warnings.warn("AppDomain.ClearShadowCopyPath has been deprecated and is not supported.", DeprecationWarning)

    @staticmethod
    def create_domain(friendly_name: str) -> System.AppDomain:
        warnings.warn("Obsoletions.AppDomainCreateUnloadMessage", DeprecationWarning)

    @overload
    def create_instance(self, assembly_name: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance(self, assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance(self, assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str) -> System.Object:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str) -> System.Object:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def execute_assembly(self, assembly_file: str) -> int:
        ...

    @overload
    def execute_assembly(self, assembly_file: str, args: typing.List[str]) -> int:
        ...

    @overload
    def execute_assembly(self, assembly_file: str, args: typing.List[str], hash_value: typing.List[int], hash_algorithm: System.Configuration.Assemblies.AssemblyHashAlgorithm) -> int:
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: System.Reflection.AssemblyName, *args: typing.Union[str, typing.Iterable[str]]) -> int:
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: str) -> int:
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: str, *args: typing.Union[str, typing.Iterable[str]]) -> int:
        ...

    def get_assemblies(self) -> typing.List[System.Reflection.Assembly]:
        ...

    @staticmethod
    def get_current_thread_id() -> int:
        warnings.warn("AppDomain.GetCurrentThreadId has been deprecated because it does not provide a stable Id when managed threads are running on fibers (aka lightweight threads). To get a stable identifier for a managed thread, use the ManagedThreadId property on Thread instead.", DeprecationWarning)

    def get_data(self, name: str) -> System.Object:
        ...

    def is_compatibility_switch_set(self, value: str) -> typing.Optional[bool]:
        ...

    def is_default_app_domain(self) -> bool:
        ...

    def is_finalizing_for_unload(self) -> bool:
        ...

    @overload
    def load(self, raw_assembly: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, raw_assembly: typing.List[int], raw_symbol_store: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, assembly_ref: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, assembly_string: str) -> System.Reflection.Assembly:
        ...

    def reflection_only_get_assemblies(self) -> typing.List[System.Reflection.Assembly]:
        ...

    def set_cache_path(self, path: str) -> None:
        warnings.warn("AppDomain.SetCachePath has been deprecated and is not supported.", DeprecationWarning)

    def set_data(self, name: str, data: typing.Any) -> None:
        ...

    def set_dynamic_base(self, path: str) -> None:
        warnings.warn("AppDomain.SetDynamicBase has been deprecated and is not supported.", DeprecationWarning)

    def set_principal_policy(self, policy: System.Security.Principal.PrincipalPolicy) -> None:
        ...

    def set_shadow_copy_files(self) -> None:
        warnings.warn("AppDomain.SetShadowCopyFiles has been deprecated and is not supported.", DeprecationWarning)

    def set_shadow_copy_path(self, path: str) -> None:
        warnings.warn("AppDomain.SetShadowCopyPath has been deprecated and is not supported.", DeprecationWarning)

    def set_thread_principal(self, principal: System.Security.Principal.IPrincipal) -> None:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def unload(domain: System.AppDomain) -> None:
        warnings.warn("Obsoletions.AppDomainCreateUnloadMessage", DeprecationWarning)


class ArithmeticException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class DivideByZeroException(System.ArithmeticException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class TupleExtensions(System.Object):
    """This class has no documentation."""


class IProgress(typing.Generic[System_IProgress_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def report(self, value: System_IProgress_T) -> None:
        ...


class Lazy(typing.Generic[System_Lazy_T, System_Lazy_TMetadata], System_Lazy):
    """This class has no documentation."""

    @property
    def is_value_created(self) -> bool:
        ...

    @property
    def value(self) -> System_Lazy_T:
        ...

    @property
    def metadata(self) -> System_Lazy_TMetadata:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: System_Lazy_T) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T]) -> None:
        ...

    @overload
    def __init__(self, is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata, is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata, is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata, mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata, mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    def to_string(self) -> str:
        ...


class Delegate(System.Object, System.ICloneable, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class InvocationListEnumerator(typing.Generic[System_Delegate_InvocationListEnumerator_TDelegate], typing.Iterable[System_Delegate_InvocationListEnumerator_TDelegate]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Delegate_InvocationListEnumerator_TDelegate:
            ...

        def __iter__(self) -> typing.Iterator[System_Delegate_InvocationListEnumerator_TDelegate]:
            ...

        def get_enumerator(self) -> System.Delegate.InvocationListEnumerator[System_Delegate_InvocationListEnumerator_TDelegate]:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def has_single_target(self) -> bool:
        ...

    @property
    def method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def target(self) -> System.Object:
        ...

    def __eq__(self, d_2: System.Delegate) -> bool:
        ...

    @overload
    def __init__(self, target: typing.Any, method: str) -> None:
        ...

    @overload
    def __init__(self, target: typing.Type, method: str) -> None:
        ...

    def __ne__(self, d_2: System.Delegate) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def combine(a: System.Delegate, b: System.Delegate) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def combine(*delegates: typing.Union[System.Delegate, typing.Iterable[System.Delegate]]) -> System.Delegate:
        ...

    def combine_impl(self, d: System.Delegate) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, first_argument: typing.Any, method: System.Reflection.MethodInfo) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str, ignore_case: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, first_argument: typing.Any, method: System.Reflection.MethodInfo, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str, ignore_case: bool, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, method: System.Reflection.MethodInfo) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str, ignore_case: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, method: System.Reflection.MethodInfo, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str, ignore_case: bool, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    def dynamic_invoke(self, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Object:
        ...

    def dynamic_invoke_impl(self, args: typing.List[System.Object]) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_list(self) -> typing.List[System.Delegate]:
        ...

    def get_method_impl(self) -> System.Reflection.MethodInfo:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def remove(source: System.Delegate, value: System.Delegate) -> System.Delegate:
        ...

    @staticmethod
    def remove_all(source: System.Delegate, value: System.Delegate) -> System.Delegate:
        ...

    def remove_impl(self, d: System.Delegate) -> System.Delegate:
        ...


class TypedReference:
    """This class has no documentation."""

    def equals(self, o: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_target_type(value: System.TypedReference) -> typing.Type:
        ...

    @staticmethod
    def make_typed_reference(target: typing.Any, flds: typing.List[System.Reflection.FieldInfo]) -> System.TypedReference:
        ...

    @staticmethod
    def set_typed_reference(target: System.TypedReference, value: typing.Any) -> None:
        ...

    @staticmethod
    def target_type_token(value: System.TypedReference) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def to_object(value: System.TypedReference) -> System.Object:
        ...


class Nullable(typing.Generic[System_Nullable_T]):
    """This class has no documentation."""

    @property
    def has_value(self) -> bool:
        ...

    @property
    def value(self) -> System_Nullable_T:
        ...

    def __init__(self, value: System_Nullable_T) -> None:
        ...

    def equals(self, other: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_underlying_type(nullable_type: typing.Type) -> typing.Type:
        ...

    @overload
    def get_value_or_default(self) -> System_Nullable_T:
        ...

    @overload
    def get_value_or_default(self, default_value: System_Nullable_T) -> System_Nullable_T:
        ...

    def to_string(self) -> str:
        ...


class ReadOnlySpan(typing.Generic[System_ReadOnlySpan_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_ReadOnlySpan_T]):
        """This class has no documentation."""

        @property
        def current(self) -> typing.Any:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def length(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    EMPTY: System.ReadOnlySpan[System_ReadOnlySpan_T]

    def __eq__(self, right: System.ReadOnlySpan[System_ReadOnlySpan_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlySpan_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlySpan_T], start: int, length: int) -> None:
        ...

    @overload
    def __init__(self, reference: System_ReadOnlySpan_T) -> None:
        ...

    def __ne__(self, right: System.ReadOnlySpan[System_ReadOnlySpan_T]) -> bool:
        ...

    def copy_to(self, destination: System.Span[System_ReadOnlySpan_T]) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        warnings.warn("Equals() on ReadOnlySpan will always throw an exception. Use the equality operator instead.", DeprecationWarning)

    def get_enumerator(self) -> System.ReadOnlySpan.Enumerator:
        ...

    def get_hash_code(self) -> int:
        warnings.warn("GetHashCode() on ReadOnlySpan will always throw an exception.", DeprecationWarning)

    def get_pinnable_reference(self) -> typing.Any:
        ...

    @overload
    def slice(self, start: int) -> System.ReadOnlySpan[System_ReadOnlySpan_T]:
        ...

    @overload
    def slice(self, start: int, length: int) -> System.ReadOnlySpan[System_ReadOnlySpan_T]:
        ...

    def to_array(self) -> typing.List[System_ReadOnlySpan_T]:
        ...

    def to_string(self) -> str:
        ...

    def try_copy_to(self, destination: System.Span[System_ReadOnlySpan_T]) -> bool:
        ...


class Random(System.Object):
    """This class has no documentation."""

    SHARED: System.Random

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, seed: int) -> None:
        ...

    @overload
    def get_hex_string(self, string_length: int, lowercase: bool = False) -> str:
        ...

    @overload
    def get_hex_string(self, destination: System.Span[str], lowercase: bool = False) -> None:
        ...

    def get_string(self, choices: System.ReadOnlySpan[str], length: int) -> str:
        ...

    @overload
    def next(self) -> int:
        ...

    @overload
    def next(self, max_value: int) -> int:
        ...

    @overload
    def next(self, min_value: int, max_value: int) -> int:
        ...

    @overload
    def next_bytes(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def next_bytes(self, buffer: System.Span[int]) -> None:
        ...

    def next_double(self) -> float:
        ...

    @overload
    def next_int_64(self) -> int:
        ...

    @overload
    def next_int_64(self, max_value: int) -> int:
        ...

    @overload
    def next_int_64(self, min_value: int, max_value: int) -> int:
        ...

    def next_single(self) -> float:
        ...

    def sample(self) -> float:
        ...


class ContextBoundObject(System.MarshalByRefObject, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class ContextMarshalException(System.SystemException):
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


class ContextStaticAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class FlagsAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StringComparison(IntEnum):
    """This class has no documentation."""

    CURRENT_CULTURE = 0

    CURRENT_CULTURE_IGNORE_CASE = 1

    INVARIANT_CULTURE = 2

    INVARIANT_CULTURE_IGNORE_CASE = 3

    ORDINAL = 4

    ORDINAL_IGNORE_CASE = 5


class StringSplitOptions(IntEnum):
    """This class has no documentation."""

    NONE = 0

    REMOVE_EMPTY_ENTRIES = 1

    TRIM_ENTRIES = 2


class MemoryExtensions(System.Object):
    """This class has no documentation."""

    class SpanSplitEnumerator(typing.Generic[System_MemoryExtensions_SpanSplitEnumerator_T], System.Collections.Generic.IEnumerator[System.Range], typing.Iterable[System_MemoryExtensions_SpanSplitEnumerator_T]):
        """This class has no documentation."""

        @property
        def source(self) -> System.ReadOnlySpan[System_MemoryExtensions_SpanSplitEnumerator_T]:
            ...

        @property
        def current(self) -> System.Range:
            ...

        def __iter__(self) -> typing.Iterator[System_MemoryExtensions_SpanSplitEnumerator_T]:
            ...

        def get_enumerator(self) -> System.MemoryExtensions.SpanSplitEnumerator[System_MemoryExtensions_SpanSplitEnumerator_T]:
            ...

        def move_next(self) -> bool:
            ...

    class TryWriteInterpolatedStringHandler:
        """This class has no documentation."""

        @overload
        def __init__(self, literal_length: int, formatted_count: int, destination: System.Span[str], should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            ...

        @overload
        def __init__(self, literal_length: int, formatted_count: int, destination: System.Span[str], provider: System.IFormatProvider, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> bool:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> bool:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> bool:
            ...

        @overload
        def append_formatted(self, value: str) -> bool:
            ...

        @overload
        def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> bool:
            ...

        def append_literal(self, value: str) -> bool:
            ...

    @staticmethod
    @overload
    def as_memory(text: str) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start: int) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start_index: System.Index) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start: int, length: int) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def as_memory(text: str, range: System.Range) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def as_span(text: str) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def as_span(text: str, start: int) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def as_span(text: str, start_index: System.Index) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def as_span(text: str, range: System.Range) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def as_span(text: str, start: int, length: int) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def compare_to(span: System.ReadOnlySpan[str], other: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    def contains(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def contains_any(span: System.Span[str], values: System.Buffers.SearchValues[str]) -> bool:
        ...

    @staticmethod
    @overload
    def contains_any(span: System.ReadOnlySpan[str], values: System.Buffers.SearchValues[str]) -> bool:
        ...

    @staticmethod
    def ends_with(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def enumerate_lines(span: System.ReadOnlySpan[str]) -> System.Text.SpanLineEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_lines(span: System.Span[str]) -> System.Text.SpanLineEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_runes(span: System.ReadOnlySpan[str]) -> System.Text.SpanRuneEnumerator:
        ...

    @staticmethod
    @overload
    def enumerate_runes(span: System.Span[str]) -> System.Text.SpanRuneEnumerator:
        ...

    @staticmethod
    def equals(span: System.ReadOnlySpan[str], other: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    def index_of(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def index_of_any(span: System.Span[str], values: System.Buffers.SearchValues[str]) -> int:
        ...

    @staticmethod
    @overload
    def index_of_any(span: System.ReadOnlySpan[str], values: System.Buffers.SearchValues[str]) -> int:
        ...

    @staticmethod
    def is_white_space(span: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    def last_index_of(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def split(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separator: str, options: System.StringSplitOptions = ...) -> int:
        ...

    @staticmethod
    @overload
    def split(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separator: System.ReadOnlySpan[str], options: System.StringSplitOptions = ...) -> int:
        ...

    @staticmethod
    def split_any(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separators: System.ReadOnlySpan[str], options: System.StringSplitOptions = ...) -> int:
        ...

    @staticmethod
    def starts_with(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[str], culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    def to_lower_invariant(source: System.ReadOnlySpan[str], destination: System.Span[str]) -> int:
        ...

    @staticmethod
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[str], culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    def to_upper_invariant(source: System.ReadOnlySpan[str], destination: System.Span[str]) -> int:
        ...

    @staticmethod
    @overload
    def trim(memory: System.Memory[str]) -> System.Memory[str]:
        ...

    @staticmethod
    @overload
    def trim(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim(span: System.Span[str]) -> System.Span[str]:
        ...

    @staticmethod
    @overload
    def trim_end(memory: System.Memory[str]) -> System.Memory[str]:
        ...

    @staticmethod
    @overload
    def trim_end(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_end(span: System.Span[str]) -> System.Span[str]:
        ...

    @staticmethod
    @overload
    def trim_start(memory: System.Memory[str]) -> System.Memory[str]:
        ...

    @staticmethod
    @overload
    def trim_start(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def trim_start(span: System.Span[str]) -> System.Span[str]:
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], handler: System.MemoryExtensions.TryWriteInterpolatedStringHandler, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], provider: System.IFormatProvider, handler: System.MemoryExtensions.TryWriteInterpolatedStringHandler, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], provider: System.IFormatProvider, format: System.Text.CompositeFormat, chars_written: typing.Optional[int], *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> typing.Tuple[bool, int]:
        ...


class WeakReference(typing.Generic[System_WeakReference_T], System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def track_resurrection(self) -> bool:
        ...

    @property
    def is_alive(self) -> bool:
        ...

    @property
    def target(self) -> System.Object:
        ...

    @target.setter
    def target(self, value: System.Object) -> None:
        ...

    @overload
    def __init__(self, target: typing.Any) -> None:
        ...

    @overload
    def __init__(self, target: typing.Any, track_resurrection: bool) -> None:
        ...

    @overload
    def __init__(self, target: System_WeakReference_T) -> None:
        ...

    @overload
    def __init__(self, target: System_WeakReference_T, track_resurrection: bool) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def set_target(self, target: System_WeakReference_T) -> None:
        ...

    def try_get_target(self, target: typing.Optional[System_WeakReference_T]) -> typing.Tuple[bool, System_WeakReference_T]:
        ...


class CannotUnloadAppDomainException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class MissingMemberException(System.MemberAccessException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def class_name(self) -> str:
        ...

    @class_name.setter
    def class_name(self, value: str) -> None:
        ...

    @property
    def member_name(self) -> str:
        ...

    @member_name.setter
    def member_name(self, value: str) -> None:
        ...

    @property
    def signature(self) -> typing.List[int]:
        ...

    @signature.setter
    def signature(self, value: typing.List[int]) -> None:
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
    def __init__(self, class_name: str, member_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class NotSupportedException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class PlatformNotSupportedException(System.NotSupportedException):
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


class ApplicationException(System.Exception):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ParamArrayAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class MissingFieldException(System.MissingMemberException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def message(self) -> str:
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
    def __init__(self, class_name: str, field_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class StringComparer(System.Object, System.Collections.IComparer, System.Collections.IEqualityComparer, System.Collections.Generic.IComparer[str], System.Collections.Generic.IEqualityComparer[str], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    INVARIANT_CULTURE: System.StringComparer

    INVARIANT_CULTURE_IGNORE_CASE: System.StringComparer

    CURRENT_CULTURE: System.StringComparer

    CURRENT_CULTURE_IGNORE_CASE: System.StringComparer

    ORDINAL: System.StringComparer

    ORDINAL_IGNORE_CASE: System.StringComparer

    @overload
    def compare(self, x: typing.Any, y: typing.Any) -> int:
        ...

    @overload
    def compare(self, x: str, y: str) -> int:
        ...

    @staticmethod
    @overload
    def create(culture: System.Globalization.CultureInfo, ignore_case: bool) -> System.StringComparer:
        ...

    @staticmethod
    @overload
    def create(culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> System.StringComparer:
        ...

    @overload
    def equals(self, x: typing.Any, y: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @staticmethod
    def from_comparison(comparison_type: System.StringComparison) -> System.StringComparer:
        ...

    @overload
    def get_hash_code(self, obj: typing.Any) -> int:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @staticmethod
    def is_well_known_culture_aware_comparer(comparer: System.Collections.Generic.IEqualityComparer[str], compare_info: typing.Optional[System.Globalization.CompareInfo], compare_options: typing.Optional[System.Globalization.CompareOptions]) -> typing.Tuple[bool, System.Globalization.CompareInfo, System.Globalization.CompareOptions]:
        ...

    @staticmethod
    def is_well_known_ordinal_comparer(comparer: System.Collections.Generic.IEqualityComparer[str], ignore_case: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...


class CultureAwareComparer(System.StringComparer, System.Collections.Generic.IAlternateEqualityComparer[System.ReadOnlySpan[str], str], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def compare(self, x: str, y: str) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class OrdinalComparer(System.StringComparer, System.Collections.Generic.IAlternateEqualityComparer[System.ReadOnlySpan[str], str]):
    """This class has no documentation."""

    def compare(self, x: str, y: str) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class UIntPtr(System.IEquatable[System_UIntPtr], System.IComparable[System_UIntPtr], System.ISpanFormattable, System.Runtime.Serialization.ISerializable, System.Numerics.IBinaryInteger[System_UIntPtr], System.Numerics.IMinMaxValue[System_UIntPtr], System.Numerics.IUnsignedNumber[System_UIntPtr], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: System.UIntPtr

    SIZE: int

    MAX_VALUE: System.UIntPtr

    MIN_VALUE: System.UIntPtr

    def __add__(self, offset: int) -> System.UIntPtr:
        ...

    def __eq__(self, value_2: System.UIntPtr) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.UIntPtr) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.UIntPtr) -> bool:
        ...

    def __iadd__(self, offset: int) -> System.UIntPtr:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    def __isub__(self, offset: int) -> System.UIntPtr:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.UIntPtr) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.UIntPtr) -> bool:
        ...

    def __ne__(self, value_2: System.UIntPtr) -> bool:
        ...

    def __sub__(self, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    def add(pointer: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    def big_mul(left: System.UIntPtr, right: System.UIntPtr, lower: typing.Optional[System.UIntPtr]) -> typing.Tuple[System.UIntPtr, System.UIntPtr]:
        ...

    @staticmethod
    def clamp(value: System.UIntPtr, min: System.UIntPtr, max: System.UIntPtr) -> System.UIntPtr:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.UIntPtr) -> int:
        ...

    @staticmethod
    def div_rem(left: System.UIntPtr, right: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.UIntPtr) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def log_2(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def max(x: System.UIntPtr, y: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def min(x: System.UIntPtr, y: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    def pop_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def rotate_left(value: System.UIntPtr, rotate_amount: int) -> System.UIntPtr:
        ...

    @staticmethod
    def rotate_right(value: System.UIntPtr, rotate_amount: int) -> System.UIntPtr:
        ...

    @staticmethod
    def sign(value: System.UIntPtr) -> int:
        ...

    @staticmethod
    def subtract(pointer: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    def to_pointer(self) -> typing.Any:
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

    def to_u_int_32(self) -> int:
        ...

    def to_u_int_64(self) -> int:
        ...

    @staticmethod
    def trailing_zero_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...


class STAThreadAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class MTAThreadAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AppContext(System.Object):
    """This class has no documentation."""

    BASE_DIRECTORY: str

    TARGET_FRAMEWORK_NAME: str

    @staticmethod
    def get_data(name: str) -> System.Object:
        ...

    @staticmethod
    def set_data(name: str, data: typing.Any) -> None:
        ...

    @staticmethod
    def set_switch(switch_name: str, is_enabled: bool) -> None:
        ...

    @staticmethod
    def try_get_switch(switch_name: str, is_enabled: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...


class InvalidTimeZoneException(System.Exception):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class Memory(typing.Generic[System_Memory_T], System.IEquatable[System_Memory]):
    """This class has no documentation."""

    EMPTY: System.Memory[System_Memory_T]

    @property
    def length(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def span(self) -> System.Span[System_Memory_T]:
        ...

    @overload
    def __init__(self, array: typing.List[System_Memory_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_Memory_T], start: int, length: int) -> None:
        ...

    def copy_to(self, destination: System.Memory[System_Memory_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Memory[System_Memory_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def pin(self) -> System.Buffers.MemoryHandle:
        ...

    @overload
    def slice(self, start: int) -> System.Memory[System_Memory_T]:
        ...

    @overload
    def slice(self, start: int, length: int) -> System.Memory[System_Memory_T]:
        ...

    def to_array(self) -> typing.List[System_Memory_T]:
        ...

    def to_string(self) -> str:
        ...

    def try_copy_to(self, destination: System.Memory[System_Memory_T]) -> bool:
        ...


class Int128(System.Numerics.ISignedNumber[System_Int128], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[System_Int128]):
    """This class has no documentation."""

    MIN_VALUE: System.Int128

    MAX_VALUE: System.Int128

    ONE: System.Int128

    ZERO: System.Int128

    NEGATIVE_ONE: System.Int128

    @overload
    def __add__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __add__(self, right: System.Int128) -> System.Int128:
        ...

    def __and__(self, right: System.Int128) -> System.Int128:
        ...

    def __eq__(self, right: System.Int128) -> bool:
        ...

    def __ge__(self, right: System.Int128) -> bool:
        ...

    def __gt__(self, right: System.Int128) -> bool:
        ...

    @overload
    def __iadd__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __iadd__(self, right: System.Int128) -> System.Int128:
        ...

    def __iand__(self, right: System.Int128) -> System.Int128:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Int128:
        ...

    def __imod__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __imul__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __imul__(self, right: System.Int128) -> System.Int128:
        ...

    def __init__(self, upper: int, lower: int) -> None:
        ...

    def __invert__(self) -> System.Int128:
        ...

    def __ior__(self, right: System.Int128) -> System.Int128:
        ...

    def __irshift__(self, shift_amount: int) -> System.Int128:
        ...

    @overload
    def __isub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __isub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __itruediv__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __itruediv__(self, right: System.Int128) -> System.Int128:
        ...

    def __ixor__(self, right: System.Int128) -> System.Int128:
        ...

    def __le__(self, right: System.Int128) -> bool:
        ...

    def __lshift__(self, shift_amount: int) -> System.Int128:
        ...

    def __lt__(self, right: System.Int128) -> bool:
        ...

    def __mod__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __mul__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __mul__(self, right: System.Int128) -> System.Int128:
        ...

    def __ne__(self, right: System.Int128) -> bool:
        ...

    @overload
    def __neg__(self) -> System.Int128:
        ...

    @overload
    def __neg__(self) -> System.Int128:
        ...

    def __or__(self, right: System.Int128) -> System.Int128:
        ...

    def __pos__(self) -> System.Int128:
        ...

    def __rshift__(self, shift_amount: int) -> System.Int128:
        ...

    @overload
    def __sub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __sub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __truediv__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __truediv__(self, right: System.Int128) -> System.Int128:
        ...

    def __xor__(self, right: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def abs(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def big_mul(left: System.Int128, right: System.Int128, lower: typing.Optional[System.Int128]) -> typing.Tuple[System.Int128, System.Int128]:
        ...

    @staticmethod
    def clamp(value: System.Int128, min: System.Int128, max: System.Int128) -> System.Int128:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Int128) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.Int128, sign: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def div_rem(left: System.Int128, right: System.Int128) -> System.ValueTuple[System.Int128, System.Int128]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Int128) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.Int128) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def log_2(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def max(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def max_magnitude(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def min(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def min_magnitude(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    def pop_count(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def rotate_left(value: System.Int128, rotate_amount: int) -> System.Int128:
        ...

    @staticmethod
    def rotate_right(value: System.Int128, rotate_amount: int) -> System.Int128:
        ...

    @staticmethod
    def sign(value: System.Int128) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: System.Int128) -> System.Int128:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...


class RankException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class MissingMethodException(System.MissingMemberException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
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
    def __init__(self, class_name: str, method_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class AccessViolationException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class UnitySerializationHolder(System.Object, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IObjectReference):
    """This class has no documentation."""

    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_real_object(self, context: System.Runtime.Serialization.StreamingContext) -> System.Object:
        ...


class Half(System.IComparable[System_Half], System.ISpanFormattable, System.IEquatable[System_Half], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[System_Half]):
    """This class has no documentation."""

    EPSILON: System.Half

    POSITIVE_INFINITY: System.Half

    NEGATIVE_INFINITY: System.Half

    NA_N: System.Half

    MIN_VALUE: System.Half

    MAX_VALUE: System.Half

    E: System.Half

    PI: System.Half

    TAU: System.Half

    NEGATIVE_ZERO: System.Half

    MULTIPLICATIVE_IDENTITY: System.Half

    ONE: System.Half

    ZERO: System.Half

    NEGATIVE_ONE: System.Half

    def __add__(self, right: System.Half) -> System.Half:
        ...

    def __eq__(self, right: System.Half) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Half) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Half) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Half) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Half) -> bool:
        ...

    def __iadd__(self, right: System.Half) -> System.Half:
        ...

    def __imod__(self, right: System.Half) -> System.Half:
        ...

    def __imul__(self, right: System.Half) -> System.Half:
        ...

    def __isub__(self, right: System.Half) -> System.Half:
        ...

    def __itruediv__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.Half) -> bool:
        ...

    @overload
    def __le__(self, other: System.Half) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Half) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Half) -> bool:
        ...

    def __mod__(self, right: System.Half) -> System.Half:
        ...

    def __mul__(self, right: System.Half) -> System.Half:
        ...

    def __ne__(self, right: System.Half) -> bool:
        ...

    def __neg__(self) -> System.Half:
        ...

    def __pos__(self) -> System.Half:
        ...

    def __sub__(self, right: System.Half) -> System.Half:
        ...

    def __truediv__(self, right: System.Half) -> System.Half:
        ...

    @staticmethod
    def abs(value: System.Half) -> System.Half:
        ...

    @staticmethod
    def acos(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def acosh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def acos_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asin(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asinh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asin_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_2(y: System.Half, x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_2_pi(y: System.Half, x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atanh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def bit_decrement(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def bit_increment(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cbrt(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def ceiling(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def clamp(value: System.Half, min: System.Half, max: System.Half) -> System.Half:
        ...

    @staticmethod
    def clamp_native(value: System.Half, min: System.Half, max: System.Half) -> System.Half:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, other: System.Half) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.Half, sign: System.Half) -> System.Half:
        ...

    @staticmethod
    def cos(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cosh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cos_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Half) -> System.Half:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Half) -> bool:
        ...

    @staticmethod
    def exp(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_10(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_10_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_2(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_2_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def floor(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Half, right: System.Half, addend: System.Half) -> System.Half:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def hypot(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def ieee_754_remainder(left: System.Half, right: System.Half) -> System.Half:
        ...

    @staticmethod
    def i_log_b(x: System.Half) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_finite(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_infinity(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_na_n(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_negative_infinity(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_normal(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_real_number(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_subnormal(value: System.Half) -> bool:
        ...

    @staticmethod
    def lerp(value_1: System.Half, value_2: System.Half, amount: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def log(x: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def log(x: System.Half, new_base: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_10(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_10_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_2(value: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_2_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def max(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_magnitude(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_magnitude_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_native(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_magnitude(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_magnitude_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_native(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Half, right: System.Half, addend: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Half:
        ...

    @staticmethod
    def pow(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Half) -> System.Half:
        ...

    @staticmethod
    def reciprocal_estimate(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def root_n(x: System.Half, n: int) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, digits: int) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, mode: System.MidpointRounding) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, digits: int, mode: System.MidpointRounding) -> System.Half:
        ...

    @staticmethod
    def scale_b(x: System.Half, n: int) -> System.Half:
        ...

    @staticmethod
    def sign(value: System.Half) -> int:
        ...

    @staticmethod
    def sin(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sin_cos(x: System.Half) -> System.ValueTuple[System.Half, System.Half]:
        ...

    @staticmethod
    def sin_cos_pi(x: System.Half) -> System.ValueTuple[System.Half, System.Half]:
        ...

    @staticmethod
    def sinh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sin_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sqrt(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tan(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tanh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tan_pi(x: System.Half) -> System.Half:
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
    def truncate(x: System.Half) -> System.Half:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...


class Activator(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def create_instance(type: typing.Type, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, non_public: bool) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, args: typing.List[System.Object], activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...


class TimeoutException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class OverflowException(System.ArithmeticException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class Boolean(System.IComparable[bool], System.IConvertible, System.IEquatable[bool], System.ISpanParsable[bool]):
    """This class has no documentation."""

    TRUE_STRING: str = ...

    FALSE_STRING: str = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: bool) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: bool) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: bool) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: bool) -> bool:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: bool) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: bool) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    @overload
    def parse(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def parse(value: System.ReadOnlySpan[str]) -> bool:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(value: str, result: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...

    @staticmethod
    @overload
    def try_parse(value: System.ReadOnlySpan[str], result: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...


class ArgumentException(System.SystemException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def param_name(self) -> str:
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
    def __init__(self, message: str, param_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, param_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def throw_if_null_or_empty(argument: str, param_name: str = None) -> None:
        ...

    @staticmethod
    def throw_if_null_or_white_space(argument: str, param_name: str = None) -> None:
        ...


class DuplicateWaitObjectException(System.ArgumentException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, parameter_name: str) -> None:
        ...

    @overload
    def __init__(self, parameter_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class AttributeTargets(IntEnum):
    """This class has no documentation."""

    ASSEMBLY = ...

    MODULE = ...

    CLASS = ...

    STRUCT = ...

    ENUM = ...

    CONSTRUCTOR = ...

    METHOD = ...

    PROPERTY = ...

    FIELD = ...

    EVENT = ...

    INTERFACE = ...

    PARAMETER = ...

    DELEGATE = ...

    RETURN_VALUE = ...

    GENERIC_PARAMETER = ...

    ALL = ...


class HashCode:
    """This class has no documentation."""

    def add_bytes(self, value: System.ReadOnlySpan[int]) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        warnings.warn("HashCode is a mutable struct and should not be compared with other HashCodes.", DeprecationWarning)

    def get_hash_code(self) -> int:
        warnings.warn("HashCode is a mutable struct and should not be compared with other HashCodes. Use ToHashCode to retrieve the computed hash code.", DeprecationWarning)

    def to_hash_code(self) -> int:
        ...


class CharEnumerator(System.Object, System.Collections.Generic.IEnumerator[str], System.ICloneable):
    """This class has no documentation."""

    @property
    def current(self) -> str:
        ...

    def clone(self) -> System.Object:
        ...

    def dispose(self) -> None:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class String(System.Object, System.IComparable[str], System.IConvertible, System.Collections.Generic.IEnumerable[str], System.IEquatable[str], System.ICloneable, System.ISpanParsable[str], typing.Iterable[str]):
    """This class has no documentation."""

    EMPTY: str

    @property
    def length(self) -> int:
        ...

    def __eq__(self, b: str) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: str) -> bool:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: str) -> bool:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any, start_index: int, length: int) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any, start_index: int, length: int, enc: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[str]) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[str], start_index: int, length: int) -> None:
        ...

    @overload
    def __init__(self, c: str, count: int) -> None:
        ...

    @overload
    def __init__(self, value: System.ReadOnlySpan[str]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[str]:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: str) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: str) -> bool:
        ...

    def __ne__(self, b: str) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, ignore_case: bool) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, ignore_case: bool) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, ignore_case: bool, culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def compare_ordinal(str_a: str, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def compare_ordinal(str_a: str, index_a: int, str_b: str, index_b: int, length: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(*args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def concat(values: System.Collections.Generic.IEnumerable[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str, str_2: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str, str_2: str, str_3: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str], str_2: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str], str_2: System.ReadOnlySpan[str], str_3: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(*values: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def contains(self, value: str) -> bool:
        ...

    @overload
    def contains(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def contains(self, value: System.Text.Rune) -> bool:
        ...

    @overload
    def contains(self, value: System.Text.Rune, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    def copy(str: str) -> str:
        warnings.warn("This API should not be used to create mutable strings. See https://go.microsoft.com/fwlink/?linkid=2084035 for alternatives.", DeprecationWarning)

    @overload
    def copy_to(self, source_index: int, destination: typing.List[str], destination_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[str]) -> None:
        ...

    @staticmethod
    @overload
    def create(provider: System.IFormatProvider, handler: System.Runtime.CompilerServices.DefaultInterpolatedStringHandler) -> str:
        ...

    @staticmethod
    @overload
    def create(provider: System.IFormatProvider, initial_buffer: System.Span[str], handler: System.Runtime.CompilerServices.DefaultInterpolatedStringHandler) -> str:
        ...

    @overload
    def ends_with(self, value: str) -> bool:
        ...

    @overload
    def ends_with(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def ends_with(self, value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> bool:
        ...

    @overload
    def ends_with(self, value: System.Text.Rune) -> bool:
        ...

    @overload
    def ends_with(self, value: System.Text.Rune, comparison_type: System.StringComparison) -> bool:
        ...

    def enumerate_runes(self) -> System.Text.StringRuneEnumerator:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: str) -> bool:
        ...

    @overload
    def equals(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def equals(a: str, b: str) -> bool:
        ...

    @staticmethod
    @overload
    def equals(a: str, b: str, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: System.Text.CompositeFormat, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    def get_enumerator(self) -> System.CharEnumerator:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    @overload
    def get_hash_code(self, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def get_hash_code(value: System.ReadOnlySpan[str]) -> int:
        ...

    @staticmethod
    @overload
    def get_hash_code(value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        ...

    def get_pinnable_reference(self) -> typing.Any:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @overload
    def index_of(self, value: str) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int) -> int:
        ...

    @overload
    def index_of(self, value: str, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune, start_index: int) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: System.Text.Rune, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str]) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str], start_index: int) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str], start_index: int, count: int) -> int:
        ...

    def insert(self, start_index: int, value: str) -> str:
        ...

    @staticmethod
    def intern(str: str) -> str:
        ...

    @staticmethod
    def is_interned(str: str) -> str:
        ...

    @overload
    def is_normalized(self) -> bool:
        ...

    @overload
    def is_normalized(self, normalization_form: System.Text.NormalizationForm) -> bool:
        ...

    @staticmethod
    def is_null_or_empty(value: str) -> bool:
        ...

    @staticmethod
    def is_null_or_white_space(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def join(separator: str, *value: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, value: typing.List[str], start_index: int, count: int) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, values: System.Collections.Generic.IEnumerable[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @overload
    def last_index_of(self, value: str) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, value: str, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: System.Text.Rune, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str]) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str], start_index: int) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str], start_index: int, count: int) -> int:
        ...

    @overload
    def normalize(self) -> str:
        ...

    @overload
    def normalize(self, normalization_form: System.Text.NormalizationForm) -> str:
        ...

    @overload
    def pad_left(self, total_width: int) -> str:
        ...

    @overload
    def pad_left(self, total_width: int, padding_char: str) -> str:
        ...

    @overload
    def pad_right(self, total_width: int) -> str:
        ...

    @overload
    def pad_right(self, total_width: int, padding_char: str) -> str:
        ...

    @overload
    def remove(self, start_index: int, count: int) -> str:
        ...

    @overload
    def remove(self, start_index: int) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str, comparison_type: System.StringComparison) -> str:
        ...

    @overload
    def replace(self, old_char: str, new_char: str) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str) -> str:
        ...

    @overload
    def replace(self, old_rune: System.Text.Rune, new_rune: System.Text.Rune) -> str:
        ...

    @overload
    def replace_line_endings(self) -> str:
        ...

    @overload
    def replace_line_endings(self, replacement_text: str) -> str:
        ...

    @overload
    def split(self, separator: str, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: str, count: int, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: System.Text.Rune, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: System.Text.Rune, count: int, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, *separator: typing.Union[str, typing.Iterable[str]]) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], count: int) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], options: System.StringSplitOptions) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], count: int, options: System.StringSplitOptions) -> typing.List[str]:
        ...

    @overload
    def starts_with(self, value: str) -> bool:
        ...

    @overload
    def starts_with(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def starts_with(self, value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> bool:
        ...

    @overload
    def starts_with(self, value: System.Text.Rune) -> bool:
        ...

    @overload
    def starts_with(self, value: System.Text.Rune, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def substring(self, start_index: int) -> str:
        ...

    @overload
    def substring(self, start_index: int, length: int) -> str:
        ...

    @overload
    def to_char_array(self) -> typing.List[str]:
        ...

    @overload
    def to_char_array(self, start_index: int, length: int) -> typing.List[str]:
        ...

    @overload
    def to_lower(self) -> str:
        ...

    @overload
    def to_lower(self, culture: System.Globalization.CultureInfo) -> str:
        ...

    def to_lower_invariant(self) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_upper(self) -> str:
        ...

    @overload
    def to_upper(self, culture: System.Globalization.CultureInfo) -> str:
        ...

    def to_upper_invariant(self) -> str:
        ...

    @overload
    def trim(self) -> str:
        ...

    @overload
    def trim(self, trim_char: str) -> str:
        ...

    @overload
    def trim(self, trim_rune: System.Text.Rune) -> str:
        ...

    @overload
    def trim(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def trim_end(self) -> str:
        ...

    @overload
    def trim_end(self, trim_char: str) -> str:
        ...

    @overload
    def trim_end(self, trim_rune: System.Text.Rune) -> str:
        ...

    @overload
    def trim_end(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def trim_start(self) -> str:
        ...

    @overload
    def trim_start(self, trim_char: str) -> str:
        ...

    @overload
    def trim_start(self, trim_rune: System.Text.Rune) -> str:
        ...

    @overload
    def trim_start(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    def try_copy_to(self, destination: System.Span[str]) -> bool:
        ...


class LoaderOptimization(IntEnum):
    """This class has no documentation."""

    DISALLOW_BINDINGS = 4

    DOMAIN_MASK = 3

    MULTI_DOMAIN = 2

    MULTI_DOMAIN_HOST = 3

    NOT_SPECIFIED = 0

    SINGLE_DOMAIN = 1


class ThreadStaticAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StackOverflowException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class Decimal(System.ISpanFormattable, System.IComparable[float], System.IConvertible, System.IEquatable[float], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Numerics.IFloatingPoint[float], System.Numerics.IMinMaxValue[float], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: float = 0

    ONE: float = 1

    MINUS_ONE: float = -1

    MAX_VALUE: float = 79228162514264337593543950335

    MIN_VALUE: float = -79228162514264337593543950335

    @property
    def scale(self) -> int:
        ...

    def __add__(self, d_2: float) -> float:
        ...

    def __eq__(self, d_2: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, d_2: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, d_2: float) -> bool:
        ...

    def __iadd__(self, d_2: float) -> float:
        ...

    def __imod__(self, d_2: float) -> float:
        ...

    def __imul__(self, d_2: float) -> float:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, bits: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, bits: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def __init__(self, lo: int, mid: int, hi: int, is_negative: bool, scale: int) -> None:
        ...

    def __isub__(self, d_2: float) -> float:
        ...

    def __itruediv__(self, d_2: float) -> float:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, d_2: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, d_2: float) -> bool:
        ...

    def __mod__(self, d_2: float) -> float:
        ...

    def __mul__(self, d_2: float) -> float:
        ...

    def __ne__(self, d_2: float) -> bool:
        ...

    def __neg__(self) -> float:
        ...

    def __pos__(self) -> float:
        ...

    def __sub__(self, d_2: float) -> float:
        ...

    def __truediv__(self, d_2: float) -> float:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def add(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def ceiling(d: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def compare(d_1: float, d_2: float) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def divide(d_1: float, d_2: float) -> float:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: float) -> bool:
        ...

    @staticmethod
    @overload
    def equals(d_1: float, d_2: float) -> bool:
        ...

    @staticmethod
    def floor(d: float) -> float:
        ...

    @staticmethod
    def from_oa_currency(cy: int) -> float:
        ...

    @staticmethod
    @overload
    def get_bits(d: float) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bits(d: float, destination: System.Span[int]) -> int:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_canonical(value: float) -> bool:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_negative(value: float) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def negate(d: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def remainder(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def sign(d: float) -> int:
        ...

    @staticmethod
    def subtract(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def to_byte(value: float) -> int:
        ...

    @staticmethod
    def to_double(d: float) -> float:
        ...

    @staticmethod
    def to_int_16(value: float) -> int:
        ...

    @staticmethod
    def to_int_32(d: float) -> int:
        ...

    @staticmethod
    def to_int_64(d: float) -> int:
        ...

    @staticmethod
    def to_oa_currency(value: float) -> int:
        ...

    @staticmethod
    def to_s_byte(value: float) -> int:
        ...

    @staticmethod
    def to_single(d: float) -> float:
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
    def to_u_int_16(value: float) -> int:
        ...

    @staticmethod
    def to_u_int_32(d: float) -> int:
        ...

    @staticmethod
    def to_u_int_64(d: float) -> int:
        ...

    @staticmethod
    def truncate(d: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_get_bits(d: float, destination: System.Span[int], values_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class SByte(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
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
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class BadImageFormatException(System.SystemException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def file_name(self) -> str:
        ...

    @property
    def fusion_log(self) -> str:
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
    def __init__(self, message: str, file_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class LoaderOptimizationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.LoaderOptimization:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: System.LoaderOptimization) -> None:
        ...


class UInt16(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = 0

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class MulticastNotSupportedException(System.SystemException):
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


class InsufficientExecutionStackException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class NonSerializedAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class NullReferenceException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class NotImplementedException(System.SystemException):
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


class UnauthorizedAccessException(System.SystemException):
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


class TimeSpan(System.IComparable[datetime.timedelta], System.IEquatable[datetime.timedelta], System.ISpanFormattable, System.ISpanParsable[datetime.timedelta], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    NANOSECONDS_PER_TICK: int = 100

    TICKS_PER_MICROSECOND: int = 10

    TICKS_PER_MILLISECOND: int = ...

    TICKS_PER_SECOND: int = ...

    TICKS_PER_MINUTE: int = ...

    TICKS_PER_HOUR: int = ...

    TICKS_PER_DAY: int = ...

    MICROSECONDS_PER_MILLISECOND: int = ...

    MICROSECONDS_PER_SECOND: int = ...

    MICROSECONDS_PER_MINUTE: int = ...

    MICROSECONDS_PER_HOUR: int = ...

    MICROSECONDS_PER_DAY: int = ...

    MILLISECONDS_PER_SECOND: int = ...

    MILLISECONDS_PER_MINUTE: int = ...

    MILLISECONDS_PER_HOUR: int = ...

    MILLISECONDS_PER_DAY: int = ...

    SECONDS_PER_MINUTE: int = ...

    SECONDS_PER_HOUR: int = ...

    SECONDS_PER_DAY: int = ...

    MINUTES_PER_HOUR: int = ...

    MINUTES_PER_DAY: int = ...

    HOURS_PER_DAY: int = ...

    ZERO: datetime.timedelta = ...

    MAX_VALUE: datetime.timedelta = ...

    MIN_VALUE: datetime.timedelta = ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def days(self) -> int:
        ...

    @property
    def hours(self) -> int:
        ...

    @property
    def milliseconds(self) -> int:
        ...

    @property
    def microseconds(self) -> int:
        ...

    @property
    def nanoseconds(self) -> int:
        ...

    @property
    def minutes(self) -> int:
        ...

    @property
    def seconds(self) -> int:
        ...

    @property
    def total_days(self) -> float:
        ...

    @property
    def total_hours(self) -> float:
        ...

    @property
    def total_milliseconds(self) -> float:
        ...

    @property
    def total_microseconds(self) -> float:
        ...

    @property
    def total_nanoseconds(self) -> float:
        ...

    @property
    def total_minutes(self) -> float:
        ...

    @property
    def total_seconds(self) -> float:
        ...

    def __add__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    def __eq__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __ge__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __gt__(self, t_2: datetime.timedelta) -> bool:
        ...

    def __iadd__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __imul__(self, factor: float) -> datetime.timedelta:
        ...

    @overload
    def __imul__(self, time_span: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        ...

    @overload
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int) -> None:
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int) -> None:
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int, microseconds: int) -> None:
        ...

    def __isub__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __itruediv__(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def __itruediv__(self, t_2: datetime.timedelta) -> float:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __le__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __lt__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __mul__(self, factor: float) -> datetime.timedelta:
        ...

    @overload
    def __mul__(self, time_span: datetime.timedelta) -> datetime.timedelta:
        ...

    def __ne__(self, t_2: datetime.timedelta) -> bool:
        ...

    def __neg__(self) -> datetime.timedelta:
        ...

    def __pos__(self) -> datetime.timedelta:
        ...

    def __sub__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __truediv__(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def __truediv__(self, t_2: datetime.timedelta) -> float:
        ...

    def add(self, ts: datetime.timedelta) -> datetime.timedelta:
        ...

    @staticmethod
    def compare(t_1: datetime.timedelta, t_2: datetime.timedelta) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: datetime.timedelta) -> int:
        ...

    @overload
    def divide(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def divide(self, ts: datetime.timedelta) -> float:
        ...

    def duration(self) -> datetime.timedelta:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def equals(t_1: datetime.timedelta, t_2: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def from_days(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_days(days: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_days(days: int, hours: int = 0, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_hours(hours: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_hours(hours: int, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_hours(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_microseconds(microseconds: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_microseconds(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_milliseconds(milliseconds: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_milliseconds(milliseconds: int, microseconds: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_milliseconds(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_minutes(minutes: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_minutes(minutes: int, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_minutes(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_seconds(seconds: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_seconds(seconds: int, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_seconds(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    def from_ticks(value: int) -> datetime.timedelta:
        ...

    def get_hash_code(self) -> int:
        ...

    def multiply(self, factor: float) -> datetime.timedelta:
        ...

    def negate(self) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider = None) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles = ...) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles = ...) -> datetime.timedelta:
        ...

    def subtract(self, ts: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...


class BitConverter(System.Object):
    """This class has no documentation."""

    IS_LITTLE_ENDIAN: bool = True

    @staticmethod
    def b_float_16_to_int_16_bits(value: System.Numerics.BFloat16) -> int:
        ...

    @staticmethod
    def b_float_16_to_u_int_16_bits(value: System.Numerics.BFloat16) -> int:
        ...

    @staticmethod
    def double_to_int_64_bits(value: float) -> int:
        ...

    @staticmethod
    def double_to_u_int_64_bits(value: float) -> int:
        ...

    @staticmethod
    @overload
    def get_bytes(value: bool) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: str) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: int) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.Int128) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.UInt128) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.Numerics.BFloat16) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.Half) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bytes(value: float) -> typing.List[int]:
        ...

    @staticmethod
    def half_to_int_16_bits(value: System.Half) -> int:
        ...

    @staticmethod
    def half_to_u_int_16_bits(value: System.Half) -> int:
        ...

    @staticmethod
    def int_16_bits_to_b_float_16(value: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def int_16_bits_to_half(value: int) -> System.Half:
        ...

    @staticmethod
    def int_32_bits_to_single(value: int) -> float:
        ...

    @staticmethod
    def int_64_bits_to_double(value: int) -> float:
        ...

    @staticmethod
    def single_to_int_32_bits(value: float) -> int:
        ...

    @staticmethod
    def single_to_u_int_32_bits(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_b_float_16(value: typing.List[int], start_index: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def to_b_float_16(value: System.ReadOnlySpan[int]) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.List[int], start_index: int) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.List[int], start_index: int) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: System.ReadOnlySpan[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.List[int], start_index: int) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    @overload
    def to_half(value: typing.List[int], start_index: int) -> System.Half:
        ...

    @staticmethod
    @overload
    def to_half(value: System.ReadOnlySpan[int]) -> System.Half:
        ...

    @staticmethod
    @overload
    def to_int_128(value: typing.List[int], start_index: int) -> System.Int128:
        ...

    @staticmethod
    @overload
    def to_int_128(value: System.ReadOnlySpan[int]) -> System.Int128:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.List[int], start_index: int) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int], start_index: int, length: int) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int], start_index: int) -> str:
        ...

    @staticmethod
    @overload
    def to_u_int_128(value: typing.List[int], start_index: int) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def to_u_int_128(value: System.ReadOnlySpan[int]) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.List[int], start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: bool) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: str) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.Int128) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.UInt128) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.Half) -> bool:
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: float) -> bool:
        ...

    @staticmethod
    def u_int_16_bits_to_b_float_16(value: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def u_int_16_bits_to_half(value: int) -> System.Half:
        ...

    @staticmethod
    def u_int_32_bits_to_single(value: int) -> float:
        ...

    @staticmethod
    def u_int_64_bits_to_double(value: int) -> float:
        ...


class TypeLoadException(System.SystemException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def type_name(self) -> str:
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

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class NotFiniteNumberException(System.ArithmeticException):
    """This class has no documentation."""

    @property
    def offending_number(self) -> float:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, offending_number: float) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, offending_number: float) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, offending_number: float, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class TypeInitializationException(System.SystemException):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        ...

    def __init__(self, full_type_name: str, inner_exception: System.Exception) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class AttributeUsageAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def valid_on(self) -> System.AttributeTargets:
        ...

    @property
    def allow_multiple(self) -> bool:
        ...

    @allow_multiple.setter
    def allow_multiple(self, value: bool) -> None:
        ...

    @property
    def inherited(self) -> bool:
        ...

    @inherited.setter
    def inherited(self, value: bool) -> None:
        ...

    def __init__(self, valid_on: System.AttributeTargets) -> None:
        ...


class IntPtr(System.IEquatable[System_IntPtr], System.IComparable[System_IntPtr], System.ISpanFormattable, System.Runtime.Serialization.ISerializable, System.Numerics.IBinaryInteger[System_IntPtr], System.Numerics.IMinMaxValue[System_IntPtr], System.Numerics.ISignedNumber[System_IntPtr], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: System.IntPtr

    SIZE: int

    MAX_VALUE: System.IntPtr

    MIN_VALUE: System.IntPtr

    def __add__(self, offset: int) -> System.IntPtr:
        ...

    def __eq__(self, value_2: System.IntPtr) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.IntPtr) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.IntPtr) -> bool:
        ...

    def __iadd__(self, offset: int) -> System.IntPtr:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    def __isub__(self, offset: int) -> System.IntPtr:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.IntPtr) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.IntPtr) -> bool:
        ...

    def __ne__(self, value_2: System.IntPtr) -> bool:
        ...

    def __sub__(self, offset: int) -> System.IntPtr:
        ...

    @staticmethod
    def abs(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def add(pointer: System.IntPtr, offset: int) -> System.IntPtr:
        ...

    @staticmethod
    def big_mul(left: System.IntPtr, right: System.IntPtr, lower: typing.Optional[System.IntPtr]) -> typing.Tuple[System.IntPtr, System.IntPtr]:
        ...

    @staticmethod
    def clamp(value: System.IntPtr, min: System.IntPtr, max: System.IntPtr) -> System.IntPtr:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.IntPtr) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.IntPtr, sign: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def div_rem(left: System.IntPtr, right: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.IntPtr) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def log_2(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def max(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def max_magnitude(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def min(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def min_magnitude(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    def pop_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def rotate_left(value: System.IntPtr, rotate_amount: int) -> System.IntPtr:
        ...

    @staticmethod
    def rotate_right(value: System.IntPtr, rotate_amount: int) -> System.IntPtr:
        ...

    @staticmethod
    def sign(value: System.IntPtr) -> int:
        ...

    @staticmethod
    def subtract(pointer: System.IntPtr, offset: int) -> System.IntPtr:
        ...

    def to_int_32(self) -> int:
        ...

    def to_int_64(self) -> int:
        ...

    def to_pointer(self) -> typing.Any:
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
    def trailing_zero_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...


class TypeAccessException(System.TypeLoadException):
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


class Progress(typing.Generic[System_Progress_T], System.Object, System.IProgress[System_Progress_T]):
    """This class has no documentation."""

    @property
    def progress_changed(self) -> _EventContainer[typing.Callable[[System.Object, System_Progress_T], typing.Any], typing.Any]:
        ...

    @progress_changed.setter
    def progress_changed(self, value: _EventContainer[typing.Callable[[System.Object, System_Progress_T], typing.Any], typing.Any]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, handler: typing.Callable[[System_Progress_T], typing.Any]) -> None:
        ...

    def on_report(self, value: System_Progress_T) -> None:
        ...


class ReadOnlyMemory(typing.Generic[System_ReadOnlyMemory_T], System.IEquatable[System_ReadOnlyMemory]):
    """This class has no documentation."""

    EMPTY: System.ReadOnlyMemory[System_ReadOnlyMemory_T]

    @property
    def length(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def span(self) -> System.ReadOnlySpan[System_ReadOnlyMemory_T]:
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlyMemory_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlyMemory_T], start: int, length: int) -> None:
        ...

    def copy_to(self, destination: System.Memory[System_ReadOnlyMemory_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.ReadOnlyMemory[System_ReadOnlyMemory_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def pin(self) -> System.Buffers.MemoryHandle:
        ...

    @overload
    def slice(self, start: int) -> System.ReadOnlyMemory[System_ReadOnlyMemory_T]:
        ...

    @overload
    def slice(self, start: int, length: int) -> System.ReadOnlyMemory[System_ReadOnlyMemory_T]:
        ...

    def to_array(self) -> typing.List[System_ReadOnlyMemory_T]:
        ...

    def to_string(self) -> str:
        ...

    def try_copy_to(self, destination: System.Memory[System_ReadOnlyMemory_T]) -> bool:
        ...


class CLSCompliantAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def is_compliant(self) -> bool:
        ...

    def __init__(self, is_compliant: bool) -> None:
        ...


class StringNormalizationExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_normalized_length(source: System.ReadOnlySpan[str], normalization_form: System.Text.NormalizationForm = ...) -> int:
        ...

    @staticmethod
    @overload
    def is_normalized(str_input: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_normalized(str_input: str, normalization_form: System.Text.NormalizationForm) -> bool:
        ...

    @staticmethod
    @overload
    def is_normalized(source: System.ReadOnlySpan[str], normalization_form: System.Text.NormalizationForm = ...) -> bool:
        ...

    @staticmethod
    @overload
    def normalize(str_input: str) -> str:
        ...

    @staticmethod
    @overload
    def normalize(str_input: str, normalization_form: System.Text.NormalizationForm) -> str:
        ...

    @staticmethod
    def try_normalize(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int], normalization_form: System.Text.NormalizationForm = ...) -> typing.Tuple[bool, int]:
        ...


class Char(System.IComparable[str], System.IEquatable[str], System.IConvertible, System.ISpanFormattable, System.Numerics.IUnsignedNumber[str], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[str], System.IUtfChar[str], System.IBinaryIntegerParseAndFormatInfo[str]):
    """This class has no documentation."""

    MAX_VALUE: str = ...

    MIN_VALUE: str = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: str) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: str) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: str) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: str) -> bool:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: str) -> int:
        ...

    @staticmethod
    def convert_from_utf_32(utf_32: int) -> str:
        ...

    @staticmethod
    @overload
    def convert_to_utf_32(high_surrogate: str, low_surrogate: str) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_utf_32(s: str, index: int) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: str) -> bool:
        ...

    @overload
    def equals(self, other: str, comparison_type: System.StringComparison) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_numeric_value(c: str) -> float:
        ...

    @staticmethod
    @overload
    def get_numeric_value(s: str, index: int) -> float:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    @overload
    def get_unicode_category(c: str) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(s: str, index: int) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    def is_ascii(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_digit(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_hex_digit(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_hex_digit_lower(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_hex_digit_upper(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_letter(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_letter_lower(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_letter_or_digit(c: str) -> bool:
        ...

    @staticmethod
    def is_ascii_letter_upper(c: str) -> bool:
        ...

    @staticmethod
    def is_between(c: str, min_inclusive: str, max_inclusive: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_control(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_control(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_digit(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_digit(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_high_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_high_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter_or_digit(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter_or_digit(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_lower(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_lower(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_low_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_low_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_number(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_number(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_punctuation(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_punctuation(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_separator(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_separator(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate_pair(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate_pair(high_surrogate: str, low_surrogate: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_symbol(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_symbol(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_upper(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_upper(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_white_space(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_white_space(s: str, index: int) -> bool:
        ...

    @staticmethod
    def parse(s: str) -> str:
        ...

    @staticmethod
    @overload
    def to_lower(c: str, culture: System.Globalization.CultureInfo) -> str:
        ...

    @staticmethod
    @overload
    def to_lower(c: str) -> str:
        ...

    @staticmethod
    def to_lower_invariant(c: str) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(c: str) -> str:
        ...

    @staticmethod
    @overload
    def to_upper(c: str, culture: System.Globalization.CultureInfo) -> str:
        ...

    @staticmethod
    @overload
    def to_upper(c: str) -> str:
        ...

    @staticmethod
    def to_upper_invariant(c: str) -> str:
        ...

    @staticmethod
    def try_parse(s: str, result: typing.Optional[str]) -> typing.Tuple[bool, str]:
        ...


class IDisposable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def dispose(self) -> None:
        ...


class IObservable(typing.Generic[System_IObservable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def subscribe(self, observer: System.IObserver[System_IObservable_T]) -> System.IDisposable:
        ...


class Tuple(typing.Generic[System_Tuple_T1, System_Tuple_T2, System_Tuple_T3, System_Tuple_T4, System_Tuple_T5, System_Tuple_T6, System_Tuple_T7, System_Tuple_TRest], System.Object, System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.ITupleInternal):
    """This class has no documentation."""

    @property
    def item_1(self) -> System_Tuple_T1:
        ...

    @property
    def item_2(self) -> System_Tuple_T2:
        ...

    @property
    def item_3(self) -> System_Tuple_T3:
        ...

    @property
    def item_4(self) -> System_Tuple_T4:
        ...

    @property
    def item_5(self) -> System_Tuple_T5:
        ...

    @property
    def item_6(self) -> System_Tuple_T6:
        ...

    @property
    def item_7(self) -> System_Tuple_T7:
        ...

    @property
    def rest(self) -> System_Tuple_TRest:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6, item_7: System_Tuple_T7) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6, item_7: System_Tuple_T7, rest: System_Tuple_TRest) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class ValueTuple(typing.Generic[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest], System.IEquatable[System_ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable[System_ValueTuple], System.IValueTupleInternal):
    """This class has no documentation."""

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_7(self) -> System_ValueTuple_T7:
        ...

    @item_7.setter
    def item_7(self, value: System_ValueTuple_T7) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_7(self) -> System_ValueTuple_T7:
        ...

    @item_7.setter
    def item_7(self, value: System_ValueTuple_T7) -> None:
        ...

    @property
    def rest(self) -> System_ValueTuple_TRest:
        ...

    @rest.setter
    def rest(self, value: System_ValueTuple_TRest) -> None:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6, item_7: System_ValueTuple_T7) -> None:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6, item_7: System_ValueTuple_T7, rest: System_ValueTuple_TRest) -> None:
        ...

    @overload
    def __le__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> int:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> int:
        ...

    @staticmethod
    def create() -> System.ValueTuple:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class Int32(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
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
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class MulticastDelegate(System.Delegate, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __eq__(self, d_2: System.MulticastDelegate) -> bool:
        ...

    @overload
    def __init__(self, target: typing.Any, method: str) -> None:
        ...

    @overload
    def __init__(self, target: typing.Type, method: str) -> None:
        ...

    def __ne__(self, d_2: System.MulticastDelegate) -> bool:
        ...

    def combine_impl(self, follow: System.Delegate) -> System.Delegate:
        ...

    def dynamic_invoke_impl(self, args: typing.List[System.Object]) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_list(self) -> typing.List[System.Delegate]:
        ...

    def get_method_impl(self) -> System.Reflection.MethodInfo:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def remove_impl(self, value: System.Delegate) -> System.Delegate:
        ...


class FormattableString(System.Object, System.IFormattable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def format(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def argument_count(self) -> int:
        ...

    @staticmethod
    def current_culture(formattable: System.FormattableString) -> str:
        ...

    def get_argument(self, index: int) -> System.Object:
        ...

    def get_arguments(self) -> typing.List[System.Object]:
        ...

    @staticmethod
    def invariant(formattable: System.FormattableString) -> str:
        ...

    @overload
    def to_string(self, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...


class IUtf8SpanParsable(typing.Generic[System_IUtf8SpanParsable_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class Double(System.IComparable[float], System.IConvertible, System.ISpanFormattable, System.IEquatable[float], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[float]):
    """This class has no documentation."""

    MIN_VALUE: float = ...

    MAX_VALUE: float = ...

    EPSILON: float = ...

    NEGATIVE_INFINITY: float = ...

    POSITIVE_INFINITY: float = ...

    NA_N: float = ...

    NEGATIVE_ZERO: float = -0.0

    E: float = ...

    PI: float = ...

    TAU: float = ...

    def __eq__(self, right: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, right: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, right: float) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, right: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, right: float) -> bool:
        ...

    def __ne__(self, right: float) -> bool:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def acos_pi(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def asin_pi(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atan_2_pi(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def atan_pi(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def clamp_native(value: float, min: float, max: float) -> float:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def cos_pi(x: float) -> float:
        ...

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: float) -> bool:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def exp_10(x: float) -> float:
        ...

    @staticmethod
    def exp_10_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_2(x: float) -> float:
        ...

    @staticmethod
    def exp_2_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_m_1(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(left: float, right: float, addend: float) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def hypot(x: float, y: float) -> float:
        ...

    @staticmethod
    def ieee_754_remainder(left: float, right: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_finite(d: float) -> bool:
        ...

    @staticmethod
    def is_infinity(d: float) -> bool:
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_na_n(d: float) -> bool:
        ...

    @staticmethod
    def is_negative(d: float) -> bool:
        ...

    @staticmethod
    def is_negative_infinity(d: float) -> bool:
        ...

    @staticmethod
    def is_normal(d: float) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(d: float) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: float) -> bool:
        ...

    @staticmethod
    def is_real_number(value: float) -> bool:
        ...

    @staticmethod
    def is_subnormal(d: float) -> bool:
        ...

    @staticmethod
    def lerp(value_1: float, value_2: float, amount: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float, new_base: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_10_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_2(value: float) -> float:
        ...

    @staticmethod
    def log_2_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_p_1(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply_add_estimate(left: float, right: float, addend: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        ...

    @staticmethod
    def root_n(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(value: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sin_cos_pi(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sin_pi(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def tan_pi(x: float) -> float:
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
    def truncate(x: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class IAsyncDisposable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...


class ArgumentNullException(System.ArgumentException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, param_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    def throw_if_null(argument: typing.Any, param_name: str = None) -> None:
        ...


class LocalDataStoreSlot(System.Object):
    """This class has no documentation."""


class DllNotFoundException(System.TypeLoadException):
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


class UInt32(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class AggregateException(System.Exception):
    """This class has no documentation."""

    @property
    def inner_exceptions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Exception]:
        ...

    @property
    def message(self) -> str:
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
    def __init__(self, inner_exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        ...

    @overload
    def __init__(self, *inner_exceptions: typing.Union[System.Exception, typing.Iterable[System.Exception]]) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        ...

    @overload
    def __init__(self, message: str, *inner_exceptions: typing.Union[System.Exception, typing.Iterable[System.Exception]]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def flatten(self) -> System.AggregateException:
        ...

    def get_base_exception(self) -> System.Exception:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def handle(self, predicate: typing.Callable[[System.Exception], bool]) -> None:
        ...

    def to_string(self) -> str:
        ...


class Single(System.IComparable[float], System.IConvertible, System.ISpanFormattable, System.IEquatable[float], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[float]):
    """This class has no documentation."""

    MIN_VALUE: float = ...

    MAX_VALUE: float = ...

    EPSILON: float = ...

    NEGATIVE_INFINITY: float = ...

    POSITIVE_INFINITY: float = ...

    NA_N: float = ...

    NEGATIVE_ZERO: float = ...

    E: float = ...

    PI: float = ...

    TAU: float = ...

    def __eq__(self, right: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, right: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, right: float) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, right: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, right: float) -> bool:
        ...

    def __ne__(self, right: float) -> bool:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def acos_pi(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def asin_pi(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atan_2_pi(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def atan_pi(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def clamp_native(value: float, min: float, max: float) -> float:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def cos_pi(x: float) -> float:
        ...

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: float) -> bool:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def exp_10(x: float) -> float:
        ...

    @staticmethod
    def exp_10_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_2(x: float) -> float:
        ...

    @staticmethod
    def exp_2_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_m_1(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(left: float, right: float, addend: float) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def hypot(x: float, y: float) -> float:
        ...

    @staticmethod
    def ieee_754_remainder(left: float, right: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_finite(f: float) -> bool:
        ...

    @staticmethod
    def is_infinity(f: float) -> bool:
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_na_n(f: float) -> bool:
        ...

    @staticmethod
    def is_negative(f: float) -> bool:
        ...

    @staticmethod
    def is_negative_infinity(f: float) -> bool:
        ...

    @staticmethod
    def is_normal(f: float) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(f: float) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: float) -> bool:
        ...

    @staticmethod
    def is_real_number(value: float) -> bool:
        ...

    @staticmethod
    def is_subnormal(f: float) -> bool:
        ...

    @staticmethod
    def lerp(value_1: float, value_2: float, amount: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float, new_base: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_10_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_2(value: float) -> float:
        ...

    @staticmethod
    def log_2_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_p_1(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply_add_estimate(left: float, right: float, addend: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        ...

    @staticmethod
    def root_n(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(value: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sin_cos_pi(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sin_pi(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def tan_pi(x: float) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def truncate(x: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class OutOfMemoryException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class Int16(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class TimeZoneNotFoundException(System.Exception):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class Math(System.Object):
    """This class has no documentation."""

    E: float = 2.7182818284590452354

    PI: float = 3.14159265358979323846

    TAU: float = 6.283185307179586476925

    @staticmethod
    @overload
    def abs(value: int) -> int:
        ...

    @staticmethod
    @overload
    def abs(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(d: float) -> float:
        ...

    @staticmethod
    def acosh(d: float) -> float:
        ...

    @staticmethod
    def asin(d: float) -> float:
        ...

    @staticmethod
    def asinh(d: float) -> float:
        ...

    @staticmethod
    def atan(d: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(d: float) -> float:
        ...

    @staticmethod
    @overload
    def big_mul(a: int, b: int) -> int:
        ...

    @staticmethod
    @overload
    def big_mul(a: int, b: int, low: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(d: float) -> float:
        ...

    @staticmethod
    @overload
    def ceiling(d: float) -> float:
        ...

    @staticmethod
    @overload
    def ceiling(a: float) -> float:
        ...

    @staticmethod
    @overload
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @staticmethod
    @overload
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    @overload
    def clamp(value: System.IntPtr, min: System.IntPtr, max: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def clamp(value: System.UIntPtr, min: System.UIntPtr, max: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def copy_sign(x: float, y: float) -> float:
        ...

    @staticmethod
    def cos(d: float) -> float:
        ...

    @staticmethod
    def cosh(value: float) -> float:
        ...

    @staticmethod
    @overload
    def div_rem(a: int, b: int, result: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    @staticmethod
    @overload
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @staticmethod
    @overload
    def div_rem(left: System.IntPtr, right: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def div_rem(left: System.UIntPtr, right: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        ...

    @staticmethod
    def exp(d: float) -> float:
        ...

    @staticmethod
    def floor(d: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(x: float, y: float, z: float) -> float:
        ...

    @staticmethod
    def ieee_remainder(x: float, y: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    @overload
    def log(a: float, new_base: float) -> float:
        ...

    @staticmethod
    @overload
    def log(d: float) -> float:
        ...

    @staticmethod
    def log_10(d: float) -> float:
        ...

    @staticmethod
    def log_2(x: float) -> float:
        ...

    @staticmethod
    @overload
    def max(val_1: int, val_2: int) -> int:
        ...

    @staticmethod
    @overload
    def max(val_1: float, val_2: float) -> float:
        ...

    @staticmethod
    @overload
    def max(val_1: System.IntPtr, val_2: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def max(val_1: System.UIntPtr, val_2: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    @overload
    def min(val_1: int, val_2: int) -> int:
        ...

    @staticmethod
    @overload
    def min(val_1: float, val_2: float) -> float:
        ...

    @staticmethod
    @overload
    def min(val_1: System.IntPtr, val_2: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def min(val_1: System.UIntPtr, val_2: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(d: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(d: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(a: float) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def sign(value: float) -> int:
        ...

    @staticmethod
    @overload
    def sign(value: int) -> int:
        ...

    @staticmethod
    @overload
    def sign(value: System.IntPtr) -> int:
        ...

    @staticmethod
    def sin(a: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(value: float) -> float:
        ...

    @staticmethod
    def sqrt(d: float) -> float:
        ...

    @staticmethod
    def tan(a: float) -> float:
        ...

    @staticmethod
    def tanh(value: float) -> float:
        ...

    @staticmethod
    def truncate(d: float) -> float:
        ...


class EntryPointNotFoundException(System.TypeLoadException):
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


class DBNull(System.Object, System.Runtime.Serialization.ISerializable, System.IConvertible):
    """This class has no documentation."""

    VALUE: System.DBNull = ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_type_code(self) -> System.TypeCode:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...


class DataMisalignedException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class AppDomainUnloadedException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ApplicationId(System.Object):
    """This class has no documentation."""

    @property
    def culture(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def processor_architecture(self) -> str:
        ...

    @property
    def version(self) -> System.Version:
        ...

    @property
    def public_key_token(self) -> typing.List[int]:
        ...

    def __init__(self, public_key_token: typing.List[int], name: str, version: System.Version, processor_architecture: str, culture: str) -> None:
        ...

    def copy(self) -> System.ApplicationId:
        ...

    def equals(self, o: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class Buffer(System.Object):
    """This class has no documentation."""

    @staticmethod
    def block_copy(src: System.Array, src_offset: int, dst: System.Array, dst_offset: int, count: int) -> None:
        ...

    @staticmethod
    def byte_length(array: System.Array) -> int:
        ...

    @staticmethod
    def get_byte(array: System.Array, index: int) -> int:
        ...

    @staticmethod
    def memory_copy(source: typing.Any, destination: typing.Any, destination_size_in_bytes: int, source_bytes_to_copy: int) -> None:
        ...

    @staticmethod
    def set_byte(array: System.Array, index: int, value: int) -> None:
        ...


class IEquatable(typing.Generic[System_IEquatable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, other: System_IEquatable_T) -> bool:
        ...


class ArraySegment(typing.Generic[System_ArraySegment_T], System.Collections.Generic.IList[System_ArraySegment_T], System.Collections.Generic.IReadOnlyList[System_ArraySegment_T], typing.Iterable[System_ArraySegment_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_ArraySegment_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_ArraySegment_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.ArraySegment[System_ArraySegment_T]

    @property
    def array(self) -> typing.List[System_ArraySegment_T]:
        ...

    @property
    def offset(self) -> int:
        ...

    @property
    def count(self) -> int:
        ...

    def __eq__(self, b: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_ArraySegment_T:
        ...

    @overload
    def __init__(self, array: typing.List[System_ArraySegment_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_ArraySegment_T], offset: int, count: int) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_ArraySegment_T]:
        ...

    def __ne__(self, b: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def __setitem__(self, index: int, value: System_ArraySegment_T) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_ArraySegment_T]) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_ArraySegment_T], destination_index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.ArraySegment[System_ArraySegment_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def get_enumerator(self) -> System.ArraySegment.Enumerator:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def slice(self, index: int) -> System.ArraySegment[System_ArraySegment_T]:
        ...

    @overload
    def slice(self, index: int, count: int) -> System.ArraySegment[System_ArraySegment_T]:
        ...

    def to_array(self) -> typing.List[System_ArraySegment_T]:
        ...


class ICustomFormatter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def format(self, format: str, arg: typing.Any, format_provider: System.IFormatProvider) -> str:
        ...


class IComparable(typing.Generic[System_IComparable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, other: System_IComparable_T) -> int:
        ...


class IAsyncResult(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_completed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def async_wait_handle(self) -> System.Threading.WaitHandle:
        ...

    @property
    @abc.abstractmethod
    def async_state(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def completed_synchronously(self) -> bool:
        ...


class GCNotificationStatus(IntEnum):
    """This class has no documentation."""

    SUCCEEDED = 0

    FAILED = 1

    CANCELED = 2

    TIMEOUT = 3

    NOT_APPLICABLE = 4


class GCCollectionMode(IntEnum):
    """This class has no documentation."""

    DEFAULT = 0

    FORCED = 1

    OPTIMIZED = 2

    AGGRESSIVE = 3


class GCGenerationInfo:
    """This class has no documentation."""

    @property
    def size_before_bytes(self) -> int:
        ...

    @property
    def fragmentation_before_bytes(self) -> int:
        ...

    @property
    def size_after_bytes(self) -> int:
        ...

    @property
    def fragmentation_after_bytes(self) -> int:
        ...


class GCMemoryInfo:
    """This class has no documentation."""

    @property
    def high_memory_load_threshold_bytes(self) -> int:
        ...

    @property
    def memory_load_bytes(self) -> int:
        ...

    @property
    def total_available_memory_bytes(self) -> int:
        ...

    @property
    def heap_size_bytes(self) -> int:
        ...

    @property
    def fragmented_bytes(self) -> int:
        ...

    @property
    def index(self) -> int:
        ...

    @property
    def generation(self) -> int:
        ...

    @property
    def compacted(self) -> bool:
        ...

    @property
    def concurrent(self) -> bool:
        ...

    @property
    def total_committed_bytes(self) -> int:
        ...

    @property
    def promoted_bytes(self) -> int:
        ...

    @property
    def pinned_objects_count(self) -> int:
        ...

    @property
    def finalization_pending_count(self) -> int:
        ...

    @property
    def pause_durations(self) -> System.ReadOnlySpan[datetime.timedelta]:
        ...

    @property
    def pause_time_percentage(self) -> float:
        ...

    @property
    def generation_info(self) -> System.ReadOnlySpan[System.GCGenerationInfo]:
        ...


class GCKind(IntEnum):
    """This class has no documentation."""

    ANY = 0

    EPHEMERAL = 1

    FULL_BLOCKING = 2

    BACKGROUND = 3


class GC(System.Object):
    """This class has no documentation."""

    MAX_GENERATION: int

    @staticmethod
    def add_memory_pressure(bytes_allocated: int) -> None:
        ...

    @staticmethod
    def cancel_full_gc_notification() -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int) -> None:
        ...

    @staticmethod
    @overload
    def collect() -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode) -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode, blocking: bool) -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode, blocking: bool, compacting: bool) -> None:
        ...

    @staticmethod
    def collection_count(generation: int) -> int:
        ...

    @staticmethod
    def end_no_gc_region() -> None:
        ...

    @staticmethod
    def get_allocated_bytes_for_current_thread() -> int:
        ...

    @staticmethod
    def get_configuration_variables() -> System.Collections.Generic.IReadOnlyDictionary[str, System.Object]:
        ...

    @staticmethod
    @overload
    def get_gc_memory_info() -> System.GCMemoryInfo:
        ...

    @staticmethod
    @overload
    def get_gc_memory_info(kind: System.GCKind) -> System.GCMemoryInfo:
        ...

    @staticmethod
    @overload
    def get_generation(obj: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def get_generation(wo: System.WeakReference) -> int:
        ...

    @staticmethod
    def get_total_allocated_bytes(precise: bool = False) -> int:
        ...

    @staticmethod
    def get_total_memory(force_full_collection: bool) -> int:
        ...

    @staticmethod
    def get_total_pause_duration() -> datetime.timedelta:
        ...

    @staticmethod
    def keep_alive(obj: typing.Any) -> None:
        ...

    @staticmethod
    def refresh_memory_limit() -> None:
        ...

    @staticmethod
    def register_for_full_gc_notification(max_generation_threshold: int, large_object_heap_threshold: int) -> None:
        ...

    @staticmethod
    def register_no_gc_region_callback(total_size: int, callback: typing.Callable[[], typing.Any]) -> None:
        ...

    @staticmethod
    def remove_memory_pressure(bytes_allocated: int) -> None:
        ...

    @staticmethod
    def re_register_for_finalize(obj: typing.Any) -> None:
        ...

    @staticmethod
    def suppress_finalize(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, loh_size: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, disallow_full_blocking_gc: bool) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, loh_size: int, disallow_full_blocking_gc: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach(timeout: datetime.timedelta) -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach() -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach(milliseconds_timeout: int) -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete(timeout: datetime.timedelta) -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete() -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete(milliseconds_timeout: int) -> System.GCNotificationStatus:
        ...

    @staticmethod
    def wait_for_pending_finalizers() -> None:
        ...


class IndexOutOfRangeException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class ArgumentOutOfRangeException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def actual_value(self) -> System.Object:
        ...

    @overload
    def __init__(self, param_name: str, actual_value: typing.Any, message: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, param_name: str) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class ExecutionEngineException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class Int64(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> System.Int128:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Void:
    """This class has no documentation."""


class InsufficientMemoryException(System.OutOfMemoryException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class InvalidCastException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class TimeZone(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    CURRENT_TIME_ZONE: System.TimeZone

    @property
    @abc.abstractmethod
    def standard_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def daylight_name(self) -> str:
        ...

    def __init__(self) -> None:
        ...

    def get_daylight_changes(self, year: int) -> System.Globalization.DaylightTime:
        ...

    def get_utc_offset(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def is_daylight_saving_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def is_daylight_saving_time(time: typing.Union[datetime.datetime, datetime.date], daylight_times: System.Globalization.DaylightTime) -> bool:
        ...

    def to_local_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...

    def to_universal_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...


class FormatException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ArrayTypeMismatchException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class UriTypeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class ConsoleSpecialKey(IntEnum):
    """This class has no documentation."""

    CONTROL_C = 0

    CONTROL_BREAK = 1


class ConsoleColor(IntEnum):
    """This class has no documentation."""

    BLACK = 0

    DARK_BLUE = 1

    DARK_GREEN = 2

    DARK_CYAN = 3

    DARK_RED = 4

    DARK_MAGENTA = 5

    DARK_YELLOW = 6

    GRAY = 7

    DARK_GRAY = 8

    BLUE = 9

    GREEN = 10

    CYAN = 11

    RED = 12

    MAGENTA = 13

    YELLOW = 14

    WHITE = 15


class ConsoleKey(IntEnum):
    """This class has no documentation."""

    NONE = ...

    BACKSPACE = ...

    TAB = ...

    CLEAR = ...

    ENTER = ...

    PAUSE = ...

    ESCAPE = ...

    SPACEBAR = ...

    PAGE_UP = ...

    PAGE_DOWN = ...

    END = ...

    HOME = ...

    LEFT_ARROW = ...

    UP_ARROW = ...

    RIGHT_ARROW = ...

    DOWN_ARROW = ...

    SELECT = ...

    PRINT = ...

    EXECUTE = ...

    PRINT_SCREEN = ...

    INSERT = ...

    DELETE = ...

    HELP = ...

    D_0 = ...

    D_1 = ...

    D_2 = ...

    D_3 = ...

    D_4 = ...

    D_5 = ...

    D_6 = ...

    D_7 = ...

    D_8 = ...

    D_9 = ...

    A = ...

    B = ...

    C = ...

    D = ...

    E = ...

    F = ...

    G = ...

    H = ...

    I = ...

    J = ...

    K = ...

    L = ...

    M = ...

    N = ...

    O = ...

    P = ...

    Q = ...

    R = ...

    S = ...

    T = ...

    U = ...

    V = ...

    W = ...

    X = ...

    Y = ...

    Z = ...

    LEFT_WINDOWS = ...

    RIGHT_WINDOWS = ...

    APPLICATIONS = ...

    SLEEP = ...

    NUM_PAD_0 = ...

    NUM_PAD_1 = ...

    NUM_PAD_2 = ...

    NUM_PAD_3 = ...

    NUM_PAD_4 = ...

    NUM_PAD_5 = ...

    NUM_PAD_6 = ...

    NUM_PAD_7 = ...

    NUM_PAD_8 = ...

    NUM_PAD_9 = ...

    MULTIPLY = ...

    ADD = ...

    SEPARATOR = ...

    SUBTRACT = ...

    DECIMAL = ...

    DIVIDE = ...

    F_1 = ...

    F_2 = ...

    F_3 = ...

    F_4 = ...

    F_5 = ...

    F_6 = ...

    F_7 = ...

    F_8 = ...

    F_9 = ...

    F_10 = ...

    F_11 = ...

    F_12 = ...

    F_13 = ...

    F_14 = ...

    F_15 = ...

    F_16 = ...

    F_17 = ...

    F_18 = ...

    F_19 = ...

    F_20 = ...

    F_21 = ...

    F_22 = ...

    F_23 = ...

    F_24 = ...

    BROWSER_BACK = ...

    BROWSER_FORWARD = ...

    BROWSER_REFRESH = ...

    BROWSER_STOP = ...

    BROWSER_SEARCH = ...

    BROWSER_FAVORITES = ...

    BROWSER_HOME = ...

    VOLUME_MUTE = ...

    VOLUME_DOWN = ...

    VOLUME_UP = ...

    MEDIA_NEXT = ...

    MEDIA_PREVIOUS = ...

    MEDIA_STOP = ...

    MEDIA_PLAY = ...

    LAUNCH_MAIL = ...

    LAUNCH_MEDIA_SELECT = ...

    LAUNCH_APP_1 = ...

    LAUNCH_APP_2 = ...

    OEM_1 = ...

    OEM_PLUS = ...

    OEM_COMMA = ...

    OEM_MINUS = ...

    OEM_PERIOD = ...

    OEM_2 = ...

    OEM_3 = ...

    OEM_4 = ...

    OEM_5 = ...

    OEM_6 = ...

    OEM_7 = ...

    OEM_8 = ...

    OEM_102 = ...

    PROCESS = ...

    PACKET = ...

    ATTENTION = ...

    CR_SEL = ...

    EX_SEL = ...

    ERASE_END_OF_FILE = ...

    PLAY = ...

    ZOOM = ...

    NO_NAME = ...

    PA_1 = ...

    OEM_CLEAR = ...


class ConsoleModifiers(IntEnum):
    """This class has no documentation."""

    NONE = 0

    ALT = 1

    SHIFT = 2

    CONTROL = 4


class ConsoleKeyInfo(System.IEquatable[System_ConsoleKeyInfo]):
    """This class has no documentation."""

    @property
    def key_char(self) -> str:
        ...

    @property
    def key(self) -> System.ConsoleKey:
        ...

    @property
    def modifiers(self) -> System.ConsoleModifiers:
        ...

    def __eq__(self, b: System.ConsoleKeyInfo) -> bool:
        ...

    def __init__(self, key_char: str, key: System.ConsoleKey, shift: bool, alt: bool, control: bool) -> None:
        ...

    def __ne__(self, b: System.ConsoleKeyInfo) -> bool:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.ConsoleKeyInfo) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ConsoleCancelEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def cancel(self) -> bool:
        ...

    @cancel.setter
    def cancel(self, value: bool) -> None:
        ...

    @property
    def special_key(self) -> System.ConsoleSpecialKey:
        ...


class Console(System.Object):
    """This class has no documentation."""

    IN: System.IO.TextReader

    input_encoding: System.Text.Encoding

    output_encoding: System.Text.Encoding

    KEY_AVAILABLE: bool

    OUT: System.IO.TextWriter

    ERROR: System.IO.TextWriter

    IS_INPUT_REDIRECTED: bool

    IS_OUTPUT_REDIRECTED: bool

    IS_ERROR_REDIRECTED: bool

    cursor_size: int

    NUMBER_LOCK: bool

    CAPS_LOCK: bool

    background_color: System.ConsoleColor

    foreground_color: System.ConsoleColor

    buffer_width: int

    buffer_height: int

    window_left: int

    window_top: int

    window_width: int

    window_height: int

    LARGEST_WINDOW_WIDTH: int

    LARGEST_WINDOW_HEIGHT: int

    cursor_visible: bool

    cursor_left: int

    cursor_top: int

    title: str

    cancel_key_press: _EventContainer[typing.Callable[[System.Object, System.ConsoleCancelEventArgs], typing.Any], typing.Any]

    treat_control_c_as_input: bool

    @staticmethod
    @overload
    def beep() -> None:
        ...

    @staticmethod
    @overload
    def beep(frequency: int, duration: int) -> None:
        ...

    @staticmethod
    def clear() -> None:
        ...

    @staticmethod
    def get_cursor_position() -> System.ValueTuple[int, int]:
        ...

    @staticmethod
    @overload
    def move_buffer_area(source_left: int, source_top: int, source_width: int, source_height: int, target_left: int, target_top: int) -> None:
        ...

    @staticmethod
    @overload
    def move_buffer_area(source_left: int, source_top: int, source_width: int, source_height: int, target_left: int, target_top: int, source_char: str, source_fore_color: System.ConsoleColor, source_back_color: System.ConsoleColor) -> None:
        ...

    @staticmethod
    @overload
    def open_standard_error() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_error(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_input() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_input(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_output() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_output(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    def read() -> int:
        ...

    @staticmethod
    @overload
    def read_key() -> System.ConsoleKeyInfo:
        ...

    @staticmethod
    @overload
    def read_key(intercept: bool) -> System.ConsoleKeyInfo:
        ...

    @staticmethod
    def read_line() -> str:
        ...

    @staticmethod
    def reset_color() -> None:
        ...

    @staticmethod
    def set_buffer_size(width: int, height: int) -> None:
        ...

    @staticmethod
    def set_cursor_position(left: int, top: int) -> None:
        ...

    @staticmethod
    def set_error(new_error: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def set_in(new_in: System.IO.TextReader) -> None:
        ...

    @staticmethod
    def set_out(new_out: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def set_window_position(left: int, top: int) -> None:
        ...

    @staticmethod
    def set_window_size(width: int, height: int) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    @overload
    def write(value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write(value: str) -> None:
        ...

    @staticmethod
    @overload
    def write(buffer: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write(buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def write(value: float) -> None:
        ...

    @staticmethod
    @overload
    def write(value: int) -> None:
        ...

    @staticmethod
    @overload
    def write(value: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line() -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(buffer: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: float) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: int) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...


class _EventContainer(typing.Generic[System__EventContainer_Callable, System__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


