from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.Runtime.CompilerServices
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks
import System.Threading.Tasks.Sources

System_Threading_Tasks_Task = typing.Any
System_Threading_Tasks_ValueTask = typing.Any

System_Threading_Tasks_Task_TResult = typing.TypeVar("System_Threading_Tasks_Task_TResult")
System_Threading_Tasks_TaskCompletionSource_TResult = typing.TypeVar("System_Threading_Tasks_TaskCompletionSource_TResult")
System_Threading_Tasks_TaskFactory_TResult = typing.TypeVar("System_Threading_Tasks_TaskFactory_TResult")
System_Threading_Tasks_ValueTask_TResult = typing.TypeVar("System_Threading_Tasks_ValueTask_TResult")
System_Threading_Tasks__EventContainer_Callable = typing.TypeVar("System_Threading_Tasks__EventContainer_Callable")
System_Threading_Tasks__EventContainer_ReturnType = typing.TypeVar("System_Threading_Tasks__EventContainer_ReturnType")


class TaskExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def unwrap(task: System.Threading.Tasks.Task[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        ...


class TaskCanceledException(System.OperationCanceledException):
    """This class has no documentation."""

    @property
    def task(self) -> System.Threading.Tasks.Task:
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
    def __init__(self, message: str, inner_exception: System.Exception, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class TaskStatus(IntEnum):
    """This class has no documentation."""

    CREATED = 0

    WAITING_FOR_ACTIVATION = 1

    WAITING_TO_RUN = 2

    RUNNING = 3

    WAITING_FOR_CHILDREN_TO_COMPLETE = 4

    RAN_TO_COMPLETION = 5

    CANCELED = 6

    FAULTED = 7


class TaskCreationOptions(IntEnum):
    """This class has no documentation."""

    NONE = ...

    PREFER_FAIRNESS = ...

    LONG_RUNNING = ...

    ATTACHED_TO_PARENT = ...

    DENY_CHILD_ATTACH = ...

    HIDE_SCHEDULER = ...

    RUN_CONTINUATIONS_ASYNCHRONOUSLY = ...


class UnobservedTaskExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def observed(self) -> bool:
        ...

    @property
    def exception(self) -> System.AggregateException:
        ...

    def __init__(self, exception: System.AggregateException) -> None:
        ...

    def set_observed(self) -> None:
        ...


class TaskScheduler(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def maximum_concurrency_level(self) -> int:
        ...

    DEFAULT: System.Threading.Tasks.TaskScheduler

    CURRENT: System.Threading.Tasks.TaskScheduler

    @property
    def id(self) -> int:
        ...

    unobserved_task_exception: _EventContainer[typing.Callable[[System.Object, System.Threading.Tasks.UnobservedTaskExceptionEventArgs], typing.Any], typing.Any]

    def __init__(self) -> None:
        ...

    @staticmethod
    def from_current_synchronization_context() -> System.Threading.Tasks.TaskScheduler:
        ...

    def get_scheduled_tasks(self) -> System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]:
        ...

    def try_execute_task(self, task: System.Threading.Tasks.Task) -> bool:
        ...

    def try_execute_task_inline(self, task: System.Threading.Tasks.Task, task_was_previously_queued: bool) -> bool:
        ...


class ConfigureAwaitOptions(IntEnum):
    """This class has no documentation."""

    NONE = ...

    CONTINUE_ON_CAPTURED_CONTEXT = ...

    SUPPRESS_THROWING = ...

    FORCE_YIELDING = ...


class TaskContinuationOptions(IntEnum):
    """This class has no documentation."""

    NONE = 0

    PREFER_FAIRNESS = ...

    LONG_RUNNING = ...

    ATTACHED_TO_PARENT = ...

    DENY_CHILD_ATTACH = ...

    HIDE_SCHEDULER = ...

    LAZY_CANCELLATION = ...

    RUN_CONTINUATIONS_ASYNCHRONOUSLY = ...

    NOT_ON_RAN_TO_COMPLETION = ...

    NOT_ON_FAULTED = ...

    NOT_ON_CANCELED = ...

    ONLY_ON_RAN_TO_COMPLETION = ...

    ONLY_ON_FAULTED = ...

    ONLY_ON_CANCELED = ...

    EXECUTE_SYNCHRONOUSLY = ...


class Task(typing.Generic[System_Threading_Tasks_Task_TResult], System_Threading_Tasks_Task):
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    CURRENT_ID: typing.Optional[int]

    @property
    def exception(self) -> System.AggregateException:
        ...

    @property
    def status(self) -> System.Threading.Tasks.TaskStatus:
        ...

    @property
    def is_canceled(self) -> bool:
        ...

    @property
    def is_completed(self) -> bool:
        ...

    @property
    def is_completed_successfully(self) -> bool:
        ...

    @property
    def creation_options(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def async_state(self) -> System.Object:
        ...

    FACTORY: System.Threading.Tasks.TaskFactory

    COMPLETED_TASK: System.Threading.Tasks.Task

    @property
    def is_faulted(self) -> bool:
        ...

    @property
    def result(self) -> System_Threading_Tasks_Task_TResult:
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[], typing.Any]) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[], typing.Any], creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult]) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        ...

    @overload
    def configure_await(self, options: System.Threading.Tasks.ConfigureAwaitOptions) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], typing.Any], state: typing.Any) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], typing.Any], state: typing.Any, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], typing.Any], state: typing.Any, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], typing.Any], state: typing.Any) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], typing.Any], state: typing.Any, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], typing.Any], state: typing.Any, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], typing.Any], scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], typing.Any], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], typing.Any], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, time_provider: System.TimeProvider) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, time_provider: System.TimeProvider, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(milliseconds_delay: int) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def delay(milliseconds_delay: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @staticmethod
    def from_canceled(cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def from_exception(exception: System.Exception) -> System.Threading.Tasks.Task:
        ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.TaskAwaiter:
        ...

    @staticmethod
    @overload
    def run(action: typing.Callable[[], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def run(action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def run(function: typing.Callable[[], System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def run(function: typing.Callable[[], System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def run_synchronously(self) -> None:
        ...

    @overload
    def run_synchronously(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        ...

    @overload
    def start(self) -> None:
        ...

    @overload
    def start(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        ...

    @overload
    def wait(self) -> None:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> None:
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken = ...) -> None:
        ...

    @staticmethod
    @overload
    def wait_any(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> int:
        ...

    @overload
    def wait_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, time_provider: System.TimeProvider) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, time_provider: System.TimeProvider, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def when_all(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def when_all(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def when_any(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_any(task_1: System.Threading.Tasks.Task, task_2: System.Threading.Tasks.Task) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_any(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_each(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Collections.Generic.IAsyncEnumerable[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_each(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Collections.Generic.IAsyncEnumerable[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    def Yield() -> System.Runtime.CompilerServices.YieldAwaitable:
        ...


class TaskCompletionSource(typing.Generic[System_Threading_Tasks_TaskCompletionSource_TResult], System.Object):
    """This class has no documentation."""

    @property
    def task(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def __init__(self, state: typing.Any) -> None:
        ...

    @overload
    def __init__(self, state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        ...

    @overload
    def set_canceled(self) -> None:
        ...

    @overload
    def set_canceled(self, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def set_exception(self, exception: System.Exception) -> None:
        ...

    @overload
    def set_exception(self, exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        ...

    @overload
    def set_from_task(self, completed_task: System.Threading.Tasks.Task) -> None:
        ...

    @overload
    def set_from_task(self, completed_task: System.Threading.Tasks.Task[System_Threading_Tasks_TaskCompletionSource_TResult]) -> None:
        ...

    @overload
    def set_result(self) -> None:
        ...

    @overload
    def set_result(self, result: System_Threading_Tasks_TaskCompletionSource_TResult) -> None:
        ...

    @overload
    def try_set_canceled(self) -> bool:
        ...

    @overload
    def try_set_canceled(self, cancellation_token: System.Threading.CancellationToken) -> bool:
        ...

    @overload
    def try_set_exception(self, exception: System.Exception) -> bool:
        ...

    @overload
    def try_set_exception(self, exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> bool:
        ...

    @overload
    def try_set_from_task(self, completed_task: System.Threading.Tasks.Task) -> bool:
        ...

    @overload
    def try_set_from_task(self, completed_task: System.Threading.Tasks.Task[System_Threading_Tasks_TaskCompletionSource_TResult]) -> bool:
        ...

    @overload
    def try_set_result(self) -> bool:
        ...

    @overload
    def try_set_result(self, result: System_Threading_Tasks_TaskCompletionSource_TResult) -> bool:
        ...


class TaskAsyncEnumerableExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def configure_await(source: System.IAsyncDisposable, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredAsyncDisposable:
        ...


class TaskFactory(typing.Generic[System_Threading_Tasks_TaskFactory_TResult], System.Object):
    """This class has no documentation."""

    @property
    def cancellation_token(self) -> System.Threading.CancellationToken:
        ...

    @property
    def scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def creation_options(self) -> System.Threading.Tasks.TaskCreationOptions:
        ...

    @property
    def continuation_options(self) -> System.Threading.Tasks.TaskContinuationOptions:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, cancellation_token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        ...

    @overload
    def __init__(self, creation_options: System.Threading.Tasks.TaskCreationOptions, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> None:
        ...

    @overload
    def __init__(self, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], typing.Any], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], typing.Any], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], typing.Any], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], typing.Any], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], typing.Any], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], typing.Any], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.Threading.Tasks.Task:
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], typing.Any], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], typing.Any], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], typing.Any], creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], typing.Any], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        ...

    @overload
    def start_new(self, action: typing.Callable[[], typing.Any]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[], typing.Any], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        ...

    @overload
    def start_new(self, action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        ...


class ConcurrentExclusiveSchedulerPair(System.Object):
    """This class has no documentation."""

    @property
    def completion(self) -> System.Threading.Tasks.Task:
        ...

    @property
    def concurrent_scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @property
    def exclusive_scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler, max_concurrency_level: int) -> None:
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler, max_concurrency_level: int, max_items_per_task: int) -> None:
        ...

    def complete(self) -> None:
        ...


class ValueTask(typing.Generic[System_Threading_Tasks_ValueTask_TResult], System.IEquatable[System_Threading_Tasks_ValueTask]):
    """This class has no documentation."""

    COMPLETED_TASK: System.Threading.Tasks.ValueTask

    @property
    def is_completed(self) -> bool:
        ...

    @property
    def is_completed_successfully(self) -> bool:
        ...

    @property
    def is_faulted(self) -> bool:
        ...

    @property
    def is_canceled(self) -> bool:
        ...

    @property
    def result(self) -> System_Threading_Tasks_ValueTask_TResult:
        ...

    @overload
    def __eq__(self, right: System.Threading.Tasks.ValueTask) -> bool:
        ...

    @overload
    def __eq__(self, right: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task) -> None:
        ...

    @overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource, token: int) -> None:
        ...

    @overload
    def __init__(self, result: System_Threading_Tasks_ValueTask_TResult) -> None:
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task[System_Threading_Tasks_ValueTask_TResult]) -> None:
        ...

    @overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource[System_Threading_Tasks_ValueTask_TResult], token: int) -> None:
        ...

    @overload
    def __ne__(self, right: System.Threading.Tasks.ValueTask) -> bool:
        ...

    @overload
    def __ne__(self, right: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        ...

    def as_task(self) -> System.Threading.Tasks.Task:
        ...

    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Threading.Tasks.ValueTask) -> bool:
        ...

    @overload
    def equals(self, other: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        ...

    @staticmethod
    def from_canceled(cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    def from_exception(exception: System.Exception) -> System.Threading.Tasks.ValueTask:
        ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.ValueTaskAwaiter:
        ...

    def get_hash_code(self) -> int:
        ...

    def preserve(self) -> System.Threading.Tasks.ValueTask:
        ...

    def to_string(self) -> str:
        ...


class TaskSchedulerException(System.Exception):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class _EventContainer(typing.Generic[System_Threading_Tasks__EventContainer_Callable, System_Threading_Tasks__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Threading_Tasks__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Threading_Tasks__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Threading_Tasks__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


