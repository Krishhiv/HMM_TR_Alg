from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections.Generic
import System.Diagnostics.Contracts
import System.Runtime.CompilerServices
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks

System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T")
System_Runtime_CompilerServices_ConditionalWeakTable_TKey = typing.TypeVar("System_Runtime_CompilerServices_ConditionalWeakTable_TKey")
System_Runtime_CompilerServices_ConditionalWeakTable_TValue = typing.TypeVar("System_Runtime_CompilerServices_ConditionalWeakTable_TValue")
System_Runtime_CompilerServices_TaskAwaiter_TResult = typing.TypeVar("System_Runtime_CompilerServices_TaskAwaiter_TResult")
System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult")
System_Runtime_CompilerServices_InlineArray2_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray2_T")
System_Runtime_CompilerServices_InlineArray3_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray3_T")
System_Runtime_CompilerServices_InlineArray4_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray4_T")
System_Runtime_CompilerServices_InlineArray5_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray5_T")
System_Runtime_CompilerServices_InlineArray6_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray6_T")
System_Runtime_CompilerServices_InlineArray7_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray7_T")
System_Runtime_CompilerServices_InlineArray8_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray8_T")
System_Runtime_CompilerServices_InlineArray9_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray9_T")
System_Runtime_CompilerServices_InlineArray10_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray10_T")
System_Runtime_CompilerServices_InlineArray11_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray11_T")
System_Runtime_CompilerServices_InlineArray12_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray12_T")
System_Runtime_CompilerServices_InlineArray13_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray13_T")
System_Runtime_CompilerServices_InlineArray14_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray14_T")
System_Runtime_CompilerServices_InlineArray15_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray15_T")
System_Runtime_CompilerServices_InlineArray16_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray16_T")
System_Runtime_CompilerServices_ValueTaskAwaiter_TResult = typing.TypeVar("System_Runtime_CompilerServices_ValueTaskAwaiter_TResult")
System_Runtime_CompilerServices_StrongBox_T = typing.TypeVar("System_Runtime_CompilerServices_StrongBox_T")
System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult")
System_Runtime_CompilerServices__EventContainer_Callable = typing.TypeVar("System_Runtime_CompilerServices__EventContainer_Callable")
System_Runtime_CompilerServices__EventContainer_ReturnType = typing.TypeVar("System_Runtime_CompilerServices__EventContainer_ReturnType")


class InterpolatedStringHandlerArgumentAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def arguments(self) -> typing.List[str]:
        ...

    @overload
    def __init__(self, argument: str) -> None:
        ...

    @overload
    def __init__(self, *arguments: typing.Union[str, typing.Iterable[str]]) -> None:
        ...


class StateMachineAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state_machine_type(self) -> typing.Type:
        ...

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class AsyncIteratorStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """This class has no documentation."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class IAsyncStateMachine(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def move_next(self) -> None:
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        ...


class AsyncValueTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult]):
    """This class has no documentation."""

    @property
    def task(self) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncValueTaskMethodBuilder:
        ...

    def set_exception(self, exception: System.Exception) -> None:
        ...

    @overload
    def set_result(self) -> None:
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult) -> None:
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        ...


class MethodCodeType(IntEnum):
    """This class has no documentation."""

    IL = ...

    NATIVE = ...

    OPTIL = ...

    RUNTIME = ...


class MethodImplOptions(IntEnum):
    """This class has no documentation."""

    UNMANAGED = ...

    NO_INLINING = ...

    FORWARD_REF = ...

    SYNCHRONIZED = ...

    NO_OPTIMIZATION = ...

    PRESERVE_SIG = ...

    AGGRESSIVE_INLINING = ...

    AGGRESSIVE_OPTIMIZATION = ...

    ASYNC = ...

    INTERNAL_CALL = ...


class MethodImplAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def method_code_type(self) -> System.Runtime.CompilerServices.MethodCodeType:
        ...

    @method_code_type.setter
    def method_code_type(self, value: System.Runtime.CompilerServices.MethodCodeType) -> None:
        ...

    @property
    def value(self) -> System.Runtime.CompilerServices.MethodImplOptions:
        ...

    @overload
    def __init__(self, method_impl_options: System.Runtime.CompilerServices.MethodImplOptions) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...


class LoadHint(IntEnum):
    """This class has no documentation."""

    DEFAULT = ...

    ALWAYS = ...

    SOMETIMES = ...


class InlineArrayAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def length(self) -> int:
        ...

    def __init__(self, length: int) -> None:
        ...


class FixedBufferAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def element_type(self) -> typing.Type:
        ...

    @property
    def length(self) -> int:
        ...

    def __init__(self, element_type: typing.Type, length: int) -> None:
        ...


class IsVolatile(System.Object):
    """This class has no documentation."""


class CallConvCdecl(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvFastcall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvStdcall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvSwift(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvSuppressGCTransition(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvThiscall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvMemberFunction(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class PoolingAsyncValueTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult]):
    """This class has no documentation."""

    @property
    def task(self) -> System.Threading.Tasks.ValueTask[System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult]:
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.PoolingAsyncValueTaskMethodBuilder[System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult]:
        ...

    def set_exception(self, exception: System.Exception) -> None:
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult) -> None:
        ...

    @overload
    def set_result(self) -> None:
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        ...


class RuntimeCompatibilityAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def wrap_non_exception_throws(self) -> bool:
        ...

    @wrap_non_exception_throws.setter
    def wrap_non_exception_throws(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...


class FixedAddressValueTypeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IsUnmanagedAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class TypeForwardedFromAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def assembly_full_name(self) -> str:
        ...

    def __init__(self, assembly_full_name: str) -> None:
        ...


class ConfiguredAsyncDisposable:
    """This class has no documentation."""

    def dispose_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        ...


class PreserveBaseOverridesAttribute(System.Attribute):
    """This class has no documentation."""


class IsByRefLikeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class ExtensionAttribute(System.Attribute):
    """This class has no documentation."""


class CompilationRelaxations(IntEnum):
    """This class has no documentation."""

    NO_STRING_INTERNING = ...


class RuntimeWrappedException(System.Exception):
    """This class has no documentation."""

    @property
    def wrapped_exception(self) -> System.Object:
        ...

    def __init__(self, thrown_object: typing.Any) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class RefSafetyRulesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def version(self) -> int:
        ...

    def __init__(self, version: int) -> None:
        ...


class AsyncTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult]):
    """This class has no documentation."""

    @property
    def task(self) -> System.Threading.Tasks.Task[System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult]:
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncTaskMethodBuilder[System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult]:
        ...

    def set_exception(self, exception: System.Exception) -> None:
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult) -> None:
        ...

    @overload
    def set_result(self) -> None:
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        ...


class INotifyCompletion(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...


class ICriticalNotifyCompletion(System.Runtime.CompilerServices.INotifyCompletion, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def unsafe_on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...


class YieldAwaitable:
    """This class has no documentation."""

    class YieldAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter):
        """This class has no documentation."""

        @property
        def is_completed(self) -> bool:
            ...

        def get_result(self) -> None:
            ...

        def on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
            ...

        def unsafe_on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
            ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter:
        ...


class CompilerGeneratedAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StringFreezingAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class NullableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def nullable_flags(self) -> typing.List[int]:
        ...

    @nullable_flags.setter
    def nullable_flags(self, value: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[int]) -> None:
        ...


class AsyncHelpers(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def Await(task: System.Threading.Tasks.Task) -> None:
        ...

    @staticmethod
    @overload
    def Await(task: System.Threading.Tasks.ValueTask) -> None:
        ...

    @staticmethod
    @overload
    def Await(configuredAwaitable: System.Runtime.CompilerServices.ConfiguredTaskAwaitable) -> None:
        ...

    @staticmethod
    @overload
    def Await(configuredAwaitable: System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable) -> None:
        ...

    @staticmethod
    @overload
    def handle_async_entry_point(task: System.Threading.Tasks.Task) -> None:
        ...

    @staticmethod
    @overload
    def handle_async_entry_point(task: System.Threading.Tasks.Task[int]) -> int:
        ...


class AsyncVoidMethodBuilder:
    """This class has no documentation."""

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncVoidMethodBuilder:
        ...

    def set_exception(self, exception: System.Exception) -> None:
        ...

    def set_result(self) -> None:
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        ...


class ConfiguredCancelableAsyncEnumerable(typing.Generic[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def current(self) -> System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T:
            ...

        def dispose_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
            ...

        def move_next_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable[bool]:
            ...

    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]:
        ...

    def get_async_enumerator(self) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable.Enumerator:
        ...

    def with_cancellation(self, cancellation_token: System.Threading.CancellationToken) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]:
        ...


class EnumeratorCancellationAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AccessedThroughPropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    def __init__(self, property_name: str) -> None:
        ...


class ConditionalWeakTable(typing.Generic[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue], System.Object, System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]]):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]]:
        ...

    def add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> None:
        ...

    def add_or_update(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def create_value_callback(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    @overload
    def get_or_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    @overload
    def get_or_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value_factory: typing.Callable[[System_Runtime_CompilerServices_ConditionalWeakTable_TKey], System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    def get_or_create_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    def get_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, create_value_callback: typing.Callable[[System_Runtime_CompilerServices_ConditionalWeakTable_TKey], System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    @overload
    def remove(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> bool:
        ...

    @overload
    def remove(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: typing.Optional[System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> typing.Tuple[bool, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]:
        ...

    def try_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> bool:
        ...

    def try_get_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: typing.Optional[System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> typing.Tuple[bool, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]:
        ...


class DefaultInterpolatedStringHandler:
    """This class has no documentation."""

    @property
    def text(self) -> System.ReadOnlySpan[str]:
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int) -> None:
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int, provider: System.IFormatProvider) -> None:
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int, provider: System.IFormatProvider, initial_buffer: System.Span[str]) -> None:
        ...

    @overload
    def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
        ...

    @overload
    def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> None:
        ...

    @overload
    def append_formatted(self, value: str) -> None:
        ...

    @overload
    def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> None:
        ...

    def append_literal(self, value: str) -> None:
        ...

    def clear(self) -> None:
        ...

    def to_string(self) -> str:
        ...

    def to_string_and_clear(self) -> str:
        ...


class DisableRuntimeMarshallingAttribute(System.Attribute):
    """This class has no documentation."""


class UnsafeAccessorTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        ...

    def __init__(self, type_name: str) -> None:
        ...


class TaskAwaiter(typing.Generic[System_Runtime_CompilerServices_TaskAwaiter_TResult], System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter):
    """This class has no documentation."""

    @property
    def is_completed(self) -> bool:
        ...

    def get_result(self) -> None:
        ...

    def on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...

    def unsafe_on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...


class ConfiguredTaskAwaitable(typing.Generic[System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult]):
    """This class has no documentation."""

    def get_awaiter(self) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        ...


class InlineArray2(typing.Generic[System_Runtime_CompilerServices_InlineArray2_T]):
    """This class has no documentation."""


class InlineArray3(typing.Generic[System_Runtime_CompilerServices_InlineArray3_T]):
    """This class has no documentation."""


class InlineArray4(typing.Generic[System_Runtime_CompilerServices_InlineArray4_T]):
    """This class has no documentation."""


class InlineArray5(typing.Generic[System_Runtime_CompilerServices_InlineArray5_T]):
    """This class has no documentation."""


class InlineArray6(typing.Generic[System_Runtime_CompilerServices_InlineArray6_T]):
    """This class has no documentation."""


class InlineArray7(typing.Generic[System_Runtime_CompilerServices_InlineArray7_T]):
    """This class has no documentation."""


class InlineArray8(typing.Generic[System_Runtime_CompilerServices_InlineArray8_T]):
    """This class has no documentation."""


class InlineArray9(typing.Generic[System_Runtime_CompilerServices_InlineArray9_T]):
    """This class has no documentation."""


class InlineArray10(typing.Generic[System_Runtime_CompilerServices_InlineArray10_T]):
    """This class has no documentation."""


class InlineArray11(typing.Generic[System_Runtime_CompilerServices_InlineArray11_T]):
    """This class has no documentation."""


class InlineArray12(typing.Generic[System_Runtime_CompilerServices_InlineArray12_T]):
    """This class has no documentation."""


class InlineArray13(typing.Generic[System_Runtime_CompilerServices_InlineArray13_T]):
    """This class has no documentation."""


class InlineArray14(typing.Generic[System_Runtime_CompilerServices_InlineArray14_T]):
    """This class has no documentation."""


class InlineArray15(typing.Generic[System_Runtime_CompilerServices_InlineArray15_T]):
    """This class has no documentation."""


class InlineArray16(typing.Generic[System_Runtime_CompilerServices_InlineArray16_T]):
    """This class has no documentation."""


class ValueTaskAwaiter(typing.Generic[System_Runtime_CompilerServices_ValueTaskAwaiter_TResult], System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter):
    """This class has no documentation."""

    @property
    def is_completed(self) -> bool:
        ...

    def get_result(self) -> None:
        ...

    def on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...

    def unsafe_on_completed(self, continuation: typing.Callable[[], typing.Any]) -> None:
        ...


class UnsafeValueTypeAttribute(System.Attribute):
    """This class has no documentation."""


class SwitchExpressionException(System.InvalidOperationException):
    """This class has no documentation."""

    @property
    def unmatched_value(self) -> System.Object:
        ...

    @property
    def message(self) -> str:
        ...

    @overload
    def __init__(self, unmatched_value: typing.Any) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class ContractHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def raise_contract_failed_event(failure_kind: System.Diagnostics.Contracts.ContractFailureKind, user_message: str, condition_text: str, inner_exception: System.Exception) -> str:
        ...

    @staticmethod
    def trigger_failure(kind: System.Diagnostics.Contracts.ContractFailureKind, display_message: str, user_message: str, condition_text: str, inner_exception: System.Exception) -> None:
        ...


class ReferenceAssemblyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def description(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, description: str) -> None:
        ...


class InterpolatedStringHandlerAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class MetadataUpdateDeletedAttribute(System.Attribute):
    """This class has no documentation."""


class RuntimeFeature(System.Object):
    """This class has no documentation."""

    PORTABLE_PDB: str = ...

    DEFAULT_IMPLEMENTATIONS_OF_INTERFACES: str = ...

    UNMANAGED_SIGNATURE_CALLING_CONVENTION: str = ...

    COVARIANT_RETURNS_OF_CLASSES: str = ...

    BY_REF_FIELDS: str = ...

    BY_REF_LIKE_GENERICS: str = ...

    VIRTUAL_STATICS_IN_INTERFACES: str = ...

    NUMERIC_INT_PTR: str = ...

    IS_DYNAMIC_CODE_SUPPORTED: bool

    IS_DYNAMIC_CODE_COMPILED: bool

    @staticmethod
    def is_supported(feature: str) -> bool:
        ...


class IteratorStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """This class has no documentation."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class SkipLocalsInitAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IndexerNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self, indexer_name: str) -> None:
        ...


class DefaultDependencyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def load_hint(self) -> System.Runtime.CompilerServices.LoadHint:
        ...

    def __init__(self, load_hint_argument: System.Runtime.CompilerServices.LoadHint) -> None:
        ...


class RequiresLocationAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class UnsafeAccessorKind(IntEnum):
    """This class has no documentation."""

    CONSTRUCTOR = 0

    METHOD = 1

    STATIC_METHOD = 2

    FIELD = 3

    STATIC_FIELD = 4


class UnsafeAccessorAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def kind(self) -> System.Runtime.CompilerServices.UnsafeAccessorKind:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    def __init__(self, kind: System.Runtime.CompilerServices.UnsafeAccessorKind) -> None:
        ...


class CompilationRelaxationsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def compilation_relaxations(self) -> int:
        ...

    @overload
    def __init__(self, relaxations: int) -> None:
        ...

    @overload
    def __init__(self, relaxations: System.Runtime.CompilerServices.CompilationRelaxations) -> None:
        ...


class TypeForwardedToAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def destination(self) -> typing.Type:
        ...

    def __init__(self, destination: typing.Type) -> None:
        ...


class CustomConstantAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def value(self) -> System.Object:
        ...


class DateTimeConstantAttribute(System.Runtime.CompilerServices.CustomConstantAttribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    def __init__(self, ticks: int) -> None:
        ...


class CompilerGlobalScopeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallerMemberNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class InternalsVisibleToAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def assembly_name(self) -> str:
        ...

    @property
    def all_internals_visible(self) -> bool:
        ...

    @all_internals_visible.setter
    def all_internals_visible(self, value: bool) -> None:
        ...

    def __init__(self, assembly_name: str) -> None:
        ...


class RuntimeHelpers(System.Object):
    """This class has no documentation."""

    OFFSET_TO_STRING_DATA: int

    @staticmethod
    @overload
    def allocate_type_associated_memory(type: typing.Type, size: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def allocate_type_associated_memory(type: typing.Type, size: int, alignment: int) -> System.IntPtr:
        ...

    @staticmethod
    def box(target: int, type: System.RuntimeTypeHandle) -> System.Object:
        ...

    def cleanup_code(self, user_data: typing.Any, exception_thrown: bool) -> None:
        ...

    @staticmethod
    def ensure_sufficient_execution_stack() -> None:
        ...

    @staticmethod
    def equals(o_1: typing.Any, o_2: typing.Any) -> bool:
        ...

    @staticmethod
    def execute_code_with_guaranteed_cleanup(code: typing.Callable[[System.Object], typing.Any], backout_code: typing.Callable[[System.Object, bool], typing.Any], user_data: typing.Any) -> None:
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def get_hash_code(o: typing.Any) -> int:
        ...

    @staticmethod
    def get_object_value(obj: typing.Any) -> System.Object:
        ...

    @staticmethod
    def get_uninitialized_object(type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def initialize_array(array: System.Array, fld_handle: System.RuntimeFieldHandle) -> None:
        ...

    @staticmethod
    def prepare_constrained_regions() -> None:
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_constrained_regions_no_op() -> None:
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_contracted_delegate(d: System.Delegate) -> None:
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_delegate(d: System.Delegate) -> None:
        ...

    @staticmethod
    @overload
    def prepare_method(method: System.RuntimeMethodHandle) -> None:
        ...

    @staticmethod
    @overload
    def prepare_method(method: System.RuntimeMethodHandle, instantiation: typing.List[System.RuntimeTypeHandle]) -> None:
        ...

    @staticmethod
    def probe_for_sufficient_stack() -> None:
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def run_class_constructor(type: System.RuntimeTypeHandle) -> None:
        ...

    @staticmethod
    def run_module_constructor(module: System.ModuleHandle) -> None:
        ...

    @staticmethod
    def size_of(type: System.RuntimeTypeHandle) -> int:
        ...

    def try_code(self, user_data: typing.Any) -> None:
        ...

    @staticmethod
    def try_ensure_sufficient_execution_stack() -> bool:
        ...


class IsReadOnlyAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CreateNewOnMetadataUpdateAttribute(System.Attribute):
    """This class has no documentation."""


class SuppressIldasmAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class FormattableStringFactory(System.Object):
    """This class has no documentation."""

    @staticmethod
    def create(format: str, *arguments: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.FormattableString:
        ...


class ITuple(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def length(self) -> int:
        ...

    def __getitem__(self, index: int) -> typing.Any:
        ...


class NullableContextAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def flag(self) -> int:
        ...

    @flag.setter
    def flag(self, value: int) -> None:
        ...

    def __init__(self, value: int) -> None:
        ...


class Unsafe(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def copy_block(destination: typing.Any, source: typing.Any, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def copy_block(destination: int, source: int, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def copy_block_unaligned(destination: typing.Any, source: typing.Any, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def copy_block_unaligned(destination: int, source: int, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def init_block(start_address: typing.Any, value: int, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def init_block(start_address: int, value: int, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def init_block_unaligned(start_address: typing.Any, value: int, byte_count: int) -> None:
        ...

    @staticmethod
    @overload
    def init_block_unaligned(start_address: int, value: int, byte_count: int) -> None:
        ...


class ModuleInitializerAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DependencyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def dependent_assembly(self) -> str:
        ...

    @property
    def load_hint(self) -> System.Runtime.CompilerServices.LoadHint:
        ...

    def __init__(self, dependent_assembly_argument: str, load_hint_argument: System.Runtime.CompilerServices.LoadHint) -> None:
        ...


class SpecialNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class ScopedRefAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class NullablePublicOnlyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def includes_internals(self) -> bool:
        ...

    @includes_internals.setter
    def includes_internals(self, value: bool) -> None:
        ...

    def __init__(self, value: bool) -> None:
        ...


class DecimalConstantAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> float:
        ...

    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int) -> None:
        ...


class MetadataUpdateOriginalTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def original_type(self) -> typing.Type:
        ...

    def __init__(self, original_type: typing.Type) -> None:
        ...


class ParamCollectionAttribute(System.Attribute):
    """This class has no documentation."""


class DiscardableAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CompilerFeatureRequiredAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def feature_name(self) -> str:
        ...

    @property
    def is_optional(self) -> bool:
        ...

    REF_STRUCTS: str = ...

    REQUIRED_MEMBERS: str = ...

    def __init__(self, feature_name: str) -> None:
        ...


class AsyncStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """This class has no documentation."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class IStrongBox(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def value(self) -> System.Object:
        ...

    @value.setter
    def value(self, value: System.Object) -> None:
        ...


class StrongBox(typing.Generic[System_Runtime_CompilerServices_StrongBox_T], System.Object, System.Runtime.CompilerServices.IStrongBox):
    """This class has no documentation."""

    @property
    def value(self) -> System_Runtime_CompilerServices_StrongBox_T:
        ...

    @value.setter
    def value(self, value: System_Runtime_CompilerServices_StrongBox_T) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: System_Runtime_CompilerServices_StrongBox_T) -> None:
        ...


class DisablePrivateReflectionAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AsyncIteratorMethodBuilder:
    """This class has no documentation."""

    def complete(self) -> None:
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncIteratorMethodBuilder:
        ...


class CallerFilePathAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AsyncMethodBuilderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def builder_type(self) -> typing.Type:
        ...

    def __init__(self, builder_type: typing.Type) -> None:
        ...


class TupleElementNamesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def transform_names(self) -> typing.List[str]:
        ...

    def __init__(self, transform_names: typing.List[str]) -> None:
        ...


class ExtensionMarkerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    def __init__(self, name: str) -> None:
        ...


class CallerLineNumberAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IsConst(System.Object):
    """This class has no documentation."""


class ConfiguredValueTaskAwaitable(typing.Generic[System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult]):
    """This class has no documentation."""

    def get_awaiter(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter:
        ...


class _EventContainer(typing.Generic[System_Runtime_CompilerServices__EventContainer_Callable, System_Runtime_CompilerServices__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Runtime_CompilerServices__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Runtime_CompilerServices__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Runtime_CompilerServices__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


