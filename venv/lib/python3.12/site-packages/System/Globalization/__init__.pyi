from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Globalization
import System.Reflection
import System.Runtime.Serialization
import System.Text

System_Globalization_SortVersion = typing.Any


class SortVersion(System.Object, System.IEquatable[System_Globalization_SortVersion]):
    """This class has no documentation."""

    @property
    def full_version(self) -> int:
        ...

    @property
    def sort_id(self) -> System.Guid:
        ...

    def __eq__(self, right: System.Globalization.SortVersion) -> bool:
        ...

    def __init__(self, full_version: int, sort_id: System.Guid) -> None:
        ...

    def __ne__(self, right: System.Globalization.SortVersion) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Globalization.SortVersion) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CompareOptions(IntEnum):
    """This class has no documentation."""

    NONE = ...

    IGNORE_CASE = ...

    IGNORE_NON_SPACE = ...

    IGNORE_SYMBOLS = ...

    IGNORE_KANA_TYPE = ...

    IGNORE_WIDTH = ...

    NUMERIC_ORDERING = ...

    ORDINAL_IGNORE_CASE = ...

    STRING_SORT = ...

    ORDINAL = ...


class SortKey(System.Object):
    """This class has no documentation."""

    @property
    def original_string(self) -> str:
        ...

    @property
    def key_data(self) -> typing.List[int]:
        ...

    @staticmethod
    def compare(sortkey_1: System.Globalization.SortKey, sortkey_2: System.Globalization.SortKey) -> int:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CompareInfo(System.Object, System.Runtime.Serialization.IDeserializationCallback):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def version(self) -> System.Globalization.SortVersion:
        ...

    @property
    def lcid(self) -> int:
        ...

    @overload
    def compare(self, string_1: str, string_2: str) -> int:
        ...

    @overload
    def compare(self, string_1: str, string_2: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, length_1: int, string_2: str, offset_2: int, length_2: int) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, string_2: str, offset_2: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, string_2: str, offset_2: int) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, length_1: int, string_2: str, offset_2: int, length_2: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: System.ReadOnlySpan[str], string_2: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def get_compare_info(culture: int, assembly: System.Reflection.Assembly) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @overload
    def get_compare_info(name: str, assembly: System.Reflection.Assembly) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @overload
    def get_compare_info(culture: int) -> System.Globalization.CompareInfo:
        ...

    @staticmethod
    @overload
    def get_compare_info(name: str) -> System.Globalization.CompareInfo:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    @overload
    def get_hash_code(self, source: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def get_hash_code(self, source: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def get_sort_key(self, source: str, options: System.Globalization.CompareOptions) -> System.Globalization.SortKey:
        ...

    @overload
    def get_sort_key(self, source: str) -> System.Globalization.SortKey:
        ...

    @overload
    def get_sort_key(self, source: System.ReadOnlySpan[str], destination: System.Span[int], options: System.Globalization.CompareOptions = ...) -> int:
        ...

    def get_sort_key_length(self, source: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, count: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: System.Globalization.CompareOptions = ...) -> int:
        ...

    @overload
    def is_prefix(self, source: str, prefix: str, options: System.Globalization.CompareOptions) -> bool:
        ...

    @overload
    def is_prefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> bool:
        ...

    @overload
    def is_prefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def is_prefix(self, source: str, prefix: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(ch: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(text: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(text: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(value: System.Text.Rune) -> bool:
        ...

    @overload
    def is_suffix(self, source: str, suffix: str, options: System.Globalization.CompareOptions) -> bool:
        ...

    @overload
    def is_suffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> bool:
        ...

    @overload
    def is_suffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def is_suffix(self, source: str, suffix: str) -> bool:
        ...

    @overload
    def last_index_of(self, source: str, value: str) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, count: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: System.Globalization.CompareOptions = ...) -> int:
        ...

    def to_string(self) -> str:
        ...


class TextInfo(System.Object, System.ICloneable, System.Runtime.Serialization.IDeserializationCallback):
    """This class has no documentation."""

    @property
    def ansi_code_page(self) -> int:
        ...

    @property
    def oem_code_page(self) -> int:
        ...

    @property
    def mac_code_page(self) -> int:
        ...

    @property
    def ebcdic_code_page(self) -> int:
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def culture_name(self) -> str:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def list_separator(self) -> str:
        ...

    @list_separator.setter
    def list_separator(self, value: str) -> None:
        ...

    @property
    def is_right_to_left(self) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def read_only(text_info: System.Globalization.TextInfo) -> System.Globalization.TextInfo:
        ...

    @overload
    def to_lower(self, c: str) -> str:
        ...

    @overload
    def to_lower(self, str: str) -> str:
        ...

    @overload
    def to_lower(self, value: System.Text.Rune) -> System.Text.Rune:
        ...

    def to_string(self) -> str:
        ...

    def to_title_case(self, str: str) -> str:
        ...

    @overload
    def to_upper(self, c: str) -> str:
        ...

    @overload
    def to_upper(self, str: str) -> str:
        ...

    @overload
    def to_upper(self, value: System.Text.Rune) -> System.Text.Rune:
        ...


class CultureTypes(IntEnum):
    """This class has no documentation."""

    NEUTRAL_CULTURES = ...

    SPECIFIC_CULTURES = ...

    INSTALLED_WIN_32_CULTURES = ...

    ALL_CULTURES = ...

    USER_CUSTOM_CULTURE = ...

    REPLACEMENT_CULTURES = ...

    WINDOWS_ONLY_CULTURES = ...

    FRAMEWORK_CULTURES = ...


class DigitShapes(IntEnum):
    """This class has no documentation."""

    CONTEXT = ...

    NONE = ...

    NATIVE_NATIONAL = ...


class NumberFormatInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """This class has no documentation."""

    INVARIANT_INFO: System.Globalization.NumberFormatInfo

    @property
    def currency_decimal_digits(self) -> int:
        ...

    @currency_decimal_digits.setter
    def currency_decimal_digits(self, value: int) -> None:
        ...

    @property
    def currency_decimal_separator(self) -> str:
        ...

    @currency_decimal_separator.setter
    def currency_decimal_separator(self, value: str) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def currency_group_sizes(self) -> typing.List[int]:
        ...

    @currency_group_sizes.setter
    def currency_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def number_group_sizes(self) -> typing.List[int]:
        ...

    @number_group_sizes.setter
    def number_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def percent_group_sizes(self) -> typing.List[int]:
        ...

    @percent_group_sizes.setter
    def percent_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def currency_group_separator(self) -> str:
        ...

    @currency_group_separator.setter
    def currency_group_separator(self, value: str) -> None:
        ...

    @property
    def currency_symbol(self) -> str:
        ...

    @currency_symbol.setter
    def currency_symbol(self, value: str) -> None:
        ...

    CURRENT_INFO: System.Globalization.NumberFormatInfo

    @property
    def na_n_symbol(self) -> str:
        ...

    @na_n_symbol.setter
    def na_n_symbol(self, value: str) -> None:
        ...

    @property
    def currency_negative_pattern(self) -> int:
        ...

    @currency_negative_pattern.setter
    def currency_negative_pattern(self, value: int) -> None:
        ...

    @property
    def number_negative_pattern(self) -> int:
        ...

    @number_negative_pattern.setter
    def number_negative_pattern(self, value: int) -> None:
        ...

    @property
    def percent_positive_pattern(self) -> int:
        ...

    @percent_positive_pattern.setter
    def percent_positive_pattern(self, value: int) -> None:
        ...

    @property
    def percent_negative_pattern(self) -> int:
        ...

    @percent_negative_pattern.setter
    def percent_negative_pattern(self, value: int) -> None:
        ...

    @property
    def negative_infinity_symbol(self) -> str:
        ...

    @negative_infinity_symbol.setter
    def negative_infinity_symbol(self, value: str) -> None:
        ...

    @property
    def negative_sign(self) -> str:
        ...

    @negative_sign.setter
    def negative_sign(self, value: str) -> None:
        ...

    @property
    def number_decimal_digits(self) -> int:
        ...

    @number_decimal_digits.setter
    def number_decimal_digits(self, value: int) -> None:
        ...

    @property
    def number_decimal_separator(self) -> str:
        ...

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: str) -> None:
        ...

    @property
    def number_group_separator(self) -> str:
        ...

    @number_group_separator.setter
    def number_group_separator(self, value: str) -> None:
        ...

    @property
    def currency_positive_pattern(self) -> int:
        ...

    @currency_positive_pattern.setter
    def currency_positive_pattern(self, value: int) -> None:
        ...

    @property
    def positive_infinity_symbol(self) -> str:
        ...

    @positive_infinity_symbol.setter
    def positive_infinity_symbol(self, value: str) -> None:
        ...

    @property
    def positive_sign(self) -> str:
        ...

    @positive_sign.setter
    def positive_sign(self, value: str) -> None:
        ...

    @property
    def percent_decimal_digits(self) -> int:
        ...

    @percent_decimal_digits.setter
    def percent_decimal_digits(self, value: int) -> None:
        ...

    @property
    def percent_decimal_separator(self) -> str:
        ...

    @percent_decimal_separator.setter
    def percent_decimal_separator(self, value: str) -> None:
        ...

    @property
    def percent_group_separator(self) -> str:
        ...

    @percent_group_separator.setter
    def percent_group_separator(self, value: str) -> None:
        ...

    @property
    def percent_symbol(self) -> str:
        ...

    @percent_symbol.setter
    def percent_symbol(self, value: str) -> None:
        ...

    @property
    def per_mille_symbol(self) -> str:
        ...

    @per_mille_symbol.setter
    def per_mille_symbol(self, value: str) -> None:
        ...

    @property
    def native_digits(self) -> typing.List[str]:
        ...

    @native_digits.setter
    def native_digits(self, value: typing.List[str]) -> None:
        ...

    @property
    def digit_substitution(self) -> System.Globalization.DigitShapes:
        ...

    @digit_substitution.setter
    def digit_substitution(self, value: System.Globalization.DigitShapes) -> None:
        ...

    def __init__(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_instance(format_provider: System.IFormatProvider) -> System.Globalization.NumberFormatInfo:
        ...

    @staticmethod
    def read_only(nfi: System.Globalization.NumberFormatInfo) -> System.Globalization.NumberFormatInfo:
        ...


class CalendarAlgorithmType(IntEnum):
    """This class has no documentation."""

    UNKNOWN = 0

    SOLAR_CALENDAR = 1

    LUNAR_CALENDAR = 2

    LUNISOLAR_CALENDAR = 3


class CalendarWeekRule(IntEnum):
    """This class has no documentation."""

    FIRST_DAY = 0

    FIRST_FULL_WEEK = 1

    FIRST_FOUR_DAY_WEEK = 2


class Calendar(System.Object, System.ICloneable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    CURRENT_ERA: int = 0

    @property
    @abc.abstractmethod
    def eras(self) -> typing.List[int]:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_days(self, time: typing.Union[datetime.datetime, datetime.date], days: int) -> datetime.datetime:
        ...

    def add_hours(self, time: typing.Union[datetime.datetime, datetime.date], hours: int) -> datetime.datetime:
        ...

    def add_milliseconds(self, time: typing.Union[datetime.datetime, datetime.date], milliseconds: float) -> datetime.datetime:
        ...

    def add_minutes(self, time: typing.Union[datetime.datetime, datetime.date], minutes: int) -> datetime.datetime:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_seconds(self, time: typing.Union[datetime.datetime, datetime.date], seconds: int) -> datetime.datetime:
        ...

    def add_weeks(self, time: typing.Union[datetime.datetime, datetime.date], weeks: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def clone(self) -> System.Object:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def get_days_in_month(self, year: int, month: int) -> int:
        ...

    @overload
    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    @overload
    def get_days_in_year(self, year: int) -> int:
        ...

    @overload
    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_hour(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def get_leap_month(self, year: int) -> int:
        ...

    @overload
    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_milliseconds(self, time: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    def get_minute(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def get_months_in_year(self, year: int) -> int:
        ...

    @overload
    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_second(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def is_leap_day(self, year: int, month: int, day: int) -> bool:
        ...

    @overload
    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    @overload
    def is_leap_month(self, year: int, month: int) -> bool:
        ...

    @overload
    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    @overload
    def is_leap_year(self, year: int) -> bool:
        ...

    @overload
    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    @staticmethod
    def read_only(calendar: System.Globalization.Calendar) -> System.Globalization.Calendar:
        ...

    @overload
    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> datetime.datetime:
        ...

    @overload
    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class DateTimeFormatInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """This class has no documentation."""

    INVARIANT_INFO: System.Globalization.DateTimeFormatInfo

    CURRENT_INFO: System.Globalization.DateTimeFormatInfo

    @property
    def am_designator(self) -> str:
        ...

    @am_designator.setter
    def am_designator(self, value: str) -> None:
        ...

    @property
    def calendar(self) -> System.Globalization.Calendar:
        ...

    @calendar.setter
    def calendar(self, value: System.Globalization.Calendar) -> None:
        ...

    @property
    def date_separator(self) -> str:
        ...

    @date_separator.setter
    def date_separator(self, value: str) -> None:
        ...

    @property
    def first_day_of_week(self) -> System.DayOfWeek:
        ...

    @first_day_of_week.setter
    def first_day_of_week(self, value: System.DayOfWeek) -> None:
        ...

    @property
    def calendar_week_rule(self) -> System.Globalization.CalendarWeekRule:
        ...

    @calendar_week_rule.setter
    def calendar_week_rule(self, value: System.Globalization.CalendarWeekRule) -> None:
        ...

    @property
    def full_date_time_pattern(self) -> str:
        ...

    @full_date_time_pattern.setter
    def full_date_time_pattern(self, value: str) -> None:
        ...

    @property
    def long_date_pattern(self) -> str:
        ...

    @long_date_pattern.setter
    def long_date_pattern(self, value: str) -> None:
        ...

    @property
    def long_time_pattern(self) -> str:
        ...

    @long_time_pattern.setter
    def long_time_pattern(self, value: str) -> None:
        ...

    @property
    def month_day_pattern(self) -> str:
        ...

    @month_day_pattern.setter
    def month_day_pattern(self, value: str) -> None:
        ...

    @property
    def pm_designator(self) -> str:
        ...

    @pm_designator.setter
    def pm_designator(self, value: str) -> None:
        ...

    @property
    def rfc_1123_pattern(self) -> str:
        ...

    @property
    def short_date_pattern(self) -> str:
        ...

    @short_date_pattern.setter
    def short_date_pattern(self, value: str) -> None:
        ...

    @property
    def short_time_pattern(self) -> str:
        ...

    @short_time_pattern.setter
    def short_time_pattern(self, value: str) -> None:
        ...

    @property
    def sortable_date_time_pattern(self) -> str:
        ...

    @property
    def time_separator(self) -> str:
        ...

    @time_separator.setter
    def time_separator(self, value: str) -> None:
        ...

    @property
    def universal_sortable_date_time_pattern(self) -> str:
        ...

    @property
    def year_month_pattern(self) -> str:
        ...

    @year_month_pattern.setter
    def year_month_pattern(self, value: str) -> None:
        ...

    @property
    def abbreviated_day_names(self) -> typing.List[str]:
        ...

    @abbreviated_day_names.setter
    def abbreviated_day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def shortest_day_names(self) -> typing.List[str]:
        ...

    @shortest_day_names.setter
    def shortest_day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def day_names(self) -> typing.List[str]:
        ...

    @day_names.setter
    def day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def abbreviated_month_names(self) -> typing.List[str]:
        ...

    @abbreviated_month_names.setter
    def abbreviated_month_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def month_names(self) -> typing.List[str]:
        ...

    @month_names.setter
    def month_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def native_calendar_name(self) -> str:
        ...

    @property
    def abbreviated_month_genitive_names(self) -> typing.List[str]:
        ...

    @abbreviated_month_genitive_names.setter
    def abbreviated_month_genitive_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def month_genitive_names(self) -> typing.List[str]:
        ...

    @month_genitive_names.setter
    def month_genitive_names(self, value: typing.List[str]) -> None:
        ...

    def __init__(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_abbreviated_day_name(self, dayofweek: System.DayOfWeek) -> str:
        ...

    def get_abbreviated_era_name(self, era: int) -> str:
        ...

    def get_abbreviated_month_name(self, month: int) -> str:
        ...

    @overload
    def get_all_date_time_patterns(self) -> typing.List[str]:
        ...

    @overload
    def get_all_date_time_patterns(self, format: str) -> typing.List[str]:
        ...

    def get_day_name(self, dayofweek: System.DayOfWeek) -> str:
        ...

    def get_era(self, era_name: str) -> int:
        ...

    def get_era_name(self, era: int) -> str:
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_instance(provider: System.IFormatProvider) -> System.Globalization.DateTimeFormatInfo:
        ...

    def get_month_name(self, month: int) -> str:
        ...

    def get_shortest_day_name(self, day_of_week: System.DayOfWeek) -> str:
        ...

    @staticmethod
    def read_only(dtfi: System.Globalization.DateTimeFormatInfo) -> System.Globalization.DateTimeFormatInfo:
        ...

    def set_all_date_time_patterns(self, patterns: typing.List[str], format: str) -> None:
        ...


class CultureInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """This class has no documentation."""

    current_culture: System.Globalization.CultureInfo

    current_ui_culture: System.Globalization.CultureInfo

    INSTALLED_UI_CULTURE: System.Globalization.CultureInfo

    default_thread_current_culture: System.Globalization.CultureInfo

    default_thread_current_ui_culture: System.Globalization.CultureInfo

    INVARIANT_CULTURE: System.Globalization.CultureInfo

    @property
    def parent(self) -> System.Globalization.CultureInfo:
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def keyboard_layout_id(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def ietf_language_tag(self) -> str:
        ...

    @property
    def display_name(self) -> str:
        ...

    @property
    def native_name(self) -> str:
        ...

    @property
    def english_name(self) -> str:
        ...

    @property
    def two_letter_iso_language_name(self) -> str:
        ...

    @property
    def three_letter_iso_language_name(self) -> str:
        ...

    @property
    def three_letter_windows_language_name(self) -> str:
        ...

    @property
    def compare_info(self) -> System.Globalization.CompareInfo:
        ...

    @property
    def text_info(self) -> System.Globalization.TextInfo:
        ...

    @property
    def is_neutral_culture(self) -> bool:
        ...

    @property
    def culture_types(self) -> System.Globalization.CultureTypes:
        ...

    @property
    def number_format(self) -> System.Globalization.NumberFormatInfo:
        ...

    @number_format.setter
    def number_format(self, value: System.Globalization.NumberFormatInfo) -> None:
        ...

    @property
    def date_time_format(self) -> System.Globalization.DateTimeFormatInfo:
        ...

    @date_time_format.setter
    def date_time_format(self, value: System.Globalization.DateTimeFormatInfo) -> None:
        ...

    @property
    def calendar(self) -> System.Globalization.Calendar:
        ...

    @property
    def optional_calendars(self) -> typing.List[System.Globalization.Calendar]:
        ...

    @property
    def use_user_override(self) -> bool:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, use_user_override: bool) -> None:
        ...

    @overload
    def __init__(self, culture: int) -> None:
        ...

    @overload
    def __init__(self, culture: int, use_user_override: bool) -> None:
        ...

    def clear_cached_data(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    def create_specific_culture(name: str) -> System.Globalization.CultureInfo:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_console_fallback_ui_culture(self) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @overload
    def get_culture_info(culture: int) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str, alt_name: str) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str, predefined_only: bool) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def get_culture_info_by_ietf_language_tag(name: str) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def get_cultures(types: System.Globalization.CultureTypes) -> typing.List[System.Globalization.CultureInfo]:
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def read_only(ci: System.Globalization.CultureInfo) -> System.Globalization.CultureInfo:
        ...

    def to_string(self) -> str:
        ...


class GlobalizationExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_string_comparer(compare_info: System.Globalization.CompareInfo, options: System.Globalization.CompareOptions) -> System.StringComparer:
        ...


class TimeSpanStyles(IntEnum):
    """This class has no documentation."""

    NONE = ...

    ASSUME_NEGATIVE = ...


class KoreanCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    KOREAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class UmAlQuraCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    UM_AL_QURA_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class CultureNotFoundException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def invalid_culture_id(self) -> typing.Optional[int]:
        ...

    @property
    def invalid_culture_name(self) -> str:
        ...

    @property
    def message(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, invalid_culture_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, invalid_culture_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, invalid_culture_id: int, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, invalid_culture_id: int, message: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class JulianCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    JULIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class JapaneseCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class ISOWeek(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def get_week_of_year(date: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def get_week_of_year(date: System.DateOnly) -> int:
        ...

    @staticmethod
    def get_weeks_in_year(year: int) -> int:
        ...

    @staticmethod
    @overload
    def get_year(date: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def get_year(date: System.DateOnly) -> int:
        ...

    @staticmethod
    def get_year_end(year: int) -> datetime.datetime:
        ...

    @staticmethod
    def get_year_start(year: int) -> datetime.datetime:
        ...

    @staticmethod
    def to_date_only(year: int, week: int, day_of_week: System.DayOfWeek) -> System.DateOnly:
        ...

    @staticmethod
    def to_date_time(year: int, week: int, day_of_week: System.DayOfWeek) -> datetime.datetime:
        ...


class TaiwanCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class GregorianCalendarTypes(IntEnum):
    """This class has no documentation."""

    LOCALIZED = ...

    US_ENGLISH = ...

    MIDDLE_EAST_FRENCH = ...

    ARABIC = ...

    TRANSLITERATED_ENGLISH = ...

    TRANSLITERATED_FRENCH = ...


class GregorianCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    AD_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def calendar_type(self) -> System.Globalization.GregorianCalendarTypes:
        ...

    @calendar_type.setter
    def calendar_type(self, value: System.Globalization.GregorianCalendarTypes) -> None:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, type: System.Globalization.GregorianCalendarTypes) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class UnicodeCategory(IntEnum):
    """This class has no documentation."""

    UPPERCASE_LETTER = 0

    LOWERCASE_LETTER = 1

    TITLECASE_LETTER = 2

    MODIFIER_LETTER = 3

    OTHER_LETTER = 4

    NON_SPACING_MARK = 5

    SPACING_COMBINING_MARK = 6

    ENCLOSING_MARK = 7

    DECIMAL_DIGIT_NUMBER = 8

    LETTER_NUMBER = 9

    OTHER_NUMBER = 10

    SPACE_SEPARATOR = 11

    LINE_SEPARATOR = 12

    PARAGRAPH_SEPARATOR = 13

    CONTROL = 14

    FORMAT = 15

    SURROGATE = 16

    PRIVATE_USE = 17

    CONNECTOR_PUNCTUATION = 18

    DASH_PUNCTUATION = 19

    OPEN_PUNCTUATION = 20

    CLOSE_PUNCTUATION = 21

    INITIAL_QUOTE_PUNCTUATION = 22

    FINAL_QUOTE_PUNCTUATION = 23

    OTHER_PUNCTUATION = 24

    MATH_SYMBOL = 25

    CURRENCY_SYMBOL = 26

    MODIFIER_SYMBOL = 27

    OTHER_SYMBOL = 28

    OTHER_NOT_ASSIGNED = 29


class CharUnicodeInfo(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def get_decimal_digit_value(ch: str) -> int:
        ...

    @staticmethod
    @overload
    def get_decimal_digit_value(s: str, index: int) -> int:
        ...

    @staticmethod
    @overload
    def get_digit_value(ch: str) -> int:
        ...

    @staticmethod
    @overload
    def get_digit_value(s: str, index: int) -> int:
        ...

    @staticmethod
    @overload
    def get_numeric_value(ch: str) -> float:
        ...

    @staticmethod
    @overload
    def get_numeric_value(s: str, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_unicode_category(ch: str) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(code_point: int) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(s: str, index: int) -> System.Globalization.UnicodeCategory:
        ...


class IdnMapping(System.Object):
    """This class has no documentation."""

    @property
    def allow_unassigned(self) -> bool:
        ...

    @allow_unassigned.setter
    def allow_unassigned(self, value: bool) -> None:
        ...

    @property
    def use_std_3_ascii_rules(self) -> bool:
        ...

    @use_std_3_ascii_rules.setter
    def use_std_3_ascii_rules(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def get_ascii(self, unicode: str) -> str:
        ...

    @overload
    def get_ascii(self, unicode: str, index: int) -> str:
        ...

    @overload
    def get_ascii(self, unicode: str, index: int, count: int) -> str:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_unicode(self, ascii: str) -> str:
        ...

    @overload
    def get_unicode(self, ascii: str, index: int) -> str:
        ...

    @overload
    def get_unicode(self, ascii: str, index: int, count: int) -> str:
        ...


class DaylightTime(System.Object):
    """This class has no documentation."""

    @property
    def start(self) -> datetime.datetime:
        ...

    @property
    def end(self) -> datetime.datetime:
        ...

    @property
    def delta(self) -> datetime.timedelta:
        ...

    def __init__(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], delta: datetime.timedelta) -> None:
        ...


class HijriCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    HIJRI_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def hijri_adjustment(self) -> int:
        ...

    @hijri_adjustment.setter
    def hijri_adjustment(self, value: int) -> None:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class EastAsianLunisolarCalendar(System.Globalization.Calendar, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_celestial_stem(self, sexagenary_year: int) -> int:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_sexagenary_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_terrestrial_branch(self, sexagenary_year: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class TaiwanLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class JapaneseLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    JAPANESE_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class RegionInfo(System.Object):
    """This class has no documentation."""

    CURRENT_REGION: System.Globalization.RegionInfo

    @property
    def name(self) -> str:
        ...

    @property
    def english_name(self) -> str:
        ...

    @property
    def display_name(self) -> str:
        ...

    @property
    def native_name(self) -> str:
        ...

    @property
    def two_letter_iso_region_name(self) -> str:
        ...

    @property
    def three_letter_iso_region_name(self) -> str:
        ...

    @property
    def three_letter_windows_region_name(self) -> str:
        ...

    @property
    def is_metric(self) -> bool:
        ...

    @property
    def geo_id(self) -> int:
        ...

    @property
    def currency_english_name(self) -> str:
        ...

    @property
    def currency_native_name(self) -> str:
        ...

    @property
    def currency_symbol(self) -> str:
        ...

    @property
    def iso_currency_symbol(self) -> str:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, culture: int) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class ThaiBuddhistCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    THAI_BUDDHIST_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class NumberStyles(IntEnum):
    """This class has no documentation."""

    NONE = ...

    ALLOW_LEADING_WHITE = ...

    ALLOW_TRAILING_WHITE = ...

    ALLOW_LEADING_SIGN = ...

    ALLOW_TRAILING_SIGN = ...

    ALLOW_PARENTHESES = ...

    ALLOW_DECIMAL_POINT = ...

    ALLOW_THOUSANDS = ...

    ALLOW_EXPONENT = ...

    ALLOW_CURRENCY_SYMBOL = ...

    ALLOW_HEX_SPECIFIER = ...

    ALLOW_BINARY_SPECIFIER = ...

    INTEGER = ...

    HEX_NUMBER = ...

    BINARY_NUMBER = ...

    NUMBER = ...

    FLOAT = ...

    CURRENCY = ...

    ANY = ...


class KoreanLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    GREGORIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class PersianCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    PERSIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class ChineseLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    CHINESE_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class HebrewCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    HEBREW_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class DateTimeStyles(IntEnum):
    """This class has no documentation."""

    NONE = ...

    ALLOW_LEADING_WHITE = ...

    ALLOW_TRAILING_WHITE = ...

    ALLOW_INNER_WHITE = ...

    ALLOW_WHITE_SPACES = ...

    NO_CURRENT_DATE_DEFAULT = ...

    ADJUST_TO_UNIVERSAL = ...

    ASSUME_LOCAL = ...

    ASSUME_UNIVERSAL = ...

    ROUNDTRIP_KIND = ...


class TextElementEnumerator(System.Object, System.Collections.IEnumerator):
    """This class has no documentation."""

    @property
    def current(self) -> System.Object:
        ...

    @property
    def element_index(self) -> int:
        ...

    def get_text_element(self) -> str:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class StringInfo(System.Object):
    """This class has no documentation."""

    @property
    def string(self) -> str:
        ...

    @string.setter
    def string(self, value: str) -> None:
        ...

    @property
    def length_in_text_elements(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_next_text_element(str: str) -> str:
        ...

    @staticmethod
    @overload
    def get_next_text_element(str: str, index: int) -> str:
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: str) -> int:
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: str, index: int) -> int:
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: System.ReadOnlySpan[str]) -> int:
        ...

    @staticmethod
    @overload
    def get_text_element_enumerator(str: str) -> System.Globalization.TextElementEnumerator:
        ...

    @staticmethod
    @overload
    def get_text_element_enumerator(str: str, index: int) -> System.Globalization.TextElementEnumerator:
        ...

    @staticmethod
    def parse_combining_characters(str: str) -> typing.List[int]:
        ...

    @overload
    def substring_by_text_elements(self, starting_text_element: int) -> str:
        ...

    @overload
    def substring_by_text_elements(self, starting_text_element: int, length_in_text_elements: int) -> str:
        ...


