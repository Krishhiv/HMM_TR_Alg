from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import QuantConnect.Lean.Engine.DataFeeds.Enumerators.Factories
import QuantConnect.Lean.Engine.Results
import QuantConnect.Securities
import System
import System.Collections.Generic


class BaseDataCollectionSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory that reads
    an entire SubscriptionDataSource into a single BaseDataCollection
    to be emitted on the tradable date at midnight
    """

    def __init__(self, object_store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Instanciates a new BaseDataCollectionSubscriptionEnumeratorFactory
        
        :param object_store: The object store to use
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class LiveCustomDataSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """Provides an implementation of ISubscriptionEnumeratorFactory to handle live custom data."""

    def __init__(self, time_provider: QuantConnect.ITimeProvider, object_store: QuantConnect.Interfaces.IObjectStore, date_adjustment: typing.Callable[[datetime.datetime], datetime.datetime] = None, minimum_interval_check: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the LiveCustomDataSubscriptionEnumeratorFactory class
        
        :param time_provider: Time provider from data feed
        :param object_store: The object store to use
        :param date_adjustment: Func that allows adjusting the datetime to use
        :param minimum_interval_check: Allows specifying the minimum interval between each enumerator refresh and data check, default is 30 minutes
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request.
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...

    def get_subscription_data_source_reader(self, source: QuantConnect.Data.SubscriptionDataSource, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], base_data_instance: QuantConnect.Data.BaseData, data_provider: QuantConnect.Interfaces.IDataProvider) -> QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader:
        """
        Gets the ISubscriptionDataSourceReader for the specified source
        
        
        This codeEntityType is protected.
        """
        ...


class TimeTriggeredUniverseSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory):
    """
    Provides an implementation of ISubscriptionEnumeratorFactory to emit
    ticks based on UserDefinedUniverse.get_trigger_times, allowing universe
    selection to fire at planned times.
    """

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.ITimeTriggeredUniverse, market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initializes a new instance of the TimeTriggeredUniverseSubscriptionEnumeratorFactory class
        
        :param universe: The user defined universe
        :param market_hours_database: The market hours database
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class SubscriptionDataReaderSubscriptionEnumeratorFactory(System.Object, QuantConnect.Data.ISubscriptionEnumeratorFactory, System.IDisposable):
    """Provides an implementation of ISubscriptionEnumeratorFactory that used the SubscriptionDataReader"""

    def __init__(self, result_handler: QuantConnect.Lean.Engine.Results.IResultHandler, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, cache_provider: QuantConnect.Interfaces.IDataCacheProvider, algorithm: QuantConnect.Interfaces.IAlgorithm, enable_price_scaling: bool = True) -> None:
        """
        Initializes a new instance of the SubscriptionDataReaderSubscriptionEnumeratorFactory class
        
        :param result_handler: The result handler for the algorithm
        :param map_file_provider: The map file provider
        :param factor_file_provider: The factor file provider
        :param cache_provider: Provider used to get data when it is not present on disk
        :param algorithm: The algorithm instance to use
        :param enable_price_scaling: Applies price factor
        """
        ...

    def create_enumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, data_provider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a SubscriptionDataReader to read the specified request
        
        :param request: The subscription request to be read
        :param data_provider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...


class CorporateEventEnumeratorFactory(System.Object):
    """
    Helper class used to create the corporate event providers
    MappingEventProvider, SplitEventProvider,
    DividendEventProvider, DelistingEventProvider
    """

    @staticmethod
    def create_enumerators(raw_data_enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], config: QuantConnect.Data.SubscriptionDataConfig, factor_file_provider: QuantConnect.Interfaces.IFactorFileProvider, tradable_day_notifier: QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, map_file_provider: QuantConnect.Interfaces.IMapFileProvider, start_time: typing.Union[datetime.datetime, datetime.date], end_time: typing.Union[datetime.datetime, datetime.date], enable_price_scaling: bool = True) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a new AuxiliaryDataEnumerator that will hold the
        corporate event providers
        
        :param raw_data_enumerator: The underlying raw data enumerator
        :param config: The SubscriptionDataConfig
        :param factor_file_provider: Used for getting factor files
        :param tradable_day_notifier: Tradable dates provider
        :param map_file_provider: The MapFile provider to use
        :param start_time: Start date for the data request
        :param end_time: End date for the data request.
        This will be used for DataNormalizationMode.SCALED_RAW data normalization mode to adjust prices to the given end date
        :param enable_price_scaling: Applies price factor
        :returns: The new auxiliary data enumerator.
        """
        ...


