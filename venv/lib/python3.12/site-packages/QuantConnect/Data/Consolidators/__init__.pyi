from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Python
import System

QuantConnect_Data_Consolidators_ClassicRenkoConsolidator = typing.Any
QuantConnect_Data_Consolidators_RenkoConsolidator = typing.Any

QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput")
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated = typing.TypeVar("QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated")
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T = typing.TypeVar("QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T")
QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T")
QuantConnect_Data_Consolidators_DataConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_DataConsolidator_TInput")
QuantConnect_Data_Consolidators_RenkoConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_RenkoConsolidator_TInput")
QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T")
QuantConnect_Data_Consolidators_IdentityDataConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_IdentityDataConsolidator_T")
QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T = typing.TypeVar("QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T")
QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T")
QuantConnect_Data_Consolidators__EventContainer_Callable = typing.TypeVar("QuantConnect_Data_Consolidators__EventContainer_Callable")
QuantConnect_Data_Consolidators__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data_Consolidators__EventContainer_ReturnType")


class CalendarInfo:
    """Calendar Info for storing information related to the start and period of a consolidator"""

    @property
    def start(self) -> datetime.datetime:
        """Calendar Start"""
        ...

    @property
    def period(self) -> datetime.timedelta:
        """Consolidation Period"""
        ...

    @property
    def end(self) -> datetime.datetime:
        """Calendar End"""
        ...

    def __eq__(self, right: QuantConnect.Data.Consolidators.CalendarInfo) -> bool:
        """
        Indicates whether the given object is equal to this object, this is, the Calendar start
        and consolidation period is the same for both
        """
        ...

    def __init__(self, start: typing.Union[datetime.datetime, datetime.date], period: datetime.timedelta) -> None:
        """
        Constructor for CalendarInfo; used for consolidation calendar
        
        :param start: Calendar Start
        :param period: Consolidation Period
        """
        ...

    def __ne__(self, right: QuantConnect.Data.Consolidators.CalendarInfo) -> bool:
        """
        Indicates whether the given object is equal to this object, this is, the Calendar start
        and consolidation period is the same for both
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Indicates whether the given object is equal to this object, this is, the Calendar start
        and consolidation period is the same for both
        """
        ...

    def get_hash_code(self) -> int:
        """Returns the hash code for this object as an integer"""
        ...

    def to_string(self) -> str:
        """Returns a string containing the Calendar start and the consolidation period"""
        ...


class BaseDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.BaseData]):
    """Type capable of consolidating trade bars from any base data instance"""

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Initializes a new instance of the BaseDataConsolidator class
        
        :param pyfuncobj: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the BaseDataConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.BaseData) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...

    @staticmethod
    def from_resolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.BaseDataConsolidator:
        """
        Create a new TickConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...


class TickQuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.QuoteBar]):
    """Consolidates ticks into quote bars. This consolidator ignores trade ticks"""

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.QuoteBar, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...

    def should_process(self, data: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        
        This codeEntityType is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...


class ClassicRenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], QuantConnect_Data_Consolidators_ClassicRenkoConsolidator):
    """Provides a type safe wrapper on the RenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving"""

    @property
    def current_bar(self) -> QuantConnect.Data.Market.RenkoBar:
        """
        Bar being created
        
        
        This codeEntityType is protected.
        """
        ...

    @current_bar.setter
    def current_bar(self, value: QuantConnect.Data.Market.RenkoBar) -> None:
        ...

    @property
    def type(self) -> QuantConnect.Data.Market.RenkoType:
        """Gets the kind of the bar"""
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets RenkoBar which is the type emitted in the IDataConsolidator.data_consolidated event."""
        ...

    @overload
    def __init__(self, bar_size: float, selector: typing.Any, volume_selector: typing.Any = None, even_bars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param bar_size: The size of each bar in units of the value produced by selector
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        :param even_bars: When true bar open/close will be a multiple of the bar_size
        """
        ...

    @overload
    def __init__(self, bar_size: float, even_bars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class using the specified bar_size.
        The value selector will by default select IBaseData.value
        The volume selector will by default select zero.
        
        :param bar_size: The constant value size of each bar
        :param even_bars: When true bar open/close will be a multiple of the bar_size
        """
        ...

    @overload
    def __init__(self, bar_size: float, selector: typing.Callable[[QuantConnect.Data.IBaseData], float], volume_selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, even_bars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param bar_size: The size of each bar in units of the value produced by selector
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        :param even_bars: When true bar open/close will be a multiple of the bar_size
        """
        ...

    @overload
    def __init__(self, bar_size: float, selector: typing.Callable[[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], float], volume_selector: typing.Callable[[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], float] = None, even_bars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param bar_size: The size of each bar in units of the value produced by selector
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        :param even_bars: When true bar open/close will be a multiple of the bar_size
        """
        ...

    @overload
    def __init__(self, bar_size: float, type: QuantConnect.Data.Market.RenkoType) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        
        Please use the new RenkoConsolidator if RenkoType is not Classic
        
        :param bar_size: The constant value size of each bar
        :param type: The RenkoType of the bar
        """
        ...

    def create_new_bar(self, data: QuantConnect.Data.IBaseData, current_value: float, volume: float) -> None:
        """
        Creates a new bar with the given data
        
        
        This codeEntityType is protected.
        
        :param data: The new data for the bar
        :param current_value: The new value for the bar
        :param volume: The new volume to the bar
        """
        ...

    def reset(self) -> None:
        """Resets the ClassicRenkoConsolidator"""
        ...

    def update(self, data: QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data.
        
        :param data: The new data for the consolidator
        """
        ...

    def update_bar(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume: float) -> None:
        """
        Updates the current RangeBar being created with the given data.
        Additionally, if it's the case, it consolidates the current RangeBar
        
        
        This codeEntityType is protected.
        
        :param time: Time of the given data
        :param current_value: Value of the given data
        :param volume: Volume of the given data
        """
        ...


class PeriodCountConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], QuantConnect.Data.Consolidators.DataConsolidator[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T], metaclass=abc.ABCMeta):
    """
    Provides a base class for consolidators that emit data based on the passing of a period of time
    or after seeing a max count of data points.
    """

    @property
    def _working_bar(self) -> QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated:
        """This codeEntityType is protected."""
        ...

    @_working_bar.setter
    def _working_bar(self, value: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated) -> None:
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], typing.Any], typing.Any]:
        """
        Event handler that fires when a new piece of data is produced. We define this as a 'new'
        event so we can expose it as a t_consolidated instead of a BaseData instance
        """
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], typing.Any], typing.Any]) -> None:
        ...

    @property
    def is_time_based(self) -> bool:
        """
        Returns true if this consolidator is time-based, false otherwise
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def period(self) -> typing.Optional[datetime.timedelta]:
        """
        Gets the time period for this consolidator
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, py_object: typing.Any) -> None:
        """
        Creates a consolidator to produce a new t_consolidated instance representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param py_object: Python object that defines either a function object that defines the start time of a consolidated data or a timespan
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Creates a consolidator to produce a new t_consolidated instance representing the period
        
        
        This codeEntityType is protected.
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new t_consolidated instance representing the last count pieces of data
        
        
        This codeEntityType is protected.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new t_consolidated instance representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new t_consolidated instance representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...

    @overload
    def get_rounded_bar_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Gets a rounded-down bar time. Called by AggregateBar in derived classes.
        
        
        This codeEntityType is protected.
        
        :param time: The bar time to be rounded down
        :returns: The rounded bar time.
        """
        ...

    @overload
    def get_rounded_bar_time(self, input_data: QuantConnect.Data.IBaseData) -> datetime.datetime:
        """
        Gets a rounded-down bar start time. Called by AggregateBar in derived classes.
        
        
        This codeEntityType is protected.
        
        :param input_data: The input data point
        :returns: The rounded bar start time.
        """
        ...

    def on_data_consolidated(self, e: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated) -> None:
        """
        Event invocator for the data_consolidated event
        
        
        This codeEntityType is protected.
        
        :param e: The consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def reset_working_bar(self) -> None:
        """
        Resets the working bar
        
        
        This codeEntityType is protected.
        """
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def should_process(self, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        
        This codeEntityType is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...

    def update(self, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> None:
        """
        Updates this consolidator with the specified data. This method is
        responsible for raising the DataConsolidated event
        In time span mode, the bar range is closed on the left and open on the right: [T, T+TimeSpan).
        For example, if time span is 1 minute, we have [10:00, 10:01): so data at 10:01 is not
        included in the bar starting at 10:00.
        
        :param data: The new data for the consolidator
        """
        ...


class FilteredIdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T], QuantConnect.Data.Consolidators.IdentityDataConsolidator[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T]):
    """
    Provides an implementation of IDataConsolidator that preserve the input
    data unmodified. The input data is filtering by the specified predicate function
    """

    def __init__(self, predicate: typing.Callable[[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T], bool]) -> None:
        """
        Initializes a new instance of the FilteredIdentityDataConsolidator{T} class
        
        :param predicate: The predicate function, returning true to accept data and false to reject data
        """
        ...

    @staticmethod
    def for_tick_type(tick_type: QuantConnect.TickType) -> QuantConnect.Data.Consolidators.FilteredIdentityDataConsolidator[QuantConnect.Data.Market.Tick]:
        """
        Creates a new instance of FilteredIdentityDataConsolidator{T} that filters ticks
        based on the specified TickType
        
        :param tick_type: The tick type of data to accept
        :returns: A new FilteredIdentityDataConsolidator{T} that filters based on the provided tick type.
        """
        ...

    def update(self, data: QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class IDataConsolidator(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Represents a type capable of taking BaseData updates and firing events containing new
    'consolidated' data. These types can be used to produce larger bars, or even be used to
    transform the data before being sent to another component. The most common usage of these
    types is with indicators.
    """

    @property
    @abc.abstractmethod
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    @abc.abstractmethod
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    @abc.abstractmethod
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]) -> None:
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class DataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_DataConsolidator_TInput], System.Object, QuantConnect.Data.Consolidators.IDataConsolidator, metaclass=abc.ABCMeta):
    """
    Represents a type that consumes BaseData instances and fires an event with consolidated
    and/or aggregated data.
    """

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]) -> None:
        ...

    @property
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @consolidated.setter
    def consolidated(self, value: QuantConnect.Data.IBaseData) -> None:
        ...

    @property
    @abc.abstractmethod
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def on_data_consolidated(self, consolidated: QuantConnect.Data.IBaseData) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        
        This codeEntityType is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    @overload
    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    @overload
    def update(self, data: QuantConnect_Data_Consolidators_DataConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data. This method is
        responsible for raising the DataConsolidated event
        
        :param data: The new data for the consolidator
        """
        ...


class VolumeRenkoConsolidator(QuantConnect.Data.Consolidators.DataConsolidator[QuantConnect.Data.BaseData]):
    """
    This consolidator can transform a stream of BaseData instances into a stream of RenkoBar
    with a constant volume for each bar.
    """

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets VolumeRenkoBar which is the type emitted in the IDataConsolidator.data_consolidated event."""
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.VolumeRenkoBar], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.VolumeRenkoBar], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, bar_size: float) -> None:
        """
        Initializes a new instance of the VolumeRenkoConsolidator class using the specified bar_size.
        
        :param bar_size: The constant volume size of each bar
        """
        ...

    def adjust_volume(self, volume: float, price: float) -> float:
        """
        Returns the raw volume without any adjustment.
        
        
        This codeEntityType is protected.
        
        :param volume: The volume
        :param price: The price
        :returns: The unmodified volume.
        """
        ...

    def on_data_consolidated(self, consolidated: QuantConnect.Data.Market.VolumeRenkoBar) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        
        This codeEntityType is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def update(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class RangeConsolidator(QuantConnect.Data.Consolidators.BaseTimelessConsolidator[QuantConnect.Data.Market.RangeBar]):
    """This consolidator can transform a stream of IBaseData instances into a stream of RangeBar"""

    @property
    def current_bar(self) -> QuantConnect.Data.Market.RangeBar:
        """
        Bar being created
        
        
        This codeEntityType is protected.
        """
        ...

    @current_bar.setter
    def current_bar(self, value: QuantConnect.Data.Market.RangeBar) -> None:
        ...

    @property
    def range_size(self) -> float:
        """
        Range for each RangeBar, this is, the difference between the High and Low for each
        RangeBar
        """
        ...

    @property
    def range(self) -> int:
        """Number of MinimumPriceVariation units"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets RangeBar which is the type emitted in the IDataConsolidator.data_consolidated event."""
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @overload
    def __init__(self, range: int, selector: typing.Any, volume_selector: typing.Any = None) -> None:
        """
        Initializes a new instance of the RangeConsolidator class.
        
        :param range: The Range interval sets the range in which the price moves, which in turn initiates the formation of a new bar.
        One range equals to one minimum price change, where this last value is defined depending of the RangeBar's symbol
        :param selector: Extracts the value from a data instance to be formed into a RangeBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        """
        ...

    @overload
    def __init__(self, range: int, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, volume_selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Initializes a new instance of the RangeConsolidator class.
        
        :param range: The Range interval sets the range in which the price moves, which in turn initiates the formation of a new bar.
        One range equals to one minimum price change, where this last value is defined depending of the RangeBar's symbol
        :param selector: Extracts the value from a data instance to be formed into a RangeBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar, except if the input is a TradeBar.
        """
        ...

    def create_new_bar(self, data: QuantConnect.Data.IBaseData, current_value: float, volume: float) -> None:
        """
        Creates a new bar with the given data
        
        
        This codeEntityType is protected.
        
        :param data: The new data for the bar
        :param current_value: The new value for the bar
        :param volume: The new volume for the bar
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def update_bar(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume: float) -> None:
        """
        Updates the current RangeBar being created with the given data.
        Additionally, if it's the case, it consolidates the current RangeBar
        
        
        This codeEntityType is protected.
        
        :param time: Time of the given data
        :param current_value: Value of the given data
        :param volume: Volume of the given data
        """
        ...


class ClassicRangeConsolidator(QuantConnect.Data.Consolidators.RangeConsolidator):
    """
    This consolidator can transform a stream of IBaseData instances into a stream of RangeBar.
    The difference between this consolidator and RangeConsolidator, is that this last one creates intermediate/
    phantom RangeBar's (RangeBar's with zero volume) if the price rises up or falls down by above/below two times the range
    size. Therefore, RangeConsolidator leaves no space between two adyacent RangeBar's since it always start
    a new RangeBar one range above the last RangeBar's High value or one range below the last RangeBar's Low value, where
    one range equals to one minimum price change.
    """

    @overload
    def __init__(self, range: int, selector: typing.Any, volume_selector: typing.Any = None) -> None:
        """
        Initializes a new instance of the RangeConsolidator class.
        
        :param range: The Range interval sets the range in which the price moves, which in turn initiates the formation of a new bar.
        One range equals to one minimum price change, where this last value is defined depending of the RangeBar's symbol
        :param selector: Extracts the value from a data instance to be formed into a RangeBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        """
        ...

    @overload
    def __init__(self, range: int, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, volume_selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Initializes a new instance of the ClassicRangeConsolidator class.
        
        :param range: The Range interval sets the range in which the price moves, which in turn initiates the formation of a new bar.
        One range equals to one minimum price change, where this last value is defined depending of the RangeBar's symbol
        :param selector: Extracts the value from a data instance to be formed into a RangeBar. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar, except if the input is a TradeBar.
        """
        ...

    def update_bar(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume: float) -> None:
        """
        Updates the current RangeBar being created with the given data.
        Additionally, if it's the case, it consolidates the current RangeBar
        
        
        This codeEntityType is protected.
        
        :param time: Time of the given data
        :param current_value: Value of the given data
        :param volume: Volume of the given data
        """
        ...


class RenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_RenkoConsolidator_TInput], QuantConnect_Data_Consolidators_RenkoConsolidator):
    """Provides a type safe wrapper on the RenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving"""

    @property
    def close_on(self) -> datetime.datetime:
        """
        Time of consolidated close.
        
        
        This codeEntityType is protected.
        """
        ...

    @close_on.setter
    def close_on(self, value: datetime.datetime) -> None:
        ...

    @property
    def close_rate(self) -> float:
        """
        Value of consolidated close.
        
        
        This codeEntityType is protected.
        """
        ...

    @close_rate.setter
    def close_rate(self, value: float) -> None:
        ...

    @property
    def high_rate(self) -> float:
        """
        Value of consolidated high.
        
        
        This codeEntityType is protected.
        """
        ...

    @high_rate.setter
    def high_rate(self, value: float) -> None:
        ...

    @property
    def low_rate(self) -> float:
        """
        Value of consolidated low.
        
        
        This codeEntityType is protected.
        """
        ...

    @low_rate.setter
    def low_rate(self, value: float) -> None:
        ...

    @property
    def open_on(self) -> datetime.datetime:
        """
        Time of consolidated open.
        
        
        This codeEntityType is protected.
        """
        ...

    @open_on.setter
    def open_on(self, value: datetime.datetime) -> None:
        ...

    @property
    def open_rate(self) -> float:
        """
        Value of consolidate open.
        
        
        This codeEntityType is protected.
        """
        ...

    @open_rate.setter
    def open_rate(self, value: float) -> None:
        ...

    @property
    def bar_size(self) -> float:
        """
        Size of the consolidated bar.
        
        
        This codeEntityType is protected.
        """
        ...

    @bar_size.setter
    def bar_size(self, value: float) -> None:
        ...

    @property
    def type(self) -> QuantConnect.Data.Market.RenkoType:
        """Gets the kind of the bar"""
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets RenkoBar which is the type emitted in the IDataConsolidator.data_consolidated event."""
        ...

    @property
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, bar_size: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified bar_size.
        
        :param bar_size: The constant value size of each bar
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def get_closest_multiple(price: float, bar_size: float) -> float:
        """
        Gets the closest BarSize-Multiple to the price.
        
        :param price: Price to be rounded to the closest BarSize-Multiple
        :param bar_size: The size of the Renko bar
        :returns: The closest BarSize-Multiple to the price.
        """
        ...

    def on_data_consolidated(self, consolidated: QuantConnect.Data.Market.RenkoBar) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        
        This codeEntityType is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    @overload
    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    @overload
    def update(self, data: QuantConnect_Data_Consolidators_RenkoConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data.
        
        :param data: The new data for the consolidator
        """
        ...


class WickedRenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T], QuantConnect.Data.Consolidators.RenkoConsolidator[QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T]):
    """
    This consolidator can transform a stream of BaseData instances into a stream of RenkoBar
    with Renko type RenkoType.WICKED.
    Provides a type safe wrapper on the WickedRenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving
    ///
    """

    def __init__(self, bar_size: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified bar_size.
        
        :param bar_size: The constant value size of each bar
        """
        ...


class IdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T], QuantConnect.Data.Consolidators.DataConsolidator[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T]):
    """
    Represents the simplest DataConsolidator implementation, one that is defined
    by a straight pass through of the data. No projection or aggregation is performed.
    """

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def update(self, data: QuantConnect_Data_Consolidators_IdentityDataConsolidator_T) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class CalendarType(System.Object):
    """
    Calendar Type Class; now obsolete routes functions to Calendar
    
    CalendarType is obsolete, please use Calendar instead
    """

    WEEKLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of week (previous Monday) of given date/time"""

    MONTHLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of month (1st of the current month) of given date/time"""


class DynamicDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.DynamicData]):
    """
    A data csolidator that can make trade bars from DynamicData derived types. This is useful for
    aggregating Quandl and other highly flexible dynamic custom data types.
    """

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period.
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.DynamicData) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...


class TradeBarConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T], QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T, QuantConnect.Data.Market.TradeBar], metaclass=abc.ABCMeta):
    """
    A data consolidator that can make bigger bars from any base data
    
    This type acts as the base for other consolidators that produce bars on a given time step or for a count of data.
    """

    @property
    def working_bar(self) -> QuantConnect.Data.Market.TradeBar:
        """Gets a copy of the current 'workingBar'."""
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        
        This codeEntityType is protected.
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        
        This codeEntityType is protected.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param max_count: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        
        This codeEntityType is protected.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...


class Calendar(System.Object):
    """Helper class that provides Func{DateTime,CalendarInfo} used to define consolidation calendar"""

    WEEKLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of week (previous Monday) of given date/time"""

    MONTHLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of month (1st of the current month) of given date/time"""

    QUARTERLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of quarter (1st of the starting month of current quarter) of given date/time"""

    YEARLY: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of year (1st of the current year) of given date/time"""


class OpenInterestConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.OpenInterest]):
    """Type capable of consolidating open interest"""

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest'
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the last count pieces of data
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the last count pieces of data or the period, whichever comes first
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest'
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.OpenInterest, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new OI bar
        :param data: The new data
        """
        ...

    @staticmethod
    def from_resolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.OpenInterestConsolidator:
        """
        Create a new OpenInterestConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...

    def should_process(self, data: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        
        This codeEntityType is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...

    def update(self, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Updates this consolidator with the specified data. This method is
        responsible for raising the DataConsolidated event.
        It will check for date or hour change and force consolidation if needed.
        
        :param data: The new data for the consolidator
        """
        ...


class QuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.QuoteBar, QuantConnect.Data.Market.QuoteBar]):
    """Consolidates QuoteBars into larger QuoteBars"""

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'QuoteBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the QuoteBarConsolidator class
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Initializes a new instance of the QuoteBarConsolidator class
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the QuoteBarConsolidator class
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'QuoteBar' representing the last count pieces of data or the period, whichever comes first
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.QuoteBar, data: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...


class TickConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.Market.Tick]):
    """
    A data consolidator that can make bigger bars from ticks over a given
    time span or a count of pieces of data.
    """

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building
        :param data: The new data
        """
        ...

    def should_process(self, data: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        
        This codeEntityType is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...


class BaseTimelessConsolidator(typing.Generic[QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T], System.Object, QuantConnect.Data.Consolidators.IDataConsolidator, metaclass=abc.ABCMeta):
    """
    Represents a timeless consolidator which depends on the given values. This consolidator
    is meant to consolidate data into bars that do not depend on time, e.g., RangeBar's.
    """

    @property
    def selector(self) -> typing.Callable[[QuantConnect.Data.IBaseData], float]:
        """
        Extracts the value from a data instance to be formed into a T.
        
        
        This codeEntityType is protected.
        """
        ...

    @selector.setter
    def selector(self, value: typing.Callable[[QuantConnect.Data.IBaseData], float]) -> None:
        ...

    @property
    def volume_selector(self) -> typing.Callable[[QuantConnect.Data.IBaseData], float]:
        """
        Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        
        
        This codeEntityType is protected.
        """
        ...

    @volume_selector.setter
    def volume_selector(self, value: typing.Callable[[QuantConnect.Data.IBaseData], float]) -> None:
        ...

    @property
    def data_consolidated_handler(self) -> typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any]:
        """
        Event handler type for the IDataConsolidator.DataConsolidated event
        
        
        This codeEntityType is protected.
        """
        ...

    @data_consolidated_handler.setter
    def data_consolidated_handler(self, value: typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any]) -> None:
        ...

    @property
    def current_bar(self) -> QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T:
        """
        Bar being created
        
        
        This codeEntityType is protected.
        """
        ...

    @current_bar.setter
    def current_bar(self, value: QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T) -> None:
        ...

    @property
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @consolidated.setter
    def consolidated(self, value: QuantConnect.Data.IBaseData) -> None:
        ...

    @property
    @abc.abstractmethod
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets T which is the type emitted in the IDataConsolidator.data_consolidated event."""
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T], typing.Any], typing.Any]) -> None:
        ...

    @overload
    def __init__(self, value_selector: typing.Any, volume_selector: typing.Any = None) -> None:
        """
        Initializes a new instance of the BaseTimelessConsolidator{T} class.
        
        
        This codeEntityType is protected.
        
        :param value_selector: Extracts the value from a data instance to be formed into a new bar which inherits from IBaseData. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        """
        ...

    @overload
    def __init__(self, selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, volume_selector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None) -> None:
        """
        Initializes a new instance of the BaseTimelessConsolidator{T} class.
        
        
        This codeEntityType is protected.
        
        :param selector: Extracts the value from a data instance to be formed into a new bar which inherits from IBaseData. The default
        value is (x => x.Value) the IBaseData.value property on IBaseData
        :param volume_selector: Extracts the volume from a data instance. The default value is null which does
        not aggregate volume per bar.
        """
        ...

    def create_new_bar(self, data: QuantConnect.Data.IBaseData, current_value: float, volume: float) -> None:
        """
        Creates a new bar with the given data
        
        
        This codeEntityType is protected.
        
        :param data: The new data for the bar
        :param current_value: The new value for the bar
        :param volume: The new volume to the bar
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def on_data_consolidated(self, consolidated: QuantConnect_Data_Consolidators_BaseTimelessConsolidator_T) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        
        This codeEntityType is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    def update_bar(self, time: typing.Union[datetime.datetime, datetime.date], current_value: float, volume: float) -> None:
        """
        Updates the current RangeBar being created with the given data.
        Additionally, if it's the case, it consolidates the current RangeBar
        
        
        This codeEntityType is protected.
        
        :param time: Time of the given data
        :param current_value: Value of the given data
        :param volume: Volume of the given data
        """
        ...


class TradeBarConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.Market.TradeBar]):
    """
    A data consolidator that can make bigger bars from smaller ones over a given
    time span or a count of pieces of data.
    
    Use this consolidator to turn data of a lower resolution into data of a higher resolution,
    for example, if you subscribe to minute data but want to have a 15 minute bar.
    """

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, start_time: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        :param start_time: Optionally the bar start time anchor to use
        """
        ...

    @overload
    def __init__(self, max_count: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, max_count: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param max_count: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Aggregates the new 'data' into the 'working_bar'. The 'working_bar' will be
        null following the event firing
        
        
        This codeEntityType is protected.
        
        :param working_bar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...

    @staticmethod
    def from_resolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.TradeBarConsolidator:
        """
        Create a new TradeBarConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...


class SequentialConsolidator(System.Object, QuantConnect.Data.Consolidators.IDataConsolidator):
    """
    This consolidator wires up the events on its First and Second consolidators
    such that data flows from the First to Second consolidator. It's output comes
    from the Second.
    """

    @property
    def first(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """Gets the first consolidator to receive data"""
        ...

    @property
    def second(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Gets the second consolidator that ends up receiving data produced
        by the first
        """
        ...

    @property
    def consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        
        For a SequentialConsolidator, this is the output from the 'Second' consolidator.
        """
        ...

    @property
    def working_data(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def input_type(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def output_type(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    def data_consolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @data_consolidated.setter
    def data_consolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], typing.Any], typing.Any]) -> None:
        ...

    def __init__(self, first: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], second: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> None:
        """
        Creates a new consolidator that will pump date through the first, and then the output
        of the first into the second. This enables 'wrapping' or 'composing' of consolidators
        
        :param first: The first consolidator to receive data
        :param second: The consolidator to receive first's output
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def on_data_consolidated(self, consolidated: QuantConnect.Data.IBaseData) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        
        This codeEntityType is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def reset(self) -> None:
        """Resets the consolidator"""
        ...

    def scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param current_local_time: The current time in the local time zone (same as BaseData.time)
        """
        ...

    def update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data_Consolidators__EventContainer_Callable, QuantConnect_Data_Consolidators__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data_Consolidators__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data_Consolidators__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data_Consolidators__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


