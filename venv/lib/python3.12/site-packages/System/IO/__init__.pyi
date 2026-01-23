from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections.Generic
import System.IO
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Text
import System.Threading
import System.Threading.Tasks


class TextReader(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.TextReader = ...

    def __init__(self) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def read_block(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    def synchronized(reader: System.IO.TextReader) -> System.IO.TextReader:
        ...


class SeekOrigin(IntEnum):
    """This class has no documentation."""

    BEGIN = 0

    CURRENT = 1

    END = 2


class Stream(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.Stream = ...

    @property
    @abc.abstractmethod
    def can_read(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_write(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_seek(self) -> bool:
        ...

    @property
    def can_timeout(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def length(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def read_timeout(self) -> int:
        ...

    @read_timeout.setter
    def read_timeout(self, value: int) -> None:
        ...

    @property
    def write_timeout(self) -> int:
        ...

    @write_timeout.setter
    def write_timeout(self, value: int) -> None:
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def close(self) -> None:
        ...

    @overload
    def copy_to(self, destination: System.IO.Stream) -> None:
        ...

    @overload
    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def create_wait_handle(self) -> System.Threading.WaitHandle:
        warnings.warn("CreateWaitHandle has been deprecated. Use the ManualResetEvent(false) constructor instead.", DeprecationWarning)

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def object_invariant(self) -> None:
        warnings.warn("Do not call or override this method.", DeprecationWarning)

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_at_least(self, buffer: System.Span[int], minimum_bytes: int, throw_on_end_of_stream: bool = True) -> int:
        ...

    def read_at_least_async(self, buffer: System.Memory[int], minimum_bytes: int, throw_on_end_of_stream: bool = True, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    @overload
    def read_exactly(self, buffer: System.Span[int]) -> None:
        ...

    @overload
    def read_exactly(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def read_exactly_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    @overload
    def read_exactly_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    @staticmethod
    def synchronized(stream: System.IO.Stream) -> System.IO.Stream:
        ...

    @staticmethod
    def validate_buffer_arguments(buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @staticmethod
    def validate_copy_to_arguments(destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


class FileMode(IntEnum):
    """This class has no documentation."""

    CREATE_NEW = 1

    CREATE = 2

    OPEN = 3

    OPEN_OR_CREATE = 4

    TRUNCATE = 5

    APPEND = 6


class FileAccess(IntEnum):
    """This class has no documentation."""

    READ = 1

    WRITE = 2

    READ_WRITE = 3


class FileShare(IntEnum):
    """This class has no documentation."""

    NONE = 0

    READ = 1

    WRITE = 2

    READ_WRITE = 3

    DELETE = 4

    INHERITABLE = ...


class FileOptions(IntEnum):
    """This class has no documentation."""

    NONE = 0

    WRITE_THROUGH = ...

    ASYNCHRONOUS = ...

    RANDOM_ACCESS = ...

    DELETE_ON_CLOSE = ...

    SEQUENTIAL_SCAN = ...

    ENCRYPTED = ...


class UnixFileMode(IntEnum):
    """This class has no documentation."""

    NONE = 0

    OTHER_EXECUTE = 1

    OTHER_WRITE = 2

    OTHER_READ = 4

    GROUP_EXECUTE = 8

    GROUP_WRITE = 16

    GROUP_READ = 32

    USER_EXECUTE = 64

    USER_WRITE = 128

    USER_READ = 256

    STICKY_BIT = 512

    SET_GROUP = 1024

    SET_USER = 2048


class FileStreamOptions(System.Object):
    """This class has no documentation."""

    @property
    def mode(self) -> System.IO.FileMode:
        ...

    @mode.setter
    def mode(self, value: System.IO.FileMode) -> None:
        ...

    @property
    def access(self) -> System.IO.FileAccess:
        ...

    @access.setter
    def access(self, value: System.IO.FileAccess) -> None:
        ...

    @property
    def share(self) -> System.IO.FileShare:
        ...

    @share.setter
    def share(self, value: System.IO.FileShare) -> None:
        ...

    @property
    def options(self) -> System.IO.FileOptions:
        ...

    @options.setter
    def options(self, value: System.IO.FileOptions) -> None:
        ...

    @property
    def preallocation_size(self) -> int:
        ...

    @preallocation_size.setter
    def preallocation_size(self, value: int) -> None:
        ...

    @property
    def buffer_size(self) -> int:
        ...

    @buffer_size.setter
    def buffer_size(self, value: int) -> None:
        ...

    @property
    def unix_create_mode(self) -> typing.Optional[System.IO.UnixFileMode]:
        ...

    @unix_create_mode.setter
    def unix_create_mode(self, value: typing.Optional[System.IO.UnixFileMode]) -> None:
        ...


class StreamReader(System.IO.TextReader):
    """This class has no documentation."""

    NULL: System.IO.StreamReader = ...

    @property
    def current_encoding(self) -> System.Text.Encoding:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @property
    def end_of_stream(self) -> bool:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, detect_encoding_from_byte_order_marks: bool = True, buffer_size: int = -1, leave_open: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, options: System.IO.FileStreamOptions) -> None:
        ...

    def close(self) -> None:
        ...

    def discard_buffered_data(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def read_block(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        ...


class TextWriter(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.TextWriter = ...

    @property
    def core_new_line(self) -> typing.List[str]:
        ...

    @core_new_line.setter
    def core_new_line(self, value: typing.List[str]) -> None:
        ...

    @property
    def format_provider(self) -> System.IFormatProvider:
        ...

    @property
    @abc.abstractmethod
    def encoding(self) -> System.Text.Encoding:
        ...

    @property
    def new_line(self) -> str:
        ...

    @new_line.setter
    def new_line(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, format_provider: System.IFormatProvider) -> None:
        ...

    def close(self) -> None:
        ...

    @staticmethod
    def create_broadcasting(*writers: typing.Union[System.IO.TextWriter, typing.Iterable[System.IO.TextWriter]]) -> System.IO.TextWriter:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def synchronized(writer: System.IO.TextWriter) -> System.IO.TextWriter:
        ...

    @overload
    def write(self, value: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, value: System.Text.Rune) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.Rune) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: str, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, value: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write_line(self) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.Rune) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, value: bool) -> None:
        ...

    @overload
    def write_line(self, value: int) -> None:
        ...

    @overload
    def write_line(self, value: float) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.Rune) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: str, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...


class StreamWriter(System.IO.TextWriter):
    """This class has no documentation."""

    NULL: System.IO.StreamWriter = ...

    @property
    def auto_flush(self) -> bool:
        ...

    @auto_flush.setter
    def auto_flush(self, value: bool) -> None:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, buffer_size: int = -1, leave_open: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, options: System.IO.FileStreamOptions) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class FileStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        warnings.warn("FileStream.Handle has been deprecated. Use FileStream's SafeFileHandle property instead.", DeprecationWarning)

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def safe_file_handle(self) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def is_async(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, buffer_size: int, is_async: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int, use_async: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int, options: System.IO.FileOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool) -> None:
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool, buffer_size: int, is_async: bool) -> None:
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    @overload
    def flush(self) -> None:
        ...

    @overload
    def flush(self, flush_to_disk: bool) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def lock(self, position: int, length: int) -> None:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    def unlock(self, position: int, length: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


class FileAttributes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    READ_ONLY = ...

    HIDDEN = ...

    SYSTEM = ...

    DIRECTORY = ...

    ARCHIVE = ...

    DEVICE = ...

    NORMAL = ...

    TEMPORARY = ...

    SPARSE_FILE = ...

    REPARSE_POINT = ...

    COMPRESSED = ...

    OFFLINE = ...

    NOT_CONTENT_INDEXED = ...

    ENCRYPTED = ...

    INTEGRITY_STREAM = ...

    NO_SCRUB_DATA = ...


class FileSystemInfo(System.MarshalByRefObject, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def attributes(self) -> System.IO.FileAttributes:
        ...

    @attributes.setter
    def attributes(self, value: System.IO.FileAttributes) -> None:
        ...

    @property
    def full_path(self) -> str:
        ...

    @full_path.setter
    def full_path(self, value: str) -> None:
        ...

    @property
    def original_path(self) -> str:
        ...

    @original_path.setter
    def original_path(self, value: str) -> None:
        ...

    @property
    def full_name(self) -> str:
        ...

    @property
    def extension(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def exists(self) -> bool:
        ...

    @property
    def creation_time(self) -> datetime.datetime:
        ...

    @creation_time.setter
    def creation_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def creation_time_utc(self) -> datetime.datetime:
        ...

    @creation_time_utc.setter
    def creation_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_access_time(self) -> datetime.datetime:
        ...

    @last_access_time.setter
    def last_access_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_access_time_utc(self) -> datetime.datetime:
        ...

    @last_access_time_utc.setter
    def last_access_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_write_time(self) -> datetime.datetime:
        ...

    @last_write_time.setter
    def last_write_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_write_time_utc(self) -> datetime.datetime:
        ...

    @last_write_time_utc.setter
    def last_write_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def link_target(self) -> str:
        ...

    @property
    def unix_file_mode(self) -> System.IO.UnixFileMode:
        ...

    @unix_file_mode.setter
    def unix_file_mode(self, value: System.IO.UnixFileMode) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def create_as_symbolic_link(self, path_to_target: str) -> None:
        ...

    def delete(self) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def refresh(self) -> None:
        ...

    def resolve_link_target(self, return_final_target: bool) -> System.IO.FileSystemInfo:
        ...

    def to_string(self) -> str:
        ...


class File(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def append_all_bytes(path: str, bytes: typing.List[int]) -> None:
        ...

    @staticmethod
    @overload
    def append_all_bytes(path: str, bytes: System.ReadOnlySpan[int]) -> None:
        ...

    @staticmethod
    @overload
    def append_all_bytes_async(path: str, bytes: typing.List[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_bytes_async(path: str, bytes: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def append_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def append_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: System.ReadOnlySpan[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: System.ReadOnlyMemory[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def append_text(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    @overload
    def copy(source_file_name: str, dest_file_name: str) -> None:
        ...

    @staticmethod
    @overload
    def copy(source_file_name: str, dest_file_name: str, overwrite: bool) -> None:
        ...

    @staticmethod
    @overload
    def create(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def create(path: str, buffer_size: int) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def create(path: str, buffer_size: int, options: System.IO.FileOptions) -> System.IO.FileStream:
        ...

    @staticmethod
    def create_hard_link(path: str, path_to_target: str) -> System.IO.FileSystemInfo:
        ...

    @staticmethod
    def create_symbolic_link(path: str, path_to_target: str) -> System.IO.FileSystemInfo:
        ...

    @staticmethod
    def create_text(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    def decrypt(path: str) -> None:
        ...

    @staticmethod
    def delete(path: str) -> None:
        ...

    @staticmethod
    def encrypt(path: str) -> None:
        ...

    @staticmethod
    def exists(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def get_attributes(path: str) -> System.IO.FileAttributes:
        ...

    @staticmethod
    @overload
    def get_attributes(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> System.IO.FileAttributes:
        ...

    @staticmethod
    @overload
    def get_creation_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_creation_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_creation_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_creation_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_unix_file_mode(path: str) -> System.IO.UnixFileMode:
        ...

    @staticmethod
    @overload
    def get_unix_file_mode(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> System.IO.UnixFileMode:
        ...

    @staticmethod
    @overload
    def move(source_file_name: str, dest_file_name: str) -> None:
        ...

    @staticmethod
    @overload
    def move(source_file_name: str, dest_file_name: str, overwrite: bool) -> None:
        ...

    @staticmethod
    @overload
    def open(path: str, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    @staticmethod
    def open_handle(path: str, mode: System.IO.FileMode = ..., access: System.IO.FileAccess = ..., share: System.IO.FileShare = ..., options: System.IO.FileOptions = ..., preallocation_size: int = 0) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @staticmethod
    def open_read(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def open_text(path: str) -> System.IO.StreamReader:
        ...

    @staticmethod
    def open_write(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def read_all_bytes(path: str) -> typing.List[int]:
        ...

    @staticmethod
    def read_all_bytes_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[int]]:
        ...

    @staticmethod
    @overload
    def read_all_lines(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def read_all_lines(path: str, encoding: System.Text.Encoding) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def read_all_lines_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def read_all_lines_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def read_all_text(path: str) -> str:
        ...

    @staticmethod
    @overload
    def read_all_text(path: str, encoding: System.Text.Encoding) -> str:
        ...

    @staticmethod
    @overload
    def read_all_text_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def read_all_text_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def read_lines(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def read_lines(path: str, encoding: System.Text.Encoding) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def read_lines_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        ...

    @staticmethod
    @overload
    def read_lines_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        ...

    @staticmethod
    @overload
    def replace(source_file_name: str, destination_file_name: str, destination_backup_file_name: str) -> None:
        ...

    @staticmethod
    @overload
    def replace(source_file_name: str, destination_file_name: str, destination_backup_file_name: str, ignore_metadata_errors: bool) -> None:
        ...

    @staticmethod
    def resolve_link_target(link_path: str, return_final_target: bool) -> System.IO.FileSystemInfo:
        ...

    @staticmethod
    @overload
    def set_attributes(path: str, file_attributes: System.IO.FileAttributes) -> None:
        ...

    @staticmethod
    @overload
    def set_attributes(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, file_attributes: System.IO.FileAttributes) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time(path: str, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time_utc(path: str, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time(path: str, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time_utc(path: str, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time(path: str, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time_utc(path: str, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_unix_file_mode(path: str, mode: System.IO.UnixFileMode) -> None:
        ...

    @staticmethod
    @overload
    def set_unix_file_mode(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, mode: System.IO.UnixFileMode) -> None:
        ...

    @staticmethod
    @overload
    def write_all_bytes(path: str, bytes: typing.List[int]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_bytes(path: str, bytes: System.ReadOnlySpan[int]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_bytes_async(path: str, bytes: typing.List[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_bytes_async(path: str, bytes: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: typing.List[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: System.ReadOnlySpan[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: System.ReadOnlyMemory[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class IOException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, hresult: int) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class PathTooLongException(System.IO.IOException):
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


class Path(System.Object):
    """This class has no documentation."""

    DIRECTORY_SEPARATOR_CHAR: str = ...

    ALT_DIRECTORY_SEPARATOR_CHAR: str = ...

    VOLUME_SEPARATOR_CHAR: str = ...

    PATH_SEPARATOR: str = ...

    INVALID_PATH_CHARS: typing.List[str] = ...

    @staticmethod
    def change_extension(path: str, extension: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str, path_3: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str, path_3: str, path_4: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(*paths: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def ends_in_directory_separator(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def ends_in_directory_separator(path: str) -> bool:
        ...

    @staticmethod
    def exists(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def get_directory_name(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_directory_name(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def get_extension(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_extension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def get_file_name(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_file_name(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def get_file_name_without_extension(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_file_name_without_extension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def get_full_path(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_full_path(path: str, base_path: str) -> str:
        ...

    @staticmethod
    def get_invalid_file_name_chars() -> typing.List[str]:
        ...

    @staticmethod
    def get_invalid_path_chars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_path_root(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_path_root(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def get_random_file_name() -> str:
        ...

    @staticmethod
    def get_relative_path(relative_to: str, path: str) -> str:
        ...

    @staticmethod
    def get_temp_file_name() -> str:
        ...

    @staticmethod
    def get_temp_path() -> str:
        ...

    @staticmethod
    @overload
    def has_extension(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def has_extension(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_fully_qualified(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_fully_qualified(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_rooted(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_rooted(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str], path_4: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str, path_3: str) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str, path_3: str, path_4: str) -> str:
        ...

    @staticmethod
    @overload
    def join(*paths: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def trim_ending_directory_separator(path: str) -> str:
        ...

    @staticmethod
    @overload
    def trim_ending_directory_separator(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def try_join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class SearchOption(IntEnum):
    """This class has no documentation."""

    TOP_DIRECTORY_ONLY = 0

    ALL_DIRECTORIES = 1


class HandleInheritability(IntEnum):
    """This class has no documentation."""

    NONE = 0

    INHERITABLE = 1


class BufferedStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def underlying_stream(self) -> System.IO.Stream:
        ...

    @property
    def buffer_size(self) -> int:
        ...

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, buffer_size: int) -> None:
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], typing.Any], state: typing.Any) -> System.IAsyncResult:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    def flush(self) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


class BinaryReader(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self, input: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding, leave_open: bool) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def fill_buffer(self, num_bytes: int) -> None:
        ...

    def peek_char(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    def read_7_bit_encoded_int(self) -> int:
        ...

    def read_7_bit_encoded_int_64(self) -> int:
        ...

    def read_boolean(self) -> bool:
        ...

    def read_byte(self) -> int:
        ...

    def read_bytes(self, count: int) -> typing.List[int]:
        ...

    def read_char(self) -> str:
        ...

    def read_chars(self, count: int) -> typing.List[str]:
        ...

    def read_decimal(self) -> float:
        ...

    def read_double(self) -> float:
        ...

    def read_exactly(self, buffer: System.Span[int]) -> None:
        ...

    def read_half(self) -> System.Half:
        ...

    def read_int_16(self) -> int:
        ...

    def read_int_32(self) -> int:
        ...

    def read_int_64(self) -> int:
        ...

    def read_s_byte(self) -> int:
        ...

    def read_single(self) -> float:
        ...

    def read_string(self) -> str:
        ...

    def read_u_int_16(self) -> int:
        ...

    def read_u_int_32(self) -> int:
        ...

    def read_u_int_64(self) -> int:
        ...


class FileNotFoundException(System.IO.IOException):
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
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class MatchType(IntEnum):
    """This class has no documentation."""

    SIMPLE = 0

    WIN_32 = 1


class MatchCasing(IntEnum):
    """This class has no documentation."""

    PLATFORM_DEFAULT = 0

    CASE_SENSITIVE = 1

    CASE_INSENSITIVE = 2


class EnumerationOptions(System.Object):
    """This class has no documentation."""

    @property
    def recurse_subdirectories(self) -> bool:
        ...

    @recurse_subdirectories.setter
    def recurse_subdirectories(self, value: bool) -> None:
        ...

    @property
    def ignore_inaccessible(self) -> bool:
        ...

    @ignore_inaccessible.setter
    def ignore_inaccessible(self, value: bool) -> None:
        ...

    @property
    def buffer_size(self) -> int:
        ...

    @buffer_size.setter
    def buffer_size(self, value: int) -> None:
        ...

    @property
    def attributes_to_skip(self) -> System.IO.FileAttributes:
        ...

    @attributes_to_skip.setter
    def attributes_to_skip(self, value: System.IO.FileAttributes) -> None:
        ...

    @property
    def match_type(self) -> System.IO.MatchType:
        ...

    @match_type.setter
    def match_type(self, value: System.IO.MatchType) -> None:
        ...

    @property
    def match_casing(self) -> System.IO.MatchCasing:
        ...

    @match_casing.setter
    def match_casing(self, value: System.IO.MatchCasing) -> None:
        ...

    @property
    def max_recursion_depth(self) -> int:
        ...

    @max_recursion_depth.setter
    def max_recursion_depth(self, value: int) -> None:
        ...

    @property
    def return_special_directories(self) -> bool:
        ...

    @return_special_directories.setter
    def return_special_directories(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...


class DirectoryInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def parent(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def root(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def exists(self) -> bool:
        ...

    def __init__(self, path: str) -> None:
        ...

    def create(self) -> None:
        ...

    def create_subdirectory(self, path: str) -> System.IO.DirectoryInfo:
        ...

    @overload
    def delete(self) -> None:
        ...

    @overload
    def delete(self, recursive: bool) -> None:
        ...

    @overload
    def enumerate_directories(self) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_files(self) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_directories(self) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_files(self) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_file_system_infos(self) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.FileSystemInfo]:
        ...

    def move_to(self, dest_dir_name: str) -> None:
        ...


class FileInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def directory_name(self) -> str:
        ...

    @property
    def directory(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @is_read_only.setter
    def is_read_only(self, value: bool) -> None:
        ...

    @property
    def exists(self) -> bool:
        ...

    def __init__(self, file_name: str) -> None:
        ...

    def append_text(self) -> System.IO.StreamWriter:
        ...

    @overload
    def copy_to(self, dest_file_name: str) -> System.IO.FileInfo:
        ...

    @overload
    def copy_to(self, dest_file_name: str, overwrite: bool) -> System.IO.FileInfo:
        ...

    def create(self) -> System.IO.FileStream:
        ...

    def create_as_hard_link(self, path_to_target: str) -> None:
        ...

    def create_text(self) -> System.IO.StreamWriter:
        ...

    def decrypt(self) -> None:
        ...

    def delete(self) -> None:
        ...

    def encrypt(self) -> None:
        ...

    @overload
    def move_to(self, dest_file_name: str) -> None:
        ...

    @overload
    def move_to(self, dest_file_name: str, overwrite: bool) -> None:
        ...

    @overload
    def open(self, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        ...

    @overload
    def open(self, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @overload
    def open(self, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @overload
    def open(self, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    def open_read(self) -> System.IO.FileStream:
        ...

    def open_text(self) -> System.IO.StreamReader:
        ...

    def open_write(self) -> System.IO.FileStream:
        ...

    @overload
    def replace(self, destination_file_name: str, destination_backup_file_name: str) -> System.IO.FileInfo:
        ...

    @overload
    def replace(self, destination_file_name: str, destination_backup_file_name: str, ignore_metadata_errors: bool) -> System.IO.FileInfo:
        ...


class MemoryStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool, publicly_visible: bool) -> None:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def flush(self) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def get_buffer(self) -> typing.List[int]:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    def to_array(self) -> typing.List[int]:
        ...

    def try_get_buffer(self, buffer: typing.Optional[System.ArraySegment[int]]) -> typing.Tuple[bool, System.ArraySegment[int]]:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...

    def write_to(self, stream: System.IO.Stream) -> None:
        ...


class Directory(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def create_directory(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    @overload
    def create_directory(path: str, unix_create_mode: System.IO.UnixFileMode) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    def create_symbolic_link(path: str, path_to_target: str) -> System.IO.FileSystemInfo:
        ...

    @staticmethod
    def create_temp_subdirectory(prefix: str = None) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    @overload
    def delete(path: str) -> None:
        ...

    @staticmethod
    @overload
    def delete(path: str, recursive: bool) -> None:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    def exists(path: str) -> bool:
        ...

    @staticmethod
    def get_creation_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_creation_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_current_directory() -> str:
        ...

    @staticmethod
    @overload
    def get_directories(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def get_directory_root(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_files(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def get_last_access_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_access_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_write_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_write_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_logical_drives() -> typing.List[str]:
        ...

    @staticmethod
    def get_parent(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    def move(source_dir_name: str, dest_dir_name: str) -> None:
        ...

    @staticmethod
    def resolve_link_target(link_path: str, return_final_target: bool) -> System.IO.FileSystemInfo:
        ...

    @staticmethod
    def set_creation_time(path: str, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_creation_time_utc(path: str, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_current_directory(path: str) -> None:
        ...

    @staticmethod
    def set_last_access_time(path: str, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_access_time_utc(path: str, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_write_time(path: str, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_write_time_utc(path: str, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...


class RandomAccess(System.Object):
    """This class has no documentation."""

    @staticmethod
    def flush_to_disk(handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> None:
        ...

    @staticmethod
    def get_length(handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> int:
        ...

    @staticmethod
    @overload
    def read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Span[int], file_offset: int) -> int:
        ...

    @staticmethod
    @overload
    def read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], file_offset: int) -> int:
        ...

    @staticmethod
    @overload
    def read_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Memory[int], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @staticmethod
    @overload
    def read_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @staticmethod
    def set_length(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, length: int) -> None:
        ...

    @staticmethod
    @overload
    def write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlySpan[int], file_offset: int) -> None:
        ...

    @staticmethod
    @overload
    def write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], file_offset: int) -> None:
        ...

    @staticmethod
    @overload
    def write_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlyMemory[int], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    @staticmethod
    @overload
    def write_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...


class EndOfStreamException(System.IO.IOException):
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


class UnmanagedMemoryAccessor(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def capacity(self) -> int:
        ...

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def is_open(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    def read_boolean(self, position: int) -> bool:
        ...

    def read_byte(self, position: int) -> int:
        ...

    def read_char(self, position: int) -> str:
        ...

    def read_decimal(self, position: int) -> float:
        ...

    def read_double(self, position: int) -> float:
        ...

    def read_int_16(self, position: int) -> int:
        ...

    def read_int_32(self, position: int) -> int:
        ...

    def read_int_64(self, position: int) -> int:
        ...

    def read_s_byte(self, position: int) -> int:
        ...

    def read_single(self, position: int) -> float:
        ...

    def read_u_int_16(self, position: int) -> int:
        ...

    def read_u_int_32(self, position: int) -> int:
        ...

    def read_u_int_64(self, position: int) -> int:
        ...

    @overload
    def write(self, position: int, value: bool) -> None:
        ...

    @overload
    def write(self, position: int, value: int) -> None:
        ...

    @overload
    def write(self, position: int, value: str) -> None:
        ...

    @overload
    def write(self, position: int, value: float) -> None:
        ...


class StringWriter(System.IO.TextWriter):
    """This class has no documentation."""

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, format_provider: System.IFormatProvider) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder, format_provider: System.IFormatProvider) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    def get_string_builder(self) -> System.Text.StringBuilder:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class UnmanagedMemoryStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def position_pointer(self) -> typing.Any:
        ...

    @position_pointer.setter
    def position_pointer(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def flush(self) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def initialize(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


class DirectoryNotFoundException(System.IO.IOException):
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


class StringReader(System.IO.TextReader):
    """This class has no documentation."""

    def __init__(self, s: str) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        ...


class FileLoadException(System.IO.IOException):
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


class InvalidDataException(System.SystemException):
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


class BinaryWriter(System.Object, System.IDisposable, System.IAsyncDisposable):
    """This class has no documentation."""

    NULL: System.IO.BinaryWriter = ...

    @property
    def out_stream(self) -> System.IO.Stream:
        ...

    @out_stream.setter
    def out_stream(self, value: System.IO.Stream) -> None:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding, leave_open: bool) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def write(self, ch: str) -> None:
        ...

    @overload
    def write(self, chars: typing.List[str]) -> None:
        ...

    @overload
    def write(self, chars: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: System.Half) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write(self, chars: System.ReadOnlySpan[str]) -> None:
        ...

    def write_7_bit_encoded_int(self, value: int) -> None:
        ...

    def write_7_bit_encoded_int_64(self, value: int) -> None:
        ...


