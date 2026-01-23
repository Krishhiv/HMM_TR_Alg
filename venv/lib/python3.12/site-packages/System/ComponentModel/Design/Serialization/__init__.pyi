from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.ComponentModel
import System.ComponentModel.Design
import System.ComponentModel.Design.Serialization
import System.IO
import System.Reflection

IServiceProvider = typing.Any
System_ComponentModel_Design_Serialization_MemberRelationship = typing.Any

System_ComponentModel_Design_Serialization__EventContainer_Callable = typing.TypeVar("System_ComponentModel_Design_Serialization__EventContainer_Callable")
System_ComponentModel_Design_Serialization__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel_Design_Serialization__EventContainer_ReturnType")


class InstanceDescriptor(System.Object):
    """This class has no documentation."""

    @property
    def arguments(self) -> System.Collections.ICollection:
        ...

    @property
    def is_complete(self) -> bool:
        ...

    @property
    def member_info(self) -> System.Reflection.MemberInfo:
        ...

    @overload
    def __init__(self, member: System.Reflection.MemberInfo, arguments: System.Collections.ICollection) -> None:
        ...

    @overload
    def __init__(self, member: System.Reflection.MemberInfo, arguments: System.Collections.ICollection, is_complete: bool) -> None:
        ...

    def invoke(self) -> System.Object:
        ...


class SerializationStore(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def errors(self) -> System.Collections.ICollection:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def save(self, stream: System.IO.Stream) -> None:
        ...


class ComponentSerializationService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create_store(self) -> System.ComponentModel.Design.Serialization.SerializationStore:
        ...

    @overload
    def deserialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore) -> System.Collections.ICollection:
        ...

    @overload
    def deserialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer) -> System.Collections.ICollection:
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer, validate_recycled_types: bool, apply_defaults: bool) -> None:
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer) -> None:
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer, validate_recycled_types: bool) -> None:
        ...

    def load_store(self, stream: System.IO.Stream) -> System.ComponentModel.Design.Serialization.SerializationStore:
        ...

    def serialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore, value: typing.Any) -> None:
        ...

    def serialize_absolute(self, store: System.ComponentModel.Design.Serialization.SerializationStore, value: typing.Any) -> None:
        ...

    def serialize_member(self, store: System.ComponentModel.Design.Serialization.SerializationStore, owning_object: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        ...

    def serialize_member_absolute(self, store: System.ComponentModel.Design.Serialization.SerializationStore, owning_object: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        ...


class INameCreationService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create_name(self, container: System.ComponentModel.IContainer, data_type: typing.Type) -> str:
        ...

    def is_valid_name(self, name: str) -> bool:
        ...

    def validate_name(self, name: str) -> None:
        ...


class RootDesignerSerializerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def reloadable(self) -> bool:
        ...

    @property
    def serializer_type_name(self) -> str:
        ...

    @property
    def serializer_base_type_name(self) -> str:
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @overload
    def __init__(self, serializer_type: typing.Type, base_serializer_type: typing.Type, reloadable: bool) -> None:
        ...

    @overload
    def __init__(self, serializer_type_name: str, base_serializer_type: typing.Type, reloadable: bool) -> None:
        ...

    @overload
    def __init__(self, serializer_type_name: str, base_serializer_type_name: str, reloadable: bool) -> None:
        ...


class ContextStack(System.Object):
    """This class has no documentation."""

    @property
    def current(self) -> System.Object:
        ...

    @overload
    def __getitem__(self, level: int) -> typing.Any:
        ...

    @overload
    def __getitem__(self, type: typing.Type) -> typing.Any:
        ...

    def append(self, context: typing.Any) -> None:
        ...

    def pop(self) -> System.Object:
        ...

    def push(self, context: typing.Any) -> None:
        ...


class IDesignerSerializationProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_serializer(self, manager: System.ComponentModel.Design.Serialization.IDesignerSerializationManager, current_serializer: typing.Any, object_type: typing.Type, serializer_type: typing.Type) -> System.Object:
        ...


class ResolveNameEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> System.Object:
        ...

    @value.setter
    def value(self, value: System.Object) -> None:
        ...

    def __init__(self, name: str) -> None:
        ...


class IDesignerSerializationManager(IServiceProvider, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def context(self) -> System.ComponentModel.Design.Serialization.ContextStack:
        ...

    @property
    @abc.abstractmethod
    def properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @property
    @abc.abstractmethod
    def resolve_name(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.Serialization.ResolveNameEventArgs], typing.Any], typing.Any]:
        ...

    @resolve_name.setter
    def resolve_name(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.Serialization.ResolveNameEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def serialization_complete(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @serialization_complete.setter
    def serialization_complete(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    def add_serialization_provider(self, provider: System.ComponentModel.Design.Serialization.IDesignerSerializationProvider) -> None:
        ...

    def create_instance(self, type: typing.Type, arguments: System.Collections.ICollection, name: str, add_to_container: bool) -> System.Object:
        ...

    def get_instance(self, name: str) -> System.Object:
        ...

    def get_name(self, value: typing.Any) -> str:
        ...

    def get_serializer(self, object_type: typing.Type, serializer_type: typing.Type) -> System.Object:
        ...

    def get_type(self, type_name: str) -> typing.Type:
        ...

    def remove_serialization_provider(self, provider: System.ComponentModel.Design.Serialization.IDesignerSerializationProvider) -> None:
        ...

    def report_error(self, error_information: typing.Any) -> None:
        ...

    def set_name(self, instance: typing.Any, name: str) -> None:
        ...


class IDesignerLoaderHost(System.ComponentModel.Design.IDesignerHost, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def end_load(self, base_class_name: str, successful: bool, error_collection: System.Collections.ICollection) -> None:
        ...

    def reload(self) -> None:
        ...


class DesignerLoader(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def loading(self) -> bool:
        ...

    def begin_load(self, host: System.ComponentModel.Design.Serialization.IDesignerLoaderHost) -> None:
        ...

    def dispose(self) -> None:
        ...

    def flush(self) -> None:
        ...


class IDesignerLoaderHost2(System.ComponentModel.Design.Serialization.IDesignerLoaderHost, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def ignore_errors_during_reload(self) -> bool:
        ...

    @ignore_errors_during_reload.setter
    def ignore_errors_during_reload(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def can_reload_with_errors(self) -> bool:
        ...

    @can_reload_with_errors.setter
    def can_reload_with_errors(self, value: bool) -> None:
        ...


class DefaultSerializationProviderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def provider_type_name(self) -> str:
        ...

    @overload
    def __init__(self, provider_type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, provider_type_name: str) -> None:
        ...


class IDesignerLoaderService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add_load_dependency(self) -> None:
        ...

    def dependent_load_complete(self, successful: bool, error_collection: System.Collections.ICollection) -> None:
        ...

    def reload(self) -> bool:
        ...


class IDesignerSerializationService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def deserialize(self, serialization_data: typing.Any) -> System.Collections.ICollection:
        ...

    def serialize(self, objects: System.Collections.ICollection) -> System.Object:
        ...


class MemberRelationship(System.IEquatable[System_ComponentModel_Design_Serialization_MemberRelationship]):
    """This class has no documentation."""

    EMPTY: System.ComponentModel.Design.Serialization.MemberRelationship

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        ...

    @property
    def owner(self) -> System.Object:
        ...

    def __eq__(self, right: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        ...

    def __init__(self, owner: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        ...

    def __ne__(self, right: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class MemberRelationshipService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def __getitem__(self, source_owner: typing.Any, source_member: System.ComponentModel.MemberDescriptor) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        ...

    @overload
    def __getitem__(self, source: System.ComponentModel.Design.Serialization.MemberRelationship) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        ...

    @overload
    def __setitem__(self, source_owner: typing.Any, source_member: System.ComponentModel.MemberDescriptor, value: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        ...

    @overload
    def __setitem__(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, value: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        ...

    def get_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        ...

    def set_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, relationship: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        ...

    def supports_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, relationship: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        ...


class _EventContainer(typing.Generic[System_ComponentModel_Design_Serialization__EventContainer_Callable, System_ComponentModel_Design_Serialization__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel_Design_Serialization__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel_Design_Serialization__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel_Design_Serialization__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


