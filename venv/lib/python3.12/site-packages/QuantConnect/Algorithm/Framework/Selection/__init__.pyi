from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Python
import QuantConnect.Scheduling
import QuantConnect.Securities
import System.Collections.Generic

QuantConnect_Algorithm_Framework_Selection_UniverseSelectionModel = typing.Any


class IUniverseSelectionModel(metaclass=abc.ABCMeta):
    """Algorithm framework model that defines the universes to be used by an algorithm"""

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


class UniverseSelectionModel(QuantConnect.Python.BasePythonWrapper[QuantConnect_Algorithm_Framework_Selection_UniverseSelectionModel], QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel):
    """Provides a base class for universe selection models."""

    def __init__(self) -> None:
        """Initializes a new instance of the UniverseSelectionModel class."""
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


class FutureUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Provides an implementation of IUniverseSelectionModel that subscribes to future chains"""

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Any) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def filter(self, filter: QuantConnect.Securities.FutureFilterUniverse) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Defines the future chain universe filter
        
        
        This codeEntityType is protected.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


class FuturesUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FutureUniverseSelectionModel):
    """Provides an implementation of IUniverseSelectionModel that subscribes to future chains"""

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, future_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of FutureUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...


class CustomUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that simply
    subscribes to the specified set of symbols
    """

    @overload
    def __init__(self, name: str, selector: typing.Any) -> None:
        """
        Initializes a new instance of the CustomUniverseSelectionModel class
        for Market.USA and SecurityType.EQUITY
        using the algorithm's universe settings
        
        :param name: A unique name for this universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        """
        ...

    @overload
    def __init__(self, security_type: QuantConnect.SecurityType, name: str, market: str, selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the CustomUniverseSelectionModel class
        
        :param security_type: The security type of the universe
        :param name: A unique name for this universe
        :param market: The market of the universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        :param universe_settings: The settings used when adding symbols to the algorithm, specify null to use algorithm.UniverseSettings
        :param interval: The interval at which selection should be performed
        """
        ...

    @overload
    def __init__(self, name: str, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        """
        Initializes a new instance of the CustomUniverseSelectionModel class
        for Market.USA and SecurityType.EQUITY
        using the algorithm's universe settings
        
        :param name: A unique name for this universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        """
        ...

    @overload
    def __init__(self, security_type: QuantConnect.SecurityType, name: str, market: str, selector: typing.Callable[[datetime.datetime], typing.List[str]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the CustomUniverseSelectionModel class
        
        :param security_type: The security type of the universe
        :param name: A unique name for this universe
        :param market: The market of the universe
        :param selector: Function delegate that accepts a DateTime and returns a collection of string symbols
        :param universe_settings: The settings used when adding symbols to the algorithm, specify null to use algorithm.UniverseSettings
        :param interval: The interval at which selection should be performed
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called at algorithm start.
        
        :returns: The universes defined by this model.
        """
        ...

    def select(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[str]:
        """
        
        
        :param algorithm: 
        :param date: 
        """
        ...

    def to_string(self) -> str:
        """Returns a string that represents the current object"""
        ...


class InceptionDateUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.CustomUniverseSelectionModel):
    """
    Inception Date Universe that accepts a Dictionary of DateTime keyed by String that represent
    the Inception date for each ticker
    """

    @overload
    def __init__(self, name: str, tickers_by_date: typing.Any) -> None:
        """
        Initializes a new instance of the InceptionDateUniverseSelectionModel class
        
        :param name: A unique name for this universe
        :param tickers_by_date: Dictionary of DateTime keyed by String that represent the Inception date for each ticker
        """
        ...

    @overload
    def __init__(self, name: str, tickers_by_date: System.Collections.Generic.Dictionary[str, datetime.datetime]) -> None:
        """
        Initializes a new instance of the InceptionDateUniverseSelectionModel class
        
        :param name: A unique name for this universe
        :param tickers_by_date: Dictionary of DateTime keyed by String that represent the Inception date for each ticker
        """
        ...

    def select(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, date: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[str]:
        """Returns all tickers that are trading at current algorithm Time"""
        ...


class USTreasuriesETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following US Treasuries ETFs at their inception date
    2002-07-26   IEF    iShares 7-10 Year Treasury Bond ETF
    2002-07-26   SHY    iShares 1-3 Year Treasury Bond ETF
    2002-07-26   TLT    iShares 20+ Year Treasury Bond ETF
    2007-01-11   SHV    iShares Short Treasury Bond ETF
    2007-01-11   IEI    iShares 3-7 Year Treasury Bond ETF
    2007-01-11   TLH    iShares 10-20 Year Treasury Bond ETF
    2007-12-10   EDV    Vanguard Ext Duration Treasury ETF
    2007-05-30   BIL    SPDR Barclays 1-3 Month T-Bill ETF
    2007-05-30   SPTL   SPDR Portfolio Long Term Treasury ETF
    2008-05-01   TBT    UltraShort Barclays 20+ Year Treasury
    2009-04-16   TMF    Direxion Daily 20-Year Treasury Bull 3X
    2009-04-16   TMV    Direxion Daily 20-Year Treasury Bear 3X
    2009-08-20   TBF    ProShares Short 20+ Year Treasury
    2009-11-23   VGSH   Vanguard Short-Term Treasury ETF
    2009-11-23   VGIT   Vanguard Intermediate-Term Treasury ETF
    2009-11-24   VGLT   Vanguard Long-Term Treasury ETF
    2010-08-06   SCHO   Schwab Short-Term U.S. Treasury ETF
    2010-08-06   SCHR   Schwab Intermediate-Term U.S. Treasury ETF
    2011-12-01   SPTS   SPDR Portfolio Short Term Treasury ETF
    2012-02-24   GOVT   iShares U.S. Treasury Bond ETF
    """

    def __init__(self) -> None:
        """Initializes a new instance of the USTreasuriesETFUniverse class"""
        ...


class TechnologyETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Technology ETFs at their inception date
    1998-12-22   XLK    Technology Select Sector SPDR Fund
    1999-03-10   QQQ    Invesco QQQ
    2001-07-13   SOXX   iShares PHLX Semiconductor ETF
    2001-07-13   IGV    iShares Expanded Tech-Software Sector ETF
    2004-01-30   VGT    Vanguard Information Technology ETF
    2006-04-25   QTEC   First Trust NASDAQ 100 Technology
    2006-06-23   FDN    First Trust Dow Jones Internet Index
    2007-05-10   FXL    First Trust Technology AlphaDEX Fund
    2008-12-17   TECL   Direxion Daily Technology Bull 3X Shares
    2008-12-17   TECS   Direxion Daily Technology Bear 3X Shares
    2010-03-11   SOXL   Direxion Daily Semiconductor Bull 3x Shares
    2010-03-11   SOXS   Direxion Daily Semiconductor Bear 3x Shares
    2011-07-06   SKYY   First Trust ISE Cloud Computing Index Fund
    2011-12-21   SMH    VanEck Vectors Semiconductor ETF
    2013-08-01   KWEB   KraneShares CSI China Internet ETF
    2013-10-24   FTEC   Fidelity MSCI Information Technology Index ETF
    """

    def __init__(self) -> None:
        """Initializes a new instance of the TechnologyETFUniverse class"""
        ...


class FundamentalUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Provides a base class for defining equity coarse/fine fundamental selection models"""

    @overload
    def __init__(self, market: str, selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param market: The target market
        :param selector: Selects symbols from the provided fundamental data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param selector: Selects symbols from the provided fundamental data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the FundamentalUniverseSelectionModel class"""
        ...

    @overload
    def __init__(self, market: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param market: The target market
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, market: str, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param market: The target market
        :param selector: Selects symbols from the provided fundamental data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        :param selector: Selects symbols from the provided fundamental data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, filter_fine_data: bool) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        
        This codeEntityType is protected.
        
        Fine and Coarse selection are merged, please use 'FundamentalUniverseSelectionModel()'
        
        :param filter_fine_data: True to also filter using fine fundamental data, false to only filter on coarse data
        """
        ...

    @overload
    def __init__(self, filter_fine_data: bool, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the FundamentalUniverseSelectionModel class
        
        
        This codeEntityType is protected.
        
        Fine and Coarse selection are merged, please use 'FundamentalUniverseSelectionModel(UniverseSettings)'
        
        :param filter_fine_data: True to also filter using fine fundamental data, false to only filter on coarse data
        :param universe_settings: The settings used when adding symbols to the algorithm, specify null to use algorithm.UniverseSettings
        """
        ...

    @staticmethod
    def coarse(coarse_selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel:
        """
        Convenience method for creating a selection model that uses only coarse data
        
        
        Fine and Coarse selection are merged, please use 'Fundamental(Func<IEnumerable<Fundamental>, IEnumerable<Symbol>>)'
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :returns: A new universe selection model that will select US equities according to the selection function specified.
        """
        warnings.warn("Fine and Coarse selection are merged, please use 'Fundamental(Func<IEnumerable<Fundamental>, IEnumerable<Symbol>>)'", DeprecationWarning)

    def create_coarse_fundamental_universe(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> QuantConnect.Data.UniverseSelection.Universe:
        """
        Creates the coarse fundamental universe object.
        This is provided to allow more flexibility when creating coarse universe.
        
        :param algorithm: The algorithm instance
        :returns: The coarse fundamental universe.
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates a new fundamental universe using this class's selection functions
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universe defined by this model.
        """
        ...

    @staticmethod
    def fine(coarse_selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]], fine_selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel:
        """
        Convenience method for creating a selection model that uses coarse and fine data
        
        
        Fine and Coarse selection are merged, please use 'Fundamental(Func<IEnumerable<Fundamental>, IEnumerable<Symbol>>)'
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :param fine_selector: Selects symbols from the provided fine data set (this set has already been filtered according to the coarse selection)
        :returns: A new universe selection model that will select US equities according to the selection functions specified.
        """
        warnings.warn("Fine and Coarse selection are merged, please use 'Fundamental(Func<IEnumerable<Fundamental>, IEnumerable<Symbol>>)'", DeprecationWarning)

    @staticmethod
    def fundamental(selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.Fundamental]], typing.List[QuantConnect.Symbol]]) -> QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel:
        """
        Convenience method for creating a selection model that uses fundamental data
        
        :param selector: Selects symbols from the provided fundamental data set
        :returns: A new universe selection model that will select US equities according to the selection functions specified.
        """
        ...

    def select(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, fundamental: typing.List[QuantConnect.Data.Fundamental.Fundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Defines the fundamental selection function.
        
        :param algorithm: The algorithm instance
        :param fundamental: The fundamental data used to perform filtering
        :returns: An enumerable of symbols passing the filter.
        """
        ...

    def select_coarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Defines the coarse fundamental selection function.
        
        
        Fine and Coarse selection are merged, please use 'Select(QCAlgorithm, IEnumerable<Fundamental>)'
        
        :param algorithm: The algorithm instance
        :param coarse: The coarse fundamental data used to perform filtering
        :returns: An enumerable of symbols passing the filter.
        """
        warnings.warn("Fine and Coarse selection are merged, please use 'Select(QCAlgorithm, IEnumerable<Fundamental>)'", DeprecationWarning)

    def select_fine(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, fine: typing.List[QuantConnect.Data.Fundamental.FineFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Defines the fine fundamental selection function.
        
        
        Fine and Coarse selection are merged, please use 'Select(QCAlgorithm, IEnumerable<Fundamental>)'
        
        :param algorithm: The algorithm instance
        :param fine: The fine fundamental data used to perform filtering
        :returns: An enumerable of symbols passing the filter.
        """
        warnings.warn("Fine and Coarse selection are merged, please use 'Select(QCAlgorithm, IEnumerable<Fundamental>)'", DeprecationWarning)


class EmaCrossUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel):
    """
    Provides an implementation of FundamentalUniverseSelectionModel that subscribes
    to symbols with the larger delta by percentage between the two exponential moving average
    """

    def __init__(self, fast_period: int = 100, slow_period: int = 300, universe_count: int = 500, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the EmaCrossUniverseSelectionModel class
        
        :param fast_period: Fast EMA period
        :param slow_period: Slow EMA period
        :param universe_count: Maximum number of members of this universe selection
        :param universe_settings: The settings used when adding symbols to the algorithm, specify null to use algorithm.UniverseSettings
        """
        ...

    def select_coarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Defines the coarse fundamental selection function.
        
        :param algorithm: The algorithm instance
        :param coarse: The coarse fundamental data used to perform filtering
        :returns: An enumerable of symbols passing the filter.
        """
        ...


class LiquidETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """Universe Selection Model that adds the following ETFs at their inception date"""

    class Grouping(typing.List[QuantConnect.Symbol]):
        """Represent a collection of ETF symbols that is grouped according to a given criteria"""

        @property
        def long(self) -> typing.List[QuantConnect.Symbol]:
            """List of Symbols that follow the components direction"""
            ...

        @property
        def inverse(self) -> typing.List[QuantConnect.Symbol]:
            """List of Symbols that follow the components inverse direction"""
            ...

        def __init__(self, long_tickers: typing.List[str], inverse_tickers: typing.List[str]) -> None:
            """
            Creates a new instance of Grouping.
            
            :param long_tickers: List of tickers of ETFs that follows the components direction
            :param inverse_tickers: List of tickers of ETFs that follows the components inverse direction
            """
            ...

        def to_string(self) -> str:
            """
            Returns a string that represents the current object.
            
            :returns: A string that represents the current object.
            """
            ...

    ENERGY: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the Energy ETF Category which can be used to access the list of Long and Inverse symbols"""

    METALS: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the Metals ETF Category which can be used to access the list of Long and Inverse symbols"""

    TECHNOLOGY: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the Technology ETF Category which can be used to access the list of Long and Inverse symbols"""

    TREASURIES: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the Treasuries ETF Category which can be used to access the list of Long and Inverse symbols"""

    VOLATILITY: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the Volatility ETF Category which can be used to access the list of Long and Inverse symbols"""

    SP_500_SECTORS: QuantConnect.Algorithm.Framework.Selection.LiquidETFUniverse.Grouping = ...
    """Represents the SP500 Sectors ETF Category which can be used to access the list of Long and Inverse symbols"""

    def __init__(self) -> None:
        """Initializes a new instance of the LiquidETFUniverse class"""
        ...


class ETFConstituentsUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Universe selection model that selects the constituents of an ETF."""

    @overload
    def __init__(self, etf_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_symbol: Symbol of the ETF to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        """
        ...

    @overload
    def __init__(self, etf_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None, universe_filter_func: typing.Any = None) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_ticker: The string ETF ticker symbol
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        """
        ...

    @overload
    def __init__(self, etf_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_symbol: Symbol of the ETF to get constituents for
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        """
        ...

    @overload
    def __init__(self, etf_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], universe_filter_func: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_symbol: Symbol of the ETF to get constituents for
        :param universe_filter_func: Function to filter universe results
        """
        ...

    @overload
    def __init__(self, etf_ticker: str, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, universe_filter_func: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_ticker: The string ETF ticker symbol
        :param universe_settings: Universe settings
        :param universe_filter_func: Function to filter universe results
        """
        ...

    @overload
    def __init__(self, etf_ticker: str, universe_filter_func: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.ETFConstituentUniverse]], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the ETFConstituentsUniverseSelectionModel class
        
        :param etf_ticker: The string ETF ticker symbol
        :param universe_filter_func: Function to filter universe results
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates a new ETF constituents universe using this class's selection function
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universe defined by this model.
        """
        ...


class SP500SectorsETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following SP500 Sectors ETFs at their inception date
    1998-12-22   XLB   Materials Select Sector SPDR ETF
    1998-12-22   XLE   Energy Select Sector SPDR Fund
    1998-12-22   XLF   Financial Select Sector SPDR Fund
    1998-12-22   XLI   Industrial Select Sector SPDR Fund
    1998-12-22   XLK   Technology Select Sector SPDR Fund
    1998-12-22   XLP   Consumer Staples Select Sector SPDR Fund
    1998-12-22   XLU   Utilities Select Sector SPDR Fund
    1998-12-22   XLV   Health Care Select Sector SPDR Fund
    1998-12-22   XLY   Consumer Discretionary Select Sector SPDR Fund
    """

    def __init__(self) -> None:
        """Initializes a new instance of the SP500SectorsETFUniverse class"""
        ...


class ScheduledUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Defines a universe selection model that invokes a selector function on a specific scheduled given by an IDateRule and an ITimeRule"""

    @overload
    def __init__(self, time_zone: typing.Any, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverseSelectionModel class
        
        :param time_zone: The time zone the date/time rules are in
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Any, settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverseSelectionModel class using the algorithm's time zone
        
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, time_zone: typing.Any, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Any, settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverseSelectionModel class
        
        :param time_zone: The time zone the date/time rules are in
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    @overload
    def __init__(self, date_rule: QuantConnect.Scheduling.IDateRule, time_rule: QuantConnect.Scheduling.ITimeRule, selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the ScheduledUniverseSelectionModel class using the algorithm's time zone
        
        :param date_rule: Date rule defines what days the universe selection function will be invoked
        :param time_rule: Time rule defines what times on each day selected by date rule the universe selection function will be invoked
        :param selector: Selector function accepting the date time firing time and returning the universe selected symbols
        :param settings: Universe settings for subscriptions added via this universe, null will default to algorithm's universe settings
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...


class MetalsETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Metals ETFs at their inception date
    2004-11-18   GLD    SPDR Gold Trust
    2005-01-28   IAU    iShares Gold Trust
    2006-04-28   SLV    iShares Silver Trust
    2006-05-22   GDX    VanEck Vectors Gold Miners ETF
    2008-12-04   AGQ    ProShares Ultra Silver
    2009-11-11   GDXJ   VanEck Vectors Junior Gold Miners ETF
    2010-01-08   PPLT   Aberdeen Standard Platinum Shares ETF
    2010-12-08   NUGT   Direxion Daily Gold Miners Bull 3X Shares
    2010-12-08   DUST   Direxion Daily Gold Miners Bear 3X Shares
    2011-10-17   USLV   VelocityShares 3x Long Silver ETN
    2011-10-17   UGLD   VelocityShares 3x Long Gold ETN
    2013-10-03   JNUG   Direxion Daily Junior Gold Miners Index Bull 3x Shares
    2013-10-03   JDST   Direxion Daily Junior Gold Miners Index Bear 3X Shares
    """

    def __init__(self) -> None:
        """Initializes a new instance of the MetalsETFUniverse class"""
        ...


class VolatilityETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Volatility ETFs at their inception date
    2010-02-11   SQQQ   ProShares UltraPro ShortQQQ
    2010-02-11   TQQQ   ProShares UltraProQQQ
    2010-11-30   TVIX   VelocityShares Daily 2x VIX Short Term ETN
    2011-01-04   VIXY   ProShares VIX Short-Term Futures ETF
    2011-05-05   SPLV   Invesco S&P 500® Low Volatility ETF
    2011-10-04   SVXY   ProShares Short VIX Short-Term Futures
    2011-10-04   UVXY   ProShares Ultra VIX Short-Term Futures
    2011-10-20   EEMV   iShares Edge MSCI Min Vol Emerging Markets ETF
    2011-10-20   EFAV   iShares Edge MSCI Min Vol EAFE ETF
    2011-10-20   USMV   iShares Edge MSCI Min Vol USA ETF
    """

    def __init__(self) -> None:
        """Initializes a new instance of the VolatilityETFUniverse class"""
        ...


class OptionUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Provides an implementation of IUniverseSelectionModel that subscribes to option chains"""

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, option_chain_symbol_selector: typing.Any) -> None:
        """
        Creates a new instance of OptionUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param option_chain_symbol_selector: Selects symbols from the provided option chain
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, option_chain_symbol_selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of OptionUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param option_chain_symbol_selector: Selects symbols from the provided option chain
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, option_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]]) -> None:
        """
        Creates a new instance of OptionUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param option_chain_symbol_selector: Selects symbols from the provided option chain
        """
        ...

    @overload
    def __init__(self, refresh_interval: datetime.timedelta, option_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new instance of OptionUniverseSelectionModel
        
        :param refresh_interval: Time interval between universe refreshes
        :param option_chain_symbol_selector: Selects symbols from the provided option chain
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def filter(self, filter: QuantConnect.Securities.OptionFilterUniverse) -> QuantConnect.Securities.OptionFilterUniverse:
        """
        Defines the option chain universe filter
        
        
        This codeEntityType is protected.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


class QC500UniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel):
    """
    Defines the QC500 universe as a universe selection model for framework algorithm
    For details: https://github.com/QuantConnect/Lean/pull/1663
    """

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the QC500UniverseSelectionModel"""
        ...

    @overload
    def __init__(self, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the QC500UniverseSelectionModel
        
        :param universe_settings: Universe settings defines what subscription properties will be applied to selected securities
        """
        ...

    def select_coarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs coarse selection for the QC500 constituents.
        The stocks must have fundamental data
        The stock must have positive previous-day close price
        The stock must have positive volume on the previous trading day
        """
        ...

    def select_fine(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, fine: typing.List[QuantConnect.Data.Fundamental.FineFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Performs fine selection for the QC500 constituents
        The company's headquarter must in the U.S.
        The stock must be traded on either the NYSE or NASDAQ
        At least half a year since its initial public offering
        The stock's market cap must be greater than 500 million
        """
        ...


class EnergyETFUniverse(QuantConnect.Algorithm.Framework.Selection.InceptionDateUniverseSelectionModel):
    """
    Universe Selection Model that adds the following Energy ETFs at their inception date
    1998-12-22   XLE    Energy Select Sector SPDR Fund
    2000-06-16   IYE    iShares U.S. Energy ETF
    2004-09-29   VDE    Vanguard Energy ETF
    2006-04-10   USO    United States Oil Fund
    2006-06-22   XES    SPDR S&P Oil & Gas Equipment & Services ETF
    2006-06-22   XOP    SPDR S&P Oil & Gas Exploration & Production ETF
    2007-04-18   UNG    United States Natural Gas Fund
    2008-06-25   ICLN   iShares Global Clean Energy ETF
    2008-11-06   ERX    Direxion Daily Energy Bull 3X Shares
    2008-11-06   ERY    Direxion Daily Energy Bear 3x Shares
    2008-11-25   SCO    ProShares UltraShort Bloomberg Crude Oil
    2008-11-25   UCO    ProShares Ultra Bloomberg Crude Oil
    2009-06-02   AMJ    JPMorgan Alerian MLP Index ETN
    2010-06-02   BNO    United States Brent Oil Fund
    2010-08-25   AMLP   Alerian MLP ETF
    2011-12-21   OIH    VanEck Vectors Oil Services ETF
    2012-02-08   DGAZ   VelocityShares 3x Inverse Natural Gas
    2012-02-08   UGAZ   VelocityShares 3x Long Natural Gas
    2012-02-15   TAN    Invesco Solar ETF
    """

    def __init__(self) -> None:
        """Initializes a new instance of the EnergyETFUniverse class"""
        ...


class FineFundamentalUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel):
    """Portfolio selection model that uses coarse/fine selectors. For US equities only."""

    @overload
    def __init__(self, coarse_selector: typing.Any, fine_selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FineFundamentalUniverseSelectionModel class
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :param fine_selector: Selects symbols from the provided fine data set (this set has already been filtered according to the coarse selection)
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, coarse_selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]], fine_selector: typing.Callable[[typing.List[QuantConnect.Data.Fundamental.FineFundamental]], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the FineFundamentalUniverseSelectionModel class
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :param fine_selector: Selects symbols from the provided fine data set (this set has already been filtered according to the coarse selection)
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    def select_coarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        ...

    def select_fine(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, fine: typing.List[QuantConnect.Data.Fundamental.FineFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        ...


class OpenInterestFutureUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FutureUniverseSelectionModel):
    """
    Selects contracts in a futures universe, sorted by open interest.  This allows the selection to identifiy current
        active contract.
    """

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, future_chain_symbol_selector: typing.Any, chain_contracts_lookup_limit: typing.Optional[int] = 6, results_limit: typing.Optional[int] = 1) -> None:
        """
        Creates a new instance of OpenInterestFutureUniverseSelectionModel
        
        :param algorithm: Algorithm
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        :param chain_contracts_lookup_limit: Limit on how many contracts to query for open interest
        :param results_limit: Limit on how many contracts will be part of the universe
        """
        ...

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, future_chain_symbol_selector: typing.Callable[[datetime.datetime], typing.List[QuantConnect.Symbol]], chain_contracts_lookup_limit: typing.Optional[int] = 6, results_limit: typing.Optional[int] = 1) -> None:
        """
        Creates a new instance of OpenInterestFutureUniverseSelectionModel
        
        :param algorithm: Algorithm
        :param future_chain_symbol_selector: Selects symbols from the provided future chain
        :param chain_contracts_lookup_limit: Limit on how many contracts to query for open interest
        :param results_limit: Limit on how many contracts will be part of the universe
        """
        ...

    def filter(self, filter: QuantConnect.Securities.FutureFilterUniverse) -> QuantConnect.Securities.FutureFilterUniverse:
        """
        Defines the future chain universe filter
        
        
        This codeEntityType is protected.
        """
        ...

    def filter_by_open_interest(self, contracts: System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Symbol, QuantConnect.Securities.MarketHoursDatabase.Entry]) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Filters a set of contracts based on open interest.
        
        :param contracts: Contracts to filter
        :returns: Filtered set.
        """
        ...


class CoarseFundamentalUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.FundamentalUniverseSelectionModel):
    """Portfolio selection model that uses coarse selectors. For US equities only."""

    @overload
    def __init__(self, coarse_selector: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverseSelectionModel class
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    @overload
    def __init__(self, coarse_selector: typing.Callable[[typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]], typing.List[QuantConnect.Symbol]], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Initializes a new instance of the CoarseFundamentalUniverseSelectionModel class
        
        :param coarse_selector: Selects symbols from the provided coarse data set
        :param universe_settings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    def select_coarse(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, coarse: typing.List[QuantConnect.Data.UniverseSelection.CoarseFundamental]) -> typing.Iterable[QuantConnect.Symbol]:
        ...


class ManualUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse):
    """
    Defines a universe as a set of manually set symbols. This differs from UserDefinedUniverse
    in that these securities were not added via AddSecurity.
    """

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, symbols: typing.List[QuantConnect.Symbol]) -> None:
        """Creates a new instance of the ManualUniverse"""
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...


class CustomUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse):
    """Defines a universe as a set of dynamically set symbols."""

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, interval: datetime.timedelta, selector: typing.Callable[[datetime.datetime], typing.List[str]]) -> None:
        """Creates a new instance of the CustomUniverse"""
        ...

    def get_subscription_requests(self, security: QuantConnect.Securities.Security, current_time_utc: typing.Union[datetime.datetime, datetime.date], maximum_end_time_utc: typing.Union[datetime.datetime, datetime.date], subscription_service: QuantConnect.Interfaces.ISubscriptionDataConfigService) -> typing.Iterable[QuantConnect.Data.UniverseSelection.SubscriptionRequest]:
        """
        Gets the subscription requests to be added for the specified security
        
        :param security: The security to get subscriptions for
        :param current_time_utc: The current time in utc. This is the frontier time of the algorithm
        :param maximum_end_time_utc: The max end time
        :param subscription_service: Instance which implements ISubscriptionDataConfigService interface
        :returns: All subscriptions required by this security.
        """
        ...


class NullUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Provides a null implementation of IUniverseSelectionModel"""

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm.
        Called at algorithm start.
        
        :returns: The universes defined by this model.
        """
        ...


class ManualUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that simply
    subscribes to the specified set of symbols
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ManualUniverseSelectionModel class using the algorithm's
        security initializer and universe settings
        """
        ...

    @overload
    def __init__(self, symbols: typing.List[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the ManualUniverseSelectionModel class using the algorithm's
        security initializer and universe settings
        
        :param symbols: The symbols to subscribe to.
        Should not send in symbols at QCAlgorithm.securities since those will be managed by the UserDefinedUniverse
        """
        ...

    @overload
    def __init__(self, *symbols: typing.Union[QuantConnect.Symbol, typing.Iterable[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the ManualUniverseSelectionModel class using the algorithm's
        security initializer and universe settings
        
        :param symbols: The symbols to subscribe to
        Should not send in symbols at QCAlgorithm.securities since those will be managed by the UserDefinedUniverse
        """
        ...

    @overload
    def __init__(self, symbols: typing.List[QuantConnect.Symbol], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Initializes a new instance of the ManualUniverseSelectionModel class
        
        :param symbols: The symbols to subscribe to
        Should not send in symbols at QCAlgorithm.securities since those will be managed by the UserDefinedUniverse
        :param universe_settings: The settings used when adding symbols to the algorithm, specify null to use algorithm.UniverseSettings
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm.
        Called at algorithm start.
        
        :returns: The universes defined by this model.
        """
        ...


class CompositeUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """
    Provides an implementation of IUniverseSelectionModel that combines multiple universe
    selection models into a single model.
    """

    @overload
    def __init__(self, *universe_selection_models: typing.Union[QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel, typing.Iterable[QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel]]) -> None:
        """
        Initializes a new instance of the CompositeUniverseSelectionModel class
        
        :param universe_selection_models: The individual universe selection models defining this composite model
        """
        ...

    @overload
    def __init__(self, *universe_selection_models: typing.Union[typing.Any, typing.Iterable[typing.Any]]) -> None:
        """
        Initializes a new instance of the CompositeUniverseSelectionModel class
        
        :param universe_selection_models: The individual universe selection models defining this composite model
        """
        ...

    @overload
    def add_universe_selection(self, py_universe_selection_model: typing.Any) -> None:
        """
        Adds a new IUniverseSelectionModel
        
        :param py_universe_selection_model: The universe selection model to add
        """
        ...

    @overload
    def add_universe_selection(self, universe_selection_model: QuantConnect.Algorithm.Framework.Selection.IUniverseSelectionModel) -> None:
        """
        Adds a new IUniverseSelectionModel
        
        :param universe_selection_model: The universe selection model to add
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm.
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


class UniverseSelectionModelPythonWrapper(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """Provides an implementation of IUniverseSelectionModel that wraps a PyObject object"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the IUniverseSelectionModel class with wrapped PyObject object
        
        :param model: Model defining universes for the algorithm
        """
        ...

    def create_universes(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def get_next_refresh_time_utc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


