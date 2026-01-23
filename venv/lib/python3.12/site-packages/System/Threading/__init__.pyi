from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Globalization
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Security.Principal
import System.Threading
import System.Threading.Tasks

System_Threading_CancellationTokenRegistration = typing.Any
System_Threading_AsyncFlowControl = typing.Any
System_Threading_CancellationToken = typing.Any

System_Threading_AsyncLocal_T = typing.TypeVar("System_Threading_AsyncLocal_T")
System_Threading_AsyncLocalValueChangedArgs_T = typing.TypeVar("System_Threading_AsyncLocalValueChangedArgs_T")
System_Threading_ThreadLocal_T = typing.TypeVar("System_Threading_ThreadLocal_T")


class WaitHandle(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    INVALID_HANDLE: System.IntPtr = ...

    WAIT_TIMEOUT: int = ...

    @property
    def handle(self) -> System.IntPtr:
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @property
    def safe_wait_handle(self) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        ...

    @safe_wait_handle.setter
    def safe_wait_handle(self, value: Microsoft.Win32.SafeHandles.SafeWaitHandle) -> None:
        ...

    def __init__(self) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, explicit_disposing: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle) -> bool:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle]) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle]) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int, exit_context: bool) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exit_context: bool) -> int:
        ...

    @overload
    def wait_one(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def wait_one(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def wait_one(self) -> bool:
        ...

    @overload
    def wait_one(self, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @overload
    def wait_one(self, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...


class RegisteredWaitHandle(System.MarshalByRefObject):
    """This class has no documentation."""

    def unregister(self, wait_object: System.Threading.WaitHandle) -> bool:
        ...


class IThreadPoolWorkItem(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def execute(self) -> None:
        ...


class ThreadPool(System.Object):
    """This class has no documentation."""

    THREAD_COUNT: int

    COMPLETED_WORK_ITEM_COUNT: int

    PENDING_WORK_ITEM_COUNT: int

    @staticmethod
    @overload
    def bind_handle(os_handle: System.Runtime.InteropServices.SafeHandle) -> bool:
        ...

    @staticmethod
    @overload
    def bind_handle(os_handle: System.IntPtr) -> bool:
        ...

    @staticmethod
    def get_available_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    def get_max_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    def get_min_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    @overload
    def queue_user_work_item(call_back: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def queue_user_work_item(call_back: typing.Callable[[System.Object], typing.Any]) -> bool:
        ...

    @staticmethod
    @overload
    def register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], typing.Any], state: typing.Any, milliseconds_time_out_interval: int, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], typing.Any], state: typing.Any, timeout: datetime.timedelta, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    def set_max_threads(worker_threads: int, completion_port_threads: int) -> bool:
        ...

    @staticmethod
    def set_min_threads(worker_threads: int, completion_port_threads: int) -> bool:
        ...

    @staticmethod
    def unsafe_queue_native_overlapped(overlapped: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_queue_user_work_item(call_back: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_queue_user_work_item(call_back: System.Threading.IThreadPoolWorkItem, prefer_local: bool) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], typing.Any], state: typing.Any, milliseconds_time_out_interval: int, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def unsafe_register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], typing.Any], state: typing.Any, timeout: datetime.timedelta, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...


class Overlapped(System.Object):
    """This class has no documentation."""

    @property
    def async_result(self) -> System.IAsyncResult:
        ...

    @async_result.setter
    def async_result(self, value: System.IAsyncResult) -> None:
        ...

    @property
    def offset_low(self) -> int:
        ...

    @offset_low.setter
    def offset_low(self, value: int) -> None:
        ...

    @property
    def offset_high(self) -> int:
        ...

    @offset_high.setter
    def offset_high(self, value: int) -> None:
        ...

    @property
    def event_handle(self) -> int:
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @event_handle.setter
    def event_handle(self, value: int) -> None:
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @property
    def event_handle_int_ptr(self) -> System.IntPtr:
        ...

    @event_handle_int_ptr.setter
    def event_handle_int_ptr(self, value: System.IntPtr) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, offset_lo: int, offset_hi: int, h_event: System.IntPtr, ar: System.IAsyncResult) -> None:
        ...

    @overload
    def __init__(self, offset_lo: int, offset_hi: int, h_event: int, ar: System.IAsyncResult) -> None:
        ...

    @staticmethod
    def free(native_overlapped_ptr: typing.Any) -> None:
        ...

    @overload
    def pack(self, iocb: typing.Callable[[int, int, typing.Any], typing.Any], user_data: typing.Any) -> typing.Any:
        ...

    @overload
    def pack(self, iocb: typing.Callable[[int, int, typing.Any], typing.Any]) -> typing.Any:
        ...

    @staticmethod
    def unpack(native_overlapped_ptr: typing.Any) -> System.Threading.Overlapped:
        ...

    @overload
    def unsafe_pack(self, iocb: typing.Callable[[int, int, typing.Any], typing.Any], user_data: typing.Any) -> typing.Any:
        ...

    @overload
    def unsafe_pack(self, iocb: typing.Callable[[int, int, typing.Any], typing.Any]) -> typing.Any:
        ...


class CancellationToken(System.IEquatable[System_Threading_CancellationToken]):
    """This class has no documentation."""

    NONE: System.Threading.CancellationToken

    @property
    def is_cancellation_requested(self) -> bool:
        ...

    @property
    def can_be_canceled(self) -> bool:
        ...

    @property
    def wait_handle(self) -> System.Threading.WaitHandle:
        ...

    def __eq__(self, right: System.Threading.CancellationToken) -> bool:
        ...

    def __init__(self, canceled: bool) -> None:
        ...

    def __ne__(self, right: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def equals(self, other: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Threading.CancellationToken) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], typing.Any], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any, use_synchronization_context: bool) -> System.Threading.CancellationTokenRegistration:
        ...

    @overload
    def register(self, callback: typing.Callable[[], typing.Any]) -> System.Threading.CancellationTokenRegistration:
        ...

    @overload
    def register(self, callback: typing.Callable[[], typing.Any], use_synchronization_context: bool) -> System.Threading.CancellationTokenRegistration:
        ...

    def throw_if_cancellation_requested(self) -> None:
        ...

    @overload
    def unsafe_register(self, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        ...

    @overload
    def unsafe_register(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], typing.Any], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        ...


class CancellationTokenRegistration(System.IEquatable[System_Threading_CancellationTokenRegistration], System.IDisposable, System.IAsyncDisposable):
    """This class has no documentation."""

    @property
    def token(self) -> System.Threading.CancellationToken:
        ...

    def __eq__(self, right: System.Threading.CancellationTokenRegistration) -> bool:
        ...

    def __ne__(self, right: System.Threading.CancellationTokenRegistration) -> bool:
        ...

    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Threading.CancellationTokenRegistration) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def unregister(self) -> bool:
        ...


class Timeout(System.Object):
    """This class has no documentation."""

    INFINITE_TIME_SPAN: datetime.timedelta = ...

    INFINITE: int = -1


class NamedWaitHandleOptions:
    """This class has no documentation."""

    @property
    def current_user_only(self) -> bool:
        ...

    @current_user_only.setter
    def current_user_only(self, value: bool) -> None:
        ...

    @property
    def current_session_only(self) -> bool:
        ...

    @current_session_only.setter
    def current_session_only(self, value: bool) -> None:
        ...


class Mutex(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initially_owned: bool, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        ...

    @overload
    def __init__(self, initially_owned: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.Mutex:
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.Mutex:
        ...

    def release_mutex(self) -> None:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.Mutex]) -> typing.Tuple[bool, System.Threading.Mutex]:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.Mutex]) -> typing.Tuple[bool, System.Threading.Mutex]:
        ...


class PreAllocatedOverlapped(System.Object, System.IDisposable, System.Threading.IDeferredDisposable):
    """This class has no documentation."""

    def __init__(self, callback: typing.Callable[[int, int, typing.Any], typing.Any], state: typing.Any, pin_data: typing.Any) -> None:
        ...

    def dispose(self) -> None:
        ...

    @staticmethod
    def unsafe_create(callback: typing.Callable[[int, int, typing.Any], typing.Any], state: typing.Any, pin_data: typing.Any) -> System.Threading.PreAllocatedOverlapped:
        ...


class ThreadInterruptedException(System.SystemException):
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


class EventResetMode(IntEnum):
    """This class has no documentation."""

    AUTO_RESET = 0

    MANUAL_RESET = 1


class EventWaitHandle(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.EventWaitHandle:
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.EventWaitHandle:
        ...

    def reset(self) -> bool:
        ...

    def set(self) -> bool:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.EventWaitHandle]) -> typing.Tuple[bool, System.Threading.EventWaitHandle]:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.EventWaitHandle]) -> typing.Tuple[bool, System.Threading.EventWaitHandle]:
        ...


class LockRecursionException(System.Exception):
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


class AsyncFlowControl(System.IEquatable[System_Threading_AsyncFlowControl], System.IDisposable):
    """This class has no documentation."""

    def __eq__(self, b: System.Threading.AsyncFlowControl) -> bool:
        ...

    def __ne__(self, b: System.Threading.AsyncFlowControl) -> bool:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Threading.AsyncFlowControl) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def undo(self) -> None:
        ...


class ExecutionContext(System.Object, System.IDisposable, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def capture() -> System.Threading.ExecutionContext:
        ...

    def create_copy(self) -> System.Threading.ExecutionContext:
        ...

    def dispose(self) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def is_flow_suppressed() -> bool:
        ...

    @staticmethod
    def restore(execution_context: System.Threading.ExecutionContext) -> None:
        ...

    @staticmethod
    def restore_flow() -> None:
        ...

    @staticmethod
    def run(execution_context: System.Threading.ExecutionContext, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> None:
        ...

    @staticmethod
    def suppress_flow() -> System.Threading.AsyncFlowControl:
        ...


class AbandonedMutexException(System.SystemException):
    """This class has no documentation."""

    @property
    def mutex(self) -> System.Threading.Mutex:
        ...

    @property
    def mutex_index(self) -> int:
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
    def __init__(self, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ApartmentState(IntEnum):
    """This class has no documentation."""

    STA = 0

    MTA = 1

    UNKNOWN = 2


class ThreadPriority(IntEnum):
    """This class has no documentation."""

    LOWEST = 0

    BELOW_NORMAL = 1

    NORMAL = 2

    ABOVE_NORMAL = 3

    HIGHEST = 4


class ThreadState(IntEnum):
    """This class has no documentation."""

    RUNNING = 0

    STOP_REQUESTED = 1

    SUSPEND_REQUESTED = 2

    BACKGROUND = 4

    UNSTARTED = 8

    STOPPED = 16

    WAIT_SLEEP_JOIN = 32

    SUSPENDED = 64

    ABORT_REQUESTED = 128

    ABORTED = 256


class CompressedStack(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def capture() -> System.Threading.CompressedStack:
        ...

    def create_copy(self) -> System.Threading.CompressedStack:
        ...

    @staticmethod
    def get_compressed_stack() -> System.Threading.CompressedStack:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def run(compressed_stack: System.Threading.CompressedStack, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> None:
        ...


class Thread(System.Runtime.ConstrainedExecution.CriticalFinalizerObject):
    """This class has no documentation."""

    @property
    def current_culture(self) -> System.Globalization.CultureInfo:
        ...

    @current_culture.setter
    def current_culture(self, value: System.Globalization.CultureInfo) -> None:
        ...

    @property
    def current_ui_culture(self) -> System.Globalization.CultureInfo:
        ...

    @current_ui_culture.setter
    def current_ui_culture(self, value: System.Globalization.CultureInfo) -> None:
        ...

    current_principal: System.Security.Principal.IPrincipal

    CURRENT_THREAD: System.Threading.Thread

    @property
    def execution_context(self) -> System.Threading.ExecutionContext:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def apartment_state(self) -> System.Threading.ApartmentState:
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @apartment_state.setter
    def apartment_state(self, value: System.Threading.ApartmentState) -> None:
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @property
    def is_alive(self) -> bool:
        ...

    @property
    def is_background(self) -> bool:
        ...

    @is_background.setter
    def is_background(self, value: bool) -> None:
        ...

    @property
    def is_thread_pool_thread(self) -> bool:
        ...

    @property
    def managed_thread_id(self) -> int:
        ...

    @property
    def priority(self) -> System.Threading.ThreadPriority:
        ...

    @priority.setter
    def priority(self, value: System.Threading.ThreadPriority) -> None:
        ...

    @property
    def thread_state(self) -> System.Threading.ThreadState:
        ...

    @overload
    def __init__(self, start: typing.Callable[[], typing.Any]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[], typing.Any], max_stack_size: int) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], typing.Any]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], typing.Any], max_stack_size: int) -> None:
        ...

    @overload
    def abort(self, state_info: typing.Any) -> None:
        ...

    @overload
    def abort(self) -> None:
        ...

    @staticmethod
    def allocate_data_slot() -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def allocate_named_data_slot(name: str) -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def begin_critical_region() -> None:
        ...

    @staticmethod
    def begin_thread_affinity() -> None:
        ...

    def disable_com_object_eager_cleanup(self) -> None:
        ...

    @staticmethod
    def end_critical_region() -> None:
        ...

    @staticmethod
    def end_thread_affinity() -> None:
        ...

    @staticmethod
    def free_named_data_slot(name: str) -> None:
        ...

    def get_apartment_state(self) -> System.Threading.ApartmentState:
        ...

    def get_compressed_stack(self) -> System.Threading.CompressedStack:
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def get_current_processor_id() -> int:
        ...

    @staticmethod
    def get_data(slot: System.LocalDataStoreSlot) -> System.Object:
        ...

    @staticmethod
    def get_domain() -> System.AppDomain:
        ...

    @staticmethod
    def get_domain_id() -> int:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_named_data_slot(name: str) -> System.LocalDataStoreSlot:
        ...

    def interrupt(self) -> None:
        ...

    @overload
    def join(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def join(self) -> None:
        ...

    @overload
    def join(self, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    def memory_barrier() -> None:
        ...

    @staticmethod
    def reset_abort() -> None:
        warnings.warn("Obsoletions.ThreadResetAbortMessage", DeprecationWarning)

    def resume(self) -> None:
        warnings.warn("Thread.Resume has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    def set_apartment_state(self, state: System.Threading.ApartmentState) -> None:
        ...

    def set_compressed_stack(self, stack: System.Threading.CompressedStack) -> None:
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def set_data(slot: System.LocalDataStoreSlot, data: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def sleep(milliseconds_timeout: int) -> None:
        ...

    @staticmethod
    @overload
    def sleep(timeout: datetime.timedelta) -> None:
        ...

    @staticmethod
    def spin_wait(iterations: int) -> None:
        ...

    @overload
    def start(self, parameter: typing.Any) -> None:
        ...

    @overload
    def start(self) -> None:
        ...

    def suspend(self) -> None:
        warnings.warn("Thread.Suspend has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    def try_set_apartment_state(self, state: System.Threading.ApartmentState) -> bool:
        ...

    @overload
    def unsafe_start(self, parameter: typing.Any) -> None:
        ...

    @overload
    def unsafe_start(self) -> None:
        ...

    @staticmethod
    @overload
    def volatile_read(address: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def volatile_read(address: int) -> int:
        ...

    @staticmethod
    @overload
    def volatile_read(address: float) -> float:
        ...

    @staticmethod
    @overload
    def volatile_read(address: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def volatile_read(address: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def volatile_write(address: typing.Any, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def volatile_write(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def volatile_write(address: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def volatile_write(address: System.IntPtr, value: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def volatile_write(address: System.UIntPtr, value: System.UIntPtr) -> None:
        ...

    @staticmethod
    def Yield() -> bool:
        ...


class AutoResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initial_state: bool) -> None:
        ...


class LazyThreadSafetyMode(IntEnum):
    """This class has no documentation."""

    NONE = 0

    PUBLICATION_ONLY = 1

    EXECUTION_AND_PUBLICATION = 2


class Monitor(System.Object):
    """This class has no documentation."""

    LOCK_CONTENTION_COUNT: int

    @staticmethod
    @overload
    def enter(obj: typing.Any, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def enter(obj: typing.Any) -> None:
        ...

    @staticmethod
    def exit(obj: typing.Any) -> None:
        ...

    @staticmethod
    def is_entered(obj: typing.Any) -> bool:
        ...

    @staticmethod
    def pulse(obj: typing.Any) -> None:
        ...

    @staticmethod
    def pulse_all(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, timeout: datetime.timedelta, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, milliseconds_timeout: int, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, milliseconds_timeout: int) -> bool:
        ...


class Semaphore(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initial_count: int, maximum_count: int) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.Semaphore:
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.Semaphore:
        ...

    @overload
    def release(self) -> int:
        ...

    @overload
    def release(self, release_count: int) -> int:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.Semaphore]) -> typing.Tuple[bool, System.Threading.Semaphore]:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.Semaphore]) -> typing.Tuple[bool, System.Threading.Semaphore]:
        ...


class Lock(System.Object):
    """This class has no documentation."""

    class Scope:
        """This class has no documentation."""

        def dispose(self) -> None:
            ...

    @property
    def is_held_by_current_thread(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def enter(self) -> None:
        ...

    def enter_scope(self) -> System.Threading.Lock.Scope:
        ...

    def exit(self) -> None:
        ...

    @overload
    def try_enter(self) -> bool:
        ...

    @overload
    def try_enter(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_enter(self, timeout: datetime.timedelta) -> bool:
        ...


class AsyncLocal(typing.Generic[System_Threading_AsyncLocal_T], System.Object, System.Threading.IAsyncLocal):
    """This class has no documentation."""

    @property
    def value(self) -> System_Threading_AsyncLocal_T:
        ...

    @value.setter
    def value(self, value: System_Threading_AsyncLocal_T) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value_changed_handler: typing.Callable[[System.Threading.AsyncLocalValueChangedArgs[System_Threading_AsyncLocal_T]], typing.Any]) -> None:
        ...


class AsyncLocalValueChangedArgs(typing.Generic[System_Threading_AsyncLocalValueChangedArgs_T]):
    """This class has no documentation."""

    @property
    def previous_value(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        ...

    @property
    def current_value(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        ...

    @property
    def thread_context_changed(self) -> bool:
        ...


class SemaphoreFullException(System.SystemException):
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


class LockRecursionPolicy(IntEnum):
    """This class has no documentation."""

    NO_RECURSION = 0

    SUPPORTS_RECURSION = 1


class ReaderWriterLockSlim(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def is_read_lock_held(self) -> bool:
        ...

    @property
    def is_upgradeable_read_lock_held(self) -> bool:
        ...

    @property
    def is_write_lock_held(self) -> bool:
        ...

    @property
    def recursion_policy(self) -> System.Threading.LockRecursionPolicy:
        ...

    @property
    def current_read_count(self) -> int:
        ...

    @property
    def recursive_read_count(self) -> int:
        ...

    @property
    def recursive_upgrade_count(self) -> int:
        ...

    @property
    def recursive_write_count(self) -> int:
        ...

    @property
    def waiting_read_count(self) -> int:
        ...

    @property
    def waiting_upgrade_count(self) -> int:
        ...

    @property
    def waiting_write_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, recursion_policy: System.Threading.LockRecursionPolicy) -> None:
        ...

    def dispose(self) -> None:
        ...

    def enter_read_lock(self) -> None:
        ...

    def enter_upgradeable_read_lock(self) -> None:
        ...

    def enter_write_lock(self) -> None:
        ...

    def exit_read_lock(self) -> None:
        ...

    def exit_upgradeable_read_lock(self) -> None:
        ...

    def exit_write_lock(self) -> None:
        ...

    @overload
    def try_enter_read_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_read_lock(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_enter_upgradeable_read_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_upgradeable_read_lock(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_enter_write_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_write_lock(self, milliseconds_timeout: int) -> bool:
        ...


class LazyInitializer(System.Object):
    """This class has no documentation."""


class ThreadStartException(System.SystemException):
    """This class has no documentation."""


class Interlocked(System.Object):
    """This class has no documentation."""

    @staticmethod
    def add(location_1: int, value: int) -> int:
        ...

    @staticmethod
    def And(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: typing.Any, value: typing.Any, comparand: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: int, value: int, comparand: int) -> int:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: float, value: float, comparand: float) -> float:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: System.IntPtr, value: System.IntPtr, comparand: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: System.UIntPtr, value: System.UIntPtr, comparand: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def decrement(location: int) -> int:
        ...

    @staticmethod
    @overload
    def exchange(location_1: typing.Any, value: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def exchange(location_1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def exchange(location_1: float, value: float) -> float:
        ...

    @staticmethod
    @overload
    def exchange(location_1: System.IntPtr, value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def exchange(location_1: System.UIntPtr, value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def increment(location: int) -> int:
        ...

    @staticmethod
    def memory_barrier() -> None:
        ...

    @staticmethod
    def memory_barrier_process_wide() -> None:
        ...

    @staticmethod
    def Or(location1: int, value: int) -> int:
        ...

    @staticmethod
    def read(location: int) -> int:
        ...


class SynchronizationLockException(System.SystemException):
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


class ManualResetEventSlim(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def wait_handle(self) -> System.Threading.WaitHandle:
        ...

    @property
    def is_set(self) -> bool:
        ...

    @property
    def spin_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, spin_count: int) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def reset(self) -> None:
        ...

    def set(self) -> None:
        ...

    @overload
    def wait(self) -> None:
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...


class ThreadPoolBoundHandle(System.Object, System.IDisposable, System.Threading.IDeferredDisposable):
    """This class has no documentation."""

    @property
    def handle(self) -> System.Runtime.InteropServices.SafeHandle:
        ...

    @overload
    def allocate_native_overlapped(self, callback: typing.Callable[[int, int, typing.Any], typing.Any], state: typing.Any, pin_data: typing.Any) -> typing.Any:
        ...

    @overload
    def allocate_native_overlapped(self, pre_allocated: System.Threading.PreAllocatedOverlapped) -> typing.Any:
        ...

    @staticmethod
    def bind_handle(handle: System.Runtime.InteropServices.SafeHandle) -> System.Threading.ThreadPoolBoundHandle:
        ...

    def dispose(self) -> None:
        ...

    def free_native_overlapped(self, overlapped: typing.Any) -> None:
        ...

    @staticmethod
    def get_native_overlapped_state(overlapped: typing.Any) -> System.Object:
        ...

    def unsafe_allocate_native_overlapped(self, callback: typing.Callable[[int, int, typing.Any], typing.Any], state: typing.Any, pin_data: typing.Any) -> typing.Any:
        ...


class ThreadLocal(typing.Generic[System_Threading_ThreadLocal_T], System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def value(self) -> System_Threading_ThreadLocal_T:
        ...

    @value.setter
    def value(self, value: System_Threading_ThreadLocal_T) -> None:
        ...

    @property
    def values(self) -> typing.List[System_Threading_ThreadLocal_T]:
        ...

    @property
    def is_value_created(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, track_all_values: bool) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Threading_ThreadLocal_T]) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Threading_ThreadLocal_T], track_all_values: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def to_string(self) -> str:
        ...


class ThreadStateException(System.SystemException):
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


class SynchronizationContext(System.Object):
    """This class has no documentation."""

    CURRENT: System.Threading.SynchronizationContext

    def __init__(self) -> None:
        ...

    def create_copy(self) -> System.Threading.SynchronizationContext:
        ...

    def is_wait_notification_required(self) -> bool:
        ...

    def operation_completed(self) -> None:
        ...

    def operation_started(self) -> None:
        ...

    def post(self, d: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> None:
        ...

    def send(self, d: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> None:
        ...

    @staticmethod
    def set_synchronization_context(sync_context: System.Threading.SynchronizationContext) -> None:
        ...

    def set_wait_notification_required(self) -> None:
        ...

    def wait(self, wait_handles: typing.List[System.IntPtr], wait_all: bool, milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    def wait_helper(wait_handles: typing.List[System.IntPtr], wait_all: bool, milliseconds_timeout: int) -> int:
        ...


class SemaphoreSlim(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def current_count(self) -> int:
        ...

    @property
    def available_wait_handle(self) -> System.Threading.WaitHandle:
        ...

    @overload
    def __init__(self, initial_count: int) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, max_count: int) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def release(self) -> int:
        ...

    @overload
    def release(self, release_count: int) -> int:
        ...

    @overload
    def wait(self) -> None:
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def wait_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, milliseconds_timeout: int) -> System.Threading.Tasks.Task[bool]:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta) -> System.Threading.Tasks.Task[bool]:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        ...

    @overload
    def wait_async(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        ...


class WaitHandleCannotBeOpenedException(System.ApplicationException):
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


class Timer(System.MarshalByRefObject, System.Threading.ITimer):
    """This class has no documentation."""

    ACTIVE_COUNT: int

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any, due_time: int, period: int) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], typing.Any], state: typing.Any, due_time: datetime.timedelta, period: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], typing.Any]) -> None:
        ...

    @overload
    def change(self, due_time: int, period: int) -> bool:
        ...

    @overload
    def change(self, due_time: datetime.timedelta, period: datetime.timedelta) -> bool:
        ...

    @overload
    def dispose(self, notify_object: System.Threading.WaitHandle) -> bool:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...


class Volatile(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def read(location: bool) -> bool:
        ...

    @staticmethod
    @overload
    def read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def read(location: float) -> float:
        ...

    @staticmethod
    @overload
    def read(location: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read(location: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def read_barrier() -> None:
        ...

    @staticmethod
    @overload
    def write(location: bool, value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def write(location: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def write(location: System.IntPtr, value: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write(location: System.UIntPtr, value: System.UIntPtr) -> None:
        ...

    @staticmethod
    def write_barrier() -> None:
        ...


class NativeOverlapped:
    """This class has no documentation."""

    @property
    def internal_low(self) -> System.IntPtr:
        ...

    @internal_low.setter
    def internal_low(self, value: System.IntPtr) -> None:
        ...

    @property
    def internal_high(self) -> System.IntPtr:
        ...

    @internal_high.setter
    def internal_high(self, value: System.IntPtr) -> None:
        ...

    @property
    def offset_low(self) -> int:
        ...

    @offset_low.setter
    def offset_low(self, value: int) -> None:
        ...

    @property
    def offset_high(self) -> int:
        ...

    @offset_high.setter
    def offset_high(self, value: int) -> None:
        ...

    @property
    def event_handle(self) -> System.IntPtr:
        ...

    @event_handle.setter
    def event_handle(self, value: System.IntPtr) -> None:
        ...


class ThreadExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception(self) -> System.Exception:
        ...

    def __init__(self, t: System.Exception) -> None:
        ...


class ThreadAbortException(System.SystemException):
    """This class has no documentation."""

    @property
    def exception_state(self) -> System.Object:
        ...


class PeriodicTimer(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def period(self) -> datetime.timedelta:
        ...

    @period.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, period: datetime.timedelta, time_provider: System.TimeProvider) -> None:
        ...

    def dispose(self) -> None:
        ...

    def wait_for_next_tick_async(self, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[bool]:
        ...


class WaitHandleExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_safe_wait_handle(wait_handle: System.Threading.WaitHandle) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        ...

    @staticmethod
    def set_safe_wait_handle(wait_handle: System.Threading.WaitHandle, value: Microsoft.Win32.SafeHandles.SafeWaitHandle) -> None:
        ...


class SpinLock:
    """This class has no documentation."""

    @property
    def is_held(self) -> bool:
        ...

    @property
    def is_held_by_current_thread(self) -> bool:
        ...

    @property
    def is_thread_owner_tracking_enabled(self) -> bool:
        ...

    def __init__(self, enable_thread_owner_tracking: bool) -> None:
        ...

    def enter(self, lock_taken: bool) -> None:
        ...

    @overload
    def exit(self) -> None:
        ...

    @overload
    def exit(self, use_memory_barrier: bool) -> None:
        ...

    @overload
    def try_enter(self, lock_taken: bool) -> None:
        ...

    @overload
    def try_enter(self, timeout: datetime.timedelta, lock_taken: bool) -> None:
        ...

    @overload
    def try_enter(self, milliseconds_timeout: int, lock_taken: bool) -> None:
        ...


class ManualResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initial_state: bool) -> None:
        ...


class CancellationTokenSource(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def is_cancellation_requested(self) -> bool:
        ...

    @property
    def token(self) -> System.Threading.CancellationToken:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, delay: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, delay: datetime.timedelta, time_provider: System.TimeProvider) -> None:
        ...

    @overload
    def __init__(self, milliseconds_delay: int) -> None:
        ...

    @overload
    def cancel(self) -> None:
        ...

    @overload
    def cancel(self, throw_on_first_exception: bool) -> None:
        ...

    @overload
    def cancel_after(self, delay: datetime.timedelta) -> None:
        ...

    @overload
    def cancel_after(self, milliseconds_delay: int) -> None:
        ...

    def cancel_async(self) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def create_linked_token_source(token_1: System.Threading.CancellationToken, token_2: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        ...

    @staticmethod
    @overload
    def create_linked_token_source(token: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        ...

    @staticmethod
    @overload
    def create_linked_token_source(*tokens: typing.Union[System.Threading.CancellationToken, typing.Iterable[System.Threading.CancellationToken]]) -> System.Threading.CancellationTokenSource:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def try_reset(self) -> bool:
        ...


class SpinWait:
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def next_spin_will_yield(self) -> bool:
        ...

    def reset(self) -> None:
        ...

    @overload
    def spin_once(self) -> None:
        ...

    @overload
    def spin_once(self, sleep_1_threshold: int) -> None:
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool]) -> None:
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool], timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool], milliseconds_timeout: int) -> bool:
        ...


