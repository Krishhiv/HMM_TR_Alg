from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.DownloaderDataProvider.Launcher.Models
import System


class BaseDataDownloadConfig(System.Object, metaclass=abc.ABCMeta):
    """Abstract base class for configuring data download parameters, including common properties and initialization logic."""

    @property
    def start_date(self) -> datetime.datetime:
        """Gets the start date for the data download."""
        ...

    @start_date.setter
    def start_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """Gets the end date for the data download."""
        ...

    @end_date.setter
    def end_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Gets or sets the resolution of the downloaded data."""
        ...

    @resolution.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def market_name(self) -> str:
        """Gets or sets the market name for which the data will be downloaded."""
        ...

    @market_name.setter
    def market_name(self, value: str) -> None:
        ...

    @property
    def security_type(self) -> QuantConnect.SecurityType:
        """Gets the type of security for which the data is being downloaded."""
        ...

    @security_type.setter
    def security_type(self, value: QuantConnect.SecurityType) -> None:
        ...

    @property
    def tick_type(self) -> QuantConnect.TickType:
        """Gets or sets the type of tick data to be downloaded."""
        ...

    @tick_type.setter
    def tick_type(self, value: QuantConnect.TickType) -> None:
        ...

    @property
    @abc.abstractmethod
    def data_type(self) -> typing.Type:
        """The type of data based on TickTypes"""
        ...

    @property
    def symbols(self) -> typing.Sequence[QuantConnect.Symbol]:
        """Gets the list of symbols for which the data will be downloaded."""
        ...

    @symbols.setter
    def symbols(self, value: typing.Sequence[QuantConnect.Symbol]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the BaseDataDownloadConfig class.
        
        
        This codeEntityType is protected.
        """
        ...

    @overload
    def __init__(self, tick_type: QuantConnect.TickType, security_type: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, start_date: typing.Union[datetime.datetime, datetime.date], end_date: typing.Union[datetime.datetime, datetime.date], market_name: str, symbols: typing.List[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the DataDownloadConfig class with the specified parameters.
        
        
        This codeEntityType is protected.
        
        :param tick_type: The type of tick data to be downloaded.
        :param security_type: The type of security for which data is being downloaded.
        :param resolution: The resolution of the data being downloaded.
        :param start_date: The start date for the data download range.
        :param end_date: The end date for the data download range.
        :param market_name: The name of the market from which the data is being downloaded.
        :param symbols: A list of symbols for which data is being downloaded.
        """
        ...

    @staticmethod
    def parse_date(date: str) -> datetime.datetime:
        """
        Parses a string to a DateTime using a specific date format.
        
        
        This codeEntityType is protected.
        
        :param date: The date string to parse.
        :returns: The parsed DateTime value.
        """
        ...


class BrokerageDataDownloader(System.Object, QuantConnect.IDataDownloader, System.IDisposable):
    """Class for downloading data from a brokerage."""

    def __init__(self) -> None:
        """Initializes a new instance of the BrokerageDataDownloader class."""
        ...

    def dispose(self) -> None:
        ...

    def get(self, data_downloader_get_parameters: QuantConnect.DataDownloaderGetParameters) -> typing.Iterable[QuantConnect.Data.BaseData]:
        """
        Get historical data enumerable for a single symbol, type and resolution given this start and end time (in UTC).
        
        :param data_downloader_get_parameters: model class for passing in parameters for historical data
        :returns: Enumerable of base data for this symbol.
        """
        ...


class DataUniverseDownloadConfig(QuantConnect.DownloaderDataProvider.Launcher.Models.BaseDataDownloadConfig):
    """Represents the configuration for downloading data for a universe of securities."""

    @property
    def data_type(self) -> typing.Type:
        """Gets the type of data universe download."""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the DataUniverseDownloadConfig class using configuration settings."""
        ...


class DataDownloadConfig(QuantConnect.DownloaderDataProvider.Launcher.Models.BaseDataDownloadConfig):
    """Represents the configuration for downloading data."""

    @property
    def data_type(self) -> typing.Type:
        """Gets the type of data download."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the DataDownloadConfig class."""
        ...

    @overload
    def __init__(self, tick_type: QuantConnect.TickType, security_type: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, start_date: typing.Union[datetime.datetime, datetime.date], end_date: typing.Union[datetime.datetime, datetime.date], market_name: str, symbols: typing.List[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the DataDownloadConfig class with the specified parameters.
        
        :param tick_type: The type of tick data to be downloaded.
        :param security_type: The type of security for which data is being downloaded.
        :param resolution: The resolution of the data being downloaded.
        :param start_date: The start date for the data download range.
        :param end_date: The end date for the data download range.
        :param market_name: The name of the market from which the data is being downloaded.
        :param symbols: A list of symbols for which data is being downloaded.
        """
        ...


