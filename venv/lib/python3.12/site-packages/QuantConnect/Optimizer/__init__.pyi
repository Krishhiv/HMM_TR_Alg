from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Optimizer.Strategies
import QuantConnect.Packets
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_Optimizer__EventContainer_Callable = typing.TypeVar("QuantConnect_Optimizer__EventContainer_Callable")
QuantConnect_Optimizer__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Optimizer__EventContainer_ReturnType")


class OptimizationResult(System.Object):
    """Defines the result of Lean compute job"""

    INITIAL: QuantConnect.Optimizer.OptimizationResult = ...
    """Corresponds to initial result to drive the optimization strategy"""

    @property
    def backtest_id(self) -> str:
        """The backtest id that generated this result"""
        ...

    @property
    def id(self) -> int:
        """Parameter set Id"""
        ...

    @property
    def json_backtest_result(self) -> str:
        """Json Backtest result"""
        ...

    @property
    def parameter_set(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """The parameter set at which the result was achieved"""
        ...

    def __init__(self, json_backtest_result: str, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet, backtest_id: str) -> None:
        """
        Create an instance of OptimizationResult
        
        :param json_backtest_result: Optimization target value for this backtest
        :param parameter_set: Parameter set used in compute job
        :param backtest_id: The backtest id that generated this result
        """
        ...


class OptimizationStatus(IntEnum):
    """The different optimization status"""

    NEW = 0
    """Just created and not running optimization (0)"""

    ABORTED = 1
    """We failed or we were aborted (1)"""

    RUNNING = 2
    """We are running (2)"""

    COMPLETED = 3
    """Optimization job has completed (3)"""


class OptimizationNodePacket(QuantConnect.Packets.Packet):
    """Provide a packet type containing information on the optimization compute job."""

    @property
    def name(self) -> str:
        """The optimization name"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def created(self) -> datetime.datetime:
        """The creation time"""
        ...

    @created.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def user_id(self) -> int:
        """User Id placing request"""
        ...

    @user_id.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def user_token(self) -> str:
        ...

    @user_token.setter
    def user_token(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the request"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Unique compile id of this optimization"""
        ...

    @compile_id.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """The unique optimization Id of the request"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def organization_id(self) -> str:
        """Organization Id of the request"""
        ...

    @organization_id.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def maximum_concurrent_backtests(self) -> int:
        """Limit for the amount of concurrent backtests being run"""
        ...

    @maximum_concurrent_backtests.setter
    def maximum_concurrent_backtests(self, value: int) -> None:
        ...

    @property
    def optimization_strategy(self) -> str:
        """Optimization strategy name"""
        ...

    @optimization_strategy.setter
    def optimization_strategy(self, value: str) -> None:
        ...

    @property
    def criterion(self) -> QuantConnect.Optimizer.Objectives.Target:
        """Objective settings"""
        ...

    @criterion.setter
    def criterion(self, value: QuantConnect.Optimizer.Objectives.Target) -> None:
        ...

    @property
    def constraints(self) -> typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint]:
        """Optimization constraints"""
        ...

    @constraints.setter
    def constraints(self, value: typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint]) -> None:
        ...

    @property
    def optimization_parameters(self) -> System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """The user optimization parameters"""
        ...

    @optimization_parameters.setter
    def optimization_parameters(self, value: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> None:
        ...

    @property
    def optimization_strategy_settings(self) -> QuantConnect.Optimizer.Strategies.OptimizationStrategySettings:
        """The user optimization parameters"""
        ...

    @optimization_strategy_settings.setter
    def optimization_strategy_settings(self, value: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """Backtest out of sample maximum end date"""
        ...

    @out_of_sample_max_end_date.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """The backtest out of sample day count"""
        ...

    @out_of_sample_days.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    @overload
    def __init__(self, packet_type: QuantConnect.Packets.PacketType) -> None:
        """
        Creates a new instance
        
        
        This codeEntityType is protected.
        """
        ...


class LeanOptimizer(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """Base Lean optimizer class in charge of handling an optimization job packet"""

    @property
    def completed_backtests(self) -> int:
        """
        The total completed backtests count
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def status(self) -> QuantConnect.Optimizer.OptimizationStatus:
        """
        The current optimization status
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def optimization_target(self) -> QuantConnect.Optimizer.Objectives.Target:
        """
        The optimization target
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def running_parameter_set_for_backtest(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Collection holding ParameterSet for each backtest id we are waiting to finish
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def pending_parameter_set(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Collection holding ParameterSet for each backtest id we are waiting to launch
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def strategy(self) -> QuantConnect.Optimizer.Strategies.IOptimizationStrategy:
        """
        The optimization strategy being used
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def node_packet(self) -> QuantConnect.Optimizer.OptimizationNodePacket:
        """
        The optimization packet
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def disposed(self) -> bool:
        """
        Indicates whether optimizer was disposed
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def ended(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.OptimizationResult], typing.Any], typing.Any]:
        """Event triggered when the optimization work ended"""
        ...

    @ended.setter
    def ended(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.OptimizationResult], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, node_packet: QuantConnect.Optimizer.OptimizationNodePacket) -> None:
        """
        Creates a new instance
        
        
        This codeEntityType is protected.
        
        :param node_packet: The optimization node packet to handle
        """
        ...

    def abort_lean(self, backtest_id: str) -> None:
        """
        Handles stopping Lean process
        
        
        This codeEntityType is protected.
        
        :param backtest_id: Specified backtest id
        """
        ...

    def dispose(self) -> None:
        """Disposes of any resources"""
        ...

    def get_backtest_name(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet) -> str:
        """
        Get's a new backtest name
        
        
        This codeEntityType is protected.
        """
        ...

    def get_current_estimate(self) -> int:
        """Returns the current optimization status and strategy estimates"""
        ...

    def get_log_details(self) -> str:
        """
        Helper method to have pretty more informative logs
        
        
        This codeEntityType is protected.
        """
        ...

    def get_runtime_statistics(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Get the current runtime statistics"""
        ...

    def new_result(self, json_backtest_result: str, backtest_id: str) -> None:
        """
        Handles a new backtest json result matching a requested backtest id
        
        
        This codeEntityType is protected.
        
        :param json_backtest_result: The backtest json result
        :param backtest_id: The associated backtest id
        """
        ...

    def run_lean(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet, backtest_name: str) -> str:
        """
        Handles starting Lean for a given parameter set
        
        
        This codeEntityType is protected.
        
        :param parameter_set: The parameter set for the backtest to run
        :param backtest_name: The backtest name to use
        :returns: The new unique backtest id.
        """
        ...

    def send_update(self) -> None:
        """
        Sends an update of the current optimization status to the user
        
        
        This codeEntityType is protected.
        """
        ...

    def set_optimization_status(self, optimization_status: QuantConnect.Optimizer.OptimizationStatus) -> None:
        """
        Sets the current optimization status
        
        
        This codeEntityType is protected.
        
        :param optimization_status: The new optimization status
        """
        ...

    def start(self) -> None:
        """Starts the optimization"""
        ...

    def trigger_on_end_event(self) -> None:
        """
        Triggers the optimization job end event
        
        
        This codeEntityType is protected.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Optimizer__EventContainer_Callable, QuantConnect_Optimizer__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Optimizer__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Optimizer__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Optimizer__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


