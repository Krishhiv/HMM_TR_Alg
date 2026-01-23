from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Securities
import QuantConnect.Securities.Future
import System
import System.Collections.Generic


class FuturesOptionsSymbolMappings(System.Object):
    """Provides conversions from a GLOBEX Futures ticker to a GLOBEX Futures Options ticker"""

    @staticmethod
    def map(future_ticker: str) -> str:
        """
        Returns the futures options ticker for the given futures ticker.
        
        :param future_ticker: Future GLOBEX ticker to get Future Option GLOBEX ticker for
        :returns: Future option ticker. Defaults to future ticker provided if no entry is found.
        """
        ...

    @staticmethod
    def map_from_option(future_option_ticker: str) -> str:
        """
        Maps a futures options ticker to its underlying future's ticker
        
        :param future_option_ticker: Future option ticker to map to the underlying
        :returns: Future ticker.
        """
        ...


class FutureMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """Represents a simple margin model for margin futures. Margin file contains Initial and Maintenance margins"""

    @property
    def enable_intraday_margins(self) -> bool:
        """True will enable usage of intraday margins."""
        ...

    @enable_intraday_margins.setter
    def enable_intraday_margins(self, value: bool) -> None:
        ...

    @property
    def initial_overnight_margin_requirement(self) -> float:
        """Initial Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def maintenance_overnight_margin_requirement(self) -> float:
        """Maintenance Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def initial_intraday_margin_requirement(self) -> float:
        """Initial Intraday margin for the contract effective from the date of change"""
        ...

    @property
    def maintenance_intraday_margin_requirement(self) -> float:
        """Maintenance Intraday margin requirement for the contract effective from the date of change"""
        ...

    def __init__(self, required_free_buying_power_percent: float = 0, security: QuantConnect.Securities.Security = None) -> None:
        """
        Initializes a new instance of the FutureMarginModel
        
        :param required_free_buying_power_percent: The percentage used to determine the required unused buying power for the account.
        :param security: The security that this model belongs to
        """
        ...

    def get_initial_margin_required_for_order(self, parameters: QuantConnect.Securities.InitialMarginRequiredForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def get_initial_margin_requirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """The margin that must be held in order to increase the position by the provided quantity"""
        ...

    def get_leverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def get_maintenance_margin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allotted to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def get_maximum_order_quantity_for_target_buying_power(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given buying power percentage.
        Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the security and the target signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def set_leverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, futures
        
        :param security: 
        :param leverage: The new leverage
        """
        ...


class FuturesListings(System.Object):
    """
    Helpers for getting the futures contracts that are trading on a given date.
    This is a substitute for the BacktestingFutureChainProvider, but
    does not outright replace it because of missing entries. This will resolve
    the listed contracts without having any data in place. We follow the listing rules
    set forth by the exchange to get the Symbols that are listed at a given date.
    """

    @staticmethod
    def listed_contracts(future_ticker: str, time: typing.Union[datetime.datetime, datetime.date]) -> typing.List[QuantConnect.Symbol]:
        """
        Gets the listed futures contracts on a given date
        
        :param future_ticker: Ticker of the future contract
        :param time: Contracts to look up that are listed at that time
        :returns: The currently trading contracts on the exchange.
        """
        ...


class Future(QuantConnect.Securities.Security, QuantConnect.Securities.IContinuousSecurity):
    """Futures Security Object Implementation for Futures Assets"""

    @property
    def is_tradable(self) -> bool:
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @is_tradable.setter
    def is_tradable(self, value: bool) -> None:
        ...

    DEFAULT_SETTLEMENT_DAYS: int = 1
    """The default number of days required to settle a futures sale"""

    DEFAULT_SETTLEMENT_TIME: datetime.timedelta = ...
    """The default time of day for settlement"""

    @property
    def is_future_chain(self) -> bool:
        """Returns true if this is the future chain security, false if it is a specific future contract"""
        ...

    @property
    def is_future_contract(self) -> bool:
        """Returns true if this is a specific future contract security, false if it is the future chain security"""
        ...

    @property
    def expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def settlement_type(self) -> QuantConnect.SettlementType:
        """Specifies if futures contract has physical or cash settlement on settlement"""
        ...

    @settlement_type.setter
    def settlement_type(self, value: QuantConnect.SettlementType) -> None:
        ...

    @property
    def mapped(self) -> QuantConnect.Symbol:
        """Gets or sets the currently mapped symbol for the security"""
        ...

    @mapped.setter
    def mapped(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def contract_filter(self) -> QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect.Data.UniverseSelection.FutureUniverse]:
        """Gets or sets the contract filter"""
        ...

    @contract_filter.setter
    def contract_filter(self, value: QuantConnect.Securities.IDerivativeSecurityFilter[QuantConnect.Data.UniverseSelection.FutureUniverse]) -> None:
        ...

    @overload
    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quote_currency: QuantConnect.Securities.Cash, symbol_properties: QuantConnect.Securities.SymbolProperties, currency_converter: QuantConnect.Securities.ICurrencyConverter, registered_types: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the Future security
        
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
        Constructor for the Future security
        
        :param symbol: The subscription security symbol
        :param exchange_hours: Defines the hours this exchange is open
        :param quote_currency: The cash object that represent the quote currency
        :param symbol_properties: The symbol properties for this security
        :param currency_converter: Currency converter used to convert CashAmount
            instances into units of the account currency
        :param registered_types: Provides all data types registered in the algorithm
        :param security_cache: Cache to store security information
        """
        ...

    @overload
    def set_filter(self, universe_func: typing.Any) -> None:
        """
        Sets the contract_filter to a new universe selection function
        
        :param universe_func: new universe selection function
        """
        ...

    @overload
    def set_filter(self, min_expiry: datetime.timedelta, max_expiry: datetime.timedelta) -> None:
        """
        Sets the contract_filter to a new instance of the filter
        using the specified expiration range values
        
        :param min_expiry: The minimum time until expiry to include, for example, TimeSpan.FromDays(10)
        would exclude contracts expiring in less than 10 days
        :param max_expiry: The maximum time until expiry to include, for example, TimeSpan.FromDays(10)
        would exclude contracts expiring in more than 10 days
        """
        ...

    @overload
    def set_filter(self, min_expiry_days: int, max_expiry_days: int) -> None:
        """
        Sets the contract_filter to a new instance of the filter
        using the specified expiration range values
        
        :param min_expiry_days: The minimum time, expressed in days, until expiry to include, for example, 10
        would exclude contracts expiring in less than 10 days
        :param max_expiry_days: The maximum time, expressed in days, until expiry to include, for example, 10
        would exclude contracts expiring in more than 10 days
        """
        ...

    @overload
    def set_filter(self, universe_func: typing.Callable[[QuantConnect.Securities.FutureFilterUniverse], QuantConnect.Securities.FutureFilterUniverse]) -> None:
        """
        Sets the contract_filter to a new universe selection function
        
        :param universe_func: new universe selection function
        """
        ...

    def set_local_time_keeper(self, local_time_keeper: QuantConnect.LocalTimeKeeper) -> None:
        """
        Sets the LocalTimeKeeper to be used for this Security.
        This is the source of this instance's time.
        
        :param local_time_keeper: The source of this Security's time.
        """
        ...


class MarginRequirementsEntry(System.Object):
    """POCO class for modeling margin requirements at given date"""

    @property
    def date(self) -> datetime.datetime:
        """Date of margin requirements change"""
        ...

    @property
    def initial_overnight(self) -> float:
        """Initial overnight margin for the contract effective from the date of change"""
        ...

    @property
    def maintenance_overnight(self) -> float:
        """Maintenance overnight margin for the contract effective from the date of change"""
        ...

    @property
    def initial_intraday(self) -> float:
        """Initial intraday margin for the contract effective from the date of change"""
        ...

    @property
    def maintenance_intraday(self) -> float:
        """Maintenance intraday margin for the contract effective from the date of change"""
        ...

    @staticmethod
    def create(csv_line: str) -> QuantConnect.Securities.Future.MarginRequirementsEntry:
        """
        Creates a new instance of MarginRequirementsEntry from the specified csv line
        
        :param csv_line: The csv line to be parsed
        :returns: A new MarginRequirementsEntry for the specified csv line.
        """
        ...


class FutureCache(QuantConnect.Securities.SecurityCache):
    """Future specific caching support"""

    @property
    def settlement_price(self) -> float:
        """The current settlement price"""
        ...

    @settlement_price.setter
    def settlement_price(self, value: float) -> None:
        ...

    def process_data_point(self, data: QuantConnect.Data.BaseData, cache_by_type: bool) -> None:
        """
        Will consume the given data point updating the cache state and it's properties
        
        
        This codeEntityType is protected.
        
        :param data: The data point to process
        :param cache_by_type: True if this data point should be cached by type
        """
        ...


class FutureSettlementModel(QuantConnect.Securities.ImmediateSettlementModel):
    """Settlement model which can handle daily profit and loss settlement"""

    def apply_funds(self, apply_funds_parameters: QuantConnect.Securities.ApplyFundsSettlementModelParameters) -> None:
        """
        Applies unsettledContractsTodaysProfit settlement rules
        
        :param apply_funds_parameters: The funds application parameters
        """
        ...

    def scan(self, settlement_parameters: QuantConnect.Securities.ScanSettlementModelParameters) -> None:
        """
        Scan for pending settlements
        
        :param settlement_parameters: The settlement parameters
        """
        ...

    def set_local_date_time_frontier(self, new_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the current datetime in terms of the exchange's local time zone
        
        :param new_local_time: Current local time
        """
        ...


class FuturesExpiryUtilityFunctions(System.Object):
    """Class to implement common functions used in FuturesExpiryFunctions"""

    @staticmethod
    def add_business_days(time: typing.Union[datetime.datetime, datetime.date], n: int, holidays: System.Collections.Generic.HashSet[datetime.datetime]) -> datetime.datetime:
        """
        Method to retrieve n^th succeeding/preceding business day for a given day
        
        :param time: The current Time
        :param n: Number of business days succeeding current time. Use negative value for preceding business days
        :param holidays: Set of holidays to exclude. These should be sourced from the MarketHoursDatabase
        :returns: The date-time after adding n business days.
        """
        ...

    @staticmethod
    def add_business_days_if_holiday(time: typing.Union[datetime.datetime, datetime.date], n: int, holiday_list: System.Collections.Generic.HashSet[datetime.datetime]) -> datetime.datetime:
        """
        Method to retrieve n^th succeeding/preceding business day for a given day if there was a holiday on that day
        
        :param time: The current Time
        :param n: Number of business days succeeding current time. Use negative value for preceding business days
        :param holiday_list: Enumerable of holidays to exclude. These should be sourced from the MarketHoursDatabase
        :returns: The date-time after adding n business days.
        """
        ...

    @staticmethod
    def get_delta_between_contract_month_and_contract_expiry(underlying: str, future_expiry_date: typing.Optional[datetime.datetime] = None) -> int:
        """
        Gets the number of months between the contract month and the expiry date.
        
        :param underlying: The future symbol ticker
        :param future_expiry_date: Expiry date to use to look up contract month delta. Only used for dairy, since we need to lookup its contract month in a pre-defined table.
        :returns: The number of months between the contract month and the contract expiry.
        """
        ...

    @staticmethod
    def get_future_contract_month(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> datetime.datetime:
        """Helper method to retrieve the futures contract month"""
        ...

    @staticmethod
    @overload
    def get_future_expiration_from_contract_month(symbol: str, market: str, contract_month: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Helper method to resolve a future expiration from it's contract month"""
        ...

    @staticmethod
    @overload
    def get_future_expiration_from_contract_month(future: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], contract_month: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Helper method to resolve a future expiration from it's contract month"""
        ...

    @staticmethod
    def last_friday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the last Friday of any month
        
        :param time: Date from the given month
        :returns: Last Friday of the given month.
        """
        ...

    @staticmethod
    def last_thursday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the last Thursday of any month
        
        :param time: Date from the given month
        :returns: Last Thursday of the given month.
        """
        ...

    @staticmethod
    def last_weekday(time: typing.Union[datetime.datetime, datetime.date], day_of_week: System.DayOfWeek) -> datetime.datetime:
        """
        Method to retrieve the last weekday of any month
        
        :param time: Date from the given month
        :param day_of_week: the last weekday to be found
        :returns: Last day of the we.
        """
        ...

    @staticmethod
    def not_holiday(time: typing.Union[datetime.datetime, datetime.date], holiday_list: typing.List[datetime.datetime]) -> bool:
        """
        Method to check whether a given time is holiday or not
        
        :param time: The DateTime for consideration
        :param holiday_list: Enumerable of holidays to exclude. These should be sourced from the MarketHoursDatabase
        :returns: True if the time is not a holidays, otherwise returns false.
        """
        ...

    @staticmethod
    def not_preceded_by_holiday(thursday: typing.Union[datetime.datetime, datetime.date], holiday_list: typing.List[datetime.datetime]) -> bool:
        """
        This function takes Thursday as input and returns true if four weekdays preceding it are not Holidays
        
        :param thursday: DateTime of a given Thursday
        :param holiday_list: Enumerable of holidays to exclude. These should be sourced from the MarketHoursDatabase
        :returns: False if DayOfWeek is not Thursday or is not preceded by four weekdays,Otherwise returns True.
        """
        ...

    @staticmethod
    def nth_business_day(time: typing.Union[datetime.datetime, datetime.date], nth_business_day: int, holiday_list: typing.List[datetime.datetime]) -> datetime.datetime:
        """
        Calculates the n^th business day of the month (includes checking for holidays)
        
        :param time: Month to calculate business day for
        :param nth_business_day: n^th business day to get
        :param holiday_list: Holidays to not count as business days
        :returns: Nth business day of the month.
        """
        ...

    @staticmethod
    def nth_friday(time: typing.Union[datetime.datetime, datetime.date], n: int) -> datetime.datetime:
        """
        Method to retrieve the Nth Friday of the given month
        
        :param time: Date from the given month
        :param n: The order of the Friday in the period
        :returns: Nth Friday of given month.
        """
        ...

    @staticmethod
    def nth_last_business_day(time: typing.Union[datetime.datetime, datetime.date], n: int, holiday_list: typing.List[datetime.datetime]) -> datetime.datetime:
        """
        Method to retrieve the n^th last business day of the delivery month.
        
        :param time: DateTime for delivery month
        :param n: Number of days
        :param holiday_list: Holidays to use while calculating n^th business day. Useful for MHDB entries
        :returns: Nth Last Business day of the month.
        """
        ...

    @staticmethod
    def nth_weekday(time: typing.Union[datetime.datetime, datetime.date], n: int, day_of_week: System.DayOfWeek) -> datetime.datetime:
        """
        Method to retrieve the Nth Weekday of the given month
        
        :param time: Date from the given month
        :param n: The order of the Weekday in the period
        :param day_of_week: The day of the week
        :returns: Nth Weekday of given month.
        """
        ...

    @staticmethod
    def second_friday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the 2nd Friday of the given month
        
        :param time: Date from the given month
        :returns: 2nd Friday of given month.
        """
        ...

    @staticmethod
    @overload
    def third_friday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the 3rd Friday of the given month
        
        :param time: Date from the given month
        :returns: 3rd Friday of given month.
        """
        ...

    @staticmethod
    @overload
    def third_friday(time: typing.Union[datetime.datetime, datetime.date], contract: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> datetime.datetime:
        """This function returns the third Friday of the month, adjusted for holidays and weekends."""
        ...

    @staticmethod
    def third_wednesday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve third Wednesday of the given month (usually Monday).
        
        :param time: Date from the given month
        :returns: Third Wednesday of the given month.
        """
        ...


class FutureExchange(QuantConnect.Securities.SecurityExchange):
    """Future exchange class - information and helper tools for future exchange properties"""

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for this security, 252."""
        ...

    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the FutureExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchange_hours: Contains the weekly exchange schedule plus holidays
        """
        ...


class FutureSymbol(System.Object):
    """Static class contains common utility methods specific to symbols representing the future contracts"""

    @staticmethod
    def is_standard(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Determine if a given Futures contract is a standard contract.
        
        :param symbol: Future symbol
        :returns: True if symbol expiration matches standard expiration.
        """
        ...

    @staticmethod
    def is_weekly(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Returns true if the future contract is a weekly contract
        
        :param symbol: Future symbol
        :returns: True if symbol is non-standard contract.
        """
        ...


class FuturesExpiryFunctions(System.Object):
    """Calculate the date of a futures expiry given an expiry month and year"""

    FUTURES_EXPIRY_DICTIONARY: System.Collections.Generic.Dictionary[QuantConnect.Symbol, typing.Callable[[datetime.datetime], datetime.datetime]] = ...
    """
    Dictionary of the Functions that calculates the expiry for a given year and month.
    It does not matter what the day and time of day are passed into the Functions.
    The Functions is responsible for calculating the day and time of day given a year and month
    """

    @staticmethod
    def futures_expiry_function(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> typing.Callable[[datetime.datetime], datetime.datetime]:
        """Method to retrieve the Function for a specific future symbol"""
        ...


class FutureHolding(QuantConnect.Securities.SecurityHolding):
    """Future holdings implementation of the base securities class"""

    @property
    def settled_profit(self) -> float:
        """The cash settled profit for the current open position"""
        ...

    @settled_profit.setter
    def settled_profit(self, value: float) -> None:
        ...

    @property
    def unsettled_profit(self) -> float:
        """Unsettled profit for the current open position settled_profit"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, currency_converter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Future Holding Class constructor
        
        :param security: The future security being held
        :param currency_converter: A currency converter instance
        """
        ...


class EmptyFutureChainProvider(System.Object, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that always returns an empty list of contracts"""

    def get_future_contract_list(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


