from typing import overload
from enum import IntEnum
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ObjectiveC


class ObjectiveCTrackedTypeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class ObjectiveCMarshal(System.Object):
    """This class has no documentation."""

    class MessageSendFunction(IntEnum):
        """This class has no documentation."""

        MSG_SEND = 0

        MSG_SEND_FPRET = 1

        MSG_SEND_STRET = 2

        MSG_SEND_SUPER = 3

        MSG_SEND_SUPER_STRET = 4

        MSG_SEND = 5

        MSG_SEND_FPRET = 6

        MSG_SEND_STRET = 7

        MSG_SEND_SUPER = 8

        MSG_SEND_SUPER_STRET = 9

    @staticmethod
    def create_reference_tracking_handle(obj: typing.Any, tagged_memory: typing.Optional[System.Span[System.IntPtr]]) -> typing.Tuple[System.Runtime.InteropServices.GCHandle, System.Span[System.IntPtr]]:
        ...

    @staticmethod
    def initialize(begin_end_callback: typing.Any, is_referenced_callback: typing.Any, tracked_object_entered_finalization: typing.Any, unhandled_exception_propagation_handler: typing.Any) -> None:
        ...

    @staticmethod
    def set_message_send_callback(msg_send_function: typing.Any, func: System.IntPtr) -> None:
        ...

    @staticmethod
    def set_message_send_pending_exception(exception: System.Exception) -> None:
        ...

    def unhandled_exception_propagation_handler(self, exception: System.Exception, last_method: System.RuntimeMethodHandle, context: typing.Optional[System.IntPtr]) -> typing.Tuple[typing.Any, System.IntPtr]:
        ...


