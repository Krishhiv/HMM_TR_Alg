from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import QuantConnect.Securities.Index
import System


class IndexExchange(QuantConnect.Securities.SecurityExchange):
    """INDEX exchange class - information and helper tools for Index exchange properties"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security, used for performance statistics."""
        ...

    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the IndexExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchange_hours: Contains the weekly exchange schedule plus holidays
        """
        ...


class Index(QuantConnect.Securities.Security):
    """INDEX Security Object Implementation for INDEX Assets"""

    @property
    def is_tradable(self) -> bool:
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @is_tradable.setter
    def is_tradable(self, value: bool) -> None:
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the INDEX security
        
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param config: The subscription configuration for this security
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
        instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, security_cache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Constructor for the INDEX security
        
        :param symbol: The security's symbol
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
        instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        :param security_cache: Cache to store security information
        """
        ...

    def reset(self) -> None:
        """
        Resets the security to its initial state by marking it as uninitialized and non-tradable
        and clearing the subscriptions.
        """
        ...


class IndexHolding(QuantConnect.Securities.SecurityHolding):
    """Index holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Index.Index, currency_converter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        INDEX Holding Class constructor
        
        :param security: The INDEX security being held
        :param currency_converter: A currency converter instance
        """
        ...


class IndexCache(QuantConnect.Securities.SecurityCache):
    """INDEX specific caching support"""


class IndexDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Index packet by packet data filtering mechanism for dynamically detecting bad ticks."""


class IndexSymbol(System.Object):
    """Helper methods for Index Symbols"""

    @staticmethod
    def get_index_exchange(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """
        Gets the actual exchange the index lives on
        
        :returns: The exchange of the index.
        """
        ...

    @staticmethod
    def try_get_index_market(ticker: str, market: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """
        Gets the lean market for this index ticker
        
        :returns: The market of the index.
        """
        ...


