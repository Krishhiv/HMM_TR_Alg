from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import QuantConnect.Securities.Crypto


class Crypto(QuantConnect.Securities.Security, QuantConnect.Securities.IBaseCurrencySymbol):
    """Crypto Security Object Implementation for Crypto Assets"""

    @property
    def base_currency(self) -> QuantConnect.Securities.Cash:
        """Gets the currency acquired by going long this currency pair"""
        ...

    @base_currency.setter
    def base_currency(self, value: QuantConnect.Securities.Cash) -> None:
        ...

    @property
    def price(self) -> float:
        """Get the current value of the security."""
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, base_currency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the Crypto security
        
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
        Constructor for the Crypto security
        
        :param symbol: The security's symbol
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param base_currency: The cash object that represent the base currency
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
        instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        :param security_cache: Cache to store Security data
        """
        ...

    @staticmethod
    def decompose_currency_pair(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], symbol_properties: QuantConnect.Securities.SymbolProperties, base_currency: typing.Optional[str], quote_currency: typing.Optional[str]) -> typing.Tuple[None, str, str]:
        """
        Decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param symbol: The input symbol to be decomposed
        :param symbol_properties: The symbol properties for this security
        :param base_currency: The output base currency
        :param quote_currency: The output quote currency
        """
        ...


class CryptoHolding(QuantConnect.Securities.SecurityHolding):
    """Crypto holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Crypto.Crypto, currency_converter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Crypto Holding Class
        
        :param security: The Crypto security being held
        :param currency_converter: A currency converter instance
        """
        ...


class CryptoExchange(QuantConnect.Securities.SecurityExchange):
    """Crypto exchange class - information and helper tools for Crypto exchange properties"""

    @overload
    def __init__(self, market: str) -> None:
        """
        Initializes a new instance of the CryptoExchange class using market hours
        derived from the market-hours-database for the Crypto market
        """
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the CryptoExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchange_hours: Contains the weekly exchange schedule plus holidays
        """
        ...


