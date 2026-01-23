from typing import overload
from enum import IntEnum
import System
import System.Configuration.Assemblies


class AssemblyVersionCompatibility(IntEnum):
    """This class has no documentation."""

    SAME_MACHINE = 1

    SAME_PROCESS = 2

    SAME_DOMAIN = 3


class AssemblyHashAlgorithm(IntEnum):
    """This class has no documentation."""

    NONE = 0

    MD_5 = ...

    SHA_1 = ...

    SHA_256 = ...

    SHA_384 = ...

    SHA_512 = ...


