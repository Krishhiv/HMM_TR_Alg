from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.DataSource
import QuantConnect.Interfaces
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import System
import System.Collections.Concurrent
import System.Collections.Generic
import System.Collections.Specialized

QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T = typing.TypeVar("QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T")
QuantConnect_Data_UniverseSelection_FuncUniverse_T = typing.TypeVar("QuantConnect_Data_UniverseSelection_FuncUniverse_T")
QuantConnect_Data_UniverseSelection__EventContainer_Callable = typing.TypeVar("QuantConnect_Data_UniverseSelection__EventContainer_Callable")
QuantConnect_Data_UniverseSelection__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data_UniverseSelection__EventContainer_ReturnType")


class Schedule(System.Object):
    """Entity in charge of managing a schedule"""

    @property
    def initialized(self) -> bool:
        """True if this schedule is set"""
        ...

    def clone(self) -> QuantConnect.Data.UniverseSelection.Schedule:
        """Creates a new instance holding the same schedule if any"""
        ...

    def get(self, start_time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[datetime.datetime]:
        """Gets the current schedule for a given start time"""
        ...

    def on(self, date_rule: QuantConnect.Scheduling.IDateRule) -> None:
        """Set a IDateRule for this schedule"""
        ...


class UniverseSettings(System.Object):
    """Defines settings required when adding a subscription"""

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """The resolution to be used"""
        ...

    @resolution.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def leverage(self) -> float:
        """The leverage to be used"""
        ...

    @leverage.setter
    def leverage(self, value: float) -> None:
        ...

    @property
    def fill_forward(self) -> bool:
        """True to fill data forward, false otherwise"""
        ...

    @fill_forward.setter
    def fill_forward(self, value: bool) -> None:
        ...

    @property
    def schedule(self) -> QuantConnect.Data.UniverseSelection.Schedule:
        """
        If configured, will be used to determine universe selection schedule and filter or skip selection data
        that does not fit the schedule
        """
        ...

    @schedule.setter
    def schedule(self, value: QuantConnect.Data.UniverseSelection.Schedule) -> None:
        ...

    @property
    def extended_market_hours(self) -> bool:
        """True to allow extended market hours data, false otherwise"""
        ...

    @extended_market_hours.setter
    def extended_market_hours(self, value: bool) -> None:
        ...

    @property
    def minimum_time_in_universe(self) -> datetime.timedelta:
        """
        Defines the minimum amount of time a security must be in
        the universe before being removed.
        """
        ...

    @minimum_time_in_universe.setter
    def minimum_time_in_universe(self, value: datetime.timedelta) -> None:
        ...

    @property
    def data_normalization_mode(self) -> QuantConnect.DataNormalizationMode:
        """Defines how universe data is normalized before being send into the algorithm"""
        ...

    @data_normalization_mode.setter
    def data_normalization_mode(self, value: QuantConnect.DataNormalizationMode) -> None:
        ...

    @property
    def data_mapping_mode(self) -> QuantConnect.DataMappingMode:
        """Defines how universe data is mapped together"""
        ...

    @data_mapping_mode.setter
    def data_mapping_mode(self, value: QuantConnect.DataMappingMode) -> None:
        ...

    @property
    def contract_depth_offset(self) -> int:
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contra
        """
        ...

    @contract_depth_offset.setter
    def contract_depth_offset(self, value: int) -> None:
        ...

    @property
    def subscription_data_types(self) -> typing.List[System.Tuple[typing.Type, QuantConnect.TickType]]:
        """Allows a universe to specify which data types to add for a selected symbol"""
        ...

    @subscription_data_types.setter
    def subscription_data_types(self, value: typing.List[System.Tuple[typing.Type, QuantConnect.TickType]]) -> None:
        ...

    @property
    def asynchronous(self) -> typing.Optional[bool]:
        """True if universe selection can run asynchronous"""
        ...

    @asynchronous.setter
    def asynchronous(self, value: typing.Optional[bool]) -> None:
        ...

    @overload
    def __init__(self, resolution: QuantConnect.Resolution, leverage: float, fill_forward: bool, extended_market_hours: bool, minimum_time_in_universe: datetime.timedelta, data_normalization_mode: QuantConnect.DataNormalizationMode = ..., data_mapping_mode: QuantConnect.DataMappingMode = ..., contract_depth_offset: int = 0, asynchronous: typing.Optional[bool] = None, selection_date_rule: QuantConnect.Scheduling.IDateRule = None) -> None:
        """
        Initializes a new instance of the UniverseSettings class
        
        :param resolution: The resolution
        :param leverage: The leverage to be used
        :param fill_forward: True to fill data forward, false otherwise
        :param extended_market_hours: True to allow extended market hours data, false otherwise
        :param minimum_time_in_universe: Defines the minimum amount of time a security must remain in the universe before being removed
        :param data_normalization_mode: Defines how universe data is normalized before being send into the algorithm
        :param data_mapping_mode: The contract mapping mode to use for the security
        :param contract_depth_offset: The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        :param asynchronous: True if universe selection can run asynchronous
        :param selection_date_rule: If provided, will be used to determine universe selection schedule
        """
        ...

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """Initializes a new instance of the UniverseSettings class"""
        ...


class BaseDataCollection(QuantConnect.Data.BaseData, typing.Iterable[QuantConnect.Data.BaseData]):
    """This type exists for transport of data as a single packet"""

    @property
    def underlying(self) -> QuantConnect.Data.BaseData:
        """The associated underlying price data if any"""
        ...

    @underlying.setter
    def underlying(self, value: QuantConnect.Data.BaseData) -> None:
        ...

    @property
    def filtered_contracts(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """Gets or sets the contracts selected by the universe"""
        ...

    @filtered_contracts.setter
    def filtered_contracts(self, value: System.Collections.Generic.HashSet[QuantConnect.Symbol]) -> None:
        ...

    @property
    def data(self) -> typing.List[QuantConnect.Data.BaseData]:
        """Gets the data list"""
        ...

    @data.setter
    def data(self, value: typing.List[QuantConnect.Data.BaseData]) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Gets or sets the end time of this data"""
        ...

    @end_time.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the BaseDataCollection c;ass"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], data: typing.List[QuantConnect.Data.BaseData] = None) -> None:
        """
        Initializes a new instance of the BaseDataCollection class
        
        :param time: The time of this data
        :param symbol: A common identifier for all data in this packet
        :param data: The data to add to this collection
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], data: typing.List[QuantConnect.Data.BaseData] = None, underlying: QuantConnect.Data.BaseData = None, filtered_contracts: System.Collections.Generic.HashSet[QuantConnect.Symbol] = None) -> None:
        """
        Initializes a new instance of the BaseDataCollection class
        
        :param time: The start time of this data
        :param end_time: The end time of this data
        :param symbol: A common identifier for all data in this packet
        :param data: The data to add to this collection
        :param underlying: The associated underlying price data if any
        :param filtered_contracts: The contracts selected by the universe
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], data: typing.List[QuantConnect.Data.BaseData], underlying: QuantConnect.Data.BaseData, filtered_contracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the BaseDataCollection class
        
        :param time: The start time of this data
        :param end_time: The end time of this data
        :param symbol: A common identifier for all data in this packet
        :param data: The data to add to this collection
        :param underlying: The associated underlying price data if any
        :param filtered_contracts: The contracts selected by the universe
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], underlying: QuantConnect.Data.BaseData, filtered_contracts: System.Collections.Generic.HashSet[QuantConnect.Symbol]) -> None:
        """
        Helper method to create an instance without setting the data list
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, other: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> None:
        """
        Copy constructor for BaseDataCollection
        
        :param other: The base data collection being copied
        """
        ...

    def __iter__(self) -> typing.Iterator[QuantConnect.Data.BaseData]:
        ...

    def add(self, new_data_point: QuantConnect.Data.BaseData) -> None:
        """
        Adds a new data point to this collection
        
        :param new_data_point: The new data point to add
        """
        ...

    def add_range(self, new_data_points: typing.List[QuantConnect.Data.BaseData]) -> None:
        """
        Adds a new data points to this collection
        
        :param new_data_points: The new data points to add
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Returns an IEnumerator for this enumerable Object.  The enumerator provides
        a simple way to access all the contents of a collection.
        """
        ...

    def should_cache_to_security(self) -> bool:
        """
        Indicates whether this contains data that should be stored in the security cache
        
        :returns: Whether this contains data that should be stored in the security cache.
        """
        ...

    def universe_symbol(self, market: str = None) -> QuantConnect.Symbol:
        """
        Creates the universe symbol for the target market
        
        :returns: The universe symbol to use.
        """
        ...


class SubscriptionRequest(QuantConnect.Data.BaseDataRequest):
    """Defines the parameters required to add a subscription to a data feed."""

    @property
    def is_universe_subscription(self) -> bool:
        """Gets true if the subscription is a universe"""
        ...

    @property
    def universe(self) -> QuantConnect.Data.UniverseSelection.Universe:
        """Gets the universe this subscription resides in"""
        ...

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security. This is the destination of data for non-internal subscriptions."""
        ...

    @property
    def configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """Gets the subscription configuration. This defines how/where to read the data."""
        ...

    @property
    def tradable_days_in_data_time_zone(self) -> typing.Iterable[datetime.datetime]:
        """Gets the tradable days specified by this request, in the security's data time zone"""
        ...

    @overload
    def __init__(self, is_universe_subscription: bool, universe: QuantConnect.Data.UniverseSelection.Universe, security: QuantConnect.Securities.Security, configuration: QuantConnect.Data.SubscriptionDataConfig, start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Initializes a new instance of the SubscriptionRequest class"""
        ...

    @overload
    def __init__(self, template: QuantConnect.Data.UniverseSelection.SubscriptionRequest, is_universe_subscription: typing.Optional[bool] = None, universe: QuantConnect.Data.UniverseSelection.Universe = None, security: QuantConnect.Securities.Security = None, configuration: QuantConnect.Data.SubscriptionDataConfig = None, start_time_utc: typing.Optional[datetime.datetime] = None, end_time_utc: typing.Optional[datetime.datetime] = None) -> None:
        """Initializes a new instance of the SubscriptionRequest class"""
        ...


class Universe(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """Provides a base class for all universes to derive from."""

    class UnchangedUniverse(System.Object, typing.Iterable[str]):
        """
        Provides a value to indicate that no changes should be made to the universe.
        This value is intended to be returned by reference via Universe.select_symbols
        """

        INSTANCE: QuantConnect.Data.UniverseSelection.Universe.UnchangedUniverse = ...
        """Read-only instance of the UnchangedUniverse value"""

        def __iter__(self) -> typing.Iterator[QuantConnect.Symbol]:
            ...

    class Member(System.Object):
        """Member of the Universe"""

        @property
        def added(self) -> datetime.datetime:
            """DateTime when added"""
            ...

        @property
        def security(self) -> QuantConnect.Securities.Security:
            """The security that was added"""
            ...

        @property
        def is_internal(self) -> bool:
            """True if the security was added as internal by this universe"""
            ...

        def __init__(self, added: typing.Union[datetime.datetime, datetime.date], security: QuantConnect.Securities.Security, is_internal: bool) -> None:
            """
            Initialize a new member for the universe
            
            :param added: DateTime added
            :param security: Security to add
            :param is_internal: True if internal member
            """
            ...

    class SelectionEventArgs(System.EventArgs):
        """Event fired when the universe selection changes"""

        @property
        def current_selection(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
            """The current universe selection"""
            ...

        def __init__(self, current_selection: System.Collections.Generic.HashSet[QuantConnect.Symbol]) -> None:
            """Creates a new instance"""
            ...

    UNCHANGED: QuantConnect.Data.UniverseSelection.Universe.UnchangedUniverse = ...
    """Gets a value indicating that no change to the universe should be made"""

    @property
    def securities(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe.Member]:
        """Gets the internal security collection used to define membership in this universe"""
        ...

    @property
    def selected(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """The currently selected symbol set"""
        ...

    @selected.setter
    def selected(self, value: System.Collections.Generic.HashSet[QuantConnect.Symbol]) -> None:
        ...

    @property
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @asynchronous.setter
    def asynchronous(self, value: bool) -> None:
        ...

    @property
    def selection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        """Event fired when the universe selection has changed"""
        ...

    @selection_changed.setter
    def selection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the security type of this universe"""
        ...

    @property
    def market(self) -> str:
        """Gets the market of this universe"""
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol of this universe"""
        ...

    @property
    def data_type(self) -> typing.Type:
        """Gets the data type of this universe"""
        ...

    @property
    def dispose_requested(self) -> bool:
        """Flag indicating if disposal of this universe has been requested"""
        ...

    @dispose_requested.setter
    def dispose_requested(self, value: bool) -> None:
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the settings used for subscriptions added for this universe"""
        ...

    @universe_settings.setter
    def universe_settings(self, value: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        ...

    @property
    def configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """Gets the configuration used to get universe data"""
        ...

    @property
    def members(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Security]:
        """
        Gets the current listing of members in this universe. Modifications
        to this dictionary do not change universe membership.
        """
        ...

    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Initializes a new instance of the Universe class
        
        
        This codeEntityType is protected.
        
        :param config: The configuration used to source data for this universe
        """
        ...

    def can_remove_member(self, utc_time: typing.Union[datetime.datetime, datetime.date], security: QuantConnect.Securities.Security) -> bool:
        """
        Determines whether or not the specified security can be removed from
        this universe. This is useful to prevent securities from being taken
        out of a universe before the algorithm has had enough time to make
        decisions on the security
        
        :param utc_time: The current utc time
        :param security: The security to check if its ok to remove
        :returns: True if we can remove the security, false otherwise.
        """
        ...

    def contains_member(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Determines whether or not the specified symbol is currently a member of this universe
        
        :param symbol: The symbol whose membership is to be checked
        :returns: True if the specified symbol is part of this universe, false otherwise.
        """
        ...

    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], algorithm: QuantConnect.Interfaces.IAlgorithm, market_hours_database: QuantConnect.Securities.MarketHoursDatabase, symbol_properties_database: QuantConnect.Securities.SymbolPropertiesDatabase) -> QuantConnect.Securities.Security:
        """
        Creates and configures a security for the specified symbol
        
        
        CreateSecurity is obsolete and will not be called. The system will create the required Securities based on selected symbols
        
        :param symbol: The symbol of the security to be created
        :param algorithm: The algorithm instance
        :param market_hours_database: The market hours database
        :param symbol_properties_database: The symbol properties database
        :returns: The newly initialized security object.
        """
        warnings.warn("CreateSecurity is obsolete and will not be called. The system will create the required Securities based on selected symbols", DeprecationWarning)

    def dispose(self) -> None:
        """Marks this universe as disposed and ready to remove all child subscriptions"""
        ...

    @overload
    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    @overload
    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        
        This overload is obsolete and will not be called. It was not capable of creating new SubscriptionDataConfig due to lack of information
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :returns: All subscriptions required by this security.
        """
        ...

    def on_selection_changed(self, selection: System.Collections.Generic.HashSet[QuantConnect.Symbol] = None) -> None:
        """
        Event invocator for the selection_changed event
        
        
        This codeEntityType is protected.
        
        :param selection: The current universe selection
        """
        ...

    def perform_selection(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class CryptoUniverseFactory(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe that reads crypto coarse data"""

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> None:
        """
        Initializes a new instance of the CryptoUniverseFactory class
        
        :param market: The target crypto market
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.DataSource.CryptoUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the CryptoUniverseFactory class
        
        :param market: The target crypto market
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @staticmethod
    def create_configuration(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates a CryptoUniverse subscription configuration for the selected Crypto market
        
        :param symbol: The symbol used in the returned configuration
        :returns: A coarse fundamental subscription configuration with the specified symbol.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class CryptoCoarseFundamentalUniverse(QuantConnect.Data.UniverseSelection.CryptoUniverseFactory):
    """
    Defines a universe that reads crypto coarse data
    
    
    'CryptoCoarseFundamentalUniverse' was renamed to 'CryptoUniverseFactory'
    """

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> None:
        ...

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.DataSource.CryptoUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        ...


class UniverseDecorator(QuantConnect.Data.UniverseSelection.Universe, metaclass=abc.ABCMeta):
    """
    Provides an implementation of UniverseSelection.Universe that redirects all calls to a
    wrapped (or decorated) universe. This provides scaffolding for other decorators who
    only need to override one or two methods.
    """

    @property
    def universe(self) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        The decorated universe instance
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the settings used for subscriptions added for this universe"""
        ...

    @universe_settings.setter
    def universe_settings(self, value: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        ...

    @property
    def securities(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe.Member]:
        """Gets the internal security collection used to define membership in this universe"""
        ...

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe) -> None:
        """
        Initializes a new instance of the UniverseDecorator class
        
        
        This codeEntityType is protected.
        
        :param universe: The decorated universe. All overridable methods delegate to this instance.
        """
        ...

    def can_remove_member(self, utc_time: typing.Union[datetime.datetime, datetime.date], security: QuantConnect.Securities.Security) -> bool:
        """
        Determines whether or not the specified security can be removed from
        this universe. This is useful to prevent securities from being taken
        out of a universe before the algorithm has had enough time to make
        decisions on the security
        
        :param utc_time: The current utc time
        :param security: The security to check if its ok to remove
        :returns: True if we can remove the security, false otherwise.
        """
        ...

    def create_security(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], algorithm: QuantConnect.Interfaces.IAlgorithm, market_hours_database: QuantConnect.Securities.MarketHoursDatabase, symbol_properties_database: QuantConnect.Securities.SymbolPropertiesDatabase) -> QuantConnect.Securities.Security:
        """
        Creates and configures a security for the specified symbol
        
        
        CreateSecurity is obsolete and will not be called. The system will create the required Securities based on selected symbols
        
        :param symbol: The symbol of the security to be created
        :param algorithm: The algorithm instance
        :param market_hours_database: The market hours database
        :param symbol_properties_database: The symbol properties database
        :returns: The newly initialized security object.
        """
        warnings.warn("CreateSecurity is obsolete and will not be called. The system will create the required Securities based on selected symbols", DeprecationWarning)

    @overload
    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    @overload
    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        
        This overload is obsolete and will not be called. It was not capable of creating new SubscriptionDataConfig due to lack of information
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :returns: All subscriptions required by this security.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class SelectSymbolsUniverseDecorator(QuantConnect.Data.UniverseSelection.UniverseDecorator):
    """Provides a univese decoration that replaces the implementation of select_symbols"""

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, select_symbols: typing.Callable[[datetime.datetime, QuantConnect.Data.UniverseSelection.BaseDataCollection], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the SelectSymbolsUniverseDecorator class
        
        :param universe: The universe to be decorated
        :param select_symbols: The new implementation of select_symbols
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...

    def select_symbols_delegate(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Delegate type for the select_symbols method
        
        :param utc_time: The current utc frontier time
        :param data: The universe selection data
        :returns: The symbols selected by the universe.
        """
        ...


class FundamentalUniverseFactory(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe that reads fundamental us equity data"""

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> None:
        """
        Initializes a new instance of the FundamentalUniverseFactory class
        
        :param market: The target market
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FundamentalUniverseFactory class
        
        :param market: The target market
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], System.Object]) -> None:
        """
        Initializes a new instance of the FundamentalUniverseFactory class
        
        :param market: The target market
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FundamentalUniverseFactory class
        
        :param symbol: Defines the symbol to use for this universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @staticmethod
    def create_configuration(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates a Fundamental.Fundamental subscription configuration for the US-equity market
        
        :param symbol: The symbol used in the returned configuration
        :returns: A fundamental subscription configuration with the specified symbol.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class FundamentalFilteredUniverse(QuantConnect.Data.UniverseSelection.SelectSymbolsUniverseDecorator):
    """Provides a universe that can be filtered with a Fundamental.Fundamental selection function"""

    @property
    def fundamental_universe(self) -> QuantConnect.Data.UniverseSelection.FundamentalUniverseFactory:
        """The universe that will be used for fine universe selection"""
        ...

    @overload
    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fundamental_selector: typing.Any) -> None:
        """
        Initializes a new instance of the FundamentalFilteredUniverse class
        
        :param universe: The universe to be filtered
        :param fundamental_selector: The fundamental selection function
        """
        ...

    @overload
    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fundamental_selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FundamentalFilteredUniverse class
        
        :param universe: The universe to be filtered
        :param fundamental_selector: The fundamental selection function
        """
        ...


class OptionChainUniverse(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe for a single option chain"""

    @property
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @property
    def option(self) -> QuantConnect.Securities.Option.Option:
        """The canonical option chain security"""
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the settings used for subscriptons added for this universe"""
        ...

    @universe_settings.setter
    def universe_settings(self, value: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        ...

    def __init__(self, option: QuantConnect.Securities.Option.Option, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the OptionChainUniverse class
        
        :param option: The canonical option chain security
        :param universe_settings: The universe settings to be used for new subscriptions
        """
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class IFundamentalDataProvider(metaclass=abc.ABCMeta):
    """"""

    def initialize(self, data_provider: QuantConnect.Interfaces.IDataProvider, live_mode: bool) -> None:
        """
        Initializes the service
        
        :param data_provider: The data provider instance to use
        :param live_mode: True if running in live mode
        """
        ...


class BaseFundamentalDataProvider(System.Object, QuantConnect.Data.UniverseSelection.IFundamentalDataProvider):
    """Base fundamental data provider"""

    @property
    def live_mode(self) -> bool:
        """True if live trading"""
        ...

    @live_mode.setter
    def live_mode(self, value: bool) -> None:
        ...

    @property
    def data_provider(self) -> QuantConnect.Interfaces.IDataProvider:
        """
        THe data provider instance to use
        
        
        This codeEntityType is protected.
        """
        ...

    @data_provider.setter
    def data_provider(self, value: QuantConnect.Interfaces.IDataProvider) -> None:
        ...

    def initialize(self, data_provider: QuantConnect.Interfaces.IDataProvider, live_mode: bool) -> None:
        """
        Initializes the service
        
        :param data_provider: The data provider instance to use
        :param live_mode: True if running in live mode
        """
        ...

    @staticmethod
    @overload
    def is_none(value: typing.Any) -> bool:
        """True if the given value is none"""
        ...

    @staticmethod
    @overload
    def is_none(type: typing.Type, value: typing.Any) -> bool:
        """True if the given value is none"""
        ...


class CoarseFundamental(QuantConnect.Data.BaseData):
    """Defines summary information about a single symbol for a given date"""

    @property
    def market(self) -> str:
        """Gets the market for this symbol"""
        ...

    @property
    def dollar_volume(self) -> float:
        """Gets the day's dollar volume for this symbol"""
        ...

    @property
    def volume(self) -> int:
        """Gets the day's total volume"""
        ...

    @property
    def has_fundamental_data(self) -> bool:
        """Returns whether the symbol has fundamental data for the given date"""
        ...

    @property
    def price_factor(self) -> float:
        """Gets the price factor for the given date"""
        ...

    @property
    def split_factor(self) -> float:
        """Gets the split factor for the given date"""
        ...

    @property
    def price_scale_factor(self) -> float:
        """Gets the combined factor used to create adjusted prices from raw prices"""
        ...

    @property
    def adjusted_price(self) -> float:
        """Gets the split and dividend adjusted price"""
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """The end time of this data."""
        ...

    @end_time.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def price(self) -> float:
        """Gets the raw price"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the CoarseFundamental class"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @staticmethod
    def to_row(coarse: QuantConnect.Data.UniverseSelection.CoarseFundamental) -> str:
        """Converts a given fundamental data point into row format"""
        ...


class CoarseFundamentalUniverse(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe that reads coarse us equity data"""

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverse class
        
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Any) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverse class
        
        :param symbol: Defines the symbol to use for this universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverse class
        
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverse class
        
        :param symbol: Defines the symbol to use for this universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @staticmethod
    def create_configuration(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates a CoarseFundamental subscription configuration for the US-equity market
        
        :param symbol: The symbol used in the returned configuration
        :returns: A coarse fundamental subscription configuration with the specified symbol.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class ETFConstituentUniverse(QuantConnect.Data.UniverseSelection.BaseDataCollection):
    """ETF constituent data"""

    @property
    def last_update(self) -> typing.Optional[datetime.datetime]:
        """Time of the previous ETF constituent data update"""
        ...

    @last_update.setter
    def last_update(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def weight(self) -> typing.Optional[float]:
        """The percentage of the ETF allocated to this constituent"""
        ...

    @weight.setter
    def weight(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def shares_held(self) -> typing.Optional[float]:
        """Number of shares held in the ETF"""
        ...

    @shares_held.setter
    def shares_held(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def market_value(self) -> typing.Optional[float]:
        """Market value of the current asset held in U.S. dollars"""
        ...

    @market_value.setter
    def market_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def period(self) -> datetime.timedelta:
        """Period of the data"""
        ...

    @period.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time that the data became available to use"""
        ...

    @end_time.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Creates a copy of the instance
        
        :returns: Clone of the instance.
        """
        ...

    def data_time_zone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> typing.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class ETFConstituentData(QuantConnect.Data.UniverseSelection.ETFConstituentUniverse):
    """
    ETF Constituent data
    
    
    'ETFConstituentData' was renamed to 'ETFConstituentUniverse'
    """


class FineFundamentalUniverse(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe that reads fine us equity data"""

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FineFundamentalUniverse class
        
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FineFundamentalUniverse class
        
        :param symbol: Defines the symbol to use for this universe
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param selector: Returns the symbols that should be included in the universe
        """
        ...

    @staticmethod
    def create_configuration(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates a FineFundamental subscription configuration for the US-equity market
        
        :param symbol: The symbol used in the returned configuration
        :returns: A fine fundamental subscription configuration with the specified symbol.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class FineFundamentalFilteredUniverse(QuantConnect.Data.UniverseSelection.SelectSymbolsUniverseDecorator):
    """Provides a universe that can be filtered with a FineFundamental selection function"""

    @property
    def fine_fundamental_universe(self) -> QuantConnect.Data.UniverseSelection.FineFundamentalUniverse:
        """The universe that will be used for fine universe selection"""
        ...

    @overload
    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fine_selector: typing.Any) -> None:
        """
        Initializes a new instance of the FineFundamentalFilteredUniverse class
        
        :param universe: The universe to be filtered
        :param fine_selector: The fine selection function
        """
        ...

    @overload
    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, fine_selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FineFundamentalFilteredUniverse class
        
        :param universe: The universe to be filtered
        :param fine_selector: The fine selection function
        """
        ...


class ITimeTriggeredUniverse(metaclass=abc.ABCMeta):
    """
    A universe implementing this interface will NOT use it's SubscriptionDataConfig to generate data
    that is used to 'pulse' the universe selection function -- instead, the times output by
    GetTriggerTimes are used to 'pulse' the universe selection function WITHOUT data.
    """

    def get_trigger_times(self, start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date], market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> typing.Iterable[datetime.datetime]:
        """
        Returns an enumerator that defines when this user defined universe will be invoked
        
        :returns: An enumerator of DateTime that defines when this universe will be invoked.
        """
        ...


class DerivativeUniverseData(System.Object):
    """Represents derivative market data including trade and open interest information."""

    @overload
    def __init__(self, open_interest: QuantConnect.Data.Market.OpenInterest) -> None:
        """
        Initializes a new instance of DerivativeUniverseData using open interest data.
        
        :param open_interest: The open interest data.
        """
        ...

    @overload
    def __init__(self, trade_bar: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Initializes a new instance of DerivativeUniverseData using trade bar data.
        
        :param trade_bar: The trade bar data.
        """
        ...

    @overload
    def __init__(self, quote_bar: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Initializes a new instance of DerivativeUniverseData using quote bar data.
        
        :param quote_bar: The quote bar data.
        """
        ...

    def to_csv(self) -> str:
        """
        Converts the current data to a CSV format string.
        
        :returns: A CSV formatted string representing the data.
        """
        ...

    def update_by_open_interest(self, open_interest: QuantConnect.Data.Market.OpenInterest) -> None:
        """
        Updates the instance with new open interest data.
        
        :param open_interest: The new open interest data.
        """
        ...

    def update_by_quote_bar(self, quote_bar: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Updates the instance with new quote bar data.
        
        :param quote_bar: The new quote bar data.
        """
        ...

    def update_by_trade_bar(self, trade_bar: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Updates the instance with new trade bar data.
        
        :param trade_bar: The new trade bar data.
        """
        ...


class UniversePythonWrapper(QuantConnect.Data.UniverseSelection.Universe):
    """Provides an implementation of Universe that wraps a PyObject object"""

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the settings used for subscriptions added for this universe"""
        ...

    @universe_settings.setter
    def universe_settings(self, value: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        ...

    @property
    def dispose_requested(self) -> bool:
        """Flag indicating if disposal of this universe has been requested"""
        ...

    @dispose_requested.setter
    def dispose_requested(self, value: bool) -> None:
        ...

    @property
    def configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """Gets the configuration used to get universe data"""
        ...

    @property
    def securities(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Symbol, QuantConnect.Data.UniverseSelection.Universe.Member]:
        """Gets the internal security collection used to define membership in this universe"""
        ...

    def __init__(self, universe: typing.Any) -> None:
        """Initializes a new instance of the UniversePythonWrapper class"""
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class UniverseExtensions(System.Object):
    """Provides extension methods for the Universe class"""

    @staticmethod
    def chained_to(first: QuantConnect.Data.UniverseSelection.Universe, second: QuantConnect.Data.UniverseSelection.Universe, configuration_per_symbol: bool) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe that logically is the result of wiring the two universes together such that
        the first will produce subscriptions for the second and the second will only select on data that has
        passed the first.
        
        NOTE: The first and second universe instances provided
        to this method should not be manually added to the algorithm.
        
        :param first: The first universe in this 'chain'
        :param second: The second universe in this 'chain'
        :param configuration_per_symbol: True if each symbol as its own configuration, false otherwise
        :returns: A new universe that can be added to the algorithm that represents invoking the first universe
        and then the second universe using the outputs of the first.
        """
        ...

    @staticmethod
    def create_symbol(security_type: QuantConnect.SecurityType, market: str, ticker: str) -> QuantConnect.Symbol:
        """
        Creates a universe symbol
        
        :param security_type: The security
        :param market: The market
        :param ticker: The Universe ticker
        :returns: A symbol for user defined universe of the specified security type and market.
        """
        ...

    @staticmethod
    def prefilter_using(second: QuantConnect.Data.UniverseSelection.Universe, first: QuantConnect.Data.UniverseSelection.Universe) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates a new universe that restricts the universe selection data to symbols that passed the
        first universe's selection critera
        
        NOTE: The second universe instance provided to this method should not be manually
        added to the algorithm. The first should still be manually (assuming no other changes).
        
        :param second: The universe to be filtere
        :param first: The universe providing the set of symbols used for filtered
        :returns: A new universe that can be added to the algorithm that represents invoking the second
        using the selections from the first as a filter.
        """
        ...

    @staticmethod
    def run_universe_downloader(data_downloader: QuantConnect.IDataDownloader, universe_download_parameters: QuantConnect.DataUniverseDownloaderGetParameters) -> None:
        """
        Processes the universe download based on parameters.
        
        :param data_downloader: The data downloader instance.
        :param universe_download_parameters: The parameters for universe downloading.
        """
        ...


class FundamentalService(System.Object):
    """Fundamental data provider service"""

    @staticmethod
    @overload
    def initialize(data_provider: QuantConnect.Interfaces.IDataProvider, live_mode: bool) -> None:
        """
        Initializes the service
        
        :param data_provider: The data provider instance to use
        :param live_mode: True if running in live mode
        """
        ...

    @staticmethod
    @overload
    def initialize(data_provider: QuantConnect.Interfaces.IDataProvider, fundamental_data_provider: str, live_mode: bool) -> None:
        """
        Initializes the service
        
        :param data_provider: The data provider instance to use
        :param fundamental_data_provider: The fundamental data provider
        :param live_mode: True if running in live mode
        """
        ...

    @staticmethod
    @overload
    def initialize(data_provider: QuantConnect.Interfaces.IDataProvider, fundamental_data_provider: QuantConnect.Data.UniverseSelection.IFundamentalDataProvider, live_mode: bool) -> None:
        """
        Initializes the service
        
        :param data_provider: The data provider instance to use
        :param fundamental_data_provider: The fundamental data provider
        :param live_mode: True if running in live mode
        """
        ...


class BaseChainUniverseData(QuantConnect.Data.UniverseSelection.BaseDataCollection, QuantConnect.Securities.IChainUniverseData, metaclass=abc.ABCMeta):
    """
    Represents a chain universe.
    Intended as a base for options and futures universe data.
    """

    @property
    def csv_line(self) -> str:
        """
        Csv line to get the values from
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def id(self) -> QuantConnect.SecurityIdentifier:
        """The security identifier of the option symbol"""
        ...

    @property
    def value(self) -> float:
        """Price of the security"""
        ...

    @property
    def open(self) -> float:
        """Open price of the security"""
        ...

    @property
    def high(self) -> float:
        """High price of the security"""
        ...

    @property
    def low(self) -> float:
        """Low price of the security"""
        ...

    @property
    def close(self) -> float:
        """Close price of the security"""
        ...

    @property
    def volume(self) -> float:
        """Volume value of the security"""
        ...

    @property
    def open_interest(self) -> float:
        """Open interest value"""
        ...

    @property
    def end_time(self) -> datetime.datetime:
        """Time that the data became available to use"""
        ...

    @end_time.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a new instance of the BaseChainUniverseData class
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], csv: str) -> None:
        """
        Creates a new instance of the BaseChainUniverseData class
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, other: QuantConnect.Data.UniverseSelection.BaseChainUniverseData) -> None:
        """
        Creates a new instance of the BaseChainUniverseData class as a copy of the given instance
        
        
        This codeEntityType is protected.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    @staticmethod
    def get_universe_full_file_path(symbol: QuantConnect.Symbol, date: datetime.datetime) -> str:
        """
        Generates the file path for a universe data file based on the given symbol and date.
        Optionally, creates the directory if it does not exist.
        
        :param symbol: The financial symbol for which the universe file is generated.
        :param date: The date associated with the universe file.
        :returns: The full file path to the universe data file.
        """
        ...

    def to_symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol of the option"""
        ...


class OptionUniverse(QuantConnect.Data.UniverseSelection.BaseChainUniverseData):
    """Represents a universe of options data"""

    @property
    def open_interest(self) -> float:
        """Open interest value of the option"""
        ...

    @property
    def implied_volatility(self) -> float:
        """Implied volatility value of the option"""
        ...

    @property
    def greeks(self) -> QuantConnect.Data.Market.Greeks:
        """Greeks values of the option"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the OptionUniverse class"""
        ...

    @overload
    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], csv: str) -> None:
        """Creates a new instance of the OptionUniverse class"""
        ...

    @overload
    def __init__(self, other: QuantConnect.Data.UniverseSelection.OptionUniverse) -> None:
        """Creates a new instance of the OptionUniverse class as a copy of the given instance"""
        ...

    def add(self, new_data_point: QuantConnect.Data.BaseData) -> None:
        """
        Adds a new data point to this collection.
        If the data point is for the underlying, it will be stored in the BaseDataCollection.underlying property.
        
        :param new_data_point: The new data point to add
        """
        ...

    @staticmethod
    def cache_symbol(key: System.ValueTuple[QuantConnect.SecurityType, str, str, datetime.datetime, float, QuantConnect.OptionRight], symbol: QuantConnect.Symbol) -> None:
        """
        Caches a symbol
        
        
        This codeEntityType is protected.
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Creates a copy of the instance
        
        :returns: Clone of the instance.
        """
        ...

    @staticmethod
    def csv_header(security_type: QuantConnect.SecurityType) -> str:
        """Gets the CSV header string for this universe entry"""
        ...

    @staticmethod
    def to_csv(symbol: QuantConnect.Symbol, open: float, high: float, low: float, close: float, volume: float, open_interest: typing.Optional[float], implied_volatility: typing.Optional[float], greeks: QuantConnect.Data.Market.Greeks) -> str:
        """Gets the CSV string representation of this universe entry"""
        ...

    @staticmethod
    def try_get_cached_symbol(key: System.ValueTuple[QuantConnect.SecurityType, str, str, datetime.datetime, float, QuantConnect.OptionRight], symbol: typing.Optional[QuantConnect.Symbol]) -> typing.Tuple[bool, QuantConnect.Symbol]:
        """
        Tries to get a symbol from the cache
        
        
        This codeEntityType is protected.
        """
        ...


class ConstituentsUniverseData(QuantConnect.Data.BaseData):
    """Custom base data class used for ConstituentsUniverse"""

    @property
    def end_time(self) -> datetime.datetime:
        """The end time of this data."""
        ...

    @end_time.setter
    def end_time(self, value: datetime.datetime) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the CoarseFundamental class"""
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    def get_source(self, config: QuantConnect.Data.SubscriptionDataConfig, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def is_sparse_data(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
        """
        ...

    def reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: datetime.datetime, is_live_mode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param is_live_mode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def requires_mapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def supported_resolutions(self) -> typing.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class ConstituentsUniverse(typing.Generic[QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T], QuantConnect.Data.UniverseSelection.FuncUniverse[QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T]):
    """
    ConstituentsUniverse allows to perform universe selection based on an
    already preselected set of Symbol.
    """

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Any = None) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param symbol: The universe symbol
        :param universe_settings: The universe settings to use
        :param constituents_filter: User-provided function to filter constituents universe with
        """
        ...

    @overload
    def __init__(self, subscription_data_config: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Any = None) -> None:
        """
        Constituent universe for a Python function
        
        :param subscription_data_config: The universe configuration to use
        :param universe_settings: The universe settings to use
        :param constituents_filter: User-provided function to filter constituents universe with
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, filter_func: typing.Any) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param symbol: The universe symbol
        :param universe_settings: The universe settings to use
        :param filter_func: The constituents filter function
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Callable[[typing.List[QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T]], typing.List[QuantConnect.Symbol]] = None) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param symbol: The universe symbol
        :param universe_settings: The universe settings to use
        :param constituents_filter: User-provided function to filter constituents universe with
        """
        ...

    @overload
    def __init__(self, subscription_data_config: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Callable[[typing.List[QuantConnect_Data_UniverseSelection_ConstituentsUniverse_T]], typing.List[QuantConnect.Symbol]] = None) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param subscription_data_config: The universe configuration to use
        :param universe_settings: The universe settings to use
        :param constituents_filter: User-provided function to filter constituents universe with
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, filter_func: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ConstituentsUniverseData]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param symbol: The universe symbol
        :param universe_settings: The universe settings to use
        :param filter_func: The constituents filter function
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of the ConstituentsUniverse
        
        :param symbol: The universe symbol
        :param universe_settings: The universe settings to use
        """
        ...


class ETFConstituentsUniverseFactory(QuantConnect.Data.UniverseSelection.ConstituentsUniverse[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]):
    """Creates a universe based on an ETF's holdings at a given date"""

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Any) -> None:
        """
        Creates a new universe for the constituents of the ETF provided as symbol
        
        :param symbol: The ETF to load constituents for
        :param universe_settings: Universe settings
        :param constituents_filter: The filter function used to filter out ETF constituents from the universe
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, constituents_filter: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], typing.List[QuantConnect.Symbol]] = None) -> None:
        """
        Creates a new universe for the constituents of the ETF provided as symbol
        
        :param symbol: The ETF to load constituents for
        :param universe_settings: Universe settings
        :param constituents_filter: The filter function used to filter out ETF constituents from the universe
        """
        ...


class UserDefinedUniverse(QuantConnect.Data.UniverseSelection.Universe, System.Collections.Specialized.INotifyCollectionChanged, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """
    Represents the universe defined by the user's algorithm. This is
    the default universe where manually added securities live by
    market/security type. They can also be manually generated and
    can be configured to fire on certain interval and will always
    return the internal list of symbols.
    """

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]:
        """Event fired when a symbol is added or removed from this universe"""
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def interval(self) -> datetime.timedelta:
        """Gets the interval of this user defined universe"""
        ...

    @overload
    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, symbols: typing.List[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the UserDefinedUniverse class
        
        :param configuration: The configuration used to resolve the data for universe selection
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param interval: The interval at which selection should be performed
        :param symbols: The initial set of symbols in this universe
        """
        ...

    @overload
    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        """
        Initializes a new instance of the UserDefinedUniverse class
        
        :param configuration: The configuration used to resolve the data for universe selection
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param interval: The interval at which selection should be performed
        :param selector: Universe selection function invoked for each time returned via GetTriggerTimes.
        The function parameter is a DateTime in the time zone of configuration.ExchangeTimeZone
        """
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Adds the specified Symbol to this universe
        
        :param symbol: The symbol to be added to this universe
        :returns: True if the symbol was added, false if it was already present.
        """
        ...

    @overload
    def add(self, subscription_data_config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Adds the specified SubscriptionDataConfig to this universe
        
        :param subscription_data_config: The subscription data configuration to be added to this universe
        :returns: True if the subscription_data_config was added, false if it was already present.
        """
        ...

    @staticmethod
    def create_symbol(security_type: QuantConnect.SecurityType, market: str) -> QuantConnect.Symbol:
        """
        Creates a user defined universe symbol
        
        :param security_type: The security
        :param market: The market
        :returns: A symbol for user defined universe of the specified security type and market.
        """
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    def get_trigger_times(self, start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date], market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> typing.Iterable[datetime.datetime]:
        """
        Returns an enumerator that defines when this user defined universe will be invoked
        
        :returns: An enumerator of DateTime that defines when this universe will be invoked.
        """
        ...

    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        Event invocator for the collection_changed event
        
        
        This codeEntityType is protected.
        
        :param e: The notify collection changed event arguments
        """
        ...

    def remove(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Removes the specified Symbol from this universe
        
        :param symbol: The symbol to be removed
        :returns: True if the symbol was removed, false if the symbol was not present.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Returns the symbols defined by the user for this universe
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class FuncUniverse(typing.Generic[QuantConnect_Data_UniverseSelection_FuncUniverse_T], QuantConnect.Data.UniverseSelection.Universe):
    """Provides a functional implementation of Universe"""

    @overload
    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_selector: typing.Any) -> None:
        """
        Initializes a new instance of the FuncUniverse{T} class for a filter function loaded from Python
        
        :param configuration: The configuration used to resolve the data for universe selection
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param universe_selector: Function that returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_selector: typing.Callable[[typing.List[QuantConnect_Data_UniverseSelection_FuncUniverse_T]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FuncUniverse{T} class
        
        :param configuration: The configuration used to resolve the data for universe selection
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param universe_selector: Returns the symbols that should be included in the universe
        """
        ...

    @overload
    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_selector: typing.Callable[[typing.List[QuantConnect.Data.BaseData]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the FuncUniverse class
        
        :param configuration: The configuration used to resolve the data for universe selection
        :param universe_settings: The settings used for new subscriptions generated by this universe
        :param universe_selector: Returns the symbols that should be included in the universe
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs an initial, coarse filter
        
        :param utc_time: The current utc time
        :param data: The coarse fundamental data
        :returns: The data that passes the filter.
        """
        ...


class ScheduledUniverse(QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """Defines a user that is fired based on a specified IDateRule and ITimeRule"""

    @overload
    def __init__(self, time_zone: typing.Any, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverse class
        
        :param time_zone: The time zone the date/time rules are in
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, time_zone: typing.Any, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Any, settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverse class
        
        :param time_zone: The time zone the date/time rules are in
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Any, settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverse class
        
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverse class
        
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    def get_trigger_times(self, start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date], market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> typing.Iterable[datetime.datetime]:
        """
        Get an enumerator of UTC DateTimes that defines when this universe will be invoked
        
        :param start_time_utc: The start time of the range in UTC
        :param end_time_utc: The end time of the range in UTC
        :returns: An enumerator of UTC DateTimes that defines when this universe will be invoked.
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class FuturesChainUniverse(QuantConnect.Data.UniverseSelection.Universe):
    """Defines a universe for a single futures chain"""

    @property
    def asynchronous(self) -> bool:
        """True if this universe filter can run async in the data stack"""
        ...

    @property
    def future(self) -> QuantConnect.Securities.Future.Future:
        """The canonical future chain security"""
        ...

    @property
    def universe_settings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the settings used for subscriptons added for this universe"""
        ...

    @universe_settings.setter
    def universe_settings(self, value: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        ...

    def __init__(self, future: QuantConnect.Securities.Future.Future, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the FuturesChainUniverse class
        
        :param future: The canonical future chain security
        :param universe_settings: The universe settings to be used for new subscriptions
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection using the data specified
        
        :param utc_time: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class SecurityChanges(System.Object):
    """Defines the additions and subtractions to the algorithm's security subscriptions"""

    NONE: QuantConnect.Data.UniverseSelection.SecurityChanges = ...
    """Gets an instance that represents no changes have been made"""

    @property
    def count(self) -> int:
        """Gets the total count of added and removed securities"""
        ...

    @property
    def filter_custom_securities(self) -> bool:
        """
        True will filter out custom securities from the
        added_securities and removed_securities properties
        """
        ...

    @filter_custom_securities.setter
    def filter_custom_securities(self, value: bool) -> None:
        ...

    @property
    def filter_internal_securities(self) -> bool:
        """
        True will filter out internal securities from the
        added_securities and removed_securities properties
        """
        ...

    @filter_internal_securities.setter
    def filter_internal_securities(self, value: bool) -> None:
        ...

    @property
    def added_securities(self) -> typing.Sequence[QuantConnect.Securities.Security]:
        """Gets the symbols that were added by universe selection"""
        ...

    @property
    def removed_securities(self) -> typing.Sequence[QuantConnect.Securities.Security]:
        """
        Gets the symbols that were removed by universe selection. This list may
        include symbols that were removed, but are still receiving data due to
        existing holdings or open orders
        """
        ...

    def __add__(self, right: QuantConnect.Data.UniverseSelection.SecurityChanges) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """
        Combines the results of two SecurityChanges
        
        :param right: The right side of the operand
        :returns: Adds the additions together and removes any removals found in the additions, that is, additions take precedence.
        """
        ...

    def __iadd__(self, right: QuantConnect.Data.UniverseSelection.SecurityChanges) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """
        Combines the results of two SecurityChanges
        
        :param right: The right side of the operand
        :returns: Adds the additions together and removes any removals found in the additions, that is, additions take precedence.
        """
        ...

    def __init__(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Initializes a new instance of the SecurityChanges class
        as a shallow clone of a given instance, sharing the same collections
        
        :param changes: The instance to clone
        """
        ...

    @staticmethod
    def create(additions: typing.Sequence[QuantConnect.Securities.Security], removals: typing.Sequence[QuantConnect.Securities.Security], internal_additions: typing.Sequence[QuantConnect.Securities.Security], internal_removals: typing.Sequence[QuantConnect.Securities.Security]) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """
        Initializes a new instance of the SecurityChanges class all none internal
        
        :param additions: Added symbols list
        :param removals: Removed symbols list
        :param internal_additions: Internal added symbols list
        :param internal_removals: Internal removed symbols list
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class SecurityChangesConstructor(System.Object):
    """Helper method to create security changes"""

    def add(self, security: QuantConnect.Securities.Security, is_internal: bool) -> None:
        """Inserts a security addition change"""
        ...

    def flush(self) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """Get the current security changes clearing state"""
        ...

    def remove(self, security: QuantConnect.Securities.Security, is_internal: bool) -> None:
        """Inserts a security removal change"""
        ...


class CoarseFundamentalDataProvider(QuantConnect.Data.UniverseSelection.BaseFundamentalDataProvider):
    """Coarse base fundamental data provider"""

    class CoarseFundamentalSource(QuantConnect.Data.UniverseSelection.CoarseFundamental):
        """Coarse fundamental with setters"""

        @property
        def volume_setter(self) -> int:
            """Property to set the volume of the Coarse Fundamental"""
            ...

        @property
        def dollar_volume_setter(self) -> float:
            """Property to set the dollar volume of the Coarse Fundamental"""
            ...

        @property
        def price_factor_setter(self) -> float:
            """Property to set the price factor of the Coarse Fundamental"""
            ...

        @price_factor_setter.setter
        def price_factor_setter(self, value: float) -> None:
            ...

        @property
        def split_factor_setter(self) -> float:
            """Property to set the split factor of the Coarse Fundamental"""
            ...

        @split_factor_setter.setter
        def split_factor_setter(self, value: float) -> None:
            ...

        @property
        def has_fundamental_data_setter(self) -> bool:
            """Property to indicate if the Coarse Fundamental has fundamental data"""
            ...

        @has_fundamental_data_setter.setter
        def has_fundamental_data_setter(self, value: bool) -> None:
            ...

        @property
        def dollar_volume(self) -> float:
            """Gets the day's dollar volume for this symbol"""
            ...

        @property
        def volume(self) -> int:
            """Gets the day's total volume"""
            ...

        @property
        def has_fundamental_data(self) -> bool:
            """Returns whether the symbol has fundamental data for the given date"""
            ...

        @property
        def price_factor(self) -> float:
            """Gets the price factor for the given date"""
            ...

        @property
        def split_factor(self) -> float:
            """Gets the split factor for the given date"""
            ...

    @staticmethod
    def read(line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.UniverseSelection.CoarseFundamentalDataProvider.CoarseFundamentalSource:
        """Reads the given line and returns a CoarseFundamentalSource with the information within it"""
        ...


class FutureUniverse(QuantConnect.Data.UniverseSelection.BaseChainUniverseData):
    """Represents a universe of futures data"""

    CSV_HEADER: str
    """Gets the CSV header string for this universe entry"""

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the FutureUniverse class"""
        ...

    @overload
    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], csv: str) -> None:
        """Creates a new instance of the FutureUniverse class"""
        ...

    @overload
    def __init__(self, other: QuantConnect.Data.UniverseSelection.FutureUniverse) -> None:
        """Creates a new instance of the FutureUniverse class as a copy of the given instance"""
        ...

    @staticmethod
    def cache_symbol(key: System.ValueTuple[QuantConnect.SecurityType, str, str, datetime.datetime], symbol: QuantConnect.Symbol) -> None:
        """
        Caches a symbol
        
        
        This codeEntityType is protected.
        """
        ...

    def clone(self) -> QuantConnect.Data.BaseData:
        """
        Creates a copy of the instance
        
        :returns: Clone of the instance.
        """
        ...

    def default_resolution(self) -> QuantConnect.Resolution:
        """Gets the default resolution for this data and security type"""
        ...

    @staticmethod
    def to_csv(symbol: QuantConnect.Symbol, open: float, high: float, low: float, close: float, volume: float, open_interest: typing.Optional[float]) -> str:
        """Gets the CSV string representation of this universe entry"""
        ...

    @staticmethod
    def try_get_cached_symbol(key: System.ValueTuple[QuantConnect.SecurityType, str, str, datetime.datetime], symbol: typing.Optional[QuantConnect.Symbol]) -> typing.Tuple[bool, QuantConnect.Symbol]:
        """
        Tries to get a symbol from the cache
        
        
        This codeEntityType is protected.
        """
        ...


class GetSubscriptionRequestsUniverseDecorator(QuantConnect.Data.UniverseSelection.UniverseDecorator):
    """Provides a universe decoration that replaces the implementation of get_subscription_requests"""

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, get_requests: typing.Callable[[QuantConnect.Securities.Security, datetime.datetime, datetime.datetime], typing.List[QuantConnect.Data.UniverseSelection.SubscriptionRequest]]) -> None:
        """
        Initializes a new instance of the GetSubscriptionRequestsUniverseDecorator class
        
        :param universe: The universe to be decorated
        :param get_requests: 
        """
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :returns: All subscriptions required by this security.
        """
        ...

    def get_subscription_requests_delegate(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Delegate type for the get_subscription_requests method
        
        :param security: The security to get subscription requests for
        :param current_time_utc: The current utc frontier time
        :param maximum_end_time_utc: 
        :returns: The subscription requests for the security to be given to the data feed.
        """
        ...


class ContinuousContractUniverse(QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse):
    """Continuous contract universe selection that based on the requested mapping mode will select each symbol"""

    @property
    def asynchronous(self) -> bool:
        """
        True if this universe filter can run async in the data stack
        TODO: see IContinuousSecurity.Mapped
        """
        ...

    def __init__(self, security: QuantConnect.Securities.Security, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, live_mode: bool, universe_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """Creates a new instance"""
        ...

    @staticmethod
    def add_configurations(subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        """Helper method to add and get the required configurations associated with a continuous universe"""
        ...

    @staticmethod
    def create_symbol(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Symbol:
        """
        Creates a continuous universe symbol
        
        :param symbol: The associated symbol
        :returns: A symbol for a continuous universe of the specified symbol.
        """
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...

    def get_trigger_times(self, start_time_utc: typing.Union[datetime.datetime, datetime.date], end_time_utc: typing.Union[datetime.datetime, datetime.date], market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> typing.Iterable[datetime.datetime]:
        """
        Each tradeable day of the future we trigger a new selection.
        Allows use to select the current contract
        """
        ...

    def select_symbols(self, utc_time: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs universe selection based on the symbol mapping
        
        :param utc_time: The current utc time
        :param data: Empty data
        :returns: The symbols to use.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data_UniverseSelection__EventContainer_Callable, QuantConnect_Data_UniverseSelection__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data_UniverseSelection__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data_UniverseSelection__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data_UniverseSelection__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


