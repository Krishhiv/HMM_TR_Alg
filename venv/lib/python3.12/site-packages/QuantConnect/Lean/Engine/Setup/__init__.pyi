from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.Setup
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets
import QuantConnect.Util
import System
import System.Collections.Generic


class SetupHandlerParameters(System.Object):
    """Defines the parameters for ISetupHandler"""

    @property
    def universe_selection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Gets the universe selection"""
        ...

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """Gets the algorithm"""
        ...

    @property
    def brokerage(self) -> QuantConnect.Interfaces.IBrokerage:
        """Gets the Brokerage"""
        ...

    @property
    def algorithm_node_packet(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """Gets the algorithm node packet"""
        ...

    @property
    def result_handler(self) -> QuantConnect.Lean.Engine.Results.IResultHandler:
        """Gets the algorithm node packet"""
        ...

    @property
    def transaction_handler(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """Gets the TransactionHandler"""
        ...

    @property
    def real_time_handler(self) -> QuantConnect.Lean.Engine.RealTime.IRealTimeHandler:
        """Gets the RealTimeHandler"""
        ...

    @property
    def data_cache_provider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """Gets the DataCacheProvider"""
        ...

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The map file provider instance of the algorithm"""
        ...

    def __init__(self, universe_selection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, algorithm: QuantConnect.Interfaces.IAlgorithm, brokerage: QuantConnect.Interfaces.IBrokerage, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, transaction_handler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, real_time_handler: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, map_file_provider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """
        Creates a new instance
        
        :param universe_selection: The universe selection instance
        :param algorithm: Algorithm instance
        :param brokerage: New brokerage output instance
        :param algorithm_node_packet: Algorithm job task
        :param result_handler: The configured result handler
        :param transaction_handler: The configured transaction handler
        :param real_time_handler: The configured real time handler
        :param data_cache_provider: The configured data cache provider
        :param map_file_provider: The map file provider
        """
        ...


class ISetupHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface to setup the algorithm. Pass in a raw algorithm, return one with portfolio, cash, etc already preset."""

    @property
    @abc.abstractmethod
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @worker_thread.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    @abc.abstractmethod
    def errors(self) -> typing.List[System.Exception]:
        """Any errors from the initialization stored here:"""
        ...

    @errors.setter
    def errors(self, value: typing.List[System.Exception]) -> None:
        ...

    @property
    @abc.abstractmethod
    def maximum_runtime(self) -> datetime.timedelta:
        """Get the maximum runtime for this algorithm job."""
        ...

    @property
    @abc.abstractmethod
    def starting_portfolio_value(self) -> float:
        """Algorithm starting capital for statistics calculations"""
        ...

    @property
    @abc.abstractmethod
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @property
    @abc.abstractmethod
    def max_orders(self) -> int:
        """Maximum number of orders for the algorithm run -- applicable for backtests only."""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param assembly_path: The path to the assembly's location
        :param algorithm_node_packet: Details of the task required
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Tuple[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates the brokerage as specified by the job packet
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...


class BacktestingSetupHandler(System.Object, QuantConnect.Lean.Engine.Setup.ISetupHandler):
    """Backtesting setup handler processes the algorithm initialize method and sets up the internal state of the algorithm class."""

    @property
    def initialization_time_out(self) -> datetime.timedelta:
        """
        Get the maximum time that the initialization of an algorithm can take
        
        
        This codeEntityType is protected.
        """
        ...

    @initialization_time_out.setter
    def initialization_time_out(self, value: datetime.timedelta) -> None:
        ...

    @property
    def algorithm_creation_timeout(self) -> datetime.timedelta:
        """
        Get the maximum time that the creation of an algorithm can take
        
        
        This codeEntityType is protected.
        """
        ...

    @algorithm_creation_timeout.setter
    def algorithm_creation_timeout(self, value: datetime.timedelta) -> None:
        ...

    @property
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @worker_thread.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    def errors(self) -> typing.List[System.Exception]:
        """Internal errors list from running the setup procedures."""
        ...

    @errors.setter
    def errors(self, value: typing.List[System.Exception]) -> None:
        ...

    @property
    def maximum_runtime(self) -> datetime.timedelta:
        """Maximum runtime of the algorithm in seconds."""
        ...

    @maximum_runtime.setter
    def maximum_runtime(self, value: datetime.timedelta) -> None:
        ...

    @property
    def starting_portfolio_value(self) -> float:
        """Starting capital according to the users initialize routine."""
        ...

    @starting_portfolio_value.setter
    def starting_portfolio_value(self, value: float) -> None:
        ...

    @property
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @starting_date.setter
    def starting_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def max_orders(self) -> int:
        """Maximum number of orders for this backtest."""
        ...

    @max_orders.setter
    def max_orders(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        """Initialize the backtest setup handler."""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param assembly_path: The path to the assembly's location
        :param algorithm_node_packet: Details of the task required
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Tuple[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates a new BacktestingBrokerage instance
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Setup the algorithm cash, dates and data subscriptions as desired.
        
        :param parameters: The parameters object to use
        :returns: Boolean true on successfully initializing the algorithm.
        """
        ...


class ConsoleSetupHandler(QuantConnect.Lean.Engine.Setup.BacktestingSetupHandler):
    """
    Kept for backwards compatibility-
    
    
    Should use BacktestingSetupHandler instead
    """


class BaseSetupHandler(System.Object):
    """
    Base class that provides shared code for
    the ISetupHandler implementations
    """

    INITIALIZATION_TIMEOUT: datetime.timedelta
    """Get the maximum time that the initialization of an algorithm can take"""

    ALGORITHM_CREATION_TIMEOUT: datetime.timedelta
    """Get the maximum time that the creation of an algorithm can take"""

    @staticmethod
    def get_configured_data_feeds() -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]:
        """Get the available data feeds from config.json,"""
        ...

    @staticmethod
    def initialize_debugging(algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, worker_thread: QuantConnect.Util.WorkerThread) -> bool:
        """
        Initialize the debugger
        
        :param algorithm_node_packet: The algorithm node packet
        :param worker_thread: The worker thread instance to use
        """
        ...

    @staticmethod
    def load_backtest_job_account_currency(algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.BacktestNodePacket) -> None:
        """Sets the account currency the algorithm should use if set in the job packet"""
        ...

    @staticmethod
    def load_backtest_job_cash_amount(algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.BacktestNodePacket) -> None:
        """Sets the initial cash for the algorithm if set in the job packet."""
        ...

    @staticmethod
    def set_brokerage_trading_day_per_year(algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Set the number of trading days per year based on the specified brokerage model.
        
        :param algorithm: The algorithm instance
        :returns: The number of trading days per year. For specific brokerages (Coinbase, Binance, Bitfinex, Bybit, FTX, Kraken),
        the value is 365. For other brokerages, the default value is 252.
        """
        ...

    @staticmethod
    def setup(parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...

    @staticmethod
    def setup_currency_conversions(algorithm: QuantConnect.Interfaces.IAlgorithm, universe_selection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, currencies_to_update_white_list: typing.Sequence[str] = None) -> None:
        """
        Will first check and add all the required conversion rate securities
        and later will seed an initial value to them.
        
        :param algorithm: The algorithm instance
        :param universe_selection: The universe selection instance
        :param currencies_to_update_white_list: If passed, the currencies in the CashBook that are contained in this list will be updated.
        By default, if not passed (null), all currencies in the cashbook without a properly set up currency conversion will be updated.
        This is not intended for actual algorithms but for tests or for this method to be used as a helper.
        """
        ...


class BrokerageSetupHandler(System.Object, QuantConnect.Lean.Engine.Setup.ISetupHandler):
    """Defines a set up handler that initializes the algorithm instance using values retrieved from the user's brokerage account"""

    max_allocation_limit_config: str = "max-allocation-limit"
    """Max allocation limit configuration variable name"""

    @property
    def worker_thread(self) -> QuantConnect.Util.WorkerThread:
        """The worker thread instance the setup handler should use"""
        ...

    @worker_thread.setter
    def worker_thread(self, value: QuantConnect.Util.WorkerThread) -> None:
        ...

    @property
    def errors(self) -> typing.List[System.Exception]:
        """Any errors from the initialization stored here:"""
        ...

    @errors.setter
    def errors(self, value: typing.List[System.Exception]) -> None:
        ...

    @property
    def maximum_runtime(self) -> datetime.timedelta:
        """Get the maximum runtime for this algorithm job."""
        ...

    @property
    def starting_portfolio_value(self) -> float:
        """Algorithm starting capital for statistics calculations"""
        ...

    @property
    def starting_date(self) -> datetime.datetime:
        """Start date for analysis loops to search for data."""
        ...

    @property
    def max_orders(self) -> int:
        """Maximum number of orders for the algorithm run -- applicable for backtests only."""
        ...

    def __init__(self) -> None:
        """Initializes a new BrokerageSetupHandler"""
        ...

    def create_algorithm_instance(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, assembly_path: str) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Create a new instance of an algorithm from a physical dll path.
        
        :param assembly_path: The path to the assembly's location
        :param algorithm_node_packet: Details of the task required
        :returns: A new instance of IAlgorithm, or throws an exception if there was an error.
        """
        ...

    def create_brokerage(self, algorithm_node_packet: QuantConnect.Packets.AlgorithmNodePacket, uninitialized_algorithm: QuantConnect.Interfaces.IAlgorithm, factory: typing.Optional[QuantConnect.Interfaces.IBrokerageFactory]) -> typing.Tuple[QuantConnect.Interfaces.IBrokerage, QuantConnect.Interfaces.IBrokerageFactory]:
        """
        Creates the brokerage as specified by the job packet
        
        :param algorithm_node_packet: Job packet
        :param uninitialized_algorithm: The algorithm instance before Initialize has been called
        :param factory: The brokerage factory
        :returns: The brokerage instance, or throws if error creating instance.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def get_open_orders(self, algorithm: QuantConnect.Interfaces.IAlgorithm, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, transaction_handler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, brokerage: QuantConnect.Interfaces.IBrokerage) -> None:
        """
        Get the open orders from a brokerage. Adds Orders.Order and Orders.OrderTicket to the transaction handler
        
        
        This codeEntityType is protected.
        
        :param algorithm: Algorithm instance
        :param result_handler: The configured result handler
        :param transaction_handler: The configurated transaction handler
        :param brokerage: Brokerage output instance
        """
        ...

    def load_existing_holdings_and_orders(self, brokerage: QuantConnect.Interfaces.IBrokerage, algorithm: QuantConnect.Interfaces.IAlgorithm, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Loads existing holdings and orders
        
        
        This codeEntityType is protected.
        """
        ...

    def setup(self, parameters: QuantConnect.Lean.Engine.Setup.SetupHandlerParameters) -> bool:
        """
        Primary entry point to setup a new algorithm
        
        :param parameters: The parameters object to use
        :returns: True on successfully setting up the algorithm state, or false on error.
        """
        ...


class AlgorithmSetupException(System.Exception):
    """Defines an exception generated in the course of invoking IsetupHandler.setup"""

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the AlgorithmSetupException class
        
        :param message: The error message
        """
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        """
        Initializes a new instance of the AlgorithmSetupException class
        
        :param message: The error message
        :param inner: The inner exception being wrapped
        """
        ...


