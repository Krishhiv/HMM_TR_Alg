from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import QuantConnect.Securities.IndexOption
import QuantConnect.Securities.Option
import System
import System.Collections.Generic


class IndexOptionSymbolProperties(QuantConnect.Securities.Option.OptionSymbolProperties):
    """Index Option Symbol Properties"""

    @property
    def minimum_price_variation(self) -> float:
        """Minimum price variation, subject to variability due to contract price"""
        ...

    @overload
    def __init__(self, description: str, quote_currency: str, contract_multiplier: float, pip_size: float, lot_size: float) -> None:
        """
        Creates an instance of index symbol properties
        
        :param description: Description of the Symbol
        :param quote_currency: Currency the price is quoted in
        :param contract_multiplier: Contract multiplier of the index option
        :param pip_size: Minimum price variation
        :param lot_size: Minimum order lot size
        """
        ...

    @overload
    def __init__(self, properties: QuantConnect.Securities.SymbolProperties) -> None:
        """
        Creates instance of index symbol properties
        
        :param properties: 
        """
        ...

    @staticmethod
    def minimum_price_variation_for_price(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], reference_price: typing.Optional[float]) -> float:
        """Minimum price variation, subject to variability due to contract price"""
        ...


class IndexOptionSymbol(System.Object):
    """Index Option Symbol"""

    SUPPORTED_INDEX_OPTION_TICKERS: System.Collections.Generic.HashSet[str] = ...
    """Supported index option tickers"""

    @staticmethod
    def get_expiry_date(ticker: str, last_trading_date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Returns the expiry date for the given index option ticker and last trading date"""
        ...

    @staticmethod
    def get_last_trading_date(ticker: str, expiration_date: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Returns the last trading date for the given index option ticker and expiration date"""
        ...

    @staticmethod
    def is_index_option(ticker: str) -> bool:
        """
        Checks if the ticker provided is a supported Index Option
        
        :param ticker: Ticker of the index option
        :returns: true if the ticker matches an index option's ticker.
        """
        ...

    @staticmethod
    def is_standard(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Determines if the Index Option Symbol is for a monthly contract
        
        :param symbol: Index Option Symbol
        :returns: True if monthly contract, false otherwise.
        """
        ...

    @staticmethod
    def map_to_underlying(index_option: str) -> str:
        """
        Maps an index option ticker to its underlying index ticker
        
        :param index_option: Index option ticker to map to the underlying
        :returns: Index ticker.
        """
        ...


class IndexOption(QuantConnect.Securities.Option.Option):
    """Index Options security"""

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.IndexOption.IndexOptionSymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, security_cache: QuantConnect.Securities.SecurityCache, underlying: QuantConnect.Securities.Security, settlement_type: QuantConnect.SettlementType = ...) -> None:
        """
        Constructor for the index option security
        
        :param symbol: Symbol of the index option
        :param exchange_hours: Exchange hours of the index option
        :param quote_currency: Quoted currency of the index option
        :param symbol_properties: Symbol properties of the index option
        :param currency_converter: Currency converter
        :param registered_types: Provides all data types registered to the algorithm
        :param security_cache: Cache of security objects
        :param underlying: Future underlying security
        :param settlement_type: Settlement type for the index option. Most index options are cash-settled.
        """
        ...

    def update_consumers_market_price(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Consumes market price data and updates the minimum price variation
        
        
        This codeEntityType is protected.
        
        :param data: Market price data
        """
        ...


class IndexOptionPriceVariationModel(System.Object, QuantConnect.Securities.IPriceVariationModel):
    """The index option price variation model"""

    def get_minimum_price_variation(self, parameters: QuantConnect.Securities.GetMinimumPriceVariationParameters) -> float:
        """
        Get the minimum price variation from a security
        
        :param parameters: An object containing the method parameters
        :returns: Decimal minimum price variation of a given security.
        """
        ...


