from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Diagnostics.Tracing
import System.Runtime.Serialization

System_Diagnostics_Tracing__EventContainer_Callable = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_Callable")
System_Diagnostics_Tracing__EventContainer_ReturnType = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_ReturnType")


class EventSourceException(System.Exception):
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


class EventSourceSettings(IntEnum):
    """This class has no documentation."""

    DEFAULT = 0

    THROW_ON_EVENT_WRITE_ERRORS = 1

    ETW_MANIFEST_EVENT_FORMAT = 4

    ETW_SELF_DESCRIBING_EVENT_FORMAT = 8


class EventLevel(IntEnum):
    """This class has no documentation."""

    LOG_ALWAYS = 0

    CRITICAL = 1

    ERROR = 2

    WARNING = 3

    INFORMATIONAL = 4

    VERBOSE = 5


class EventKeywords(IntEnum):
    """This class has no documentation."""

    NONE = ...

    ALL = ...

    MICROSOFT_TELEMETRY = ...

    WDI_CONTEXT = ...

    WDI_DIAGNOSTIC = ...

    SQM = ...

    AUDIT_FAILURE = ...

    AUDIT_SUCCESS = ...

    CORRELATION_HINT = ...

    EVENT_LOG_CLASSIC = ...


class EventChannel(IntEnum):
    """This class has no documentation."""

    NONE = 0

    ADMIN = 16

    OPERATIONAL = 17

    ANALYTIC = 18

    DEBUG = 19


class EventManifestOptions(IntEnum):
    """This class has no documentation."""

    NONE = ...

    STRICT = ...

    ALL_CULTURES = ...

    ONLY_IF_NEEDED_FOR_REGISTRATION = ...

    ALLOW_EVENT_SOURCE_OVERRIDE = ...


class EventCommand(IntEnum):
    """This class has no documentation."""

    UPDATE = 0

    SEND_MANIFEST = -1

    ENABLE = -2

    DISABLE = -3


class EventCommandEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def command(self) -> System.Diagnostics.Tracing.EventCommand:
        ...

    @property
    def arguments(self) -> System.Collections.Generic.IDictionary[str, str]:
        ...

    def disable_event(self, event_id: int) -> bool:
        ...

    def enable_event(self, event_id: int) -> bool:
        ...


class EventOpcode(IntEnum):
    """This class has no documentation."""

    INFO = 0

    START = 1

    STOP = 2

    DATA_COLLECTION_START = 3

    DATA_COLLECTION_STOP = 4

    EXTENSION = 5

    REPLY = 6

    RESUME = 7

    SUSPEND = 8

    SEND = 9

    RECEIVE = 240


class EventTags(IntEnum):
    """This class has no documentation."""

    NONE = 0


class EventActivityOptions(IntEnum):
    """This class has no documentation."""

    NONE = 0

    DISABLE = ...

    RECURSIVE = ...

    DETACHABLE = ...


class EventSourceOptions:
    """This class has no documentation."""

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        ...

    @level.setter
    def level(self, value: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        ...

    @opcode.setter
    def opcode(self, value: System.Diagnostics.Tracing.EventOpcode) -> None:
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @keywords.setter
    def keywords(self, value: System.Diagnostics.Tracing.EventKeywords) -> None:
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventTags) -> None:
        ...

    @property
    def activity_options(self) -> System.Diagnostics.Tracing.EventActivityOptions:
        ...

    @activity_options.setter
    def activity_options(self, value: System.Diagnostics.Tracing.EventActivityOptions) -> None:
        ...


class EventSource(System.Object, System.IDisposable):
    """This class has no documentation."""

    class EventSourcePrimitive:
        """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def guid(self) -> System.Guid:
        ...

    @property
    def settings(self) -> System.Diagnostics.Tracing.EventSourceSettings:
        ...

    @property
    def construction_exception(self) -> System.Exception:
        ...

    @property
    def event_command_executed(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], typing.Any], typing.Any]:
        ...

    @event_command_executed.setter
    def event_command_executed(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], typing.Any], typing.Any]) -> None:
        ...

    CURRENT_THREAD_ACTIVITY_ID: System.Guid

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, throw_on_event_write_errors: bool) -> None:
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings, *traits: typing.Union[str, typing.Iterable[str]]) -> None:
        ...

    @overload
    def __init__(self, event_source_name: str, event_source_guid: System.Guid) -> None:
        ...

    @overload
    def __init__(self, event_source_name: str, event_source_guid: System.Guid, settings: System.Diagnostics.Tracing.EventSourceSettings, traits: typing.List[str] = None) -> None:
        ...

    @overload
    def __init__(self, event_source_name: str) -> None:
        ...

    @overload
    def __init__(self, event_source_name: str, config: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        ...

    @overload
    def __init__(self, event_source_name: str, config: System.Diagnostics.Tracing.EventSourceSettings, *traits: typing.Union[str, typing.Iterable[str]]) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @staticmethod
    @overload
    def generate_manifest(event_source_type: typing.Type, assembly_path_to_include_in_manifest: str) -> str:
        ...

    @staticmethod
    @overload
    def generate_manifest(event_source_type: typing.Type, assembly_path_to_include_in_manifest: str, flags: System.Diagnostics.Tracing.EventManifestOptions) -> str:
        ...

    @staticmethod
    def get_guid(event_source_type: typing.Type) -> System.Guid:
        ...

    @staticmethod
    def get_name(event_source_type: typing.Type) -> str:
        ...

    @staticmethod
    def get_sources() -> System.Collections.Generic.IEnumerable[System.Diagnostics.Tracing.EventSource]:
        ...

    def get_trait(self, key: str) -> str:
        ...

    @overload
    def is_enabled(self) -> bool:
        ...

    @overload
    def is_enabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords) -> bool:
        ...

    @overload
    def is_enabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords, channel: System.Diagnostics.Tracing.EventChannel) -> bool:
        ...

    def on_event_command(self, command: System.Diagnostics.Tracing.EventCommandEventArgs) -> None:
        ...

    @staticmethod
    def send_command(event_source: System.Diagnostics.Tracing.EventSource, command: System.Diagnostics.Tracing.EventCommand, command_arguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @staticmethod
    @overload
    def set_current_thread_activity_id(activity_id: System.Guid) -> None:
        ...

    @staticmethod
    @overload
    def set_current_thread_activity_id(activity_id: System.Guid, old_activity_that_will_continue: typing.Optional[System.Guid]) -> typing.Tuple[None, System.Guid]:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def write(self, event_name: str) -> None:
        ...

    @overload
    def write(self, event_name: str, options: System.Diagnostics.Tracing.EventSourceOptions) -> None:
        ...

    @overload
    def write_event(self, event_id: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: int, arg_3: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: str) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: str, arg_3: str) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: int, arg_3: int) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: str) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: typing.List[int]) -> None:
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: typing.List[int]) -> None:
        ...

    @overload
    def write_event(self, event_id: int, *args: typing.Union[System.Diagnostics.Tracing.EventSource.EventSourcePrimitive, typing.Iterable[System.Diagnostics.Tracing.EventSource.EventSourcePrimitive]]) -> None:
        ...

    @overload
    def write_event(self, event_id: int, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def write_event_core(self, event_id: int, event_data_count: int, data: typing.Any) -> None:
        ...

    def write_event_with_related_activity_id(self, event_id: int, related_activity_id: System.Guid, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def write_event_with_related_activity_id_core(self, event_id: int, related_activity_id: typing.Any, event_data_count: int, data: typing.Any) -> None:
        ...


class DiagnosticCounter(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def display_name(self) -> str:
        ...

    @display_name.setter
    def display_name(self, value: str) -> None:
        ...

    @property
    def display_units(self) -> str:
        ...

    @display_units.setter
    def display_units(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        ...

    def add_metadata(self, key: str, value: str) -> None:
        ...

    def dispose(self) -> None:
        ...


class PollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """This class has no documentation."""

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource, metric_provider: typing.Callable[[], float]) -> None:
        ...

    def to_string(self) -> str:
        ...


class EventTask(IntEnum):
    """This class has no documentation."""

    NONE = 0


class EventSourceCreatedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        ...


class EventWrittenEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def event_name(self) -> str:
        ...

    @property
    def event_id(self) -> int:
        ...

    @property
    def activity_id(self) -> System.Guid:
        ...

    @property
    def related_activity_id(self) -> System.Guid:
        ...

    @property
    def payload(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Object]:
        ...

    @property
    def payload_names(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        ...

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        ...

    @property
    def task(self) -> System.Diagnostics.Tracing.EventTask:
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        ...

    @property
    def message(self) -> str:
        ...

    @property
    def channel(self) -> System.Diagnostics.Tracing.EventChannel:
        ...

    @property
    def version(self) -> int:
        ...

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        ...

    @property
    def os_thread_id(self) -> int:
        ...

    @property
    def time_stamp(self) -> datetime.datetime:
        ...


class EventListener(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def event_source_created(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], typing.Any], typing.Any]:
        ...

    @event_source_created.setter
    def event_source_created(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def event_written(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], typing.Any], typing.Any]:
        ...

    @event_written.setter
    def event_written(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self) -> None:
        ...

    def disable_events(self, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, match_any_keyword: System.Diagnostics.Tracing.EventKeywords) -> None:
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, match_any_keyword: System.Diagnostics.Tracing.EventKeywords, arguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...


class EventSourceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def guid(self) -> str:
        ...

    @guid.setter
    def guid(self, value: str) -> None:
        ...

    @property
    def localization_resources(self) -> str:
        ...

    @localization_resources.setter
    def localization_resources(self, value: str) -> None:
        ...


class EventAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def event_id(self) -> int:
        ...

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        ...

    @level.setter
    def level(self, value: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @keywords.setter
    def keywords(self, value: System.Diagnostics.Tracing.EventKeywords) -> None:
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        ...

    @opcode.setter
    def opcode(self, value: System.Diagnostics.Tracing.EventOpcode) -> None:
        ...

    @property
    def task(self) -> System.Diagnostics.Tracing.EventTask:
        ...

    @task.setter
    def task(self, value: System.Diagnostics.Tracing.EventTask) -> None:
        ...

    @property
    def channel(self) -> System.Diagnostics.Tracing.EventChannel:
        ...

    @channel.setter
    def channel(self, value: System.Diagnostics.Tracing.EventChannel) -> None:
        ...

    @property
    def version(self) -> int:
        ...

    @version.setter
    def version(self, value: int) -> None:
        ...

    @property
    def message(self) -> str:
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventTags) -> None:
        ...

    @property
    def activity_options(self) -> System.Diagnostics.Tracing.EventActivityOptions:
        ...

    @activity_options.setter
    def activity_options(self, value: System.Diagnostics.Tracing.EventActivityOptions) -> None:
        ...

    def __init__(self, event_id: int) -> None:
        ...


class NonEventAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IncrementingPollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """This class has no documentation."""

    @property
    def display_rate_time_scale(self) -> datetime.timedelta:
        ...

    @display_rate_time_scale.setter
    def display_rate_time_scale(self, value: datetime.timedelta) -> None:
        ...

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource, total_value_provider: typing.Callable[[], float]) -> None:
        ...

    def to_string(self) -> str:
        ...


class EventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """This class has no documentation."""

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        ...

    def to_string(self) -> str:
        ...

    def write_metric(self, value: float) -> None:
        ...


class IncrementingEventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """This class has no documentation."""

    @property
    def display_rate_time_scale(self) -> datetime.timedelta:
        ...

    @display_rate_time_scale.setter
    def display_rate_time_scale(self, value: datetime.timedelta) -> None:
        ...

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        ...

    def increment(self, increment: float = 1) -> None:
        ...

    def to_string(self) -> str:
        ...


class EventFieldFormat(IntEnum):
    """This class has no documentation."""

    DEFAULT = 0

    STRING = 2

    BOOLEAN = 3

    HEXADECIMAL = 4

    XML = 11

    JSON = 12

    H_RESULT = 15


class EventIgnoreAttribute(System.Attribute):
    """This class has no documentation."""


class EventFieldTags(IntEnum):
    """This class has no documentation."""

    NONE = 0


class EventFieldAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventFieldTags:
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventFieldTags) -> None:
        ...

    @property
    def format(self) -> System.Diagnostics.Tracing.EventFieldFormat:
        ...

    @format.setter
    def format(self, value: System.Diagnostics.Tracing.EventFieldFormat) -> None:
        ...


class EventDataAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...


class _EventContainer(typing.Generic[System_Diagnostics_Tracing__EventContainer_Callable, System_Diagnostics_Tracing__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Diagnostics_Tracing__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


