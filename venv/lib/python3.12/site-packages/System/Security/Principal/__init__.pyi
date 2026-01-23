from typing import overload
from enum import IntEnum
import abc

import System
import System.Security.Principal


class TokenImpersonationLevel(IntEnum):
    """This class has no documentation."""

    NONE = 0

    ANONYMOUS = 1

    IDENTIFICATION = 2

    IMPERSONATION = 3

    DELEGATION = 4


class IIdentity(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def authentication_type(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def is_authenticated(self) -> bool:
        ...


class PrincipalPolicy(IntEnum):
    """This class has no documentation."""

    UNAUTHENTICATED_PRINCIPAL = 0

    NO_PRINCIPAL = 1

    WINDOWS_PRINCIPAL = 2


class IPrincipal(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def identity(self) -> System.Security.Principal.IIdentity:
        ...

    def is_in_role(self, role: str) -> bool:
        ...


