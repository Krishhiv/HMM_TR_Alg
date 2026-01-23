from typing import overload
from enum import IntEnum
import datetime
import typing

import QuantConnect
import QuantConnect.AlgorithmFactory
import QuantConnect.Interfaces
import QuantConnect.Util
import System
import System.Reflection


class Loader(System.MarshalByRefObject):
    """Loader creates and manages the memory and exception space of the algorithm, ensuring if it explodes the Lean Engine is intact."""

    @property
    def app_domain(self) -> System.AppDomain:
        """Memory space of the user algorithm"""
        ...

    @app_domain.setter
    def app_domain(self, value: System.AppDomain) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new loader with a 10 second maximum load time that forces exactly one derived type to be found"""
        ...

    @overload
    def __init__(self, debugging: bool, language: QuantConnect.Language, loader_time_limit: datetime.timedelta, multiple_type_name_resolver_function: typing.Callable[[typing.List[str]], str], worker_thread: QuantConnect.Util.WorkerThread = None) -> None:
        """
        Creates a new loader with the specified configuration
        
        :param debugging: True if we are debugging
        :param language: Which language are we trying to load
        :param loader_time_limit: Used to limit how long it takes to create a new instance
        :param multiple_type_name_resolver_function: Used to resolve multiple type names found in assembly to a single type name, if null, defaults to names => names.SingleOrDefault()
        
        When we search an assembly for derived types of IAlgorithm, sometimes the assembly will contain multiple matching types. This is the case
        for the QuantConnect.Algorithm assembly in this solution.  In order to pick the correct type, consumers must specify how to pick the type,
        that's what this function does, it picks the correct type from the list of types found within the assembly.
        :param worker_thread: The worker thread instance the loader should use
        """
        ...

    @staticmethod
    def get_extended_type_names(assembly: System.Reflection.Assembly) -> typing.List[str]:
        """
        Get a list of all the matching type names in this DLL assembly:
        
        :param assembly: Assembly dll we're loading.
        :returns: String list of types available.
        """
        ...

    def try_create_algorithm_instance(self, assembly_path: str, algorithm_instance: typing.Optional[QuantConnect.Interfaces.IAlgorithm], error_message: typing.Optional[str]) -> typing.Tuple[bool, QuantConnect.Interfaces.IAlgorithm, str]:
        """
        Creates a new instance of the specified class in the library, safely.
        
        :param assembly_path: Location of the DLL
        :param algorithm_instance: Output algorithm instance
        :param error_message: Output error message on failure
        :returns: Bool true on successfully loading the class.
        """
        ...

    def try_create_algorithm_instance_with_isolator(self, assembly_path: str, ram_limit: int, algorithm_instance: typing.Optional[QuantConnect.Interfaces.IAlgorithm], error_message: typing.Optional[str]) -> typing.Tuple[bool, QuantConnect.Interfaces.IAlgorithm, str]:
        """
        Creates a new instance of the class in the library, safely.
        
        :param assembly_path: Location of the DLL
        :param ram_limit: Limit of the RAM for this process
        :param algorithm_instance: Output algorithm instance
        :param error_message: Output error message on failure
        :returns: bool success.
        """
        ...

    def unload(self) -> None:
        ...


class DebuggerHelper(System.Object):
    """Helper class used to start a new debugging session"""

    class DebuggingMethod(IntEnum):
        """The different implemented debugging methods"""

        LOCAL_CMDLINE = 0
        """
        Local debugging through cmdline.
        Language.PYTHON will use built in 'pdb'
        """

        VISUAL_STUDIO = 1
        """
        Visual studio local debugging.
        Language.PYTHON will use 'Python Tools for Visual Studio',
        attach manually selecting `Python` code type.
        """

        PTVSD = 2
        """
        Python Tool for Visual Studio Debugger for remote python debugging.
        Language.PYTHON. Deprecated, routes to DebugPy which
        is it's replacement. Used in the same way.
        """

        DEBUG_PY = 3
        """
        DebugPy - a debugger for Python.
        Language.PYTHON can use  `Python Extension` in VS Code
        or attach to Python in Visual Studio
        """

        PY_CHARM = 4
        """
        PyCharm PyDev Debugger for remote python debugging.
        Language.PYTHON will use 'Python Debug Server' in PyCharm
        """

    @staticmethod
    def initialize(language: QuantConnect.Language, workers_initialization_callback: typing.Optional[typing.Callable[[], typing.Any]]) -> typing.Tuple[None, typing.Callable[[], typing.Any]]:
        """
        Will start a new debugging session
        
        :param language: The algorithms programming language
        :param workers_initialization_callback: Optionally, the debugging method will set an action which the data stack workers should execute
        so we can debug code executed by them, this is specially important for python.
        """
        ...


