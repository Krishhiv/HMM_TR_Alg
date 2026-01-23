from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.Brokerages.LevelOneOrderBook
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import System

QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_Callable = typing.TypeVar("QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_Callable")
QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_ReturnType")


class LevelOneServiceManager(System.Object, System.IDisposable):
    """
    Manages subscriptions and real-time updates for multiple LevelOneMarketData instances.
    Facilitates routing of quote and trade data to a shared IDataAggregator in a thread-safe manner.
    """

    @property
    def is_empty(self) -> bool:
        """Gets whether there are no active subscriptions."""
        ...

    @property
    def count(self) -> int:
        """Gets the number of currently subscribed symbols."""
        ...

    def __init__(self, data_aggregator: QuantConnect.Data.IDataAggregator, subscribe_callback: typing.Callable[[typing.List[QuantConnect.Symbol], QuantConnect.TickType], bool], unsubscribe_callback: typing.Callable[[typing.List[QuantConnect.Symbol], QuantConnect.TickType], bool]) -> None:
        """
        Initializes a new instance of the LevelOneServiceManager class.
        
        :param data_aggregator: The aggregator to which all tick data will be published.
        :param subscribe_callback: Delegate used to perform symbol subscription logic.
        :param unsubscribe_callback: Delegate used to perform symbol unsubscription logic.
        """
        ...

    def dispose(self) -> None:
        """Releases all resources used by the LevelOneServiceManager."""
        ...

    def get_subscribed_symbols(self) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Returns subscribed symbols
        
        :returns: list of Symbol currently subscribed.
        """
        ...

    def handle_last_trade(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], trade_date_time_utc: typing.Optional[datetime.datetime], last_quantity: typing.Optional[float], last_price: typing.Optional[float], sale_condition: str = ..., exchange: str = ...) -> None:
        """
        Handles incoming last trade data for a symbol and routes it to the corresponding LevelOneMarketData instance.
        
        :param symbol: The symbol for which trade data is received.
        :param trade_date_time_utc: The UTC timestamp of the trade.
        :param last_quantity: The trade size.
        :param last_price: The trade price.
        :param sale_condition: Optional sale condition string.
        :param exchange: Optional exchange identifier.
        """
        ...

    def handle_open_interest(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], open_interest_date_time_utc: typing.Optional[datetime.datetime], open_interest: typing.Optional[float]) -> None:
        """
        Handles open interest updates for the specified symbol.
        If the symbol is subscribed, forwards the open interest data to the corresponding
        LevelOneMarketData instance for publishing.
        
        :param symbol: The trading symbol associated with the open interest update.
        :param open_interest_date_time_utc: The UTC timestamp when the open interest value was observed.
        :param open_interest: The reported open interest value.
        """
        ...

    def handle_quote(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], quote_date_time_utc: typing.Optional[datetime.datetime], bid_price: typing.Optional[float], bid_size: typing.Optional[float], ask_price: typing.Optional[float], ask_size: typing.Optional[float]) -> None:
        """
        Handles incoming quote data for a symbol.
        Deduplicates updates and routes changes to the relevant LevelOneMarketData instance.
        
        :param symbol: The symbol for which quote data is received.
        :param quote_date_time_utc: The UTC timestamp of the quote.
        :param bid_price: The bid price.
        :param bid_size: The size at the bid price.
        :param ask_price: The ask price.
        :param ask_size: The size at the ask price.
        """
        ...

    def set_ignore_zero_size_updates(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], ignore_zero_size_updates: bool) -> None:
        """
        Sets the LevelOneMarketData.ignore_zero_size_updates flag for the specified symbol,
        controlling how zero-sized quote updates are handled for that symbol's market data stream.
        
        :param symbol: The symbol whose quote update behavior should be configured.
        :param ignore_zero_size_updates: If true, zero-sized bid or ask updates will be ignored for the given symbol,
        preserving existing book values. If false, zero sizes will be applied as valid updates.
        """
        ...

    def subscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Subscribes to the specified symbol based on the given SubscriptionDataConfig.
        
        :param data_config: The subscription configuration containing symbol and type information.
        """
        ...

    def unsubscribe(self, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Unsubscribes from the specified symbol and removes its associated service instance.
        
        :param data_config: The subscription configuration used for unsubscription.
        """
        ...


class BaseDataEventArgs(System.EventArgs):
    """Provides data for an event that is triggered when a new base_data is received."""

    @property
    def base_data(self) -> QuantConnect.Data.BaseData:
        """Gets the base_data data associated with the event."""
        ...

    def __init__(self, tick: QuantConnect.Data.BaseData) -> None:
        """
        Initializes a new instance of the BaseDataEventArgs class with the specified base_data.
        
        :param tick: The base_data data associated with the event.
        """
        ...


class LevelOneMarketData(System.Object):
    """This class has no documentation."""

    @property
    def base_data_received(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.LevelOneOrderBook.BaseDataEventArgs], typing.Any], typing.Any]:
        """Occurs when a new tick is received, such as a last trade update or a change in bid/ask values."""
        ...

    @base_data_received.setter
    def base_data_received(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Brokerages.LevelOneOrderBook.BaseDataEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol this service is tracking."""
        ...

    @property
    def symbol_date_time_zone(self) -> typing.Any:
        """
        Gets the time zone associated with the symbol's exchange.
        Used for consistent time stamping.
        """
        ...

    @property
    def last_trade_price(self) -> float:
        """Gets the price of the last executed trade."""
        ...

    @property
    def last_trade_size(self) -> float:
        """Gets the size of the last executed trade."""
        ...

    @property
    def best_bid_price(self) -> float:
        """Gets the best available bid price."""
        ...

    @property
    def best_bid_size(self) -> float:
        """Gets the size of the best available bid."""
        ...

    @property
    def best_ask_price(self) -> float:
        """Gets the best available ask price."""
        ...

    @property
    def best_ask_size(self) -> float:
        """Gets the size of the best available ask."""
        ...

    @property
    def open_interest(self) -> float:
        """Gets the latest reported open interest value."""
        ...

    @property
    def ignore_zero_size_updates(self) -> bool:
        """
        Gets or sets a value indicating whether quote updates with a size of zero should be ignored
        when updating Level 1 market data.
        
        When set to true, incoming bid or ask updates with a size of zero are treated
        as missing or incomplete and will not overwrite the existing known price or size.
        This is typically used for real-time (non-delayed) feeds where a zero size may indicate
        a temporary data gap rather than an actionable market change.
        
        When set to false (default), zero-sized updates are applied normally,
        which is appropriate for delayed feeds or sources where a size of zero has
        semantic meaning (e.g., clearing out a book level).
        """
        ...

    @ignore_zero_size_updates.setter
    def ignore_zero_size_updates(self, value: bool) -> None:
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        """
        Initializes a new instance of the LevelOneMarketData class for a given symbol.
        
        :param symbol: The trading symbol to monitor.
        """
        ...

    def update_last_trade(self, trade_date_time_utc: typing.Optional[datetime.datetime], last_quantity: typing.Optional[float], last_price: typing.Optional[float], sale_condition: str = ..., exchange: str = ...) -> None:
        """
        Updates the last trade price and size.
        Constructs and publishes a trade Tick to the Data.IDataAggregator.
        
        :param trade_date_time_utc: The UTC timestamp when the trade occurred.
        :param last_quantity: The quantity of the last trade.
        :param last_price: The price at which the last trade occurred.
        :param sale_condition: Optional sale condition string.
        :param exchange: Optional exchange identifier.
        """
        ...

    def update_open_interest(self, open_interest_date_time_utc: typing.Optional[datetime.datetime], open_interest: typing.Optional[float]) -> None:
        """
        Updates the open interest value and publishes a corresponding Tick.
        
        :param open_interest_date_time_utc: The UTC timestamp of the open interest update.
        :param open_interest: The reported open interest value.
        """
        ...

    def update_quote(self, quote_date_time_utc: typing.Optional[datetime.datetime], bid_price: typing.Optional[float], bid_size: typing.Optional[float], ask_price: typing.Optional[float], ask_size: typing.Optional[float]) -> None:
        """
        Updates the best bid and ask prices and sizes.
        Constructs and publishes a quote Tick to the IDataAggregator.
        
        :param quote_date_time_utc: The UTC timestamp when the quote was received.
        :param bid_price: The best bid price.
        :param bid_size: The size available at the best bid.
        :param ask_price: The best ask price.
        :param ask_size: The size available at the best ask.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_Callable, QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Brokerages_LevelOneOrderBook__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


