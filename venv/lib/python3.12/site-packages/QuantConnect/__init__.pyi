from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Brokerages
import QuantConnect.Commands
import QuantConnect.Data
import QuantConnect.Data.Auxiliary
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Exceptions
import QuantConnect.Indicators
import QuantConnect.Interfaces
import QuantConnect.Optimizer.Objectives
import QuantConnect.Orders
import QuantConnect.Orders.Fills
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Option
import QuantConnect.Securities.Positions
import QuantConnect.Statistics
import QuantConnect.Util
import System
import System.Collections
import System.Collections.Generic
import System.Drawing
import System.Globalization
import System.IO
import System.Net
import System.Reflection
import System.Text
import System.Threading
import System.Threading.Tasks
import System.Timers

QuantConnect_Symbol = typing.Any
DateTimeZone = typing.Any
QuantConnect_SecurityIdentifier = typing.Any
ZipArchiveMode = typing.Any
CompressionLevel = typing.Any

QuantConnect_ExtendedDictionary_TKey = typing.TypeVar("QuantConnect_ExtendedDictionary_TKey")
QuantConnect_ExtendedDictionary_TValue = typing.TypeVar("QuantConnect_ExtendedDictionary_TValue")
QuantConnect__EventContainer_Callable = typing.TypeVar("QuantConnect__EventContainer_Callable")
QuantConnect__EventContainer_ReturnType = typing.TypeVar("QuantConnect__EventContainer_ReturnType")


class StubsIgnoreAttribute(System.Attribute):
    """
    P
    Custom attribute used for marking classes, methods, properties, etc. that should be ignored by the stubs generator
    """


class IsolatorLimitResult(System.Object):
    """Represents the result of the Isolator limiter callback"""

    @property
    def current_time_step_elapsed(self) -> datetime.timedelta:
        """Gets the amount of time spent on the current time step"""
        ...

    @property
    def error_message(self) -> str:
        """Gets the error message or an empty string if no error on the current time step"""
        ...

    @property
    def is_within_custom_limits(self) -> bool:
        """Returns true if there are no errors in the current time step"""
        ...

    def __init__(self, current_time_step_elapsed: datetime.timedelta, error_message: str) -> None:
        """
        Initializes a new instance of the IsolatorLimitResult class
        
        :param current_time_step_elapsed: The amount of time spent on the current time step
        :param error_message: The error message or an empty string if no error on the current time step
        """
        ...


class Isolator(System.Object):
    """
    Isolator class - create a new instance of the algorithm and ensure it doesn't
    exceed memory or time execution limits.
    """

    @property
    def cancellation_token_source(self) -> System.Threading.CancellationTokenSource:
        """Algo cancellation controls - cancel source."""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the Isolator class"""
        ...

    @overload
    def execute_with_time_limit(self, time_span: datetime.timedelta, within_custom_limits: typing.Callable[[], QuantConnect.IsolatorLimitResult], code_block: typing.Callable[[], typing.Any], memory_cap: int = 1024, sleep_interval_millis: int = 1000, worker_thread: QuantConnect.Util.WorkerThread = None) -> bool:
        """
        Execute a code block with a maximum limit on time and memory.
        
        :param time_span: Timeout in timespan
        :param within_custom_limits: Function used to determine if the code_block is within custom limits, such as with algorithm manager
        timing individual time loops, return a non-null and non-empty string with a message indicating the error/reason for stoppage
        :param code_block: Action codeblock to execute
        :param memory_cap: Maximum memory allocation, default 1024Mb
        :param sleep_interval_millis: Sleep interval between each check in ms
        :param worker_thread: The worker thread instance that will execute the provided action, if null
        will use a Task
        :returns: True if algorithm exited successfully, false if cancelled because it exceeded limits.
        """
        ...

    @overload
    def execute_with_time_limit(self, time_span: datetime.timedelta, code_block: typing.Callable[[], typing.Any], memory_cap: int, sleep_interval_millis: int = 1000, worker_thread: QuantConnect.Util.WorkerThread = None) -> bool:
        """
        Execute a code block with a maximum limit on time and memory.
        
        :param time_span: Timeout in timespan
        :param code_block: Action codeblock to execute
        :param memory_cap: Maximum memory allocation, default 1024Mb
        :param sleep_interval_millis: Sleep interval between each check in ms
        :param worker_thread: The worker thread instance that will execute the provided action, if null
        will use a Task
        :returns: True if algorithm exited successfully, false if cancelled because it exceeded limits.
        """
        ...


class Field(System.Object):
    """Provides static properties to be used as selectors with the indicator system"""

    BID_CLOSE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Bid close price"""

    BID_OPEN: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Bid open price"""

    BID_LOW: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Bid low price"""

    BID_HIGH: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Bid high price"""

    ASK_CLOSE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Ask close price"""

    ASK_OPEN: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Ask open price"""

    ASK_LOW: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Ask low price"""

    ASK_HIGH: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Ask high price"""

    ASK_PRICE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Ask price"""

    BID_PRICE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectes the Bid price"""

    OPEN: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selects the Open value"""

    HIGH: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selects the High value"""

    LOW: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selects the Low value"""

    CLOSE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selects the Close value"""

    AVERAGE: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Defines an average price that is equal to (O + H + L + C) / 4"""

    MEDIAN: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Defines an average price that is equal to (H + L) / 2"""

    TYPICAL: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Defines an average price that is equal to (H + L + C) / 3"""

    WEIGHTED: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Defines an average price that is equal to (H + L + 2*C) / 4"""

    SEVEN_BAR: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Defines an average price that is equal to (2*O + H + L + 3*C)/7"""

    VOLUME: typing.Callable[[QuantConnect.Data.IBaseData], float]
    """Gets a selector that selectors the Volume value"""


class DefaultConverter:
    """Helper json converter to use the default json converter, breaking inheritance json converter"""

    @property
    def can_read(self) -> bool:
        """Indicates if this object can be read"""
        ...

    @property
    def can_write(self) -> bool:
        """Indicates if this object can be written"""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """Indicates if the given type can be assigned to this object"""
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Creates an object from a given JSON reader and other arguments"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Writes a JSON file from the given object and the other arguments"""
        ...


class StubsAvoidImplicitsAttribute(System.Attribute):
    """
    Custom attribute used for marking properties, fields or arguments types that should not
    be expanded to include other types they can be implicitly converted to.
    """


class SecurityType(IntEnum):
    """Type of tradable security / underlying asset"""

    BASE = 0
    """Base class for all security types (0)"""

    EQUITY = 1
    """US Equity Security (1)"""

    OPTION = 2
    """Option Security Type (2)"""

    COMMODITY = 3
    """Commodity Security Type (3)"""

    FOREX = 4
    """FOREX Security (4)"""

    FUTURE = 5
    """Future Security Type (5)"""

    CFD = 6
    """Contract For a Difference Security Type (6)"""

    CRYPTO = 7
    """Cryptocurrency Security Type (7)"""

    FUTURE_OPTION = 8
    """Futures Options Security Type (8)"""

    INDEX = 9
    """Index Security Type (9)"""

    INDEX_OPTION = 10
    """Index Option Security Type (10)"""

    CRYPTO_FUTURE = 11
    """Crypto Future Type (11)"""


class OptionRight(IntEnum):
    """Specifies the different types of options"""

    CALL = 0
    """A call option, the right to buy at the strike price (0)"""

    PUT = 1
    """A put option, the right to sell at the strike price (1)"""


class OptionStyle(IntEnum):
    """Specifies the style of an option"""

    AMERICAN = 0
    """American style options are able to be exercised at any time on or before the expiration date (0)"""

    EUROPEAN = 1
    """European style options are able to be exercised on the expiration date only (1)"""


class SecurityIdentifier(System.Object, System.IEquatable[QuantConnect_SecurityIdentifier], System.IComparable[QuantConnect_SecurityIdentifier]):
    """Defines a unique identifier for securities"""

    EMPTY: QuantConnect.SecurityIdentifier = ...
    """Gets an instance of SecurityIdentifier that is empty, that is, one with no symbol specified"""

    NONE: QuantConnect.SecurityIdentifier = ...
    """Gets an instance of SecurityIdentifier that is explicitly no symbol"""

    DEFAULT_DATE: datetime.datetime = ...
    """Gets the date to be used when it does not apply."""

    INVALID_SYMBOL_CHARACTERS: System.Collections.Generic.HashSet[str] = ...
    """Gets the set of invalids symbol characters"""

    @property
    def has_underlying(self) -> bool:
        """
        Gets whether or not this SecurityIdentifier is a derivative,
        that is, it has a valid underlying property
        """
        ...

    @property
    def underlying(self) -> QuantConnect.SecurityIdentifier:
        """
        Gets the underlying security identifier for this security identifier. When there is
        no underlying, this property will return a value of EMPTY.
        """
        ...

    @property
    def date(self) -> datetime.datetime:
        """
        Gets the date component of this identifier. For equities this
        is the first date the security traded. Technically speaking,
        in LEAN, this is the first date mentioned in the map_files.
        For futures and options this is the expiry date of the contract.
        For other asset classes, this property will throw an
        exception as the field is not specified.
        """
        ...

    @property
    def symbol(self) -> str:
        """
        Gets the original symbol used to generate this security identifier.
        For equities, by convention this is the first ticker symbol for which
        the security traded
        """
        ...

    @property
    def market(self) -> str:
        """
        Gets the market component of this security identifier. If located in the
        internal mappings, the full string is returned. If the value is unknown,
        the integer value is returned as a string.
        """
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the security type component of this security identifier."""
        ...

    @property
    def strike_price(self) -> float:
        """
        Gets the option strike price. This only applies if SecurityType is Option,
        IndexOption or FutureOption and will thrown anexception if accessed otherwise.
        """
        ...

    @property
    def option_right(self) -> QuantConnect.OptionRight:
        """
        Gets the option type component of this security identifier. This
        only applies if SecurityType is Option, IndexOption or FutureOption
        and will throw an exception if accessed otherwise.
        """
        ...

    @property
    def option_style(self) -> QuantConnect.OptionStyle:
        """
        Gets the option style component of this security identifier. This
        only applies if SecurityType is Option, IndexOption or FutureOption
        and will throw an exception if accessed otherwise.
        """
        ...

    def __eq__(self, right: QuantConnect.SecurityIdentifier) -> bool:
        """Override equals operator"""
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: QuantConnect.SecurityIdentifier) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: QuantConnect.SecurityIdentifier) -> bool:
        ...

    @overload
    def __init__(self, symbol: str, properties: int) -> None:
        """
        Initializes a new instance of the SecurityIdentifier class
        
        :param symbol: The base36 string encoded as a long using alpha <0-9A-Z>
        :param properties: Other data defining properties of the symbol including market,
        security type, listing or expiry date, strike/call/put/style for options, ect...
        """
        ...

    @overload
    def __init__(self, symbol: str, properties: int, underlying: QuantConnect.SecurityIdentifier) -> None:
        """
        Initializes a new instance of the SecurityIdentifier class
        
        :param symbol: The base36 string encoded as a long using alpha <0-9A-Z>
        :param properties: Other data defining properties of the symbol including market,
        security type, listing or expiry date, strike/call/put/style for options, ect...
        :param underlying: Specifies a SecurityIdentifier that represents the underlying security
        """
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: QuantConnect.SecurityIdentifier) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: QuantConnect.SecurityIdentifier) -> bool:
        ...

    def __ne__(self, right: QuantConnect.SecurityIdentifier) -> bool:
        """Override not equals operator"""
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param obj: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This instance precedes obj in the sort order. Zero This instance occurs in the same position in the sort order as obj. Greater than zero This instance follows obj in the sort order.
        """
        ...

    @overload
    def compare_to(self, other: QuantConnect.SecurityIdentifier) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param other: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This instance precedes other in the sort order.  Zero This instance occurs in the same position in the sort order as other. Greater than zero This instance follows other in the sort order.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified System.Object is equal to the current System.Object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: QuantConnect.SecurityIdentifier) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the other parameter; otherwise, false.
        """
        ...

    @staticmethod
    def generate_base(data_type: typing.Type, symbol: str, market: str, map_symbol: bool = False, date: typing.Optional[datetime.datetime] = None) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a custom security with the option of providing the first date
        
        :param data_type: The custom data type
        :param symbol: The ticker symbol of this security
        :param market: The security's market
        :param map_symbol: Whether or not we should map this symbol
        :param date: First date that the security traded on
        :returns: A new SecurityIdentifier representing the specified base security.
        """
        ...

    @staticmethod
    def generate_base_symbol(data_type: typing.Type, symbol: str) -> str:
        """
        Generates the symbol property for QuantConnect.SecurityType.Base security identifiers
        
        :param data_type: The base data custom data type if namespacing is required, null otherwise
        :param symbol: The ticker symbol
        :returns: The value used for the security identifier's symbol.
        """
        ...

    @staticmethod
    def generate_cfd(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a CFD security
        
        :param symbol: The CFD contract symbol
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified CFD security.
        """
        ...

    @staticmethod
    def generate_constituent_identifier(symbol: str, security_type: QuantConnect.SecurityType, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a ConstituentsUniverseData.
        Note that the symbol ticker is case sensitive here.
        
        :param symbol: The ticker to use for this constituent identifier
        :param security_type: The security type of this constituent universe
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified constituent universe.
        """
        ...

    @staticmethod
    def generate_crypto(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a Crypto pair
        
        :param symbol: The currency pair in the format similar to: 'EURUSD'
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified Crypto pair.
        """
        ...

    @staticmethod
    def generate_crypto_future(expiry: typing.Union[datetime.datetime, datetime.date], symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a CryptoFuture pair
        
        :param expiry: The date the future expires
        :param symbol: The currency pair in the format similar to: 'EURUSD'
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified CryptoFuture pair.
        """
        ...

    @staticmethod
    @overload
    def generate_equity(symbol: str, market: str, map_symbol: bool = True, map_file_provider: QuantConnect.Interfaces.IMapFileProvider = None, mapping_resolve_date: typing.Optional[datetime.datetime] = None) -> QuantConnect.SecurityIdentifier:
        """
        Helper overload that will search the mapfiles to resolve the first date. This implementation
        uses the configured IMapFileProvider via the Composer.INSTANCE
        
        :param symbol: The symbol as it is known today
        :param market: The market
        :param map_symbol: Specifies if symbol should be mapped using map file provider
        :param map_file_provider: Specifies the IMapFileProvider to use for resolving symbols, specify null to load from Composer
        :param mapping_resolve_date: The date to use to resolve the map file. Default value is DateTime.Today
        :returns: A new SecurityIdentifier representing the specified symbol today.
        """
        ...

    @staticmethod
    @overload
    def generate_equity(date: typing.Union[datetime.datetime, datetime.date], symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for an equity
        
        :param date: The first date this security traded (in LEAN this is the first date in the map_file
        :param symbol: The ticker symbol this security traded under on the date
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified equity security.
        """
        ...

    @staticmethod
    def generate_forex(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a forex pair
        
        :param symbol: The currency pair in the format similar to: 'EURUSD'
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified forex pair.
        """
        ...

    @staticmethod
    def generate_future(expiry: typing.Union[datetime.datetime, datetime.date], symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a future
        
        :param expiry: The date the future expires
        :param symbol: The security's symbol
        :param market: The market
        :returns: A new SecurityIdentifier representing the specified futures security.
        """
        ...

    @staticmethod
    def generate_index(symbol: str, market: str) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for a INDEX security
        
        :param symbol: The Index contract symbol
        :param market: The security's market
        :returns: A new SecurityIdentifier representing the specified INDEX security.
        """
        ...

    @staticmethod
    @overload
    def generate_option(expiry: typing.Union[datetime.datetime, datetime.date], underlying: QuantConnect.SecurityIdentifier, market: str, strike: float, option_right: QuantConnect.OptionRight, option_style: QuantConnect.OptionStyle) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for an option
        
        :param expiry: The date the option expires
        :param underlying: The underlying security's symbol
        :param market: The market
        :param strike: The strike price
        :param option_right: The option type, call or put
        :param option_style: The option style, American or European
        :returns: A new SecurityIdentifier representing the specified option security.
        """
        ...

    @staticmethod
    @overload
    def generate_option(expiry: typing.Union[datetime.datetime, datetime.date], underlying: QuantConnect.SecurityIdentifier, target_option: str, market: str, strike: float, option_right: QuantConnect.OptionRight, option_style: QuantConnect.OptionStyle) -> QuantConnect.SecurityIdentifier:
        """
        Generates a new SecurityIdentifier for an option
        
        :param expiry: The date the option expires
        :param underlying: The underlying security's symbol
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param market: The market
        :param strike: The strike price
        :param option_right: The option type, call or put
        :param option_style: The option style, American or European
        :returns: A new SecurityIdentifier representing the specified option security.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        :returns: A hash code for the current System.Object.
        """
        ...

    @staticmethod
    def parse(value: str) -> QuantConnect.SecurityIdentifier:
        """
        Parses the specified string into a SecurityIdentifier
        The string must be a 40 digit number. The first 20 digits must be parseable
        to a 64 bit unsigned integer and contain ancillary data about the security.
        The second 20 digits must also be parseable as a 64 bit unsigned integer and
        contain the symbol encoded from base36, this provides for 12 alpha numeric case
        insensitive characters.
        
        :param value: The string value to be parsed
        :returns: A new SecurityIdentifier instance if the value is able to be parsed.
        """
        ...

    @staticmethod
    def ticker(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], date: typing.Union[datetime.datetime, datetime.date]) -> str:
        """
        For the given symbol will resolve the ticker it used at the requested date
        
        :param symbol: The symbol to get the ticker for
        :param date: The date to map the symbol to
        :returns: The ticker for a date and symbol.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @staticmethod
    def try_get_custom_data_type(symbol: str, type: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """Tries to fetch the custom data type associated with a symbol"""
        ...

    @staticmethod
    def try_get_custom_data_type_instance(symbol: str, type: typing.Optional[typing.Type]) -> typing.Tuple[bool, typing.Type]:
        """Tries to fetch the custom data type associated with a symbol"""
        ...

    @staticmethod
    def try_parse(value: str, identifier: typing.Optional[QuantConnect.SecurityIdentifier]) -> typing.Tuple[bool, QuantConnect.SecurityIdentifier]:
        """
        Attempts to parse the specified value as a SecurityIdentifier.
        
        :param value: The string value to be parsed
        :param identifier: The result of parsing, when this function returns true, identifier
        was properly created and reflects the input string, when this function returns false identifier
        will equal default(SecurityIdentifier)
        :returns: True on success, otherwise false.
        """
        ...


class Symbol(System.Object, System.IEquatable[QuantConnect_Symbol], System.IComparable):
    """
    Represents a unique security identifier. This is made of two components,
    the unique SID and the Value. The value is the current ticker symbol while
    the SID is constant over the life of a security
    """

    EMPTY: QuantConnect.Symbol = ...
    """
    Represents an unassigned symbol. This is intended to be used as an
    uninitialized, default value
    """

    NONE: QuantConnect.Symbol = ...
    """Represents no symbol. This is intended to be used when no symbol is explicitly intended"""

    @property
    def canonical(self) -> QuantConnect.Symbol:
        """Get's the canonical representation of this symbol"""
        ...

    @property
    def value(self) -> str:
        """Gets the current symbol for this ticker"""
        ...

    @property
    def id(self) -> QuantConnect.SecurityIdentifier:
        """Gets the security identifier for this symbol"""
        ...

    @property
    def has_underlying(self) -> bool:
        """
        Gets whether or not this Symbol is a derivative,
        that is, it has a valid underlying property
        """
        ...

    @property
    def underlying(self) -> QuantConnect.Symbol:
        """Gets the security underlying symbol, if any"""
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the security type of the symbol"""
        ...

    @property
    def cusip(self) -> str:
        """The Committee on Uniform Securities Identification Procedures (CUSIP) number corresponding to this Symbol"""
        ...

    @property
    def composite_figi(self) -> str:
        """The composite Financial Instrument Global Identifier (FIGI) corresponding to this Symbol"""
        ...

    @property
    def sedol(self) -> str:
        """The Stock Exchange Daily Official List (SEDOL) security identifier corresponding to this Symbol"""
        ...

    @property
    def isin(self) -> str:
        """The International Securities Identification Number (ISIN) corresponding to this Symbol"""
        ...

    @property
    def cik(self) -> typing.Optional[int]:
        """The Central Index Key number (CIK) corresponding to this Symbol"""
        ...

    @overload
    def __eq__(self, right: typing.Any) -> bool:
        """
        Equals operator
        
        :param right: The right operand
        :returns: True if both symbols are equal, otherwise false.
        """
        ...

    @overload
    def __eq__(self, right: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Equals operator
        
        :param right: The right operand
        :returns: True if both symbols are equal, otherwise false.
        """
        ...

    @overload
    def __eq__(self, right: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Equals operator
        
        :param right: The right operand
        :returns: True if both symbols are equal, otherwise false.
        """
        ...

    def __ge__(self, other: typing.Any) -> bool:
        ...

    def __gt__(self, other: typing.Any) -> bool:
        ...

    def __init__(self, sid: QuantConnect.SecurityIdentifier, value: str) -> None:
        """
        Initializes a new instance of the Symbol class
        
        :param sid: The security identifier for this symbol
        :param value: The current ticker symbol value
        """
        ...

    def __le__(self, other: typing.Any) -> bool:
        ...

    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ne__(self, right: typing.Any) -> bool:
        """
        Not equals operator
        
        :param right: The right operand
        :returns: True if both symbols are not equal, otherwise false.
        """
        ...

    @overload
    def __ne__(self, right: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Not equals operator
        
        :param right: The right operand
        :returns: True if both symbols are not equal, otherwise false.
        """
        ...

    @overload
    def __ne__(self, right: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Not equals operator
        
        :param right: The right operand
        :returns: True if both symbols are not equal, otherwise false.
        """
        ...

    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param obj: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings: Value Meaning Less than zero This instance precedes obj in the sort order. Zero This instance occurs in the same position in the sort order as obj. Greater than zero This instance follows obj in the sort order.
        """
        ...

    def contains(self, value: str) -> bool:
        """Symbol.Contains is a pass-through for Symbol.Value.Contains"""
        warnings.warn("Symbol.Contains is a pass-through for Symbol.Value.Contains", DeprecationWarning)

    @staticmethod
    def create(ticker: str, security_type: QuantConnect.SecurityType, market: str, alias: str = None, base_data_type: typing.Type = None) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating a Symbol for most security types.
        This method currently does not support Commodities
        
        :param ticker: The string ticker symbol
        :param security_type: The security type of the ticker. If security_type == Option, then a canonical symbol is created
        :param market: The market the ticker resides in
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from different markets
        :param base_data_type: Optional for SecurityType.BASE and used for generating the base data SID
        :returns: A new Symbol object for the specified ticker.
        """
        ...

    @staticmethod
    @overload
    def create_base(base_type: typing.Any, underlying: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], market: str = None) -> QuantConnect.Symbol:
        """
        Creates a new Symbol for custom data. This method allows for the creation of a new Base Symbol
        using the first ticker and the first traded date from the provided underlying Symbol. This avoids
        the issue for mappable types, where the ticker is remapped supposing the provided ticker value is from today.
        See SecurityIdentifier's private method GetFirstTickerAndDate.
        The provided symbol is also set to Symbol.underlying so that it can be accessed using the custom data Symbol.
        This is useful for associating custom data Symbols to other asset classes so that it is possible to filter using custom data
        and place trades on the underlying asset based on the filtered custom data.
        
        :param base_type: Type of BaseData instance
        :param underlying: Underlying symbol to set for the Base Symbol
        :param market: Market
        :returns: New non-mapped Base Symbol that contains an Underlying Symbol.
        """
        ...

    @staticmethod
    @overload
    def create_base(base_type: typing.Type, underlying: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], market: str = None) -> QuantConnect.Symbol:
        """
        Creates a new Symbol for custom data. This method allows for the creation of a new Base Symbol
        using the first ticker and the first traded date from the provided underlying Symbol. This avoids
        the issue for mappable types, where the ticker is remapped supposing the provided ticker value is from today.
        See SecurityIdentifier's private method GetFirstTickerAndDate.
        The provided symbol is also set to Symbol.underlying so that it can be accessed using the custom data Symbol.
        This is useful for associating custom data Symbols to other asset classes so that it is possible to filter using custom data
        and place trades on the underlying asset based on the filtered custom data.
        
        :param base_type: Type of BaseData instance
        :param underlying: Underlying symbol to set for the Base Symbol
        :param market: Market
        :returns: New non-mapped Base Symbol that contains an Underlying Symbol.
        """
        ...

    @staticmethod
    @overload
    def create_canonical_option(underlying_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], market: str = None, alias: str = None) -> QuantConnect.Symbol:
        """
        Simple method to create the canonical option symbol for any given underlying symbol
        
        :param underlying_symbol: Underlying of this option
        :param market: Market for this option
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from different markets
        :returns: New Canonical Option.
        """
        ...

    @staticmethod
    @overload
    def create_canonical_option(underlying_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], target_option: str, market: str = None, alias: str = None) -> QuantConnect.Symbol:
        """
        Simple method to create the canonical option symbol for any given underlying symbol
        
        :param underlying_symbol: Underlying of this option
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param market: Market for this option
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from different markets
        :returns: New Canonical Option.
        """
        ...

    @staticmethod
    def create_future(ticker: str, market: str, expiry: typing.Union[datetime.datetime, datetime.date], alias: str = None) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating a future Symbol.
        
        :param ticker: The ticker
        :param market: The market the future resides in
        :param expiry: The future expiry date
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from different markets
        :returns: A new Symbol object for the specified future contract.
        """
        ...

    @staticmethod
    @overload
    def create_option(underlying: str, market: str, style: QuantConnect.OptionStyle, right: QuantConnect.OptionRight, strike: float, expiry: typing.Union[datetime.datetime, datetime.date], alias: str = None, map_symbol: bool = True) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating an option Symbol.
        
        :param underlying: The underlying ticker
        :param market: The market the underlying resides in
        :param style: The option style (American, European, ect..)
        :param right: The option right (Put/Call)
        :param strike: The option strike price
        :param expiry: The option expiry date
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from different markets
        :param map_symbol: Specifies if symbol should be mapped using map file provider
        :returns: A new Symbol object for the specified option contract.
        """
        ...

    @staticmethod
    @overload
    def create_option(underlying_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], market: str, style: QuantConnect.OptionStyle, right: QuantConnect.OptionRight, strike: float, expiry: typing.Union[datetime.datetime, datetime.date], alias: str = None) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating an option Symbol using SecurityIdentifier.
        
        :param underlying_symbol: The underlying security symbol
        :param market: The market the underlying resides in
        :param style: The option style (American, European, ect..)
        :param right: The option right (Put/Call)
        :param strike: The option strike price
        :param expiry: The option expiry date
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from diferent markets
        :returns: A new Symbol object for the specified option contract.
        """
        ...

    @staticmethod
    @overload
    def create_option(underlying_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], target_option: str, market: str, style: QuantConnect.OptionStyle, right: QuantConnect.OptionRight, strike: float, expiry: typing.Union[datetime.datetime, datetime.date], alias: str = None) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating an option Symbol using SecurityIdentifier.
        
        :param underlying_symbol: The underlying security symbol
        :param target_option: The target option ticker. This is useful when the option ticker does not match the underlying, e.g. SPX index and the SPXW weekly option. If null is provided will use underlying
        :param market: The market the underlying resides in
        :param style: The option style (American, European, ect..)
        :param right: The option right (Put/Call)
        :param strike: The option strike price
        :param expiry: The option expiry date
        :param alias: An alias to be used for the symbol cache. Required when
        adding the same security from diferent markets
        :returns: A new Symbol object for the specified option contract.
        """
        ...

    @staticmethod
    @overload
    def create_option(sid: QuantConnect.SecurityIdentifier, value: str, underlying: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security] = None) -> QuantConnect.Symbol:
        """
        Provides a convenience method for creating an option Symbol from its SecurityIdentifier and alias.
        
        :param sid: The option SID
        :param value: The alias
        :param underlying: Optional underlying symbol to use. If null, it will we created from the given option SID and value
        :returns: A new Symbol object for the specified option.
        """
        ...

    def ends_with(self, value: str) -> bool:
        """Symbol.EndsWith is a pass-through for Symbol.Value.EndsWith"""
        warnings.warn("Symbol.EndsWith is a pass-through for Symbol.Value.EndsWith", DeprecationWarning)

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified System.Object is equal to the current System.Object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the other parameter; otherwise, false.
        """
        ...

    @staticmethod
    def get_alias(security_identifier: QuantConnect.SecurityIdentifier, underlying: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security] = None) -> str:
        """Centralized helper method to resolve alias for a symbol"""
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        :returns: A hash code for the current System.Object.
        """
        ...

    @staticmethod
    @overload
    def get_option_type_from_underlying(underlying_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> QuantConnect.SecurityType:
        """
        Determines the SecurityType based on the underlying Symbol's SecurityType
        
        :param underlying_symbol: Underlying Symbol of an option
        :returns: SecurityType of the option.
        """
        ...

    @staticmethod
    @overload
    def get_option_type_from_underlying(security_type: QuantConnect.SecurityType) -> QuantConnect.SecurityType:
        """
        Determines the SecurityType based on the underlying Symbol's SecurityType  get_underlying_from_option_type(SecurityType)
        
        :param security_type: SecurityType of the underlying Symbol
        :returns: SecurityType of the option.
        """
        ...

    @staticmethod
    def get_underlying_from_option_type(security_type: QuantConnect.SecurityType) -> QuantConnect.SecurityType:
        """
        Determines the underlying SecurityType based on the option Symbol's SecurityType get_option_type_from_underlying(SecurityType)
        
        :param security_type: SecurityType of the option Symbol
        :returns: SecurityType of the underlying.
        """
        ...

    def has_canonical(self) -> bool:
        """Determines whether the symbol has a canonical representation"""
        ...

    def has_underlying_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Determines if the specified symbol is an underlying of this symbol instance
        
        :param symbol: The underlying to check for
        :returns: True if the specified symbol is an underlying of this symbol instance.
        """
        ...

    def is_canonical(self) -> bool:
        """
        Method returns true, if symbol is a derivative canonical symbol
        
        :returns: true, if symbol is a derivative canonical symbol.
        """
        ...

    def starts_with(self, value: str) -> bool:
        """Symbol.StartsWith is a pass-through for Symbol.Value.StartsWith"""
        warnings.warn("Symbol.StartsWith is a pass-through for Symbol.Value.StartsWith", DeprecationWarning)

    def to_lower(self) -> str:
        """Symbol.ToLower is a pass-through for Symbol.Value.ToLower"""
        warnings.warn("Symbol.ToLower is a pass-through for Symbol.Value.ToLower", DeprecationWarning)

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def to_upper(self) -> str:
        """Symbol.ToUpper is a pass-through for Symbol.Value.ToUpper"""
        warnings.warn("Symbol.ToUpper is a pass-through for Symbol.Value.ToUpper", DeprecationWarning)

    def update_mapped_symbol(self, mapped_symbol: str, contract_depth_offset: int = 0) -> QuantConnect.Symbol:
        """
        Creates new symbol with updated mapped symbol. Symbol Mapping: When symbols change over time (e.g. CHASE-> JPM) need to update the symbol requested.
        Method returns newly created symbol
        """
        ...


class AccountType(IntEnum):
    """Account type: margin or cash"""

    MARGIN = 0
    """Margin account type (0)"""

    CASH = 1
    """Cash account type (1)"""


class AlgorithmConfiguration(System.Object):
    """
    This class includes algorithm configuration settings and parameters.
    This is used to include configuration parameters in the result packet to be used for report generation.
    """

    @property
    def name(self) -> str:
        """The algorithm's name"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Collections.Generic.ISet[str]:
        """List of tags associated with the algorithm"""
        ...

    @tags.setter
    def tags(self, value: System.Collections.Generic.ISet[str]) -> None:
        ...

    @property
    def account_currency(self) -> str:
        """The algorithm's account currency"""
        ...

    @account_currency.setter
    def account_currency(self, value: str) -> None:
        ...

    @property
    def brokerage(self) -> QuantConnect.Brokerages.BrokerageName:
        """The algorithm's brokerage model"""
        ...

    @brokerage.setter
    def brokerage(self, value: QuantConnect.Brokerages.BrokerageName) -> None:
        ...

    @property
    def account_type(self) -> QuantConnect.AccountType:
        """The algorithm's account type"""
        ...

    @account_type.setter
    def account_type(self, value: QuantConnect.AccountType) -> None:
        ...

    @property
    def parameters(self) -> System.Collections.Generic.IReadOnlyDictionary[str, str]:
        """The parameters used by the algorithm"""
        ...

    @parameters.setter
    def parameters(self, value: System.Collections.Generic.IReadOnlyDictionary[str, str]) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """Backtest maximum end date"""
        ...

    @out_of_sample_max_end_date.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """The backtest out of sample day count"""
        ...

    @out_of_sample_days.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @property
    def start_date(self) -> datetime.datetime:
        """The backtest start date"""
        ...

    @start_date.setter
    def start_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """The backtest end date"""
        ...

    @end_date.setter
    def end_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def trading_days_per_year(self) -> int:
        """Number of trading days per year for Algorithm's portfolio statistics."""
        ...

    @trading_days_per_year.setter
    def trading_days_per_year(self, value: int) -> None:
        ...

    @overload
    def __init__(self, name: str, tags: System.Collections.Generic.ISet[str], account_currency: str, brokerage_name: QuantConnect.Brokerages.BrokerageName, account_type: QuantConnect.AccountType, parameters: System.Collections.Generic.IReadOnlyDictionary[str, str], start_date: typing.Union[datetime.datetime, datetime.date], end_date: typing.Union[datetime.datetime, datetime.date], out_of_sample_max_end_date: typing.Optional[datetime.datetime], out_of_sample_days: int = 0, trading_days_per_year: int = 0) -> None:
        """Initializes a new instance of the AlgorithmConfiguration class"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new empty instance of the AlgorithmConfiguration class"""
        ...

    @staticmethod
    def create(algorithm: QuantConnect.Interfaces.IAlgorithm, backtest_node_packet: QuantConnect.Packets.BacktestNodePacket) -> QuantConnect.AlgorithmConfiguration:
        """
        Provides a convenience method for creating a AlgorithmConfiguration for a given algorithm.
        
        :param algorithm: Algorithm for which the configuration object is being created
        :param backtest_node_packet: The associated backtest node packet if any
        :returns: A new AlgorithmConfiguration object for the specified algorithm.
        """
        ...


class DateFormat(System.Object):
    """Shortcut date format strings"""

    SIX_CHARACTER: str = "yyMMdd"

    EIGHT_CHARACTER: str = "yyyyMMdd"

    TWELVE_CHARACTER: str = "yyyyMMdd HH:mm"

    JSON_FORMAT: str

    DB: str = "yyyy-MM-dd HH:mm:ss"

    UI: str = "yyyy-MM-dd HH:mm:ss"

    ISO_SHORT: str = "yyyy-MM-ddTHH:mm:ssZ"

    US_SHORT: str = "M/d/yy h:mm tt"

    US_SHORT_DATE_ONLY: str = "M/d/yy"

    US: str = "M/d/yyyy h:mm:ss tt"

    US_DATE_ONLY: str = "M/d/yyyy"

    FOREX: str = "yyyyMMdd HH:mm:ss.ffff"

    FIX: str = "yyyyMMdd-HH:mm:ss"

    FIX_WITH_MILLISECOND: str = "yyyyMMdd-HH:mm:ss.fff"

    YEAR_MONTH: str = "yyyyMM"


class Holding(System.Object):
    """Singular holding of assets from backend live nodes:"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        ...

    @symbol.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def type(self) -> QuantConnect.SecurityType:
        ...

    @property
    def currency_symbol(self) -> str:
        ...

    @currency_symbol.setter
    def currency_symbol(self, value: str) -> None:
        ...

    @property
    def average_price(self) -> float:
        ...

    @average_price.setter
    def average_price(self, value: float) -> None:
        ...

    @property
    def quantity(self) -> float:
        ...

    @quantity.setter
    def quantity(self, value: float) -> None:
        ...

    @property
    def market_price(self) -> float:
        ...

    @market_price.setter
    def market_price(self, value: float) -> None:
        ...

    @property
    def conversion_rate(self) -> typing.Optional[float]:
        ...

    @conversion_rate.setter
    def conversion_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def market_value(self) -> float:
        ...

    @market_value.setter
    def market_value(self, value: float) -> None:
        ...

    @property
    def unrealized_pn_l(self) -> float:
        ...

    @unrealized_pn_l.setter
    def unrealized_pn_l(self, value: float) -> None:
        ...

    @property
    def unrealized_pn_l_percent(self) -> float:
        ...

    @unrealized_pn_l_percent.setter
    def unrealized_pn_l_percent(self, value: float) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, security: QuantConnect.Securities.Security) -> None:
        """
        Create a simple JSON holdings from a Security holding class.
        
        :param security: The security instance
        """
        ...

    def clone(self) -> QuantConnect.Holding:
        """
        Clones this instance
        
        :returns: A new Holding object with the same values as this one.
        """
        ...

    def to_string(self) -> str:
        """Writes out the properties of this instance to string"""
        ...


class BrokerageEnvironment(IntEnum):
    """Represents the types of environments supported by brokerages for trading"""

    LIVE = 0
    """Live trading (0)"""

    PAPER = 1
    """Paper trading (1)"""


class Language(IntEnum):
    """Multilanguage support enum: which language is this project for the interop bridge converter."""

    C_SHARP = 0
    """C# Language Project (0)"""

    F_SHARP = 1
    """FSharp Project (1)"""

    VISUAL_BASIC = 2
    """Visual Basic Project (2)"""

    JAVA = 3
    """Java Language Project (3)"""

    PYTHON = 4
    """Python Language Project (4)"""


class ServerType(IntEnum):
    """Live server types available through the web IDE. / QC deployment."""

    SERVER_512 = 0
    """Additional server (0)"""

    SERVER_1024 = 1
    """Upgraded server (1)"""

    SERVER_2048 = 2
    """Server with 2048 MB Ram (2)"""


class MarketDataType(IntEnum):
    """Market data style: is the market data a summary (OHLC style) bar, or is it a time-price value."""

    BASE = 0
    """Base market data type (0)"""

    TRADE_BAR = 1
    """TradeBar market data type (OHLC summary bar) (1)"""

    TICK = 2
    """Tick market data type (price-time pair) (2)"""

    AUXILIARY = 3
    """Data associated with an instrument (3)"""

    QUOTE_BAR = 4
    """QuoteBar market data type (4) <Bid(OHLC), Ask(OHLC) and Mid(OHLC) summary bar>"""

    OPTION_CHAIN = 5
    """Option chain data (5)"""

    FUTURES_CHAIN = 6
    """Futures chain data (6)"""


class DataFeedEndpoint(IntEnum):
    """Datafeed enum options for selecting the source of the datafeed."""

    BACKTESTING = 0
    """Backtesting Datafeed Endpoint (0)"""

    FILE_SYSTEM = 1
    """Loading files off the local system (1)"""

    LIVE_TRADING = 2
    """Getting datafeed from a QC-Live-Cloud (2)"""

    DATABASE = 3
    """Database (3)"""


class StoragePermissions(IntEnum):
    """Cloud storage permission options."""

    PUBLIC = 0
    """Public Storage Permissions (0)"""

    AUTHENTICATED = 1
    """Authenticated Read Storage Permissions (1)"""


class TickType(IntEnum):
    """Types of tick data"""

    TRADE = 0
    """Trade type tick object (0)"""

    QUOTE = 1
    """Quote type tick object (1)"""

    OPEN_INTEREST = 2
    """Open Interest type tick object (for options, futures) (2)"""


class DelistingType(IntEnum):
    """Specifies the type of QuantConnect.Data.Market.Delisting data"""

    WARNING = 0
    """Specifies a warning of an imminent delisting (0)"""

    DELISTED = 1
    """Specifies the symbol has been delisted (1)"""


class SplitType(IntEnum):
    """Specifies the type of QuantConnect.Data.Market.Split data"""

    WARNING = 0
    """Specifies a warning of an imminent split event (0)"""

    SPLIT_OCCURRED = 1
    """Specifies the symbol has been split (1)"""


class Resolution(IntEnum):
    """Resolution of data requested."""

    TICK = 0
    """Tick Resolution (0)"""

    SECOND = 1
    """Second Resolution (1)"""

    MINUTE = 2
    """Minute Resolution (2)"""

    HOUR = 3
    """Hour Resolution (3)"""

    DAILY = 4
    """Daily Resolution (4)"""


class PositionSide(IntEnum):
    """Specifies what side a position is on, long/short"""

    SHORT = -1
    """A short position, quantity less than zero (-1)"""

    NONE = 0
    """No position, quantity equals zero (0)"""

    LONG = 1
    """A long position, quantity greater than zero (1)"""


class SettlementType(IntEnum):
    """Specifies the type of settlement in derivative deals"""

    PHYSICAL_DELIVERY = 0
    """Physical delivery of the underlying security (0)"""

    CASH = 1
    """Cash is paid/received on settlement (1)"""


class AlgorithmStatus(IntEnum):
    """States of a live deployment."""

    DEPLOY_ERROR = 0
    """Error compiling algorithm at start (0)"""

    IN_QUEUE = 1
    """Waiting for a server (1)"""

    RUNNING = 2
    """Running algorithm (2)"""

    STOPPED = 3
    """Stopped algorithm or exited with runtime errors (3)"""

    LIQUIDATED = 4
    """Liquidated algorithm (4)"""

    DELETED = 5
    """Algorithm has been deleted (5)"""

    COMPLETED = 6
    """Algorithm completed running (6)"""

    RUNTIME_ERROR = 7
    """Runtime Error Stoped Algorithm (7)"""

    INVALID = 8
    """Error in the algorithm id (not used) (8)"""

    LOGGING_IN = 9
    """The algorithm is logging into the brokerage (9)"""

    INITIALIZING = 10
    """The algorithm is initializing (10)"""

    HISTORY = 11
    """History status update (11)"""


class AlgorithmControl(System.Object):
    """Wrapper for algorithm status enum to include the charting subscription."""

    @property
    def initialized(self) -> bool:
        """Register this control packet as not defaults."""
        ...

    @initialized.setter
    def initialized(self, value: bool) -> None:
        ...

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Current run status of the algorithm id."""
        ...

    @status.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def chart_subscription(self) -> str:
        """Currently requested chart."""
        ...

    @chart_subscription.setter
    def chart_subscription(self, value: str) -> None:
        ...

    @property
    def has_subscribers(self) -> bool:
        """True if there's subscribers on the channel"""
        ...

    @has_subscribers.setter
    def has_subscribers(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Default initializer for algorithm control class."""
        ...


class SubscriptionTransportMedium(IntEnum):
    """Specifies where a subscription's data comes from"""

    LOCAL_FILE = 0
    """The subscription's data comes from disk (0)"""

    REMOTE_FILE = 1
    """The subscription's data is downloaded from a remote source (1)"""

    REST = 2
    """The subscription's data comes from a rest call that is polled and returns a single line/data point of information (2)"""

    STREAMING = 3
    """The subscription's data is streamed (3)"""

    OBJECT_STORE = 4
    """The subscription's data comes from the object store (4)"""


class WritePolicy(IntEnum):
    """Used by the Data.LeanDataWriter to determine which merge write policy should be applied"""

    OVERWRITE = 0
    """Will overwrite any existing file or zip entry with the new content (0)"""

    MERGE = 1
    """Will inject and merge new content with the existings file content (1)"""

    APPEND = 2
    """Will append new data to the end of the file or zip entry (2)"""


class Period(IntEnum):
    """enum Period - Enum of all the analysis periods, AS integers. Reference "Period" Array to access the values"""

    TEN_SECONDS = 10
    """Period Short Codes - 10"""

    THIRTY_SECONDS = 30
    """Period Short Codes - 30 Second"""

    ONE_MINUTE = 60
    """Period Short Codes - 60 Second"""

    TWO_MINUTES = 120
    """Period Short Codes - 120 Second"""

    THREE_MINUTES = 180
    """Period Short Codes - 180 Second"""

    FIVE_MINUTES = 300
    """Period Short Codes - 300 Second"""

    TEN_MINUTES = 600
    """Period Short Codes - 600 Second"""

    FIFTEEN_MINUTES = 900
    """Period Short Codes - 900 Second"""

    TWENTY_MINUTES = 1200
    """Period Short Codes - 1200 Second"""

    THIRTY_MINUTES = 1800
    """Period Short Codes - 1800 Second"""

    ONE_HOUR = 3600
    """Period Short Codes - 3600 Second"""

    TWO_HOURS = 7200
    """Period Short Codes - 7200 Second"""

    FOUR_HOURS = 14400
    """Period Short Codes - 14400 Second"""

    SIX_HOURS = 21600
    """Period Short Codes - 21600 Second"""


class DataNormalizationMode(IntEnum):
    """Specifies how data is normalized before being sent into an algorithm"""

    RAW = 0
    """No modifications to the asset price at all. For Equities, dividends are paid in cash and splits are applied directly to your portfolio quantity. (0)"""

    ADJUSTED = 1
    """Splits and dividends are backward-adjusted into the price of the asset. The price today is identical to the current market price. (1)"""

    SPLIT_ADJUSTED = 2
    """Equity splits are applied to the price adjustment but dividends are paid in cash to your portfolio. This normalization mode allows you to manage dividend payments (e.g. reinvestment) while still giving a smooth time series of prices for indicators. (2)"""

    TOTAL_RETURN = 3
    """Equity splits are applied to the price adjustment and the value of all future dividend payments is added to the initial asset price. (3)"""

    FORWARD_PANAMA_CANAL = 4
    """Eliminates price jumps between two consecutive contracts, adding a factor based on the difference of their prices. The first contract has the true price. Factor 0. (4)"""

    BACKWARDS_PANAMA_CANAL = 5
    """Eliminates price jumps between two consecutive contracts, adding a factor based on the difference of their prices. The last contract has the true price. Factor 0. (5)"""

    BACKWARDS_RATIO = 6
    """Eliminates price jumps between two consecutive contracts, multiplying the prices by their ratio. The last contract has the true price. Factor 1. (6)"""

    SCALED_RAW = 7
    """Splits and dividends are adjusted into the prices in a given date. Only for history requests. (7)"""


class DataMappingMode(IntEnum):
    """Continuous contracts mapping modes"""

    LAST_TRADING_DAY = 0
    """The contract maps on the previous day of expiration of the front month (0)"""

    FIRST_DAY_MONTH = 1
    """
    The contract maps on the first date of the delivery month of the front month. If the contract expires prior to this date,
    then it rolls on the contract's last trading date instead (1)
    """

    OPEN_INTEREST = 2
    """The contract maps when the following back month contract has a higher open interest that the current front month (2)"""

    OPEN_INTEREST_ANNUAL = 3
    """The contract maps when any of the back month contracts of the next year have a higher volume that the current front month (3)"""


class CashBookUpdateType(IntEnum):
    """The different types of CashBook.updated events"""

    ADDED = 0
    """A new Cash.symbol was added (0)"""

    REMOVED = 1
    """One or more Cash instances were removed (1)"""

    UPDATED = 2
    """An existing Cash.symbol was updated (2)"""


class Exchange(System.Object):
    """Lean exchange definition"""

    UNKNOWN: QuantConnect.Exchange
    """Unknown exchange value"""

    MEMX: QuantConnect.Exchange
    """The Members Exchange (MEMX) is an independently owned, technology-driven stock exchange"""

    LTSE: QuantConnect.Exchange
    """Long-Term Stock Exchange"""

    NASDAQ: QuantConnect.Exchange
    """National Association of Securities Dealers Automated Quotation."""

    NASDAQ_OPTIONS: QuantConnect.Exchange
    """The NASDAQ options market"""

    BATS: QuantConnect.Exchange
    """Bats Global Markets, Better Alternative Trading System"""

    ARCA: QuantConnect.Exchange
    """New York Stock Archipelago Exchange"""

    ARCA_OPTIONS: QuantConnect.Exchange
    """New York Stock Archipelago Exchange"""

    NYSE: QuantConnect.Exchange
    """New York Stock Exchange"""

    SMART: QuantConnect.Exchange
    """Smart Exchange"""

    OTCX: QuantConnect.Exchange
    """Over The Counter Exchange"""

    IEX: QuantConnect.Exchange
    """The Investors Exchange"""

    NSX: QuantConnect.Exchange
    """National Stock Exchange"""

    FINRA: QuantConnect.Exchange
    """The Financial Industry Regulatory Authority"""

    ISE: QuantConnect.Exchange
    """Nasdaq International Securities Exchange"""

    CSE: QuantConnect.Exchange
    """Chicago Stock Exchange"""

    CBOE: QuantConnect.Exchange
    """The Chicago Board Options Exchange"""

    C_2: QuantConnect.Exchange
    """CBOE Options Exchange"""

    NASDAQ_BX: QuantConnect.Exchange
    """The American Options Exchange"""

    SIAC: QuantConnect.Exchange
    """The Securities Industry Automation Corporation"""

    EDGA: QuantConnect.Exchange
    """CBOE EDGA U.S. equities Exchange"""

    EDGX: QuantConnect.Exchange
    """CBOE EDGX U.S. equities Exchange"""

    EDGO: QuantConnect.Exchange
    """CBOE EDGO U.S. option Exchange"""

    NASDAQ_PSX: QuantConnect.Exchange
    """National Association of Securities Dealers Automated Quotation PSX"""

    BATS_Y: QuantConnect.Exchange
    """National Association of Securities Dealers Automated Quotation PSX"""

    BOSTON: QuantConnect.Exchange
    """The Boston Stock Exchange"""

    BOX: QuantConnect.Exchange
    """The Boston Option Exchange"""

    AMEX: QuantConnect.Exchange
    """The American Stock Exchange"""

    BSE: QuantConnect.Exchange
    """Bombay Stock Exchange"""

    NSE: QuantConnect.Exchange
    """National Stock Exchange of India"""

    AMEX_OPTIONS: QuantConnect.Exchange
    """The American Options Exchange"""

    OPRA: QuantConnect.Exchange
    """The Options Price Reporting Authority"""

    MIAX: QuantConnect.Exchange
    """Miami International Securities Options Exchange"""

    MIAX_PEARL: QuantConnect.Exchange
    """MIAX Pearl Option and Equity exchange. Offers a Price-Time allocation and Maker-Taker fee structure"""

    MIAX_EMERALD: QuantConnect.Exchange
    """Serves as a counterpart to MIAX Options and MIAX Pearl by providing Pro-Rata allocation like MIAX Options and a Maker-Taker fee structure like MIAX Pearl"""

    MIAX_SAPPHIRE: QuantConnect.Exchange
    """MIAX Sapphire: Electronic and floor trading for derivatives."""

    ISE_GEMINI: QuantConnect.Exchange
    """International Securities Options Exchange GEMINI"""

    ISE_MERCURY: QuantConnect.Exchange
    """International Securities Options Exchange MERCURY"""

    CME: QuantConnect.Exchange
    """The Chicago Mercantile Exchange (CME), is an organized exchange for the trading of futures and options."""

    EUREX: QuantConnect.Exchange
    """The European Derivatives Exchange (EUREX)"""

    CBOT: QuantConnect.Exchange
    """The Chicago Board of Trade (CBOT) is a commodity exchange"""

    CFE: QuantConnect.Exchange
    """Cboe Futures Exchange"""

    COMEX: QuantConnect.Exchange
    """COMEX Commodity Exchange"""

    ICE: QuantConnect.Exchange
    """The Intercontinental Exchange"""

    NYMEX: QuantConnect.Exchange
    """New York Mercantile Exchange"""

    NYSELIFFE: QuantConnect.Exchange
    """London International Financial Futures and Options Exchange"""

    CSFB: QuantConnect.Exchange
    """Credit Suisse First Boston (also known as CSFB and CS First Boston) is the investment banking affiliate of Credit Suisse headquartered in New York."""

    PHLX: QuantConnect.Exchange
    """Philadelphia Stock Exchange (PHLX), now known as Nasdaq PHLX, is the first stock exchange established in the United States and the oldest stock exchange in the nation."""

    @property
    def description(self) -> str:
        """Exchange description"""
        ...

    @property
    def code(self) -> str:
        """The exchange short code"""
        ...

    @property
    def name(self) -> str:
        """The exchange name"""
        ...

    @property
    def market(self) -> str:
        """The associated lean market market"""
        ...

    @property
    def security_types(self) -> typing.Sequence[QuantConnect.SecurityType]:
        """Security types traded in this exchange"""
        ...

    def __eq__(self, right: QuantConnect.Exchange) -> bool:
        """
        Equals operator
        
        :param right: The right operand
        :returns: True if both symbols are equal, otherwise false.
        """
        ...

    def __init__(self, name: str, code: str, description: str, market: str, *security_types: typing.Union[QuantConnect.SecurityType, typing.Iterable[QuantConnect.SecurityType]]) -> None:
        """Creates a new exchange instance"""
        ...

    def __ne__(self, right: QuantConnect.Exchange) -> bool:
        """
        Not equals operator
        
        :param right: The right operand
        :returns: True if both symbols are not equal, otherwise false.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """Indicates whether the current object is equal to another object"""
        ...

    def get_hash_code(self) -> int:
        """Serves as a hash function for a particular type."""
        ...

    def to_string(self) -> str:
        """Returns a string that represents the current object."""
        ...


class Exchanges(System.Object):
    """Defines Lean exchanges codes and names"""

    @staticmethod
    def get_primary_exchange(exchange: str, security_type: QuantConnect.SecurityType = ..., market: str = ...) -> QuantConnect.Exchange:
        """Gets the exchange as PrimaryExchange object."""
        ...

    @staticmethod
    def get_primary_exchange_code_get_primary_exchange(exchange: str, security_type: QuantConnect.SecurityType = ..., market: str = ...) -> str:
        """Gets the exchange as single character representation."""
        ...


class ChannelStatus(System.Object):
    """Defines the different channel status values"""

    VACATED: str = "channel_vacated"
    """The channel is empty"""

    OCCUPIED: str = "channel_occupied"
    """The channel has subscribers"""


class DeploymentTarget(IntEnum):
    """Represents the types deployment targets for algorithms"""

    CLOUD_PLATFORM = 0
    """Cloud Platform (0)"""

    LOCAL_PLATFORM = 1
    """Local Platform (1)"""

    PRIVATE_CLOUD_PLATFORM = 2
    """Private Cloud Platform (2)"""


class AlgorithmMode(IntEnum):
    """Represents the deployment modes of an algorithm"""

    LIVE = 0
    """Live (0)"""

    OPTIMIZATION = 1
    """Optimization (1)"""

    BACKTESTING = 2
    """Backtesting (2)"""

    RESEARCH = 3
    """Research (3)"""


class RealTimeSynchronizedTimer(System.Object):
    """Real time timer class for precise callbacks on a millisecond resolution in a self managed thread."""

    @overload
    def __init__(self) -> None:
        """Constructor for Real Time Event Driver:"""
        ...

    @overload
    def __init__(self, period: datetime.timedelta, callback: typing.Callable[[datetime.datetime], typing.Any]) -> None:
        """
        Trigger an event callback after precisely milliseconds-lapsed.
        This is expensive, it creates a new thread and closely monitors the loop.
        
        :param period: delay period between event callbacks
        :param callback: Callback event passed the UTC time the event is intended to be triggered
        """
        ...

    def pause(self) -> None:
        """Hang the real time event:"""
        ...

    def resume(self) -> None:
        """Resume clock"""
        ...

    def scanner(self) -> None:
        """Scan the stopwatch for the desired millisecond delay:"""
        ...

    def start(self) -> None:
        """Start the synchronized real time timer - fire events at start of each second or minute"""
        ...

    def stop(self) -> None:
        """Stop the real time timer:"""
        ...


class SymbolValueJsonConverter:
    """
    Defines a JsonConverter to be used when you only want to serialize
    the Symbol.value property instead of the full Symbol
    instance
    """

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class DataProviderEventArgs(System.EventArgs, metaclass=abc.ABCMeta):
    """Defines a base class for IDataProviderEvents"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol being processed that generated the event"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        """
        Initializes a new instance of the DataProviderEventArgs class
        
        
        This codeEntityType is protected.
        
        :param symbol: Symbol being processed that generated the event
        """
        ...


class InvalidConfigurationDetectedEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the IDataProviderEvents.invalid_configuration_detected event"""

    @property
    def message(self) -> str:
        """Gets the error message"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], message: str) -> None:
        """
        Initializes a new instance of the InvalidConfigurationDetectedEventArgs class
        
        :param symbol: Symbol being processed that generated the event
        :param message: The error message
        """
        ...


class NumericalPrecisionLimitedEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the IDataProviderEvents.numerical_precision_limited event"""

    @property
    def message(self) -> str:
        """Gets the error message"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], message: str) -> None:
        """
        Initializes a new instance of the NumericalPrecisionLimitedEventArgs class
        
        :param symbol: Symbol being processed that generated the event
        :param message: The error message
        """
        ...


class DownloadFailedEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the IDataProviderEvents.download_failed event"""

    @property
    def message(self) -> str:
        """Gets the error message"""
        ...

    @property
    def stack_trace(self) -> str:
        """Gets the error stack trace"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], message: str, stack_trace: str = ...) -> None:
        """
        Initializes a new instance of the DownloadFailedEventArgs class
        
        :param symbol: Symbol being processed that generated the event
        :param message: The error message
        :param stack_trace: The error stack trace
        """
        ...


class ReaderErrorDetectedEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the IDataProviderEvents.reader_error_detected event"""

    @property
    def message(self) -> str:
        """Gets the error message"""
        ...

    @property
    def stack_trace(self) -> str:
        """Gets the error stack trace"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], message: str, stack_trace: str = ...) -> None:
        """
        Initializes a new instance of the ReaderErrorDetectedEventArgs class
        
        :param symbol: Symbol being processed that generated the event
        :param message: The error message
        :param stack_trace: The error stack trace
        """
        ...


class StartDateLimitedEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the IDataProviderEvents.start_date_limited event"""

    @property
    def message(self) -> str:
        """Gets the error message"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], message: str) -> None:
        """
        Initializes a new instance of the StartDateLimitedEventArgs class
        
        :param symbol: Symbol being processed that generated the event
        :param message: The error message
        """
        ...


class NewTradableDateEventArgs(QuantConnect.DataProviderEventArgs):
    """Event arguments for the NewTradableDate event"""

    @property
    def date(self) -> datetime.datetime:
        """The new tradable date"""
        ...

    @property
    def last_base_data(self) -> QuantConnect.Data.BaseData:
        """
        The last BaseData of the Security
        for which we are enumerating
        """
        ...

    @property
    def last_raw_price(self) -> typing.Optional[float]:
        """The last raw security price we have"""
        ...

    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], last_base_data: QuantConnect.Data.BaseData, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], last_raw_price: typing.Optional[float]) -> None:
        """
        Initializes a new instance of the NewTradableDateEventArgs class
        
        :param date: The new tradable date
        :param last_base_data: The last BaseData of the
        Security for which we are enumerating
        :param symbol: The Symbol of the new tradable date
        :param last_raw_price: The last raw security price we have
        """
        ...


class ITimeProvider(metaclass=abc.ABCMeta):
    """
    Provides access to the current time in UTC. This doesn't necessarily
    need to be wall-clock time, but rather the current time in some system
    """

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class RealTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """
    Provides an implementation of ITimeProvider that
    uses DateTime.UtcNow to provide the current time
    """

    INSTANCE: QuantConnect.ITimeProvider = ...
    """Provides a static instance of the RealTimeProvider"""

    def get_utc_now(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class TimeUpdatedEventArgs(System.EventArgs):
    """Event arguments class for the LocalTimeKeeper.time_updated event"""

    @property
    def time(self) -> datetime.datetime:
        """Gets the new time"""
        ...

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone"""
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], time_zone: typing.Any) -> None:
        """
        Initializes a new instance of the TimeUpdatedEventArgs class
        
        :param time: The newly updated time
        :param time_zone: The time zone of the new time
        """
        ...


class LocalTimeKeeper(System.Object):
    """
    Represents the current local time. This object is created via the TimeKeeper to
    manage conversions to local time.
    """

    @property
    def time_updated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.TimeUpdatedEventArgs], typing.Any], typing.Any]:
        """Event fired each time UpdateTime is called"""
        ...

    @time_updated.setter
    def time_updated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.TimeUpdatedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone of this LocalTimeKeeper"""
        ...

    @property
    def local_time(self) -> datetime.datetime:
        """Gets the current time in terms of the time_zone"""
        ...


class AlgorithmSettings(System.Object, QuantConnect.Interfaces.IAlgorithmSettings):
    """This class includes user settings for the algorithm which can be changed in the IAlgorithm.initialize method"""

    @property
    def automatic_indicator_warm_up(self) -> bool:
        """Gets whether or not WarmUpIndicator is allowed to warm up indicators"""
        ...

    @automatic_indicator_warm_up.setter
    def automatic_indicator_warm_up(self, value: bool) -> None:
        ...

    @property
    def rebalance_portfolio_on_security_changes(self) -> typing.Optional[bool]:
        """True if should rebalance portfolio on security changes. True by default"""
        ...

    @rebalance_portfolio_on_security_changes.setter
    def rebalance_portfolio_on_security_changes(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def rebalance_portfolio_on_insight_changes(self) -> typing.Optional[bool]:
        """True if should rebalance portfolio on new insights or expiration of insights. True by default"""
        ...

    @rebalance_portfolio_on_insight_changes.setter
    def rebalance_portfolio_on_insight_changes(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def max_absolute_portfolio_target_percentage(self) -> float:
        """The absolute maximum valid total portfolio value target percentage"""
        ...

    @max_absolute_portfolio_target_percentage.setter
    def max_absolute_portfolio_target_percentage(self, value: float) -> None:
        ...

    @property
    def min_absolute_portfolio_target_percentage(self) -> float:
        """The absolute minimum valid total portfolio value target percentage"""
        ...

    @min_absolute_portfolio_target_percentage.setter
    def min_absolute_portfolio_target_percentage(self, value: float) -> None:
        ...

    @property
    def minimum_order_margin_portfolio_percentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    @minimum_order_margin_portfolio_percentage.setter
    def minimum_order_margin_portfolio_percentage(self, value: float) -> None:
        ...

    @property
    def data_subscription_limit(self) -> int:
        """
        Gets/sets the maximum number of concurrent market data subscriptions available
        
        
        This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.
        """
        warnings.warn("This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.", DeprecationWarning)

    @data_subscription_limit.setter
    def data_subscription_limit(self, value: int) -> None:
        warnings.warn("This property is deprecated. Please observe data subscription limits set by your brokerage to avoid runtime errors.", DeprecationWarning)

    @property
    def free_portfolio_value(self) -> typing.Optional[float]:
        """
        Gets/sets the SetHoldings buffers value.
        The buffer is used for orders not to be rejected due to volatility when using SetHoldings and CalculateOrderQuantity
        """
        ...

    @free_portfolio_value.setter
    def free_portfolio_value(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def free_portfolio_value_percentage(self) -> float:
        """
        Gets/sets the SetHoldings buffers value percentage.
        This percentage will be used to set the free_portfolio_value
        based on the SecurityPortfolioManager.total_portfolio_value
        """
        ...

    @free_portfolio_value_percentage.setter
    def free_portfolio_value_percentage(self, value: float) -> None:
        ...

    @property
    def liquidate_enabled(self) -> bool:
        """Gets/sets if Liquidate() is enabled"""
        ...

    @liquidate_enabled.setter
    def liquidate_enabled(self, value: bool) -> None:
        ...

    @property
    def stale_price_time_span(self) -> datetime.timedelta:
        """Gets/sets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)"""
        ...

    @stale_price_time_span.setter
    def stale_price_time_span(self, value: datetime.timedelta) -> None:
        ...

    @property
    def warmup_resolution(self) -> typing.Optional[QuantConnect.Resolution]:
        """The warmup resolution to use if any"""
        ...

    @warmup_resolution.setter
    def warmup_resolution(self, value: typing.Optional[QuantConnect.Resolution]) -> None:
        ...

    @property
    def warm_up_resolution(self) -> typing.Optional[QuantConnect.Resolution]:
        """The warmup resolution to use if any"""
        ...

    @warm_up_resolution.setter
    def warm_up_resolution(self, value: typing.Optional[QuantConnect.Resolution]) -> None:
        ...

    @property
    def trading_days_per_year(self) -> typing.Optional[int]:
        """Number of trading days per year for this Algorithm's portfolio statistics."""
        ...

    @trading_days_per_year.setter
    def trading_days_per_year(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def daily_precise_end_time(self) -> bool:
        """True if daily strict end times are enabled"""
        ...

    @daily_precise_end_time.setter
    def daily_precise_end_time(self, value: bool) -> None:
        ...

    @property
    def daily_consolidation_use_extended_market_hours(self) -> bool:
        """True if extended market hours should be used for daily consolidation, when extended market hours is enabled"""
        ...

    @daily_consolidation_use_extended_market_hours.setter
    def daily_consolidation_use_extended_market_hours(self, value: bool) -> None:
        ...

    @property
    def databases_refresh_period(self) -> datetime.timedelta:
        """Gets the time span used to refresh the market hours and symbol properties databases"""
        ...

    @databases_refresh_period.setter
    def databases_refresh_period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def ignore_unknown_asset_holdings(self) -> bool:
        """
        Determines whether to terminate the algorithm when an asset holding is not supported by Lean or the brokerage.
        Defaults to true, meaning that the algorithm will not be terminated if an asset holding is not supported.
        """
        ...

    @ignore_unknown_asset_holdings.setter
    def ignore_unknown_asset_holdings(self, value: bool) -> None:
        ...

    @property
    def performance_sample_period(self) -> datetime.timedelta:
        """Performance tracking sample period to use if any, useful to debug performance issues"""
        ...

    @performance_sample_period.setter
    def performance_sample_period(self, value: datetime.timedelta) -> None:
        ...

    @property
    def seed_initial_prices(self) -> bool:
        """Determines whether to seed initial prices for all selected and manually added securities."""
        ...

    @seed_initial_prices.setter
    def seed_initial_prices(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the AlgorithmSettings class"""
        ...


class FileExtension(System.Object):
    """Helper methods for file management"""

    RESERVED_WORDS_PREFIX: str = ...
    """Reserved words prefix from Configuration"""

    @staticmethod
    def from_normalized_path(path: str) -> str:
        """
        Takes a modified path (see to_normalized_path(string)) and (if applicable)
        returns the original path proposed by LEAN
        """
        ...

    @staticmethod
    def to_normalized_path(path: str) -> str:
        """
        Takes a given path and (if applicable) returns a modified path accepted by
        Windows OS
        """
        ...


class TradingDay(System.Object):
    """Class contains trading events associated with particular day in TradingCalendar"""

    @property
    def date(self) -> datetime.datetime:
        """The date that this instance is associated with"""
        ...

    @property
    def business_day(self) -> bool:
        """Property returns true, if the day is a business day"""
        ...

    @property
    def public_holiday(self) -> bool:
        """Property returns true, if the day is a public holiday"""
        ...

    @property
    def weekend(self) -> bool:
        """Property returns true, if the day is a weekend"""
        ...

    @property
    def option_expirations(self) -> typing.Iterable[QuantConnect.Symbol]:
        """Property returns the list of options (among currently traded) that expire on this day"""
        ...

    @property
    def future_expirations(self) -> typing.Iterable[QuantConnect.Symbol]:
        """Property returns the list of futures (among currently traded) that expire on this day"""
        ...

    @property
    def future_rolls(self) -> typing.Iterable[QuantConnect.Symbol]:
        """Property returns the list of futures (among currently traded) that roll forward on this day"""
        ...

    @property
    def symbol_delistings(self) -> typing.Iterable[QuantConnect.Symbol]:
        """Property returns the list of symbols (among currently traded) that are delisted on this day"""
        ...

    @property
    def equity_dividends(self) -> typing.Iterable[QuantConnect.Symbol]:
        """Property returns the list of symbols (among currently traded) that have ex-dividend date on this day"""
        ...


class TradingDayType(IntEnum):
    """Enum lists available trading events"""

    BUSINESS_DAY = 0
    """Business day (0)"""

    PUBLIC_HOLIDAY = 1
    """Public Holiday (1)"""

    WEEKEND = 2
    """Weekend (2)"""

    OPTION_EXPIRATION = 3
    """Option Expiration Date (3)"""

    FUTURE_EXPIRATION = 4
    """Futures Expiration Date (4)"""

    FUTURE_ROLL = 5
    """Futures Roll Date (5)"""

    SYMBOL_DELISTING = 6
    """Symbol Delisting Date (6)"""

    EQUITY_DIVIDENDS = 7
    """Equity Ex-dividend Date (7)"""

    ECONOMIC_EVENT = 8
    """FX Economic Event (8)"""


class TradingCalendar(System.Object):
    """Class represents trading calendar, populated with variety of events relevant to currently trading instruments"""

    def __init__(self, security_manager: QuantConnect.Securities.SecurityManager, market_hours_database: QuantConnect.Securities.MarketHoursDatabase) -> None:
        """
        Initialize a new TradingCalendar instance.
        
        :param security_manager: SecurityManager for this calendar
        :param market_hours_database: MarketHoursDatabase for this calendar
        """
        ...

    def get_days_by_type(self, type: QuantConnect.TradingDayType, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.TradingDay]:
        """
        Method returns TradingDay of the specified type (TradingDayType) that contains trading events associated with the range of dates
        
        :param type: Type of the events
        :param start: Start date of the range (inclusive)
        :param end: End date of the range (inclusive)
        :returns: >Populated list of TradingDay.
        """
        ...

    @overload
    def get_trading_day(self) -> QuantConnect.TradingDay:
        """
        Method returns TradingDay that contains trading events associated with today's date
        
        :returns: Populated instance of TradingDay.
        """
        ...

    @overload
    def get_trading_day(self, day: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.TradingDay:
        """
        Method returns TradingDay that contains trading events associated with the given date
        
        :returns: Populated instance of TradingDay.
        """
        ...

    def get_trading_days(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[QuantConnect.TradingDay]:
        """
        Method returns TradingDay that contains trading events associated with the range of dates
        
        :param start: Start date of the range (inclusive)
        :param end: End date of the range (inclusive)
        :returns: >Populated list of TradingDay.
        """
        ...


class SymbolJsonConverter:
    """
    Defines a JsonConverter to be used when deserializing to
    the Symbol class.
    """

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class BinaryComparisonExtensions(System.Object):
    """Provides convenience extension methods for applying a BinaryComparison to collections."""


class DocumentationAttribute(System.Attribute):
    """Custom attribute used for documentation"""

    @property
    def tag(self) -> str:
        """The documentation tag"""
        ...

    @property
    def weight(self) -> int:
        """The associated weight of this attribute and tag"""
        ...

    @property
    def line(self) -> int:
        """The associated line of this attribute"""
        ...

    @property
    def file_name(self) -> str:
        """The associated file name of this attribute"""
        ...

    @property
    def type_id(self) -> System.Object:
        """The attributes type id, we override it to ignore it when serializing"""
        ...

    def __init__(self, tag: str, weight: int = 0, line: int = 0, file_name: str = ...) -> None:
        """Creates a new instance"""
        ...


class SeriesType(IntEnum):
    """Available types of chart series"""

    LINE = 0
    """Line Plot for Value Types (0)"""

    SCATTER = 1
    """Scatter Plot for Chart Distinct Types (1)"""

    CANDLE = 2
    """Charts (2)"""

    BAR = 3
    """Bar chart (3)"""

    FLAG = 4
    """Flag indicators (4)"""

    STACKED_AREA = 5
    """100% area chart showing relative proportions of series values at each time index (5)"""

    PIE = 6
    """Pie chart (6)"""

    TREEMAP = 7
    """Treemap Plot (7)"""

    HEATMAP = 9
    """Heatmap Plot (9) -- NOTE: 8 is reserved"""

    SCATTER_3D = 9
    """Scatter 3D Plot (10)"""


class ISeriesPoint(metaclass=abc.ABCMeta):
    """Single chart series point/bar data."""

    @property
    @abc.abstractmethod
    def time(self) -> datetime.datetime:
        """Time of this chart series point"""
        ...

    @time.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    def clone(self) -> QuantConnect.ISeriesPoint:
        """
        Clone implementation for ISeriesPoint
        
        :returns: Clone of the series.
        """
        ...


class BaseSeries(System.Object, metaclass=abc.ABCMeta):
    """Chart Series Object - Series data and properties for a chart:"""

    @property
    def name(self) -> str:
        """Name of the series."""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def unit(self) -> str:
        """Axis for the chart series."""
        ...

    @unit.setter
    def unit(self, value: str) -> None:
        ...

    @property
    def index(self) -> int:
        """Index/position of the series on the chart."""
        ...

    @index.setter
    def index(self, value: int) -> None:
        ...

    @property
    def index_name(self) -> str:
        """Axis name for the chart series."""
        ...

    @index_name.setter
    def index_name(self, value: str) -> None:
        ...

    @property
    def z_index(self) -> typing.Optional[int]:
        """Defines the visual Z index of the series on the chart."""
        ...

    @z_index.setter
    def z_index(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def series_type(self) -> QuantConnect.SeriesType:
        """Chart type for the series:"""
        ...

    @series_type.setter
    def series_type(self, value: QuantConnect.SeriesType) -> None:
        ...

    @property
    def tooltip(self) -> str:
        """An optional tooltip template"""
        ...

    @tooltip.setter
    def tooltip(self, value: str) -> None:
        ...

    @property
    def values(self) -> typing.List[QuantConnect.ISeriesPoint]:
        """
        The series list of values.
        These values are assumed to be in ascending time order (first points earliest, last points latest)
        """
        ...

    @values.setter
    def values(self, value: typing.List[QuantConnect.ISeriesPoint]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Default constructor for chart series
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType) -> None:
        """
        Constructor method for Chart Series
        
        
        This codeEntityType is protected.
        
        :param name: Name of the chart series
        :param type: Type of the series
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, index: int) -> None:
        """
        Foundational constructor on the series class
        
        
        This codeEntityType is protected.
        
        :param name: Name of the series
        :param type: Type of the series
        :param index: Series index position on the chart
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, index: int, unit: str) -> None:
        """
        Foundational constructor on the series class
        
        
        This codeEntityType is protected.
        
        :param name: Name of the series
        :param type: Type of the series
        :param index: Series index position on the chart
        :param unit: Unit for the series axis
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, unit: str) -> None:
        """
        Constructor method for Chart Series
        
        
        This codeEntityType is protected.
        
        :param name: Name of the chart series
        :param type: Type of the chart series
        :param unit: Unit of the series
        """
        ...

    @overload
    def add_point(self, point: QuantConnect.ISeriesPoint) -> None:
        """
        Add a new point to this series
        
        :param point: The data point to add
        """
        ...

    @overload
    def add_point(self, time: typing.Union[datetime.datetime, datetime.date], values: typing.List[float]) -> None:
        """
        Add a new point to this series
        
        :param time: The time of the data point
        :param values: The values of the data point
        """
        ...

    def clone(self, empty: bool = False) -> QuantConnect.BaseSeries:
        """Return a new instance clone of this object"""
        ...

    def clone_values(self) -> typing.List[QuantConnect.ISeriesPoint]:
        """
        Return a list of cloned values
        
        
        This codeEntityType is protected.
        """
        ...

    def consolidate_chart_points(self) -> QuantConnect.ISeriesPoint:
        """
        Will sum up all chart points into a new single value, using the time of latest point
        
        :returns: The new chart point.
        """
        ...

    @staticmethod
    def create(series_type: QuantConnect.SeriesType, name: str, index: int = 0, unit: str = "$") -> QuantConnect.BaseSeries:
        """
        Creates a series according to the specified type.
        
        :param series_type: The series type
        :param name: The name of the series
        :param index: Series index position on the chart
        :param unit: Unit for the series axis
        :returns: A CandlestickSeries if series_type is SeriesType.CANDLE.
        A Series otherwise.
        """
        ...

    def get_updates(self) -> QuantConnect.BaseSeries:
        """
        Get the updates since the last call to this function.
        
        :returns: List of the updates from the series.
        """
        ...

    def purge(self) -> None:
        """Removes the data from this series and resets the update position to 0"""
        ...


class ScatterMarkerSymbol(IntEnum):
    """Shape or symbol for the marker in a scatter plot"""

    NONE = 0
    """Circle symbol (0)"""

    CIRCLE = 1
    """Circle symbol (1)"""

    SQUARE = 2
    """Square symbol (2)"""

    DIAMOND = 3
    """Diamond symbol (3)"""

    TRIANGLE = 4
    """Triangle symbol (4)"""

    TRIANGLE_DOWN = 5
    """Triangle-down symbol (5)"""


class Series(QuantConnect.BaseSeries):
    """Chart Series Object - Series data and properties for a chart:"""

    @property
    def color(self) -> System.Drawing.Color:
        """Color the series"""
        ...

    @color.setter
    def color(self, value: System.Drawing.Color) -> None:
        ...

    @property
    def scatter_marker_symbol(self) -> QuantConnect.ScatterMarkerSymbol:
        """Shape or symbol for the marker in a scatter plot"""
        ...

    @scatter_marker_symbol.setter
    def scatter_marker_symbol(self, value: QuantConnect.ScatterMarkerSymbol) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for chart series"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, index: int) -> None:
        """
        Foundational constructor on the series class
        
        :param name: Name of the series
        :param type: Type of the series
        :param index: Index position on the chart of the series
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, index: int, unit: str) -> None:
        """
        Foundational constructor on the series class
        
        :param name: Name of the series
        :param type: Type of the series
        :param index: Index position on the chart of the series
        :param unit: Unit for the series axis
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType = ..., unit: str = "$") -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        :param type: Type of the chart series
        :param unit: Unit of the series
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, unit: str, color: System.Drawing.Color) -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        :param type: Type of the chart series
        :param unit: Unit of the series
        :param color: Color of the series
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.SeriesType, unit: str, color: System.Drawing.Color, symbol: QuantConnect.ScatterMarkerSymbol = ...) -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        :param type: Type of the chart series
        :param unit: Unit of the series
        :param color: Color of the series
        :param symbol: Symbol for the marker in a scatter plot series
        """
        ...

    @overload
    def add_point(self, time: typing.Union[datetime.datetime, datetime.date], value: float) -> None:
        """
        Add a new point to this series
        
        :param time: Time of the chart point
        :param value: Value of the chart point
        """
        ...

    @overload
    def add_point(self, point: QuantConnect.ISeriesPoint) -> None:
        """
        Add a new point to this series
        
        :param point: The data point to add
        """
        ...

    @overload
    def add_point(self, time: typing.Union[datetime.datetime, datetime.date], values: typing.List[float]) -> None:
        """
        Add a new point to this series
        
        :param time: The time of the data point
        :param values: The values of the data point
        """
        ...

    def clone(self, empty: bool = False) -> QuantConnect.BaseSeries:
        """Return a new instance clone of this object"""
        ...

    def consolidate_chart_points(self) -> QuantConnect.ISeriesPoint:
        """
        Will sum up all chart points into a new single value, using the time of latest point
        
        :returns: The new chart point.
        """
        ...


class TimeKeeper(System.Object, QuantConnect.Interfaces.ITimeKeeper):
    """Provides a means of centralizing time for various time zones."""

    @property
    def utc_time(self) -> datetime.datetime:
        """Gets the current time in UTC"""
        ...

    @overload
    def __init__(self, utc_date_time: typing.Union[datetime.datetime, datetime.date], *time_zones: typing.Union[DateTimeZone, typing.Iterable[DateTimeZone]]) -> None:
        """
        Initializes a new instance of the TimeKeeper class at the specified
        UTC time and for the specified time zones. Each time zone specified will cause the
        creation of a LocalTimeKeeper to handle conversions for that time zone.
        
        :param utc_date_time: The initial time
        :param time_zones: The time zones used to instantiate LocalTimeKeeper instances.
        """
        ...

    @overload
    def __init__(self, utc_date_time: typing.Union[datetime.datetime, datetime.date], time_zones: typing.List[DateTimeZone]) -> None:
        """
        Initializes a new instance of the TimeKeeper class at the specified
        UTC time and for the specified time zones. Each time zone specified will cause the
        creation of a LocalTimeKeeper to handle conversions for that time zone.
        
        :param utc_date_time: The initial time
        :param time_zones: The time zones used to instantiate LocalTimeKeeper instances.
        """
        ...

    def add_time_zone(self, time_zone: typing.Any) -> None:
        """
        Adds the specified time zone to this time keeper
        
        :param time_zone: 
        """
        ...

    def get_local_time_keeper(self, time_zone: typing.Any) -> QuantConnect.LocalTimeKeeper:
        """
        Gets the LocalTimeKeeper instance for the specified time zone
        
        :param time_zone: The time zone whose LocalTimeKeeper we seek
        :returns: The LocalTimeKeeper instance for the specified time zone.
        """
        ...

    def get_time_in(self, time_zone: typing.Any) -> datetime.datetime:
        """
        Gets the local time in the specified time zone. If the specified DateTimeZone
        has not already been added, this will throw a KeyNotFoundException.
        
        :param time_zone: The time zone to get local time for
        :returns: The local time in the specifed time zone.
        """
        ...

    def set_utc_date_time(self, utc_date_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the current UTC time for this time keeper and the attached child LocalTimeKeeper instances.
        
        :param utc_date_time: The current time in UTC
        """
        ...


class Country(System.Object):
    """
    The Country class contains all countries normalized for your convenience.
    It maps the country name to its ISO 3166-1 alpha-3 code, see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
    """

    AFGHANISTAN: str = "AFG"
    """Afghanistan"""

    ALAND_ISLANDS: str = "ALA"
    """Aland Islands"""

    ALBANIA: str = "ALB"
    """Albania"""

    ALGERIA: str = "DZA"
    """Algeria"""

    AMERICAN_SAMOA: str = "ASM"
    """American Samoa"""

    ANDORRA: str = "AND"
    """Andorra"""

    ANGOLA: str = "AGO"
    """Angola"""

    ANGUILLA: str = "AIA"
    """Anguilla"""

    ANTARCTICA: str = "ATA"
    """Antarctica"""

    ANTIGUA_AND_BARBUDA: str = "ATG"
    """Antigua and Barbuda"""

    ARGENTINA: str = "ARG"
    """Argentina"""

    ARMENIA: str = "ARM"
    """Armenia"""

    ARUBA: str = "ABW"
    """Aruba"""

    AUSTRALIA: str = "AUS"
    """Australia"""

    AUSTRIA: str = "AUT"
    """Austria"""

    AZERBAIJAN: str = "AZE"
    """Azerbaijan"""

    BAHAMAS: str = "BHS"
    """Bahamas"""

    BAHRAIN: str = "BHR"
    """Bahrain"""

    BANGLADESH: str = "BGD"
    """Bangladesh"""

    BARBADOS: str = "BRB"
    """Barbados"""

    BELARUS: str = "BLR"
    """Belarus"""

    BELGIUM: str = "BEL"
    """Belgium"""

    BELIZE: str = "BLZ"
    """Belize"""

    BENIN: str = "BEN"
    """Benin"""

    BERMUDA: str = "BMU"
    """Bermuda"""

    BHUTAN: str = "BTN"
    """Bhutan"""

    BOLIVIA: str = "BOL"
    """Bolivia"""

    BONAIRE: str = "BES"
    """Bonaire"""

    BOSNIA_AND_HERZEGOVINA: str = "BIH"
    """Bosnia and Herzegovina"""

    BOTSWANA: str = "BWA"
    """Botswana"""

    BOUVET_ISLAND: str = "BVT"
    """Bouvet Island"""

    BRAZIL: str = "BRA"
    """Brazil"""

    BRITISH_INDIAN_OCEAN_TERRITORY: str = "IOT"
    """British Indian Ocean Territory"""

    BRUNEI_DARUSSALAM: str = "BRN"
    """Brunei Darussalam"""

    BULGARIA: str = "BGR"
    """Bulgaria"""

    BURKINA_FASO: str = "BFA"
    """Burkina Faso"""

    BURUNDI: str = "BDI"
    """Burundi"""

    CABO_VERDE: str = "CPV"
    """Cabo Verde"""

    CAMBODIA: str = "KHM"
    """Cambodia"""

    CAMEROON: str = "CMR"
    """Cameroon"""

    CANADA: str = "CAN"
    """Canada"""

    CAYMAN_ISLANDS: str = "CYM"
    """Cayman Islands"""

    CENTRAL_AFRICAN_REPUBLIC: str = "CAF"
    """Central African Republic"""

    CHAD: str = "TCD"
    """Chad"""

    CHILE: str = "CHL"
    """Chile"""

    CHINA: str = "CHN"
    """China"""

    CHRISTMAS_ISLAND: str = "CXR"
    """Christmas Island"""

    COCOS_KEELING_ISLANDS: str = "CCK"
    """Cocos Keeling Islands"""

    COLOMBIA: str = "COL"
    """Colombia"""

    COMOROS: str = "COM"
    """Comoros"""

    DEMOCRATIC_REPUBLIC_OF_CONGO: str = "COD"
    """Democratic Republic of Congo"""

    CONGO: str = "COG"
    """Congo"""

    COOK_ISLANDS: str = "COK"
    """Cook Islands"""

    COSTA_RICA: str = "CRI"
    """Costa Rica"""

    IVORY_COAST: str = "CIV"
    """Ivory Coast"""

    CROATIA: str = "HRV"
    """Croatia"""

    CUBA: str = "CUB"
    """Cuba"""

    CURAÇAO: str = "CUW"
    """Curaçao"""

    CYPRUS: str = "CYP"
    """Cyprus"""

    CZECHIA: str = "CZE"
    """Czechia"""

    DENMARK: str = "DNK"
    """Denmark"""

    DJIBOUTI: str = "DJI"
    """Djibouti"""

    DOMINICA: str = "DMA"
    """Dominica"""

    DOMINICAN_REPUBLIC: str = "DOM"
    """Dominican Republic"""

    ECUADOR: str = "ECU"
    """Ecuador"""

    EGYPT: str = "EGY"
    """Egypt"""

    EL_SALVADOR: str = "SLV"
    """El Salvador"""

    EQUATORIAL_GUINEA: str = "GNQ"
    """Equatorial Guinea"""

    ERITREA: str = "ERI"
    """Eritrea"""

    ESTONIA: str = "EST"
    """Estonia"""

    ESWATINI: str = "SWZ"
    """Eswatini"""

    ETHIOPIA: str = "ETH"
    """Ethiopia"""

    FALKLAND_ISLANDS: str = "FLK"
    """Falkland Islands"""

    FAROE_ISLANDS: str = "FRO"
    """Faroe Islands"""

    FIJI: str = "FJI"
    """Fiji"""

    FINLAND: str = "FIN"
    """Finland"""

    FRANCE: str = "FRA"
    """France"""

    FRENCH_GUIANA: str = "GUF"
    """French Guiana"""

    FRENCH_POLYNESIA: str = "PYF"
    """French Polynesia"""

    FRENCH_SOUTHERN_TERRITORIES: str = "ATF"
    """French Southern Territories"""

    GABON: str = "GAB"
    """Gabon"""

    GAMBIA: str = "GMB"
    """Gambia"""

    GEORGIA: str = "GEO"
    """Georgia"""

    GERMANY: str = "DEU"
    """Germany"""

    GHANA: str = "GHA"
    """Ghana"""

    GIBRALTAR: str = "GIB"
    """Gibraltar"""

    GREECE: str = "GRC"
    """Greece"""

    GREENLAND: str = "GRL"
    """Greenland"""

    GRENADA: str = "GRD"
    """Grenada"""

    GUADELOUPE: str = "GLP"
    """Guadeloupe"""

    GUAM: str = "GUM"
    """Guam"""

    GUATEMALA: str = "GTM"
    """Guatemala"""

    GUERNSEY: str = "GGY"
    """Guernsey"""

    GUINEA: str = "GIN"
    """Guinea"""

    GUINEA_BISSAU: str = "GNB"
    """Guinea-Bissau"""

    GUYANA: str = "GUY"
    """Guyana"""

    HAITI: str = "HTI"
    """Haiti"""

    HEARD_ISLAND_AND_MCDONALD_ISLANDS: str = "HMD"
    """Heard Island and McDonald Islands"""

    HOLY_SEE: str = "VAT"
    """Holy See"""

    HONDURAS: str = "HND"
    """Honduras"""

    HONG_KONG: str = "HKG"
    """Hong Kong"""

    HUNGARY: str = "HUN"
    """Hungary"""

    ICELAND: str = "ISL"
    """Iceland"""

    INDIA: str = "IND"
    """India"""

    INDONESIA: str = "IDN"
    """Indonesia"""

    IRAN: str = "IRN"
    """Iran"""

    IRAQ: str = "IRQ"
    """Iraq"""

    IRELAND: str = "IRL"
    """Ireland"""

    ISLE_OF_MAN: str = "IMN"
    """Isle of Man"""

    ISRAEL: str = "ISR"
    """Israel"""

    ITALY: str = "ITA"
    """Italy"""

    JAMAICA: str = "JAM"
    """Jamaica"""

    JAPAN: str = "JPN"
    """Japan"""

    JERSEY: str = "JEY"
    """Jersey"""

    JORDAN: str = "JOR"
    """Jordan"""

    KAZAKHSTAN: str = "KAZ"
    """Kazakhstan"""

    KENYA: str = "KEN"
    """Kenya"""

    KIRIBATI: str = "KIR"
    """Kiribati"""

    NORTH_KOREA: str = "PRK"
    """North Korea"""

    KOREA: str = "KOR"
    """Korea"""

    KUWAIT: str = "KWT"
    """Kuwait"""

    KYRGYZSTAN: str = "KGZ"
    """Kyrgyzstan"""

    LAOS: str = "LAO"
    """Laos"""

    LATVIA: str = "LVA"
    """Latvia"""

    LEBANON: str = "LBN"
    """Lebanon"""

    LESOTHO: str = "LSO"
    """Lesotho"""

    LIBERIA: str = "LBR"
    """Liberia"""

    LIBYA: str = "LBY"
    """Libya"""

    LIECHTENSTEIN: str = "LIE"
    """Liechtenstein"""

    LITHUANIA: str = "LTU"
    """Lithuania"""

    LUXEMBOURG: str = "LUX"
    """Luxembourg"""

    MACAO: str = "MAC"
    """Macao"""

    MADAGASCAR: str = "MDG"
    """Madagascar"""

    MALAWI: str = "MWI"
    """Malawi"""

    MALAYSIA: str = "MYS"
    """Malaysia"""

    MALDIVES: str = "MDV"
    """Maldives"""

    MALI: str = "MLI"
    """Mali"""

    MALTA: str = "MLT"
    """Malta"""

    MARSHALL_ISLANDS: str = "MHL"
    """Marshall Islands"""

    MARTINIQUE: str = "MTQ"
    """Martinique"""

    MAURITANIA: str = "MRT"
    """Mauritania"""

    MAURITIUS: str = "MUS"
    """Mauritius"""

    MAYOTTE: str = "MYT"
    """Mayotte"""

    MEXICO: str = "MEX"
    """Mexico"""

    MICRONESIA: str = "FSM"
    """Micronesia"""

    MOLDOVA: str = "MDA"
    """Moldova"""

    MONACO: str = "MCO"
    """Monaco"""

    MONGOLIA: str = "MNG"
    """Mongolia"""

    MONTENEGRO: str = "MNE"
    """Montenegro"""

    MONTSERRAT: str = "MSR"
    """Montserrat"""

    MOROCCO: str = "MAR"
    """Morocco"""

    MOZAMBIQUE: str = "MOZ"
    """Mozambique"""

    MYANMAR: str = "MMR"
    """Myanmar"""

    NAMIBIA: str = "NAM"
    """Namibia"""

    NAURU: str = "NRU"
    """Nauru"""

    NEPAL: str = "NPL"
    """Nepal"""

    NETHERLANDS: str = "NLD"
    """Netherlands"""

    NEW_CALEDONIA: str = "NCL"
    """New Caledonia"""

    NEW_ZEALAND: str = "NZL"
    """New Zealand"""

    NICARAGUA: str = "NIC"
    """Nicaragua"""

    NIGER: str = "NER"
    """Niger"""

    NIGERIA: str = "NGA"
    """Nigeria"""

    NIUE: str = "NIU"
    """Niue"""

    NORFOLK_ISLAND: str = "NFK"
    """Norfolk Island"""

    NORTH_MACEDONIA: str = "MKD"
    """North Macedonia"""

    NORTHERN_MARIANA_ISLANDS: str = "MNP"
    """Northern Mariana Islands"""

    NORWAY: str = "NOR"
    """Norway"""

    OMAN: str = "OMN"
    """Oman"""

    PAKISTAN: str = "PAK"
    """Pakistan"""

    PALAU: str = "PLW"
    """Palau"""

    PALESTINE: str = "PSE"
    """Palestine"""

    PANAMA: str = "PAN"
    """Panama"""

    PAPUA_NEW_GUINEA: str = "PNG"
    """Papua New Guinea"""

    PARAGUAY: str = "PRY"
    """Paraguay"""

    PERU: str = "PER"
    """Peru"""

    PHILIPPINES: str = "PHL"
    """Philippines"""

    PITCAIRN: str = "PCN"
    """Pitcairn"""

    POLAND: str = "POL"
    """Poland"""

    PORTUGAL: str = "PRT"
    """Portugal"""

    PUERTO_RICO: str = "PRI"
    """Puerto Rico"""

    QATAR: str = "QAT"
    """Qatar"""

    REUNION: str = "REU"
    """Reunion"""

    ROMANIA: str = "ROU"
    """Romania"""

    RUSSIA: str = "RUS"
    """Russia"""

    RWANDA: str = "RWA"
    """Rwanda"""

    SAINT_BARTHÉLEMY: str = "BLM"
    """Saint Barthélemy"""

    SAINT_HELENA: str = "SHN"
    """Saint Helena"""

    SAINT_KITTS_AND_NEVIS: str = "KNA"
    """Saint Kitts and Nevis"""

    SAINT_LUCIA: str = "LCA"
    """Saint Lucia"""

    SAINT_MARTIN_FRENCH_PART: str = "MAF"
    """Saint Martin French part"""

    SAINT_PIERRE_AND_MIQUELON: str = "SPM"
    """Saint Pierre and Miquelon"""

    SAINT_VINCENT_AND_THE_GRENADINES: str = "VCT"
    """Saint Vincent and the Grenadines"""

    SAMOA: str = "WSM"
    """Samoa"""

    SAN_MARINO: str = "SMR"
    """San Marino"""

    SAO_TOME_AND_PRINCIPE: str = "STP"
    """Sao Tome and Principe"""

    SAUDI_ARABIA: str = "SAU"
    """Saudi Arabia"""

    SENEGAL: str = "SEN"
    """Senegal"""

    SERBIA: str = "SRB"
    """Serbia"""

    SEYCHELLES: str = "SYC"
    """Seychelles"""

    SIERRA_LEONE: str = "SLE"
    """Sierra Leone"""

    SINGAPORE: str = "SGP"
    """Singapore"""

    SINT_MAARTEN_DUTCH_PART: str = "SXM"
    """Sint Maarten Dutch part"""

    SLOVAKIA: str = "SVK"
    """Slovakia"""

    SLOVENIA: str = "SVN"
    """Slovenia"""

    SOLOMON_ISLANDS: str = "SLB"
    """Solomon Islands"""

    SOMALIA: str = "SOM"
    """Somalia"""

    SOUTH_AFRICA: str = "ZAF"
    """South Africa"""

    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS: str = "SGS"
    """South Georgia and the South Sandwich Islands"""

    SOUTH_SUDAN: str = "SSD"
    """South Sudan"""

    SPAIN: str = "ESP"
    """Spain"""

    SRI_LANKA: str = "LKA"
    """Sri Lanka"""

    SUDAN: str = "SDN"
    """Sudan"""

    SURINAME: str = "SUR"
    """Suriname"""

    SVALBARD: str = "SJM"
    """Svalbard"""

    SWEDEN: str = "SWE"
    """Sweden"""

    SWITZERLAND: str = "CHE"
    """Switzerland"""

    SYRIA: str = "SYR"
    """Syria"""

    TAIWAN: str = "TWN"
    """Taiwan"""

    TAJIKISTAN: str = "TJK"
    """Tajikistan"""

    TANZANIA: str = "TZA"
    """Tanzania"""

    THAILAND: str = "THA"
    """Thailand"""

    TIMOR_LESTE: str = "TLS"
    """Timor-Leste"""

    TOGO: str = "TGO"
    """Togo"""

    TOKELAU: str = "TKL"
    """Tokelau"""

    TONGA: str = "TON"
    """Tonga"""

    TRINIDAD_AND_TOBAGO: str = "TTO"
    """Trinidad and Tobago"""

    TUNISIA: str = "TUN"
    """Tunisia"""

    TURKEY: str = "TUR"
    """Turkey"""

    TURKMENISTAN: str = "TKM"
    """Turkmenistan"""

    TURKS_AND_CAICOS_ISLANDS: str = "TCA"
    """Turks and Caicos Islands"""

    TUVALU: str = "TUV"
    """Tuvalu"""

    UGANDA: str = "UGA"
    """Uganda"""

    UKRAINE: str = "UKR"
    """Ukraine"""

    UNITED_ARAB_EMIRATES: str = "ARE"
    """United Arab Emirates"""

    UNITED_KINGDOM: str = "GBR"
    """United Kingdom"""

    UNITED_STATES_MINOR_OUTLYING_ISLANDS: str = "UMI"
    """United States Minor Outlying Islands"""

    UNITED_STATES: str = "USA"
    """United States"""

    EUROPEAN_UNION: str = "EUR"
    """European Union"""

    URUGUAY: str = "URY"
    """Uruguay"""

    UZBEKISTAN: str = "UZB"
    """Uzbekistan"""

    VANUATU: str = "VUT"
    """Vanuatu"""

    VENEZUELA: str = "VEN"
    """Venezuela"""

    VIETNAM: str = "VNM"
    """Vietnam"""

    VIRGIN_ISLANDS_BRITISH: str = "VGB"
    """Virgin Islands British"""

    VIRGIN_ISLANDS_US: str = "VIR"
    """Virgin Islands US"""

    WALLIS_AND_FUTUNA: str = "WLF"
    """Wallis and Futuna"""

    WESTERN_SAHARA: str = "ESH"
    """Western Sahara"""

    YEMEN: str = "YEM"
    """Yemen"""

    ZAMBIA: str = "ZMB"
    """Zambia"""

    ZIMBABWE: str = "ZWE"
    """Zimbabwe"""


class ChartPoint(System.Object, QuantConnect.ISeriesPoint):
    """Single Chart Point Value Type for QCAlgorithm.Plot();"""

    @property
    def time(self) -> datetime.datetime:
        """Time of this chart series point"""
        ...

    @time.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def x(self) -> int:
        """Chart point time"""
        ...

    @x.setter
    def x(self, value: int) -> None:
        ...

    @property
    def y(self) -> typing.Optional[float]:
        """Chart point value"""
        ...

    @y.setter
    def y(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def x(self) -> int:
        """Shortcut for x for C# naming conventions"""
        ...

    @property
    def y(self) -> typing.Optional[float]:
        """Shortcut for y for C# naming conventions"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor. Using in SeriesSampler."""
        ...

    @overload
    def __init__(self, x_value: int, y_value: typing.Optional[float]) -> None:
        """
        Constructor that takes both x, y value pairs
        
        :param x_value: X value often representing a time in seconds
        :param y_value: Y value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], value: typing.Optional[float]) -> None:
        """
        Constructor that takes both x, y value pairs
        
        :param time: This point time
        :param value: Y value
        """
        ...

    @overload
    def __init__(self, point: QuantConnect.ChartPoint) -> None:
        ...

    def clone(self) -> QuantConnect.ISeriesPoint:
        """
        Clones this instance
        
        :returns: Clone of this instance.
        """
        ...

    def to_string(self) -> str:
        """Provides a readable string representation of this instance."""
        ...


class ScatterChartPoint(QuantConnect.ChartPoint):
    """A chart point for a scatter series plot"""

    @property
    def tooltip(self) -> str:
        """A summary of this point for the tooltip"""
        ...

    @tooltip.setter
    def tooltip(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new empty instance"""
        ...

    @overload
    def __init__(self, time: int, value: typing.Optional[float], tooltip: str = None) -> None:
        """Creates a new instance at the specified time and value"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], value: typing.Optional[float], tooltip: str = None) -> None:
        """Creates a new instance at the specified time and value"""
        ...

    def clone(self) -> QuantConnect.ISeriesPoint:
        """
        Clones this instance
        
        :returns: Clone of this instance.
        """
        ...


class Expiry(System.Object):
    """Provides static functions that can be used to compute a future DateTime (expiry) given a DateTime."""

    ONE_MONTH: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes a date/time one month after a given date/time (nth day to nth day)"""

    ONE_QUARTER: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes a date/time one quarter after a given date/time (nth day to nth day)"""

    ONE_YEAR: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes a date/time one year after a given date/time (nth day to nth day)"""

    END_OF_DAY: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes the end of day (mid-night of the next day) of given date/time"""

    END_OF_WEEK: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes the end of week (next Monday) of given date/time"""

    END_OF_MONTH: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes the end of month (1st of the next month) of given date/time"""

    END_OF_QUARTER: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes the end of quarter (1st of the starting month of next quarter) of given date/time"""

    END_OF_YEAR: typing.Callable[[datetime.datetime], datetime.datetime]
    """Computes the end of year (1st of the next year) of given date/time"""


class SymbolRepresentation(System.Object):
    """Public static helper class that does parsing/generation of symbol representations (options, futures)"""

    class FutureTickerProperties(System.Object):
        """Class contains future ticker properties returned by ParseFutureTicker()"""

        @property
        def underlying(self) -> str:
            """Underlying name"""
            ...

        @underlying.setter
        def underlying(self, value: str) -> None:
            ...

        @property
        def expiration_year_short(self) -> int:
            """Short expiration year"""
            ...

        @expiration_year_short.setter
        def expiration_year_short(self, value: int) -> None:
            ...

        @property
        def expiration_year_short_length(self) -> int:
            """Short expiration year digits"""
            ...

        @expiration_year_short_length.setter
        def expiration_year_short_length(self, value: int) -> None:
            ...

        @property
        def expiration_month(self) -> int:
            """Expiration month"""
            ...

        @expiration_month.setter
        def expiration_month(self, value: int) -> None:
            ...

        @property
        def expiration_day(self) -> int:
            """Expiration day"""
            ...

        @expiration_day.setter
        def expiration_day(self, value: int) -> None:
            ...

    class OptionTickerProperties(System.Object):
        """Class contains option ticker properties returned by ParseOptionTickerIQFeed()"""

        @property
        def underlying(self) -> str:
            """Underlying name"""
            ...

        @underlying.setter
        def underlying(self, value: str) -> None:
            ...

        @property
        def option_right(self) -> QuantConnect.OptionRight:
            """Option right"""
            ...

        @option_right.setter
        def option_right(self, value: QuantConnect.OptionRight) -> None:
            ...

        @property
        def option_strike(self) -> float:
            """Option strike"""
            ...

        @option_strike.setter
        def option_strike(self, value: float) -> None:
            ...

        @property
        def expiration_date(self) -> datetime.datetime:
            """Expiration date"""
            ...

        @expiration_date.setter
        def expiration_date(self, value: datetime.datetime) -> None:
            ...

    OPTION_CODE_LOOKUP: System.Collections.Generic.IReadOnlyDictionary[str, System.Tuple[int, QuantConnect.OptionRight]]
    """
    A dictionary that maps option symbols to a tuple containing the option series number and the option right (Call or Put).
    The key represents a single character option symbol, and the value contains the series number and the associated option right.
    """

    FUTURES_MONTH_CODE_LOOKUP: System.Collections.Generic.IReadOnlyDictionary[str, int]
    """Provides a lookup dictionary for mapping futures month codes to their corresponding numeric values."""

    FUTURES_MONTH_LOOKUP: System.Collections.Generic.IReadOnlyDictionary[int, str]
    """Provides a lookup dictionary for mapping numeric values to their corresponding futures month codes."""

    @staticmethod
    def generate_future_ticker(underlying: str, expiration: typing.Union[datetime.datetime, datetime.date], double_digits_year: bool = True, include_expiration_date: bool = True) -> str:
        """
        Returns future symbol ticker from underlying and expiration date. Function can generate tickers of two formats: one and two digits year.
        Format <Ticker><2 digit day code><1 char month code><2/1 digit year code>, more information at http://help.tradestation.com/09_01/tradestationhelp/symbology/futures_symbology.htm
        
        :param underlying: String underlying
        :param expiration: Expiration date
        :param double_digits_year: True if year should represented by two digits; False - one digit
        :param include_expiration_date: True if expiration date should be included
        :returns: The user friendly future ticker.
        """
        ...

    @staticmethod
    def generate_option_ticker(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """
        Function returns option ticker from IQFeed option ticker
        For example CSCO1220V19 Cisco October Put at 19.00 Expiring on 10/20/12
        Symbology details: http://www.iqfeed.net/symbolguide/index.cfm?symbolguide=guide&displayaction=support%C2%A7ion=guide&web=iqfeed&guide=options&web=IQFeed&type=stock
        
        :param symbol: THe option symbol
        :returns: The option ticker.
        """
        ...

    @staticmethod
    @overload
    def generate_option_ticker_osi(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """
        Returns option symbol ticker in accordance with OSI symbology
        More information can be found at http://www.optionsclearing.com/components/docs/initiatives/symbology/symbology_initiative_v1_8.pdf
        
        :param symbol: Symbol object to create OSI ticker from
        :returns: The OSI ticker representation.
        """
        ...

    @staticmethod
    @overload
    def generate_option_ticker_osi(underlying: str, right: QuantConnect.OptionRight, strike_price: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> str:
        """
        Returns option symbol ticker in accordance with OSI symbology
        More information can be found at http://www.optionsclearing.com/components/docs/initiatives/symbology/symbology_initiative_v1_8.pdf
        
        :param underlying: Underlying string
        :param right: Option right
        :param strike_price: Option strike
        :param expiration: Option expiration date
        :returns: The OSI ticker representation.
        """
        ...

    @staticmethod
    @overload
    def generate_option_ticker_osi_compact(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """
        Returns option symbol ticker in accordance with OSI symbology
        More information can be found at http://www.optionsclearing.com/components/docs/initiatives/symbology/symbology_initiative_v1_8.pdf
        
        :param symbol: Symbol object to create OSI ticker from
        :returns: The OSI ticker representation.
        """
        ...

    @staticmethod
    @overload
    def generate_option_ticker_osi_compact(underlying: str, right: QuantConnect.OptionRight, strike_price: float, expiration: typing.Union[datetime.datetime, datetime.date]) -> str:
        """
        Returns option symbol ticker in accordance with OSI symbology
        More information can be found at http://www.optionsclearing.com/components/docs/initiatives/symbology/symbology_initiative_v1_8.pdf
        
        :param underlying: Underlying string
        :param right: Option right
        :param strike_price: Option strike
        :param expiration: Option expiration date
        :returns: The OSI ticker representation.
        """
        ...

    @staticmethod
    def parse_future_option_symbol(ticker: str, strike_scale: int = 1) -> QuantConnect.Symbol:
        """
        Creates a future option Symbol from the provided ticker
        
        :param ticker: The future option ticker, for example 'ESZ0 P3590'
        :param strike_scale: Optional the future option strike scale factor
        """
        ...

    @staticmethod
    def parse_future_symbol(ticker: str, future_year: typing.Optional[int] = None) -> QuantConnect.Symbol:
        """
        Helper method to parse and generate a future symbol from a given user friendly representation
        
        :param ticker: The future ticker, for example 'ESZ1'
        :param future_year: Clarifies the year for the current future
        :returns: The future symbol or null if failed.
        """
        ...

    @staticmethod
    def parse_future_ticker(ticker: str) -> QuantConnect.SymbolRepresentation.FutureTickerProperties:
        """
        Function returns underlying name, expiration year, expiration month, expiration day for the future contract ticker. Function detects if
        the format used is either 1 or 2 digits year, and if day code is present (will default to 1rst day of month). Returns null, if parsing failed.
        Format <Ticker><2 digit day code OPTIONAL><1 char month code><2/1 digit year code>
        
        :param ticker: 
        :returns: Results containing 1) underlying name, 2) short expiration year, 3) expiration month.
        """
        ...

    @staticmethod
    def parse_option_ticker_iq_feed(ticker: str) -> QuantConnect.SymbolRepresentation.OptionTickerProperties:
        """
        Function returns option contract parameters (underlying name, expiration date, strike, right) from IQFeed option ticker
        Symbology details: http://www.iqfeed.net/symbolguide/index.cfm?symbolguide=guide&displayaction=support%C2%A7ion=guide&web=iqfeed&guide=options&web=IQFeed&type=stock
        
        :param ticker: IQFeed option ticker
        :returns: Results containing 1) underlying name, 2) option right, 3) option strike 4) expiration date.
        """
        ...

    @staticmethod
    @overload
    def parse_option_ticker_osi(ticker: str, security_type: QuantConnect.SecurityType = ..., market: str = ...) -> QuantConnect.Symbol:
        """
        Parses the specified OSI options ticker into a Symbol object
        
        :param ticker: The OSI compliant option ticker string
        :param security_type: The security type
        :param market: The associated market
        :returns: Symbol object for the specified OSI option ticker string.
        """
        ...

    @staticmethod
    @overload
    def parse_option_ticker_osi(ticker: str, security_type: QuantConnect.SecurityType, option_style: QuantConnect.OptionStyle, market: str) -> QuantConnect.Symbol:
        """
        Parses the specified OSI options ticker into a Symbol object
        
        :param ticker: The OSI compliant option ticker string
        :param security_type: The security type
        :param market: The associated market
        :param option_style: The option style
        :returns: Symbol object for the specified OSI option ticker string.
        """
        ...

    @staticmethod
    @overload
    def try_decompose_option_ticker_osi(ticker: str, option_ticker: typing.Optional[str], expiry: typing.Optional[typing.Union[datetime.datetime, datetime.date]], right: typing.Optional[QuantConnect.OptionRight], strike: typing.Optional[float]) -> typing.Tuple[bool, str, typing.Union[datetime.datetime, datetime.date], QuantConnect.OptionRight, float]:
        """
        Tries to decompose the specified OSI options ticker into its components
        
        :param ticker: The OSI option ticker
        :param option_ticker: The option ticker extracted from the OSI symbol
        :param expiry: The option contract expiry date
        :param right: The option contract right
        :param strike: The option contract strike price
        :returns: True if the OSI symbol was in the right format and could be decomposed.
        """
        ...

    @staticmethod
    @overload
    def try_decompose_option_ticker_osi(ticker: str, security_type: QuantConnect.SecurityType, option_ticker: typing.Optional[str], underlying_ticker: typing.Optional[str], expiry: typing.Optional[typing.Union[datetime.datetime, datetime.date]], right: typing.Optional[QuantConnect.OptionRight], strike: typing.Optional[float]) -> typing.Tuple[bool, str, str, typing.Union[datetime.datetime, datetime.date], QuantConnect.OptionRight, float]:
        """
        Tries to decompose the specified OSI options ticker into its components
        
        :param ticker: The OSI option ticker
        :param security_type: The option security type
        :param option_ticker: The option ticker extracted from the OSI symbol
        :param underlying_ticker: The underlying ticker
        :param expiry: The option contract expiry date
        :param right: The option contract right
        :param strike: The option contract strike price
        :returns: True if the OSI symbol was in the right format and could be decomposed.
        """
        ...


class ChartSeriesJsonConverter:
    """Convert a Chart Series to and from JSON"""

    @property
    def can_read(self) -> bool:
        """This converter wont be used to read JSON. Will throw exception if manually called."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """Indicates whether the given object type can be converted into Chart Series"""
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Converts a JSON file into a Chart Series object"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Converts a Chart Series object into a JSON file"""
        ...


class Market(System.Object):
    """Markets Collection: Soon to be expanded to a collection of items specifying the market hour, timezones and country codes."""

    USA: str = "usa"
    """USA Market"""

    OANDA: str = "oanda"
    """Oanda Market"""

    FXCM: str = "fxcm"
    """FXCM Market Hours"""

    DUKASCOPY: str = "dukascopy"
    """Dukascopy Market"""

    BITFINEX: str = "bitfinex"
    """Bitfinex market"""

    GLOBEX: str = "cmeglobex"
    """CME Globex"""

    NYMEX: str = "nymex"
    """NYMEX"""

    CBOT: str = "cbot"
    """CBOT"""

    ICE: str = "ice"
    """ICE"""

    CBOE: str = "cboe"
    """CBOE"""

    CFE: str = "cfe"
    """CFE"""

    INDIA: str = "india"
    """NSE - National Stock Exchange"""

    COMEX: str = "comex"
    """Comex"""

    CME: str = "cme"
    """CME"""

    EUREX: str = "eurex"
    """EUREX"""

    SGX: str = "sgx"
    """Singapore Exchange"""

    HKFE: str = "hkfe"
    """Hong Kong Exchange"""

    OSE: str = "ose"
    """Osaka Stock Exchange"""

    NYSELIFFE: str = "nyseliffe"
    """London International Financial Futures and Options Exchange"""

    GDAX: str = ...
    """
    GDAX
    
    
    The GDAX constant is deprecated. Please use Coinbase instead.
    """

    KRAKEN: str = "kraken"
    """Kraken"""

    BITSTAMP: str = "bitstamp"
    """Bitstamp"""

    OK_COIN: str = "okcoin"
    """OkCoin"""

    BITHUMB: str = "bithumb"
    """Bithumb"""

    BINANCE: str = "binance"
    """Binance"""

    POLONIEX: str = "poloniex"
    """Poloniex"""

    COINONE: str = "coinone"
    """Coinone"""

    HIT_BTC: str = "hitbtc"
    """HitBTC"""

    BITTREX: str = "bittrex"
    """Bittrex"""

    FTX: str = "ftx"
    """FTX"""

    FTXUS: str = "ftxus"
    """FTX.US"""

    BINANCE_US: str = "binanceus"
    """Binance.US"""

    BYBIT: str = "bybit"
    """Bybit"""

    COINBASE: str = "coinbase"
    """Coinbase"""

    INTERACTIVE_BROKERS: str = "interactivebrokers"
    """InteractiveBrokers market"""

    DYDX: str = "dydx"
    """dYdX market"""

    @staticmethod
    def add(market: str, identifier: int) -> None:
        """
        Adds the specified market to the map of available markets with the specified identifier.
        
        :param market: The market string to add
        :param identifier: The identifier for the market, this value must be positive and less than 1000
        """
        ...

    @staticmethod
    def decode(code: int) -> str:
        """
        Gets the market string for the specified market code.
        
        :param code: The market code to be decoded
        :returns: The string representation of the market, or null if not found.
        """
        ...

    @staticmethod
    def encode(market: str) -> typing.Optional[int]:
        """
        Gets the market code for the specified market. Returns null if the market is not found
        
        :param market: The market to check for (case sensitive)
        :returns: The internal code used for the market. Corresponds to the value used when calling add.
        """
        ...

    @staticmethod
    def supported_markets() -> typing.List[str]:
        """Returns a list of the supported markets"""
        ...


class IIsolatorLimitResultProvider(metaclass=abc.ABCMeta):
    """
    Provides an abstraction for managing isolator limit results.
    This is originally intended to be used by the training feature to permit a single
    algorithm time loop to extend past the default of ten minutes
    """

    def is_within_limit(self) -> QuantConnect.IsolatorLimitResult:
        """Determines whether or not a custom isolator limit has be reached."""
        ...

    def request_additional_time(self, minutes: int) -> None:
        """
        Requests additional time from the isolator result provider. This is intended
        to prevent is_within_limit from returning an error result.
        This method will throw a TimeoutException if there is insufficient
        resources available to fulfill the specified number of minutes.
        
        :param minutes: The number of additional minutes to request
        """
        ...

    def try_request_additional_time(self, minutes: int) -> bool:
        """
        Attempts to request additional time from the isolator result provider. This is intended
        to prevent is_within_limit from returning an error result.
        This method will only return false if there is insufficient resources available to fulfill
        the specified number of minutes.
        
        :param minutes: The number of additional minutes to request
        """
        ...


class StringExtensions(System.Object):
    """
    Provides extension methods for properly parsing and serializing values while properly using
    an IFormatProvider/CultureInfo when applicable
    """

    @staticmethod
    def convert_invariant(value: typing.Any, conversion_type: typing.Type) -> System.Object:
        """
        Converts the provided value as conversion_type
        using CultureInfo
        """
        ...

    @staticmethod
    def ends_with_invariant(value: str, ending: str, ignore_case: bool = False) -> bool:
        """
        Checks if the string ends with the provided ending using CultureInfo
        while optionally ignoring case.
        """
        ...

    @staticmethod
    @overload
    def index_of_invariant(value: str, character: str) -> int:
        """Gets the index of the specified character using StringComparison"""
        ...

    @staticmethod
    @overload
    def index_of_invariant(value: str, substring: str, ignore_case: bool = False) -> int:
        """
        Gets the index of the specified substring using StringComparison
        or System.StringComparison.InvariantCultureIgnoreCase when ignore_case is true
        """
        ...

    @staticmethod
    def invariant(formattable: System.FormattableString) -> str:
        """
        Non-extension method alias for FormattableString.Invariant
        This supports the using static QuantConnect.StringExtensions syntax
        and is aimed at ensuring all formatting is piped through this class instead of
        alternatively piping through directly to FormattableString.Invariant
        """
        ...

    @staticmethod
    def last_index_of_invariant(value: str, substring: str, ignore_case: bool = False) -> int:
        """
        Gets the index of the specified substring using StringComparison
        or System.StringComparison.InvariantCultureIgnoreCase when ignore_case is true
        """
        ...

    @staticmethod
    def safe_substring(value: str, start_index: int, length: int) -> str:
        """
        Retrieves a substring from this instance. The substring starts at a specified
        character position and has a specified length.
        """
        ...

    @staticmethod
    def starts_with_invariant(value: str, beginning: str, ignore_case: bool = False) -> bool:
        """
        Checks if the string starts with the provided beginning using CultureInfo
        while optionally ignoring case.
        """
        ...

    @staticmethod
    def to_iso_8601_invariant(date_time: typing.Union[datetime.datetime, datetime.date]) -> str:
        """Provides a convenience methods for converting a DateTime to an invariant ISO-8601 string"""
        ...

    @staticmethod
    @overload
    def to_string_invariant(convertible: System.IConvertible) -> str:
        """Converts the provided value to a string using CultureInfo"""
        ...

    @staticmethod
    @overload
    def to_string_invariant(formattable: System.IFormattable, format: str) -> str:
        """
        Formats the provided value using the specified format and
        CultureInfo
        """
        ...

    @staticmethod
    def truncate(value: str, max_length: int) -> str:
        """
        Truncates a string to the specified maximum length
        
        :param value: The string
        :param max_length: The maximum allowed string
        :returns: A new string with max_length characters if the original one's length was greater than the maximum allowed length.
        Otherwise, the original string is returned.
        """
        ...


class Time(System.Object):
    """Time helper class collection for working with trading dates"""

    class DateTimeWithZone:
        """Live charting is sensitive to timezone so need to convert the local system time to a UTC and display in browser as UTC."""

        @property
        def universal_time(self) -> datetime.datetime:
            """Gets the universal time."""
            ...

        @property
        def time_zone(self) -> System.TimeZoneInfo:
            """Gets the time zone."""
            ...

        @property
        def local_time(self) -> datetime.datetime:
            """Gets the local time."""
            ...

        def __init__(self, date_time: typing.Union[datetime.datetime, datetime.date], time_zone: System.TimeZoneInfo) -> None:
            """
            Initializes a new instance of the QuantConnect.Time.DateTimeWithZone struct.
            
            :param date_time: Date time.
            :param time_zone: Time zone.
            """
            ...

    class MonthYearJsonConverter:
        """Helper method to deserialize month/year"""

        def __init__(self) -> None:
            """Creates a new instance"""
            ...

    live_auxiliary_data_offset: datetime.timedelta
    """Allows specifying an offset to trigger the tradable date event"""

    END_OF_TIME: datetime.datetime = ...
    """Provides a value far enough in the future the current computer hardware will have decayed :)"""

    end_of_time_time_span: datetime.timedelta = ...
    """Provides a time span based on END_OF_TIME"""

    START: datetime.datetime = ...
    """Provides a common and normalized start time for Lean data"""

    BEGINNING_OF_TIME: datetime.datetime = ...
    """Provides a value far enough in the past that can be used as a lower bound on dates, 12/30/1899"""

    MAX_TIME_SPAN: datetime.timedelta = ...
    """
    Provides a value large enough that we won't hit the limit, while small enough
    we can still do math against it without checking everywhere for TimeSpan.MaxValue
    """

    ONE_YEAR: datetime.timedelta = ...
    """One Year TimeSpan Period Constant"""

    ONE_DAY: datetime.timedelta = ...
    """One Day TimeSpan Period Constant"""

    ONE_HOUR: datetime.timedelta = ...
    """One Hour TimeSpan Period Constant"""

    ONE_MINUTE: datetime.timedelta = ...
    """One Minute TimeSpan Period Constant"""

    ONE_SECOND: datetime.timedelta = ...
    """One Second TimeSpan Period Constant"""

    ONE_MILLISECOND: datetime.timedelta = ...
    """One Millisecond TimeSpan Period Constant"""

    @staticmethod
    def abs(time_span: datetime.timedelta) -> datetime.timedelta:
        """
        Gets the absolute value of the specified time span
        
        :param time_span: Time span whose absolute value we seek
        :returns: The absolute value of the specified time span.
        """
        ...

    @staticmethod
    def date_time_range(_from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date], step: datetime.timedelta) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date time range using the given time step
        
        :param _from: DateTime start date time
        :param thru: DateTime end date time
        :returns: Enumerable date time range.
        """
        ...

    @staticmethod
    def date_time_to_unix_time_stamp(time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Convert a Datetime to Unix Timestamp
        
        :param time: C# datetime object
        :returns: Double unix timestamp.
        """
        ...

    @staticmethod
    def date_time_to_unix_time_stamp_milliseconds(time: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Convert a Datetime to Unix Timestamp
        
        :param time: C# datetime object
        :returns: Double unix timestamp.
        """
        ...

    @staticmethod
    def date_time_to_unix_time_stamp_nanoseconds(time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Convert a Datetime to Unix Timestamp
        
        :param time: C# datetime object
        :returns: Int64 unix timestamp.
        """
        ...

    @staticmethod
    def each_day(_from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date range and return each date as a datetime object in the date range
        
        :param _from: DateTime start date
        :param thru: DateTime end date
        :returns: Enumerable date range.
        """
        ...

    @staticmethod
    @overload
    def each_tradeable_day(securities: System.Collections.Generic.ICollection[QuantConnect.Securities.Security], _from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date]) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date range of tradeable dates - skip the holidays and weekends when securities in this algorithm don't trade.
        
        :param securities: Securities we have in portfolio
        :param _from: Start date
        :param thru: End date
        :returns: Enumerable date range.
        """
        ...

    @staticmethod
    @overload
    def each_tradeable_day(security: QuantConnect.Securities.Security, _from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool = False) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date range of tradeable dates - skip the holidays and weekends when securities in this algorithm don't trade.
        
        :param security: The security to get tradeable dates for
        :param _from: Start date
        :param thru: End date
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: Enumerable date range.
        """
        ...

    @staticmethod
    @overload
    def each_tradeable_day(exchange: QuantConnect.Securities.SecurityExchangeHours, _from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool = False) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date range of tradeable dates - skip the holidays and weekends when securities in this algorithm don't trade.
        
        :param exchange: The security to get tradeable dates for
        :param _from: Start date
        :param thru: End date
        :param extended_market_hours: True to include days with extended market hours only, like sunday for futures
        :returns: Enumerable date range.
        """
        ...

    @staticmethod
    def each_tradeable_day_in_time_zone(exchange: QuantConnect.Securities.SecurityExchangeHours, _from: typing.Union[datetime.datetime, datetime.date], thru: typing.Union[datetime.datetime, datetime.date], time_zone: typing.Any, include_extended_market_hours: bool = True) -> typing.Iterable[datetime.datetime]:
        """
        Define an enumerable date range of tradeable dates but expressed in a different time zone.
        
        :param exchange: The exchange hours
        :param _from: The start time in the exchange time zone
        :param thru: The end time in the exchange time zone (inclusive of the final day)
        :param time_zone: The timezone to project the dates into (inclusive of the final day)
        :param include_extended_market_hours: True to include extended market hours trading in the search, false otherwise
        """
        ...

    @staticmethod
    def get_end_time_for_trade_bars(exchange_hours: QuantConnect.Securities.SecurityExchangeHours, start: typing.Union[datetime.datetime, datetime.date], bar_size: datetime.timedelta, bar_count: int, extended_market_hours: bool) -> datetime.datetime:
        """
        Determines the end time at which the requested number of bars of the given  will have elapsed.
        NOTE: The start time is not discretized by bar_size units like is done in get_start_time_for_trade_bars
        
        :param exchange_hours: The exchange hours used to test for market open hours
        :param start: The end time of the last bar over the requested period
        :param bar_size: The length of each bar
        :param bar_count: The number of bars requested
        :param extended_market_hours: True to allow extended market hours bars, otherwise false for only normal market hours
        :returns: The start time that would provide the specified number of bars ending at the specified end time, rounded down by the requested bar size.
        """
        ...

    @staticmethod
    @overload
    def get_next_live_auxiliary_data_due_time() -> datetime.timedelta:
        """
        Helper method to get the new live auxiliary data due time
        
        :returns: The due time for the new auxiliary data emission.
        """
        ...

    @staticmethod
    @overload
    def get_next_live_auxiliary_data_due_time(utc_now: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        """
        Helper method to get the new live auxiliary data due time
        
        :param utc_now: The current utc time
        :returns: The due time for the new auxiliary data emission.
        """
        ...

    @staticmethod
    def get_number_of_trade_bars_in_interval(exchange_hours: QuantConnect.Securities.SecurityExchangeHours, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], bar_size: datetime.timedelta) -> int:
        """
        Gets the number of trade bars of the specified bar_size that fit between the start and end
        
        :param exchange_hours: The exchange used to test for market open hours
        :param start: The start time of the interval in the exchange time zone
        :param end: The end time of the interval in the exchange time zone
        :param bar_size: The step size used to count number of bars between start and end
        :returns: The number of bars of the specified size between start and end times.
        """
        ...

    @staticmethod
    @overload
    def get_second_uneven_wait(wait_time_millis: int) -> int:
        """
        Helper method to adjust a waiting time, in milliseconds, so it's uneven with the second turn around
        
        :param wait_time_millis: The desired wait time
        :returns: The adjusted wait time.
        """
        ...

    @staticmethod
    @overload
    def get_second_uneven_wait(now: typing.Union[datetime.datetime, datetime.date], wait_time_millis: int) -> int:
        """
        Helper method to adjust a waiting time, in milliseconds, so it's uneven with the second turn around
        
        :param now: The current time
        :param wait_time_millis: The desired wait time
        :returns: The adjusted wait time.
        """
        ...

    @staticmethod
    def get_start_time_for_trade_bars(exchange_hours: QuantConnect.Securities.SecurityExchangeHours, end: typing.Union[datetime.datetime, datetime.date], bar_size: datetime.timedelta, bar_count: int, extended_market_hours: bool, data_time_zone: typing.Any, daily_precise_end_time: bool = False) -> datetime.datetime:
        """
        Determines the start time required to produce the requested number of bars and the given size
        
        :param exchange_hours: The exchange hours used to test for market open hours
        :param end: The end time of the last bar over the requested period
        :param bar_size: The length of each bar
        :param bar_count: The number of bars requested
        :param extended_market_hours: True to allow extended market hours bars, otherwise false for only normal market hours
        :param data_time_zone: Timezone for this data
        :param daily_precise_end_time: True if daily strict end times are enabled
        :returns: The start time that would provide the specified number of bars ending at the specified end time, rounded down by the requested bar size.
        """
        ...

    @staticmethod
    @overload
    def max(one: datetime.timedelta, two: datetime.timedelta) -> datetime.timedelta:
        """Returns the timespan with the larger value"""
        ...

    @staticmethod
    @overload
    def max(one: typing.Union[datetime.datetime, datetime.date], two: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Returns the larger of two date times"""
        ...

    @staticmethod
    @overload
    def min(one: datetime.timedelta, two: datetime.timedelta) -> datetime.timedelta:
        """Returns the timespan with the smaller value"""
        ...

    @staticmethod
    @overload
    def min(one: typing.Union[datetime.datetime, datetime.date], two: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Returns the smaller of two date times"""
        ...

    @staticmethod
    def multiply(interval: datetime.timedelta, multiplier: float) -> datetime.timedelta:
        """
        Multiplies the specified interval by the multiplier
        
        :param interval: The interval to be multiplied, such as TimeSpan.FromSeconds(1)
        :param multiplier: The number of times to multiply the interval
        :returns: The multiplied interval, such as 1s*5 = 5s.
        """
        ...

    @staticmethod
    def normalize_instant_within_range(start: typing.Union[datetime.datetime, datetime.date], current: typing.Union[datetime.datetime, datetime.date], period: datetime.timedelta) -> float:
        """
        Normalizes the current time within the specified period
        time = start => 0
        time = start + period => 1
        
        :param start: The start time of the range
        :param current: The current time we seek to normalize
        :param period: The time span of the range
        :returns: The normalized time.
        """
        ...

    @staticmethod
    def normalize_time_step(period: datetime.timedelta, step_size: datetime.timedelta) -> float:
        """
        Normalizes the step size as a percentage of the period.
        
        :param period: The period to normalize against
        :param step_size: The step size to be normaized
        :returns: The normalized step size as a percentage of the period.
        """
        ...

    @staticmethod
    def parse_date(date_to_parse: str) -> datetime.datetime:
        """
        Parse a standard YY MM DD date into a DateTime. Attempt common date formats
        
        :param date_to_parse: String date time to parse
        :returns: Date time.
        """
        ...

    @staticmethod
    def parse_fix_utc_timestamp(date_to_parse: str) -> datetime.datetime:
        """
        Parse a standard YY MM DD date into a DateTime. Attempt common date formats
        
        :param date_to_parse: String date time to parse
        :returns: Date time.
        """
        ...

    @staticmethod
    def time_stamp() -> float:
        """
        Get the current time as a unix timestamp
        
        :returns: Double value of the unix as UTC timestamp.
        """
        ...

    @staticmethod
    def tradable_date(securities: typing.List[QuantConnect.Securities.Security], day: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Make sure this date is not a holiday, or weekend for the securities in this algorithm.
        
        :param securities: Security manager from the algorithm
        :param day: DateTime to check if trade-able.
        :returns: True if tradeable date.
        """
        ...

    @staticmethod
    def tradeable_dates(securities: System.Collections.Generic.ICollection[QuantConnect.Securities.Security], start: typing.Union[datetime.datetime, datetime.date], finish: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Could of the number of tradeable dates within this period.
        
        :param securities: Securities we're trading
        :param start: Start of Date Loop
        :param finish: End of Date Loop
        :returns: Number of dates.
        """
        ...

    @staticmethod
    def unix_millisecond_time_stamp_to_date_time(unix_time_stamp: float) -> datetime.datetime:
        """
        Create a C# DateTime from a UnixTimestamp
        
        :param unix_time_stamp: Decimal unix timestamp (Time since Midnight Jan 1 1970) in milliseconds
        :returns: C# date time object.
        """
        ...

    @staticmethod
    def unix_nanosecond_time_stamp_to_date_time(unix_time_stamp: int) -> datetime.datetime:
        """
        Create a C# DateTime from a UnixTimestamp
        
        :param unix_time_stamp: Int64 unix timestamp (Time since Midnight Jan 1 1970) in nanoseconds
        :returns: C# date time object.
        """
        ...

    @staticmethod
    @overload
    def unix_time_stamp_to_date_time(unix_time_stamp: float) -> datetime.datetime:
        """
        Create a C# DateTime from a UnixTimestamp
        
        :param unix_time_stamp: Double unix timestamp (Time since Midnight Jan 1 1970)
        :returns: C# date timeobject.
        """
        ...

    @staticmethod
    @overload
    def unix_time_stamp_to_date_time(unix_time_stamp: int) -> datetime.datetime:
        """
        Create a C# DateTime from a UnixTimestamp
        
        :param unix_time_stamp: Long unix timestamp (Time since Midnight Jan 1 1970)
        :returns: C# date time object.
        """
        ...


class TimeZones(System.Object):
    """Provides access to common time zones"""

    UTC: typing.Any = ...
    """Gets the Universal Coordinated time zone."""

    NEW_YORK: typing.Any = ...
    """Gets the time zone for New York City, USA. This is a daylight savings time zone."""

    EASTERN_STANDARD: typing.Any = ...
    """Get the Eastern Standard Time (EST) WITHOUT daylight savings, this is a constant -5 hour offset"""

    LONDON: typing.Any = ...
    """Gets the time zone for London, England. This is a daylight savings time zone."""

    HONG_KONG: typing.Any = ...
    """Gets the time zone for Hong Kong, China."""

    TOKYO: typing.Any = ...
    """Gets the time zone for Tokyo, Japan."""

    ROME: typing.Any = ...
    """Gets the time zone for Rome, Italy. This is a daylight savings time zone."""

    SYDNEY: typing.Any = ...
    """Gets the time zone for Sydney, Australia. This is a daylight savings time zone."""

    VANCOUVER: typing.Any = ...
    """Gets the time zone for Vancouver, Canada."""

    TORONTO: typing.Any = ...
    """Gets the time zone for Toronto, Canada. This is a daylight savings time zone."""

    CHICAGO: typing.Any = ...
    """Gets the time zone for Chicago, USA. This is a daylight savings time zone."""

    LOS_ANGELES: typing.Any = ...
    """Gets the time zone for Los Angeles, USA. This is a daylight savings time zone."""

    PHOENIX: typing.Any = ...
    """Gets the time zone for Phoenix, USA. This is a daylight savings time zone."""

    AUCKLAND: typing.Any = ...
    """Gets the time zone for Auckland, New Zealand. This is a daylight savings time zone."""

    MOSCOW: typing.Any = ...
    """Gets the time zone for Moscow, Russia."""

    MADRID: typing.Any = ...
    """Gets the time zone for Madrid, Span. This is a daylight savings time zone."""

    BUENOS_AIRES: typing.Any = ...
    """Gets the time zone for Buenos Aires, Argentia."""

    BRISBANE: typing.Any = ...
    """Gets the time zone for Brisbane, Australia."""

    SAO_PAULO: typing.Any = ...
    """Gets the time zone for Sao Paulo, Brazil. This is a daylight savings time zone."""

    CAIRO: typing.Any = ...
    """Gets the time zone for Cairo, Egypt."""

    JOHANNESBURG: typing.Any = ...
    """Gets the time zone for Johannesburg, South Africa."""

    ANCHORAGE: typing.Any = ...
    """Gets the time zone for Anchorage, USA. This is a daylight savings time zone."""

    DENVER: typing.Any = ...
    """Gets the time zone for Denver, USA. This is a daylight savings time zone."""

    DETROIT: typing.Any = ...
    """Gets the time zone for Detroit, USA. This is a daylight savings time zone."""

    MEXICO_CITY: typing.Any = ...
    """Gets the time zone for Mexico City, Mexico. This is a daylight savings time zone."""

    JERUSALEM: typing.Any = ...
    """Gets the time zone for Jerusalem, Israel. This is a daylight savings time zone."""

    SHANGHAI: typing.Any = ...
    """Gets the time zone for Shanghai, China."""

    MELBOURNE: typing.Any = ...
    """Gets the time zone for Melbourne, Australia. This is a daylight savings time zone."""

    AMSTERDAM: typing.Any = ...
    """Gets the time zone for Amsterdam, Netherlands. This is a daylight savings time zone."""

    ATHENS: typing.Any = ...
    """Gets the time zone for Athens, Greece. This is a daylight savings time zone."""

    BERLIN: typing.Any = ...
    """Gets the time zone for Berlin, Germany. This is a daylight savings time zone."""

    BUCHAREST: typing.Any = ...
    """Gets the time zone for Bucharest, Romania. This is a daylight savings time zone."""

    DUBLIN: typing.Any = ...
    """Gets the time zone for Dublin, Ireland. This is a daylight savings time zone."""

    HELSINKI: typing.Any = ...
    """Gets the time zone for Helsinki, Finland. This is a daylight savings time zone."""

    ISTANBUL: typing.Any = ...
    """Gets the time zone for Istanbul, Turkey. This is a daylight savings time zone."""

    MINSK: typing.Any = ...
    """Gets the time zone for Minsk, Belarus."""

    PARIS: typing.Any = ...
    """Gets the time zone for Paris, France. This is a daylight savings time zone."""

    ZURICH: typing.Any = ...
    """Gets the time zone for Zurich, Switzerland. This is a daylight savings time zone."""

    HONOLULU: typing.Any = ...
    """Gets the time zone for Honolulu, USA. This is a daylight savings time zone."""

    KOLKATA: typing.Any = ...
    """Gets the time zone for Kolkata, India."""


class Globals(System.Object):
    """Provides application level constant values"""

    api: str
    """The base api url address to use"""

    user_id: int
    """The user Id"""

    project_id: int
    """The project id"""

    user_token: str
    """The user token"""

    organization_id: str
    """The organization id"""

    results_destination_folder: str
    """The results destination folder"""

    data_folder: str
    """The root directory of the data folder for this application"""

    live_mode: bool
    """True if running in live mode"""

    CACHE: str = "./cache/data"
    """The directory used for storing downloaded remote files"""

    version: str
    """The version of lean"""

    cache_data_folder: str
    """Data path to cache folder location"""

    @staticmethod
    def get_data_folder_path(relative_path: str) -> str:
        """Helper method that will build a data folder path checking if it exists on the cache folder else will return data folder"""
        ...

    @staticmethod
    def reset() -> None:
        """Resets global values with the Config data."""
        ...


class ExtendedDictionary(typing.Generic[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue], System.Object, QuantConnect.Interfaces.IExtendedDictionary[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue], metaclass=abc.ABCMeta):
    """Provides a base class for types holding key value pairs with helper methods for easy usage in Python"""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        """Gets the number of elements contained in the dictionary"""
        ...

    @property
    @abc.abstractmethod
    def get_keys(self) -> typing.Iterable[QuantConnect_ExtendedDictionary_TKey]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the key objects of the System.Collections.Generic.IDictionary`2.
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    @abc.abstractmethod
    def get_values(self) -> typing.Iterable[QuantConnect_ExtendedDictionary_TValue]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2.
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def is_read_only(self) -> bool:
        """Gets a value indicating whether the IDictionary object is read-only."""
        ...

    def __contains__(self, key: QuantConnect_ExtendedDictionary_TKey) -> bool:
        """
        Checks if the dictionary contains the specified key.
        
        :param key: The key to locate in the dictionary
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...

    def __getitem__(self, key: QuantConnect_ExtendedDictionary_TKey) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Indexer method for the base dictioanry to access the objects by their symbol.
        
        :param key: Key object indexer
        :returns: Object of t_value.
        """
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: QuantConnect_ExtendedDictionary_TKey, value: QuantConnect_ExtendedDictionary_TValue) -> None:
        """
        Indexer method for the base dictioanry to access the objects by their symbol.
        
        :param key: Key object indexer
        :returns: Object of t_value.
        """
        ...

    def check_for_implicitly_created_symbol(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        """
        Checks if the symbol is implicitly created from a string, in which case it is not in the symbol cache,
        and throws a KeyNotFoundException.
        
        
        This codeEntityType is protected.
        """
        ...

    def clear(self) -> None:
        """Removes all keys and values from the IExtendedDictionary{TKey, TValue}."""
        ...

    def clear(self) -> None:
        """Removes all items from the System.Collections.Generic.ICollection`1."""
        ...

    def contains_key(self, key: QuantConnect_ExtendedDictionary_TKey) -> bool:
        """
        Checks if the dictionary contains the specified key.
        
        :param key: The key to locate in the dictionary
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...

    def copy(self) -> typing.Dict[typing.Any, typing.Any]:
        """
        Creates a shallow copy of the IExtendedDictionary{TKey, TValue}.
        
        :returns: Returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
        """
        ...

    @overload
    def fromkeys(self, sequence: typing.List[QuantConnect_ExtendedDictionary_TKey]) -> typing.Dict[typing.Any, typing.Any]:
        """
        Creates a new dictionary from the given sequence of elements.
        
        :param sequence: Sequence of elements which is to be used as keys for the new dictionary
        :returns: Returns a new dictionary with the given sequence of elements as the keys of the dictionary.
        """
        ...

    @overload
    def fromkeys(self, sequence: typing.List[QuantConnect_ExtendedDictionary_TKey], value: QuantConnect_ExtendedDictionary_TValue) -> typing.Dict[typing.Any, typing.Any]:
        """
        Creates a new dictionary from the given sequence of elements with a value provided by the user.
        
        :param sequence: Sequence of elements which is to be used as keys for the new dictionary
        :param value: Value which is set to each each element of the dictionary
        :returns: Returns a new dictionary with the given sequence of elements as the keys of the dictionary.
        Each element of the newly created dictionary is set to the provided value.
        """
        ...

    @overload
    def get(self, key: QuantConnect_ExtendedDictionary_TKey) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Returns the value for the specified key if key is in dictionary.
        
        :param key: key to be searched in the dictionary
        :returns: The value for the specified key if key is in dictionary.
        None if the key is not found and value is not specified.
        """
        ...

    @overload
    def get(self, key: QuantConnect_ExtendedDictionary_TKey, value: QuantConnect_ExtendedDictionary_TValue) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Returns the value for the specified key if key is in dictionary.
        
        :param key: key to be searched in the dictionary
        :param value: Value to be returned if the key is not found. The default value is null.
        :returns: The value for the specified key if key is in dictionary.
        value if the key is not found and value is specified.
        """
        ...

    def get_items(self) -> typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect_ExtendedDictionary_TKey, QuantConnect_ExtendedDictionary_TValue]]:
        """
        Gets all the items in the dictionary
        
        :returns: All the items in the dictionary.
        """
        ...

    def items(self) -> typing.List[typing.Any]:
        """
        Returns a view object that displays a list of dictionary's (key, value) tuple pairs.
        
        :returns: Returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
        """
        ...

    def keys(self) -> typing.List[typing.Any]:
        """
        Returns a view object that displays a list of all the key objects in the dictionary
        
        :returns: Returns a view object that displays a list of all the key objects.
        When the dictionary is changed, the view object also reflect these changes.
        """
        ...

    @overload
    def pop(self, key: QuantConnect_ExtendedDictionary_TKey) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Removes and returns an element from a dictionary having the given key.
        
        :param key: Key which is to be searched for removal
        :returns: If key is found - removed/popped element from the dictionary
        If key is not found - KeyError exception is raised.
        """
        ...

    @overload
    def pop(self, key: QuantConnect_ExtendedDictionary_TKey, default_value: QuantConnect_ExtendedDictionary_TValue) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Removes and returns an element from a dictionary having the given key.
        
        :param key: Key which is to be searched for removal
        :param default_value: Value which is to be returned when the key is not in the dictionary
        :returns: If key is found - removed/popped element from the dictionary
        If key is not found - value specified as the second argument(default).
        """
        ...

    def popitem(self) -> typing.Any:
        """
        Returns and removes an arbitrary element (key, value) pair from the dictionary.
        
        :returns: Returns an arbitrary element (key, value) pair from the dictionary
        removes an arbitrary element(the same element which is returned) from the dictionary.
        Note: Arbitrary elements and random elements are not same.The popitem() doesn't return a random element.
        """
        ...

    def remove(self, key: QuantConnect_ExtendedDictionary_TKey) -> bool:
        """
        Removes the value with the specified key
        
        :param key: The key object of the element to remove.
        :returns: true if the element is successfully found and removed; otherwise, false.
        """
        ...

    @overload
    def setdefault(self, key: QuantConnect_ExtendedDictionary_TKey) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
        
        :param key: Key with null/None value is inserted to the dictionary if key is not in the dictionary.
        :returns: The value of the key if it is in the dictionary
        None if key is not in the dictionary.
        """
        ...

    @overload
    def setdefault(self, key: QuantConnect_ExtendedDictionary_TKey, default_value: QuantConnect_ExtendedDictionary_TValue) -> QuantConnect_ExtendedDictionary_TValue:
        """
        Returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
        
        :param key: Key with a value default_value is inserted to the dictionary if key is not in the dictionary.
        :param default_value: Default value
        :returns: The value of the key if it is in the dictionary
        default_value if key is not in the dictionary and default_value is specified.
        """
        ...

    def try_get_value(self, key: QuantConnect_ExtendedDictionary_TKey, value: typing.Optional[QuantConnect_ExtendedDictionary_TValue]) -> typing.Tuple[bool, QuantConnect_ExtendedDictionary_TValue]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :param value: When this method returns, the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter. This parameter is passed uninitialized.
        :returns: true if the object that implements System.Collections.Generic.IDictionary`2 contains an element with the specified key; otherwise, false.
        """
        ...

    def update(self, other: typing.Any) -> None:
        """
        Updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
        The update() method adds element(s) to the dictionary if the key is not in the dictionary.If the key is in the dictionary, it updates the key with the new value.
        
        :param other: Takes either a dictionary or an iterable object of key/value pairs (generally tuples).
        """
        ...

    def values(self) -> typing.List[typing.Any]:
        """
        Returns a view object that displays a list of all the values in the dictionary.
        
        :returns: Returns a view object that displays a list of all values in a given dictionary.
        """
        ...


class IsolatorLimitResultProvider(System.Object):
    """Provides access to the NullIsolatorLimitResultProvider and extension methods supporting ScheduledEvent"""

    NULL: QuantConnect.IIsolatorLimitResultProvider = ...
    """Provides access to a null implementation of IIsolatorLimitResultProvider"""

    @staticmethod
    @overload
    def consume(isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider, scheduled_event: QuantConnect.Scheduling.ScheduledEvent, scan_time_utc: typing.Union[datetime.datetime, datetime.date], time_monitor: QuantConnect.Scheduling.TimeMonitor) -> None:
        """Convenience method for invoking a scheduled event's Scan method inside the IsolatorLimitResultProvider"""
        ...

    @staticmethod
    @overload
    def consume(isolator_limit_provider: QuantConnect.IIsolatorLimitResultProvider, time_provider: QuantConnect.ITimeProvider, code: typing.Callable[[], typing.Any], time_monitor: QuantConnect.Scheduling.TimeMonitor) -> None:
        """
        Executes the provided code block and while the code block is running, continually consume from
        the limit result provided one token each minute. This function allows the code to run for the
        first full minute without requesting additional time from the provider. Following that, every
        minute an additional one minute will be requested from the provider.
        """
        ...


class CapacityEstimate(System.Object):
    """Estimates dollar volume capacity of algorithm (in account currency) using all Symbols in the portfolio."""

    @property
    def capacity(self) -> float:
        """The total capacity of the strategy at a point in time"""
        ...

    @property
    def lowest_capacity_asset(self) -> QuantConnect.Symbol:
        """Provide a reference to the lowest capacity symbol used in scaling down the capacity for debugging."""
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes an instance of the class.
        
        :param algorithm: Used to get data at the current time step and access the portfolio state
        """
        ...

    def on_order_event(self, order_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Processes an order whenever it's encountered so that we can calculate the capacity
        
        :param order_event: Order event to use to calculate capacity
        """
        ...

    def update_market_capacity(self, force_process: bool) -> None:
        ...


class ChartType(IntEnum):
    """Type of chart - should we draw the series as overlayed or stacked"""

    OVERLAY = 0

    STACKED = 1


class Chart(System.Object):
    """Single Parent Chart Object for Custom Charting"""

    @property
    def name(self) -> str:
        """Name of the Chart"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def chart_type(self) -> QuantConnect.ChartType:
        """ChartType is now obsolete. Please use Series indexes instead by setting index in the series constructor."""
        warnings.warn("ChartType is now obsolete. Please use Series indexes instead by setting index in the series constructor.", DeprecationWarning)

    @chart_type.setter
    def chart_type(self, value: QuantConnect.ChartType) -> None:
        warnings.warn("ChartType is now obsolete. Please use Series indexes instead by setting index in the series constructor.", DeprecationWarning)

    @property
    def series(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.BaseSeries]:
        ...

    @series.setter
    def series(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.BaseSeries]) -> None:
        ...

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Associated symbol if any, making this an asset plot"""
        ...

    @symbol.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def legend_disabled(self) -> bool:
        """True to hide this series legend from the chart"""
        ...

    @legend_disabled.setter
    def legend_disabled(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for chart:"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Constructor for a chart
        
        :param name: String name of the chart
        """
        ...

    @overload
    def __init__(self, name: str, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        """
        Constructor for a chart
        
        :param name: String name of the chart
        :param symbol: Associated symbol if any
        """
        ...

    @overload
    def __init__(self, name: str, type: QuantConnect.ChartType = ...) -> None:
        """
        Chart Constructor:
        
        
        ChartType is now obsolete and ignored in charting. Please use Series indexes instead by setting index in the series constructor.
        
        :param name: Name of the Chart
        :param type: Type of the chart
        """
        ...

    def add_series(self, series: QuantConnect.BaseSeries) -> None:
        """
        Add a reference to this chart series:
        
        :param series: Chart series class object
        """
        ...

    def aggregate(self, series_type: QuantConnect.SeriesType = ...) -> QuantConnect.Chart:
        """Helper method to consolidate a chart into a single series chart by summing all values"""
        ...

    def clone(self) -> QuantConnect.Chart:
        """Return a new instance clone of this object"""
        ...

    def clone_empty(self) -> QuantConnect.Chart:
        """Return a new empty instance clone of this object"""
        ...

    def get_updates(self) -> QuantConnect.Chart:
        """
        Fetch a chart with only the updates since the last request,
        Underlying series will save the index position.
        """
        ...

    @overload
    def try_add_and_get_series(self, name: str, type: QuantConnect.SeriesType, index: int, unit: str, color: System.Drawing.Color, symbol: QuantConnect.ScatterMarkerSymbol, force_add_new: bool = False) -> QuantConnect.Series:
        """
        Gets Series if already present in chart, else will add a new series and return it
        
        :param name: Name of the series
        :param type: Type of the series
        :param index: Index position on the chart of the series
        :param unit: Unit for the series axis
        :param color: Color of the series
        :param symbol: Symbol for the marker in a scatter plot series
        :param force_add_new: True will always add a new Series instance, stepping on existing if any
        """
        ...

    @overload
    def try_add_and_get_series(self, name: str, template_series: QuantConnect.BaseSeries, force_add_new: bool = False) -> QuantConnect.BaseSeries:
        """
        Gets Series if already present in chart, else will add a new series and return it
        
        :param name: Name of the series
        :param template_series: Series to be used as a template. It will be clone without values if the series is added to the chart
        :param force_add_new: True will always add a new Series instance, stepping on existing if any
        """
        ...


class Result(System.Object):
    """
    Base class for backtesting and live results that packages result data.
    LiveResultBacktestResult
    """

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @charts.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...

    @property
    def orders(self) -> System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]:
        """Order updates since the last result packet"""
        ...

    @orders.setter
    def orders(self, value: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]) -> None:
        ...

    @property
    def order_events(self) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """OrderEvent updates since the last result packet"""
        ...

    @order_events.setter
    def order_events(self, value: typing.List[QuantConnect.Orders.OrderEvent]) -> None:
        ...

    @property
    def profit_loss(self) -> System.Collections.Generic.IDictionary[datetime.datetime, float]:
        """Trade profit and loss information since the last algorithm result packet"""
        ...

    @profit_loss.setter
    def profit_loss(self, value: System.Collections.Generic.IDictionary[datetime.datetime, float]) -> None:
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Statistics information sent during the algorithm operations."""
        ...

    @statistics.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @runtime_statistics.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def state(self) -> System.Collections.Generic.IDictionary[str, str]:
        """State of the result packet."""
        ...

    @state.setter
    def state(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def server_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Server status information, including CPU/RAM usage, ect..."""
        ...

    @server_statistics.setter
    def server_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def algorithm_configuration(self) -> QuantConnect.AlgorithmConfiguration:
        """The algorithm's configuration required for report generation"""
        ...

    @algorithm_configuration.setter
    def algorithm_configuration(self, value: QuantConnect.AlgorithmConfiguration) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @total_performance.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Creates new empty instance"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.BaseResultParameters) -> None:
        """Creates a new result from the given parameters"""
        ...


class DataDownloaderGetParameters(System.Object):
    """Model class for passing in parameters for historical data"""

    @property
    def symbol(self) -> QuantConnect.Symbol:
        """Symbol for the data we're looking for."""
        ...

    @symbol.setter
    def symbol(self, value: QuantConnect.Symbol) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Resolution of the data request"""
        ...

    @resolution.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def start_utc(self) -> datetime.datetime:
        """Start time of the data in UTC"""
        ...

    @start_utc.setter
    def start_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_utc(self) -> datetime.datetime:
        """End time of the data in UTC"""
        ...

    @end_utc.setter
    def end_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """The type of tick to get"""
        ...

    @tick_type.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], resolution: QuantConnect.Resolution, start_utc: typing.Union[datetime.datetime, datetime.date], end_utc: typing.Union[datetime.datetime, datetime.date], tick_type: typing.Optional[QuantConnect.TickType] = None) -> None:
        """
        Initialize model class for passing in parameters for historical data
        
        :param symbol: Symbol for the data we're looking for.
        :param resolution: Resolution of the data request
        :param start_utc: Start time of the data in UTC
        :param end_utc: End time of the data in UTC
        :param tick_type: <Optional> The type of tick to get. Defaults to QuantConnect.TickType.Trade
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string representation of the DataDownloaderGetParameters object.
        
        :returns: A string representing the object's properties.
        """
        ...


class AlgorithmUtils(System.Object):
    """Provides utility methods for or related to algorithms"""

    @staticmethod
    def seed_securities(securities: typing.Sequence[QuantConnect.Securities.Security], algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Seeds the provided securities with their last known prices from the algorithm
        
        :param securities: The securities to seed
        :param algorithm: The algorithm instance
        """
        ...


class Currencies(System.Object):
    """Provides commonly used currency pairs and symbols"""

    USD: str = "USD"
    """USD (United States Dollar) currency string"""

    EUR: str = "EUR"
    """EUR (Euro) currency string"""

    GBP: str = "GBP"
    """GBP (British pound sterling) currency string"""

    INR: str = "INR"
    """INR (Indian rupee) currency string"""

    IDR: str = "IDR"
    """IDR (Indonesian rupiah) currency string"""

    CNH: str = "CNH"
    """CNH (Chinese Yuan Renminbi) currency string"""

    CHF: str = "CHF"
    """CHF (Swiss Franc) currency string"""

    HKD: str = "HKD"
    """HKD (Hong Kong dollar) currency string"""

    JPY: str = "JPY"
    """JPY (Japanese yen) currency string"""

    NULL_CURRENCY: str = "QCC"
    """Null currency used when a real one is not required"""

    CURRENCY_SYMBOLS: System.Collections.Generic.IReadOnlyDictionary[str, str] = ...
    """A mapping of currency codes to their display symbols"""

    STABLE_PAIRS_GDAX: System.Collections.Generic.HashSet[str] = ...
    """
    Stable pairs in GDAX. We defined them because they have different fees in GDAX market
    
    
    StablePairsGDAX is deprecated. Use StablePairsCoinbase instead.
    """

    STABLE_PAIRS_COINBASE: System.Collections.Generic.HashSet[str] = ...
    """Stable pairs in Coinbase. We defined them because they have different fees in Coinbase market"""

    @staticmethod
    def get_currency_symbol(currency: str) -> str:
        """
        Gets the currency symbol for the specified currency code
        
        :param currency: The currency code
        :returns: The currency symbol.
        """
        ...

    @staticmethod
    def is_stable_coin_without_pair(symbol: str, market: str) -> bool:
        """
        Checks whether or not certain symbol is a StableCoin without pair in a given market
        
        :param symbol: The Symbol from wich we want to know if it's a StableCoin without pair
        :param market: The market in which we want to search for that StableCoin
        :returns: True if the given symbol is a StableCoin without pair in the given market.
        """
        ...

    @staticmethod
    def parse(value: str) -> float:
        """
        Converts the string representation of number with currency in the format {currency}{value} to its decimal equivalent.
        It throws if the value cannot be converted to a decimal number.
        
        :param value: The value with currency
        :returns: The decimal equivalent to the value.
        """
        ...

    @staticmethod
    def try_parse(value: str, parsed_value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Converts the string representation of number with currency in the format {currency}{value} to its decimal equivalent.
        
        :param value: The value with currency
        :param parsed_value: The decimal equivalent to the string value after conversion
        :returns: True if the value was succesfuly converted.
        """
        ...


class DataMonitorReport(System.Object):
    """Report generated by the IDataMonitor class that contains information about data requests"""

    @property
    def succeeded_data_requests_count(self) -> int:
        """Gets the number of data files that were requested and successfully fetched"""
        ...

    @succeeded_data_requests_count.setter
    def succeeded_data_requests_count(self, value: int) -> None:
        ...

    @property
    def failed_data_requests_count(self) -> int:
        """Gets the number of data files that were requested but could not be fetched"""
        ...

    @failed_data_requests_count.setter
    def failed_data_requests_count(self, value: int) -> None:
        ...

    @property
    def succeeded_universe_data_requests_count(self) -> int:
        """Gets the number of universe data files that were requested and successfully fetched"""
        ...

    @succeeded_universe_data_requests_count.setter
    def succeeded_universe_data_requests_count(self, value: int) -> None:
        ...

    @property
    def failed_universe_data_requests_count(self) -> int:
        """Gets the number of universe data files that were requested but could not be fetched"""
        ...

    @failed_universe_data_requests_count.setter
    def failed_universe_data_requests_count(self, value: int) -> None:
        ...

    @property
    def total_requests_count(self) -> int:
        """Gets the number of data files that were requested"""
        ...

    @property
    def failed_data_requests_percentage(self) -> float:
        """Fets the percentage of data requests that could not be satisfied"""
        ...

    @property
    def total_universe_data_requests_count(self) -> int:
        """Gets the number of universe data files that were requested"""
        ...

    @property
    def failed_universe_data_requests_percentage(self) -> float:
        """Fets the percentage of universe data requests that could not be satisfied"""
        ...

    @property
    def data_request_rates(self) -> typing.Sequence[float]:
        """Rates at which data requests were made per second"""
        ...

    @data_request_rates.setter
    def data_request_rates(self, value: typing.Sequence[float]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes an empty instance of the DataMonitorReport class"""
        ...

    @overload
    def __init__(self, succeeded_data_requests_count: int, failed_data_requests_count: int, succeeded_universe_data_requests_count: int, failed_universe_data_requests_count: int, data_request_rates: typing.Sequence[float]) -> None:
        """
        Initializes a new instance of the DataMonitorReport class
        
        :param succeeded_data_requests_count: Number of data paths that were requested and successfuly served
        :param failed_data_requests_count: Number of data paths that were requested but could not be served
        :param succeeded_universe_data_requests_count: Number of universe data paths that were requested and successfuly served
        :param failed_universe_data_requests_count: Number of universe data paths that were requested but could not be served
        :param data_request_rates: Rates at which data requests were made per second
        """
        ...


class CandlestickSeries(QuantConnect.BaseSeries):
    """Candlestick Chart Series Object - Series data and properties for a candlestick chart"""

    @overload
    def __init__(self) -> None:
        """Default constructor for chart series"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        """
        ...

    @overload
    def __init__(self, name: str, index: int) -> None:
        """
        Foundational constructor on the series class
        
        :param name: Name of the series
        :param index: Index position on the chart of the series
        """
        ...

    @overload
    def __init__(self, name: str, index: int, unit: str) -> None:
        """
        Foundational constructor on the series class
        
        :param name: Name of the series
        :param index: Index position on the chart of the series
        :param unit: Unit for the series axis
        """
        ...

    @overload
    def __init__(self, name: str, unit: str) -> None:
        """
        Constructor method for Chart Series
        
        :param name: Name of the chart series
        :param unit: Unit of the series
        """
        ...

    @overload
    def add_point(self, time: typing.Union[datetime.datetime, datetime.date], open: float, high: float, low: float, close: float) -> None:
        """
        Add a new point to this series
        
        :param time: Time of the chart point
        :param open: Candlestick open price
        :param high: Candlestick high price
        :param low: Candlestick low price
        :param close: Candlestick close price
        """
        ...

    @overload
    def add_point(self, bar: QuantConnect.Data.Market.TradeBar) -> None:
        """Add a new point to this series"""
        ...

    @overload
    def add_point(self, point: QuantConnect.ISeriesPoint) -> None:
        """
        Add a new point to this series
        
        :param point: The data point to add
        """
        ...

    @overload
    def add_point(self, time: typing.Union[datetime.datetime, datetime.date], values: typing.List[float]) -> None:
        """
        Add a new point to this series
        
        :param time: The time of the data point
        :param values: The values of the data point
        """
        ...

    def clone(self, empty: bool = False) -> QuantConnect.BaseSeries:
        """Return a new instance clone of this object"""
        ...

    def consolidate_chart_points(self) -> QuantConnect.ISeriesPoint:
        """
        Will sum up all candlesticks into a new single one, using the time of latest point
        
        :returns: The new candlestick.
        """
        ...


class Candlestick(System.Object, QuantConnect.ISeriesPoint):
    """Single candlestick for a candlestick chart"""

    @property
    def time(self) -> datetime.datetime:
        """The candlestick time"""
        ...

    @time.setter
    def time(self, value: datetime.datetime) -> None:
        ...

    @property
    def long_time(self) -> int:
        """The candlestick time in seconds since Unix Epoch"""
        ...

    @property
    def open(self) -> typing.Optional[float]:
        """The candlestick open price"""
        ...

    @open.setter
    def open(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def high(self) -> typing.Optional[float]:
        """The candlestick high price"""
        ...

    @high.setter
    def high(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def low(self) -> typing.Optional[float]:
        """The candlestick low price"""
        ...

    @low.setter
    def low(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def close(self) -> typing.Optional[float]:
        """The candlestick close price"""
        ...

    @close.setter
    def close(self, value: typing.Optional[float]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor"""
        ...

    @overload
    def __init__(self, time: int, open: typing.Optional[float], high: typing.Optional[float], low: typing.Optional[float], close: typing.Optional[float]) -> None:
        """
        Constructor taking the candlestick values
        
        :param time: Candlestick time in seconds since Unix Epoch
        :param open: Candlestick open price
        :param high: Candlestick high price
        :param low: Candlestick low price
        :param close: Candlestick close price
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], open: typing.Optional[float], high: typing.Optional[float], low: typing.Optional[float], close: typing.Optional[float]) -> None:
        """
        Constructor taking candlestick values and time in DateTime format
        
        :param time: Candlestick time in seconds
        :param open: Candlestick open price
        :param high: Candlestick high price
        :param low: Candlestick low price
        :param close: Candlestick close price
        """
        ...

    @overload
    def __init__(self, bar: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Constructor taking candlestick values and time in DateTime format
        
        :param bar: Bar which data will be used to create the candlestick
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], bar: QuantConnect.Data.Market.Bar) -> None:
        """
        Constructor taking candlestick values and time in DateTime format
        
        :param time: Candlestick time in seconds
        :param bar: Bar which data will be used to create the candlestick
        """
        ...

    @overload
    def __init__(self, candlestick: QuantConnect.Candlestick) -> None:
        """
        Copy constructor
        
        :param candlestick: Candlestick to copy from
        """
        ...

    def clone(self) -> QuantConnect.ISeriesPoint:
        """
        Clones this instance
        
        :returns: Clone of this instance.
        """
        ...

    def to_string(self) -> str:
        """Provides a readable string representation of this instance."""
        ...

    @overload
    def update(self, value: typing.Optional[float]) -> None:
        """
        Updates the candlestick with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...

    @overload
    def update(self, value: float) -> None:
        """
        Updates the candlestick with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...


class TimeZoneOffsetProvider(System.Object):
    """
    Represents the discontinuties in a single time zone and provides offsets to UTC.
    This type assumes that times will be asked in a forward marching manner.
    This type is not thread safe.
    """

    @property
    def time_zone(self) -> typing.Any:
        """Gets the time zone this instances provides offsets for"""
        ...

    def __init__(self, time_zone: typing.Any, utc_start_time: typing.Union[datetime.datetime, datetime.date], utc_end_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the TimeZoneOffsetProvider class
        
        :param time_zone: The time zone to provide offsets for
        :param utc_start_time: The start of the range of offsets.
        Careful here, it will determine the current discontinuity offset value. When requested to convert a date we only look forward for new discontinuities
        but we suppose the current offset is correct for the requested date if in the past.
        :param utc_end_time: The end of the range of offsets
        """
        ...

    def convert_from_utc(self, utc_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Converts the specified utc_time using the offset resolved from
        a call to get_offset_ticks
        
        :param utc_time: The time to convert from utc
        :returns: The same instant in time represented in the time_zone.
        """
        ...

    def convert_to_utc(self, local_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Converts the specified local time to UTC. This function will advance this offset provider
        
        :param local_time: The local time to be converted to UTC
        :returns: The specified time in UTC.
        """
        ...

    def get_next_discontinuity(self) -> int:
        """
        Gets this offset provider's next discontinuity
        
        :returns: The next discontinuity in UTC ticks.
        """
        ...

    def get_offset_ticks(self, utc_time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Gets the offset in ticks from this time zone to UTC, such that UTC time + offset = local time
        
        :param utc_time: The time in UTC to get an offset to local
        :returns: The offset in ticks between UTC and the local time zone.
        """
        ...


class Parse(System.Object):
    """Provides methods for parsing strings using CultureInfo.InvariantCulture"""

    @staticmethod
    def date_time(value: str) -> datetime.datetime:
        """
        Parses the provided value as a System.DateTime using System.DateTime.Parse(string,IFormatProvider)
        with CultureInfo.InvariantCulture
        """
        ...

    @staticmethod
    @overload
    def date_time_exact(value: str, format: str) -> datetime.datetime:
        """
        Parses the provided value as a System.DateTime using System.DateTime.ParseExact(string,string,IFormatProvider)
        with the specified format and CultureInfo.InvariantCulture
        """
        ...

    @staticmethod
    @overload
    def date_time_exact(value: str, format: str, date_time_styles: System.Globalization.DateTimeStyles) -> datetime.datetime:
        """
        Parses the provided value as a System.DateTime using System.DateTime.ParseExact(string,string,IFormatProvider)
        with the specified format, date_time_styles and CultureInfo.InvariantCulture
        """
        ...

    @staticmethod
    @overload
    def decimal(value: str) -> float:
        """Parses the provided value as a decimal using CultureInfo.InvariantCulture"""
        ...

    @staticmethod
    @overload
    def decimal(value: str, number_styles: System.Globalization.NumberStyles) -> float:
        """
        Parses the provided value as a decimal using the specified number_styles
        and CultureInfo.InvariantCulture
        """
        ...

    @staticmethod
    def double(value: str) -> float:
        """Parses the provided value as a double using CultureInfo.InvariantCulture"""
        ...

    @staticmethod
    def int(value: str) -> int:
        """Parses the provided value as a int using CultureInfo.InvariantCulture"""
        ...

    @staticmethod
    @overload
    def long(value: str) -> int:
        """Parses the provided value as a long using CultureInfo.InvariantCulture"""
        ...

    @staticmethod
    @overload
    def long(value: str, number_styles: System.Globalization.NumberStyles) -> int:
        """
        Parses the provided value as a long using CultureInfo.InvariantCulture
        and the specified number_styles
        """
        ...

    @staticmethod
    def time_span(value: str) -> datetime.timedelta:
        """
        Parses the provided value as a System.TimeSpan using System.TimeSpan.Parse(string,IFormatProvider)
        with CultureInfo.InvariantCulture
        """
        ...

    @staticmethod
    @overload
    def try_parse(input: str, value: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        """Tries to parse the provided value with TryParse as a System.TimeSpan using CultureInfo.InvariantCulture."""
        ...

    @staticmethod
    @overload
    def try_parse(input: str, date_time_style: System.Globalization.DateTimeStyles, value: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        """
        Tries to parse the provided value with TryParse as a System.DateTime using the specified date_time_style
        and CultureInfo.InvariantCulture.
        """
        ...

    @staticmethod
    @overload
    def try_parse(input: str, number_style: System.Globalization.NumberStyles, value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Tries to parse the provided value with TryParse as a double using the specified number_style
        and CultureInfo.InvariantCulture.
        """
        ...

    @staticmethod
    @overload
    def try_parse(input: str, number_style: System.Globalization.NumberStyles, value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to parse the provided value with TryParse as a int using the specified number_style
        and CultureInfo.InvariantCulture.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, time_span_style: System.Globalization.TimeSpanStyles, value: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        """
        Tries to parse the provided value with TryParse as a System.TimeSpan, format
        string, TimeSpanStyles, and using CultureInfo.InvariantCulture
        
        :param input: 
        :param format: 
        :param time_span_style: 
        :param value: 
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, date_time_style: System.Globalization.DateTimeStyles, value: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        """
        Tries to parse the provided value with TryParse as a System.DateTime using the
        specified date_time_style, the format format, and
        CultureInfo.InvariantCulture.
        """
        ...


class OS(System.Object):
    """Operating systems class for managing anything that is operation system specific."""

    IS_LINUX: bool
    """Global Flag :: Operating System"""

    IS_WINDOWS: bool
    """Global Flag :: Operating System"""

    PATH_SEPARATION: str
    """Character Separating directories in this OS:"""

    DRIVE_SPACE_REMAINING: int
    """Get the drive space remaining on windows and linux in MB"""

    DRIVE_SPACE_USED: int
    """Get the drive space remaining on windows and linux in MB"""

    DRIVE_TOTAL_SPACE: int
    """Total space on the drive"""

    APPLICATION_MEMORY_USED: int
    """Gets the amount of private memory allocated for the current process (includes both managed and unmanaged memory)."""

    TOTAL_PHYSICAL_MEMORY_USED: int
    """Get the RAM used on the machine:"""

    CPU_USAGE: float
    """Total CPU usage as a percentage"""

    @staticmethod
    def dispose() -> None:
        """Disposes of the OS internal resources"""
        ...

    @staticmethod
    def get_server_statistics() -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the statistics of the machine, including CPU% and RAM"""
        ...

    @staticmethod
    def initialize() -> None:
        """Initializes the OS internal resources"""
        ...


class SeriesSampler(System.Object):
    """A type capable of taking a chart and resampling using a linear interpolation strategy"""

    @property
    def step(self) -> datetime.timedelta:
        """
        The desired sampling resolution
        
        
        This codeEntityType is protected.
        """
        ...

    @step.setter
    def step(self, value: datetime.timedelta) -> None:
        ...

    @property
    def sub_sample(self) -> bool:
        """True if sub sampling is enabled, if false only subsampling will happen"""
        ...

    @sub_sample.setter
    def sub_sample(self, value: bool) -> None:
        ...

    def __init__(self, resolution: datetime.timedelta) -> None:
        """
        Creates a new SeriesSampler to sample Series data on the specified resolution
        
        :param resolution: The desired sampling resolution
        """
        ...

    @staticmethod
    def interpolate(x_0: float, y_0: typing.Optional[float], x_1: float, y_1: typing.Optional[float], x_target: float, step: float) -> typing.Optional[float]:
        """
        Linear interpolation used for sampling
        
        
        This codeEntityType is protected.
        """
        ...

    def sample(self, series: QuantConnect.BaseSeries, start: typing.Union[datetime.datetime, datetime.date], stop: typing.Union[datetime.datetime, datetime.date], truncate_values: bool = False) -> QuantConnect.BaseSeries:
        """
        Samples the given series
        
        :param series: The series to be sampled
        :param start: The date to start sampling, if before start of data then start of data will be used
        :param stop: The date to stop sampling, if after stop of data, then stop of data will be used
        :param truncate_values: True will truncate values to integers
        :returns: The sampled series.
        """
        ...

    def sample_chart(self, chart: QuantConnect.Chart, start: typing.Union[datetime.datetime, datetime.date], stop: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Chart:
        """
        Samples the given chart
        
        :param chart: The chart to be sampled
        :param start: The date to start sampling
        :param stop: The date to stop sampling
        :returns: The sampled chart.
        """
        ...

    def sample_charts(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], start: typing.Union[datetime.datetime, datetime.date], stop: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.Dictionary[str, QuantConnect.Chart]:
        """
        Samples the given charts
        
        :param charts: The charts to be sampled
        :param start: The date to start sampling
        :param stop: The date to stop sampling
        :returns: The sampled charts.
        """
        ...


class DataUniverseDownloaderGetParameters(QuantConnect.DataDownloaderGetParameters):
    """Represents the parameters required for downloading universe data."""

    @property
    def underlying_symbol(self) -> QuantConnect.Symbol:
        """Gets the underlying symbol associated with the universe."""
        ...

    def __init__(self, canonical_symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], start_date: typing.Union[datetime.datetime, datetime.date], end_date: typing.Union[datetime.datetime, datetime.date], security_exchange_hours: QuantConnect.Securities.SecurityExchangeHours = ...) -> None:
        """
        Initializes a new instance of the DataUniverseDownloaderGetParameters class.
        
        :param canonical_symbol: The canonical symbol for the data request.
        :param start_date: The start date for the data request.
        :param end_date: The end date for the data request.
        :param security_exchange_hours: The security exchange hours for this symbol
        """
        ...

    def create_data_downloader_get_parameters(self) -> typing.Iterable[System.ValueTuple[datetime.datetime, typing.Iterable[QuantConnect.DataDownloaderGetParameters]]]:
        """Creates data download parameters for each day in the range."""
        ...

    def get_universe_file_name(self, processing_date: typing.Union[datetime.datetime, datetime.date]) -> str:
        """
        Gets the file name where the universe data will be saved.
        
        :param processing_date: The date for which the file name is generated.
        :returns: The universe file name.
        """
        ...


class IDataDownloader(metaclass=abc.ABCMeta):
    """Data Downloader Interface for pulling data from a remote source."""

    def get(self, data_downloader_get_parameters: QuantConnect.DataDownloaderGetParameters) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Get historical data enumerable for a single symbol, type and resolution given this start and end time (in UTC).
        
        :param data_downloader_get_parameters: model class for passing in parameters for historical data
        :returns: Enumerable of base data for this symbol.
        """
        ...


class RegressionTestException(System.Exception):
    """Custom exception class for regression tests"""

    @overload
    def __init__(self) -> None:
        """Creates a new instance of a RegressionTestException"""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Creates a new isntance of a RegressionTestException
        
        :param message: Message to be thrown by the exception
        """
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        """
        Creates a new instance of a RegressionTestException
        
        :param message: Message to be thrown by the exception
        :param inner: Inner exception thrown
        """
        ...


class ScatterChartPointJsonConverter:
    """ScatterChartPoint json converter"""

    @property
    def can_write(self) -> bool:
        """Default writer"""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determine if this Converter can convert this type
        
        :param object_type: Type that we would like to convert
        :returns: True if Series.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """Reads series from Json"""
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Writes a Json from series"""
        ...


class SymbolCache(System.Object):
    """
    Provides a string->Symbol mapping to allow for user defined strings to be lifted into a Symbol
    This is mainly used via the Symbol implicit operator, but also functions that create securities
    should also call Set to add new mappings
    """

    @staticmethod
    def clear() -> None:
        """Clears the current caches"""
        ...

    @staticmethod
    def get_symbol(ticker: str) -> QuantConnect.Symbol:
        """
        Gets the Symbol object that is mapped to the specified string ticker symbol
        
        :param ticker: The string ticker symbol
        :returns: The symbol object that maps to the specified string ticker symbol.
        """
        ...

    @staticmethod
    def get_ticker(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """
        Gets the string ticker symbol that is mapped to the specified Symbol
        
        :param symbol: The symbol object
        :returns: The string ticker symbol that maps to the specified symbol object.
        """
        ...

    @staticmethod
    def set(ticker: str, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        """
        Adds a mapping for the specified ticker
        
        :param ticker: The string ticker symbol
        :param symbol: The symbol object that maps to the string ticker symbol
        """
        ...

    @staticmethod
    def try_get_symbol(ticker: str, symbol: typing.Optional[typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]]) -> typing.Tuple[bool, typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]]:
        """
        Gets the Symbol object that is mapped to the specified string ticker symbol
        
        :param ticker: The string ticker symbol
        :param symbol: The output symbol object
        :returns: The symbol object that maps to the specified string ticker symbol.
        """
        ...

    @staticmethod
    def try_get_ticker(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], ticker: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """
        Gets the string ticker symbol that is mapped to the specified Symbol
        
        :param symbol: The symbol object
        :param ticker: The output string ticker symbol
        :returns: The string ticker symbol that maps to the specified symbol object.
        """
        ...

    @staticmethod
    @overload
    def try_remove(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Removes the mapping for the specified symbol from the cache
        
        :param symbol: The symbol whose mappings are to be removed
        :returns: True if the symbol mapping were removed from the cache.
        """
        ...

    @staticmethod
    @overload
    def try_remove(ticker: str) -> bool:
        """
        Removes the mapping for the specified symbol from the cache
        
        :param ticker: The ticker whose mappings are to be removed
        :returns: True if the symbol mapping were removed from the cache.
        """
        ...


class Extensions(System.Object):
    """Extensions function collections - group all static extensions functions here."""

    delisting_market_close_offset_span: datetime.timedelta
    """The offset span from the market close to liquidate or exercise a security on the delisting date"""

    @staticmethod
    def add(dictionary: QuantConnect.Data.Market.Ticks, key: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], tick: QuantConnect.Data.Market.Tick) -> None:
        """
        Adds the specified Tick to the Ticks collection. If an entry does not exist for the specified key then one will be created.
        
        :param dictionary: The ticks dictionary
        :param key: The symbol
        :param tick: The tick to add
        """
        ...

    @staticmethod
    def adjust_symbol_by_offset(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], offset: int) -> QuantConnect.Symbol:
        """
        Helper method that will return a back month, with future expiration, future contract based on the given offset
        
        :param symbol: The none canonical future symbol
        :param offset: The quantity of contracts to move into the future expiration chain
        :returns: A new future expiration symbol instance.
        """
        ...

    @staticmethod
    def batch(result_packets: typing.List[QuantConnect.Packets.AlphaResultPacket]) -> QuantConnect.Packets.AlphaResultPacket:
        """
        Helper method to batch a collection of AlphaResultPacket into 1 single instance.
        Will return null if the provided list is empty. Will keep the last Order instance per order id,
        which is the latest. Implementations trusts the provided 'result_packets' list to batch is in order
        """
        ...

    @staticmethod
    def closes(direction: QuantConnect.Orders.OrderDirection, side: QuantConnect.PositionSide) -> bool:
        """
        Determines if an order with the specified direction would close a position with the
        specified side
        
        :param direction: The direction of the order, buy/sell
        :param side: The side of the position, long/short
        :returns: True if the order direction would close the position, otherwise false.
        """
        ...

    @staticmethod
    def convert_from_utc(time: typing.Union[datetime.datetime, datetime.date], to: typing.Any, strict: bool = False) -> datetime.datetime:
        """
        Converts the specified time from UTC to the to time zone
        
        :param time: The time to be converted expressed in UTC
        :param to: The destinatio time zone
        :param strict: True for strict conversion, this will throw during ambiguitities, false for lenient conversion
        :returns: The time in terms of the to time zone.
        """
        ...

    @staticmethod
    @overload
    def convert_to(time: typing.Union[datetime.datetime, datetime.date], _from: typing.Any, to: typing.Any, strict: bool = False) -> datetime.datetime:
        """
        Converts the specified time from the from time zone to the to time zone
        
        :param time: The time to be converted in terms of the from time zone
        :param _from: The time zone the specified time is in
        :param to: The time zone to be converted to
        :param strict: True for strict conversion, this will throw during ambiguitities, false for lenient conversion
        :returns: The time in terms of the to time zone.
        """
        ...

    @staticmethod
    @overload
    def convert_to(value: str, type: typing.Type) -> System.Object:
        """
        Converts the specified string value into the specified type
        
        :param value: The string value to be converted
        :param type: The output type
        :returns: The converted value.
        """
        ...

    @staticmethod
    def convert_to_symbol_enumerable(py_object: typing.Any) -> typing.Iterable[QuantConnect.Symbol]:
        """
        Gets Enumerable of Symbol from a PyObject
        
        :param py_object: PyObject containing Symbol or Array of Symbol
        :returns: Enumerable of Symbol.
        """
        ...

    @staticmethod
    def convert_to_utc(time: typing.Union[datetime.datetime, datetime.date], _from: typing.Any, strict: bool = False) -> datetime.datetime:
        """
        Converts the specified time from the from time zone to TimeZones.UTC
        
        :param time: The time to be converted in terms of the from time zone
        :param _from: The time zone the specified time is in
        :param strict: True for strict conversion, this will throw during ambiguitities, false for lenient conversion
        :returns: The time in terms of the to time zone.
        """
        ...

    @staticmethod
    @overload
    def create_future_chain(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], filter: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates a FuturesChainUniverse for a given symbol
        
        :param algorithm: The algorithm instance to create universes for
        :param symbol: Symbol of the future
        :param filter: The future filter to use
        :param universe_settings: The universe settings, will use algorithm settings if null
        """
        ...

    @staticmethod
    @overload
    def create_future_chain(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], filter: typing.Callable[[QuantConnect.Securities.FutureFilterUniverse], QuantConnect.Securities.FutureFilterUniverse], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> typing.Iterable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates a FuturesChainUniverse for a given symbol
        
        :param algorithm: The algorithm instance to create universes for
        :param symbol: Symbol of the future
        :param filter: The future filter to use
        :param universe_settings: The universe settings, will use algorithm settings if null
        """
        ...

    @staticmethod
    @overload
    def create_option_chain(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], filter: typing.Any, universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.OptionChainUniverse:
        """
        Creates a OptionChainUniverse for a given symbol
        
        :param algorithm: The algorithm instance to create universes for
        :param symbol: Symbol of the option
        :param filter: The option filter to use
        :param universe_settings: The universe settings, will use algorithm settings if null
        :returns: OptionChainUniverse for the given symbol.
        """
        ...

    @staticmethod
    @overload
    def create_option_chain(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], filter: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse], universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> QuantConnect.Data.UniverseSelection.OptionChainUniverse:
        """
        Creates a OptionChainUniverse for a given symbol
        
        :param algorithm: The algorithm instance to create universes for
        :param symbol: Symbol of the option
        :param filter: The option filter to use
        :param universe_settings: The universe settings, will use algorithm settings if null
        :returns: OptionChainUniverse for the given symbol.
        """
        ...

    @staticmethod
    def create_type(py_object: typing.Any) -> typing.Type:
        """
        Creates a type with a given name, if PyObject is not a CLR type. Otherwise, convert it.
        
        :param py_object: Python object representing a type.
        :returns: Type object.
        """
        ...

    @staticmethod
    def decode_base_36(symbol: str) -> int:
        """Converts an upper case alpha numeric string into a long"""
        ...

    @staticmethod
    def decode_base_64(base_64_encoded_text: str) -> str:
        """
        Decode a Base64 Encoded string
        
        :param base_64_encoded_text: Text to decode
        :returns: Decoded result.
        """
        ...

    @staticmethod
    def default_option_style(security_type: QuantConnect.SecurityType) -> QuantConnect.OptionStyle:
        """
        Gets the default OptionStyle for the provided SecurityType
        
        :param security_type: SecurityType to get default OptionStyle for
        :returns: Default OptionStyle for the SecurityType.
        """
        ...

    @staticmethod
    def deserialize_list(json_array: str) -> typing.List[str]:
        """
        Helper method to deserialize a json array into a list also handling single json values
        
        :param json_array: The value to deserialize
        """
        ...

    @staticmethod
    def discretely_round_by(value: float, quanta: float, mode: System.MidpointRounding = ...) -> float:
        """
        Discretizes the value to a maximum precision specified by quanta. Quanta
        can be an arbitrary positive number and represents the step size. Consider a quanta equal to 0.15 and rounding
        a value of 1.0. Valid values would be 0.9 (6 quanta) and 1.05 (7 quanta) which would be rounded up to 1.05.
        
        :param value: The value to be rounded by discretization
        :param quanta: The maximum precision allowed by the value
        :param mode: Specifies how to handle the rounding of half value, defaulting to away from zero.
        """
        ...

    @staticmethod
    def download_byte_array(url: str) -> typing.List[int]:
        """
        Helper method to download a provided url as a byte array
        
        :param url: The url to download data from
        """
        ...

    @staticmethod
    @overload
    def download_data(client: typing.Any, url: str, headers: System.Collections.Generic.Dictionary[str, str] = None) -> str:
        """
        Helper method to download a provided url as a string
        
        :param client: The http client to use
        :param url: The url to download data from
        :param headers: Add custom headers for the request
        """
        ...

    @staticmethod
    @overload
    def download_data(url: str, headers: System.Collections.Generic.Dictionary[str, str] = None) -> str:
        """
        Helper method to download a provided url as a string
        
        :param url: The url to download data from
        :param headers: Add custom headers for the request
        """
        ...

    @staticmethod
    def encode_base_36(data: int) -> str:
        """Converts a long to an uppercase alpha numeric string"""
        ...

    @staticmethod
    def encode_base_64(text: str) -> str:
        """
        Convert a string to Base64 Encoding
        
        :param text: Text to encode
        :returns: Encoded result.
        """
        ...

    @staticmethod
    def exchange_round_down(date_time: typing.Union[datetime.datetime, datetime.date], interval: datetime.timedelta, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, extended_market_hours: bool) -> datetime.datetime:
        """
        Extension method to round a datetime down by a timespan interval until it's
        within the specified exchange's open hours. This works by first rounding down
        the specified time using the interval, then producing a bar between that
        rounded time and the interval plus the rounded time and incrementally walking
        backwards until the exchange is open
        
        :param date_time: Time to be rounded down
        :param interval: Timespan interval to round to.
        :param exchange_hours: The exchange hours to determine open times
        :param extended_market_hours: True for extended market hours, otherwise false
        :returns: Rounded datetime.
        """
        ...

    @staticmethod
    def exchange_round_down_in_time_zone(date_time: typing.Union[datetime.datetime, datetime.date], interval: datetime.timedelta, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, rounding_time_zone: typing.Any, extended_market_hours: bool) -> datetime.datetime:
        """
        Extension method to round a datetime down by a timespan interval until it's
        within the specified exchange's open hours. The rounding is performed in the
        specified time zone
        
        :param date_time: Time to be rounded down
        :param interval: Timespan interval to round to.
        :param exchange_hours: The exchange hours to determine open times
        :param rounding_time_zone: The time zone to perform the rounding in
        :param extended_market_hours: True for extended market hours, otherwise false
        :returns: Rounded datetime.
        """
        ...

    @staticmethod
    def get_assembly_name(py_object: typing.Any) -> System.Reflection.AssemblyName:
        """
        Helper method to get the assembly name from a python type
        
        :param py_object: Python object pointing to the python type. PyObject.GetPythonType
        :returns: The python type assembly name.
        """
        ...

    @staticmethod
    def get_base_data_instance(type: typing.Type) -> QuantConnect.Data.BaseData:
        """
        Given a type will create a new instance using the parameterless constructor
        and assert the type implements BaseData
        """
        ...

    @staticmethod
    def get_better_type_name(type: typing.Type) -> str:
        """
        Gets a type's name with the generic parameters filled in the way they would look when
        defined in code, such as converting Dictionary<`1,`2> to Dictionary<string,int>
        
        :param type: The type who's name we seek
        :returns: A better type name.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(str: str) -> typing.List[int]:
        """
        Extension method to convert a string into a byte array
        
        :param str: String to convert to bytes.
        :returns: Byte array.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(stream: System.IO.Stream) -> typing.List[int]:
        """
        Reads the entire content of a stream and returns it as a byte array.
        
        :param stream: Stream to read bytes from
        :returns: The bytes read from the stream.
        """
        ...

    @staticmethod
    def get_custom_data_type_from_symbols(symbols: typing.List[QuantConnect.Symbol]) -> typing.Type:
        """
        Retrieve a common custom data types from the given symbols if any
        
        :param symbols: The target symbols to search
        :returns: The custom data type or null.
        """
        ...

    @staticmethod
    def get_decimal_epsilon() -> float:
        """
        Gets the smallest positive number that can be added to a decimal instance and return
        a new value that does not == the old value
        """
        ...

    @staticmethod
    def get_decimal_from_csv(csv_line: str, index: int) -> float:
        """
        Gets the value at the specified index from a CSV line, converted into a decimal.
        
        :param csv_line: The CSV line
        :param index: The index of the value to be extracted from the CSV line
        :returns: The decimal value at the given index. If the index is invalid or conversion fails, it will return zero.
        """
        ...

    @staticmethod
    def get_decimal_places(input: float) -> int:
        """
        Helper method to determine the amount of decimal places associated with the given decimal
        
        :param input: The value to get the decimal count from
        :returns: The quantity of decimal places.
        """
        ...

    @staticmethod
    def get_delisting_date(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], map_file: QuantConnect.Data.Auxiliary.MapFile = None) -> datetime.datetime:
        """
        Gets the delisting date for the provided Symbol
        
        :param symbol: The symbol to lookup the last trading date
        :param map_file: Map file to use for delisting date. Defaults to SID.DefaultDate if no value is passed and is equity.
        """
        ...

    @staticmethod
    def get_entry(market_hours_database: QuantConnect.Securities.MarketHoursDatabase, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], data_types: typing.List[typing.Type]) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
        """
        Helper method to get a market hours entry
        
        :param market_hours_database: The market hours data base instance
        :param symbol: The symbol to get the entry for
        :param data_types: For custom data types can optionally provide data type so that a new entry is added
        """
        ...

    @staticmethod
    @overload
    def get_enum_string(value: int, py_object: typing.Any) -> str:
        """
        Converts the numeric value of one or more enumerated constants to an equivalent enumerated string.
        
        
        Deprecated as of 2025-07. Please use `str()`.
        
        :param value: Numeric value
        :param py_object: Python object that encapsulated a Enum Type
        :returns: String that represents the enumerated object.
        """
        ...

    @staticmethod
    @overload
    def get_enum_string(value: System.Enum, py_object: typing.Any) -> str:
        """
        Converts the numeric value of one or more enumerated constants to an equivalent enumerated string.
        
        
        Deprecated as of 2025-07. Please use `str()`.
        
        :param value: Numeric value
        :param py_object: Python object that encapsulated a Enum Type
        :returns: String that represents the enumerated object.
        """
        ...

    @staticmethod
    def get_exercise_direction(right: QuantConnect.OptionRight, is_short: bool) -> QuantConnect.Orders.OrderDirection:
        """
        Gets the option exercise order direction resulting from the specified right and
        whether or not we wrote the option (is_short is true) or bought to
        option (is_short is false)
        
        :param right: The option right
        :param is_short: True if we wrote the option, false if we purchased the option
        :returns: The order direction resulting from an exercised option.
        """
        ...

    @staticmethod
    def get_extension(str: str) -> str:
        """
        Extension method to extract the extension part of this file name if it matches a safe list, or return a ".custom" extension for ones which do not match.
        
        :param str: String we're looking for the extension for.
        :returns: Last 4 character string of string.
        """
        ...

    @staticmethod
    def get_hash(orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]) -> str:
        """
        Generates a hash code from a given collection of orders
        
        :param orders: The order collection
        :returns: The hash value.
        """
        ...

    @staticmethod
    def get_market_order_fees(security: QuantConnect.Securities.Security, quantity: float, time: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Securities.CashAmount:
        """
        Returns the amount of fee's charged by executing a market order with the given arguments
        
        :param security: Security for which we would like to make a market order
        :param quantity: Quantity of the security we are seeking to trade
        :param time: Time the order was placed
        """
        ...

    @staticmethod
    def get_md_5_hash(stream: System.IO.Stream) -> typing.List[int]:
        """
        Gets the MD5 hash from a stream
        
        :param stream: The stream to compute a hash for
        :returns: The MD5 hash.
        """
        ...

    @staticmethod
    def get_memory_stream(guid: System.Guid) -> System.IO.MemoryStream:
        """
        Will return a memory stream using the RecyclableMemoryStreamManager instance.
        
        :param guid: Unique guid
        :returns: A memory stream.
        """
        ...

    @staticmethod
    def get_method(instance: typing.Any, name: str) -> typing.Any:
        """
        Gets a method from a PyObject instance by name.
        First, it tries to get the snake-case version of the method name, in case the user is using that style.
        Else, it tries to get the method with the original name, regardless of whether the class has a Python overload or not.
        
        :param instance: The object instance to search the method in
        :param name: The name of the method
        :returns: The method matching the name.
        """
        ...

    @staticmethod
    def get_or_add_unrequested_security(algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], security: typing.Optional[QuantConnect.Securities.Security], on_error: typing.Callable[[typing.Sequence[QuantConnect.SecurityType]], typing.Any] = None) -> typing.Tuple[bool, QuantConnect.Securities.Security]:
        """
        Gets the security for the specified symbol from the algorithm's securities collection.
        In case the security is not found, it will be created using the IAlgorithm.universe_settings
        and a best effort configuration setup.
        
        :param algorithm: The algorithm instance
        :param symbol: The symbol which security is being looked up
        :param security: The found or added security instance
        :param on_error: Callback to invoke in case of unsupported security type
        :returns: True if the security was found or added.
        """
        ...

    @staticmethod
    def get_order_direction(quantity: float) -> QuantConnect.Orders.OrderDirection:
        """Gets the OrderDirection for the specified quantity"""
        ...

    @staticmethod
    def get_python_arg_count(method: typing.Any) -> int:
        """
        Get a python methods arg count
        
        :param method: The Python method
        :returns: Count of arguments.
        """
        ...

    @staticmethod
    def get_python_bool_property(instance: typing.Any, name: str) -> typing.Any:
        """
        Gets a python property by name
        
        :param instance: The object instance to search the property in
        :param name: The name of the property
        :returns: The python property or null if not defined or CSharp implemented.
        """
        ...

    @staticmethod
    def get_python_bool_property_with_checks(instance: typing.Any, name: str) -> typing.Any:
        """
        Gets a python property by name
        
        :param instance: The object instance to search the property in
        :param name: The name of the method
        :returns: The python property or null if not defined or CSharp implemented.
        """
        ...

    @staticmethod
    def get_python_method(instance: typing.Any, name: str) -> typing.Any:
        """
        Gets a python method by name
        
        :param instance: The object instance to search the method in
        :param name: The name of the method
        :returns: The python method or null if not defined or CSharp implemented.
        """
        ...

    @staticmethod
    def get_python_method_with_checks(instance: typing.Any, name: str) -> typing.Any:
        """
        Gets a python method by name
        
        :param instance: The object instance to search the method in
        :param name: The name of the method
        :returns: The python method or null if not defined or CSharp implemented.
        """
        ...

    @staticmethod
    def get_string(bytes: typing.List[int], encoding: System.Text.Encoding = None) -> str:
        """
        Extension method to convert a byte array into a string.
        
        :param bytes: Byte array to convert.
        :param encoding: The encoding to use for the conversion. Defaults to Encoding.ASCII
        :returns: String from bytes.
        """
        ...

    @staticmethod
    def get_string_between_chars(value: str, left: str, right: str) -> str:
        """
        Get the first occurence of a string between two characters from another string
        
        :param value: The original string
        :param left: Left bound of the substring
        :param right: Right bound of the substring
        :returns: Substring from original string bounded by the two characters.
        """
        ...

    @staticmethod
    def get_universe_mapping_mode_or_default(universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, security_type: QuantConnect.SecurityType, market: str) -> QuantConnect.DataMappingMode:
        """Helper method to determine the right data mapping mode to use by default"""
        ...

    @staticmethod
    def get_universe_normalization_mode_or_default(universe_settings: QuantConnect.Data.UniverseSelection.UniverseSettings, security_type: QuantConnect.SecurityType) -> QuantConnect.DataNormalizationMode:
        """Helper method to determine the right data normalization mode to use by default"""
        ...

    @staticmethod
    def get_update_price_scale_frontier(data: QuantConnect.Data.BaseData) -> datetime.datetime:
        """Helper method to determine if price scales need an update based on the given data point"""
        ...

    @staticmethod
    def get_zero_price_message(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
        """Extension method to get security price is 0 messages for users"""
        ...

    @staticmethod
    @overload
    def greatest_common_divisor(values: typing.List[float]) -> float:
        """
        Gets the greatest common divisor of a list of numbers
        
        :param values: List of numbers which greatest common divisor is requested
        :returns: The greatest common divisor for the given list of numbers.
        """
        ...

    @staticmethod
    @overload
    def greatest_common_divisor(values: typing.List[int]) -> int:
        """
        Gets the greatest common divisor of a list of numbers
        
        :param values: List of numbers which greatest common divisor is requested
        :returns: The greatest common divisor for the given list of numbers.
        """
        ...

    @staticmethod
    def has_options(security_type: QuantConnect.SecurityType) -> bool:
        """
        Determines if the provided SecurityType has a matching option SecurityType, used to represent
        the current SecurityType as a derivative.
        
        :param security_type: The SecurityType to check if it has options available
        :returns: true if there are options for the SecurityType, false otherwise.
        """
        ...

    @staticmethod
    def implements_stream_reader(base_data_type: typing.Type) -> bool:
        """Helper method to determine if a data type implements the Stream reader method"""
        ...

    @staticmethod
    def in_the_money_amount(option: QuantConnect.Securities.Option.Option, quantity: float) -> QuantConnect.Securities.ConvertibleCashAmount:
        """
        Gets the option's ITM amount for the given quantity.
        
        :param option: The option security
        :param quantity: The quantity
        :returns: The ITM amount for the absolute quantity.
        """
        ...

    @staticmethod
    def invert(right: QuantConnect.OptionRight) -> QuantConnect.OptionRight:
        """Inverts the specified right"""
        ...

    @staticmethod
    def is_common_business_day(date: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Business day here is defined as any day of the week that is not saturday or sunday
        
        :param date: The date to be examined
        :returns: A bool indicating wether the datetime is a weekday or not.
        """
        ...

    @staticmethod
    def is_custom_data_type(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], type: typing.Type) -> bool:
        """
        Determines if certain data type is custom
        
        :param symbol: Symbol associated with the data type
        :param type: Data type to determine if it's custom
        """
        ...

    @staticmethod
    def is_directory_empty(directory_path: str) -> bool:
        """
        Helper method to check if a directory exists and is not empty
        
        :param directory_path: The path to check
        :returns: True if the directory does not exist or is empty.
        """
        ...

    @staticmethod
    @overload
    def is_empty(series: QuantConnect.BaseSeries) -> bool:
        """Returns true if the specified BaseSeries instance holds no ISeriesPoint"""
        ...

    @staticmethod
    @overload
    def is_empty(chart: QuantConnect.Chart) -> bool:
        """
        Returns if the specified Chart instance holds no Series
        or they are all empty Extensions.is_empty(BaseSeries)
        """
        ...

    @staticmethod
    @overload
    def is_market_open(security: QuantConnect.Securities.Security, extended_market_hours: bool) -> bool:
        """
        Helper method to determine if a specific market is open
        
        :param security: The target security
        :param extended_market_hours: True if should consider extended market hours
        :returns: True if the market is open.
        """
        ...

    @staticmethod
    @overload
    def is_market_open(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], utc_time: typing.Union[datetime.datetime, datetime.date], extended_market_hours: bool) -> bool:
        """
        Helper method to determine if a specific market is open
        
        :param symbol: The target symbol
        :param utc_time: The current UTC time
        :param extended_market_hours: True if should consider extended market hours
        :returns: True if the market is open.
        """
        ...

    @staticmethod
    def is_na_n_or_infinity(value: float) -> bool:
        """
        Check if a number is NaN or infinity
        
        :param value: The double value to check
        """
        ...

    @staticmethod
    def is_na_n_or_zero(value: float) -> bool:
        """
        Check if a number is NaN or equal to zero
        
        :param value: The double value to check
        """
        ...

    @staticmethod
    def is_option(security_type: QuantConnect.SecurityType) -> bool:
        """
        Determines if the provided SecurityType is a type of Option.
        Valid option types are: Equity Options, Futures Options, and Index Options.
        
        :param security_type: The SecurityType to check if it's an option asset
        :returns: true if the asset has the makings of an option (exercisable, expires, and is a derivative of some underlying),
        false otherwise.
        """
        ...

    @staticmethod
    def is_out_of_date(filepath: str) -> bool:
        """
        Determine if the file is out of date according to our download period.
        Date based files are never out of date (Files with YYYYMMDD)
        
        :param filepath: Path to the file
        :returns: True if the file is out of date.
        """
        ...

    @staticmethod
    def is_subclass_of_generic(type: typing.Type, possible_super_type: typing.Type) -> bool:
        """
        Checks the specified type to see if it is a subclass of the possible_super_type. This method will
        crawl up the inheritance heirarchy to check for equality using generic type definitions (if exists)
        
        :param type: The type to be checked as a subclass of possible_super_type
        :param possible_super_type: The possible superclass of type
        :returns: True if type is a subclass of the generic type definition possible_super_type.
        """
        ...

    @staticmethod
    def is_valid(security_type: QuantConnect.SecurityType) -> bool:
        """
        Asserts the specified security_type value is valid
        
        :param security_type: The SecurityType value
        :returns: True if valid security type value.
        """
        ...

    @staticmethod
    def is_win(fill: QuantConnect.Orders.OrderEvent, security: QuantConnect.Securities.Security, profit_loss: float) -> bool:
        """
        Checks whether the fill event for closing a trade is a winning trade
        
        :param fill: The fill event
        :param security: The security being traded
        :param profit_loss: The profit-loss for the closed trade
        :returns: Whether the trade is a win.
        For options assignments this depends on whether the option is ITM or OTM and the position side.
        See Trade.is_win for more information.
        """
        ...

    @staticmethod
    def lazy_to_lower(data: str) -> str:
        """
        Lazy string to lower implementation.
        Will first verify the string is not already lower and avoid
        the call to string.ToLowerInvariant() if possible.
        
        :param data: The string to lower
        :returns: The lower string.
        """
        ...

    @staticmethod
    def lazy_to_upper(data: str) -> str:
        """
        Lazy string to upper implementation.
        Will first verify the string is not already upper and avoid
        the call to string.ToUpperInvariant() if possible.
        
        :param data: The string to upper
        :returns: The upper string.
        """
        ...

    @staticmethod
    def make_tradable(security: QuantConnect.Securities.Security) -> None:
        """
        Helper method to set the Security.is_tradable property to true
        for the given security when possible
        """
        ...

    @staticmethod
    def matches_type_name(type: typing.Type, type_name: str) -> bool:
        """
        Function used to match a type against a string type name. This function compares on the AssemblyQualfiedName,
        the FullName, and then just the Name of the type.
        
        :param type: The type to test for a match
        :param type_name: The name of the type to match
        :returns: True if the specified type matches the type name, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def normalize(input: float) -> float:
        """
        Will remove any trailing zeros for the provided decimal input
        
        :param input: The decimal to remove trailing zeros from
        :returns: Provided input with no trailing zeros.
        """
        ...

    @staticmethod
    @overload
    def normalize(data: QuantConnect.Data.BaseData, factor: float, normalization_mode: QuantConnect.DataNormalizationMode, sum_of_dividends: float) -> QuantConnect.Data.BaseData:
        """
        Normalize prices based on configuration
        
        :param data: Data to be normalized
        :param factor: Price scale
        :param normalization_mode: The price scaling normalization mode
        :param sum_of_dividends: The current dividend sum
        :returns: The provided data point adjusted.
        """
        ...

    @staticmethod
    def normalize_to_str(input: float) -> str:
        """
        Will remove any trailing zeros for the provided decimal and convert to string.
        Uses normalize(decimal).
        
        :param input: The decimal to convert to string
        :returns: Input converted to string with no trailing zeros.
        """
        ...

    @staticmethod
    def option_right_to_lower(option_right: QuantConnect.OptionRight) -> str:
        """
        Converts the specified option_right value to its corresponding lower-case string representation
        
        :param option_right: The option_right value
        :returns: A lower case string representation of the specified OptionRight value.
        """
        ...

    @staticmethod
    def option_style_to_lower(option_style: QuantConnect.OptionStyle) -> str:
        """
        Converts the specified option_style value to its corresponding lower-case string representation
        
        :param option_style: The option_style value
        :returns: A lower case string representation of the specified option_style value.
        """
        ...

    @staticmethod
    def order_targets_by_margin_impact(targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget], algorithm: QuantConnect.Interfaces.IAlgorithm, target_is_delta: bool = False) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Returns an ordered enumerable where position reducing orders are executed first
        and the remaining orders are executed in decreasing order value.
        Will NOT return targets during algorithm warmup.
        Will NOT return targets for securities that have no data yet.
        Will NOT return targets for which current holdings + open orders quantity, sum up to the target quantity
        
        :param targets: The portfolio targets to order by margin
        :param algorithm: The algorithm instance
        :param target_is_delta: True if the target quantity is the delta between the
        desired and existing quantity
        """
        ...

    @staticmethod
    def parse_data_mapping_mode(data_mapping_mode: str) -> typing.Optional[QuantConnect.DataMappingMode]:
        """
        Converts the specified string to its corresponding DataMappingMode
        
        :param data_mapping_mode: The data_mapping_mode string value
        :returns: The DataMappingMode value.
        """
        ...

    @staticmethod
    def parse_option_right(option_right: str) -> QuantConnect.OptionRight:
        """
        Converts the specified string to its corresponding OptionRight
        
        :param option_right: The option_right string value
        :returns: The OptionRight value.
        """
        ...

    @staticmethod
    def parse_option_style(option_style: str) -> QuantConnect.OptionStyle:
        """
        Converts the specified string to its corresponding OptionStyle
        
        :param option_style: The OptionStyle string value
        :returns: The OptionStyle value.
        """
        ...

    @staticmethod
    def process_security_changes(algorithm: QuantConnect.Interfaces.IAlgorithm, security_changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Helper method to process an algorithms security changes, will add and remove securities according to them"""
        ...

    @staticmethod
    @overload
    def protobuf_serialize(ticks: typing.List[QuantConnect.Data.Market.Tick], guid: System.Guid) -> typing.List[int]:
        """
        Serialize a list of ticks using protobuf
        
        :param ticks: The list of ticks to serialize
        :param guid: Unique guid
        :returns: The resulting byte array.
        """
        ...

    @staticmethod
    @overload
    def protobuf_serialize(base_data: QuantConnect.Data.IBaseData, guid: System.Guid) -> typing.List[int]:
        """
        Serialize a base data instance using protobuf
        
        :param base_data: The data point to serialize
        :param guid: Unique guid
        :returns: The resulting byte array.
        """
        ...

    @staticmethod
    @overload
    def protobuf_serialize(base_data: QuantConnect.Data.IBaseData, stream: System.IO.Stream) -> None:
        """
        Serialize a base data instance using protobuf
        
        :param base_data: The data point to serialize
        :param stream: The destination stream
        """
        ...

    @staticmethod
    def read_lines(data_provider: QuantConnect.Interfaces.IDataProvider, file: str) -> typing.Iterable[str]:
        """
        Helper method to stream read lines from a file
        
        :param data_provider: The data provider to use
        :param file: The file path to read from
        :returns: Enumeration of lines in file.
        """
        ...

    @staticmethod
    def remove_from_end(s: str, ending: str) -> str:
        """
        Returns a new string in which specified ending in the current instance is removed.
        
        :param s: original string value
        :param ending: the string to be removed
        """
        ...

    @staticmethod
    def remove_from_start(s: str, start: str) -> str:
        """
        Returns a new string in which specified start in the current instance is removed.
        
        :param s: original string value
        :param start: the string to be removed
        :returns: Substring with start removed.
        """
        ...

    @staticmethod
    def requires_mapping(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> bool:
        """
        Determine if this SecurityType requires mapping
        
        :param symbol: Type to check
        :returns: True if it needs to be mapped.
        """
        ...

    @staticmethod
    def reset(timer: System.Timers.Timer) -> None:
        """
        Add the reset method to the System.Timer class.
        
        :param timer: System.timer object
        """
        ...

    @staticmethod
    def resolution_to_lower(resolution: QuantConnect.Resolution) -> str:
        """
        Converts the specified resolution value to its corresponding lower-case string representation
        
        :param resolution: The resolution value
        :returns: A lower-case string representation of the specified resolution value.
        """
        ...

    @staticmethod
    @overload
    def round(time: datetime.timedelta, rounding_interval: datetime.timedelta, rounding_type: System.MidpointRounding) -> datetime.timedelta:
        """
        Extension method to round a timeSpan to nearest timespan period.
        
        :param time: TimeSpan To Round
        :param rounding_interval: Rounding Unit
        :param rounding_type: Rounding method
        :returns: Rounded timespan.
        """
        ...

    @staticmethod
    @overload
    def round(time: datetime.timedelta, rounding_interval: datetime.timedelta) -> datetime.timedelta:
        """
        Extension method to round timespan to nearest timespan period.
        
        :param time: Base timespan we're looking to round.
        :param rounding_interval: Timespan period we're rounding.
        :returns: Rounded timespan period.
        """
        ...

    @staticmethod
    @overload
    def round(datetime: typing.Union[datetime.datetime, datetime.date], rounding_interval: datetime.timedelta) -> datetime.datetime:
        """
        Extension method to round a datetime to the nearest unit timespan.
        
        :param datetime: Datetime object we're rounding.
        :param rounding_interval: Timespan rounding period.
        :returns: Rounded datetime.
        """
        ...

    @staticmethod
    def round_down(date_time: typing.Union[datetime.datetime, datetime.date], interval: datetime.timedelta) -> datetime.datetime:
        """
        Extension method to round a datetime down by a timespan interval.
        
        :param date_time: Base DateTime object we're rounding down.
        :param interval: Timespan interval to round to
        :returns: Rounded datetime.
        """
        ...

    @staticmethod
    def round_down_in_time_zone(date_time: typing.Union[datetime.datetime, datetime.date], rounding_interval: datetime.timedelta, source_time_zone: typing.Any, rounding_time_zone: typing.Any) -> datetime.datetime:
        """
        Rounds the specified date time in the specified time zone. Careful with calling this method in a loop while modifying date_time, check unit tests.
        
        :param date_time: Date time to be rounded
        :param rounding_interval: Timespan rounding period
        :param source_time_zone: Time zone of the date time
        :param rounding_time_zone: Time zone in which the rounding is performed
        :returns: The rounded date time in the source time zone.
        """
        ...

    @staticmethod
    def round_to_significant_digits(d: float, digits: int) -> float:
        """
        Extension method to round a double value to a fixed number of significant figures instead of a fixed decimal places.
        
        :param d: Double we're rounding
        :param digits: Number of significant figures
        :returns: New double rounded to digits-significant figures.
        """
        ...

    @staticmethod
    def round_up(time: typing.Union[datetime.datetime, datetime.date], interval: datetime.timedelta) -> datetime.datetime:
        """
        Extension method to explicitly round up to the nearest timespan interval.
        
        :param time: Base datetime object to round up.
        :param interval: Timespan interval to round to
        :returns: Rounded datetime.
        """
        ...

    @staticmethod
    def safe_as_managed_object(py_object: typing.Any, type_to_convert_to: typing.Type = None) -> typing.Any:
        """
        Safely convert PyObject to ManagedObject using Py.GIL Lock
        If no type is given it will convert the PyObject's Python Type to a ManagedObject Type
        in a attempt to resolve the target type to convert to.
        
        :param py_object: PyObject to convert to managed
        :param type_to_convert_to: The target type to convert to
        :returns: The resulting ManagedObject.
        """
        ...

    @staticmethod
    def safe_decimal_cast(input: float) -> float:
        """
        Casts the specified input value to a decimal while acknowledging the overflow conditions
        
        :param input: The value to be cast
        :returns: The input value as a decimal, if the value is too large or to small to be represented
        as a decimal, then the closest decimal value will be returned.
        """
        ...

    @staticmethod
    def safe_division(numerator: float, denominator: float, fail_value: float = 0) -> float:
        """
        Safe method to perform divisions avoiding DivideByZeroException and Overflow/Underflow exceptions
        
        :param fail_value: Value to be returned if the denominator is zero
        :returns: The numerator divided by the denominator if the denominator is not
        zero. Otherwise, the default fail_value or the provided one.
        """
        ...

    @staticmethod
    def safe_multiply_100(value: float) -> float:
        """
        Safe multiplies a decimal by 100
        
        :param value: The decimal to multiply
        :returns: The result, maxed out at decimal.MaxValue.
        """
        ...

    @staticmethod
    def scale(data: QuantConnect.Data.BaseData, factor_func: typing.Callable[[float, float, float], float], volume_factor: float, factor: float, sum_of_dividends: float) -> QuantConnect.Data.BaseData:
        """
        Scale data based on factor function
        
        :param data: Data to Adjust
        :param factor_func: Function to factor prices by
        :param volume_factor: Factor to multiply volume/askSize/bidSize/quantity by
        :param factor: Price scale
        :param sum_of_dividends: The current dividend sum
        """
        ...

    @staticmethod
    def security_type_to_lower(security_type: QuantConnect.SecurityType) -> str:
        """
        Converts the specified security_type value to its corresponding lower-case string representation
        
        :param security_type: The SecurityType value
        :returns: A lower-case string representation of the specified SecurityType value.
        """
        ...

    @staticmethod
    def set_runtime_error(algorithm: QuantConnect.Interfaces.IAlgorithm, exception: System.Exception, context: str) -> None:
        """Helper method to set an algorithm runtime exception in a normalized fashion"""
        ...

    @staticmethod
    def should_emit_data(config: QuantConnect.Data.SubscriptionDataConfig, data: QuantConnect.Data.BaseData, is_universe: bool = False) -> bool:
        """
        Centralized logic used at the top of the subscription enumerator stacks to determine if we should emit base data points
        based on the configuration for this subscription and the type of data we are handling.
        
        Currently we only want to emit split/dividends/delisting events for non internal TradeBar configurations
        this last part is because equities also have QuoteBar subscriptions which will also subscribe to the
        same aux events and we don't want duplicate emits of these events in the TimeSliceFactory
        """
        ...

    @staticmethod
    def single_or_algorithm_type_name(names: typing.List[str], algorithm_type_name: str) -> str:
        """
        Return the first in the series of names, or find the one that matches the configured algorithm_type_name
        
        :param names: The list of class names
        :param algorithm_type_name: The configured algorithm type name from the config
        :returns: The name of the class being run.
        """
        ...

    @staticmethod
    @overload
    def smart_rounding(input: typing.Optional[float]) -> typing.Optional[float]:
        """
        Provides global smart rounding, numbers larger than 1000 will round to 4 decimal places,
        while numbers smaller will round to 7 significant digits
        """
        ...

    @staticmethod
    @overload
    def smart_rounding(input: float) -> float:
        """
        Provides global smart rounding, numbers larger than 1000 will round to 4 decimal places,
        while numbers smaller will round to 7 significant digits
        """
        ...

    @staticmethod
    def smart_rounding_short(input: float) -> float:
        """Provides global smart rounding to a shorter version"""
        ...

    @staticmethod
    def stop_safely(thread: System.Threading.Thread, timeout: datetime.timedelta, token: System.Threading.CancellationTokenSource = None) -> None:
        """
        Helper method to safely stop a running thread
        
        :param thread: The thread to stop
        :param timeout: The timeout to wait till the thread ends after which abort will be called
        :param token: Cancellation token source to use if any
        """
        ...

    @staticmethod
    def subscribe_with_mapping(data_queue_handler: QuantConnect.Interfaces.IDataQueueHandler, data_config: QuantConnect.Data.SubscriptionDataConfig, new_data_available_handler: typing.Callable[[System.Object, System.EventArgs], typing.Any], is_expired: typing.Callable[[QuantConnect.Data.SubscriptionDataConfig], bool], subscribed_config: typing.Optional[QuantConnect.Data.SubscriptionDataConfig]) -> typing.Tuple[System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], QuantConnect.Data.SubscriptionDataConfig]:
        """Helper method to subscribe a given configuration, handling any required mapping"""
        ...

    @staticmethod
    @overload
    def synchronously_await_task(task: System.Threading.Tasks.Task) -> None:
        """
        Safely blocks until the specified task has completed executing
        
        :param task: The task to be awaited
        :returns: The result of the task.
        """
        ...

    @staticmethod
    @overload
    def synchronously_await_task(task: System.Threading.Tasks.ValueTask) -> None:
        """
        Safely blocks until the specified task has completed executing
        
        :param task: The task to be awaited
        :returns: The result of the task.
        """
        ...

    @staticmethod
    def tick_type_to_lower(tick_type: QuantConnect.TickType) -> str:
        """
        Converts the specified tick_type value to its corresponding lower-case string representation
        
        :param tick_type: The tick_type value
        :returns: A lower-case string representation of the specified tick_type value.
        """
        ...

    @staticmethod
    def to_camel_case(value: str) -> str:
        """Converts the provided string into camel case notation"""
        ...

    @staticmethod
    def to_csv(str: str, size: int = 4) -> typing.List[str]:
        """
        Breaks the specified string into csv components, all commas are considered separators
        
        :param str: The string to be broken into csv
        :param size: The expected size of the output list
        :returns: A list of the csv pieces.
        """
        ...

    @staticmethod
    def to_csv_data(str: str, size: int = 4, delimiter: str = ...) -> typing.List[str]:
        """
        Breaks the specified string into csv components, works correctly with commas in data fields
        
        :param str: The string to be broken into csv
        :param size: The expected size of the output list
        :param delimiter: The delimiter used to separate entries in the line
        :returns: A list of the csv pieces.
        """
        ...

    @staticmethod
    def to_decimal(str: str) -> float:
        """
        Extension method for faster string to decimal conversion.
        
        :param str: String to be converted to positive decimal value
        :returns: Decimal value of the string.
        """
        ...

    @staticmethod
    def to_decimal_allow_exponent(str: str) -> float:
        """
        Extension method for string to decimal conversion where string can represent a number with exponent xe-y
        
        :param str: String to be converted to decimal value
        :returns: Decimal value of the string.
        """
        ...

    @staticmethod
    def to_financial_figures(number: float) -> str:
        """
        Converts a decimal into a rounded number ending with K (thousands), M (millions), B (billions), etc.
        
        :param number: Number to convert
        :returns: Formatted number with figures written in shorthand form.
        """
        ...

    @staticmethod
    def to_func(date_rule: QuantConnect.Scheduling.IDateRule) -> typing.Callable[[datetime.datetime], typing.Optional[datetime.datetime]]:
        """
        Converts a date rule into a function that receives current time
        and returns the next date.
        
        :param date_rule: The date rule to convert
        :returns: A function that will enumerate the provided date rules.
        """
        ...

    @staticmethod
    def to_hex_string(source: typing.List[int]) -> str:
        """
        Returns a hex string of the byte array.
        
        :param source: the byte array to be represented as string
        :returns: A new string containing the items in the enumerable.
        """
        ...

    @staticmethod
    def to_higher_resolution_equivalent(time_span: datetime.timedelta, require_exact_match: bool) -> QuantConnect.Resolution:
        """
        Converts the specified time span into a resolution enum value. If an exact match
        is not found and `require_exact_match` is false, then the higher resoluion will be
        returned. For example, time_span=5min will return Minute resolution.
        
        :param time_span: The time span to convert to resolution
        :param require_exact_match: True to throw an exception if an exact match is not found
        :returns: The resolution.
        """
        ...

    @staticmethod
    def to_int_32(str: str) -> int:
        """
        Extension method for faster string to Int32 conversion.
        
        :param str: String to be converted to positive Int32 value
        :returns: Int32 value of the string.
        """
        ...

    @staticmethod
    def to_int_64(str: str) -> int:
        """
        Extension method for faster string to Int64 conversion.
        
        :param str: String to be converted to positive Int64 value
        :returns: Int32 value of the string.
        """
        ...

    @staticmethod
    def to_lower(_enum: System.Enum) -> str:
        """
        Converts the specified enum value to its corresponding lower-case string representation
        
        :param _enum: The enumeration value
        :returns: A lower-case string representation of the specified enumeration value.
        """
        ...

    @staticmethod
    def to_md_5(str: str) -> str:
        """
        Extension method to convert a string to a MD5 hash.
        
        :param str: String we want to MD5 encode.
        :returns: MD5 hash of a string.
        """
        ...

    @staticmethod
    def to_normalized_decimal(str: str) -> float:
        """
        Extension method for faster string to normalized decimal conversion, i.e. 20.0% should be parsed into 0.2
        
        :param str: String to be converted to positive decimal value
        :returns: Decimal value of the string.
        """
        ...

    @staticmethod
    def to_order_direction(side: QuantConnect.PositionSide) -> QuantConnect.Orders.OrderDirection:
        """
        Gets the OrderDirection that corresponds to the specified side
        
        :param side: The position side to be converted
        :returns: The order direction that maps from the provided position side.
        """
        ...

    @staticmethod
    def to_order_ticket(order: QuantConnect.Orders.Order, transaction_manager: QuantConnect.Securities.SecurityTransactionManager) -> QuantConnect.Orders.OrderTicket:
        """
        Turn order into an order ticket
        
        :param order: The Order being converted
        :param transaction_manager: The transaction manager, SecurityTransactionManager
        """
        ...

    @staticmethod
    def to_py_list(enumerable: System.Collections.IEnumerable) -> typing.List[typing.Any]:
        """
        Converts an IEnumerable to a PyList
        
        :param enumerable: IEnumerable object to convert
        :returns: PyList.
        """
        ...

    @staticmethod
    def to_py_list_un_safe(enumerable: System.Collections.IEnumerable) -> typing.List[typing.Any]:
        """
        Converts an IEnumerable to a PyList
        
        :param enumerable: IEnumerable object to convert
        :returns: PyList.
        """
        ...

    @staticmethod
    def to_query_string(pairs: System.Collections.Generic.IDictionary[str, System.Object]) -> str:
        """
        Convert dictionary to query string
        
        :param pairs: 
        """
        ...

    @staticmethod
    def to_safe_string(py_object: typing.Any) -> str:
        """
        Returns a string that represents the current PyObject
        
        :param py_object: The PyObject being converted
        :returns: string that represents the current PyObject.
        """
        ...

    @staticmethod
    def to_sha_256(data: str) -> str:
        """
        Encrypt the token:time data to make our API hash.
        
        :param data: Data to be hashed by SHA256
        :returns: Hashed string.
        """
        ...

    @staticmethod
    def to_stream(str: str) -> System.IO.Stream:
        """
        Extension method to convert strings to stream to be read.
        
        :param str: String to convert to stream
        :returns: Stream instance.
        """
        ...

    @staticmethod
    def to_string_performance(option_right: QuantConnect.OptionRight) -> str:
        """
        Converts the specified option_right value to its corresponding string representation
        
        :param option_right: The option_right value
        :returns: A string representation of the specified OptionRight value.
        """
        ...

    @staticmethod
    def to_subscription_data_config(request: QuantConnect.Data.HistoryRequest, is_internal_feed: bool = False, is_filtered_subscription: bool = True) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Converts a Data.HistoryRequest instance to a SubscriptionDataConfig instance
        
        :param request: History request
        :param is_internal_feed: Set to true if this subscription is added for the sole purpose of providing currency conversion rates,
        setting this flag to true will prevent the data from being sent into the algorithm's OnData methods
        :param is_filtered_subscription: True if this subscription should have filters applied to it (market hours/user filters from security), false otherwise
        :returns: Subscription data configuration.
        """
        ...

    @staticmethod
    def to_time_span(resolution: QuantConnect.Resolution) -> datetime.timedelta:
        """
        Converts the Resolution instance into a TimeSpan instance
        
        :param resolution: The resolution to be converted
        :returns: A TimeSpan instance that represents the resolution specified.
        """
        ...

    @staticmethod
    def truncate_to_3_decimal_places(value: float) -> float:
        """
        Will truncate the provided decimal, without rounding, to 3 decimal places
        
        :param value: The value to truncate
        :returns: New instance with just 3 decimal places.
        """
        ...

    @staticmethod
    def try_create_type(py_object: typing.Any, type: typing.Optional[typing.Type]) -> typing.Tuple[bool, typing.Type]:
        """
        Try to create a type with a given name, if PyObject is not a CLR type. Otherwise, convert it.
        
        :param py_object: Python object representing a type.
        :param type: Type object
        :returns: True if was able to create the type.
        """
        ...

    @staticmethod
    def try_download_data(client: typing.Any, url: str, data: typing.Optional[str], status_code: typing.Optional[typing.Optional[System.Net.HttpStatusCode]], headers: System.Collections.Generic.Dictionary[str, str] = None) -> typing.Tuple[bool, str, typing.Optional[System.Net.HttpStatusCode]]:
        """
        Helper method to download a provided url as a string
        
        :param client: The http client to use
        :param url: The url to download data from
        :param data: The downloaded data
        :param status_code: The request status code
        :param headers: Add custom headers for the request
        """
        ...

    @staticmethod
    def try_get_decimal_from_csv(csv_line: str, index: int, value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Gets the value at the specified index from a CSV line, converted into a decimal.
        
        :param csv_line: The CSV line
        :param index: The index of the value to be extracted from the CSV line
        :param value: The decimal value at the given index
        :returns: Whether there was a value at the given index and could be extracted and converted into a decimal.
        """
        ...

    @staticmethod
    def try_get_from_csv(csv_line: str, index: int, result: typing.Optional[System.ReadOnlySpan[str]]) -> typing.Tuple[bool, System.ReadOnlySpan[str]]:
        """
        Gets the value at the specified index from a CSV line.
        
        :param csv_line: The CSV line
        :param index: The index of the value to be extracted from the CSV line
        :param result: The value at the given index
        :returns: Whether there was a value at the given index and could be extracted.
        """
        ...

    @staticmethod
    def try_get_live_subscription_symbol(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], mapped: typing.Optional[typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]]) -> typing.Tuple[bool, typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]]:
        """Helper method to determine symbol for a live subscription"""
        ...

    @staticmethod
    def try_parse_security_type(value: str, security_type: typing.Optional[QuantConnect.SecurityType], ignore_case: bool = True) -> typing.Tuple[bool, QuantConnect.SecurityType]:
        """
        Attempts to convert the string into a SecurityType enum value
        
        :param value: string value to convert to SecurityType
        :param security_type: SecurityType output
        :param ignore_case: Ignore casing
        :returns: true if parsed into a SecurityType successfully, false otherwise.
        """
        ...

    @staticmethod
    def unsubscribe_with_mapping(data_queue_handler: QuantConnect.Interfaces.IDataQueueHandler, data_config: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """Helper method to unsubscribe a given configuration, handling any required mapping"""
        ...

    @staticmethod
    @overload
    def wait_one(wait_handle: System.Threading.WaitHandle, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current System.Threading.WaitHandle receives a signal, while observing a System.Threading.CancellationToken.
        
        :param wait_handle: The wait handle to wait on
        :param cancellation_token: The System.Threading.CancellationToken to observe.
        """
        ...

    @staticmethod
    @overload
    def wait_one(wait_handle: System.Threading.WaitHandle, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current System.Threading.WaitHandle is set, using a System.TimeSpan to measure the time interval, while observing a System.Threading.CancellationToken.
        
        :param wait_handle: The wait handle to wait on
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellation_token: The System.Threading.CancellationToken to observe.
        :returns: true if the System.Threading.WaitHandle was set; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def wait_one(wait_handle: System.Threading.WaitHandle, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current System.Threading.WaitHandle is set, using a 32-bit signed integer to measure the time interval, while observing a System.Threading.CancellationToken.
        
        :param wait_handle: The wait handle to wait on
        :param milliseconds_timeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite(-1) to wait indefinitely.
        :param cancellation_token: The System.Threading.CancellationToken to observe.
        :returns: true if the System.Threading.WaitHandle was set; otherwise, false.
        """
        ...

    @staticmethod
    def with_embedded_html_anchors(source: str) -> str:
        """
        Convert a string into the same string with a URL! :)
        
        :param source: The source string to be converted
        :returns: The same source string but with anchor tags around substrings matching a link regex.
        """
        ...


class BinaryComparison(System.Object):
    """
    Enumeration class defining binary comparisons and providing access to expressions and functions
    capable of evaluating a particular comparison for any type. If a particular type does not implement
    a binary comparison than an exception will be thrown.
    """

    EQUAL: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.Equal"""

    NOT_EQUAL: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.NotEqual"""

    LESS_THAN: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.LessThan"""

    GREATER_THAN: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.GreaterThan"""

    LESS_THAN_OR_EQUAL: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.LessThanOrEqual"""

    GREATER_THAN_OR_EQUAL: QuantConnect.BinaryComparison = ...
    """Gets the BinaryComparison equivalent of ExpressionType.GreaterThanOrEqual"""

    @property
    def type(self) -> typing.Any:
        """Gets the expression type defining the binary comparison."""
        ...

    def flip_operands(self) -> QuantConnect.BinaryComparison:
        """
        Flips the logic ordering of the comparison's operands. For example, LESS_THAN
        is converted into GREATER_THAN
        """
        ...

    @staticmethod
    def from_expression_type(type: typing.Any) -> QuantConnect.BinaryComparison:
        """Gets the BinaryComparison matching the provided type"""
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class Compression(System.Object):
    """Compression class manages the opening and extraction of compressed files (zip, tar, tar.gz)."""

    @staticmethod
    def extract_7_zip_archive(input_file: str, output_directory: str, exec_timeout: int = 60000) -> None:
        """
        Extracts a 7-zip archive to disk, using the 7-zip CLI utility
        
        :param input_file: Path to the 7z file
        :param output_directory: Directory to output contents of 7z
        :param exec_timeout: Timeout in seconds for how long we should wait for the extraction to complete
        """
        ...

    @staticmethod
    @overload
    def get_zip_entry_file_names(zip_file_name: str) -> typing.Iterable[str]:
        """
        Returns the entry file names contained in a zip file
        
        :param zip_file_name: The zip file name
        :returns: An IEnumerable of entry file names.
        """
        ...

    @staticmethod
    @overload
    def get_zip_entry_file_names(zip_file_stream: System.IO.Stream) -> typing.Iterable[str]:
        """
        Return the entry file names contained in a zip file
        
        :param zip_file_stream: Stream to the file
        :returns: IEnumerable of entry file names.
        """
        ...

    @staticmethod
    def read_lines(filename: str) -> typing.List[str]:
        """
        Streams each line from the first zip entry in the specified zip file
        
        :param filename: The zip file path to stream
        :returns: An enumerable containing each line from the first unzipped entry.
        """
        ...

    @staticmethod
    def un_g_zip(gzip_file_name: str, target_directory: str) -> str:
        """
        Extract .gz files to disk
        
        :param gzip_file_name: 
        :param target_directory: 
        """
        ...

    @staticmethod
    @overload
    def un_tar(stream: System.IO.Stream, is_tar_gz: bool) -> typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]:
        """
        Enumerate through the files of a TAR and get a list of KVP names-byte arrays
        
        :param stream: The input tar stream
        :param is_tar_gz: True if the input stream is a .tar.gz or .tgz
        :returns: An enumerable containing each tar entry and it's contents.
        """
        ...

    @staticmethod
    @overload
    def un_tar(source: str) -> typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]:
        """
        Enumerate through the files of a TAR and get a list of KVP names-byte arrays.
        
        :param source: 
        """
        ...

    @staticmethod
    def un_tar_files(source: str, destination: str) -> None:
        """
        Extracts all file from a zip archive and copies them to a destination folder.
        
        :param source: The source zip file.
        :param destination: The destination folder to extract the file to.
        """
        ...

    @staticmethod
    def un_tar_gz_files(source: str, destination: str) -> None:
        """
        Extract tar.gz files to disk
        
        :param source: Tar.gz source file
        :param destination: Location folder to unzip to
        """
        ...

    @staticmethod
    @overload
    def unzip(zip: str, directory: str, overwrite: bool = False) -> bool:
        """
        Unzips the specified zip file to the specified directory
        
        :param zip: The zip to be unzipped
        :param directory: The directory to place the unzipped files
        :param overwrite: Flag specifying whether or not to overwrite existing files
        """
        ...

    @staticmethod
    @overload
    def unzip(filename: str, zip: typing.Optional[typing.Any]) -> typing.Tuple[System.IO.StreamReader, typing.Any]:
        """
        Streams a local zip file using a streamreader.
        Important: the caller must call Dispose() on the returned ZipFile instance.
        
        :param filename: Location of the original zip file
        :param zip: The ZipFile instance to be returned to the caller
        :returns: Stream reader of the first file contents in the zip file.
        """
        ...

    @staticmethod
    @overload
    def unzip(filename: str, zip_entry_name: str, zip: typing.Optional[typing.Any]) -> typing.Tuple[System.IO.StreamReader, typing.Any]:
        """
        Streams a local zip file using a streamreader.
        Important: the caller must call Dispose() on the returned ZipFile instance.
        
        :param filename: Location of the original zip file
        :param zip_entry_name: The zip entry name to open a reader for. Specify null to access the first entry
        :param zip: The ZipFile instance to be returned to the caller
        :returns: Stream reader of the first file contents in the zip file.
        """
        ...

    @staticmethod
    @overload
    def unzip(filename: str) -> typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[str]]]:
        """
        Streams the unzipped file as key value pairs of file name to file contents.
        NOTE: When the returned enumerable finishes enumerating, the zip stream will be
        closed rendering all key value pair Value properties unaccessible. Ideally this
        would be enumerated depth first.
        
        :param filename: The zip file to stream
        :returns: The stream zip contents.
        """
        ...

    @staticmethod
    @overload
    def unzip(stream: System.IO.Stream) -> typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[str]]]:
        """
        Lazily unzips the specified stream
        
        :param stream: The zipped stream to be read
        :returns: An enumerable whose elements are zip entry key value pairs with
        a key of the zip entry name and the value of the zip entry's file lines.
        """
        ...

    @staticmethod
    def unzip_data(zip_data: typing.List[int], encoding: System.Text.Encoding = None) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Uncompress zip data byte array into a dictionary string array of filename-contents.
        
        :param zip_data: Byte data array of zip compressed information
        :param encoding: Specifies the encoding used to read the bytes. If not specified, defaults to ASCII
        :returns: Uncompressed dictionary string-sting of files in the zip.
        """
        ...

    @staticmethod
    def unzip_data_async(stream: System.IO.Stream, encoding: System.Text.Encoding = None) -> System.Threading.Tasks.Task[System.Collections.Generic.Dictionary[str, str]]:
        """
        Uncompress zip data byte array into a dictionary string array of filename-contents.
        
        :param stream: Stream data of zip compressed information
        :param encoding: Specifies the encoding used to read the bytes. If not specified, defaults to ASCII
        :returns: Uncompressed dictionary string-sting of files in the zip.
        """
        ...

    @staticmethod
    def unzip_stream(zipstream: System.IO.Stream, zip_file: typing.Optional[typing.Any], entry_name: str = None) -> typing.Tuple[System.IO.Stream, typing.Any]:
        """Unzip a stream that represents a zip file and return the first entry as a stream"""
        ...

    @staticmethod
    def unzip_stream_to_stream_reader(zipstream: System.IO.Stream) -> System.IO.StreamReader:
        """Unzip a local file and return its contents via streamreader:"""
        ...

    @staticmethod
    @overload
    def unzip_to_folder(zip_data: typing.List[int], output_folder: str) -> typing.List[str]:
        """
        Unzip the given byte array and return the created file names.
        
        :param zip_data: A byte array containing the zip
        :param output_folder: The target output folder
        :returns: List of unzipped file names.
        """
        ...

    @staticmethod
    @overload
    def unzip_to_folder(zip_file: str) -> typing.List[str]:
        """
        Unzip a local file and return the created file names
        
        :param zip_file: Location of the zip on the HD
        :returns: List of unzipped file names.
        """
        ...

    @staticmethod
    def validate_zip(path: str) -> bool:
        """
        Validates whether the zip is corrupted or not
        
        :param path: Path to the zip file
        :returns: true if archive tests ok; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def zip(text_path: str, zip_entry_name: str, delete_original: bool = True) -> str:
        """
        Compress a given file and delete the original file. Automatically rename the file to name.zip.
        
        :param text_path: Path of the original file
        :param zip_entry_name: The name of the entry inside the zip file
        :param delete_original: Boolean flag to delete the original file after completion
        :returns: String path for the new zip file.
        """
        ...

    @staticmethod
    @overload
    def zip(source: str, destination: str, zip_entry_name: str, delete_original: bool) -> None:
        """
        Compresses the specified source file.
        
        :param source: The source file to be compressed
        :param destination: The destination zip file path
        :param zip_entry_name: The zip entry name for the file
        :param delete_original: True to delete the source file upon completion
        """
        ...

    @staticmethod
    @overload
    def zip(text_path: str, delete_original: bool = True) -> str:
        """
        Compress a given file and delete the original file. Automatically rename the file to name.zip.
        
        :param text_path: Path of the original file
        :param delete_original: Boolean flag to delete the original file after completion
        :returns: String path for the new zip file.
        """
        ...

    @staticmethod
    @overload
    def zip(data: str, zip_path: str, zip_entry: str) -> None:
        """
        Compress given data to the path given
        
        :param data: Data to write to zip
        :param zip_path: Path to write to
        :param zip_entry: Entry to save the data as
        """
        ...

    @staticmethod
    def zip_bytes(bytes: typing.List[int], zip_entry_name: str) -> typing.List[int]:
        """
        Performs an in memory zip of the specified bytes
        
        :param bytes: The file contents in bytes to be zipped
        :param zip_entry_name: The zip entry name
        :returns: The zipped file as a byte array.
        """
        ...

    @staticmethod
    @overload
    def zip_bytes_async(target: System.IO.Stream, data: typing.List[int], zip_entry_name: str, mode: typing.Optional[ZipArchiveMode] = None, compression_level: typing.Optional[CompressionLevel] = None) -> System.Threading.Tasks.Task:
        """
        Performs an in memory zip of the specified bytes in the target stream
        
        :param target: The target stream
        :param data: The file contents in bytes to be zipped
        :param zip_entry_name: The zip entry name
        :param mode: The archive mode
        :param compression_level: The desired compression level
        :returns: The zipped file as a byte array.
        """
        ...

    @staticmethod
    @overload
    def zip_bytes_async(target: System.IO.Stream, data: typing.List[System.Collections.Generic.KeyValuePair[typing.List[int], str]], mode: typing.Optional[ZipArchiveMode] = None, compression_level: typing.Optional[CompressionLevel] = None) -> System.Threading.Tasks.Task:
        """
        Performs an in memory zip of the specified bytes in the target stream
        
        :param target: The target stream
        :param data: The file contents in bytes to be zipped
        :param mode: The archive mode
        :param compression_level: The desired compression level
        :returns: The zipped file as a byte array.
        """
        ...

    @staticmethod
    @overload
    def zip_create_append_data(path: str, entry: str, data: str, override_entry: bool = False) -> bool:
        """
        Append the zip data to the file-entry specified.
        
        :param path: The zip file path
        :param entry: The entry name
        :param data: The entry data
        :param override_entry: True if should override entry if it already exists
        :returns: True on success.
        """
        ...

    @staticmethod
    @overload
    def zip_create_append_data(path: str, entry: str, data: typing.List[int], override_entry: bool = False) -> bool:
        """
        Append the zip data to the file-entry specified.
        
        :param path: The zip file path
        :param entry: The entry name
        :param data: The entry data
        :param override_entry: True if should override entry if it already exists
        :returns: True on success.
        """
        ...

    @staticmethod
    @overload
    def zip_data(zip_path: str, filenames_and_data: System.Collections.Generic.Dictionary[str, str]) -> bool:
        """
        Create a zip file of the supplied file names and string data source
        
        :param zip_path: Output location to save the file.
        :param filenames_and_data: File names and data in a dictionary format.
        :returns: True on successfully creating the zip file.
        """
        ...

    @staticmethod
    @overload
    def zip_data(zip_path: str, filenames_and_data: typing.List[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]) -> bool:
        """
        Create a zip file of the supplied file names and data using a byte array
        
        :param zip_path: Output location to save the file.
        :param filenames_and_data: File names and data in a dictionary format.
        :returns: True on successfully saving the file.
        """
        ...

    @staticmethod
    @overload
    def zip_data(zip_path: str, zip_entry: str, lines: typing.List[str]) -> bool:
        """
        Zips the specified lines of text into the zip_path
        
        :param zip_path: The destination zip file path
        :param zip_entry: The entry name in the zip
        :param lines: The lines to be written to the zip
        :returns: True if successful, otherwise false.
        """
        ...

    @staticmethod
    def zip_directory(directory: str, destination: str, include_root_in_zip: bool = True) -> bool:
        """
        Zips the specified directory, preserving folder structure
        
        :param directory: The directory to be zipped
        :param destination: The output zip file destination
        :param include_root_in_zip: True to include the root 'directory' in the zip, false otherwise
        :returns: True on a successful zip, false otherwise.
        """
        ...

    @staticmethod
    def zip_files(destination: str, files: typing.List[str]) -> None:
        """Zips all files specified to a new zip at the destination path"""
        ...

    @staticmethod
    @overload
    def zip_streams_async(target: str, data: typing.List[System.Collections.Generic.KeyValuePair[str, System.IO.Stream]], mode: typing.Optional[ZipArchiveMode] = None, compression_level: typing.Optional[CompressionLevel] = None) -> System.Threading.Tasks.Task:
        """
        Performs an in memory zip of the specified stream in the target stream
        
        :param target: The target stream
        :param data: The file contents in bytes to be zipped
        :param mode: The archive mode
        :param compression_level: The desired compression level
        :returns: The zipped file as a byte array.
        """
        ...

    @staticmethod
    @overload
    def zip_streams_async(target: System.IO.Stream, data: typing.List[System.Collections.Generic.KeyValuePair[str, System.IO.Stream]], mode: typing.Optional[ZipArchiveMode] = None, compression_level: typing.Optional[CompressionLevel] = None, leave_stream_open: bool = False) -> System.Threading.Tasks.Task:
        """
        Performs an in memory zip of the specified stream in the target stream
        
        :param target: The target stream
        :param data: The file contents in bytes to be zipped
        :param mode: The archive mode
        :param compression_level: The desired compression level
        :param leave_stream_open: True to leave the taget stream open
        :returns: The zipped file as a byte array.
        """
        ...


class ZipStreamWriter(System.IO.TextWriter):
    """Provides an implementation of TextWriter to write to a zip file"""

    @property
    def encoding(self) -> System.Text.Encoding:
        """When overridden in a derived class, returns the character encoding in which the output is written."""
        ...

    def __init__(self, filename: str, zip_entry: str) -> None:
        """
        Initializes a new instance of the ZipStreamWriter class
        
        :param filename: The output zip file name
        :param zip_entry: The file name in the zip file
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """
        Releases the unmanaged resources used by the System.IO.TextWriter and optionally releases the managed resources.
        
        
        This codeEntityType is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def flush(self) -> None:
        """Clears all buffers for the current writer and causes any buffered data to be written to the underlying device."""
        ...

    def write(self, value: str) -> None:
        """
        Writes a character to the text string or stream.
        
        :param value: The character to write to the text stream.
        """
        ...

    def write_line(self, value: str) -> None:
        """
        Writes a string followed by a line terminator to the text string or stream.
        
        :param value: The string to write. If value is null, only the line terminator is written.
        """
        ...


class Messages(System.Object):
    """Provides user-facing message construction methods and static messages for the QuantConnect namespace"""

    class AlphaRuntimeStatistics(System.Object):
        """Provides user-facing messages for the AlphaRuntimeStatistics class and its consumers or related classes"""

        return_over_maximum_drawdown_key: str = "Return Over Maximum Drawdown"
        """Returns a string message saying: Return Over Maximum Drawdown"""

        portfolio_turnover_key: str = "Portfolio Turnover"
        """Returns a string message saying: Portfolio Turnover"""

        total_insights_generated_key: str = "Total Insights Generated"
        """Returns a string message saying: Total Insights Generated"""

        total_insights_closed_key: str = "Total Insights Closed"
        """Returns a string message saying: Total Insights Closed"""

        total_insights_analysis_completed_key: str = "Total Insights Analysis Completed"
        """Returns a string message saying: Total Insights Analysis Completed"""

        long_insight_count_key: str = "Long Insight Count"
        """Returns a string message saying: Long Insight Count"""

        short_insight_count_key: str = "Short Insight Count"
        """Returns a string message saying: Short Insight Count"""

        long_short_ratio_key: str = "Long/Short Ratio"
        """Returns a string message saying: Long/Short Ratio"""

    class Chart(System.Object):
        """Provides user-facing messages for the QuantConnect.Chart class and its consumers or related classes"""

        chart_series_already_exists: str = "Chart series name already exists"
        """Returns a string message saying Chart series name already exists"""

    class ChartPoint(System.Object):
        """Provides user-facing messages for the QuantConnect.ChartPoint class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.ChartPoint) -> str:
            """Parses a given ChartPoint object into a string message"""
            ...

    class Candlestick(System.Object):
        """Provides user-facing messages for the QuantConnect.Candlestick class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.Candlestick) -> str:
            """Parses a given Candlestick object into a string message"""
            ...

    class Currencies(System.Object):
        """Provides user-facing messages for the QuantConnect.Currencies class and its consumers or related classes"""

        @staticmethod
        def failed_conversion_to_decimal(value: str) -> str:
            """Returns a string message saying the given value cannot be converted to a decimal number"""
            ...

    class ExtendedDictionary(System.Object):
        """Provides user-facing messages for the QuantConnect.ExtendedDictionary{T} class and its consumers or related classes"""

        clear_method_not_implemented: str = "Types deriving from 'ExtendedDictionary' must implement the 'void Clear() method."
        """Returns a string message saying the types deriving from ExtendedDictionary must implement the void Clear() method"""

        remove_method_not_implemented: str = "Types deriving from 'ExtendedDictionary' must implement the 'void Remove(Symbol) method."
        """Returns a string message saying the types deriving from ExtendedDictionary must implement the void Remove(Symbol) method"""

        indexer_by_symbol_not_implemented: str = "Types deriving from 'ExtendedDictionary' must implement the 'T this[Symbol] method."
        """Returns a string message saying the types deriving from ExtendedDictionary must implement the T this<Symbol> method"""

        @staticmethod
        def ticker_not_found_in_symbol_cache(ticker: str) -> str:
            """
            Returns a string message saying that the given ticker was not found in the SymbolCache. It also gives a recommendation
            for solving this problem
            """
            ...

    class Extensions(System.Object):
        """Provides user-facing messages for the QuantConnect.Extensions class and its consumers or related classes"""

        error_adjusting_symbol_by_offset: str = "Adjusting a symbol by an offset is currently only supported for non canonical futures"
        """Returns a string message saying adjusting a symbol by an offset is currently only supported for non canonical futures"""

        null_data_provider: str = ...
        """Returns a string message saying the provided DataProvider instance is null"""

        null_or_empty_source_to_convert_to_hex_string: str = "Source cannot be null or empty."
        """Returns a string message saying the source cannot be null or empty"""

        create_option_chain_requires_option_symbol: str = "CreateOptionChain requires an option symbol."
        """Returns a string message saying the CreateOptionChain method requires an option symbol"""

        create_future_chain_requires_future_symbol: str = "CreateFutureChain requires a future symbol."
        """Returns a string message saying the CreateFutureChain method requires a future symbol"""

        greatest_common_divisor_empty_list: str = "The list of values cannot be empty"
        """Returns a string message saying the list of values cannot be empty"""

        @staticmethod
        def cannot_cast_non_finite_floating_point_value_to_decimal(input: float) -> str:
            """
            Returns a string message saying it is impossible to cast the given non-finite floating-point value
            as a decimal
            """
            ...

        @staticmethod
        def convert_to_dictionary_failed(source_type: str, target_type: str, reason: str) -> str:
            """
            Returns a string message saying the method ConvertToDictionary cannot be used to convert a given source
            type into another given target type. It also specifies the reason.
            """
            ...

        @staticmethod
        def convert_to_symbol_enumerable_failed(item: typing.Any) -> str:
            """
            Returns a string message saying the given argument type should Symbol or a list of Symbol. It also
            shows the given item as well as its Python type
            """
            ...

        @staticmethod
        def data_type_missing_parameterless_constructor(type: typing.Type) -> str:
            """Returns a string message saying the given data type is missing a parameterless constructor"""
            ...

        @staticmethod
        def download_data_failed(url: str) -> str:
            """Returns a string message saying the process of downloading data from the given url failed"""
            ...

        @staticmethod
        def failed_to_create_instance_of_type(type: typing.Type) -> str:
            """Returns a string message saying the process of creating an instance of the given type failed"""
            ...

        @staticmethod
        def no_default_option_style_for_security_type(security_type: QuantConnect.SecurityType) -> str:
            """
            Returns a string message saying the given security type has no default OptionStyle, because it has no options
            available for it
            """
            ...

        @staticmethod
        def object_from_python_is_not_ac_sharp_type(object_repr: str) -> str:
            """Returns a string message saying the given object is not a C# type"""
            ...

        @staticmethod
        def runtime_error(algorithm: QuantConnect.Interfaces.IAlgorithm, context: str) -> str:
            """
            Returns a string message saying there was a RuntimeError at a given time in UTC. It also
            shows the given context
            """
            ...

        @staticmethod
        def timeout_waiting_for_thread_to_stop_safely(thread_name: str) -> str:
            """Returns a string message saying: Timeout waiting for the given thread to stop"""
            ...

        @staticmethod
        def type_is_not_base_data(type: typing.Type) -> str:
            """
            Returns a string message saying the given data type does not inherit the required BaseData
            methods and/or attributes
            """
            ...

        @staticmethod
        def unable_to_convert_time_span_to_resolution(time_span: datetime.timedelta) -> str:
            """Returns a string message saying it was not able to exactly convert the given time span to resolution"""
            ...

        @staticmethod
        def unable_to_parse_unknown_security_type(value: str) -> str:
            """Returns a string message saying it was attempted to parse the given unknown security type"""
            ...

        @staticmethod
        def unknown_data_mapping_mode(value: str) -> str:
            """Returns a string message saying the given DataMappingMode was unexpected/unknown"""
            ...

        @staticmethod
        @overload
        def unknown_option_right(value: str) -> str:
            """Returns a string message saying the given OptionRight was unexpected/unknown"""
            ...

        @staticmethod
        @overload
        def unknown_option_right(value: QuantConnect.OptionRight) -> str:
            """Returns a string message saying the given OptionRight was unexpected/unknown"""
            ...

        @staticmethod
        @overload
        def unknown_option_style(value: str) -> str:
            """Returns a string message saying the given OptionStyle was unexpected/unknown"""
            ...

        @staticmethod
        @overload
        def unknown_option_style(value: QuantConnect.OptionStyle) -> str:
            """Returns a string message saying the given OptionStyle was unexpected/unknown"""
            ...

        @staticmethod
        def waiting_for_thread_to_stop_safely(thread_name: str) -> str:
            """Returns a string message saying: Waiting for the given thread to stop"""
            ...

        @staticmethod
        def zero_price_for_security(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """
            Returns a string message saying the security does not have an accurate price as it has not yet received
            a bar of data, as well as some recommendations
            """
            ...

    class Holding(System.Object):
        """Provides user-facing messages for the QuantConnect.Holding class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.Holding) -> str:
            """Parses a Holding object into a string message"""
            ...

    class AlgorithmControl(System.Object):
        """Provides user-facing messages for the QuantConnect.AlgorithmControl class and its consumers or related classes"""

        chart_subscription: str = "Strategy Equity"
        """Returns a string message saying: Strategy Equity"""

    class Isolator(System.Object):
        """Provides user-facing messages for the QuantConnect.Isolator class and its consumers or related classes"""

        @staticmethod
        def memory_usage_info(memory_used: str, last_sample: str, memory_used_by_app: str, current_time_step_elapsed: datetime.timedelta, cpu_usage: int) -> str:
            """
            Returns a string message with useful information about the memory usage, such us the memory used, the last sample
            the current memory used by the given app and the CPU usage
            """
            ...

        @staticmethod
        def memory_usage_maxed_out(memory_cap: str, last_sample: str) -> str:
            """
            Returns a string message saying: Execution Security Error: Memory Usage Maxed out, with the max memory capacity
            and a last sample of the usage
            """
            ...

        @staticmethod
        def memory_usage_monitor_task_timed_out(timeout: datetime.timedelta) -> str:
            """
            Returns a string message saying: Execution Security Error: Operation timed out, with the maximum amount of minutes
            allowed
            """
            ...

        @staticmethod
        def memory_usage_over_80_percent(last_sample: float) -> str:
            """Returns a string message saying: Execution Security Error: Memory usage over 80% capacity, and the last sample taken"""
            ...

    class Market(System.Object):
        """Provides user-facing messages for the QuantConnect.Market class and its consumers or related classes"""

        @staticmethod
        def invalid_market_identifier(max_market_identifier: int) -> str:
            """Returns a string message saying the market identifier is limited to positive values less than the given maximum market identifier"""
            ...

        @staticmethod
        def tried_to_add_existing_market_identifier(market: str, existing_market: str) -> str:
            """Returns a string message saying it was attempted to add a market identifier that is already in use"""
            ...

        @staticmethod
        def tried_to_add_existing_market_with_different_identifier(market: str) -> str:
            """Returns a string message saying it was attempted to add an already added market with a different identifier"""
            ...

    class OS(System.Object):
        """Provides user-facing messages for the QuantConnect.OS class and its consumers or related classes"""

        cpu_usage_key: str = "CPU Usage"
        """CPU Usage string"""

        used_ram_key: str = "Used RAM (MB)"
        """Used RAM (MB) string"""

        total_ram_key: str = "Total RAM (MB)"
        """Total RAM (MB) string"""

        hostname_key: str = "Hostname"
        """Hostname string"""

        lean_version_key: str = "LEAN Version"
        """LEAN Version string"""

    class Parse(System.Object):
        """Provides user-facing messages for the QuantConnect.Parse class and its consumers or related classes"""

        @staticmethod
        def value_is_not_parseable(input: str, target_type: typing.Type) -> str:
            """Returns a string message saying the provided input was not parseable as the given target type"""
            ...

    class SecurityIdentifier(System.Object):
        """Provides user-facing messages for the QuantConnect.SecurityIdentifier class and its consumers or related classes"""

        no_underlying_for_identifier: str = "No underlying specified for this identifier. Check that HasUnderlying is true before accessing the Underlying property."
        """Returns a string message saying no underlying was specified for certain identifier"""

        date_not_supported_by_security_type: str = "Date is only defined for SecurityType.Equity, SecurityType.Option, SecurityType.Future, SecurityType.FutureOption, SecurityType.IndexOption, and SecurityType.Base"
        """Returns a string message saying Date is only defined for SecurityType.Equity, SecurityType.Option, SecurityType.Future, SecurityType.FutureOption, SecurityType.IndexOption, and SecurityType.Base"""

        strike_price_not_supported_by_security_type: str = "StrikePrice is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"
        """Returns a string message saying StrikePrice is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"""

        option_right_not_supported_by_security_type: str = "OptionRight is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"
        """Returns a string message saying OptionRight is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"""

        option_style_not_supported_by_security_type: str = "OptionStyle is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"
        """Returns a string message saying OptionStyle is only defined for SecurityType.Option, SecurityType.FutureOption, and SecurityType.IndexOption"""

        null_symbol: str = "SecurityIdentifier requires a non-null string 'symbol'"
        """Returns a string message saying SecurityIdentifier requires a non-null string 'symbol'"""

        symbol_with_invalid_characters: str = "Symbol must not contain the characters '|' or ' '."
        """Returns a string message saying Symbol must not contain the characters '|' or ' '"""

        properties_do_not_match_any_security_type: str = ...
        """Returns a string message saying the provided properties do not match with a valid SecurityType"""

        string_is_not_splittable: str = "The string must be splittable on space into two parts."
        """Returns a string message saying the string must be splittable on space into two parts"""

        unexpected_type_to_compare_to: str = ...
        """Returns a string message saying object must be of type SecurityIdentifier"""

        @staticmethod
        def error_parsing_security_identifier(value: str, exception: System.Exception) -> str:
            """Returns a string message saying there was an error parsing SecurityIdentifier. It also says the given error and exception"""
            ...

        @staticmethod
        def invalid_option_right(parameter_name: str) -> str:
            """Returns a string message saying the given parameter must be either 0 or 1"""
            ...

        @staticmethod
        def invalid_security_type(parameter_name: str) -> str:
            """Returns a string message saying the given parameter must be between 0 and 99"""
            ...

        @staticmethod
        def invalid_strike_price(strike_price: float) -> str:
            """Returns a string message saying the specified strike price's precision is too high"""
            ...

        @staticmethod
        def market_not_found(market: str) -> str:
            """Returns a string message saying the given market could not be found in the markets lookup"""
            ...

    class StringExtensions(System.Object):
        """Provides user-facing messages for the QuantConnect.StringExtensions class and its consumers or related classes"""

        @staticmethod
        def convert_invariant_cannot_convert_to(target_type_code: System.TypeCode) -> str:
            """Returns a string message saying StringExtensinos.ConvertInvariant does not support converting to the given TypeCode"""
            ...

    class Symbol(System.Object):
        """Provides user-facing messages for the QuantConnect.Symbol class and its consumers or related classes"""

        insufficient_information_to_create_future_option_symbol: str = "Cannot create future option Symbol using this method (insufficient information). Use `CreateOption(Symbol, ...)` instead."
        """Returns a string message saying there is insufficient information for creating certain future option symbol"""

        canonical_not_defined: str = "Canonical is only defined for SecurityType.Option, SecurityType.Future, SecurityType.FutureOption"
        """Returns a string message saying Canonical is only defined for SecurityType.Option, SecurityType.Future, SecurityType.FutureOption"""

        unexpected_object_type_to_compare_to: str = "Object must be of type Symbol or string."
        """Returns a string message saying certain object must be of type Symbol or string"""

        @staticmethod
        def no_option_type_for_underlying(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying no option type exists for the given underlying SecurityType"""
            ...

        @staticmethod
        def no_underlying_for_option(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying no underlying type exists for the given option SecurityType"""
            ...

        @staticmethod
        def security_type_cannot_be_mapped(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying the given security can not be mapped"""
            ...

        @staticmethod
        def security_type_not_implemented_yet(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying the given security type has not been implemented yet"""
            ...

        @staticmethod
        def sid_not_for_option(sid: QuantConnect.SecurityIdentifier) -> str:
            ...

        @staticmethod
        def underlying_sid_does_not_match(sid: QuantConnect.SecurityIdentifier, underlying: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            ...

    class SymbolCache(System.Object):
        """Provides user-facing messages for the QuantConnect.SymbolCache class and its consumers or related classes"""

        @staticmethod
        def multiple_matching_tickers_located(tickers: typing.List[str]) -> str:
            """Returns a string message saying mutiple potentially matching tickers were localized"""
            ...

        @staticmethod
        def unable_to_locate_ticker(ticker: str) -> str:
            """Returns a string message saying the given ticker could not be localized"""
            ...

    class SymbolRepresentation(System.Object):
        """Provides user-facing messages for the QuantConnect.SymbolRepresentation class and its consumers or related classes"""

        @staticmethod
        def failed_to_get_market_for_ticker_and_underlying(ticker: str, underlying: str) -> str:
            """Returns a string message saying SymbolRepresentation failed to get market for the given ticker and underlying"""
            ...

        @staticmethod
        def invalid_osi_ticker_format(ticker: str) -> str:
            """Returns a string message saying the given ticker is not in the expected OSI format"""
            ...

        @staticmethod
        def no_market_found(ticker: str) -> str:
            """Returns a string message saying no market was found for the given ticker"""
            ...

        @staticmethod
        def security_type_not_implemented(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying the given security type is not implemented"""
            ...

        @staticmethod
        def unexpected_security_type_for_method(method_name: str, security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message saying an unexpected security type was received by the given method name"""
            ...

    class SymbolValueJsonConverter(System.Object):
        """Provides user-facing messages for the QuantConnect.SymbolValueJsonConverter class and its consumers or related classes"""

        converter_is_write_only: str = "The SymbolValueJsonConverter is write-only."
        """String message saying converter is write only"""

        converter_is_intended_to_be_directly_decorated_in_member: str = "The SymbolValueJsonConverter is intended to be decorated on the appropriate member directly."
        """String message saying converter is intended to be directly decorated in member"""

    class Time(System.Object):
        """Provides user-facing messages for the QuantConnect.Time class and its consumers or related classes"""

        invalid_bar_size: str = "barSize must be greater than TimeSpan.Zero"
        """Invalid Bar Size string message"""

        @staticmethod
        def security_count(count: int) -> str:
            """Returns a string message containing the number of securities"""
            ...

    class TradingCalendar(System.Object):
        """Provides user-facing messages for the QuantConnect.TradingCalendar class and its consumers or related classes"""

        @staticmethod
        def invalid_total_days(total_days: int) -> str:
            """Returns a string message for invalid total days"""
            ...

    class PythonCommon(System.Object):
        """Provides user-facing common messages for the Python namespace classes"""

    class MarginCallModelPythonWrapper(System.Object):
        """Provides user-facing common messages for the Python.MarginCallModelPythonWrapper namespace classes"""

        get_margin_call_orders_must_return_tuple: str = "Must return a tuple, where the first item is a list and the second a boolean"
        """String message saying: Must return a tuple, where the first item is a list and the second a boolean"""

    class PandasConverter(System.Object):
        """Provides user-facing common messages for the Python.PandasConverter namespace classes"""

        pandas_module_not_imported: str = "pandas module was not imported."
        """String message saying: Pandas module was not imported"""

    class PandasData(System.Object):
        """Provides user-facing common messages for the Python.PandasData namespace classes"""

    class PythonInitializer(System.Object):
        """Provides user-facing common messages for the Python.PythonInitializer namespace classes"""

        start: str = "start"
        """String message saying: start"""

        ended: str = "ended"
        """String message saying: ended"""

    class PythonWrapper(System.Object):
        """Provides user-facing common messages for the Python.PythonWrapper namespace classes"""

        expected_interface_type_parameter: str = "expected an interface type parameter."
        """String message saying: expected and interface type parameter"""

    class BasePythonWrapper(System.Object):
        """Provides user-facing common messages for the Python.BasePythonWrapper{TInterface} class"""

    class VolumeShareSlippageModel(System.Object):
        """Provides user-facing messages for the Orders.Slippage.VolumeShareSlippageModel class and its consumers or related classes"""

        @staticmethod
        def invalid_market_data_type(data: QuantConnect.Data.BaseData) -> str:
            """Returns a message for an invalid market data type in Volume Share Slippage Model"""
            ...

        @staticmethod
        def negative_or_zero_bar_volume(bar_volume: float, slippage_percent: float) -> str:
            """Returns a message for a negative or zero bar volume in Volume Share Slippage Model"""
            ...

        @staticmethod
        def volume_not_reported_for_market_data_type(security_type: QuantConnect.SecurityType) -> str:
            """Returns a message for a volume not reported for market data type in Volume Share Slippage Model"""
            ...

    class IndicatorDataPoint(System.Object):
        """Provides user-facing messages for the Indicators.IndicatorDataPoint class and its consumers or related classes"""

        @staticmethod
        def invalid_object_type_to_compare_to(type: typing.Type) -> str:
            """Returns a string message saying the given type is invalid for certain object"""
            ...

        @staticmethod
        def to_string(instance: QuantConnect.Indicators.IndicatorDataPoint) -> str:
            """Parses a IndicatorDataPoint instance into a string message containing basic information about it"""
            ...

        @staticmethod
        def unsupported_method(method_name: str) -> str:
            """Returns a string message saying the given method cannot be called on this type"""
            ...

    class RollingWindow(System.Object):
        """Provides user-facing messages for the Indicators.RollingWindow{T} class and its consumers or related classes"""

        no_items_removed_yet: str = "No items have been removed yet!"
        """String message saying no items have been removed yet from the rolling window"""

        index_out_of_size_range: str = "Index must be a non-negative integer"
        """String message saying the index must be a non-negative integer"""

        @staticmethod
        def invalid_size(minimum_size: int) -> str:
            """String message saying the rolling windows must have size of at least 1"""
            ...

    class DllNotFoundPythonExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.DllNotFoundPythonExceptionInterpreter class and its consumers or related classes"""

        @staticmethod
        def dynamic_link_library_not_found(dll_name: str, platform: str) -> str:
            """Returns a string message saying the given dynamic-link library could not be found"""
            ...

    class InvalidTokenPythonExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.InvalidTokenPythonExceptionInterpreter class and its consumers or related classes"""

        invalid_token_expected_substring: str = "invalid token"
        """String message saying: invalid token"""

        not_permitted_expected_substring: str = "are not permitted;"
        """String message saying: are not permitted"""

        @staticmethod
        def interpret_exception(exception: typing.Any) -> str:
            """
            Returns a string message saying: Tring to include an invalid token/character in any statement throws s SyntaxError
            exception. It also contains an advice to prevent that exception
            """
            ...

    class KeyErrorPythonExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.KeyErrorPythonExceptionInterpreter class and its consumers or related classes"""

        @staticmethod
        def key_not_found_in_collection(key: str) -> str:
            """
            Returns a string message saying the given key does not exists in the collection and the exception that is thrown
            in this case. It also advises the user on how to prevent this exception
            """
            ...

    class NoMethodMatchPythonExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.NoMethodMatchPythonExceptionInterpreter class and its consumers or related classes"""

        no_method_match_expected_substring: str = "No method match"
        """String message saying: No method match"""

        @staticmethod
        def attempted_to_access_method_that_does_not_exist(method_name: str) -> str:
            """
            Returns a string message saying the given method does not exists. It also contains the exception
            thrown is this case and an advice on how to prevent it
            """
            ...

    class ScheduledEventExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.ScheduledEventExceptionInterpreter class and its consumers or related classes"""

        @staticmethod
        def scheduled_event_name(event_name: str) -> str:
            """Returns a string message with the given event name"""
            ...

    class StackExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.StackExceptionInterpreter class and its consumers or related classes"""

        @staticmethod
        def loaded_exception_interpreter(interpreter: QuantConnect.Exceptions.IExceptionInterpreter) -> str:
            """Returns a message for a Loaded Exception Interpreter"""
            ...

    class UnsupportedOperandPythonExceptionInterpreter(System.Object):
        """Provides user-facing messages for the Exceptions.UnsupportedOperandPythonExceptionInterpreter class and its consumers or related classes"""

        unsupported_operand_type_expected_substring: str = "unsupported operand type"
        """Unsupported Operand Type Expected substring"""

        @staticmethod
        def invalid_object_types_for_operation(types: str) -> str:
            """Returns a message for invalid object types for operation"""
            ...

    class InsightManager(System.Object):
        """Provides user-facing messages for the Algorithm.Framework.Alphas.Analysis.InsightManager class and its consumers or related classes"""

        invalid_extra_analysis_period_ratio: str = "extraAnalysisPeriodRatio must be greater than or equal to zero."
        """String message saying extraAnalysisPeriodRatio must be greater than or equal to zero"""

        @staticmethod
        def zero_initial_price_value(frontier_time_utc: typing.Union[datetime.datetime, datetime.date], insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> str:
            """Returns a string message warning the user of an insight with zero initial price"""
            ...

    class ReadOnlySecurityValuesCollection(System.Object):
        """Provides user-facing messages for the ReadOnlySecurityValuesCollection class and its consumers or related classes"""

        @staticmethod
        def security_values_for_symbol_not_found(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """Returns a string message saying no SecurityValues were found for the given symbol"""
            ...

    class OptimizationParameterJsonConverter(System.Object):
        """Provides user-facing messages for the Optimizer.Parameters.OptimizationParameterJsonConverter class and its consumers or related classes"""

        optimization_parameter_not_specified: str = "Optimization parameter name is not specified."
        """String message saying optimization parameter name is not specified"""

        optimization_parameter_not_supported: str = "Optimization parameter is not currently supported."
        """String message saying optimization parameter is not currently supported"""

    class OptimizationStepParameter(System.Object):
        """Provides user-facing messages for the Optimizer.Parameters.OptimizationStepParameter class and its consumers or related classes"""

        step_less_than_min_step: str = ...
        """String message saying the step should be great or equal than minStep"""

        @staticmethod
        def invalid_step_range(min: float, max: float) -> str:
            """Returns a string message saying the step range is invalid"""
            ...

        @staticmethod
        def non_positive_step_value(step_var_name: str, value: float) -> str:
            """Returns a string message saying the step should be positive value"""
            ...

    class DefaultBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.DefaultBrokerageModel class and its consumers or related classes"""

        unsupported_market_on_open_orders_for_futures_and_future_options: str = "MarketOnOpen orders are not supported for futures and future options."
        """String message saying: MarketOnOpen orders are not supported for futures and future options"""

        no_data_for_symbol: str = "There is no data for this symbol yet, please check the security.HasData flag to ensure there is at least one data point."
        """String message saying: There is no data for this symbol yet"""

        order_update_not_supported: str = "Brokerage does not support update. You must cancel and re-create instead."
        """String message saying: Brokerage does not support update. You must cancel and re-create instead"""

        @staticmethod
        def invalid_order_quantity(security: QuantConnect.Securities.Security, quantity: float) -> str:
            """Returns a string message saying the quantity given was invalid for the given security"""
            ...

        @staticmethod
        def invalid_order_size(security: QuantConnect.Securities.Security, quantity: float, price: float) -> str:
            """Returns a string message saying the given order size (quantity * price) was invalid for the given security"""
            ...

        @staticmethod
        def invalid_security_type_for_leverage(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security is invalid"""
            ...

        @staticmethod
        def invalid_security_type_to_get_fill_model(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security is invalid for the given brokerage GetFillModel() method"""
            ...

        @staticmethod
        def unsupported_cross_zero_by_order_type(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, order_type: QuantConnect.Orders.OrderType) -> str:
            """Returns a message indicating that the specified order type is not supported for orders that cross the zero holdings threshold."""
            ...

        @staticmethod
        def unsupported_cross_zero_order_update(brokerage_model: QuantConnect.Brokerages.IBrokerageModel) -> str:
            """Returns a string message saying the given brokerage does not support updating the quantity of Cross Zero orders"""
            ...

        @staticmethod
        def unsupported_market_on_open_order_time(window_start: System.TimeOnly, window_end: System.TimeOnly) -> str:
            """
            Builds a descriptive error message when a OrderType.MARKET_ON_OPEN
            order is submitted outside the valid submission window.
            
            :param window_start: The start of the valid submission window (typically evening of the prior day).
            :param window_end: The end of the valid submission window (typically morning of the next day).
            :returns: A formatted string describing why the order is not valid at the current time,
            including the allowed submission window and suggested fixes.
            """
            ...

        @staticmethod
        def unsupported_order_type(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, order: QuantConnect.Orders.Order, supported_order_types: typing.List[QuantConnect.Orders.OrderType]) -> str:
            """
            Returns a string message saying the type of the given order is unsupported by the given brokerage model. It also
            mentions the supported order types
            """
            ...

        @staticmethod
        def unsupported_security_type(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, security: QuantConnect.Securities.Security) -> str:
            """Retunrns a string message saying the type of the given security is not supported by the given brokerage"""
            ...

        @staticmethod
        def unsupported_time_in_force(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying the Time In Force of the given order is unsupported by the given brokerage
            model
            """
            ...

        @staticmethod
        def unsupported_update_quantity_order(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, order_type: QuantConnect.Orders.OrderType) -> str:
            """Returns a message indicating that the specified order type cannot be updated quantity using the given brokerage model."""
            ...

    class AlpacaBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.AlpacaBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def trading_outside_regular_hours_not_supported(brokerage_model: QuantConnect.Brokerages.IBrokerageModel, order_type: QuantConnect.Orders.OrderType, time_in_force: QuantConnect.Orders.TimeInForce) -> str:
            """
            Returns a message indicating that the specified order type is not supported for trading outside
            regular hours by the given brokerage model.
            """
            ...

    class AlphaStreamsBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.AlphaStreamsBrokerageModel class and its consumers or related classes"""

        unsupported_account_type: str = "The Alpha Streams brokerage does not currently support Cash trading."
        """String message saying: The Alpha Streams brokerage does not currently support Cash trading"""

    class AxosBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.AxosClearingBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def non_integer_order_quantity(order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying the order quantity must be Integer. It also contains
            the quantity of the given order
            """
            ...

    class BinanceBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.BinanceBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_order_type_for_security_type(order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying the type of the given order is unsupported for the symbol of the given
            security
            """
            ...

        @staticmethod
        def unsupported_order_type_with_link_to_supported_types(base_api_endpoint: str, order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying the type of the given order is unsupported for the symbol of the given
            security. The message also contains a link to the supported order types in Binance
            """
            ...

    class BinanceUSBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.BinanceUSBrokerageModel class and its consumers or related classes"""

        unsupported_account_type: str = "The Binance.US brokerage does not currently support Margin trading."
        """String message saying: The Binance.US brokerage does not currently support Margin trading"""

    class BrokerageMessageEvent(System.Object):
        """Provides user-facing messages for the Brokerages.BrokerageMessageEvent class and its consumers or related classes"""

        disconnect_code: str = "Disconnect"
        """String message saying: Disconnect"""

        reconnect_code: str = "Reconnect"
        """String message saying: Reconnect"""

        @staticmethod
        def to_string(message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> str:
            """Parses a given BrokerageMessageEvent object into a string containing basic information about it"""
            ...

    class DefaultBrokerageMessageHandler(System.Object):
        """Provides user-facing messages for the Brokerages.DefaultBrokerageMessageHandler class and its consumers or related classes"""

        brokerage_error_context: str = "Brokerage Error"
        """String message saying: Brokerage Error"""

        disconnected: str = "DefaultBrokerageMessageHandler.Handle(): Disconnected."
        """String message saying: DefaultBrokerageMessageHandler.Handle(): Disconnected"""

        reconnected: str = "DefaultBrokerageMessageHandler.Handle(): Reconnected."
        """String message saying: DefaultBrookerageMessageHandler.Handle(): Reconnected"""

        disconnected_when_exchanges_are_closed: str = "DefaultBrokerageMessageHandler.Handle(): Disconnect when exchanges are closed, checking back before exchange open."
        """
        String message saying: DefaultBrokerageMessageHandler.Handle(): Disconnect when exchanges are closed,
        checking back before exchange open
        """

        still_disconnected: str = "DefaultBrokerageMessageHandler.Handle(): Still disconnected, goodbye."
        """String message saying: DefaultBrokerageMessageHandler.Handle(): Still disconnected, goodbye"""

        brokerage_disconnected_shut_down_context: str = "Brokerage Disconnect"
        """String message saying: Brokerage Disconnect"""

        @staticmethod
        def brokerage_info(message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> str:
            """Returns a string message with basic information about the given message event"""
            ...

        @staticmethod
        def brokerage_warning(message_event: QuantConnect.Brokerages.BrokerageMessageEvent) -> str:
            """Returns a string message warning from the given message event"""
            ...

        @staticmethod
        def disconnected_when_exchanges_are_open(reconnection_timeout: datetime.timedelta) -> str:
            """
            Returns a string message saying the brokerage is disconnected when exchanges are open and that it's
            trying to reconnect for the given reconnection timeout minutes
            """
            ...

        @staticmethod
        def time_until_next_market_open(time_until_next_market_open: datetime.timedelta) -> str:
            """Returns a string message with the time until the next market open"""
            ...

    class ExanteBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.ExanteBrokerageModel class and its consumers or related classes"""

        null_order: str = "Order is null."
        """String message saying: Order is null"""

        price_not_set: str = "Price is not set."
        """String message saying: Price is not set"""

    class FTXBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.FTXBrokerageModel class and its consumers or related classes"""

        trigger_price_too_high: str = "Trigger price too high: must be below current market price."
        """String message saying: Trigger price too high, must be below current market price"""

        trigger_price_too_low: str = "Trigger price too low: must be above current market price."
        """String message saying: Trigger price too low, must be above current market price"""

    class FxcmBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.FxcmBrokerageModel class and its consumers or related classes"""

        invalid_order_price: str = "Limit Buy orders and Stop Sell orders must be below market, Limit Sell orders and Stop Buy orders must be above market."
        """
        String message saying: Limit Buy orders and Stop Sell orders must be below market, Limit Sell orders and Stop Buy orders
        must be above market
        """

        @staticmethod
        def invalid_order_quantity_for_lot_size(security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying the order quantity must be a multiple of LotSize. It also contains the security's Lot
            Size
            """
            ...

        @staticmethod
        def price_out_of_range(order_type: QuantConnect.Orders.OrderType, order_direction: QuantConnect.Orders.OrderDirection, order_price: float, current_price: float) -> str:
            """Returns a string message saying the order price is too far from the current market price"""
            ...

    class CoinbaseBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.CoinbaseBrokerageModel class and its consumers or related classes"""

        unsupported_account_type: str = "The Coinbase brokerage does not currently support Margin trading."
        """String message saying: The Coinbase brokerage does not currently support Margin trading"""

        @staticmethod
        def stop_market_orders_no_longer_supported(stop_market_order_support_end_date: typing.Union[datetime.datetime, datetime.date]) -> str:
            """Returns a string message saying the Stop Market orders are no longer supported since the given end date"""
            ...

    class InteractiveBrokersFixModel(System.Object):
        """Provides user-facing messages for the Brokerages.InteractiveBrokersFixModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_combo_orders_for_future_options(brokerage_model: QuantConnect.Brokerages.InteractiveBrokersFixModel, order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying the given brokerage model does not support order exercises
            for index and cash-settled options
            """
            ...

    class InteractiveBrokersBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.InteractiveBrokersBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def invalid_forex_order_size(min: float, max: float, currency: str) -> str:
            """Returns a string message containing the minimum and maximum limits for the allowable order size as well as the currency"""
            ...

        @staticmethod
        def unsupported_exercise_for_index_and_cash_settled_options(brokerage_model: QuantConnect.Brokerages.InteractiveBrokersBrokerageModel, order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying the given brokerage model does not support order exercises
            for index and cash-settled options
            """
            ...

    class TradierBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.TradierBrokerageModel class and its consumers or related classes"""

        unsupported_security_type: str = "This model only supports equities and options."
        """Unsupported Security Type string message"""

        unsupported_time_in_force_type: str = ...
        """Unsupported Time In Force Type string message"""

        extended_market_hours_trading_not_supported: str = "Tradier does not support extended market hours trading. Your order will be processed at market open."
        """Extended Market Hours Trading Not Supported string message"""

        order_quantity_update_not_supported: str = "Tradier does not support updating order quantities."
        """Order Quantity Update Not Supported string message"""

        open_orders_cancel_on_reverse_split_symbols: str = "Tradier Brokerage cancels open orders on reverse split symbols"
        """Open Orders Cancel On Reverse Split Symbols string message"""

        short_order_is_gtc: str = "You cannot place short stock orders with GTC, only day orders are allowed"
        """Short Order Is GTC string message"""

        sell_short_order_last_price_below_5: str = "Sell Short order cannot be placed for stock priced below $5"
        """Sell Short Order Last Price Below 5 string message"""

        incorrect_order_quantity: str = "Quantity should be between 1 and 10,000,000"
        """Incorrect Order Quantity string message"""

        @staticmethod
        def extended_market_hours_trading_not_supported_outside_extended_session(pre_market_segment: QuantConnect.Securities.MarketHoursSegment, post_market_segment: QuantConnect.Securities.MarketHoursSegment) -> str:
            """Extended Market Hours Trading Not Supported Outside Extended Session string message"""
            ...

    class TradingTechnologiesBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.TradingTechnologiesBrokerageModel class and its consumers or related classes"""

        invalid_stop_market_order_price: str = "StopMarket Sell orders must be below market, StopMarket Buy orders must be above market."
        """Invalid Stop Market Order Price string message"""

        invalid_stop_limit_order_price: str = "StopLimit Sell orders must be below market, StopLimit Buy orders must be above market."
        """Invalid Stop Limit Order Price string message"""

        invalid_stop_limit_order_limit_price: str = "StopLimit Buy limit price must be greater than or equal to stop price, StopLimit Sell limit price must be smaller than or equal to stop price."
        """Invalid Stop Limit Order Limit Price string message"""

    class WolverineBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.WolverineBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_order_type(order: QuantConnect.Orders.Order) -> str:
            """Returns a message for an unsupported order type in Wolverine Brokerage Model"""
            ...

    class RBIBrokerageModel(System.Object):
        """Provides user-facing messages for the Brokerages.RBIBrokerageModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_order_type(order: QuantConnect.Orders.Order) -> str:
            """
            Returns a message for an unsupported order type in RBI Brokerage Model
            
            :param order: 
            """
            ...

    class OptimizerObjectivesCommon(System.Object):
        """Provides user-facing common messages for the Optimizer.Objectives namespace classes"""

        null_or_empty_backtest_result: str = "Backtest result can not be null or empty."
        """String message saying the backtest result can not be null or empty"""

    class Constraint(System.Object):
        """Provides user-facing messages for the Optimizer.Objectives.Constraint class and its consumers or related classes"""

        constraint_target_value_not_specified: str = "Constraint target value is not specified"
        """String message saying the constraint target value is not specified"""

    class ExtremumJsonConverter(System.Object):
        """Provides user-facing messages for the Optimizer.Objectives.ExtremumJsonConverter class and its consumers or related classes"""

        unrecognized_target_direction: str = "Could not recognize target direction"
        """String message saying it could not recognize target direction"""

    class Objective(System.Object):
        """Provides user-facing messages for the Optimizer.Objectives.Objective class and its consumers or related classes"""

        null_or_empty_objective: str = "Objective can not be null or empty"
        """Null or empty Objective string message"""

    class Target(System.Object):
        """Provides user-facing messages for the Optimizer.Objectives.Target class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.Optimizer.Objectives.Target) -> str:
            """Parses a Target object into a string message"""
            ...

    class NotificationEmail(System.Object):
        """Provides user-facing messages for the Notifications.NotificationEmail class and its consumers or related classes"""

        @staticmethod
        def invalid_email_address(email: str) -> str:
            """Returns a string message saying the given email is invalid"""
            ...

    class NotificationFtp(System.Object):
        """Provides user-facing messages for the Notifications.NotificationFtp class and its consumers or related classes"""

        missing_ssh_key: str = "FTP SSH key missing for SFTP notification."
        """String message saying the SSH key is missing"""

        missing_password: str = "FTP password is missing for unsecure FTP notification."
        """String message saying the password is missing"""

    class NotificationJsonConverter(System.Object):
        """Provides user-facing messages for the Notifications.NotificationJsonConverter class and its consumers or related classes"""

        write_not_implemented: str = "Not implemented, should not be called"
        """String message saying the write method has not been implemented and should not be called"""

        @staticmethod
        def unexpected_json_object(j_object: typing.Any) -> str:
            """String message saying the given object is unexpected"""
            ...

    class FuncBenchmark(System.Object):
        """Provides user-facing messages for the Benchmarks.FuncBenchmark class and its consumers or related classes"""

        unable_to_convert_python_function_to_benchmark_function: str = "Unable to convert Python function to benchmark function, please ensure the function supports Datetime input and decimal output"
        """String message saying it was impossible to convert the Python function to a benchmark function"""

    class BaseCommand(System.Object):
        """Provides user-facing messages for the Commands.BaseCommand class and its consumers or related classes"""

        missing_values_to_get_symbol: str = "Please provide values for: Ticker, Market & SecurityType"
        """Returns a string message saying: Please provide values for: Ticker, Market and SecurityType"""

    class BaseCommandHandler(System.Object):
        """Provides user-facing messages for the Commands.BaseCommandHandler class and its consumers or related classes"""

        @staticmethod
        def executing_command(command: QuantConnect.Commands.ICommand) -> str:
            """Returns a string with the given command"""
            ...

    class FileCommandHandler(System.Object):
        """Provides user-facing messages for the Commands.FileCommandHandler class and its consumers or related classes"""

        null_or_empty_command_id: str = "Command Id is null or empty, will skip writing result file"
        """Returns a string message saying: Command Id is null or empty, will skip writing result file"""

        @staticmethod
        def command_file_does_not_exist(command_file_path: str) -> str:
            """Returns a string message saying the given command_file_path does not exists"""
            ...

        @staticmethod
        def reading_command_file(command_file_path: str) -> str:
            """Returns a string message saying the given command_file_path is being read"""
            ...

    class OrderCommand(System.Object):
        """Provides user-facing messages for the Commands.OrderCommand class and its consumers or related classes"""

        @staticmethod
        def command_info(order_type: QuantConnect.Orders.OrderType, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], quantity: float, response: QuantConnect.Orders.OrderResponse) -> str:
            """
            Returns a string message with basic information about a command, such us:
            order type, symbol, quantity and response
            """
            ...

    class CancelOrderRequest(System.Object):
        """Provides user-facing messages for the Orders.CancelOrderRequest class and its consumers or related classes"""

        @staticmethod
        def to_string(request: QuantConnect.Orders.CancelOrderRequest) -> str:
            """Parses the given CancelOrderRequest into a string message containing basic information about it"""
            ...

    class GroupOrderExtensions(System.Object):
        """Provides user-facing messages for the Orders.GroupOrderExtensions class and its consumers or related classes"""

        @staticmethod
        def insufficient_buying_power_for_orders(securities: System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security], has_sufficient_buying_power_result: QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult) -> str:
            """Returns a string message saying there is insufficient buying power to complete the given orders"""
            ...

    class LimitIfTouchedOrder(System.Object):
        """Provides user-facing messages for the Orders.LimitIfTouchedOrder class and its consumers or related classes"""

        @staticmethod
        def tag(order: QuantConnect.Orders.LimitIfTouchedOrder) -> str:
            """Returns an empty string tag"""
            ...

        @staticmethod
        def to_string(order: QuantConnect.Orders.LimitIfTouchedOrder) -> str:
            """
            Parses the given LimitIfTouched order to a string message containing basic information
            about it
            """
            ...

    class LimitOrder(System.Object):
        """Provides user-facing messages for the Orders.LimitOrder class and its consumers or related classes"""

        @staticmethod
        def tag(order: QuantConnect.Orders.LimitOrder) -> str:
            """Returns an empty string tag"""
            ...

        @staticmethod
        def to_string(order: QuantConnect.Orders.LimitOrder) -> str:
            """Parses a Limit order to a string message with basic information about it"""
            ...

    class Order(System.Object):
        """Provides user-facing messages for the Orders.Order class and its consumers or related classes"""

        @staticmethod
        def to_string(order: QuantConnect.Orders.Order) -> str:
            """Parses the given order into a string message with basic information about it"""
            ...

    class OrderEvent(System.Object):
        """Provides user-facing messages for the Orders.OrderEvent class and its consumers or related classes"""

        @staticmethod
        def short_to_string(order_event: QuantConnect.Orders.OrderEvent) -> str:
            """Parses the given order event into a string message which summarizes the basic information about it"""
            ...

        @staticmethod
        def to_string(order_event: QuantConnect.Orders.OrderEvent) -> str:
            """Parses the given order event into a string message containing basic information about it"""
            ...

    class OrderRequest(System.Object):
        """Provides user-facing messages for the Orders.OrderRequest class and its consumers or related classes"""

        @staticmethod
        def to_string(request: QuantConnect.Orders.OrderRequest) -> str:
            """Parses the given order request into a string message containing basic information about it"""
            ...

    class OrderResponse(System.Object):
        """Provides user-facing messages for the Orders.OrderResponse class and its consumers or related classes"""

        default_error_message: str = "An unexpected error occurred."
        """String message saying: An unexpected error occurred"""

        unprocessed_order_response_error_message: str = "The request has not yet been processed."
        """String message saying: The request has not yet been processed"""

        @staticmethod
        def invalid_new_status(request: QuantConnect.Orders.OrderRequest, order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying it was impossible to update or cancel the order with the
            id from the given request because the submit confirmation had not been received yet
            """
            ...

        @staticmethod
        def invalid_status(request: QuantConnect.Orders.OrderRequest, order: QuantConnect.Orders.Order) -> str:
            """
            Returns a string message saying it was impossible to udpate the order with the id
            from the given request because it already had the status of the given order
            """
            ...

        @staticmethod
        def missing_security(request: QuantConnect.Orders.SubmitOrderRequest) -> str:
            """
            Returns a string message saying the user has not requested data for the symbol of the given
            request. It also advises the user on how to add this data
            
            :param request: 
            """
            ...

        @staticmethod
        def to_string(response: QuantConnect.Orders.OrderResponse) -> str:
            """Parses the given order response into a string message containing basic information about it"""
            ...

        @staticmethod
        def unable_to_find_order(request: QuantConnect.Orders.OrderRequest) -> str:
            """
            Returns a string message saying it was impossible to locate the order with the id from the
            given request
            """
            ...

        @staticmethod
        def warming_up(request: QuantConnect.Orders.OrderRequest) -> str:
            """
            Returns a string message saying the given order request operation is not allowed
            in Initialize or during warm up. It also advises the user on where it is allowed
            to make it
            """
            ...

        @staticmethod
        def zero_quantity(request: QuantConnect.Orders.OrderRequest) -> str:
            """
            Returns a string message saying it was impossible to process the given order request
            that has zero quantity
            """
            ...

    class OrderTicket(System.Object):
        """Provides user-facing messages for the Orders.OrderTicket class and its consumers or related classes"""

        @staticmethod
        def cancel_request_already_submitted(ticket: QuantConnect.Orders.OrderTicket) -> str:
            """
            Returns a string message saying the order associated with the given ticket has already received a
            cancellation request
            """
            ...

        @staticmethod
        def get_field_error(ticket: QuantConnect.Orders.OrderTicket, field: QuantConnect.Orders.OrderField) -> str:
            """
            Returns a string message saying it was impossible to get the given field on the order type from the given
            ticket
            """
            ...

        @staticmethod
        def to_string(ticket: QuantConnect.Orders.OrderTicket, order: QuantConnect.Orders.Order, request_count: int, response_count: int) -> str:
            """Parses the given order ticket into a string message containing basic information about it"""
            ...

    class StopLimitOrder(System.Object):
        """Provides user-facing messages for the Orders.StopLimitOrder class and its consumers or related classes"""

        @staticmethod
        def tag(order: QuantConnect.Orders.StopLimitOrder) -> str:
            """Returns an empty string as a tag"""
            ...

        @staticmethod
        def to_string(order: QuantConnect.Orders.StopLimitOrder) -> str:
            """Parses the given StopLimitOrder object into a string message"""
            ...

    class StopMarketOrder(System.Object):
        """Provides user-facing messages for the Orders.StopMarketOrder class and its consumers or related classes"""

        @staticmethod
        def tag(order: QuantConnect.Orders.StopMarketOrder) -> str:
            """Returns an empty string as a tag"""
            ...

        @staticmethod
        def to_string(order: QuantConnect.Orders.StopMarketOrder) -> str:
            """Parses a given StopMarketOrder object into a string message"""
            ...

    class TrailingStopOrder(System.Object):
        """Provides user-facing messages for the Orders.TrailingStopOrder class and its consumers or related classes"""

        @staticmethod
        def tag(order: QuantConnect.Orders.TrailingStopOrder) -> str:
            """Returns a tag message for the given TrailingStopOrder"""
            ...

        @staticmethod
        def to_string(order: QuantConnect.Orders.TrailingStopOrder) -> str:
            """Parses a TrailingStopOrder into a string"""
            ...

        @staticmethod
        @overload
        def trailing_amount(order: QuantConnect.Orders.TrailingStopOrder) -> str:
            """Returns a TrailingAmount string representation for the given TrailingStopOrder"""
            ...

        @staticmethod
        @overload
        def trailing_amount(trailing_amount: float, trailing_as_percentage: bool, price_currency: str) -> str:
            """Returns a message for the given TrailingAmount and PriceCurrency values taking into account if the trailing is as percentage"""
            ...

    class SubmitOrderRequest(System.Object):
        """Provides user-facing messages for the Orders.SubmitOrderRequest class and its consumers or related classes"""

        @staticmethod
        def to_string(request: QuantConnect.Orders.SubmitOrderRequest) -> str:
            """Parses a given SubmitOrderRequest object to a string message"""
            ...

    class UpdateOrderRequest(System.Object):
        """Provides user-facing messages for the Orders.UpdateOrderRequest class and its consumers or related classes"""

        @staticmethod
        def to_string(request: QuantConnect.Orders.UpdateOrderRequest) -> str:
            """Parses an UpdateOrderRequest to a string"""
            ...

    class PositionGroup(System.Object):
        """Provides user-facing messages for the Securities.Positions.PositionGroup class and its consumers or related classes"""

        @staticmethod
        def invalid_quantity(quantity: float, positions: typing.List[QuantConnect.Securities.Positions.IPosition]) -> str:
            """
            Returns a string message saying the given quantity is invalid. It also contains the quantities from the
            given positions as well as the unit quantities
            """
            ...

    class Insight(System.Object):
        """Provides user-facing messages for the Algorithm.Framework.Alphas.Insight class and its consumers or related classes"""

        invalid_bar_count: str = "Insight barCount must be greater than zero."
        """Returns a string message saying: Insight barCount must be grater than zero"""

        invalid_period: str = "Insight period must be greater than or equal to 1 second."
        """Returns a string message saying: Insight period must be greater than or equal to 1 second"""

        invalid_close_time_utc: str = "Insight closeTimeUtc must be greater than generatedTimeUtc."
        """Returns a string message saying: Insight closeTimeUtc must be greater than generatedTimeUtc"""

        invalid_close_time_local: str = "Insight closeTimeLocal must not be in the past."
        """Returns a string message saying: Insight closeTimeLocal must not be in the past"""

        @staticmethod
        def generated_time_utc_not_set(insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> str:
            """Returns a string message saying the Insight's GeneratedTimeUtc property must be set before calling SetPeriodAndCloseTime"""
            ...

        @staticmethod
        def insight_already_assigned_to_a_group(insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> str:
            """
            Returns a string message saying it was impossible to set group id on the given insight because it has already
            been assigned to a group
            """
            ...

        @staticmethod
        def short_to_string(insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> str:
            """Parses a short insight into a string containing basic information about it"""
            ...

        @staticmethod
        def to_string(insight: QuantConnect.Algorithm.Framework.Alphas.Insight) -> str:
            """Parses the given insight into a string containing basic information about it"""
            ...

    class InsightScore(System.Object):
        """Provides user-facing messages for the Algorithm.Framework.Alphas.InsightScore class and its consumers or related classes"""

        @staticmethod
        def to_string(insight_score: QuantConnect.Algorithm.Framework.Alphas.InsightScore) -> str:
            """Parses an InsightScore object into a string message containing basic information about it"""
            ...

    class DefaultExerciseModel(System.Object):
        """Provides user-facing messages for the Orders.OptionExercise.DefaultExerciseModel class and its consumers or related classes"""

        option_assignment: str = "Option Assignment"
        """String message saying: Option Assignment"""

        option_exercise: str = "Option Exercise"
        """String message saying: Option exercise"""

        @staticmethod
        def contract_holdings_adjustment_fill_tag(in_the_money: bool, is_assignment: bool, option: QuantConnect.Securities.Option.Option) -> str:
            """
            Returns a string message containing basic information such as if it's
            an assignment or an exercise, if it's ITM or OTM  and the underlying option price
            """
            ...

    class FillModel(System.Object):
        """Provides user-facing messages for the Orders.Fills.FillModel class and its consumers or related classes"""

        @staticmethod
        def filled_at_stale_price(security: QuantConnect.Securities.Security, prices: QuantConnect.Orders.Fills.Prices) -> str:
            """Returns a string message warning saying the order was filled at stale price"""
            ...

        @staticmethod
        def market_never_closes(security: QuantConnect.Securities.Security, order_type: QuantConnect.Orders.OrderType) -> str:
            """
            Returns a string message saying the market never closes for the given symbol, and that an order of the given
            type cannot be submitted
            """
            ...

        @staticmethod
        def no_data_subscription_found_for_filling(security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying it was impossible to perform a fill for the given security symbol because
            no data subscription was found
            """
            ...

        @staticmethod
        def no_market_data_to_get_ask_price_for_filling(security: QuantConnect.Securities.Security, subscribed_types: System.Collections.Generic.HashSet[typing.Type] = None) -> str:
            """
            Returns a string message saying it was impossible to get ask price to perform the fill for the given security symbol because
            no market data was found
            """
            ...

        @staticmethod
        def no_market_data_to_get_bid_price_for_filling(security: QuantConnect.Securities.Security, subscribed_types: System.Collections.Generic.HashSet[typing.Type] = None) -> str:
            """
            Returns a string message saying it was impossible to get bid price to perform the fill for the given security symbol because
            no market data was found
            """
            ...

    class EquityFillModel(System.Object):
        """Provides user-facing messages for the Orders.Fills.EquityFillModel class and its consumers or related classes"""

        market_on_open_fill_no_official_open_or_opening_prints_within_one_minute: str = "No trade with the OfficialOpen or OpeningPrints flag within the 1-minute timeout."
        """String message saying: No trade with the OfficialOpen or OpeningPrints flag within the 1-minute timeout"""

        market_on_close_fill_no_official_close_or_closing_prints_within_one_minute: str = "No trade with the OfficialClose or ClosingPrints flag within the 1-minute timeout."
        """String message saying: No trade with the OfficialClose or ClosingPrints flag within the 1-minute timeout"""

        market_on_close_fill_no_official_close_or_closing_prints_without_extended_market_hours: str = "No trade with the OfficialClose or ClosingPrints flag for data that does not include extended market hours."
        """
        String message saying: No trade with the OfficialClose or ClosingPrints flag for data that does not include
        extended market hours
        """

        @staticmethod
        def filled_with_last_tick_type_data(tick: QuantConnect.Data.Market.Tick) -> str:
            """Returns a string message saying the last data (of the given tick type) has been used to fill"""
            ...

        @staticmethod
        def filled_with_open_due_to_favorable_gap(security: QuantConnect.Securities.Security, trade_bar: QuantConnect.Data.Market.TradeBar) -> str:
            """Returns a string message saying that the order was filled using the open price due to a favorable gap"""
            ...

        @staticmethod
        def filled_with_open_due_to_unfavorable_gap(security: QuantConnect.Securities.Security, trade_bar: QuantConnect.Data.Market.TradeBar) -> str:
            """Returns a string message saying that the order was filled using the open price due to an unfavorable gap"""
            ...

        @staticmethod
        def filled_with_quote_bar_data(security: QuantConnect.Securities.Security, quote_bar: QuantConnect.Data.Market.QuoteBar) -> str:
            """
            Returns a string message warning the user that the fill was at stale price, so quote bar data
            was used to fill the order
            """
            ...

        @staticmethod
        def filled_with_quote_data(security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message warnning the user that no trade information was available, so the order was filled
            using quote data
            """
            ...

        @staticmethod
        def filled_with_quote_tick_data(security: QuantConnect.Securities.Security, quote_tick: QuantConnect.Data.Market.Tick) -> str:
            """
            Returns a string message warning the user that the fill is at stale price and that the order will
            be filled using quote tick data
            """
            ...

        @staticmethod
        def filled_with_trade_bar_data(security: QuantConnect.Securities.Security, trade_bar: QuantConnect.Data.Market.TradeBar) -> str:
            """
            Returns a string message warning the user that no quote information was available, so that trade bar
            data was used to fill the order
            """
            ...

        @staticmethod
        def filled_with_trade_tick_data(security: QuantConnect.Securities.Security, trade_tick: QuantConnect.Data.Market.Tick) -> str:
            """
            Returns a string message warning the user that no quote information was available, so the order
            was filled using trade tick data
            """
            ...

    class FeeModel(System.Object):
        """Provides user-facing messages for the Orders.Fees.FeeModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_security_type(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security is unsupported"""
            ...

    class AlphaStreamsFeeModel(System.Object):
        """Provides user-facing messages for the Orders.Fees.AlphaStreamsFeeModel class and its consumers or related classes"""

        @staticmethod
        def unexpected_equity_market(market: str) -> str:
            """Returns a string message saying the given market is unexpected"""
            ...

    class ExanteFeeModel(System.Object):
        """Provides user-facing messages for the Orders.Fees.ExanteFeeModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_exchange(order: QuantConnect.Orders.Order) -> str:
            """Returns a string message saying the market associated with the given order symbol is unsupported"""
            ...

    class InteractiveBrokersFeeModel(System.Object):
        """Provides user-facing messages for the Orders.Fees.InteractiveBrokersFeeModel class and its consumers or related classes"""

        @staticmethod
        def eurex_future_fees_unsupported_security_type(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security was unsupported"""
            ...

        @staticmethod
        def hong_kong_future_fees_unexpected_quote_currency(security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying the quote currency of the given security was
            unexpected for Hong Kong futures exchange
            """
            ...

        @staticmethod
        def unexpected_equity_market(market: str) -> str:
            """Returns a string message saying the given equity market was unexpected"""
            ...

        @staticmethod
        def unexpected_future_market(market: str) -> str:
            """Returns a string message saying the given future market was unexpected"""
            ...

        @staticmethod
        def unexpected_option_market(market: str) -> str:
            """Returns a string message saying the given option market was unexpected"""
            ...

        @staticmethod
        def united_states_future_fees_unsupported_security_type(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security was unsupported"""
            ...

    class TDAmeritradeFeeModel(System.Object):
        """Provides user-facing messages for the Orders.Fees.TDAmeritradeFeeModel class and its consumers or related classes"""

        @staticmethod
        def unsupported_security_type(security_type: QuantConnect.SecurityType) -> str:
            """Returns a string message for unsupported security types in TDAmeritradeFeeModel"""
            ...

    class PortfolioTarget(System.Object):
        """Provides user-facing messages for the Algorithm.Framework.Portfolio.PortfolioTarget class and its consumers or related classes"""

        @staticmethod
        def invalid_insight_direction(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], insight_direction: QuantConnect.Algorithm.Framework.Alphas.InsightDirection) -> str:
            """Returns a string message saying the insight direction is invalid for the given symbol"""
            ...

        @staticmethod
        def invalid_target_percent(algorithm: QuantConnect.Interfaces.IAlgorithm, percent: float) -> str:
            """Returns a string message saying the portfolio target percent is invalid"""
            ...

        @staticmethod
        def symbol_not_found(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """Returns a string message saying the given symbol was not found in the portfolio"""
            ...

        @staticmethod
        def to_string(portfolio_target: QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget) -> str:
            """Parses the given portfolio target into a string message containing basic information about it"""
            ...

        @staticmethod
        def unable_to_compute_order_quantity_due_to_null_result(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], result: QuantConnect.Securities.Positions.GetMaximumLotsResult) -> str:
            """
            Returns a string message saying it was impossible to compute the order quantity of the given symbol. It also
            explains the reason why it was impossible
            """
            ...

    class AccountEvent(System.Object):
        """Provides user-facing messages for the Securities.AccountEvent class and its consumers or related classes"""

        @staticmethod
        def to_string(account_event: QuantConnect.Securities.AccountEvent) -> str:
            """Returns a string message containing basic information about the given account_event"""
            ...

    class BuyingPowerModel(System.Object):
        """Provides user-facing messages for the Securities.BuyingPowerModel class and its consumers or related classes"""

        invalid_initial_margin_requirement: str = "Initial margin requirement must be between 0 and 1"
        """String message saying: Initial margin requirement must be between 0 and 1"""

        invalid_maintenance_margin_requirement: str = "Maintenance margin requirement must be between 0 and 1"
        """String messsage saying: Maintenance margin requirement must be between 0 and 1"""

        invalid_free_buying_power_percent_requirement: str = "Free Buying Power Percent requirement must be between 0 and 1"
        """String message saying: Free Buying Power Percent requirement must be between 0 and 1"""

        invalid_leverage: str = "Leverage must be greater than or equal to 1."
        """String message saying: Leverage must be greater than or equal to 1"""

        @staticmethod
        def failed_to_converge_on_the_target_margin(parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters, signed_target_final_margin_value: float, order_fees: float) -> str:
            """
            Returns a string message saying GetMaximumOrderQuantityForTargetBuyingPower failed to converge on the target margin.
            It also contains useful information to reproduce the issue
            """
            ...

        @staticmethod
        def failed_to_converge_on_the_target_margin_underlying_security_info(underlying: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message containing basic information related with the underlying security such as the price,
            the holdings and the average price of them
            """
            ...

        @staticmethod
        def insufficient_buying_power_due_to_null_order_ticket(order: QuantConnect.Orders.Order) -> str:
            """Returns a string message saying the order associated with the id of the given order is null"""
            ...

        @staticmethod
        def insufficient_buying_power_due_to_unsufficient_margin(order: QuantConnect.Orders.Order, initial_margin_required_for_remainder_of_order: float, free_margin: float) -> str:
            """
            Returns a string mesage containing information about the order ID, the initial margin and
            the free margin
            """
            ...

        @staticmethod
        def margin_being_adjusted_in_the_wrong_direction(target_margin: float, margin_for_one_unit: float, security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying the margin is being adjusted in the wrong direction. It also provides useful information to
            reproduce the issue
            """
            ...

        @staticmethod
        def margin_being_adjusted_in_the_wrong_direction_underlying_security_info(underlying: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message containing basic information related with the underlying security such as the price,
            the holdings and the average price of them
            """
            ...

        @staticmethod
        def order_quantity_less_than_lot_size(security: QuantConnect.Securities.Security, target_order_margin: float) -> str:
            """
            Returns a string message saying that the order quantity is less that the lot size of the given security
            and that it has been rounded to zero
            """
            ...

        @staticmethod
        @overload
        def target_order_margin_not_above_minimum(abs_difference_of_margin: float, minimum_value: float) -> str:
            """Returns a string message saying the given target order margin is less than the given minimum value"""
            ...

        @staticmethod
        @overload
        def target_order_margin_not_above_minimum() -> str:
            """
            Returns a string message warning the user that the Portfolio rebalance result ignored as it resulted in
            a single share trade recommendation which can generate high fees.
            """
            ...

    class PositionGroupBuyingPowerModel(System.Object):
        """Provides user-facing messages for the Securities.Positions.PositionGroupBuyingPowerModel class and its consumers or related classes"""

        delta_cannot_be_applied: str = "No buying power used, delta cannot be applied"
        """String message saying: No buying power used, delta cannot be applied"""

        @staticmethod
        def computed_zero_initial_margin(position_group: QuantConnect.Securities.Positions.IPositionGroup) -> str:
            """
            Returns a string message saying the zero initial margin requirement was computed
            for the given position group
            """
            ...

        @staticmethod
        def failed_to_converge_on_target_margin(target_margin: float, position_group_quantity: float, order_fees: float, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> str:
            """Returns a string message saying the process to converge on the given target margin failed"""
            ...

        @staticmethod
        def position_group_quantity_rounded_to_zero(target_order_margin: float) -> str:
            """Returns a string message saying the position group order quantity has been rounded to zero"""
            ...

    class Cash(System.Object):
        """Provides user-facing messages for the Securities.Cash class and its consumers or related classes"""

        null_or_empty_cash_symbol: str = "Cash symbols cannot be null or empty."
        """String message saying: Cash symbols cannot be null or empty"""

        @staticmethod
        def adding_security_symbol_for_cash_currency_feed(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security], cash_currency_symbol: str) -> str:
            """
            Returns a string message saying the security symbol is being added for cash currency feed (this comes from the
            given cash currency symbol)
            """
            ...

        @staticmethod
        def no_tradable_pair_found_for_currency_conversion(cash_currency_symbol: str, account_currency: str, market_map: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.SecurityType, str]]) -> str:
            """
            Returns a string message saying no tradeable pair was found for the given currency symbol. It also mentions
            that the given account currency will be set to zero
            """
            ...

        @staticmethod
        def to_string(cash: QuantConnect.Securities.Cash, account_currency: str) -> str:
            """Parses the given Cash object into a string containing basic information about it"""
            ...

    class CashBook(System.Object):
        """Provides user-facing messages for the Securities.CashBook class and its consumers or related classes"""

        unexpected_request_for_null_currency: str = "Unexpected request for NullCurrency Cash instance"
        """String message saying: Unexpected request for NullCurrency Cash instance"""

        @staticmethod
        def cash_symbol_not_found(symbol: str) -> str:
            """Returns a string message saying the given cash symbol was not found"""
            ...

        @staticmethod
        def conversion_rate_not_found(currency: str) -> str:
            """Returns a string message saying the conversion rate for the given currency is not available"""
            ...

        @staticmethod
        def failed_to_remove_record(symbol: str) -> str:
            """
            Returns a string message saying it was impossible to remove the cash book record
            for the given symbol
            """
            ...

        @staticmethod
        def to_string(cash_book: QuantConnect.Securities.CashBook) -> str:
            """Parses the given CashBook into a string mesage with basic information about it"""
            ...

    class CashBuyingPowerModel(System.Object):
        """Provides user-facing messages for the Securities.CashBuyingPowerModel class and its consumers or related classes"""

        unsupported_leverage: str = "CashBuyingPowerModel does not allow setting leverage. Cash accounts have no leverage."
        """String message saying: CashBuyingPowerModel does not allow setting leverage. Cash accounts have no leverage"""

        get_maximum_order_quantity_for_delta_buying_power_not_implemented: str = ...
        """String message saying: The CashBuyingPowerModel does not require GetMaximumOrderQuantityForDeltaBuyingPower"""

        shorting_not_supported: str = "The cash model does not allow shorting."
        """String message saying: The cash model does not allow shorting"""

        invalid_security: str = ...
        """String message saying: The security type must be Crypto or Forex"""

        @staticmethod
        def buy_order_quantity_greater_than_max_for_buying_power(total_quantity: float, maximum_quantity: float, open_orders_reserved_quantity: float, order_quantity: float, base_currency: QuantConnect.Securities.IBaseCurrencySymbol, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> str:
            """Returns a string message containing the portfolio holdings, the buy order and the maximum buying power"""
            ...

        @staticmethod
        def failed_to_converge_on_target_order_value(target_order_value: float, current_order_value: float, order_quantity: float, order_fees: float, security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying GetMaximumOrderQuantityForTargetBuyingPower failed to converge to
            the given target order value
            """
            ...

        @staticmethod
        def no_data_in_internal_cash_feed_yet(security: QuantConnect.Securities.Security, portfolio: QuantConnect.Securities.SecurityPortfolioManager) -> str:
            """
            Returns a string message saying the internal cash feed required for converting the quote currency, from the given security,
            to the target account currency, from the given portfolio, does not have any data
            """
            ...

        @staticmethod
        def order_quantity_less_than_lot_size(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the order quantity is less than the lot size for the given security"""
            ...

        @staticmethod
        def order_quantity_less_than_lot_size_order_details(target_order_value: float, order_quantity: float, order_fees: float) -> str:
            """
            Returns a string message containing information about the target order value, the order fees and
            the order quantity
            """
            ...

        @staticmethod
        def sell_order_short_holdings_not_supported(total_quantity: float, open_orders_reserved_quantity: float, order_quantity: float, base_currency: QuantConnect.Securities.IBaseCurrencySymbol) -> str:
            """
            Returns a string message saying Cash Modeling trading does not permit short holdings as well as portfolio
            holdings and an advise to ensure the user is selling only what it has
            """
            ...

        @staticmethod
        def unsupported_security(security: QuantConnect.Securities.Security) -> str:
            """
            Returns a string message saying: The security is not supported by this cash model. It also mentioned that
            currently just crypt and forex securities are supported
            """
            ...

        @staticmethod
        def zero_contract_multiplier(security: QuantConnect.Securities.Security) -> str:
            """Returns a string mesasge saying the contract multiplier for the given security is zero"""
            ...

    class DefaultMarginCallModel(System.Object):
        """Provides user-facing messages for the Securities.DefaultMarginCallModel class and its consumers or related classes"""

        margin_call_order_tag: str = "Margin Call"
        """String message saying: Margin Call"""

    class DynamicSecurityData(System.Object):
        """Provides user-facing messages for the Securities.DynamicSecurityData class and its consumers or related classes"""

        properties_cannot_be_set: str = "DynamicSecurityData is a view of the SecurityCache. It is readonly, properties can not be set"
        """String message saying: DynamicSecurityData is a view of the SecurityCache. It is readonly, properties can not bet set"""

        @staticmethod
        def property_not_found(name: str) -> str:
            """Returns a string message saying no property exists with the given name"""
            ...

        @staticmethod
        def unexpected_types_for_get_all(type: typing.Type, data: typing.Any) -> str:
            """Returns a string message saying a list of the given type was expected but the one found was of the given data type"""
            ...

    class EquityPriceVariationModel(System.Object):
        """Provides user-facing messages for the Securities.EquityPriceVariationModel class and its consumers or related classes"""

        @staticmethod
        def invalid_security_type(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying the type of the given security was invalid"""
            ...

    class ErrorCurrencyConverter(System.Object):
        """Provides user-facing messages for the Securities.ErrorCurrencyConverter class and its consumers or related classes"""

        account_currency_unexpected_usage: str = "Unexpected usage of ErrorCurrencyConverter.AccountCurrency"
        """String message saying: Unexpected usage of ErrorCurrencyConverter.AccountCurrency"""

        convert_to_account_currency_purposefully_throw: str = ...
        """String message saying: This method purposefully throws as a proof that a test does not depend on a currency converter"""

    class FuncSecuritySeeder(System.Object):
        """Provides user-facing messages for the Securities.FuncSecuritySeeder class and its consumers or related classes"""

        @staticmethod
        def seeded_security_info(seed_data: QuantConnect.Data.BaseData) -> str:
            """Returns a string message with basic information about the given BaseData object"""
            ...

        @staticmethod
        def unable_to_security_price(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying it was impossible to seed price for the given security"""
            ...

        @staticmethod
        def unable_to_seed_security(security: QuantConnect.Securities.Security) -> str:
            """Returns a string message saying it was impossible to seed the given security"""
            ...

    class IdentityCurrencyConverter(System.Object):
        """Provides user-facing messages for the Securities.IdentityCurrencyConverter class and its consumers or related classes"""

        unable_to_handle_cash_in_non_account_currency: str = ...
        """String message saying: The IdentityCurrencyConverter can only handle CashAmounts in units of the account currency"""

    class InitialMarginParameters(System.Object):
        """Provides user-facing messages for the Securities.InitialMarginParameters class and its consumers or related classes"""

        for_underlying_only_invokable_for_i_derivative_security: str = "ForUnderlying is only invokable for IDerivativeSecurity (Option|Future)"
        """String message saying: ForUnderlying is only invokable for IDerivativeSecurity (Option|Future)"""

    class LocalMarketHours(System.Object):
        """Provides user-facing messages for the Securities.LocalMarketHours class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.Securities.LocalMarketHours) -> str:
            """Parses the given LocalMarketHours object into a string message containing basic information about it"""
            ...

    class MaintenanceMarginParameters(System.Object):
        """Provides user-facing messages for the Securities.MaintenanceMarginParameters class and its consumers or related classes"""

        for_underlying_only_invokable_for_i_derivative_security: str = "ForUnderlying is only invokable for IDerivativeSecurity (Option|Future)"
        """String message saying: ForUnderlying is only invokable for IDerivativeSecurity"""

    class MarketHoursDatabase(System.Object):
        """Provides user-facing messages for the Securities.MarketHoursDatabase class and its consumers or related classes"""

        future_usa_market_type_no_longer_supported: str = ...
        """String message saying: Future.Usa market type is no longer supported as we mapped each ticker to its actual exchange"""

        @staticmethod
        def exchange_hours_not_found(key: QuantConnect.Securities.SecurityDatabaseKey, available_keys: typing.List[QuantConnect.Securities.SecurityDatabaseKey] = None) -> str:
            """
            Returns a string message saying it was impossible to locate exchange hours for the given key. It also
            mentiones the available keys
            """
            ...

        @staticmethod
        def suggested_market_based_on_ticker(market: str) -> str:
            """Returns a string message that suggests the given market based on the provided ticker"""
            ...

    class MarketHoursSegment(System.Object):
        """Provides user-facing messages for the Securities.MarketHoursSegment class and its consumers or related classes"""

        invalid_extended_market_open_time: str = "Extended market open time must be less than or equal to market open time."
        """String message saying: Extended market open time must be less than or equal to market open time"""

        invalid_market_close_time: str = "Market close time must be after market open time."
        """String message saying: Market close time must be after market open time"""

        invalid_extended_market_close_time: str = "Extended market close time must be greater than or equal to market close time."
        """String message saying: Extended market close time must be greater than or equal to market close time"""

        @staticmethod
        def to_string(instance: QuantConnect.Securities.MarketHoursSegment) -> str:
            """Parses a MarketHourSegment object into a string message containing basic information about it"""
            ...

    class RegisteredSecurityDataTypesProvider(System.Object):
        """Provides user-facing messages for the Securities.RegisteredSecurityDataTypesProvider class and its consumers or related classes"""

        @staticmethod
        def two_different_types_detected_for_the_same_type_name(type: typing.Type, existing_type: typing.Type) -> str:
            """
            Returns a string message saying two different types were detected trying to register the same type name. It also
            mentions the two different types
            """
            ...

    class Security(System.Object):
        """Provides user-facing messages for the Securities.Security class and its consumers or related classes"""

        valid_symbol_properties_instance_required: str = "Security requires a valid SymbolProperties instance."
        """String message saying: Security requires a valid SymbolProperties instance"""

        unmatching_quote_currencies: str = "symbolProperties.QuoteCurrency must match the quoteCurrency.Symbol"
        """String message saying: symbolProperties.QuoteCurrency must match the quoteCurrency.Symbol"""

        set_local_time_keeper_must_be_called_before_using_local_time: str = "Security.SetLocalTimeKeeper(LocalTimeKeeper) must be called in order to use the LocalTime property."
        """String message saying: Security.SetLocalTimeKeeper(LocalTimeKeeper) must be called in order to use the LocalTime property"""

        unmatching_symbols: str = "Symbols must match."
        """String message saying: Symbols must match"""

        unmatching_exchange_time_zones: str = "ExchangeTimeZones must match."
        """String message saying: ExchangeTimeZones must match"""

    class SecurityDatabaseKey(System.Object):
        """Provides user-facing messages for the Securities.SecurityDatabaseKey class and its consumers or related classes"""

        @staticmethod
        def key_not_in_expected_format(key: str) -> str:
            """Returns a string message saying the specified and given key was not in the expected format"""
            ...

        @staticmethod
        def to_string(instance: QuantConnect.Securities.SecurityDatabaseKey) -> str:
            """Parses a SecurityDatabaseKey into a string message with basic information about it"""
            ...

    class SecurityDefinitionSymbolResolver(System.Object):
        """Provides user-facing messages for the Securities.SecurityDefinitionSymbolResolver class and its consumers or related classes"""

        @staticmethod
        def no_security_definitions_loaded(securities_definition_key: str) -> str:
            """Returns a string message saying no security definitions data have been loaded from the given file"""
            ...

    class SecurityExchangeHours(System.Object):
        """Provides user-facing messages for the Securities.SecurityExchangeHours class and its consumers or related classes"""

        @staticmethod
        def last_market_open_not_found(local_date_time: typing.Union[datetime.datetime, datetime.date], is_market_always_open: bool) -> str:
            """
            Returns a string message saying it did not find last market open for the given local date time. It also mentions
            if the market is always open or not
            """
            ...

        @staticmethod
        def unable_to_locate_next_market_close_in_two_weeks(is_market_always_open: bool) -> str:
            """
            Returns an error message when the next market close could not be located within two weeks.
            Includes additional guidance if the market is always open (e.g., crypto assets).
            """
            ...

        @staticmethod
        def unable_to_locate_next_market_open_in_two_weeks(is_market_always_open: bool) -> str:
            """
            Returns an error message when the next market open could not be located within two weeks.
            Includes additional guidance if the market is always open (e.g., crypto assets).
            """
            ...

    class SecurityHolding(System.Object):
        """Provides user-facing messages for the Securities.SecurityHolding class and its consumers or related classes"""

        @staticmethod
        def to_string(instance: QuantConnect.Securities.SecurityHolding) -> str:
            """Parses the given SecurityHolding object into a string message containing basic information about it"""
            ...

    class SecurityManager(System.Object):
        """Provides user-facing messages for the Securities.SecurityManager class and its consumers or related classes"""

        @staticmethod
        def symbol_not_found_in_securities(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """Returns a string message saying the given symbol was not found in the user security list"""
            ...

        @staticmethod
        def unable_to_overwrite_security(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """Returns a string message saying the given symbol could not be overwritten"""
            ...

    class SecurityPortfolioManager(System.Object):
        """Provides user-facing messages for the Securities.SecurityPortfolioManager class and its consumers or related classes"""

        dictionary_add_not_implemented: str = "Portfolio object is an adaptor for Security Manager. To add a new asset add the required data during initialization."
        """
        Returns a string message saying Portfolio object is an adaptor for Security Manager and that to add a new asset
        the required data should added during initialization
        """

        dictionary_clear_not_implemented: str = "Portfolio object is an adaptor for Security Manager and cannot be cleared."
        """Returns a string message saying the Portfolio object object is an adaptor for Security Manager and cannot be cleared"""

        dictionary_remove_not_implemented: str = "Portfolio object is an adaptor for Security Manager and objects cannot be removed."
        """Returns a string message saying the Portfolio object is an adaptor for Security Manager and objects cannot be removed"""

        cannot_change_account_currency_after_adding_security: str = "Cannot change AccountCurrency after adding a Security. Please move SetAccountCurrency() before AddSecurity()."
        """
        Returns a string message saying the AccountCurrency cannot be changed after adding a Security and that the method
        SetAccountCurrency() should be moved before AddSecurity()
        """

        cannot_change_account_currency_after_setting_cash: str = "Cannot change AccountCurrency after setting cash. Please move SetAccountCurrency() before SetCash()."
        """
        Returns a string message saying the AccountCurrency cannot be changed after setting cash and that the method
        SetAccountCurrency() should be moved before SetCash()
        """

        @staticmethod
        def account_currency_already_set(cash_book: QuantConnect.Securities.CashBook, new_account_currency: str) -> str:
            """
            Returns a string message saying the AccountCurrency has already been set and that the new value for this property
            will be ignored
            """
            ...

        @staticmethod
        def order_request_margin_information(margin_used: float, margin_remaining: float) -> str:
            """Returns a string message saying the order request margin information, this is, the margin used and the margin remaining"""
            ...

        @staticmethod
        def setting_account_currency(account_currency: str) -> str:
            """Returns a string message saying the AccountCurrency is being set to the given account currency"""
            ...

        @staticmethod
        def total_margin_information(total_margin_used: float, margin_remaining: float) -> str:
            """
            Returns a string message saying the total margin information, this is, the total margin used as well as the
            margin remaining
            """
            ...

    class SecurityService(System.Object):
        """Provides user-facing messages for the Securities.SecurityService class and its consumers or related classes"""

        @staticmethod
        def symbol_not_found_in_symbol_properties_database(symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> str:
            """Returns a string message saying the given Symbol could not be found in the Symbol Properties Database"""
            ...

    class SecurityTransactionManager(System.Object):
        """Provides user-facing messages for the Securities.SecurityTransactionManager class and its consumers or related classes"""

        cancel_open_orders_not_allowed_on_initialize_or_warm_up: str = "This operation is not allowed in Initialize or during warm up: CancelOpenOrders. Please move this code to the OnWarmupFinished() method."
        """Returns a string message saying CancelOpenOrders operation is not allowed in Initialize or during warm up"""

        @staticmethod
        def order_canceled_by_cancel_open_orders(time: typing.Union[datetime.datetime, datetime.date]) -> str:
            """Returns a string message saying the order was canceled by the CancelOpenOrders() at the given time"""
            ...

        @staticmethod
        def order_not_filled_within_expected_time(fill_timeout: datetime.timedelta) -> str:
            """Returns a string message saying the order did not fill within the given amount of seconds"""
            ...

        @staticmethod
        def unable_to_locate_order_ticket(order_id: int) -> str:
            """Returns a string message saying the ticket for the given order ID could not be localized"""
            ...

    class SymbolProperties(System.Object):
        """Provides user-facing messages for the Securities.SymbolProperties class and its consumers or related classes"""

        invalid_lot_size: str = "SymbolProperties LotSize can not be less than or equal to 0"
        """String message saying the SymbolProperties LotSize can not be less than or equal to 0"""

        invalid_price_magnifier: str = "SymbolProprties PriceMagnifier can not be less than or equal to 0"
        """String message saying the SymbolProperties PriceMagnifier can not be less than or equal to 0"""

        invalid_strike_multiplier: str = "SymbolProperties StrikeMultiplier can not be less than or equal to 0"
        """String message saying the SymbolProperties StrikeMultiplier can not be less than or equal to 0"""

        @staticmethod
        def to_string(instance: QuantConnect.Securities.SymbolProperties) -> str:
            """Parses a given SymbolProperties object into a string message"""
            ...

    class SymbolPropertiesDatabase(System.Object):
        """Provides user-facing messages for the Securities.SymbolPropertiesDatabase class and its consumers or related classes"""

        @staticmethod
        def database_file_not_found(file: str) -> str:
            """Returns a string saying the given symbol properties file could not be localized"""
            ...

        @staticmethod
        def duplicate_key_in_file(file: str, key: QuantConnect.Securities.SecurityDatabaseKey) -> str:
            """Returns a string saying a duplicated key was found while processing the given file"""
            ...


class _EventContainer(typing.Generic[QuantConnect__EventContainer_Callable, QuantConnect__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


