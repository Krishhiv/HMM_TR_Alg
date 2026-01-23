from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections
import System.Reflection
import System.Runtime.Serialization
import System.Security
import System.Security.Permissions


class SecurityRuleSet(IntEnum):
    """This class has no documentation."""

    NONE = 0

    LEVEL_1 = 1

    LEVEL_2 = 2


class SecurityTreatAsSafeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class SecurityElement(System.Object):
    """This class has no documentation."""

    @property
    def tag(self) -> str:
        ...

    @tag.setter
    def tag(self, value: str) -> None:
        ...

    @property
    def attributes(self) -> System.Collections.Hashtable:
        ...

    @attributes.setter
    def attributes(self, value: System.Collections.Hashtable) -> None:
        ...

    @property
    def text(self) -> str:
        ...

    @text.setter
    def text(self, value: str) -> None:
        ...

    @property
    def children(self) -> System.Collections.ArrayList:
        ...

    @children.setter
    def children(self, value: System.Collections.ArrayList) -> None:
        ...

    @overload
    def __init__(self, tag: str) -> None:
        ...

    @overload
    def __init__(self, tag: str, text: str) -> None:
        ...

    def add_attribute(self, name: str, value: str) -> None:
        ...

    def add_child(self, child: System.Security.SecurityElement) -> None:
        ...

    def attribute(self, name: str) -> str:
        ...

    def copy(self) -> System.Security.SecurityElement:
        ...

    def equal(self, other: System.Security.SecurityElement) -> bool:
        ...

    @staticmethod
    def escape(str: str) -> str:
        ...

    @staticmethod
    def from_string(xml: str) -> System.Security.SecurityElement:
        ...

    @staticmethod
    def is_valid_attribute_name(name: str) -> bool:
        ...

    @staticmethod
    def is_valid_attribute_value(value: str) -> bool:
        ...

    @staticmethod
    def is_valid_tag(tag: str) -> bool:
        ...

    @staticmethod
    def is_valid_text(text: str) -> bool:
        ...

    def search_for_child_by_tag(self, tag: str) -> System.Security.SecurityElement:
        ...

    def search_for_text_of_tag(self, tag: str) -> str:
        ...

    def to_string(self) -> str:
        ...


class ISecurityEncodable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def from_xml(self, e: System.Security.SecurityElement) -> None:
        ...

    def to_xml(self) -> System.Security.SecurityElement:
        ...


class SecuritySafeCriticalAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class SecurityCriticalScope(IntEnum):
    """This class has no documentation."""

    EXPLICIT = 0

    EVERYTHING = ...


class SecurityCriticalAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def scope(self) -> System.Security.SecurityCriticalScope:
        warnings.warn("SecurityCriticalScope is only used for .NET 2.0 transparency compatibility.", DeprecationWarning)

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, scope: System.Security.SecurityCriticalScope) -> None:
        ...


class PartialTrustVisibilityLevel(IntEnum):
    """This class has no documentation."""

    VISIBLE_TO_ALL_HOSTS = 0

    NOT_VISIBLE_BY_DEFAULT = 1


class SecurityException(System.SystemException):
    """This class has no documentation."""

    @property
    def demanded(self) -> System.Object:
        ...

    @demanded.setter
    def demanded(self, value: System.Object) -> None:
        ...

    @property
    def deny_set_instance(self) -> System.Object:
        ...

    @deny_set_instance.setter
    def deny_set_instance(self, value: System.Object) -> None:
        ...

    @property
    def failed_assembly_info(self) -> System.Reflection.AssemblyName:
        ...

    @failed_assembly_info.setter
    def failed_assembly_info(self, value: System.Reflection.AssemblyName) -> None:
        ...

    @property
    def granted_set(self) -> str:
        ...

    @granted_set.setter
    def granted_set(self, value: str) -> None:
        ...

    @property
    def method(self) -> System.Reflection.MethodInfo:
        ...

    @method.setter
    def method(self, value: System.Reflection.MethodInfo) -> None:
        ...

    @property
    def permission_state(self) -> str:
        ...

    @permission_state.setter
    def permission_state(self, value: str) -> None:
        ...

    @property
    def permission_type(self) -> typing.Type:
        ...

    @permission_type.setter
    def permission_type(self, value: typing.Type) -> None:
        ...

    @property
    def permit_only_set_instance(self) -> System.Object:
        ...

    @permit_only_set_instance.setter
    def permit_only_set_instance(self, value: System.Object) -> None:
        ...

    @property
    def refused_set(self) -> str:
        ...

    @refused_set.setter
    def refused_set(self, value: str) -> None:
        ...

    @property
    def url(self) -> str:
        ...

    @url.setter
    def url(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, message: str, type: typing.Type, state: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class SecurityRulesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def skip_verification_in_full_trust(self) -> bool:
        ...

    @skip_verification_in_full_trust.setter
    def skip_verification_in_full_trust(self, value: bool) -> None:
        ...

    @property
    def rule_set(self) -> System.Security.SecurityRuleSet:
        ...

    def __init__(self, rule_set: System.Security.SecurityRuleSet) -> None:
        ...


class SecureString(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def length(self) -> int:
        ...

    @overload
    def __init__(self, value: typing.Any, length: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def append_char(self, c: str) -> None:
        ...

    def clear(self) -> None:
        ...

    def copy(self) -> System.Security.SecureString:
        ...

    def dispose(self) -> None:
        ...

    def insert_at(self, index: int, c: str) -> None:
        ...

    def is_read_only(self) -> bool:
        ...

    def make_read_only(self) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def set_at(self, index: int, c: str) -> None:
        ...


class IStackWalk(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Assert(self) -> None:
        ...

    def demand(self) -> None:
        ...

    def deny(self) -> None:
        ...

    def permit_only(self) -> None:
        ...


class UnverifiableCodeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AllowPartiallyTrustedCallersAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def partial_trust_visibility_level(self) -> System.Security.PartialTrustVisibilityLevel:
        ...

    @partial_trust_visibility_level.setter
    def partial_trust_visibility_level(self, value: System.Security.PartialTrustVisibilityLevel) -> None:
        ...

    def __init__(self) -> None:
        ...


class IPermission(System.Security.ISecurityEncodable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def copy(self) -> System.Security.IPermission:
        ...

    def demand(self) -> None:
        ...

    def intersect(self, target: System.Security.IPermission) -> System.Security.IPermission:
        ...

    def is_subset_of(self, target: System.Security.IPermission) -> bool:
        ...

    def union(self, target: System.Security.IPermission) -> System.Security.IPermission:
        ...


class VerificationException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class PermissionSet(System.Object, System.Collections.ICollection, System.Runtime.Serialization.IDeserializationCallback, System.Security.ISecurityEncodable, System.Security.IStackWalk):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @overload
    def __init__(self, state: System.Security.Permissions.PermissionState) -> None:
        ...

    @overload
    def __init__(self, perm_set: System.Security.PermissionSet) -> None:
        ...

    def add_permission(self, perm: System.Security.IPermission) -> System.Security.IPermission:
        ...

    def add_permission_impl(self, perm: System.Security.IPermission) -> System.Security.IPermission:
        ...

    def Assert(self) -> None:
        ...

    def contains_non_code_access_permissions(self) -> bool:
        ...

    @staticmethod
    def convert_permission_set(in_format: str, in_data: typing.List[int], out_format: str) -> typing.List[int]:
        warnings.warn("This member is marked as obsolete.", DeprecationWarning)

    def copy(self) -> System.Security.PermissionSet:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def demand(self) -> None:
        ...

    def deny(self) -> None:
        warnings.warn("This member is marked as obsolete.", DeprecationWarning)

    def equals(self, o: typing.Any) -> bool:
        ...

    def from_xml(self, et: System.Security.SecurityElement) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_enumerator_impl(self) -> System.Collections.IEnumerator:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_permission(self, perm_class: typing.Type) -> System.Security.IPermission:
        ...

    def get_permission_impl(self, perm_class: typing.Type) -> System.Security.IPermission:
        ...

    def intersect(self, other: System.Security.PermissionSet) -> System.Security.PermissionSet:
        ...

    def is_empty(self) -> bool:
        ...

    def is_subset_of(self, target: System.Security.PermissionSet) -> bool:
        ...

    def is_unrestricted(self) -> bool:
        ...

    def permit_only(self) -> None:
        ...

    def remove_permission(self, perm_class: typing.Type) -> System.Security.IPermission:
        ...

    def remove_permission_impl(self, perm_class: typing.Type) -> System.Security.IPermission:
        ...

    @staticmethod
    def revert_assert() -> None:
        ...

    def set_permission(self, perm: System.Security.IPermission) -> System.Security.IPermission:
        ...

    def set_permission_impl(self, perm: System.Security.IPermission) -> System.Security.IPermission:
        ...

    def to_string(self) -> str:
        ...

    def to_xml(self) -> System.Security.SecurityElement:
        ...

    def union(self, other: System.Security.PermissionSet) -> System.Security.PermissionSet:
        ...


class SecurityTransparentAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class SuppressUnmanagedCodeSecurityAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


