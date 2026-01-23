from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import QuantConnect.Securities.Forex


class ForexCache(QuantConnect.Securities.SecurityCache):
    """Forex specific caching support"""

    def __init__(self) -> None:
        """Initialize forex cache"""
        ...


class ForexDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Forex packet by packet data filtering mechanism for dynamically detecting bad ticks."""

    def __init__(self) -> None:
        """Initialize forex data filter class:"""
        ...

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Forex data filter: a true value means accept the packet, a false means fail.
        
        :param data: Data object we're scanning to filter
        :param vehicle: Security asset
        """
        ...


class ForexExchange(QuantConnect.Securities.SecurityExchange):
    """Forex exchange class - information and helper tools for forex exchange properties"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security, used for performance statistics."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ForexExchange class using market hours
        derived from the market-hours-database for the FXCM Forex market
        """
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the ForexExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchange_hours: Contains the weekly exchange schedule plus holidays
        """
        ...


class Forex(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """FOREX Security Object Implementation for FOREX Assets"""

    @property
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...

    @base_currency.setter
    def base_currency(self, value: QuantConnect.Securities.Cash) -> None:
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, base_currency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the forex security
        
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param base_currency: The cash object that represent the base currency
        :param config: The subscription configuration for this security
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
        instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, base_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, security_cache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Constructor for the forex security
        
        :param symbol: The security's symbol
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param base_currency: The cash object that represent the base currency
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
        instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        :param security_cache: Cache for storing Security data
        """
        ...

    @staticmethod
    def decompose_currency_pair(currency_pair: str, base_currency: typing.Optional[str], quote_currency: typing.Optional[str]) -> typing.Tuple[None, str, str]:
        """
        Decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param currency_pair: The input currency pair to be decomposed, for example, "EURUSD"
        :param base_currency: The output base currency
        :param quote_currency: The output quote currency
        """
        ...


class ForexHolding(QuantConnect.Securities.SecurityHolding):
    """FOREX holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Forex.Forex, currency_converter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Forex Holding Class
        
        :param security: The forex security being held
        :param currency_converter: A currency converter instance
        """
        ...

    def total_close_profit_pips(self) -> float:
        """Profit in pips if we closed the holdings right now including the approximate fees"""
        ...


