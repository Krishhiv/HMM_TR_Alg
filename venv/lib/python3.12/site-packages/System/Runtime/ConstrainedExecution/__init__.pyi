from typing import overload
from enum import IntEnum
import abc

import System
import System.Runtime.ConstrainedExecution


class Consistency(IntEnum):
    """This class has no documentation."""

    MAY_CORRUPT_PROCESS = 0

    MAY_CORRUPT_APP_DOMAIN = 1

    MAY_CORRUPT_INSTANCE = 2

    WILL_NOT_CORRUPT_STATE = 3


class Cer(IntEnum):
    """This class has no documentation."""

    NONE = 0

    MAY_FAIL = 1

    SUCCESS = 2


class ReliabilityContractAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def consistency_guarantee(self) -> System.Runtime.ConstrainedExecution.Consistency:
        ...

    @property
    def cer(self) -> System.Runtime.ConstrainedExecution.Cer:
        ...

    def __init__(self, consistency_guarantee: System.Runtime.ConstrainedExecution.Consistency, cer: System.Runtime.ConstrainedExecution.Cer) -> None:
        ...


class PrePrepareMethodAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CriticalFinalizerObject(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


