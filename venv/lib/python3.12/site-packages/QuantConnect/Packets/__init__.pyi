from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic


class BaseResultParameters(System.Object):
    """Base parameters used by LiveResultParameters and BacktestResultParameters"""

    @property
    def profit_loss(self) -> System.Collections.Generic.IDictionary[datetime.datetime, float]:
        """Trade profit and loss information since the last algorithm result packet"""
        ...

    @profit_loss.setter
    def profit_loss(self, value: System.Collections.Generic.IDictionary[datetime.datetime, float]) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @charts.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...

    @property
    def orders(self) -> System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]:
        """Order updates since the last result packet"""
        ...

    @orders.setter
    def orders(self, value: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]) -> None:
        ...

    @property
    def order_events(self) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """Order events updates since the last result packet"""
        ...

    @order_events.setter
    def order_events(self, value: typing.List[QuantConnect.Orders.OrderEvent]) -> None:
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Statistics information sent during the algorithm operations."""
        ...

    @statistics.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @runtime_statistics.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def state(self) -> System.Collections.Generic.IDictionary[str, str]:
        """State information of the algorithm."""
        ...

    @state.setter
    def state(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def algorithm_configuration(self) -> QuantConnect.AlgorithmConfiguration:
        """The algorithm's configuration required for report generation"""
        ...

    @algorithm_configuration.setter
    def algorithm_configuration(self, value: QuantConnect.AlgorithmConfiguration) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @total_performance.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profit_loss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtime_statistics: System.Collections.Generic.IDictionary[str, str], order_events: typing.List[QuantConnect.Orders.OrderEvent], total_performance: QuantConnect.Statistics.AlgorithmPerformance = None, algorithm_configuration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class BacktestResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for BacktestResult"""

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @rolling_window.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profit_loss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtime_statistics: System.Collections.Generic.IDictionary[str, str], rolling_window: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], order_events: typing.List[QuantConnect.Orders.OrderEvent], total_performance: QuantConnect.Statistics.AlgorithmPerformance = None, algorithm_configuration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class PacketType(IntEnum):
    """Classifications of internal packet system"""

    NONE = 0
    """Default, unset:"""

    ALGORITHM_NODE = 1
    """Base type for backtest and live work"""

    AUTOCOMPLETE_WORK = 2
    """Autocomplete Work Packet"""

    AUTOCOMPLETE_RESULT = 3
    """Result of the Autocomplete Job:"""

    BACKTEST_NODE = 4
    """Controller->Backtest Node Packet:"""

    BACKTEST_RESULT = 5
    """Packet out of backtest node:"""

    BACKTEST_WORK = 6
    """API-> Controller Work Packet:"""

    LIVE_NODE = 7
    """Controller -> Live Node Packet:"""

    LIVE_RESULT = 8
    """Live Node -> User Packet:"""

    LIVE_WORK = 9
    """API -> Controller Packet:"""

    SECURITY_TYPES = 10
    """Node -> User Algo Security Types"""

    BACKTEST_ERROR = 11
    """Controller -> User Error in Backtest Settings:"""

    ALGORITHM_STATUS = 12
    """Nodes -> User Algorithm Status Packet:"""

    BUILD_WORK = 13
    """API -> Compiler Work Packet:"""

    BUILD_SUCCESS = 14
    """Compiler -> User Build Success"""

    BUILD_ERROR = 15
    """Compiler -> User, Compile Error"""

    RUNTIME_ERROR = 16
    """Node -> User Algorithm Runtime Error"""

    HANDLED_ERROR = 17
    """Error is an internal handled error packet inside users algorithm"""

    LOG = 18
    """Nodes -> User Log Message"""

    DEBUG = 19
    """Nodes -> User Debug Message"""

    ORDER_EVENT = 20
    """Nodes -> User, Order Update Event"""

    SUCCESS = 21
    """Boolean true/false success"""

    HISTORY = 22
    """History live job packets"""

    COMMAND_RESULT = 23
    """Result from a command"""

    GIT_HUB_HOOK = 24
    """Hook from git hub"""

    DOCUMENTATION_RESULT = 25
    """Documentation result from docs server"""

    DOCUMENTATION = 26
    """Documentation request to the docs server"""

    SYSTEM_DEBUG = 27
    """Debug packet generated by Lean"""

    ALPHA_RESULT = 28
    """Packet containing insights generated by the algorithm"""

    ALPHA_WORK = 29
    """Alpha API -> Controller packet"""

    ALPHA_NODE = 30
    """Alpha Controller -> Alpha Node packet"""

    REGRESSION_ALGORITHM = 31
    """Packet containing list of algorithms to run as a regression test"""

    ALPHA_HEARTBEAT = 32
    """Packet containing a heartbeat"""

    DEBUGGING_STATUS = 33
    """Used when debugging to send status updates"""

    OPTIMIZATION_NODE = 34
    """Optimization Node Packet:"""

    OPTIMIZATION_ESTIMATE = 35
    """Optimization Estimate Packet:"""

    OPTIMIZATION_STATUS = 36
    """Optimization work status update"""

    OPTIMIZATION_RESULT = 37
    """Optimization work result"""

    AGGREGATED = 38
    """Aggregated packets"""

    LANGUAGE_MODEL_QUERY = 39
    """Query the language model"""

    LANGUAGE_MODEL_FEEDBACK = 40
    """Send feedback to a language model response"""

    LANGUAGE_MODEL_RESPONSE = 41
    """The language models response"""

    LANGUAGE_MODEL_CODE_ANALYSIS = 42
    """Language model code analysis"""

    LANGUAGE_MODEL_CHAT_WORK = 43
    """Language model chat work"""

    LANGUAGE_MODEL_CHAT_RESPONSE = 44
    """Language model chat response"""

    ALGORITHM_NAME_UPDATE = 45
    """Algorithm name update"""

    ALGORITHM_TAGS_UPDATE = 46
    """Algorithm tags update"""

    RESEARCH_NODE = 47
    """Research job packet"""

    ORGANIZATION_UPDATE = 48
    """Organization update"""

    BUILD_WARNING = 49
    """Compiler -> User Build Warnings"""

    LANGUAGE_MODEL_FUNCTION_CALL = 50
    """Language model function call related packet"""

    LANGUAGE_MODEL_AGENT_MESSAGE = 51
    """Language model agent message"""


class Packet(System.Object):
    """Base class for packet messaging system"""

    @property
    def type(self) -> QuantConnect.Packets.PacketType:
        """Packet type defined by a string enum"""
        ...

    @type.setter
    def type(self, value: QuantConnect.Packets.PacketType) -> None:
        ...

    @property
    def channel(self) -> str:
        """User unique specific channel endpoint to send the packets"""
        ...

    @channel.setter
    def channel(self, value: str) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Initialize the base class and setup the packet type.
        
        :param type: PacketType for the class.
        """
        ...


class PythonEnvironmentPacket(QuantConnect.Packets.Packet, metaclass=abc.ABCMeta):
    """
    Python Environment Packet is an abstract packet that contains a PythonVirtualEnvironment
    definition. Intended to be used by inheriting classes that may use a PythonVirtualEnvironment
    """

    @property
    def python_virtual_environment(self) -> str:
        """
        Virtual environment ID used to find PythonEvironments
        Ideally MD5, but environment names work as well.
        """
        ...

    @python_virtual_environment.setter
    def python_virtual_environment(self, value: str) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Default constructor for a PythonEnvironmentPacket
        
        
        This codeEntityType is protected.
        
        :param type: 
        """
        ...


class LeakyBucketControlParameters(System.Object):
    """
    Provides parameters that control the behavior of a leaky bucket rate limiting algorithm. The
    parameter names below are phrased in the positive, such that the bucket is filled up over time
    vs leaking out over time.
    """

    default_capacity: int

    default_time_interval: int
    """Default time interval"""

    default_refill_amount: int
    """Default refill amount"""

    @property
    def capacity(self) -> int:
        """
        Sets the total capacity of the bucket in a leaky bucket algorithm. This is the maximum
        number of 'units' the bucket can hold and also defines the maximum burst rate, assuming
        instantaneous usage of 'units'. In reality, the usage of 'units' takes times, and so it
        is possible for the bucket to incrementally refill while consuming from the bucket.
        """
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def refill_amount(self) -> int:
        """
        Sets the refill amount of the bucket. This defines the quantity of 'units' that become available
        to a consuming entity after the time interval has elapsed. For example, if the refill amount is
        equal to one, then each time interval one new 'unit' will be made available for a consumer that is
        throttled by the leaky bucket.
        """
        ...

    @refill_amount.setter
    def refill_amount(self, value: int) -> None:
        ...

    @property
    def time_interval_minutes(self) -> int:
        """
        Sets the time interval for the refill amount of the bucket, in minutes. After this amount of wall-clock
        time has passed, the bucket will refill the refill amount, thereby making more 'units' available
        for a consumer. For example, if the refill amount equals 10 and the time interval is 30 minutes, then
        every 30 minutes, 10 more 'units' become available for a consumer. The available 'units' will
        continue to increase until the bucket capacity is reached.
        """
        ...

    @time_interval_minutes.setter
    def time_interval_minutes(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LeakyBucketControlParameters using default values"""
        ...

    @overload
    def __init__(self, capacity: int, refill_amount: int, time_interval_minutes: int) -> None:
        """
        Initializes a new instance of the LeakyBucketControlParameters with the specified value
        
        :param capacity: The total capacity of the bucket in minutes
        :param refill_amount: The number of additional minutes to add to the bucket
        after time_interval_minutes has elapsed
        :param time_interval_minutes: The interval, in minutes, that must pass before the refill_amount
        is added back to the bucket for reuse
        """
        ...


class StoragePermissions(System.Object):
    """Holds the permissions for the object store"""

    @property
    def read(self) -> bool:
        """Whether the user has read permissions on the object store"""
        ...

    @read.setter
    def read(self, value: bool) -> None:
        ...

    @property
    def write(self) -> bool:
        """Whether the user has write permissions on the object store"""
        ...

    @write.setter
    def write(self, value: bool) -> None:
        ...

    @property
    def delete(self) -> bool:
        """Whether the user has delete permissions on the object store"""
        ...

    @delete.setter
    def delete(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the StoragePermissions struct with default permissions."""
        ...

    def to_string(self) -> str:
        """Returns a string representation of the storage permissions."""
        ...


class Controls(System.Object):
    """Specifies values used to control algorithm limits"""

    @property
    def maximum_runtime_minutes(self) -> int:
        """The maximum runtime in minutes"""
        ...

    @maximum_runtime_minutes.setter
    def maximum_runtime_minutes(self, value: int) -> None:
        ...

    @property
    def minute_limit(self) -> int:
        """The maximum number of minute symbols"""
        ...

    @minute_limit.setter
    def minute_limit(self, value: int) -> None:
        ...

    @property
    def second_limit(self) -> int:
        """The maximum number of second symbols"""
        ...

    @second_limit.setter
    def second_limit(self, value: int) -> None:
        ...

    @property
    def tick_limit(self) -> int:
        """The maximum number of tick symbol"""
        ...

    @tick_limit.setter
    def tick_limit(self, value: int) -> None:
        ...

    @property
    def ram_allocation(self) -> int:
        """Ram allocation for this algorithm in MB"""
        ...

    @ram_allocation.setter
    def ram_allocation(self, value: int) -> None:
        ...

    @property
    def cpu_allocation(self) -> float:
        """CPU allocation for this algorithm"""
        ...

    @cpu_allocation.setter
    def cpu_allocation(self, value: float) -> None:
        ...

    @property
    def live_log_limit(self) -> int:
        """The user live log limit"""
        ...

    @live_log_limit.setter
    def live_log_limit(self, value: int) -> None:
        ...

    @property
    def backtest_log_limit(self) -> int:
        """The user backtesting log limit"""
        ...

    @backtest_log_limit.setter
    def backtest_log_limit(self, value: int) -> None:
        ...

    @property
    def daily_log_limit(self) -> int:
        """The daily log limit of a user"""
        ...

    @daily_log_limit.setter
    def daily_log_limit(self, value: int) -> None:
        ...

    @property
    def remaining_log_allowance(self) -> int:
        """The remaining log allowance for a user"""
        ...

    @remaining_log_allowance.setter
    def remaining_log_allowance(self, value: int) -> None:
        ...

    @property
    def backtesting_max_insights(self) -> int:
        """Maximimum number of insights we'll store and score in a single backtest"""
        ...

    @backtesting_max_insights.setter
    def backtesting_max_insights(self, value: int) -> None:
        ...

    @property
    def backtesting_max_orders(self) -> int:
        """Maximimum number of orders we'll allow in a backtest."""
        ...

    @backtesting_max_orders.setter
    def backtesting_max_orders(self, value: int) -> None:
        ...

    @property
    def maximum_data_points_per_chart_series(self) -> int:
        """Limits the amount of data points per chart series. Applies only for backtesting"""
        ...

    @maximum_data_points_per_chart_series.setter
    def maximum_data_points_per_chart_series(self, value: int) -> None:
        ...

    @property
    def maximum_chart_series(self) -> int:
        """Limits the amount of chart series. Applies only for backtesting"""
        ...

    @maximum_chart_series.setter
    def maximum_chart_series(self, value: int) -> None:
        ...

    @property
    def second_time_out(self) -> int:
        """The amount seconds used for timeout limits"""
        ...

    @second_time_out.setter
    def second_time_out(self, value: int) -> None:
        ...

    @property
    def training_limits(self) -> QuantConnect.Packets.LeakyBucketControlParameters:
        """
        Sets parameters used for determining the behavior of the leaky bucket algorithm that
        controls how much time is available for an algorithm to use the training feature.
        """
        ...

    @training_limits.setter
    def training_limits(self, value: QuantConnect.Packets.LeakyBucketControlParameters) -> None:
        ...

    @property
    def storage_limit(self) -> int:
        """Limits the total size of storage used by IObjectStore"""
        ...

    @storage_limit.setter
    def storage_limit(self, value: int) -> None:
        ...

    @property
    def storage_file_count(self) -> int:
        """Limits the number of files to be held under the IObjectStore"""
        ...

    @storage_file_count.setter
    def storage_file_count(self, value: int) -> None:
        ...

    @property
    def storage_access(self) -> QuantConnect.Packets.StoragePermissions:
        """Holds the permissions for the object store"""
        ...

    @storage_access.setter
    def storage_access(self, value: QuantConnect.Packets.StoragePermissions) -> None:
        ...

    @property
    def persistence_interval_seconds(self) -> int:
        """
        The interval over which the IObjectStore will persistence the contents of
        the object store
        """
        ...

    @persistence_interval_seconds.setter
    def persistence_interval_seconds(self, value: int) -> None:
        ...

    @property
    def credit_cost(self) -> float:
        """The cost associated with running this job"""
        ...

    @credit_cost.setter
    def credit_cost(self, value: float) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the Controls class"""
        ...


class AlgorithmNodePacket(QuantConnect.Packets.PythonEnvironmentPacket):
    """Algorithm Node Packet is a work task for the Lean Engine"""

    @property
    def host_name(self) -> str:
        """The host name to use if any"""
        ...

    @host_name.setter
    def host_name(self, value: str) -> None:
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
    def organization_id(self) -> str:
        ...

    @organization_id.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the request"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Project name of the request"""
        ...

    @project_name.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id - BacktestId or DeployId - Common Id property between packets."""
        ...

    @property
    def session_id(self) -> str:
        """User session Id for authentication"""
        ...

    @session_id.setter
    def session_id(self, value: str) -> None:
        ...

    @property
    def language(self) -> QuantConnect.Language:
        """Language flag: Currently represents IL code or Dynamic Scripted Types."""
        ...

    @language.setter
    def language(self, value: QuantConnect.Language) -> None:
        ...

    @property
    def server_type(self) -> QuantConnect.ServerType:
        """Server type for the deployment (512, 1024, 2048)"""
        ...

    @server_type.setter
    def server_type(self, value: QuantConnect.ServerType) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Unique compile id of this backtest"""
        ...

    @compile_id.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def version(self) -> str:
        """Version number identifier for the lean engine."""
        ...

    @version.setter
    def version(self, value: str) -> None:
        ...

    @property
    def redelivered(self) -> bool:
        """
        An algorithm packet which has already been run and is being redelivered on this node.
        In this event we don't want to relaunch the task as it may result in unexpected behaviour for user.
        """
        ...

    @redelivered.setter
    def redelivered(self, value: bool) -> None:
        ...

    @property
    def algorithm(self) -> typing.List[int]:
        """Algorithm binary with zip of contents"""
        ...

    @algorithm.setter
    def algorithm(self, value: typing.List[int]) -> None:
        ...

    @property
    def request_source(self) -> str:
        """Request source - Web IDE or API - for controling result handler behaviour"""
        ...

    @request_source.setter
    def request_source(self, value: str) -> None:
        ...

    @property
    def ram_allocation(self) -> int:
        """The maximum amount of RAM (in MB) this algorithm is allowed to utilize"""
        ...

    @property
    def controls(self) -> QuantConnect.Packets.Controls:
        """Specifies values to control algorithm limits"""
        ...

    @controls.setter
    def controls(self, value: QuantConnect.Packets.Controls) -> None:
        ...

    @property
    def parameters(self) -> System.Collections.Generic.Dictionary[str, str]:
        """The parameter values used to set algorithm parameters"""
        ...

    @parameters.setter
    def parameters(self, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        ...

    @property
    def history_provider(self) -> str:
        """String name of the HistoryProvider we're running with"""
        ...

    @history_provider.setter
    def history_provider(self, value: str) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @property
    def deployment_target(self) -> QuantConnect.DeploymentTarget:
        """Deployment target, either local or cloud."""
        ...

    @deployment_target.setter
    def deployment_target(self, value: QuantConnect.DeploymentTarget) -> None:
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Default constructor for the algorithm node:
        
        :param type: 
        """
        ...

    def get_algorithm_name(self) -> str:
        """Gets a unique name for the algorithm defined by this packet"""
        ...


class BacktestNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Algorithm backtest task information packet."""

    @property
    def name(self) -> str:
        """Name of the backtest as randomly defined in the IDE."""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """BacktestId / Algorithm Id for this task"""
        ...

    @backtest_id.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """Optimization Id for this task"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def period_start(self) -> typing.Optional[datetime.datetime]:
        """Backtest start-date as defined in the Initialize() method."""
        ...

    @period_start.setter
    def period_start(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def period_finish(self) -> typing.Optional[datetime.datetime]:
        """Backtest end date as defined in the Initialize() method."""
        ...

    @period_finish.setter
    def period_finish(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """Backtest maximum end date"""
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

    @property
    def tradeable_dates(self) -> int:
        """Estimated number of trading days in this backtest task based on the start-end dates."""
        ...

    @tradeable_dates.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @property
    def debugging(self) -> bool:
        """True, if this is a debugging backtest"""
        ...

    @debugging.setter
    def debugging(self, value: bool) -> None:
        ...

    @property
    def cash_amount(self) -> typing.Optional[QuantConnect.Securities.CashAmount]:
        """Optional initial cash amount if set"""
        ...

    @cash_amount.setter
    def cash_amount(self, value: typing.Optional[QuantConnect.Securities.CashAmount]) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, user_id: int, project_id: int, session_id: str, algorithm_data: typing.List[int], starting_capital: float, name: str) -> None:
        """Initialize the backtest task packet."""
        ...

    @overload
    def __init__(self, user_id: int, project_id: int, session_id: str, algorithm_data: typing.List[int], name: str, starting_capital: typing.Optional[QuantConnect.Securities.CashAmount] = None) -> None:
        """Initialize the backtest task packet."""
        ...


class AlgorithmNameUpdatePacket(QuantConnect.Packets.Packet):
    """Packet to communicate updates to the algorithm's name"""

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """The new name"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, name: str) -> None:
        """Create a new instance of the algorithm tags up[date packet"""
        ...


class LiveNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Live job task packet: container for any live specific job variables"""

    @property
    def deploy_id(self) -> str:
        """Deploy Id for this live algorithm."""
        ...

    @deploy_id.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """String name of the brokerage we're trading with"""
        ...

    @brokerage.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def brokerage_data(self) -> System.Collections.Generic.Dictionary[str, str]:
        """String-String Dictionary of Brokerage Data for this Live Job"""
        ...

    @brokerage_data.setter
    def brokerage_data(self, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        ...

    @property
    def data_queue_handler(self) -> str:
        """String name of the DataQueueHandler or LiveDataProvider we're running with"""
        ...

    @data_queue_handler.setter
    def data_queue_handler(self, value: str) -> None:
        ...

    @property
    def data_channel_provider(self) -> str:
        """String name of the DataChannelProvider we're running with"""
        ...

    @data_channel_provider.setter
    def data_channel_provider(self, value: str) -> None:
        ...

    @property
    def disable_acknowledgement(self) -> bool:
        """Gets flag indicating whether or not the message should be acknowledged and removed from the queue"""
        ...

    @disable_acknowledgement.setter
    def disable_acknowledgement(self, value: bool) -> None:
        ...

    @property
    def notification_events(self) -> System.Collections.Generic.HashSet[str]:
        """A list of event types to generate notifications for, which will use notification_targets"""
        ...

    @notification_events.setter
    def notification_events(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def notification_targets(self) -> typing.List[QuantConnect.Notifications.Notification]:
        """A list of notification targets to use"""
        ...

    @notification_targets.setter
    def notification_targets(self, value: typing.List[QuantConnect.Notifications.Notification]) -> None:
        ...

    @property
    def live_data_types(self) -> System.Collections.Generic.HashSet[str]:
        """List of real time data types available in the live trading environment"""
        ...

    @live_data_types.setter
    def live_data_types(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @property
    def algorithm_mode(self) -> QuantConnect.AlgorithmMode:
        """Algorithm running mode."""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON of the Live Task Packet"""
        ...


class ResearchNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Represents a research node packet"""

    @property
    def research_id(self) -> str:
        """The research id"""
        ...

    @research_id.setter
    def research_id(self, value: str) -> None:
        ...

    @property
    def research_token(self) -> str:
        """Associated research token"""
        ...

    @research_token.setter
    def research_token(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance"""
        ...


class DebugPacket(QuantConnect.Packets.Packet):
    """Send a simple debug message from the users algorithm to the console."""

    @property
    def message(self) -> str:
        """String debug message to send to the users console"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Associated algorithm Id."""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Compile id of the algorithm sending this message"""
        ...

    @compile_id.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id for this message"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def toast(self) -> bool:
        """
        True to emit message as a popup notification (toast),
        false to emit message in console as text
        """
        ...

    @toast.setter
    def toast(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, packet_type: QuantConnect.Packets.PacketType) -> None:
        """
        Constructor for inherited types
        
        
        This codeEntityType is protected.
        
        :param packet_type: The type of packet to create
        """
        ...

    @overload
    def __init__(self, project_id: int, algorithm_id: str, compile_id: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the notify debug packet:"""
        ...


class AlphaNodePacket(QuantConnect.Packets.LiveNodePacket):
    """Alpha job packet"""

    @property
    def alpha_id(self) -> str:
        """Gets or sets the alpha id"""
        ...

    @alpha_id.setter
    def alpha_id(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the AlgorithmNodePacket class"""
        ...


class BacktestResult(QuantConnect.Result):
    """Backtest results object class - result specific items from the packet."""

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @rolling_window.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.BacktestResultParameters) -> None:
        """Constructor for the result class using dictionary objects."""
        ...


class BacktestResultPacket(QuantConnect.Packets.Packet):
    """Backtest result packet: send backtest information to GUI for user consumption."""

    @property
    def user_id(self) -> int:
        """User Id placing this task"""
        ...

    @user_id.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the this task."""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def session_id(self) -> str:
        """User Session Id"""
        ...

    @session_id.setter
    def session_id(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """BacktestId for this result packet"""
        ...

    @backtest_id.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def compile_id(self) -> str:
        """Compile Id for the algorithm which generated this result packet."""
        ...

    @compile_id.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def period_start(self) -> datetime.datetime:
        """Start of the backtest period as defined in Initialize() method."""
        ...

    @period_start.setter
    def period_start(self, value: datetime.datetime) -> None:
        ...

    @property
    def period_finish(self) -> datetime.datetime:
        """End of the backtest period as defined in the Initialize() method."""
        ...

    @period_finish.setter
    def period_finish(self, value: datetime.datetime) -> None:
        ...

    @property
    def date_requested(self) -> datetime.datetime:
        """DateTime (EST) the user requested this backtest."""
        ...

    @date_requested.setter
    def date_requested(self, value: datetime.datetime) -> None:
        ...

    @property
    def date_finished(self) -> datetime.datetime:
        """DateTime (EST) when the backtest was completed."""
        ...

    @date_finished.setter
    def date_finished(self, value: datetime.datetime) -> None:
        ...

    @property
    def progress(self) -> float:
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @progress.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of this backtest."""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.BacktestResult:
        """Result data object for this backtest"""
        ...

    @results.setter
    def results(self, value: QuantConnect.Packets.BacktestResult) -> None:
        ...

    @property
    def processing_time(self) -> float:
        """Processing time of the algorithm (from moment the algorithm arrived on the algorithm node)"""
        ...

    @processing_time.setter
    def processing_time(self, value: float) -> None:
        ...

    @property
    def tradeable_dates(self) -> int:
        """Estimated number of tradeable days in the backtest based on the start and end date or the backtest"""
        ...

    @tradeable_dates.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.BacktestNodePacket, results: QuantConnect.Packets.BacktestResult, end_date: typing.Union[datetime.datetime, datetime.date], start_date: typing.Union[datetime.datetime, datetime.date], progress: float = 1) -> None:
        """
        Compose result data packet - with tradable dates from the backtest job task and the partial result packet.
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        :param end_date: The algorithms backtest end date
        :param start_date: The algorithms backtest start date
        :param progress: Progress of the packet. For the packet we assume progess of 100%.
        """
        ...

    @staticmethod
    def create_empty(job: QuantConnect.Packets.BacktestNodePacket) -> QuantConnect.Packets.BacktestResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class LiveResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for LiveResult"""

    @property
    def holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @holdings.setter
    def holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash_book(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @cash_book.setter
    def cash_book(self, value: QuantConnect.Securities.CashBook) -> None:
        ...

    @property
    def server_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Server status information, including CPU/RAM usage, ect..."""
        ...

    @server_statistics.setter
    def server_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profit_loss: System.Collections.Generic.IDictionary[datetime.datetime, float], holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding], cash_book: QuantConnect.Securities.CashBook, statistics: System.Collections.Generic.IDictionary[str, str], runtime_statistics: System.Collections.Generic.IDictionary[str, str], order_events: typing.List[QuantConnect.Orders.OrderEvent], total_performance: QuantConnect.Statistics.AlgorithmPerformance = None, server_statistics: System.Collections.Generic.IDictionary[str, str] = None, algorithm_configuration: QuantConnect.AlgorithmConfiguration = None, state: System.Collections.Generic.IDictionary[str, str] = None) -> None:
        """Creates a new instance"""
        ...


class SystemDebugPacket(QuantConnect.Packets.DebugPacket):
    """Debug packets generated by Lean"""

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, project_id: int, algorithm_id: str, compile_id: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the system debug packet"""
        ...


class HistoryRequest(System.Object):
    """
    Specifies request parameters for a single historical request.
    A HistoryPacket is made of multiple requests for data. These
    are used to request data during live mode from a data server
    """

    @property
    def start_time_utc(self) -> datetime.datetime:
        """The start time to request data in UTC"""
        ...

    @start_time_utc.setter
    def start_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_time_utc(self) -> datetime.datetime:
        """The end time to request data in UTC"""
        ...

    @end_time_utc.setter
    def end_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """The symbol to request data for"""
        ...

    @symbol.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """The requested resolution"""
        ...

    @resolution.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """The type of data to retrieve"""
        ...

    @tick_type.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...


class HistoryPacket(QuantConnect.Packets.Packet):
    """Packet for history jobs"""

    @property
    def queue_name(self) -> str:
        """The queue where the data should be sent"""
        ...

    @queue_name.setter
    def queue_name(self, value: str) -> None:
        ...

    @property
    def requests(self) -> typing.List[QuantConnect.Packets.HistoryRequest]:
        """The individual requests to be processed"""
        ...

    @requests.setter
    def requests(self, value: typing.List[QuantConnect.Packets.HistoryRequest]) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the HistoryPacket class"""
        ...


class HistoryResultType(IntEnum):
    """Specifies various types of history results"""

    FILE = 0
    """The requested file data"""

    STATUS = 1
    """The request's status"""

    COMPLETED = 2
    """The request is completed"""

    ERROR = 3
    """The request had an error"""


class HistoryResult(System.Object, metaclass=abc.ABCMeta):
    """
    Provides a container for results from history requests. This contains
    the file path relative to the /Data folder where the data can be written
    """

    @property
    def type(self) -> QuantConnect.Packets.HistoryResultType:
        """Gets the type of history result"""
        ...

    def __init__(self, type: QuantConnect.Packets.HistoryResultType) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        
        This codeEntityType is protected.
        
        :param type: The type of history result
        """
        ...


class FileHistoryResult(QuantConnect.Packets.HistoryResult):
    """Defines requested file data for a history request"""

    @property
    def filepath(self) -> str:
        """The relative file path where the data should be written"""
        ...

    @filepath.setter
    def filepath(self, value: str) -> None:
        ...

    @property
    def file(self) -> typing.List[int]:
        """The file's contents, this is a zipped csv file"""
        ...

    @file.setter
    def file(self, value: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, filepath: str, file: typing.List[int]) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        :param filepath: The relative file path where the file should be written, rooted in /Data, so for example ./forex/fxcm/daily/eurusd.zip
        :param file: The zipped csv file content in bytes
        """
        ...


class CompletedHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the completed message from a history result"""

    def __init__(self) -> None:
        """Initializes a new instance of CompletedHistoryResult class"""
        ...


class ErrorHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specfies an error message in a history result"""

    @property
    def message(self) -> str:
        """Gets the error that was encountered"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the ErrorHistoryResult class
        
        :param message: The error message
        """
        ...


class StatusHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the progress of a request"""

    @property
    def progress(self) -> int:
        """Gets the progress of the request"""
        ...

    @progress.setter
    def progress(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, progress: int) -> None:
        """
        Initializes a new instance of the StatusHistoryResult class
        
        :param progress: The progress, from 0 to 100
        """
        ...


class AlgorithmStatusPacket(QuantConnect.Packets.Packet):
    """Algorithm status update information packet"""

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Current algorithm status"""
        ...

    @status.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def chart_subscription(self) -> str:
        """Chart we're subscribed to for live trading."""
        ...

    @chart_subscription.setter
    def chart_subscription(self, value: str) -> None:
        ...

    @property
    def message(self) -> str:
        """Optional message or reason for state change."""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id associated with this status packet"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id associated with this status packet"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def channel_status(self) -> str:
        """The current state of the channel"""
        ...

    @channel_status.setter
    def channel_status(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, project_id: int, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """Initialize algorithm state packet:"""
        ...


class RuntimeErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @stack_trace.setter
    def stack_trace(self, value: str) -> None:
        ...

    @property
    def user_id(self) -> int:
        """User Id associated with the backtest that threw the error"""
        ...

    @user_id.setter
    def user_id(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, user_id: int, algorithm_id: str, message: str, stacktrace: str = ...) -> None:
        """Create a new runtime error packet"""
        ...


class SecurityTypesPacket(QuantConnect.Packets.Packet):
    """Security types packet contains information on the markets the user data has requested."""

    @property
    def types(self) -> typing.List[QuantConnect.SecurityType]:
        """List of Security Type the user has requested (Equity, Forex, Futures etc)."""
        ...

    @types.setter
    def types(self, value: typing.List[QuantConnect.SecurityType]) -> None:
        ...

    @property
    def types_csv(self) -> str:
        """CSV formatted, lower case list of SecurityTypes for the web API."""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...


class AlphaResultPacket(QuantConnect.Packets.Packet):
    """Provides a packet type for transmitting alpha insights data"""

    @property
    def user_id(self) -> int:
        """The user's id that deployed the alpha stream"""
        ...

    @user_id.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def alpha_id(self) -> str:
        """
        The deployed alpha id. This is the id generated upon submssion to the alpha marketplace.
        If this is a user backtest or live algo then this will not be specified
        """
        ...

    @alpha_id.setter
    def alpha_id(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """The algorithm's unique identifier"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def insights(self) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """The generated insights"""
        ...

    @insights.setter
    def insights(self, value: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        ...

    @property
    def order_events(self) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """The generated OrderEvents"""
        ...

    @order_events.setter
    def order_events(self, value: typing.List[QuantConnect.Orders.OrderEvent]) -> None:
        ...

    @property
    def orders(self) -> typing.List[QuantConnect.Orders.Order]:
        """The new or updated Orders"""
        ...

    @orders.setter
    def orders(self, value: typing.List[QuantConnect.Orders.Order]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlphaResultPacket class"""
        ...

    @overload
    def __init__(self, algorithm_id: str, user_id: int, insights: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight] = None, order_events: typing.List[QuantConnect.Orders.OrderEvent] = None, orders: typing.List[QuantConnect.Orders.Order] = None) -> None:
        """
        Initializes a new instance of the AlphaResultPacket class
        
        :param algorithm_id: The algorithm's unique identifier
        :param user_id: The user's id
        :param insights: Alphas generated by the algorithm
        :param order_events: OrderEvents generated by the algorithm
        :param orders: Orders generated or updated by the algorithm
        """
        ...


class AlgorithmTagsUpdatePacket(QuantConnect.Packets.Packet):
    """Packet to communicate updates to the algorithm tags"""

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.HashSet[str]:
        """The new tags"""
        ...

    @tags.setter
    def tags(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, tags: System.Collections.Generic.HashSet[str]) -> None:
        """Create a new instance of the algorithm tags up[date packet"""
        ...


class LiveResult(QuantConnect.Result):
    """Live results object class for packaging live result data."""

    @property
    def holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @holdings.setter
    def holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash_book(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @cash_book.setter
    def cash_book(self, value: QuantConnect.Securities.CashBook) -> None:
        ...

    @property
    def cash(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Cash for the algorithm's live results."""
        ...

    @cash.setter
    def cash(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...

    @property
    def account_currency(self) -> str:
        """The algorithm's account currency"""
        ...

    @account_currency.setter
    def account_currency(self, value: str) -> None:
        ...

    @property
    def account_currency_symbol(self) -> str:
        """The algorithm's account currency"""
        ...

    @account_currency_symbol.setter
    def account_currency_symbol(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.LiveResultParameters) -> None:
        """Constructor for the result class for dictionary objects"""
        ...


class LiveResultPacket(QuantConnect.Packets.Packet):
    """Live result packet from a lean engine algorithm."""

    @property
    def user_id(self) -> int:
        """User Id sending result packet"""
        ...

    @user_id.setter
    def user_id(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id of the result packet"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Live Algorithm Id (DeployId) for this result packet"""
        ...

    @deploy_id.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.LiveResult:
        """Result data object for this result packet"""
        ...

    @results.setter
    def results(self, value: QuantConnect.Packets.LiveResult) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.LiveNodePacket, results: QuantConnect.Packets.LiveResult) -> None:
        """
        Compose Live Result Data Packet - With tradable dates
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        """
        ...

    @staticmethod
    def create_empty(job: QuantConnect.Packets.LiveNodePacket) -> QuantConnect.Packets.LiveResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class MarketHours(System.Object):
    """Market open hours model for pre, normal and post market hour definitions."""

    @property
    def start(self) -> datetime.datetime:
        """Start time for this market hour category"""
        ...

    @start.setter
    def start(self, value: datetime.datetime) -> None:
        ...

    @property
    def end(self) -> datetime.datetime:
        """End time for this market hour category"""
        ...

    @end.setter
    def end(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, reference_date: typing.Union[datetime.datetime, datetime.date], default_start: float, default_end: float) -> None:
        """
        Market hours initializer given an hours since midnight measure for the market hours today
        
        :param reference_date: Reference date used for as base date from the specified hour offsets
        :param default_start: Time in hours since midnight to start this open period.
        :param default_end: Time in hours since midnight to end this open period.
        """
        ...


class MarketToday(System.Object):
    """Market today information class"""

    @property
    def date(self) -> datetime.datetime:
        """Date this packet was generated."""
        ...

    @date.setter
    def date(self, value: datetime.datetime) -> None:
        ...

    @property
    def status(self) -> str:
        """Given the dates and times above, what is the current market status - open or closed."""
        ...

    @status.setter
    def status(self, value: str) -> None:
        ...

    @property
    def pre_market(self) -> QuantConnect.Packets.MarketHours:
        """Premarket hours for today"""
        ...

    @pre_market.setter
    def pre_market(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    @property
    def open(self) -> QuantConnect.Packets.MarketHours:
        """Normal trading market hours for today"""
        ...

    @open.setter
    def open(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    @property
    def post_market(self) -> QuantConnect.Packets.MarketHours:
        """Post market hours for today"""
        ...

    @post_market.setter
    def post_market(self, value: QuantConnect.Packets.MarketHours) -> None:
        ...

    def __init__(self) -> None:
        """Default constructor (required for JSON serialization)"""
        ...


class LogPacket(QuantConnect.Packets.Packet):
    """Simple log message instruction from the lean engine."""

    @property
    def message(self) -> str:
        """Log message to the users console:"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm Id requesting this logging"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, message: str) -> None:
        """Create a new instance of the notify Log packet:"""
        ...


class HandledErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @stack_trace.setter
    def stack_trace(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, message: str, stacktrace: str = ...) -> None:
        """Create a new handled error packet"""
        ...


class OrderEventPacket(QuantConnect.Packets.Packet):
    """Order event packet for passing updates on the state of an order to the portfolio."""

    @property
    def event(self) -> QuantConnect.Orders.OrderEvent:
        """Order event object"""
        ...

    @event.setter
    def event(self, value: QuantConnect.Orders.OrderEvent) -> None:
        ...

    @property
    def algorithm_id(self) -> str:
        """Algorithm id for this order event"""
        ...

    @algorithm_id.setter
    def algorithm_id(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithm_id: str, event_order: QuantConnect.Orders.OrderEvent) -> None:
        """Create a new instance of the order event packet"""
        ...


