from typing import overload
from enum import IntEnum
import datetime
import typing
import warnings

import System
import System.Runtime
import System.Runtime.ConstrainedExecution
import System.Threading


class GCLargeObjectHeapCompactionMode(IntEnum):
    """This class has no documentation."""

    DEFAULT = 1

    COMPACT_ONCE = 2


class GCLatencyMode(IntEnum):
    """This class has no documentation."""

    BATCH = 0

    INTERACTIVE = 1

    LOW_LATENCY = 2

    SUSTAINED_LOW_LATENCY = 3

    NO_GC_REGION = 4


class GCSettings(System.Object):
    """This class has no documentation."""

    latency_mode: System.Runtime.GCLatencyMode

    large_object_heap_compaction_mode: System.Runtime.GCLargeObjectHeapCompactionMode

    IS_SERVER_GC: bool


class JitInfo(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_compilation_time(current_thread: bool = False) -> datetime.timedelta:
        ...

    @staticmethod
    def get_compiled_il_bytes(current_thread: bool = False) -> int:
        ...

    @staticmethod
    def get_compiled_method_count(current_thread: bool = False) -> int:
        ...


class MemoryFailPoint(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable):
    """This class has no documentation."""

    def __init__(self, size_in_megabytes: int) -> None:
        ...

    def dispose(self) -> None:
        ...


class AssemblyTargetedPatchBandAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def targeted_patch_band(self) -> str:
        ...

    def __init__(self, targeted_patch_band: str) -> None:
        ...


class TargetedPatchingOptOutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def reason(self) -> str:
        ...

    def __init__(self, reason: str) -> None:
        ...


class ProfileOptimization(System.Object):
    """This class has no documentation."""

    @staticmethod
    def set_profile_root(directory_path: str) -> None:
        ...

    @staticmethod
    def start_profile(profile: str) -> None:
        ...


class AmbiguousImplementationException(System.Exception):
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


class ControlledExecution(System.Object):
    """This class has no documentation."""

    @staticmethod
    def run(action: typing.Callable[[], typing.Any], cancellation_token: System.Threading.CancellationToken) -> None:
        warnings.warn("Obsoletions.ControlledExecutionRunMessage", DeprecationWarning)


