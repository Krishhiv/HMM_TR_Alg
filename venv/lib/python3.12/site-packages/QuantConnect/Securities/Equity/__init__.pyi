from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Securities
import QuantConnect.Securities.Equity
import System


class Equity(QuantConnect.Securities.Security):
    """Equity Security Type : Extension of the underlying Security class for equity specific behaviours."""

    default_settlement_days: int
    """The default number of days required to settle an equity sale"""

    DEFAULT_SETTLEMENT_TIME: datetime.timedelta = ...
    """The default time of day for settlement"""

    @property
    def shortable(self) -> bool:
        """
        Checks if the equity is a shortable asset. Note that this does not
        take into account any open orders or existing holdings. To check if the asset
        is currently shortable, use QCAlgorithm's ShortableQuantity property instead.
        """
        ...

    @property
    def total_shortable_quantity(self) -> typing.Optional[int]:
        """
        Gets the total quantity shortable for this security. This does not take into account
        any open orders or existing holdings. To check the asset's currently shortable quantity,
        use QCAlgorithm's ShortableQuantity property instead.
        """
        ...

    @property
    def primary_exchange(self) -> QuantConnect.Exchange:
        """Equity primary exchange."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], exchange_hours: QuantConnect.Securities.SecurityExchangeHours, quote_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, security_cache: QuantConnect.Securities.SecurityCache, primary_exchange: QuantConnect.Exchange = None) -> None:
        """Construct the Equity Object"""
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quote_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, primary_exchange: QuantConnect.Exchange = None) -> None:
        """Construct the Equity Object"""
        ...

    def set_data_normalization_mode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        """Sets the data normalization mode to be used by this security"""
        ...


class EquityCache(QuantConnect.Securities.SecurityCache):
    """Equity cache override."""

    def __init__(self) -> None:
        """Start a new Cache for the set Index Code"""
        ...


class EquityHolding(QuantConnect.Securities.SecurityHolding):
    """Holdings class for equities securities: no specific properties here but it is a placeholder for future equities specific behaviours."""

    def __init__(self, security: QuantConnect.Securities.Security, currency_converter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Constructor for equities holdings.
        
        :param security: The security being held
        :param currency_converter: A currency converter instance
        """
        ...


class EquityDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Equity security type data filter"""

    def __init__(self) -> None:
        """Initialize Data Filter Class:"""
        ...

    def filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Equity filter the data: true - accept, false - fail.
        
        :param data: Data class
        :param vehicle: Security asset
        """
        ...


class ShortMarginInterestRateModel(System.Object, QuantConnect.Securities.IMarginInterestRateModel):
    """
    Short margin interest rate model
    
    When shorting charges the fee rate provided by the QuantConnect.Interfaces.IShortableProvider.
    When long adds the rebate fee provided by the QuantConnect.Interfaces.IShortableProvider.
    """

    @property
    def amount(self) -> float:
        """
        Accumulated shorting fee, negative means paid, positive earned.
        
        Negative due to borrowing the asset to short, the fee rate.
        Positive due to lending the asset for shorting, the rebate rate.
        """
        ...

    @amount.setter
    def amount(self, value: float) -> None:
        ...

    def apply_margin_interest_rate(self, margin_interest_rate_parameters: QuantConnect.Securities.MarginInterestRateParameters) -> None:
        """
        Apply margin interest rates to the portfolio
        
        :param margin_interest_rate_parameters: The parameters to use
        """
        ...


class EquityExchange(QuantConnect.Securities.SecurityExchange):
    """Equity exchange information"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days in an equity calendar year - 252"""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the EquityExchange class using market hours
        derived from the market-hours-database for the USA Equity market
        """
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the EquityExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchange_hours: Contains the weekly exchange schedule plus holidays
        """
        ...


