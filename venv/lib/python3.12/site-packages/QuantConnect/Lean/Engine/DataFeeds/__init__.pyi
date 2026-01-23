from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import QuantConnect.Lean.Engine.Results
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections.Generic
import System.IO
import System.Linq
import System.Threading

QuantConnect_Lean_Engine_DataFeeds_UpdateData_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_UpdateData_T")
QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable")
QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType")


class SubscriptionDataReader(System.Object, System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, QuantConnect.Interfaces.IDataProviderEvents):
    """Subscription data reader is a wrapper on the stream reader class to download, unpack and iterate over a data file."""

    @property
    def invalid_configuration_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], typing.Any], typing.Any]:
        """Event fired when an invalid configuration has been detected"""
        ...

    @invalid_configuration_detected.setter
    def invalid_configuration_detected(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def numerical_precision_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], typing.Any], typing.Any]:
        """Event fired when the numerical precision in the factor file has been limited"""
        ...

    @numerical_precision_limited.setter
    def numerical_precision_limited(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def start_date_limited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], typing.Any], typing.Any]:
        """Event fired when the start date has been limited"""
        ...

    @start_date_limited.setter
    def start_date_limited(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def download_failed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], typing.Any], typing.Any]:
        """Event fired when there was an error downloading a remote file"""
        ...

    @download_failed.setter
    def download_failed(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def reader_error_detected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], typing.Any], typing.Any]:
        """Event fired when there was an error reading the data"""
        ...

    @reader_error_detected.setter
    def reader_error_detected(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def new_tradable_date(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], typing.Any], typing.Any]:
        """Event fired when there is a new tradable date"""
        ...

    @new_tradable_date.setter
    def new_tradable_date(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def current(self) -> QuantConnect.Data.BaseData:
        """Last read BaseData object from this type and source"""
        ...

    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, data_request: QuantConnect.Data.BaseDataRequest, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, data_provider: QuantConnect.Interfaces.IDataProvider, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Subscription data reader takes a subscription request, loads the type, accepts the data source and enumerate on the results.
        
        :param config: Subscription configuration object
        :param data_request: The data request
        :param map_file_provider: Used for resolving the correct map files
        :param factor_file_provider: Used for getting factor files
        :param data_cache_provider: Used for caching files
        :param data_provider: The data provider to use
        """
        ...

    def dispose(self) -> None:
        """Dispose of the Stream Reader and close out the source stream and file connections."""
        ...

    def initialize(self) -> None:
        """Initializes the SubscriptionDataReader instance"""
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def on_download_failed(self, e: QuantConnect.DownloadFailedEventArgs) -> None:
        """
        Event invocator for the download_failed event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the download_failed event
        """
        ...

    def on_invalid_configuration_detected(self, e: QuantConnect.InvalidConfigurationDetectedEventArgs) -> None:
        """
        Event invocator for the invalid_configuration_detected event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the invalid_configuration_detected event
        """
        ...

    def on_new_tradable_date(self, e: QuantConnect.NewTradableDateEventArgs) -> None:
        """
        Event invocator for the new_tradable_date event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the new_tradable_date event
        """
        ...

    def on_numerical_precision_limited(self, e: QuantConnect.NumericalPrecisionLimitedEventArgs) -> None:
        """
        Event invocator for the numerical_precision_limited event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the numerical_precision_limited event
        """
        ...

    def on_reader_error_detected(self, e: QuantConnect.ReaderErrorDetectedEventArgs) -> None:
        """
        Event invocator for the reader_error_detected event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the reader_error_detected event
        """
        ...

    def on_start_date_limited(self, e: QuantConnect.StartDateLimitedEventArgs) -> None:
        """
        Event invocator for the start_date_limited event
        
        
        This codeEntityType is protected.
        
        :param e: Event arguments for the start_date_limited event
        """
        ...

    def reset(self) -> None:
        """Reset the IEnumeration"""
        ...


class SubscriptionData(System.Object):
    """Store data (either raw or adjusted) and the time at which it should be synchronized"""

    @property
    def _data(self) -> QuantConnect.Data.BaseData:
        """
        Data
        
        
        This codeEntityType is protected.
        """
        ...

    @_data.setter
    def _data(self, value: QuantConnect.Data.BaseData) -> None:
        ...

    @property
    def data(self) -> QuantConnect.Data.BaseData:
        """Gets the data"""
        ...

    @property
    def emit_time_utc(self) -> datetime.datetime:
        """Gets the UTC emit time for this data"""
        ...

    def __init__(self, data: QuantConnect.Data.BaseData, emit_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the SubscriptionData class
        
        :param data: The base data
        :param emit_time_utc: The emit time for the data
        """
        ...

    @staticmethod
    def create(daily_strict_end_time_enabled: bool, configuration: QuantConnect.Data.SubscriptionDataConfig, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, offset_provider: QuantConnect.TimeZoneOffsetProvider, data: QuantConnect.Data.BaseData, normalization_mode: QuantConnect.DataNormalizationMode, factor: typing.Optional[float] = None) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionData:
        """
        Clones the data, computes the utc emit time and performs exchange round down behavior, storing the result in a new SubscriptionData instance
        
        :param configuration: The subscription's configuration
        :param exchange_hours: The exchange hours of the security
        :param offset_provider: The subscription's offset provider
        :param data: The data being emitted
        :param normalization_mode: Specifies how data is normalized
        :param factor: price scale factor
        :returns: A new SubscriptionData containing the specified data.
        """
        ...


class Subscription(System.Object, System.Collections.Generic.IEnumerator[QuantConnect.Lean.Engine.DataFeeds.SubscriptionData]):
    """Represents the data required for a data feed to process a single subscription"""

    @property
    def new_data_available(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        """Event fired when a new data point is available"""
        ...

    @new_data_available.setter
    def new_data_available(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def universes(self) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """Gets the universe for this subscription"""
        ...

    @property
    def security(self) -> QuantConnect.Interfaces.ISecurityPrice:
        """Gets the security this subscription points to"""
        ...

    @property
    def configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """Gets the configuration for this subscritions"""
        ...

    @property
    def time_zone(self) -> typing.Any:
        """Gets the exchange time zone associated with this subscription"""
        ...

    @property
    def offset_provider(self) -> QuantConnect.TimeZoneOffsetProvider:
        """Gets the offset provider for time zone conversions to and from the data's local time"""
        ...

    @property
    def realtime_price(self) -> float:
        """Gets the most current value from the subscription source"""
        ...

    @realtime_price.setter
    def realtime_price(self, value: float) -> None:
        ...

    @property
    def end_of_stream(self) -> bool:
        """Gets true if this subscription is finished, false otherwise"""
        ...

    @property
    def is_universe_selection_subscription(self) -> bool:
        """Gets true if this subscription is used in universe selection"""
        ...

    @property
    def utc_start_time(self) -> datetime.datetime:
        """Gets the start time of this subscription in UTC"""
        ...

    @property
    def utc_end_time(self) -> datetime.datetime:
        """Gets the end time of this subscription in UTC"""
        ...

    @property
    def removed_from_universe(self) -> QuantConnect.Util.IReadOnlyRef[bool]:
        """Gets whether or not this subscription has been removed from its parent universe"""
        ...

    @property
    def current(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, subscription_request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Lean.Engine.DataFeeds.SubscriptionData], time_zone_offset_provider: QuantConnect.TimeZoneOffsetProvider) -> None:
        """
        Initializes a new instance of the Subscription class with a universe
        
        :param subscription_request: Specified for universe subscriptions
        :param enumerator: The subscription's data source
        :param time_zone_offset_provider: The offset provider used to convert data local times to utc
        """
        ...

    def add_subscription_request(self, subscription_request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a SubscriptionRequest for this subscription
        
        :param subscription_request: The SubscriptionRequest to add
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        :returns: A hash code for the current System.Object.
        """
        ...

    def mark_as_removed_from_universe(self) -> None:
        """
        Mark this subscription as having been removed from the universe.
        Data for this time step will be discarded.
        """
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def on_new_data_available(self) -> None:
        """Event invocator for the new_data_available event"""
        ...

    def remove_subscription_request(self, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes one or all SubscriptionRequest from this subscription
        
        :param universe: Universe requesting to remove SubscriptionRequest.
        Default value, null, will remove all universes
        :returns: True, if the subscription is empty and ready to be removed.
        """
        ...

    def reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class FillForwardResolutionChangedEvent(System.Object):
    """Helper class for fill forward resolution change events"""

    @property
    def old(self) -> datetime.timedelta:
        """The old fill forward time span"""
        ...

    @old.setter
    def old(self, value: datetime.timedelta) -> None:
        ...

    @property
    def new(self) -> datetime.timedelta:
        """The new fill forward time span"""
        ...

    @new.setter
    def new(self, value: datetime.timedelta) -> None:
        ...


class SubscriptionCollection(System.Object, typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.Subscription]):
    """Provides a collection for holding subscriptions."""

    @property
    def fill_forward_resolution_changed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.FillForwardResolutionChangedEvent], typing.Any], typing.Any]:
        """Event fired when the fill forward resolution changes"""
        ...

    @fill_forward_resolution_changed.setter
    def fill_forward_resolution_changed(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.FillForwardResolutionChangedEvent], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the SubscriptionCollection class"""
        ...

    def __iter__(self) -> typing.Iterator[QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        ...

    def contains(self, configuration: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Checks the collection for the specified subscription configuration
        
        :param configuration: The subscription configuration to check for
        :returns: True if a subscription with the specified configuration is found in this collection, false otherwise.
        """
        ...

    def freeze_fill_forward_resolution(self, freeze: bool) -> None:
        """Will disable or enable fill forward resolution updates"""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    def try_add(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> bool:
        """
        Attempts to add the specified subscription to the collection. If another subscription
        exists with the same configuration then it won't be added.
        
        :param subscription: The subscription to add
        :returns: True if the subscription is successfully added, false otherwise.
        """
        ...

    def try_get_value(self, configuration: QuantConnect.Data.SubscriptionDataConfig, subscription: typing.Optional[QuantConnect.Lean.Engine.DataFeeds.Subscription]) -> typing.Tuple[bool, QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Attempts to retrieve the subscription with the specified configuration
        
        :param configuration: The subscription's configuration
        :param subscription: The subscription matching the configuration, null if not found
        :returns: True if the subscription is successfully retrieved, false otherwise.
        """
        ...

    def try_remove(self, configuration: QuantConnect.Data.SubscriptionDataConfig, subscription: typing.Optional[QuantConnect.Lean.Engine.DataFeeds.Subscription]) -> typing.Tuple[bool, QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Attempts to remove the subscription with the specified configuraton from the collection.
        
        :param configuration: The configuration of the subscription to remove
        :param subscription: The removed subscription, null if not found.
        :returns: True if the subscription is successfully removed, false otherwise.
        """
        ...

    def update_and_get_fill_forward_resolution(self, configuration: QuantConnect.Data.SubscriptionDataConfig = None) -> QuantConnect.Util.Ref[datetime.timedelta]:
        """
        Gets and updates the fill forward resolution by checking specified subscription configurations and
        selecting the smallest resoluton not equal to tick
        """
        ...


class UniverseSelection(System.Object):
    """Provides methods for apply the results of universe selection to an algorithm"""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, security_service: QuantConnect.Interfaces.ISecurityService, data_permission_manager: QuantConnect.Interfaces.IDataPermissionManager, data_provider: QuantConnect.Interfaces.IDataProvider, internal_config_resolution: QuantConnect.Resolution = ...) -> None:
        """
        Initializes a new instance of the UniverseSelection class
        
        :param algorithm: The algorithm to add securities to
        :param security_service: The security service
        :param data_permission_manager: The data permissions manager
        :param data_provider: The data provider to use
        :param internal_config_resolution: The resolution to use for internal configuration
        """
        ...

    def add_pending_internal_data_feeds(self, utc_start: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Will add any pending internal currency subscriptions
        
        :param utc_start: The current date time in utc
        :returns: Will return true if any subscription was added.
        """
        ...

    def apply_universe_selection(self, universe: QuantConnect.Data.UniverseSelection.Universe, date_time_utc: typing.Union[datetime.datetime, datetime.date], universe_data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """
        Applies universe selection the the data feed and algorithm
        
        :param universe: The universe to perform selection on
        :param date_time_utc: The current date time in utc
        :param universe_data: The data provided to perform selection with
        """
        ...

    def ensure_currency_data_feeds(self, security_changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Checks the current subscriptions and adds necessary currency pair feeds to provide real time conversion data"""
        ...

    def handle_delisting(self, data: QuantConnect.Data.BaseData, is_internal_feed: bool) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """Handles the delisting process of the given data symbol from the algorithm securities"""
        ...

    def set_data_manager(self, data_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """Sets the data manager"""
        ...


class IDataFeedSubscriptionManager(metaclass=abc.ABCMeta):
    """DataFeedSubscriptionManager interface will manage the subscriptions for the Data Feed"""

    @property
    @abc.abstractmethod
    def subscription_added(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when a new subscription is added"""
        ...

    @subscription_added.setter
    def subscription_added(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def subscription_removed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when an existing subscription is removed"""
        ...

    @subscription_removed.setter
    def subscription_removed(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def data_feed_subscriptions(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionCollection:
        """Gets the data feed subscription collection"""
        ...

    @property
    @abc.abstractmethod
    def universe_selection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Get the universe selection instance"""
        ...

    def add_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a new Subscription to provide data for the specified security.
        
        :param request: Defines the SubscriptionRequest to be added
        :returns: True if the subscription was created and added successfully, false otherwise.
        """
        ...

    def remove_subscription(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes the Subscription, if it exists
        
        :param configuration: The SubscriptionDataConfig of the subscription to remove
        :param universe: Universe requesting to remove Subscription.
        Default value, null, will remove all universes
        :returns: True if the subscription was successfully removed, false otherwise.
        """
        ...


class SubscriptionFrontierTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """A time provider which updates 'now' time based on the current data emit time of all subscriptions"""

    def __init__(self, utc_now: typing.Union[datetime.datetime, datetime.date], subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """
        Creates a new instance of the SubscriptionFrontierTimeProvider
        
        :param utc_now: Initial UTC now time
        :param subscription_manager: Subscription manager. Will be used to obtain current subscriptions
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class CachingFutureChainProvider(System.Object, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that will cache by date future contracts returned by another future chain provider."""

    def __init__(self, future_chain_provider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """
        Initializes a new instance of the CachingFutureChainProvider class
        
        :param future_chain_provider: 
        """
        ...

    def get_future_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class ProcessedDataProvider(System.Object, QuantConnect.Interfaces.IDataProvider, System.IDisposable):
    """A data provider that will check the processed data folder first"""

    @property
    def new_data_request(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]:
        """Ignored"""
        ...

    @new_data_request.setter
    def new_data_request(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    @overload
    def dispose(self) -> None:
        """Disposes of resources"""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Disposes of the internal data provider
        
        
        This codeEntityType is protected.
        """
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data from disc to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...


class ChainProviderInitializeParameters(System.Object):
    """DTO for initializing the BacktestingOptionChainProvider"""

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The map file provider instance to us"""
        ...

    @map_file_provider.setter
    def map_file_provider(self, value: QuantConnect.Interfaces.IMapFileProvider) -> None:
        ...

    @property
    def history_provider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """The history provider to use"""
        ...

    @history_provider.setter
    def history_provider(self, value: QuantConnect.Interfaces.IHistoryProvider) -> None:
        ...

    def __init__(self, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, history_provider: QuantConnect.Interfaces.IHistoryProvider) -> None:
        """
        Initializes a new instance of the ChainProviderInitializeParameters class
        
        :param map_file_provider: The map file provider instance to use
        :param history_provider: The history provider to use
        """
        ...


class BacktestingChainProvider(System.Object, metaclass=abc.ABCMeta):
    """Base backtesting cache provider which will source symbols from local zip files"""

    @property
    def map_file_provider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """
        The map file provider instance to use
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def history_provider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """
        The history provider instance to use
        
        
        This codeEntityType is protected.
        """
        ...

    def __init__(self) -> None:
        """
        Initializes a new instance of the BacktestingChainProvider class
        
        
        This codeEntityType is protected.
        """
        ...

    def get_symbols(self, canonical_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Get the contract symbols associated with the given canonical symbol and date
        
        
        This codeEntityType is protected.
        
        :param canonical_symbol: The canonical symbol
        :param date: The date to search for
        """
        ...

    def initialize(self, parameters: QuantConnect.Lean.Engine.DataFeeds.ChainProviderInitializeParameters) -> None:
        """
        Initializes a new instance of the BacktestingChainProvider class
        
        :param parameters: The initialization parameters
        """
        ...

    @staticmethod
    def is_contract_expired(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Helper method to determine if a contract is expired for the requested date
        
        
        This codeEntityType is protected.
        """
        ...


class BacktestingOptionChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingChainProvider, QuantConnect.Interfaces.IOptionChainProvider):
    """An implementation of IOptionChainProvider that reads the list of contracts from open interest zip data files"""

    def get_option_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The option or the underlying symbol to get the option chain for.
        Providing the option allows targeting an option ticker different than the default e.g. SPXW
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class LiveOptionChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingOptionChainProvider):
    """
    An implementation of IOptionChainProvider that fetches the list of contracts
    from the Options Clearing Corporation (OCC) website
    """

    def get_option_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the option chain associated with the underlying Symbol
        
        :param symbol: The option or the underlying symbol to get the option chain for.
        Providing the option allows targetting an option ticker different than the default e.g. SPXW
        :param date: The date to ask for the option contract list for
        :returns: Option chain.
        """
        ...


class InvalidSourceEventArgs(System.EventArgs):
    """Event arguments for the ISubscriptionDataSourceReader.invalid_source event"""

    @property
    def source(self) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source that was considered invalid"""
        ...

    @property
    def exception(self) -> System.Exception:
        """Gets the exception that was encountered"""
        ...

    def __init__(self, source: QuantConnect.Data.SubscriptionDataSource, exception: System.Exception) -> None:
        """
        Initializes a new instance of the InvalidSourceEventArgs class
        
        :param source: The source that was considered invalid
        :param exception: The exception that was encountered
        """
        ...


class ISubscriptionDataSourceReader(metaclass=abc.ABCMeta):
    """
    Represents a type responsible for accepting an input SubscriptionDataSource
    and returning an enumerable of the source's BaseData
    """

    @property
    @abc.abstractmethod
    def invalid_source(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], typing.Any], typing.Any]:
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    @invalid_source.setter
    def invalid_source(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class BaseSubscriptionDataSourceReader(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader, metaclass=abc.ABCMeta):
    """A base class for implementations of the ISubscriptionDataSourceReader"""

    @property
    def is_live_mode(self) -> bool:
        """
        True if we're in live mode, false for backtesting
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def data_cache_provider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """
        The data cache provider to use
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def object_store(self) -> QuantConnect.Interfaces.IObjectStore:
        """
        The object store to use
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def invalid_source(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], typing.Any], typing.Any]:
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    @invalid_source.setter
    def invalid_source(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, is_live_mode: bool, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Creates a new instance
        
        
        This codeEntityType is protected.
        """
        ...

    def create_stream_reader(self, subscription_data_source: QuantConnect.Data.SubscriptionDataSource) -> QuantConnect.Interfaces.IStreamReader:
        """
        Creates a new IStreamReader for the specified subscription_data_source
        
        This codeEntityType is protected.
        
        :param subscription_data_source: The source to produce an IStreamReader for
        :returns: A new instance of IStreamReader to read the source, or null if there was an error.
        """
        ...

    def on_invalid_source(self, source: QuantConnect.Data.SubscriptionDataSource, exception: System.Exception) -> None:
        """
        Event invocator for the invalid_source event
        
        
        This codeEntityType is protected.
        
        :param source: The SubscriptionDataSource that was invalid
        :param exception: The exception if one was raised, otherwise null
        """
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class IndexSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    This ISubscriptionDataSourceReader implementation supports
    the FileFormat.INDEX and IndexedBaseData types.
    Handles the layer of indirection for the index data source and forwards
    the target source to the corresponding ISubscriptionDataSourceReader
    """

    def __init__(self, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool, data_provider: QuantConnect.Interfaces.IDataProvider, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """Creates a new instance of this ISubscriptionDataSourceReader"""
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CreateStreamReaderErrorEventArgs(System.EventArgs):
    """Event arguments for the TextSubscriptionDataSourceReader's CreateStreamReader event"""

    @property
    def date(self) -> datetime.datetime:
        """Gets the date of the source"""
        ...

    @property
    def source(self) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source that caused the error"""
        ...

    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], source: QuantConnect.Data.SubscriptionDataSource) -> None:
        """
        Initializes a new instance of the CreateStreamReaderErrorEventArgs class
        
        :param date: The date of the source
        :param source: The source that cause the error
        """
        ...


class DefaultDataProvider(System.Object, QuantConnect.Interfaces.IDataProvider, System.IDisposable):
    """Default file provider functionality that retrieves data from disc to be used in an algorithm"""

    @property
    def new_data_request(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]:
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    @new_data_request.setter
    def new_data_request(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def dispose(self) -> None:
        """
        The stream created by this type is passed up the stack to the IStreamReader
        The stream is closed when the StreamReader that wraps this stream is disposed
        """
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data from disc to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...

    def on_new_data_request(self, e: QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs) -> None:
        """
        Event invocator for the new_data_request event
        
        
        This codeEntityType is protected.
        """
        ...


class BaseDownloaderDataProvider(QuantConnect.Lean.Engine.DataFeeds.DefaultDataProvider, metaclass=abc.ABCMeta):
    """Base downloader implementation with some helper methods"""

    def download_once(self, key: str, download: typing.Callable[[str], typing.Any]) -> System.IO.Stream:
        """
        Helper method which guarantees each requested key is downloaded only once concurrently if required based on need_to_download
        
        This codeEntityType is protected.
        
        :param key: A string representing where the data is stored
        :param download: The download operation we want to perform once concurrently per key
        :returns: A Stream of the data requested.
        """
        ...

    def get_stream(self, key: str) -> System.IO.Stream:
        """
        Get's the stream for a given file path
        
        
        This codeEntityType is protected.
        """
        ...

    def need_to_download(self, file_path: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        
        This codeEntityType is protected.
        
        :param file_path: File we are looking at
        :returns: True if should download.
        """
        ...


class ApiDataProvider(QuantConnect.Lean.Engine.DataFeeds.BaseDownloaderDataProvider):
    """An instance of the IDataProvider that will download and update data files as needed via QC's Api."""

    def __init__(self) -> None:
        """Initialize a new instance of the ApiDataProvider"""
        ...

    def download_data(self, file_path: str) -> bool:
        """
        Attempt to download data using the Api for and return a FileStream of that data.
        
        
        This codeEntityType is protected.
        
        :param file_path: The path to store the file
        :returns: A FileStream of the data.
        """
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data to be used in an algorithm.
        If file does not exist, an attempt is made to download them from the api
        
        :param key: File path representing where the data requested
        :returns: A Stream of the data requested.
        """
        ...

    def need_to_download(self, file_path: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        
        This codeEntityType is protected.
        
        :param file_path: File we are looking at
        :returns: True if should download.
        """
        ...


class IDataManager(metaclass=abc.ABCMeta):
    """IDataManager is the engines view of the Data Manager."""

    @property
    @abc.abstractmethod
    def universe_selection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Get the universe selection instance"""
        ...


class RealTimeScheduleEventService(System.Object, System.IDisposable):
    """
    Allows to setup a real time scheduled event, internally using a Thread,
    that is guaranteed to trigger at or after the requested time, never before.
    """

    @property
    def new_event(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        """Event fired when the scheduled time is past"""
        ...

    @new_event.setter
    def new_event(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, time_provider: QuantConnect.ITimeProvider) -> None:
        """
        Creates a new instance
        
        :param time_provider: The time provider to use
        """
        ...

    def dispose(self) -> None:
        """Disposes of the underlying Timer instance"""
        ...

    def schedule_event(self, due_time: datetime.timedelta, utc_now: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Schedules a new event
        
        :param due_time: The desired due time
        :param utc_now: Current utc time
        """
        ...


class ReaderErrorEventArgs(System.EventArgs):
    """Event arguments for the TextSubscriptionDataSourceReader.reader_error event."""

    @property
    def line(self) -> str:
        """Gets the line that caused the error"""
        ...

    @property
    def exception(self) -> System.Exception:
        """Gets the exception that was caught"""
        ...

    def __init__(self, line: str, exception: System.Exception) -> None:
        """
        Initializes a new instance of the ReaderErrorEventArgs class
        
        :param line: The line that caused the error
        :param exception: The exception that was caught during the read
        """
        ...


class DataFeedPacket(System.Object):
    """Defines a container type to hold data produced by a data feed subscription"""

    @property
    def security(self) -> QuantConnect.Interfaces.ISecurityPrice:
        """The security"""
        ...

    @property
    def configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """The subscription configuration that produced this data"""
        ...

    @property
    def count(self) -> int:
        """Gets the number of data points held within this packet"""
        ...

    @property
    def data(self) -> typing.List[QuantConnect.Data.BaseData]:
        """The data for the security"""
        ...

    @property
    def is_subscription_removed(self) -> bool:
        """Gets whether or not this packet should be filtered out due to the subscription being removed"""
        ...

    @overload
    def __init__(self, security: QuantConnect.Interfaces.ISecurityPrice, configuration: QuantConnect.Data.SubscriptionDataConfig, is_subscription_removed: QuantConnect.Util.IReadOnlyRef[bool] = None) -> None:
        """
        Initializes a new instance of the DataFeedPacket class
        
        :param security: The security whose data is held in this packet
        :param configuration: The subscription configuration that produced this data
        :param is_subscription_removed: Reference to whether or not the subscription has since been removed, defaults to false
        """
        ...

    @overload
    def __init__(self, security: QuantConnect.Interfaces.ISecurityPrice, configuration: QuantConnect.Data.SubscriptionDataConfig, data: typing.List[QuantConnect.Data.BaseData], is_subscription_removed: QuantConnect.Util.IReadOnlyRef[bool] = None) -> None:
        """
        Initializes a new instance of the DataFeedPacket class
        
        :param security: The security whose data is held in this packet
        :param configuration: The subscription configuration that produced this data
        :param data: The data to add to this packet. The list reference is reused
        internally and NOT copied.
        :param is_subscription_removed: Reference to whether or not the subscription has since been removed, defaults to false
        """
        ...

    def add(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Adds the specified data to this packet
        
        :param data: The data to be added to this packet
        """
        ...


class TimeSlice(System.Object):
    """Represents a grouping of data emitted at a certain time."""

    @property
    def data_point_count(self) -> int:
        """Gets the count of data points in this TimeSlice"""
        ...

    @property
    def time(self) -> datetime.datetime:
        """Gets the UTC time this data was emitted"""
        ...

    @property
    def data(self) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket]:
        """Gets the data in the time slice"""
        ...

    @property
    def slice(self) -> QuantConnect.Data.Slice:
        """Gets the slice that will be used as input for the algorithm"""
        ...

    @property
    def securities_update_data(self) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]]:
        """Gets the data used to update securities"""
        ...

    @property
    def consolidator_update_data(self) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Data.SubscriptionDataConfig]]:
        """Gets the data used to update the consolidators"""
        ...

    @property
    def custom_data(self) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]]:
        """Gets all the custom data in this TimeSlice"""
        ...

    @property
    def security_changes(self) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """Gets the changes to the data subscriptions as a result of universe selection"""
        ...

    @property
    def universe_data(self) -> System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection]:
        """Gets the universe data generated this time step."""
        ...

    @property
    def is_time_pulse(self) -> bool:
        """True indicates this time slice is a time pulse for the algorithm containing no data"""
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data_point_count: int, slice: QuantConnect.Data.Slice, data: typing.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket], securities_update_data: typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]], consolidator_update_data: typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Data.SubscriptionDataConfig]], custom_data: typing.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]], security_changes: QuantConnect.Data.UniverseSelection.SecurityChanges, universe_data: System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection], is_time_pulse: bool = False) -> None:
        """Initializes a new TimeSlice containing the specified data"""
        ...


class ISynchronizer(metaclass=abc.ABCMeta):
    """Interface which provides the data to stream to the algorithm"""

    def stream_data(self, cancellation_token: System.Threading.CancellationToken) -> typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class IDataFeedTimeProvider(metaclass=abc.ABCMeta):
    """Reduced interface which exposes required ITimeProvider for IDataFeed implementations"""

    @property
    @abc.abstractmethod
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider"""
        ...

    @property
    @abc.abstractmethod
    def frontier_time_provider(self) -> QuantConnect.ITimeProvider:
        """Time provider which returns current UTC frontier time"""
        ...


class IDataFeed(metaclass=abc.ABCMeta):
    """Datafeed interface for creating custom datafeed sources."""

    @property
    @abc.abstractmethod
    def is_active(self) -> bool:
        """Public flag indicator that the thread is still busy."""
        ...

    def create_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def exit(self) -> None:
        """External controller calls to signal a terminate of the thread."""
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider, subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, data_feed_time_provider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, data_channel_provider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def remove_subscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...


class DataManager(System.Object, QuantConnect.Interfaces.IAlgorithmSubscriptionManager, QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, QuantConnect.Lean.Engine.DataFeeds.IDataManager):
    """DataManager will manage the subscriptions for both the DataFeeds and the SubscriptionManager"""

    @property
    def subscription_added(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when a new subscription is added"""
        ...

    @subscription_added.setter
    def subscription_added(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    @property
    def subscription_removed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when an existing subscription is removed"""
        ...

    @subscription_removed.setter
    def subscription_removed(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    @property
    def data_feed_subscriptions(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionCollection:
        """Gets the data feed subscription collection"""
        ...

    @property
    def subscription_manager_subscriptions(self) -> typing.Iterable[QuantConnect.Data.SubscriptionDataConfig]:
        """Gets all the current data config subscriptions that are being processed for the SubscriptionManager"""
        ...

    @property
    def available_data_types(self) -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, typing.List[QuantConnect.TickType]]:
        """The different TickType each SecurityType supports"""
        ...

    @property
    def universe_selection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Get the universe selection instance"""
        ...

    def __init__(self, data_feed: QuantConnect.Lean.Engine.DataFeeds.IDataFeed, universe_selection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, algorithm: QuantConnect.Interfaces.IAlgorithm, time_keeper: QuantConnect.Interfaces.ITimeKeeper, market_hours_database: QuantConnect.Securities.MarketHoursDatabase, live_mode: bool, registered_types_provider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, data_permission_manager: QuantConnect.Interfaces.IDataPermissionManager) -> None:
        """Creates a new instance of the DataManager"""
        ...

    @overload
    def add(self, data_type: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, extended_market_hours: bool = False, is_filtered_subscription: bool = True, is_internal_feed: bool = False, is_custom_data: bool = False, data_normalization_mode: QuantConnect.DataNormalizationMode = ..., data_mapping_mode: QuantConnect.DataMappingMode = ..., contract_depth_offset: int = 0) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data type to use.
        If the config already existed will return existing instance instead
        """
        ...

    @overload
    def add(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], resolution: typing.Optional[QuantConnect.Resolution] = None, fill_forward: bool = True, extended_market_hours: bool = False, is_filtered_subscription: bool = True, is_internal_feed: bool = False, is_custom_data: bool = False, subscription_data_types: typing.List[System.Tuple[typing.Type, QuantConnect.TickType]] = None, data_normalization_mode: QuantConnect.DataNormalizationMode = ..., data_mapping_mode: QuantConnect.DataMappingMode = ..., contract_depth_offset: int = 0) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data types to use.
         If the config already existed will return existing instance instead
        """
        ...

    def add_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a new Subscription to provide data for the specified security.
        
        :param request: Defines the SubscriptionRequest to be added
        :returns: True if the subscription was created and added successfully, false otherwise.
        """
        ...

    def get_subscription_data_configs(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security] = None, include_internal_configs: bool = False) -> typing.List[QuantConnect.Data.SubscriptionDataConfig]:
        """Gets a list of all registered SubscriptionDataConfig for a given Symbol"""
        ...

    def lookup_subscription_config_data_types(self, symbol_security_type: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, is_canonical: bool) -> typing.List[System.Tuple[typing.Type, QuantConnect.TickType]]:
        """
        Get the data feed types for a given SecurityTypeResolution
        
        :param symbol_security_type: The SecurityType used to determine the types
        :param resolution: The resolution of the data requested
        :param is_canonical: Indicates whether the security is Canonical (future and options)
        :returns: Types that should be added to the SubscriptionDataConfig.
        """
        ...

    def remove_all_subscriptions(self) -> None:
        """Will remove all current Subscription"""
        ...

    def remove_subscription(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes the Subscription, if it exists
        
        :param configuration: The SubscriptionDataConfig of the subscription to remove
        :param universe: Universe requesting to remove Subscription.
        Default value, null, will remove all universes
        :returns: True if the subscription was successfully removed, false otherwise.
        """
        ...

    def subscription_manager_count(self) -> int:
        """Returns the amount of data config subscriptions processed for the SubscriptionManager"""
        ...

    def subscription_manager_get_or_add(self, new_config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Gets existing or adds new SubscriptionDataConfig
        
        :returns: Returns the SubscriptionDataConfig instance used.
        """
        ...


class PendingRemovalsManager(System.Object):
    """Helper class used to managed pending security removals UniverseSelection"""

    class RemovedMember(System.Object):
        """Helper class used to report removed universe members"""

        @property
        def universe(self) -> QuantConnect.Data.UniverseSelection.Universe:
            """Universe the security was removed from"""
            ...

        @property
        def security(self) -> QuantConnect.Securities.Security:
            """Security that is removed"""
            ...

        def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, security: QuantConnect.Securities.Security) -> None:
            """
            Initialize a new instance of RemovedMember
            
            :param universe: universe the security was removed from
            :param security: security that is removed
            """
            ...

    @property
    def pending_removals(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Data.UniverseSelection.Universe, typing.List[QuantConnect.Data.UniverseSelection.Universe.Member]]:
        """Current pending removals"""
        ...

    def __init__(self, order_provider: QuantConnect.Securities.IOrderProvider) -> None:
        """
        Create a new instance
        
        :param order_provider: The order provider used to determine if it is safe to remove a security
        """
        ...

    def check_pending_removals(self, selected_symbols: System.Collections.Generic.HashSet[QuantConnect.Symbol], current_universe: QuantConnect.Data.UniverseSelection.Universe) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.PendingRemovalsManager.RemovedMember]:
        """
        Will check pending security removals
        
        :param selected_symbols: Currently selected symbols
        :param current_universe: Current universe
        :returns: The members to be removed.
        """
        ...

    @overload
    def is_pending_for_removal(self, security: QuantConnect.Securities.Security, is_internal: bool) -> bool:
        """
        Will check if the security is pending for removal
        
        :param security: The security
        :param is_internal: Whether it's an internal subscription
        :returns: Whether the security is pending for removal.
        """
        ...

    @overload
    def is_pending_for_removal(self, member: QuantConnect.Data.UniverseSelection.Universe.Member) -> bool:
        """
        Will check if the member is pending for removal
        
        :param member: The universe member
        :returns: Whether the security is pending for removal.
        """
        ...

    def try_remove_member(self, member: QuantConnect.Data.UniverseSelection.Universe.Member, universe: QuantConnect.Data.UniverseSelection.Universe) -> typing.List[QuantConnect.Lean.Engine.DataFeeds.PendingRemovalsManager.RemovedMember]:
        """
        Will determine if the Security can be removed.
        If it can be removed will add it to pending_removals
        
        :param member: The security to remove
        :param universe: The universe which the security is a member of
        :returns: The member to remove.
        """
        ...


class ZipDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """File provider implements optimized zip archives caching facility. Cache is thread safe."""

    @property
    def is_data_ephemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    def __init__(self, data_provider: QuantConnect.Interfaces.IDataProvider, is_data_ephemeral: bool = True, cache_timer: float = ...) -> None:
        """Constructor that sets the IDataProvider used to retrieve data"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """Does not attempt to retrieve any data"""
        ...

    def get_zip_entries(self, zip_file: str) -> typing.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def store(self, key: str, data: typing.List[int]) -> None:
        """
        Store the data in the cache.
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data as a byte array
        """
        ...


class BacktestingFutureChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingChainProvider, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that reads the list of contracts from open interest zip data files"""

    def get_future_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...

    @staticmethod
    def get_symbol(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Symbol:
        """
        Helper method to get the symbol to use
        
        
        This codeEntityType is protected.
        """
        ...


class CurrencySubscriptionDataConfigManager(System.Object):
    """
    Helper class to keep track of required internal currency SubscriptionDataConfig.
    This class is used by the UniverseSelection
    """

    def __init__(self, cash_book: QuantConnect.Securities.CashBook, security_manager: QuantConnect.Securities.SecurityManager, subscription_manager: QuantConnect.Data.SubscriptionManager, security_service: QuantConnect.Interfaces.ISecurityService, default_resolution: QuantConnect.Resolution) -> None:
        """
        Creates a new instance
        
        :param cash_book: The cash book instance
        :param security_manager: The SecurityManager, required by the cash book for creating new securities
        :param subscription_manager: The SubscriptionManager, required by the cash book for creating new subscription data configs
        :param security_service: The SecurityService, required by the cash book for creating new securities
        :param default_resolution: The default resolution to use for the internal subscriptions
        """
        ...

    def ensure_currency_subscription_data_configs(self, security_changes: QuantConnect.Data.UniverseSelection.SecurityChanges, brokerage_model: QuantConnect.Brokerages.IBrokerageModel) -> None:
        """Checks the current SubscriptionDataConfig and adds new necessary currency pair feeds to provide real time conversion data"""
        ...

    def get_pending_subscription_data_configs(self) -> typing.Iterable[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Will return any pending internal currency SubscriptionDataConfig and remove them as pending.
        
        :returns: Will return the SubscriptionDataConfig to be added.
        """
        ...

    def get_subscription_data_config_to_remove(self, added_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Will verify if there are any SubscriptionDataConfig to be removed
        for a given added Symbol.
        
        :param added_symbol: The symbol that was added to the data feed system
        :returns: The SubscriptionDataConfig to be removed, null if none.
        """
        ...

    def update_pending_subscription_data_configs(self, brokerage_model: QuantConnect.Brokerages.IBrokerageModel) -> bool:
        """
        Will update pending currency SubscriptionDataConfig
        
        :returns: True when there are pending currency subscriptions get_pending_subscription_data_configs.
        """
        ...


class PredicateTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """
    Will generate time steps around the desired ITimeProvider
    Provided step evaluator should return true when the next time step
    is valid and time can advance
    """

    def __init__(self, underlying_time_provider: QuantConnect.ITimeProvider, custom_step_evaluator: typing.Callable[[datetime.datetime], bool]) -> None:
        """
        Creates a new instance
        
        :param underlying_time_provider: The timer provider instance to wrap
        :param custom_step_evaluator: Function to evaluate whether or not
        to advance time. Should return true if provided DateTime is a
        valid new next time. False will avoid time advancing
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """Gets the current utc time step"""
        ...


class DownloaderDataProvider(QuantConnect.Lean.Engine.DataFeeds.BaseDownloaderDataProvider):
    """Data provider which downloads data using an IDataDownloader or IBrokerage implementation"""

    @overload
    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    @overload
    def __init__(self, data_downloader: QuantConnect.IDataDownloader) -> None:
        """Creates a new instance using a target data downloader used for testing"""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Determines if it should downloads new data and retrieves data from disc
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...

    @staticmethod
    def filter_and_group_download_data_by_symbol(download_data: typing.List[QuantConnect.Data.BaseData], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], data_type: typing.Type, exchange_time_zone: typing.Any, data_time_zone: typing.Any, downloader_start_time_utc: typing.Union[datetime.datetime, datetime.date], downloader_end_time_utc: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[System.Linq.IGrouping[QuantConnect.Symbol, QuantConnect.Data.BaseData]]:
        """
        Filters and groups the provided download data by symbol, based on specified criteria.
        
        :param download_data: The collection of download data to process.
        :param symbol: The symbol to filter the data for.
        :param data_type: The type of data to filter for.
        :param exchange_time_zone: The time zone of the exchange.
        :param data_time_zone: The desired time zone for the data.
        :param downloader_start_time_utc: The start time of data downloading in UTC.
        :param downloader_end_time_utc: The end time of data downloading in UTC.
        :returns: An enumerable collection of groupings of download data, grouped by symbol.
        """
        ...

    def get_downloaded_data(self, downloader_data_parameters: typing.List[QuantConnect.DataDownloaderGetParameters], symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], exchange_time_zone: typing.Any, data_time_zone: typing.Any, data_type: typing.Type) -> typing.Iterable[System.Linq.IGrouping[QuantConnect.Symbol, QuantConnect.Data.BaseData]]:
        """
        Retrieves downloaded data grouped by symbol based on IDownloadProvider.
        
        :param downloader_data_parameters: Parameters specifying the data to be retrieved.
        :param symbol: Represents a unique security identifier, generate by ticker name.
        :param exchange_time_zone: The time zone of the exchange where the symbol is traded.
        :param data_time_zone: The time zone in which the data is represented.
        :param data_type: The type of data to be retrieved. (e.g. Data.Market.TradeBar)
        :returns: An IEnumerable containing groups of data grouped by symbol. Each group contains data related to a specific symbol.
        """
        ...

    def get_stream(self, key: str) -> System.IO.Stream:
        """
        Get's the stream for a given file path
        
        
        This codeEntityType is protected.
        """
        ...

    def need_to_download(self, file_path: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        
        This codeEntityType is protected.
        
        :param file_path: File we are looking at
        :returns: True if should download.
        """
        ...


class SingleEntryDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """
    Default implementation of the IDataCacheProvider
    Does not cache data.  If the data is a zip, the first entry is returned
    """

    @property
    def is_data_ephemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    def __init__(self, data_provider: QuantConnect.Interfaces.IDataProvider, is_data_ephemeral: bool = True) -> None:
        """Constructor that takes the IDataProvider to be used to retrieve data"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Fetch data from the cache
        
        :param key: A string representing the key of the cached data
        :returns: An Stream of the cached data.
        """
        ...

    def get_zip_entries(self, zip_file: str) -> typing.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def store(self, key: str, data: typing.List[int]) -> None:
        """
        Not implemented
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data to cache as a byte array
        """
        ...


class TextSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    Provides an implementations of ISubscriptionDataSourceReader that uses the
    BaseData.reader(SubscriptionDataConfig,string,DateTime,bool)
    method to read lines of text from a SubscriptionDataSource
    """

    @property
    def config(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        The requested subscription configuration
        
        
        This codeEntityType is protected.
        """
        ...

    @config.setter
    def config(self, value: QuantConnect.Data.SubscriptionDataConfig) -> None:
        ...

    @property
    def reader_error(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], typing.Any], typing.Any]:
        """
        Event fired when an exception is thrown during a call to
        BaseData.reader(SubscriptionDataConfig,string,DateTime,bool)
        """
        ...

    @reader_error.setter
    def reader_error(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Initializes a new instance of the TextSubscriptionDataSourceReader class
        
        :param data_cache_provider: This provider caches files if needed
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param is_live_mode: True if we're in live mode, false for backtesting
        :param object_store: The object storage for data persistence.
        """
        ...

    @staticmethod
    def clear_cache() -> None:
        """
        Will clear the data cache.
        Used for testing different time zones for the same data set and allow a clean fresh start for each backtest
        """
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...

    @staticmethod
    def set_cache_size(mega_bytes_to_use: int) -> None:
        """Set the cache size to use"""
        ...


class ManualTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """
    Provides an implementation of ITimeProvider that can be
    manually advanced through time
    """

    @overload
    def __init__(self, set_current_time_time_zone: typing.Any = None) -> None:
        """
        Initializes a new instance of the ManualTimeProvider
        
        :param set_current_time_time_zone: Specify to use this time zone when calling set_current_time,
        leave null for the default of TimeZones.UTC
        """
        ...

    @overload
    def __init__(self, current_time: typing.Union[datetime.datetime, datetime.date], set_current_time_time_zone: typing.Any = None) -> None:
        """
        Initializes a new instance of the ManualTimeProvider class
        
        :param current_time: The current time in the specified time zone, if the time zone is
        null then the time is interpreted as being in TimeZones.UTC
        :param set_current_time_time_zone: Specify to use this time zone when calling set_current_time,
        leave null for the default of TimeZones.UTC
        """
        ...

    def advance(self, span: datetime.timedelta) -> None:
        """
        Advances the current time by the specified span
        
        :param span: The amount of time to advance the current time by
        """
        ...

    def advance_seconds(self, seconds: float) -> None:
        """
        Advances the current time by the specified number of seconds
        
        :param seconds: The number of seconds to advance the current time by
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...

    def set_current_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the current time interpeting the specified time as a local time
        using the time zone used at instatiation.
        
        :param time: The local time to set the current time time, will be
        converted into UTC
        """
        ...

    def set_current_time_utc(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the current time interpreting the specified time as a UTC time
        
        :param time: The current time in UTC
        """
        ...


class PrecalculatedSubscriptionData(QuantConnect.Lean.Engine.DataFeeds.SubscriptionData):
    """Store data both raw and adjusted and the time at which it should be synchronized"""

    @property
    def data(self) -> QuantConnect.Data.BaseData:
        """Gets the data"""
        ...

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, raw_data: QuantConnect.Data.BaseData, normalized_data: QuantConnect.Data.BaseData, normalization_mode: QuantConnect.DataNormalizationMode, emit_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the PrecalculatedSubscriptionData class
        
        :param configuration: The subscription's configuration
        :param raw_data: The base data
        :param normalized_data: The normalized calculated based on raw data
        :param normalization_mode: Specifies how data is normalized
        :param emit_time_utc: The emit time for the data
        """
        ...


class DataPermissionManager(System.Object, QuantConnect.Interfaces.IDataPermissionManager):
    """Entity in charge of handling data permissions"""

    @property
    def data_channel_provider(self) -> QuantConnect.Interfaces.IDataChannelProvider:
        """The data channel provider instance"""
        ...

    def __init__(self) -> None:
        ...

    def assert_configuration(self, subscription_request: QuantConnect.Data.SubscriptionDataConfig, start_time_local: typing.Union[datetime.datetime, datetime.date], end_time_local: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Will assert the requested configuration is valid for the current job
        
        :param subscription_request: The data subscription configuration to assert
        :param start_time_local: The start time of this request
        :param end_time_local: The end time of this request
        """
        ...

    def initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initialize the data permission manager
        
        :param job: The job packet
        """
        ...


class ISubscriptionSynchronizer(metaclass=abc.ABCMeta):
    """Provides the ability to synchronize subscriptions into time slices"""

    @property
    @abc.abstractmethod
    def subscription_finished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when a subscription is finished"""
        ...

    @subscription_finished.setter
    def subscription_finished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    def sync(self, subscriptions: typing.List[QuantConnect.Lean.Engine.DataFeeds.Subscription], cancellation_token: System.Threading.CancellationToken) -> typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """
        Syncs the specified subscriptions. The frontier time used for synchronization is
        managed internally and dependent upon previous synchronization operations.
        
        :param subscriptions: The subscriptions to sync
        :param cancellation_token: The cancellation token to stop enumeration
        """
        ...


class TimeSliceFactory(System.Object):
    """Instance base class that will provide methods for creating new TimeSlice"""

    def __init__(self, time_zone: typing.Any) -> None:
        """
        Creates a new instance
        
        :param time_zone: The time zone required for computing algorithm and slice time
        """
        ...

    def create(self, utc_date_time: typing.Union[datetime.datetime, datetime.date], data: typing.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, universe_data: System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection]) -> QuantConnect.Lean.Engine.DataFeeds.TimeSlice:
        """
        Creates a new TimeSlice for the specified time using the specified data
        
        :param utc_date_time: The UTC frontier date time
        :param data: The data in this TimeSlice
        :param changes: The new changes that are seen in this time slice as a result of universe selection
        :param universe_data: 
        :returns: A new TimeSlice containing the specified data.
        """
        ...

    def create_time_pulse(self, utc_date_time: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Lean.Engine.DataFeeds.TimeSlice:
        """
        Creates a new empty TimeSlice to be used as a time pulse
        
        :param utc_date_time: The UTC frontier date time
        :returns: A new TimeSlice time pulse.
        """
        ...


class SubscriptionSynchronizer(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISubscriptionSynchronizer, QuantConnect.ITimeProvider):
    """Provides the ability to synchronize subscriptions into time slices"""

    @property
    def subscription_finished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]:
        """Event fired when a Subscription is finished"""
        ...

    @subscription_finished.setter
    def subscription_finished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, universe_selection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, performance_tracking_tool: QuantConnect.Util.PerformanceTrackingTool) -> None:
        """
        Initializes a new instance of the SubscriptionSynchronizer class
        
        :param universe_selection: The universe selection instance used to handle universe
        selection subscription output
        :returns: A time slice for the specified frontier time.
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """Returns the current UTC frontier time"""
        ...

    def on_subscription_finished(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Event invocator for the subscription_finished event
        
        
        This codeEntityType is protected.
        """
        ...

    def set_time_provider(self, time_provider: QuantConnect.ITimeProvider) -> None:
        """
        Sets the time provider. If already set will throw.
        
        :param time_provider: The time provider, used to obtain the current frontier UTC value
        """
        ...

    def set_time_slice_factory(self, time_slice_factory: QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory) -> None:
        """
        Sets the TimeSliceFactory instance to use
        
        :param time_slice_factory: Used to create the new TimeSlice
        """
        ...

    def sync(self, subscriptions: typing.List[QuantConnect.Lean.Engine.DataFeeds.Subscription], cancellation_token: System.Threading.CancellationToken) -> typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """
        Syncs the specified subscriptions. The frontier time used for synchronization is
        managed internally and dependent upon previous synchronization operations.
        
        :param subscriptions: The subscriptions to sync
        :param cancellation_token: The cancellation token to stop enumeration
        """
        ...


class DataQueueHandlerManager(System.Object, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IDataQueueUniverseProvider):
    """This is an implementation of IDataQueueHandler used to handle multiple live datafeeds"""

    @property
    def frontier_time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Frontier time provider to use
        
        
        This codeEntityType is protected.
        """
        ...

    @frontier_time_provider.setter
    def frontier_time_provider(self, value: QuantConnect.ITimeProvider) -> None:
        ...

    @property
    def data_handlers(self) -> typing.List[QuantConnect.Interfaces.IDataQueueHandler]:
        """
        Collection of data queue handles being used
        
        
        This codeEntityType is protected.
        """
        ...

    @data_handlers.setter
    def data_handlers(self, value: typing.List[QuantConnect.Interfaces.IDataQueueHandler]) -> None:
        ...

    @property
    def has_universe_provider(self) -> bool:
        """True if the composite queue handler has any IDataQueueUniverseProvider instance"""
        ...

    @property
    def unsupported_configuration(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.SubscriptionDataConfig], typing.Any], typing.Any]:
        """Event triggered when an unsupported configuration is detected"""
        ...

    @unsupported_configuration.setter
    def unsupported_configuration(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.SubscriptionDataConfig], typing.Any], typing.Any]) -> None:
        ...

    @property
    def is_connected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    def __init__(self, settings: QuantConnect.Interfaces.IAlgorithmSettings) -> None:
        """Creates a new instance"""
        ...

    def can_perform_selection(self) -> bool:
        """
        Returns whether selection can take place or not.
        
        :returns: True if selection can take place.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def initialize_frontier_time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Creates the frontier time provider instance
        
        
        This codeEntityType is protected.
        """
        ...

    def lookup_symbols(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], include_expired: bool, security_currency: str = None) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Method returns a collection of Symbols that are available at the data source.
        
        :param symbol: Symbol to lookup
        :param include_expired: Include expired contracts
        :param security_currency: Expected security currency(if any)
        :returns: Enumerable of Symbols, that are associated with the provided Symbol.
        """
        ...

    def set_job(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], typing.Any]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Subscribe to the specified configuration
        
        :param data_config: defines the parameters to subscribe to a data feed
        :param new_data_available_handler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Removes the specified configuration
        
        :param data_config: Subscription config to be removed
        """
        ...


class LiveTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """Live time provide which supports an initial warmup period using the given time provider SubscriptionFrontierTimeProvider, used by the LiveSynchronizer"""

    def __init__(self, real_time: QuantConnect.ITimeProvider) -> None:
        """
        Creates a new instance
        
        :param real_time: Real time provider
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...

    def initialize(self, warmup_time_provider: QuantConnect.ITimeProvider) -> None:
        """
        Fully initializes this instance providing the initial warmup time provider to use
        
        :param warmup_time_provider: The warmup provider to use
        """
        ...


class LiveFutureChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingFutureChainProvider):
    """
    An implementation of IFutureChainProvider that fetches the list of contracts
    from an external source
    """

    def get_future_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class FileSystemDataFeed(System.Object, QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """Historical datafeed stream reader for processing files on a local disk."""

    @property
    def is_active(self) -> bool:
        """Flag indicating the hander thread is completely finished and ready to dispose."""
        ...

    def add_schedule_wrapper(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, underlying: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], time_provider: QuantConnect.ITimeProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Returns a scheduled enumerator from the given arguments. It can also return the given underlying enumerator
        
        
        This codeEntityType is protected.
        """
        ...

    def configure_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, aggregate: bool, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], fill_forward_resolution: typing.Optional[QuantConnect.Resolution], last_point_tracker: QuantConnect.Lean.Engine.DataFeeds.Enumerators.LastPointTracker, is_warm_up_enumerator: bool = False) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Configure the enumerator with aggregation/fill-forward/filter behaviors. Returns new instance if re-configured
        
        
        This codeEntityType is protected.
        """
        ...

    def configure_last_point_tracker(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], last_point_tracker: QuantConnect.Lean.Engine.DataFeeds.Enumerators.LastPointTracker, is_warm_up_enumerator: bool) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Configures the enumerator to track the last data point, if requested, and if this is a warmup enumerator
        
        
        This codeEntityType is protected.
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, fill_forward_resolution: typing.Optional[QuantConnect.Resolution] = None, last_point_tracker: QuantConnect.Lean.Engine.DataFeeds.Enumerators.LastPointTracker = None, is_warm_up: bool = False) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a file based data enumerator for the given subscription request
        
        
        This codeEntityType is protected.
        """
        ...

    def create_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def create_universe_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a universe enumerator from the Subscription request, the underlying enumerator func and the fill forward resolution (in some cases)
        
        
        This codeEntityType is protected.
        """
        ...

    def exit(self) -> None:
        """Send an exit signal to the thread."""
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider, subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, data_feed_time_provider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, data_channel_provider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def remove_subscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...

    def try_add_fill_forward_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], fill_forward: bool, fill_forward_resolution: typing.Optional[QuantConnect.Resolution], last_point_tracker: QuantConnect.Lean.Engine.DataFeeds.Enumerators.LastPointTracker = None) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Will add a fill forward enumerator if requested
        
        
        This codeEntityType is protected.
        """
        ...


class DataChannelProvider(System.Object, QuantConnect.Interfaces.IDataChannelProvider):
    """Specifies data channel settings"""

    def initialize(self, packet: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initializes the instance with an algorithm node packet
        
        :param packet: Algorithm node packet
        """
        ...

    @staticmethod
    def is_streaming_type(configuration: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Returns true if the data type for the given subscription configuration supports streaming
        
        
        This codeEntityType is protected.
        """
        ...

    def should_stream_subscription(self, config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """True if this subscription request should be streamed"""
        ...


class SubscriptionDataSourceReader(System.Object):
    """Provides a factory method for creating ISubscriptionDataSourceReader instances"""

    @staticmethod
    def check_remote_file_cache() -> None:
        """Creates cache directory if not existing and deletes old files from the cache"""
        ...

    @staticmethod
    def for_source(source: QuantConnect.Data.SubscriptionDataSource, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool, factory: QuantConnect.Data.BaseData, data_provider: QuantConnect.Interfaces.IDataProvider, object_store: QuantConnect.Interfaces.IObjectStore) -> QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader:
        """
        Creates a new ISubscriptionDataSourceReader capable of handling the specified source
        
        :param source: The subscription data source to create a factory for
        :param data_cache_provider: Used to cache data
        :param config: The configuration of the subscription
        :param date: The date to be processed
        :param is_live_mode: True for live mode, false otherwise
        :param factory: The base data instance factory
        :param data_provider: The data provider to use
        :returns: A new ISubscriptionDataSourceReader that can read the specified source.
        """
        ...


class UpdateData(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_UpdateData_T], System.Object):
    """
    Transport type for algorithm update data. This is intended to provide a
    list of base data used to perform updates against the specified target
    """

    @property
    def contains_fill_forward_data(self) -> typing.Optional[bool]:
        """Flag indicating whether data contains any fill forward bar or not"""
        ...

    @property
    def target(self) -> QuantConnect_Lean_Engine_DataFeeds_UpdateData_T:
        """The target, such as a security or subscription data config"""
        ...

    @property
    def data(self) -> typing.Sequence[QuantConnect.Data.BaseData]:
        """The data used to update the target"""
        ...

    @property
    def data_type(self) -> typing.Type:
        """The type of data in the data list"""
        ...

    @property
    def is_internal_config(self) -> bool:
        """
        True if this update data corresponds to an internal subscription
        such as currency or security benchmark
        """
        ...

    def __init__(self, target: QuantConnect_Lean_Engine_DataFeeds_UpdateData_T, data_type: typing.Type, data: typing.Sequence[QuantConnect.Data.BaseData], is_internal_config: bool, contains_fill_forward_data: typing.Optional[bool] = None) -> None:
        """
        Initializes a new instance of the UpdateData{T} class
        
        :param target: The end consumer/user of the dat
        :param data_type: The type of data in the list
        :param data: The update data
        :param is_internal_config: True if this update data corresponds to an internal subscription
        such as currency or security benchmark
        :param contains_fill_forward_data: True if this update data contains fill forward bars
        """
        ...


class BaseDataCollectionAggregatorReader(QuantConnect.Lean.Engine.DataFeeds.TextSubscriptionDataSourceReader):
    """Data source reader that will aggregate data points into a base data collection"""

    def __init__(self, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Initializes a new instance of the TextSubscriptionDataSourceReader class
        
        :param data_cache_provider: This provider caches files if needed
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param is_live_mode: True if we're in live mode, false for backtesting
        :param object_store: The object storage for data persistence
        """
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CompositeDataProvider(System.Object, QuantConnect.Interfaces.IDataProvider):
    """This data provider will wrap and use multiple data providers internally in the provided order"""

    @property
    def new_data_request(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]:
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    @new_data_request.setter
    def new_data_request(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self) -> None:
        """Creates a new instance and initialize data providers used"""
        ...

    def fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...


class Synchronizer(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISynchronizer, QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, System.IDisposable):
    """Implementation of the ISynchronizer interface which provides the mechanism to stream data to the algorithm"""

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        
        This codeEntityType is protected.
        """
        ...

    @algorithm.setter
    def algorithm(self, value: QuantConnect.Interfaces.IAlgorithm) -> None:
        ...

    @property
    def subscription_manager(self) -> QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager:
        """
        The subscription manager
        
        
        This codeEntityType is protected.
        """
        ...

    @subscription_manager.setter
    def subscription_manager(self, value: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        ...

    @property
    def subscription_synchronizer(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionSynchronizer:
        """
        The subscription synchronizer
        
        
        This codeEntityType is protected.
        """
        ...

    @subscription_synchronizer.setter
    def subscription_synchronizer(self, value: QuantConnect.Lean.Engine.DataFeeds.SubscriptionSynchronizer) -> None:
        ...

    @property
    def time_slice_factory(self) -> QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory:
        """
        The time slice factory
        
        
        This codeEntityType is protected.
        """
        ...

    @time_slice_factory.setter
    def time_slice_factory(self, value: QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory) -> None:
        ...

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider, only valid for live trading see LiveSynchronizer"""
        ...

    @property
    def frontier_time_provider(self) -> QuantConnect.ITimeProvider:
        """Time provider which returns current UTC frontier time"""
        ...

    def dispose(self) -> None:
        """Free resources"""
        ...

    def get_time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Gets the ITimeProvider to use. By default this will load the
        RealTimeProvider for live mode, else SubscriptionFrontierTimeProvider
        
        This codeEntityType is protected.
        
        :returns: The ITimeProvider to use.
        """
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, data_feed_subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, performance_tracking_tool: QuantConnect.Util.PerformanceTrackingTool) -> None:
        """Initializes the instance of the Synchronizer class"""
        ...

    def post_initialize(self) -> None:
        """
        Performs additional initialization steps after algorithm initialization
        
        
        This codeEntityType is protected.
        """
        ...

    def stream_data(self, cancellation_token: System.Threading.CancellationToken) -> typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class SubscriptionUtils(System.Object):
    """Utilities related to data Subscription"""

    @staticmethod
    def create(request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], daily_strict_end_time_enabled: bool) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new Subscription which will directly consume the provided enumerator
        
        :param request: The subscription data request
        :param enumerator: The data enumerator stack
        :returns: A new subscription instance ready to consume.
        """
        ...

    @staticmethod
    def create_and_schedule_worker(request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, enable_price_scale: bool, daily_strict_end_time_enabled: bool) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Setups a new Subscription which will consume a blocking EnqueueableEnumerator{T}
        that will be feed by a worker task
        
        :param request: The subscription data request
        :param enumerator: The data enumerator stack
        :param factor_file_provider: The factor file provider
        :param enable_price_scale: Enables price factoring
        :returns: A new subscription instance ready to consume.
        """
        ...


class ZipEntryNameSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """Provides an implementation of ISubscriptionDataSourceReader that reads zip entry names"""

    def __init__(self, data_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool) -> None:
        """
        Initializes a new instance of the ZipEntryNameSubscriptionDataSourceReader class
        
        :param data_provider: Used to fetch data
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param is_live_mode: True if we're in live mode, false for backtesting
        """
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CachingOptionChainProvider(System.Object, QuantConnect.Interfaces.IOptionChainProvider):
    """An implementation of IOptionChainProvider that will cache by date option contracts returned by another option chain provider."""

    def __init__(self, option_chain_provider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        """
        Initializes a new instance of the CachingOptionChainProvider class
        
        :param option_chain_provider: 
        """
        ...

    def get_option_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The option or the underlying symbol to get the option chain for.
        Providing the option allows targetting an option ticker different than the default e.g. SPXW
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class BaseDataExchange(System.Object):
    """Provides a means of distributing output from enumerators from a dedicated separate thread"""

    class EnumeratorHandler(System.Object):
        """Handler used to manage a single enumerator's move next/end of stream behavior"""

        @property
        def enumerator_finished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], typing.Any], typing.Any]:
            """Event fired when MoveNext returns false"""
            ...

        @enumerator_finished.setter
        def enumerator_finished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], typing.Any], typing.Any]) -> None:
            ...

        @property
        def symbol(self) -> QuantConnect.Symbol:
            """A unique symbol used to identify this enumerator"""
            ...

        @property
        def enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
            """The enumerator this handler handles"""
            ...

        def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], should_move_next: typing.Callable[[], bool] = None, handle_data: typing.Callable[[QuantConnect.Data.BaseData], typing.Any] = None) -> None:
            """
            Initializes a new instance of the EnumeratorHandler class
            
            :param symbol: The symbol to identify this enumerator
            :param enumerator: The enumeator this handler handles
            :param should_move_next: Predicate function used to determine if we should call move next
            on the symbol's enumerator
            :param handle_data: Handler for data if HandlesData=true
            """
            ...

        def handle_data(self, data: QuantConnect.Data.BaseData) -> None:
            """
            Handles the specified data.
            
            :param data: The data to be handled
            """
            ...

        def on_enumerator_finished(self) -> None:
            """Event invocator for the enumerator_finished event"""
            ...

        def should_move_next(self) -> bool:
            """Returns true if this enumerator should move next"""
            ...

    @property
    def sleep_interval(self) -> int:
        """Gets or sets how long this thread will sleep when no data is available"""
        ...

    @sleep_interval.setter
    def sleep_interval(self, value: int) -> None:
        ...

    @property
    def name(self) -> str:
        """Gets a name for this exchange"""
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the BaseDataExchange
        
        :param name: A name for this exchange
        """
        ...

    @overload
    def add_enumerator(self, handler: QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler) -> None:
        """
        Adds the enumerator to this exchange. If it has already been added
        then it will remain registered in the exchange only once
        
        :param handler: The handler to use when this symbol's data is encountered
        """
        ...

    @overload
    def add_enumerator(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], should_move_next: typing.Callable[[], bool] = None, enumerator_finished: typing.Callable[[QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], typing.Any] = None, handle_data: typing.Callable[[QuantConnect.Data.BaseData], typing.Any] = None) -> None:
        """
        Adds the enumerator to this exchange. If it has already been added
        then it will remain registered in the exchange only once
        
        :param symbol: A unique symbol used to identify this enumerator
        :param enumerator: The enumerator to be added
        :param should_move_next: Function used to determine if move next should be called on this
        enumerator, defaults to always returning true
        :param enumerator_finished: Delegate called when the enumerator move next returns false
        :param handle_data: Handler for data if HandlesData=true
        """
        ...

    def remove_enumerator(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler:
        """
        Removes and returns enumerator handler with the specified symbol.
        The removed handler is returned, null if not found
        """
        ...

    def set_error_handler(self, is_fatal_error: typing.Callable[[System.Exception], bool]) -> None:
        """
        Sets the specified function as the error handler. This function
        returns true if it is a fatal error and queue consumption should
        cease.
        
        :param is_fatal_error: The error handling function to use when an
        error is encountered during queue consumption. Returns true if queue
        consumption should be stopped, returns false if queue consumption should
        continue
        """
        ...

    def start(self) -> None:
        """
        Begins consumption of the wrapped IDataQueueHandler on
        a separate thread
        """
        ...

    def stop(self) -> None:
        """Ends consumption of the wrapped IDataQueueHandler"""
        ...


class LiveSynchronizer(QuantConnect.Lean.Engine.DataFeeds.Synchronizer):
    """Implementation of the ISynchronizer interface which provides the mechanism to stream live data to the algorithm"""

    BATCHING_DELAY: int = ...
    """Consumer batching timeout in ms"""

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider"""
        ...

    def dispose(self) -> None:
        """Free resources"""
        ...

    def get_pulse_due_time(self, now: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Will return the amount of milliseconds that are missing for the next time pulse
        
        
        This codeEntityType is protected.
        """
        ...

    def get_time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Gets the ITimeProvider to use. By default this will load the
        RealTimeProvider for live mode, else SubscriptionFrontierTimeProvider
        
        This codeEntityType is protected.
        
        :returns: The ITimeProvider to use.
        """
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, data_feed_subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, performance_tracking_tool: QuantConnect.Util.PerformanceTrackingTool) -> None:
        """Initializes the instance of the Synchronizer class"""
        ...

    def on_subscription_new_data_available(self, sender: typing.Any, args: System.EventArgs) -> None:
        """
        Trigger new data event
        
        
        This codeEntityType is protected.
        
        :param sender: Sender of the event
        :param args: Event information
        """
        ...

    def post_initialize(self) -> None:
        """
        Performs additional initialization steps after algorithm initialization
        
        
        This codeEntityType is protected.
        """
        ...

    def stream_data(self, cancellation_token: System.Threading.CancellationToken) -> typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class CollectionSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    Collection Subscription Factory takes a BaseDataCollection from BaseData factories
    and yields it one point at a time to the algorithm
    """

    @property
    def reader_error(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], typing.Any], typing.Any]:
        """
        Event fired when an exception is thrown during a call to
        BaseData.reader(SubscriptionDataConfig, string, DateTime, bool)
        """
        ...

    @reader_error.setter
    def reader_error(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], is_live_mode: bool, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Initializes a new instance of the CollectionSubscriptionDataSourceReader class
        
        :param data_cache_provider: Used to cache data for requested from the IDataProvider
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param is_live_mode: True if we're in live mode, false for backtesting
        """
        ...

    def read(self, source: QuantConnect.Data.SubscriptionDataSource) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Reads the specified source
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CompositeTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """The composite time provider will source it's current time using the smallest time from the given providers"""

    def __init__(self, time_providers: typing.List[QuantConnect.ITimeProvider]) -> None:
        """
        Creates a new instance
        
        :param time_providers: The time providers to use. Will default to the real time provider if empty
        """
        ...

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class InternalSubscriptionManager(System.Object):
    """Class in charge of handling Leans internal subscriptions"""

    @property
    def added(self) -> typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], typing.Any]:
        """Event fired when a new internal subscription request is to be added"""
        ...

    @added.setter
    def added(self, value: typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], typing.Any]) -> None:
        ...

    @property
    def removed(self) -> typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], typing.Any]:
        """Event fired when an existing internal subscription should be removed"""
        ...

    @removed.setter
    def removed(self, value: typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], typing.Any]) -> None:
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, resolution: QuantConnect.Resolution) -> None:
        """
        Creates a new instances
        
        :param algorithm: The associated algorithm
        :param resolution: The resolution to use for the internal subscriptions
        """
        ...

    def added_subscription_request(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> None:
        """
        Notifies about a removed subscription request
        
        :param request: The removed subscription request
        """
        ...

    def removed_subscription_request(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> None:
        """
        Notifies about an added subscription request
        
        :param request: The added subscription request
        """
        ...


class AggregationManager(System.Object, QuantConnect.Data.IDataAggregator):
    """
    Aggregates ticks and bars based on given subscriptions.
    Current implementation is based on IDataConsolidator that consolidates ticks and put them into enumerator.
    """

    @property
    def time_provider(self) -> QuantConnect.ITimeProvider:
        """
        Continuous UTC time provider
        
        
        This codeEntityType is protected.
        """
        ...

    @time_provider.setter
    def time_provider(self, value: QuantConnect.ITimeProvider) -> None:
        ...

    def add(self, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], typing.Any]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Add new subscription to current IDataAggregator instance
        
        :param data_config: defines the parameters to subscribe to a data feed
        :param new_data_available_handler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def dispose(self) -> None:
        """Dispose of the aggregation manager."""
        ...

    def get_consolidator(self, config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Gets the consolidator to aggregate data for the given config
        
        
        This codeEntityType is protected.
        """
        ...

    def initialize(self, parameters: QuantConnect.Data.DataAggregatorInitializeParameters) -> None:
        """
        Initialize this instance
        
        :param parameters: The parameters dto instance
        """
        ...

    def remove(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Removes the handler with the specified identifier
        
        :param data_config: Subscription data configuration to be removed
        """
        ...

    def update(self, input: QuantConnect.Data.BaseData) -> None:
        """
        Add new data to aggregator
        
        :param input: The new data
        """
        ...


class NullDataFeed(System.Object, QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """Null data feed implementation. DataManager"""

    @property
    def should_throw(self) -> bool:
        """Allows specifying if this implementation should throw always or not"""
        ...

    @should_throw.setter
    def should_throw(self, value: bool) -> None:
        ...

    @property
    def is_active(self) -> bool:
        ...

    def create_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        ...

    def exit(self) -> None:
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider, subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, data_feed_time_provider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, data_channel_provider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        ...

    def remove_subscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        ...


class LiveTradingDataFeed(QuantConnect.Lean.Engine.DataFeeds.FileSystemDataFeed):
    """
    Provides an implementation of IDataFeed that is designed to deal with
    live, remote data sources
    """

    @property
    def is_active(self) -> bool:
        """Public flag indicator that the thread is still busy."""
        ...

    def create_subscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def exit(self) -> None:
        """External controller calls to signal a terminate of the thread."""
        ...

    def get_base_data_exchange(self) -> QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange:
        """
        Gets the BaseDataExchange to use
        
        
        This codeEntityType is protected.
        """
        ...

    def get_data_queue_handler(self) -> QuantConnect.Interfaces.IDataQueueHandler:
        """
        Gets the IDataQueueHandler to use by default DataQueueHandlerManager
        
        This codeEntityType is protected.
        
        :returns: The loaded IDataQueueHandler.
        """
        ...

    def initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, data_provider: QuantConnect.Interfaces.IDataProvider, subscription_manager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, data_feed_time_provider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, data_channel_provider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def remove_subscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable, QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


