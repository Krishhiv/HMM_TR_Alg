from typing import overload
from enum import IntEnum
import typing

import QuantConnect.Interfaces
import QuantConnect.Messaging
import QuantConnect.Notifications
import QuantConnect.Packets
import System

QuantConnect_Messaging__EventContainer_Callable = typing.TypeVar("QuantConnect_Messaging__EventContainer_Callable")
QuantConnect_Messaging__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Messaging__EventContainer_ReturnType")


class StreamingMessageHandler(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Message handler that sends messages over tcp using NetMQ."""

    @property
    def has_subscribers(self) -> bool:
        """
        Gets or sets whether this messaging handler has any current subscribers.
        This is not used in this message handler.  Messages are sent via tcp as they arrive
        """
        ...

    @has_subscribers.setter
    def has_subscribers(self, value: bool) -> None:
        ...

    def dispose(self) -> None:
        """Dispose any resources used before destruction"""
        ...

    def initialize(self, initialize_parameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the messaging system
        
        :param initialize_parameters: The parameters required for initialization
        """
        ...

    def send(self, packet: QuantConnect.Packets.Packet) -> None:
        """Send all types of packets"""
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """
        Send any notification with a base type of Notification.
        
        :param notification: The notification to be sent.
        """
        ...

    def set_authentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Set the user communication channel
        
        :param job: 
        """
        ...

    def transmit(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Send a message to the _server using ZeroMQ
        
        :param packet: Packet to transmit
        """
        ...


class Messaging(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Local/desktop implementation of messaging system for Lean Engine."""

    @property
    def has_subscribers(self) -> bool:
        """
        This implementation ignores the has_subscribers flag and
        instead will always write to the log.
        """
        ...

    @has_subscribers.setter
    def has_subscribers(self, value: bool) -> None:
        ...

    def dispose(self) -> None:
        """Dispose of any resources"""
        ...

    def initialize(self, initialize_parameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the messaging system
        
        :param initialize_parameters: The parameters required for initialization
        """
        ...

    def send(self, packet: QuantConnect.Packets.Packet) -> None:
        """Send a generic base packet without processing"""
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """Send any notification with a base type of Notification."""
        ...

    def set_authentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """Set the messaging channel"""
        ...


class EventMessagingHandler(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Desktop implementation of messaging system for Lean Engine"""

    @property
    def has_subscribers(self) -> bool:
        """
        Gets or sets whether this messaging handler has any current subscribers.
        When set to false, messages won't be sent.
        """
        ...

    @has_subscribers.setter
    def has_subscribers(self, value: bool) -> None:
        ...

    @property
    def debug_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.DebugPacket], typing.Any], typing.Any]:
        ...

    @debug_event.setter
    def debug_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.DebugPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def system_debug_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.SystemDebugPacket], typing.Any], typing.Any]:
        ...

    @system_debug_event.setter
    def system_debug_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.SystemDebugPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def log_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.LogPacket], typing.Any], typing.Any]:
        ...

    @log_event.setter
    def log_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.LogPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def runtime_error_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.RuntimeErrorPacket], typing.Any], typing.Any]:
        ...

    @runtime_error_event.setter
    def runtime_error_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.RuntimeErrorPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def handled_error_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.HandledErrorPacket], typing.Any], typing.Any]:
        ...

    @handled_error_event.setter
    def handled_error_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.HandledErrorPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def backtest_result_event(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.BacktestResultPacket], typing.Any], typing.Any]:
        ...

    @backtest_result_event.setter
    def backtest_result_event(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.BacktestResultPacket], typing.Any], typing.Any]) -> None:
        ...

    @property
    def consumer_ready_event(self) -> _EventContainer[typing.Callable[[], typing.Any], typing.Any]:
        ...

    @consumer_ready_event.setter
    def consumer_ready_event(self, value: _EventContainer[typing.Callable[[], typing.Any], typing.Any]) -> None:
        ...

    def backtest_result_event_raised(self, packet: QuantConnect.Packets.BacktestResultPacket) -> None:
        ...

    def consumer_ready_event_raised(self) -> None:
        ...

    def debug_event_raised(self, packet: QuantConnect.Packets.DebugPacket) -> None:
        ...

    def dispose(self) -> None:
        """Dispose of any resources"""
        ...

    def handled_error_event_raised(self, packet: QuantConnect.Packets.HandledErrorPacket) -> None:
        ...

    def initialize(self, initialize_parameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the Messaging System Plugin.
        
        :param initialize_parameters: The parameters required for initialization
        """
        ...

    def loading_complete(self) -> None:
        """Set Loaded to true"""
        ...

    def log_event_raised(self, packet: QuantConnect.Packets.LogPacket) -> None:
        ...

    def on_backtest_result_event(self, packet: QuantConnect.Packets.BacktestResultPacket) -> None:
        """
        Raise a backtest result event safely.
        
        
        This codeEntityType is protected.
        """
        ...

    def on_consumer_ready_event(self) -> None:
        """Handler for consumer ready code."""
        ...

    def on_debug_event(self, packet: QuantConnect.Packets.DebugPacket) -> None:
        """
        Raise a debug event safely
        
        
        This codeEntityType is protected.
        """
        ...

    def on_handled_error_event(self, packet: QuantConnect.Packets.HandledErrorPacket) -> None:
        """
        Raise a handled error event safely
        
        
        This codeEntityType is protected.
        """
        ...

    def on_log_event(self, packet: QuantConnect.Packets.LogPacket) -> None:
        """
        Raise a log event safely
        
        
        This codeEntityType is protected.
        """
        ...

    def on_runtime_error_event(self, packet: QuantConnect.Packets.RuntimeErrorPacket) -> None:
        """
        Raise runtime error safely
        
        
        This codeEntityType is protected.
        """
        ...

    def on_system_debug_event(self, packet: QuantConnect.Packets.SystemDebugPacket) -> None:
        """
        Raise a system debug event safely
        
        
        This codeEntityType is protected.
        """
        ...

    def runtime_error_event_raised(self, packet: QuantConnect.Packets.RuntimeErrorPacket) -> None:
        ...

    def send(self, packet: QuantConnect.Packets.Packet) -> None:
        """Send any message with a base type of Packet."""
        ...

    def send_enqueued_packets(self) -> None:
        """Send any message with a base type of Packet that has been enqueued."""
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """
        Send any notification with a base type of Notification.
        
        :param notification: The notification to be sent.
        """
        ...

    def set_authentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Set the user communication channel
        
        :param job: 
        """
        ...

    def system_debug_event_raised(self, packet: QuantConnect.Packets.SystemDebugPacket) -> None:
        ...


class _EventContainer(typing.Generic[QuantConnect_Messaging__EventContainer_Callable, QuantConnect_Messaging__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Messaging__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Messaging__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Messaging__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


