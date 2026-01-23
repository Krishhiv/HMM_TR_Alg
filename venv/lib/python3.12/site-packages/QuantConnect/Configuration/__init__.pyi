from typing import overload
from enum import IntEnum
import typing

import QuantConnect.Configuration
import System
import System.Collections.Generic


class ReportArgumentParser(System.Object):
    """Command Line arguments parser for Report Creator"""

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Parse and construct the args."""
        ...


class ToolboxArgumentParser(System.Object):
    """Command Line arguments parser for Toolbox configuration"""

    @staticmethod
    def get_tickers(options_object: System.Collections.Generic.Dictionary[str, System.Object]) -> typing.List[str]:
        """Helper method to get the tickers from the provided options"""
        ...

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Argument parser contructor"""
        ...


class Config(System.Object):
    """Configuration class loads the required external setup variables to launch the Lean engine."""

    @staticmethod
    @overload
    def flatten(config: typing.Any, override_environment: str) -> typing.Any:
        """
        Flattens the jobject with respect to the selected environment and then
        removes the 'environments' node
        
        :param config: The configuration represented as a JObject
        :param override_environment: The environment to use
        :returns: The flattened JObject.
        """
        ...

    @staticmethod
    @overload
    def flatten(override_environment: str) -> typing.Any:
        """
        Flattens the jobject with respect to the selected environment and then
        removes the 'environments' node
        
        :param override_environment: The environment to use
        :returns: The flattened JObject.
        """
        ...

    @staticmethod
    def get(key: str, default_value: str = ...) -> str:
        """
        Get the matching config setting from the file searching for this key.
        
        :param key: String key value we're seaching for in the config file.
        :param default_value: 
        :returns: String value of the configuration setting or empty string if nothing found.
        """
        ...

    @staticmethod
    def get_bool(key: str, default_value: bool = False) -> bool:
        """
        Get a boolean value configuration setting by a configuration key.
        
        :param key: String value of the configuration key.
        :param default_value: The default value to use if not found in configuration
        :returns: Boolean value of the config setting.
        """
        ...

    @staticmethod
    def get_double(key: str, default_value: float = 0.0) -> float:
        """
        Get the double value of a config string.
        
        :param key: Search key from the config file
        :param default_value: The default value to use if not found in configuration
        :returns: Double value of the config setting.
        """
        ...

    @staticmethod
    def get_environment() -> str:
        """
        Gets the currently selected environment. If sub-environments are defined,
        they'll be returned as {env1}.{env2}
        
        :returns: The fully qualified currently selected environment.
        """
        ...

    @staticmethod
    def get_int(key: str, default_value: int = 0) -> int:
        """
        Get the int value of a config string.
        
        :param key: Search key from the config file
        :param default_value: The default value to use if not found in configuration
        :returns: Int value of the config setting.
        """
        ...

    @staticmethod
    def get_token(key: str) -> typing.Any:
        """Gets the underlying JToken for the specified key"""
        ...

    @staticmethod
    def merge_command_line_arguments_with_configuration(cli_arguments: System.Collections.Generic.Dictionary[str, System.Object]) -> None:
        """
        Merge CLI arguments with configuration file + load custom config file via CLI arg
        
        :param cli_arguments: 
        """
        ...

    @staticmethod
    def reset() -> None:
        """
        Resets the config settings to their default values.
        Called in regression tests where multiple algorithms are run sequentially,
        and we need to guarantee that every test starts with the same configuration.
        """
        ...

    @staticmethod
    def set(key: str, value: typing.Any) -> None:
        """
        Sets a configuration value. This is really only used to help testing. The key heye can be
        specified as {environment}.key to set a value on a specific environment
        
        :param key: The key to be set
        :param value: The new value
        """
        ...

    @staticmethod
    def set_configuration_file(file_name: str) -> None:
        """
        Set configuration file on-fly
        
        :param file_name: 
        """
        ...

    @staticmethod
    def write(target_path: str = None) -> None:
        """Write the contents of the serialized configuration back to the disk."""
        ...


class OptimizerArgumentParser(System.Object):
    """Command Line arguments parser for Lean Optimizer"""

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Parse and construct the args"""
        ...


class CommandLineOption(System.Object):
    """Auxiliary class to keep information about a specific command line option"""

    @property
    def type(self) -> typing.Any:
        """Command line option type"""
        ...

    @property
    def description(self) -> str:
        """Command line option description"""
        ...

    @property
    def name(self) -> str:
        """Command line option name"""
        ...

    def __init__(self, name: str, type: typing.Any, description: str = ...) -> None:
        """Command line option contructor"""
        ...


class LeanArgumentParser(System.Object):
    """Command Line arguments parser for Lean configuration"""

    @staticmethod
    def parse_arguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Argument parser contructor"""
        ...


class ApplicationParser(System.Object):
    """Command Line application parser"""

    @staticmethod
    def get_parameter_or_default(options_object: System.Collections.Generic.IReadOnlyDictionary[str, System.Object], parameter: str, default_value: str) -> str:
        """Gets the parameter object from the given parameter. If it does not exists, it returns a default parameter object"""
        ...

    @staticmethod
    def get_parameter_or_exit(options_object: System.Collections.Generic.IReadOnlyDictionary[str, System.Object], parameter: str) -> str:
        """Gets the parameter object from the given parameter (if it exists)"""
        ...

    @staticmethod
    def parse(application_name: str, application_description: str, application_help_text: str, args: typing.List[str], options: typing.List[QuantConnect.Configuration.CommandLineOption], no_args_show_help: bool = False) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """
        This function will parse args based on options and will show application name, version, help
        
        :param application_name: The application name to be shown
        :param application_description: The application description to be shown
        :param application_help_text: The application help text
        :param args: The command line arguments
        :param options: The applications command line available options
        :param no_args_show_help: To show help when no command line arguments were provided
        :returns: The user provided options. Key is option name.
        """
        ...

    @staticmethod
    def print_message_and_exit(exit_code: int = 0, message: str = ...) -> None:
        """Prints a message advising the user to use the --help parameter for more information"""
        ...


