from typing import overload
from enum import IntEnum
import datetime
import typing

import System
import System.Collections.Generic
import System.Diagnostics
import System.Reflection


class StackFrame(System.Object):
    """This class has no documentation."""

    OFFSET_UNKNOWN: int = -1

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, skip_frames: int) -> None:
        ...

    @overload
    def __init__(self, skip_frames: int, need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, file_name: str, line_number: int) -> None:
        ...

    @overload
    def __init__(self, file_name: str, line_number: int, col_number: int) -> None:
        ...

    def get_file_column_number(self) -> int:
        ...

    def get_file_line_number(self) -> int:
        ...

    def get_file_name(self) -> str:
        ...

    def get_il_offset(self) -> int:
        ...

    def get_method(self) -> System.Reflection.MethodBase:
        ...

    def get_native_offset(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class DiagnosticMethodInfo(System.Object):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def declaring_type_name(self) -> str:
        ...

    @property
    def declaring_assembly_name(self) -> str:
        ...

    @staticmethod
    @overload
    def create(delegate: System.Delegate) -> System.Diagnostics.DiagnosticMethodInfo:
        ...

    @staticmethod
    @overload
    def create(frame: System.Diagnostics.StackFrame) -> System.Diagnostics.DiagnosticMethodInfo:
        ...


class DebugProvider(System.Object):
    """This class has no documentation."""

    def fail(self, message: str, detail_message: str) -> None:
        ...

    @staticmethod
    def fail_core(stack_trace: str, message: str, detail_message: str, error_source: str) -> None:
        ...

    def on_indent_level_changed(self, indent_level: int) -> None:
        ...

    def on_indent_size_changed(self, indent_size: int) -> None:
        ...

    def write(self, message: str) -> None:
        ...

    @staticmethod
    def write_core(message: str) -> None:
        ...

    def write_line(self, message: str) -> None:
        ...


class Debug(System.Object):
    """This class has no documentation."""

    class AssertInterpolatedStringHandler:
        """This class has no documentation."""

        def __init__(self, literal_length: int, formatted_count: int, condition: bool, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
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

    class WriteIfInterpolatedStringHandler:
        """This class has no documentation."""

        def __init__(self, literal_length: int, formatted_count: int, condition: bool, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
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

    auto_flush: bool

    indent_level: int

    indent_size: int

    @staticmethod
    @overload
    def Assert(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str = None) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: System.Diagnostics.Debug.AssertInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str, detailMessage: str) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: System.Diagnostics.Debug.AssertInterpolatedStringHandler, detailMessage: System.Diagnostics.Debug.AssertInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str, detailMessageFormat: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    def close() -> None:
        ...

    @staticmethod
    @overload
    def fail(message: str) -> None:
        ...

    @staticmethod
    @overload
    def fail(message: str, detail_message: str) -> None:
        ...

    @staticmethod
    def flush() -> None:
        ...

    @staticmethod
    def get_provider() -> System.Diagnostics.DebugProvider:
        ...

    @staticmethod
    def indent() -> None:
        ...

    @staticmethod
    @overload
    def print(message: str) -> None:
        ...

    @staticmethod
    @overload
    def print(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    def set_provider(provider: System.Diagnostics.DebugProvider) -> System.Diagnostics.DebugProvider:
        ...

    @staticmethod
    def unindent() -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write(message: str) -> None:
        ...

    @staticmethod
    @overload
    def write(message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler, category: str) -> None:
        ...


class Stopwatch(System.Object):
    """This class has no documentation."""

    FREQUENCY: int = ...

    IS_HIGH_RESOLUTION: bool = True

    @property
    def is_running(self) -> bool:
        ...

    @property
    def elapsed(self) -> datetime.timedelta:
        ...

    @property
    def elapsed_milliseconds(self) -> int:
        ...

    @property
    def elapsed_ticks(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def get_elapsed_time(starting_timestamp: int) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def get_elapsed_time(starting_timestamp: int, ending_timestamp: int) -> datetime.timedelta:
        ...

    @staticmethod
    def get_timestamp() -> int:
        ...

    def reset(self) -> None:
        ...

    def restart(self) -> None:
        ...

    def start(self) -> None:
        ...

    @staticmethod
    def start_new() -> System.Diagnostics.Stopwatch:
        ...

    def stop(self) -> None:
        ...

    def to_string(self) -> str:
        ...


class DebuggerBrowsableState(IntEnum):
    """This class has no documentation."""

    NEVER = 0

    COLLAPSED = 2

    ROOT_HIDDEN = 3


class DebuggerBrowsableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state(self) -> System.Diagnostics.DebuggerBrowsableState:
        ...

    def __init__(self, state: System.Diagnostics.DebuggerBrowsableState) -> None:
        ...


class DebuggerStepThroughAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StackTrace(System.Object):
    """This class has no documentation."""

    METHODS_TO_SKIP: int = 0

    @property
    def frame_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, f_need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, skip_frames: int) -> None:
        ...

    @overload
    def __init__(self, skip_frames: int, f_need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception, f_need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception, skip_frames: int) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception, skip_frames: int, f_need_file_info: bool) -> None:
        ...

    @overload
    def __init__(self, frame: System.Diagnostics.StackFrame) -> None:
        ...

    @overload
    def __init__(self, frames: System.Collections.Generic.IEnumerable[System.Diagnostics.StackFrame]) -> None:
        ...

    def get_frame(self, index: int) -> System.Diagnostics.StackFrame:
        ...

    def get_frames(self) -> typing.List[System.Diagnostics.StackFrame]:
        ...

    def to_string(self) -> str:
        ...


class ConditionalAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def condition_string(self) -> str:
        ...

    def __init__(self, condition_string: str) -> None:
        ...


class StackFrameExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_native_image_base(stack_frame: System.Diagnostics.StackFrame) -> System.IntPtr:
        ...

    @staticmethod
    def get_native_ip(stack_frame: System.Diagnostics.StackFrame) -> System.IntPtr:
        ...

    @staticmethod
    def has_il_offset(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_method(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_native_image(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_source(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...


class DebuggerDisplayAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def type(self) -> str:
        ...

    @type.setter
    def type(self, value: str) -> None:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    def __init__(self, value: str) -> None:
        ...


class UnreachableException(System.Exception):
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


class StackTraceHiddenAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class Debugger(System.Object):
    """This class has no documentation."""

    DEFAULT_CATEGORY: str

    @staticmethod
    def break_for_user_unhandled_exception(exception: System.Exception) -> None:
        ...


class DebuggerStepperBoundaryAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DebuggerTypeProxyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def proxy_type_name(self) -> str:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...


class DebuggerDisableUserUnhandledExceptionsAttribute(System.Attribute):
    """This class has no documentation."""


class DebuggerVisualizerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def visualizer_object_source_type_name(self) -> str:
        ...

    @property
    def visualizer_type_name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str, visualizer_object_source_type_name: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str, visualizer_object_source: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type, visualizer_object_source: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type, visualizer_object_source_type_name: str) -> None:
        ...


class DebuggableAttribute(System.Attribute):
    """This class has no documentation."""

    class DebuggingModes(IntEnum):
        """This class has no documentation."""

        NONE = ...

        DEFAULT = ...

        DISABLE_OPTIMIZATIONS = ...

        IGNORE_SYMBOL_STORE_SEQUENCE_POINTS = ...

        ENABLE_EDIT_AND_CONTINUE = ...

    @property
    def is_jit_tracking_enabled(self) -> bool:
        ...

    @property
    def is_jit_optimizer_disabled(self) -> bool:
        ...

    @property
    def debugging_flags(self) -> System.Diagnostics.DebuggableAttribute.DebuggingModes:
        ...

    @overload
    def __init__(self, is_jit_tracking_enabled: bool, is_jit_optimizer_disabled: bool) -> None:
        ...

    @overload
    def __init__(self, modes: System.Diagnostics.DebuggableAttribute.DebuggingModes) -> None:
        ...


class DebuggerHiddenAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DebuggerNonUserCodeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


