from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.DownloaderDataProvider.Launcher
import QuantConnect.DownloaderDataProvider.Launcher.Models
import QuantConnect.Interfaces
import System
import System.Collections.Generic


class DownloaderDataProviderArgumentParser(System.Object):
    """This class has no documentation."""

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """
        Parses the command-line arguments and returns a dictionary containing parsed values.
        
        :param args: An array of command-line arguments.
        :returns: A dictionary containing parsed values from the command-line arguments.
        """
        ...


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def initialize_configurations() -> None:
        """
        Initializes various configurations for the application.
        This method sets up logging, data providers, map file providers, and factor file providers.
        """
        ...

    @staticmethod
    def main(args: typing.List[str]) -> None:
        """
        The main entry point for the application.
        
        :param args: Command-line arguments passed to the application.
        """
        ...

    @staticmethod
    def run_download(data_downloader: QuantConnect.IDataDownloader, data_download_config: QuantConnect.DownloaderDataProvider.Launcher.Models.DataDownloadConfig, data_directory: str, data_cache_provider: QuantConnect.Interfaces.IDataCacheProvider, map_symbol: bool = True) -> None:
        """
        Executes a data download operation using the specified data downloader.
        
        :param data_downloader: An instance of an object implementing the IDataDownloader interface, responsible for downloading data.
        :param data_download_config: Configuration settings for the data download operation.
        :param data_directory: The directory where the downloaded data will be stored.
        :param data_cache_provider: The provider used to cache history data files
        :param map_symbol: True if the symbol should be mapped while writing the data
        """
        ...


