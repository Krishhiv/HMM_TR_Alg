from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.ComponentModel
import System.ComponentModel.Design
import System.Globalization
import System.Reflection
import System.Resources
import System.Runtime.InteropServices
import System.Runtime.Serialization

IServiceProvider = typing.Any

System_ComponentModel_BindingList_T = typing.TypeVar("System_ComponentModel_BindingList_T")
System_ComponentModel__EventContainer_Callable = typing.TypeVar("System_ComponentModel__EventContainer_Callable")
System_ComponentModel__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel__EventContainer_ReturnType")


class Win32Exception(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

    @property
    def native_error_code(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, error: int) -> None:
        ...

    @overload
    def __init__(self, error: int, message: str) -> None:
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

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class DefaultValueAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, value: str) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, value: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def set_value(self, value: typing.Any) -> None:
        ...


class EditorBrowsableState(IntEnum):
    """This class has no documentation."""

    ALWAYS = 0

    NEVER = 1

    ADVANCED = 2


class EditorBrowsableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state(self) -> System.ComponentModel.EditorBrowsableState:
        ...

    @overload
    def __init__(self, state: System.ComponentModel.EditorBrowsableState) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class PropertyChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    def __init__(self, property_name: str) -> None:
        ...


class INotifyPropertyChanged(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]:
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...


class TypeDescriptionProviderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...


class PropertyChangingEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    def __init__(self, property_name: str) -> None:
        ...


class INotifyPropertyChanging(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def property_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangingEventArgs], typing.Any], typing.Any]:
        ...

    @property_changing.setter
    def property_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangingEventArgs], typing.Any], typing.Any]) -> None:
        ...


class TypeConverterAttribute(System.Attribute):
    """This class has no documentation."""

    DEFAULT: System.ComponentModel.TypeConverterAttribute = ...

    @property
    def converter_type_name(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DataErrorsChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    def __init__(self, property_name: str) -> None:
        ...


class INotifyDataErrorInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def has_errors(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def errors_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.DataErrorsChangedEventArgs], typing.Any], typing.Any]:
        ...

    @errors_changed.setter
    def errors_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.DataErrorsChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def get_errors(self, property_name: str) -> System.Collections.IEnumerable:
        ...


class AttributeCollection(System.Object, System.Collections.ICollection):
    """This class has no documentation."""

    EMPTY: System.ComponentModel.AttributeCollection = ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __getitem__(self, index: int) -> System.Attribute:
        ...

    @overload
    def __getitem__(self, attribute_type: typing.Type) -> System.Attribute:
        ...

    @overload
    def __init__(self, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def contains(self, attribute: System.Attribute) -> bool:
        ...

    @overload
    def contains(self, attributes: typing.List[System.Attribute]) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    @staticmethod
    def from_existing(existing: System.ComponentModel.AttributeCollection, *new_attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.AttributeCollection:
        ...

    def get_default_attribute(self, attribute_type: typing.Type) -> System.Attribute:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def matches(self, attribute: System.Attribute) -> bool:
        ...

    @overload
    def matches(self, attributes: typing.List[System.Attribute]) -> bool:
        ...


class MemberDescriptor(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def attribute_array(self) -> typing.List[System.Attribute]:
        ...

    @attribute_array.setter
    def attribute_array(self, value: typing.List[System.Attribute]) -> None:
        ...

    @property
    def attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    @property
    def category(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @property
    def is_browsable(self) -> bool:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def name_hash_code(self) -> int:
        ...

    @property
    def design_time_only(self) -> bool:
        ...

    @property
    def display_name(self) -> str:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, attributes: typing.List[System.Attribute]) -> None:
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        ...

    @overload
    def __init__(self, old_member_descriptor: System.ComponentModel.MemberDescriptor, new_attributes: typing.List[System.Attribute]) -> None:
        ...

    def create_attribute_collection(self) -> System.ComponentModel.AttributeCollection:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def fill_attributes(self, attribute_list: System.Collections.IList) -> None:
        ...

    @staticmethod
    @overload
    def find_method(component_class: typing.Type, name: str, args: typing.List[typing.Type], return_type: typing.Type) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    @overload
    def find_method(component_class: typing.Type, name: str, args: typing.List[typing.Type], return_type: typing.Type, public_only: bool) -> System.Reflection.MethodInfo:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_target(self, type: typing.Type, instance: typing.Any) -> System.Object:
        ...

    @staticmethod
    def get_invokee(component_class: typing.Type, component: typing.Any) -> System.Object:
        warnings.warn("MemberDescriptor.GetInvokee has been deprecated. Use GetInvocationTarget instead.", DeprecationWarning)

    @staticmethod
    def get_site(component: typing.Any) -> System.ComponentModel.ISite:
        ...


class PropertyDescriptor(System.ComponentModel.MemberDescriptor, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def component_type(self) -> typing.Type:
        ...

    @property
    def converter(self) -> System.ComponentModel.TypeConverter:
        ...

    @property
    def converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        ...

    @property
    def is_localizable(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        ...

    @property
    def serialization_visibility(self) -> System.ComponentModel.DesignerSerializationVisibility:
        ...

    @property
    @abc.abstractmethod
    def property_type(self) -> typing.Type:
        ...

    @property
    def supports_change_events(self) -> bool:
        ...

    @overload
    def __init__(self, name: str, attrs: typing.List[System.Attribute]) -> None:
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: typing.List[System.Attribute]) -> None:
        ...

    def add_value_changed(self, component: typing.Any, handler: typing.Callable[[System.Object, System.EventArgs], typing.Any]) -> None:
        ...

    def can_reset_value(self, component: typing.Any) -> bool:
        ...

    def create_instance(self, type: typing.Type) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def fill_attributes(self, attribute_list: System.Collections.IList) -> None:
        ...

    @overload
    def get_child_properties(self, instance: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_child_properties(self, instance: typing.Any, filter: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_child_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_child_properties(self, filter: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_target(self, type: typing.Type, instance: typing.Any) -> System.Object:
        ...

    def get_type_from_name(self, type_name: str) -> typing.Type:
        ...

    def get_value(self, component: typing.Any) -> System.Object:
        ...

    def on_value_changed(self, component: typing.Any, e: System.EventArgs) -> None:
        ...

    def remove_value_changed(self, component: typing.Any, handler: typing.Callable[[System.Object, System.EventArgs], typing.Any]) -> None:
        ...

    def reset_value(self, component: typing.Any) -> None:
        ...

    def set_value(self, component: typing.Any, value: typing.Any) -> None:
        ...

    def should_serialize_value(self, component: typing.Any) -> bool:
        ...


class ITypeDescriptorContext(IServiceProvider, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    @abc.abstractmethod
    def instance(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    def on_component_changed(self) -> None:
        ...

    def on_component_changing(self) -> bool:
        ...


class PropertyDescriptorCollection(System.Object, System.Collections.IList, System.Collections.IDictionary):
    """This class has no documentation."""

    EMPTY: System.ComponentModel.PropertyDescriptorCollection = ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __getitem__(self, index: int) -> System.ComponentModel.PropertyDescriptor:
        ...

    @overload
    def __getitem__(self, name: str) -> System.ComponentModel.PropertyDescriptor:
        ...

    @overload
    def __init__(self, properties: typing.List[System.ComponentModel.PropertyDescriptor]) -> None:
        ...

    @overload
    def __init__(self, properties: typing.List[System.ComponentModel.PropertyDescriptor], read_only: bool) -> None:
        ...

    def add(self, value: System.ComponentModel.PropertyDescriptor) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System.ComponentModel.PropertyDescriptor) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def find(self, name: str, ignore_case: bool) -> System.ComponentModel.PropertyDescriptor:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def index_of(self, value: System.ComponentModel.PropertyDescriptor) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def internal_sort(self, names: typing.List[str]) -> None:
        ...

    @overload
    def internal_sort(self, sorter: System.Collections.IComparer) -> None:
        ...

    def remove(self, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    @overload
    def sort(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def sort(self, names: typing.List[str]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def sort(self, names: typing.List[str], comparer: System.Collections.IComparer) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def sort(self, comparer: System.Collections.IComparer) -> System.ComponentModel.PropertyDescriptorCollection:
        ...


class TypeConverter(System.Object):
    """This class has no documentation."""

    class SimplePropertyDescriptor(System.ComponentModel.PropertyDescriptor, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        @property
        def component_type(self) -> typing.Type:
            ...

        @property
        def is_read_only(self) -> bool:
            ...

        @property
        def property_type(self) -> typing.Type:
            ...

        @overload
        def __init__(self, component_type: typing.Type, name: str, property_type: typing.Type) -> None:
            ...

        @overload
        def __init__(self, component_type: typing.Type, name: str, property_type: typing.Type, attributes: typing.List[System.Attribute]) -> None:
            ...

        def can_reset_value(self, component: typing.Any) -> bool:
            ...

        def reset_value(self, component: typing.Any) -> None:
            ...

        def should_serialize_value(self, component: typing.Any) -> bool:
            ...

    class StandardValuesCollection(System.Object, System.Collections.ICollection):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __getitem__(self, index: int) -> typing.Any:
            ...

        def __init__(self, values: System.Collections.ICollection) -> None:
            ...

        def copy_to(self, array: System.Array, index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.IEnumerator:
            ...

    @overload
    def can_convert_from(self, source_type: typing.Type) -> bool:
        ...

    @overload
    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    @overload
    def can_convert_to(self, destination_type: typing.Type) -> bool:
        ...

    @overload
    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    @overload
    def convert_from(self, value: typing.Any) -> System.Object:
        ...

    @overload
    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    @overload
    def convert_from_invariant_string(self, text: str) -> System.Object:
        ...

    @overload
    def convert_from_invariant_string(self, context: System.ComponentModel.ITypeDescriptorContext, text: str) -> System.Object:
        ...

    @overload
    def convert_from_string(self, text: str) -> System.Object:
        ...

    @overload
    def convert_from_string(self, context: System.ComponentModel.ITypeDescriptorContext, text: str) -> System.Object:
        ...

    @overload
    def convert_from_string(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, text: str) -> System.Object:
        ...

    @overload
    def convert_to(self, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    @overload
    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    @overload
    def convert_to_invariant_string(self, value: typing.Any) -> str:
        ...

    @overload
    def convert_to_invariant_string(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> str:
        ...

    @overload
    def convert_to_string(self, value: typing.Any) -> str:
        ...

    @overload
    def convert_to_string(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> str:
        ...

    @overload
    def convert_to_string(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> str:
        ...

    @overload
    def create_instance(self, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    @overload
    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_convert_from_exception(self, value: typing.Any) -> System.Exception:
        ...

    def get_convert_to_exception(self, value: typing.Any, destination_type: typing.Type) -> System.Exception:
        ...

    @overload
    def get_create_instance_supported(self) -> bool:
        ...

    @overload
    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    @overload
    def get_properties(self, value: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_properties_supported(self) -> bool:
        ...

    @overload
    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    @overload
    def get_standard_values(self) -> System.Collections.ICollection:
        ...

    @overload
    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    @overload
    def get_standard_values_exclusive(self) -> bool:
        ...

    @overload
    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    @overload
    def get_standard_values_supported(self) -> bool:
        ...

    @overload
    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    @overload
    def is_valid(self, value: typing.Any) -> bool:
        ...

    @overload
    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...

    def sort_properties(self, props: System.ComponentModel.PropertyDescriptorCollection, names: typing.List[str]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...


class BaseNumberConverter(System.ComponentModel.TypeConverter, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class ByteConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class DefaultBindingPropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    DEFAULT: System.ComponentModel.DefaultBindingPropertyAttribute = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class PasswordPropertyTextAttribute(System.Attribute):
    """This class has no documentation."""

    YES: System.ComponentModel.PasswordPropertyTextAttribute = ...

    NO: System.ComponentModel.PasswordPropertyTextAttribute = ...

    DEFAULT: System.ComponentModel.PasswordPropertyTextAttribute = ...

    @property
    def password(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, password: bool) -> None:
        ...

    def equals(self, o: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class IIntellisenseBuilder(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    def show(self, language: str, value: str, new_value: str) -> bool:
        ...


class AmbientValueAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, value: str) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, value: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class VersionConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class BindableSupport(IntEnum):
    """This class has no documentation."""

    NO = ...

    YES = ...

    DEFAULT = ...


class ListBindableAttribute(System.Attribute):
    """This class has no documentation."""

    YES: System.ComponentModel.ListBindableAttribute = ...

    NO: System.ComponentModel.ListBindableAttribute = ...

    DEFAULT: System.ComponentModel.ListBindableAttribute = ...

    @property
    def list_bindable(self) -> bool:
        ...

    @overload
    def __init__(self, list_bindable: bool) -> None:
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class LicenseUsageMode(IntEnum):
    """This class has no documentation."""

    RUNTIME = 0

    DESIGNTIME = 1


class LicenseContext:
    """This class has no documentation."""

    @property
    def usage_mode(self) -> System.ComponentModel.LicenseUsageMode:
        ...

    def get_saved_license_key(self, type: typing.Type, resource_assembly: System.Reflection.Assembly) -> str:
        ...

    def get_service(self, type: typing.Type) -> System.Object:
        ...

    def set_saved_license_key(self, type: typing.Type, key: str) -> None:
        ...


class DateTimeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class License(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def license_key(self) -> str:
        ...

    def dispose(self) -> None:
        ...


class LicenseManager(System.Object):
    """This class has no documentation."""

    current_context: System.ComponentModel.LicenseContext

    USAGE_MODE: System.ComponentModel.LicenseUsageMode

    @staticmethod
    @overload
    def create_with_context(type: typing.Type, creation_context: System.ComponentModel.LicenseContext) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_with_context(type: typing.Type, creation_context: System.ComponentModel.LicenseContext, args: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    def is_licensed(type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_valid(type: typing.Type, instance: typing.Any, license: typing.Optional[System.ComponentModel.License]) -> typing.Tuple[bool, System.ComponentModel.License]:
        ...

    @staticmethod
    @overload
    def is_valid(type: typing.Type) -> bool:
        ...

    @staticmethod
    def lock_context(context_user: typing.Any) -> None:
        ...

    @staticmethod
    def unlock_context(context_user: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def validate(type: typing.Type, instance: typing.Any) -> System.ComponentModel.License:
        ...

    @staticmethod
    @overload
    def validate(type: typing.Type) -> None:
        ...


class EventDescriptor(System.ComponentModel.MemberDescriptor, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def component_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def event_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def is_multicast(self) -> bool:
        ...

    @overload
    def __init__(self, name: str, attrs: typing.List[System.Attribute]) -> None:
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: typing.List[System.Attribute]) -> None:
        ...

    def add_event_handler(self, component: typing.Any, value: System.Delegate) -> None:
        ...

    def remove_event_handler(self, component: typing.Any, value: System.Delegate) -> None:
        ...


class EventDescriptorCollection(System.Object, System.Collections.IList):
    """This class has no documentation."""

    EMPTY: System.ComponentModel.EventDescriptorCollection = ...

    @property
    def count(self) -> int:
        ...

    @overload
    def __getitem__(self, index: int) -> System.ComponentModel.EventDescriptor:
        ...

    @overload
    def __getitem__(self, name: str) -> System.ComponentModel.EventDescriptor:
        ...

    @overload
    def __init__(self, events: typing.List[System.ComponentModel.EventDescriptor]) -> None:
        ...

    @overload
    def __init__(self, events: typing.List[System.ComponentModel.EventDescriptor], read_only: bool) -> None:
        ...

    def add(self, value: System.ComponentModel.EventDescriptor) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System.ComponentModel.EventDescriptor) -> bool:
        ...

    def find(self, name: str, ignore_case: bool) -> System.ComponentModel.EventDescriptor:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def index_of(self, value: System.ComponentModel.EventDescriptor) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.EventDescriptor) -> None:
        ...

    @overload
    def internal_sort(self, names: typing.List[str]) -> None:
        ...

    @overload
    def internal_sort(self, sorter: System.Collections.IComparer) -> None:
        ...

    def remove(self, value: System.ComponentModel.EventDescriptor) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    @overload
    def sort(self) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def sort(self, names: typing.List[str]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def sort(self, names: typing.List[str], comparer: System.Collections.IComparer) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def sort(self, comparer: System.Collections.IComparer) -> System.ComponentModel.EventDescriptorCollection:
        ...


class ICustomTypeDescriptor(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def require_registered_types(self) -> typing.Optional[bool]:
        ...

    def get_attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    def get_class_name(self) -> str:
        ...

    def get_component_name(self) -> str:
        ...

    def get_converter(self) -> System.ComponentModel.TypeConverter:
        ...

    def get_converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        ...

    def get_default_event(self) -> System.ComponentModel.EventDescriptor:
        ...

    def get_default_property(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        ...

    @overload
    def get_events(self) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_events(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    def get_events_from_registered_type(self) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_properties(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_from_registered_type(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_property_owner(self, pd: System.ComponentModel.PropertyDescriptor) -> System.Object:
        ...


class CollectionChangeAction(IntEnum):
    """This class has no documentation."""

    ADD = 1

    REMOVE = 2

    REFRESH = 3


class CollectionChangeEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def action(self) -> System.ComponentModel.CollectionChangeAction:
        ...

    @property
    def element(self) -> System.Object:
        ...

    def __init__(self, action: System.ComponentModel.CollectionChangeAction, element: typing.Any) -> None:
        ...


class SByteConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class WarningException(System.SystemException):
    """This class has no documentation."""

    @property
    def help_url(self) -> str:
        ...

    @property
    def help_topic(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, help_url: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, help_url: str, help_topic: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class ToolboxItemAttribute(System.Attribute):
    """This class has no documentation."""

    DEFAULT: System.ComponentModel.ToolboxItemAttribute = ...

    NONE: System.ComponentModel.ToolboxItemAttribute = ...

    @property
    def toolbox_item_type(self) -> typing.Type:
        ...

    @property
    def toolbox_item_type_name(self) -> str:
        ...

    @overload
    def __init__(self, default_type: bool) -> None:
        ...

    @overload
    def __init__(self, toolbox_item_type_name: str) -> None:
        ...

    @overload
    def __init__(self, toolbox_item_type: typing.Type) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class BooleanConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class INestedContainer(System.ComponentModel.IContainer, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def owner(self) -> System.ComponentModel.IComponent:
        ...


class HalfConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class LicenseProvider(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_license(self, context: System.ComponentModel.LicenseContext, type: typing.Type, instance: typing.Any, allow_exceptions: bool) -> System.ComponentModel.License:
        ...


class LicFileLicenseProvider(System.ComponentModel.LicenseProvider):
    """This class has no documentation."""

    def get_key(self, type: typing.Type) -> str:
        ...

    def get_license(self, context: System.ComponentModel.LicenseContext, type: typing.Type, instance: typing.Any, allow_exceptions: bool) -> System.ComponentModel.License:
        ...

    def is_key_valid(self, key: str, type: typing.Type) -> bool:
        ...


class ReferenceConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def __init__(self, type: typing.Type) -> None:
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def is_value_allowed(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class LicenseException(System.SystemException):
    """This class has no documentation."""

    @property
    def licensed_type(self) -> typing.Type:
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any, message: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class RecommendedAsConfigurableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def recommended_as_configurable(self) -> bool:
        ...

    NO: System.ComponentModel.RecommendedAsConfigurableAttribute = ...

    YES: System.ComponentModel.RecommendedAsConfigurableAttribute = ...

    DEFAULT: System.ComponentModel.RecommendedAsConfigurableAttribute = ...

    def __init__(self, recommended_as_configurable: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class IComNativeDescriptorHandler(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_attributes(self, component: typing.Any) -> System.ComponentModel.AttributeCollection:
        ...

    def get_class_name(self, component: typing.Any) -> str:
        ...

    def get_converter(self, component: typing.Any) -> System.ComponentModel.TypeConverter:
        ...

    def get_default_event(self, component: typing.Any) -> System.ComponentModel.EventDescriptor:
        ...

    def get_default_property(self, component: typing.Any) -> System.ComponentModel.PropertyDescriptor:
        ...

    def get_editor(self, component: typing.Any, base_editor_type: typing.Type) -> System.Object:
        ...

    @overload
    def get_events(self, component: typing.Any) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_events(self, component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    def get_name(self, component: typing.Any) -> str:
        ...

    def get_properties(self, component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_property_value(self, component: typing.Any, property_name: str, success: bool) -> System.Object:
        ...

    @overload
    def get_property_value(self, component: typing.Any, dispid: int, success: bool) -> System.Object:
        ...


class IDataErrorInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def error(self) -> str:
        ...

    def __getitem__(self, column_name: str) -> str:
        ...


class UInt128Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class DataObjectAttribute(System.Attribute):
    """This class has no documentation."""

    DATA_OBJECT: System.ComponentModel.DataObjectAttribute = ...

    NON_DATA_OBJECT: System.ComponentModel.DataObjectAttribute = ...

    DEFAULT: System.ComponentModel.DataObjectAttribute = ...

    @property
    def is_data_object(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, is_data_object: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class EnumConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    @property
    def enum_type(self) -> typing.Type:
        ...

    @property
    def values(self) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    @values.setter
    def values(self, value: System.ComponentModel.TypeConverter.StandardValuesCollection) -> None:
        ...

    @property
    def comparer(self) -> System.Collections.IComparer:
        ...

    def __init__(self, type: typing.Type) -> None:
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class StringConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...


class Int16Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class IExtenderProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def can_extend(self, extendee: typing.Any) -> bool:
        ...


class ExtenderProvidedPropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def extender_property(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def provider(self) -> System.ComponentModel.IExtenderProvider:
        ...

    @property
    def receiver_type(self) -> typing.Type:
        ...

    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class ListSortDirection(IntEnum):
    """This class has no documentation."""

    ASCENDING = 0

    DESCENDING = 1


class ListSortDescription(System.Object):
    """This class has no documentation."""

    @property
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property_descriptor.setter
    def property_descriptor(self, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @property
    def sort_direction(self) -> System.ComponentModel.ListSortDirection:
        ...

    @sort_direction.setter
    def sort_direction(self, value: System.ComponentModel.ListSortDirection) -> None:
        ...

    def __init__(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        ...


class TypeListConverter(System.ComponentModel.TypeConverter, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self, types: typing.List[typing.Type]) -> None:
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class DefaultPropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    DEFAULT: System.ComponentModel.DefaultPropertyAttribute = ...

    def __init__(self, name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ComponentConverter(System.ComponentModel.ReferenceConverter):
    """This class has no documentation."""

    def __init__(self, type: typing.Type) -> None:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class UInt32Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class DateOnlyConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class DataObjectMethodType(IntEnum):
    """This class has no documentation."""

    FILL = 0

    SELECT = 1

    UPDATE = 2

    INSERT = 3

    DELETE = 4


class DataObjectMethodAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def is_default(self) -> bool:
        ...

    @property
    def method_type(self) -> System.ComponentModel.DataObjectMethodType:
        ...

    @overload
    def __init__(self, method_type: System.ComponentModel.DataObjectMethodType) -> None:
        ...

    @overload
    def __init__(self, method_type: System.ComponentModel.DataObjectMethodType, is_default: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...


class BindingDirection(IntEnum):
    """This class has no documentation."""

    ONE_WAY = 0

    TWO_WAY = 1


class BindableAttribute(System.Attribute):
    """This class has no documentation."""

    YES: System.ComponentModel.BindableAttribute = ...

    NO: System.ComponentModel.BindableAttribute = ...

    DEFAULT: System.ComponentModel.BindableAttribute = ...

    @property
    def bindable(self) -> bool:
        ...

    @property
    def direction(self) -> System.ComponentModel.BindingDirection:
        ...

    @overload
    def __init__(self, bindable: bool) -> None:
        ...

    @overload
    def __init__(self, bindable: bool, direction: System.ComponentModel.BindingDirection) -> None:
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport) -> None:
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport, direction: System.ComponentModel.BindingDirection) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class NullableConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    @property
    def nullable_type(self) -> typing.Type:
        ...

    @property
    def underlying_type(self) -> typing.Type:
        ...

    @property
    def underlying_type_converter(self) -> System.ComponentModel.TypeConverter:
        ...

    def __init__(self, type: typing.Type) -> None:
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class INestedSite(System.ComponentModel.ISite, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def full_name(self) -> str:
        ...


class ToolboxItemFilterType(IntEnum):
    """This class has no documentation."""

    ALLOW = 0

    CUSTOM = 1

    PREVENT = 2

    REQUIRE = 3


class ITypedList(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_item_properties(self, list_accessors: typing.List[System.ComponentModel.PropertyDescriptor]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_list_name(self, list_accessors: typing.List[System.ComponentModel.PropertyDescriptor]) -> str:
        ...


class ComponentEditor(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def edit_component(self, component: typing.Any) -> bool:
        ...

    @overload
    def edit_component(self, context: System.ComponentModel.ITypeDescriptorContext, component: typing.Any) -> bool:
        ...


class Container(System.Object, System.ComponentModel.IContainer):
    """This class has no documentation."""

    @property
    def components(self) -> System.ComponentModel.ComponentCollection:
        ...

    @overload
    def add(self, component: System.ComponentModel.IComponent) -> None:
        ...

    @overload
    def add(self, component: System.ComponentModel.IComponent, name: str) -> None:
        ...

    def create_site(self, component: System.ComponentModel.IComponent, name: str) -> System.ComponentModel.ISite:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        ...

    def remove(self, component: System.ComponentModel.IComponent) -> None:
        ...

    def remove_without_unsiting(self, component: System.ComponentModel.IComponent) -> None:
        ...

    def validate_name(self, component: System.ComponentModel.IComponent, name: str) -> None:
        ...


class DefaultEventAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    DEFAULT: System.ComponentModel.DefaultEventAttribute = ...

    def __init__(self, name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class HandledEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def handled(self) -> bool:
        ...

    @handled.setter
    def handled(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, default_handled_value: bool) -> None:
        ...


class SettingsBindableAttribute(System.Attribute):
    """This class has no documentation."""

    YES: System.ComponentModel.SettingsBindableAttribute = ...

    NO: System.ComponentModel.SettingsBindableAttribute = ...

    @property
    def bindable(self) -> bool:
        ...

    def __init__(self, bindable: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DecimalConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class ListChangedType(IntEnum):
    """This class has no documentation."""

    RESET = 0

    ITEM_ADDED = 1

    ITEM_DELETED = 2

    ITEM_MOVED = 3

    ITEM_CHANGED = 4

    PROPERTY_DESCRIPTOR_ADDED = 5

    PROPERTY_DESCRIPTOR_DELETED = 6

    PROPERTY_DESCRIPTOR_CHANGED = 7


class ListChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def list_changed_type(self) -> System.ComponentModel.ListChangedType:
        ...

    @property
    def new_index(self) -> int:
        ...

    @property
    def old_index(self) -> int:
        ...

    @property
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int, prop_desc: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, prop_desc: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int, old_index: int) -> None:
        ...


class RunInstallerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def run_installer(self) -> bool:
        ...

    YES: System.ComponentModel.RunInstallerAttribute = ...

    NO: System.ComponentModel.RunInstallerAttribute = ...

    DEFAULT: System.ComponentModel.RunInstallerAttribute = ...

    def __init__(self, run_installer: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class CustomTypeDescriptor(System.Object, System.ComponentModel.ICustomTypeDescriptor, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def require_registered_types(self) -> typing.Optional[bool]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, parent: System.ComponentModel.ICustomTypeDescriptor) -> None:
        ...

    def get_attributes(self) -> System.ComponentModel.AttributeCollection:
        ...

    def get_class_name(self) -> str:
        ...

    def get_component_name(self) -> str:
        ...

    def get_converter(self) -> System.ComponentModel.TypeConverter:
        ...

    def get_converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        ...

    def get_default_event(self) -> System.ComponentModel.EventDescriptor:
        ...

    def get_default_property(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        ...

    @overload
    def get_events(self) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_events(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    def get_events_from_registered_type(self) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_properties(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_from_registered_type(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_property_owner(self, pd: System.ComponentModel.PropertyDescriptor) -> System.Object:
        ...


class GuidConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class TypeDescriptionProvider(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def require_registered_types(self) -> typing.Optional[bool]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, parent: System.ComponentModel.TypeDescriptionProvider) -> None:
        ...

    def create_instance(self, provider: typing.Optional[IServiceProvider], object_type: typing.Type, arg_types: typing.List[typing.Type], args: typing.List[System.Object]) -> System.Object:
        ...

    def get_cache(self, instance: typing.Any) -> System.Collections.IDictionary:
        ...

    def get_extended_type_descriptor(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    def get_extended_type_descriptor_from_registered_type(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    def get_full_component_name(self, component: typing.Any) -> str:
        ...

    @overload
    def get_reflection_type(self, instance: typing.Any) -> typing.Type:
        ...

    @overload
    def get_reflection_type(self, object_type: typing.Type, instance: typing.Any) -> typing.Type:
        ...

    @overload
    def get_reflection_type(self, object_type: typing.Type) -> typing.Type:
        ...

    def get_runtime_type(self, reflection_type: typing.Type) -> typing.Type:
        ...

    @overload
    def get_type_descriptor(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    @overload
    def get_type_descriptor(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    @overload
    def get_type_descriptor(self, object_type: typing.Type) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, object_type: typing.Type) -> System.ComponentModel.ICustomTypeDescriptor:
        ...

    def is_registered_type(self, type: typing.Type) -> bool:
        ...

    def is_supported_type(self, type: typing.Type) -> bool:
        ...


class ExpandableObjectConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class CollectionConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...


class IBindingList(System.Collections.IList, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def allow_new(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def allow_edit(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def allow_remove(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_change_notification(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_searching(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_sorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_sorted(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def sort_property(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    @abc.abstractmethod
    def sort_direction(self) -> System.ComponentModel.ListSortDirection:
        ...

    @property
    @abc.abstractmethod
    def list_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], typing.Any], typing.Any]:
        ...

    @list_changed.setter
    def list_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def add_index(self, property: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def add_new(self) -> System.Object:
        ...

    def apply_sort(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        ...

    def find(self, property: System.ComponentModel.PropertyDescriptor, key: typing.Any) -> int:
        ...

    def remove_index(self, property: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def remove_sort(self) -> None:
        ...


class ICancelAddNew(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def cancel_new(self, item_index: int) -> None:
        ...

    def end_new(self, item_index: int) -> None:
        ...


class IRaiseItemChangedEvents(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def raises_item_changed_events(self) -> bool:
        ...


class AddingNewEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def new_object(self) -> System.Object:
        ...

    @new_object.setter
    def new_object(self, value: System.Object) -> None:
        ...

    @overload
    def __init__(self, new_object: typing.Any) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...


class BindingList(typing.Generic[System_ComponentModel_BindingList_T], System.Collections.ObjectModel.Collection[System_ComponentModel_BindingList_T], System.ComponentModel.IBindingList, System.ComponentModel.ICancelAddNew, System.ComponentModel.IRaiseItemChangedEvents):
    """This class has no documentation."""

    @property
    def adding_new(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.AddingNewEventArgs], typing.Any], typing.Any]:
        ...

    @adding_new.setter
    def adding_new(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.AddingNewEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def list_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], typing.Any], typing.Any]:
        ...

    @list_changed.setter
    def list_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def raise_list_changed_events(self) -> bool:
        ...

    @raise_list_changed_events.setter
    def raise_list_changed_events(self, value: bool) -> None:
        ...

    @property
    def allow_new(self) -> bool:
        ...

    @allow_new.setter
    def allow_new(self, value: bool) -> None:
        ...

    @property
    def allow_edit(self) -> bool:
        ...

    @allow_edit.setter
    def allow_edit(self, value: bool) -> None:
        ...

    @property
    def allow_remove(self) -> bool:
        ...

    @allow_remove.setter
    def allow_remove(self, value: bool) -> None:
        ...

    @property
    def supports_change_notification_core(self) -> bool:
        ...

    @property
    def supports_searching_core(self) -> bool:
        ...

    @property
    def supports_sorting_core(self) -> bool:
        ...

    @property
    def is_sorted_core(self) -> bool:
        ...

    @property
    def sort_property_core(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    def sort_direction_core(self) -> System.ComponentModel.ListSortDirection:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.IList[System_ComponentModel_BindingList_T]) -> None:
        ...

    def add_new(self) -> System_ComponentModel_BindingList_T:
        ...

    def add_new_core(self) -> System.Object:
        ...

    def apply_sort_core(self, prop: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        ...

    def cancel_new(self, item_index: int) -> None:
        ...

    def clear_items(self) -> None:
        ...

    def end_new(self, item_index: int) -> None:
        ...

    def find_core(self, prop: System.ComponentModel.PropertyDescriptor, key: typing.Any) -> int:
        ...

    def insert_item(self, index: int, item: System_ComponentModel_BindingList_T) -> None:
        ...

    def on_adding_new(self, e: System.ComponentModel.AddingNewEventArgs) -> None:
        ...

    def on_list_changed(self, e: System.ComponentModel.ListChangedEventArgs) -> None:
        ...

    def remove_item(self, index: int) -> None:
        ...

    def remove_sort_core(self) -> None:
        ...

    def reset_bindings(self) -> None:
        ...

    def reset_item(self, position: int) -> None:
        ...

    def set_item(self, index: int, item: System_ComponentModel_BindingList_T) -> None:
        ...


class ListSortDescriptionCollection(System.Object, System.Collections.IList):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    def __getitem__(self, index: int) -> System.ComponentModel.ListSortDescription:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, sorts: typing.List[System.ComponentModel.ListSortDescription]) -> None:
        ...

    def __setitem__(self, index: int, value: System.ComponentModel.ListSortDescription) -> None:
        ...

    def contains(self, value: typing.Any) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def index_of(self, value: typing.Any) -> int:
        ...


class ProvidePropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    @property
    def receiver_type_name(self) -> str:
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @overload
    def __init__(self, property_name: str, receiver_type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, property_name: str, receiver_type_name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class Int128Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class DateTimeOffsetConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class Int64Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class UInt16Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class RefreshEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def component_changed(self) -> System.Object:
        ...

    @property
    def type_changed(self) -> typing.Type:
        ...

    @overload
    def __init__(self, component_changed: typing.Any) -> None:
        ...

    @overload
    def __init__(self, type_changed: typing.Type) -> None:
        ...


class TypeDescriptor(System.Object):
    """This class has no documentation."""

    INTERFACE_TYPE: typing.Type

    refreshed: _EventContainer[typing.Callable[[System.ComponentModel.RefreshEventArgs], typing.Any], typing.Any]

    COM_OBJECT_TYPE: typing.Type

    com_native_descriptor_handler: System.ComponentModel.IComNativeDescriptorHandler

    @staticmethod
    @overload
    def add_attributes(instance: typing.Any, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @staticmethod
    @overload
    def add_attributes(type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @staticmethod
    def add_editor_table(editor_base_type: typing.Type, table: System.Collections.Hashtable) -> None:
        ...

    @staticmethod
    @overload
    def add_provider(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def add_provider(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def add_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def add_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        ...

    @staticmethod
    def create_association(primary: typing.Any, secondary: typing.Any) -> None:
        ...

    @staticmethod
    def create_designer(component: System.ComponentModel.IComponent, designer_base_type: typing.Type) -> System.ComponentModel.Design.IDesigner:
        ...

    @staticmethod
    @overload
    def create_event(component_type: typing.Type, name: str, type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    @overload
    def create_event(component_type: typing.Type, old_event_descriptor: System.ComponentModel.EventDescriptor, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    def create_instance(provider: typing.Optional[IServiceProvider], object_type: typing.Type, arg_types: typing.List[typing.Type], args: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_property(component_type: typing.Type, name: str, type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    @overload
    def create_property(component_type: typing.Type, old_property_descriptor: System.ComponentModel.PropertyDescriptor, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    def get_association(type: typing.Type, primary: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def get_attributes(component: typing.Any) -> System.ComponentModel.AttributeCollection:
        ...

    @staticmethod
    @overload
    def get_attributes(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.AttributeCollection:
        ...

    @staticmethod
    @overload
    def get_attributes(component_type: typing.Type) -> System.ComponentModel.AttributeCollection:
        ...

    @staticmethod
    @overload
    def get_class_name(component: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def get_class_name(component: typing.Any, no_custom_type_desc: bool) -> str:
        ...

    @staticmethod
    @overload
    def get_class_name(component_type: typing.Type) -> str:
        ...

    @staticmethod
    @overload
    def get_component_name(component: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def get_component_name(component: typing.Any, no_custom_type_desc: bool) -> str:
        ...

    @staticmethod
    @overload
    def get_converter(component: typing.Any) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    @overload
    def get_converter(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    @overload
    def get_converter(type: typing.Type) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    @overload
    def get_converter_from_registered_type(component: typing.Any) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    @overload
    def get_converter_from_registered_type(type: typing.Type) -> System.ComponentModel.TypeConverter:
        ...

    @staticmethod
    @overload
    def get_default_event(component: typing.Any) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    @overload
    def get_default_event(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    @overload
    def get_default_event(component_type: typing.Type) -> System.ComponentModel.EventDescriptor:
        ...

    @staticmethod
    @overload
    def get_default_property(component: typing.Any) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    @overload
    def get_default_property(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    @overload
    def get_default_property(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptor:
        ...

    @staticmethod
    @overload
    def get_editor(component: typing.Any, editor_base_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def get_editor(component: typing.Any, editor_base_type: typing.Type, no_custom_type_desc: bool) -> System.Object:
        ...

    @staticmethod
    @overload
    def get_editor(type: typing.Type, editor_base_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, attributes: typing.List[System.Attribute], no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_events(component_type: typing.Type) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_events(component_type: typing.Type, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    def get_events_from_registered_type(component_type: typing.Type) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @staticmethod
    def get_full_component_name(component: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, attributes: typing.List[System.Attribute], no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties(component_type: typing.Type, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties_from_registered_type(component: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_properties_from_registered_type(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @staticmethod
    @overload
    def get_provider(instance: typing.Any) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @staticmethod
    @overload
    def get_provider(type: typing.Type) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @staticmethod
    @overload
    def get_reflection_type(instance: typing.Any) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_reflection_type(type: typing.Type) -> typing.Type:
        ...

    @staticmethod
    @overload
    def refresh(component: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def refresh(type: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def refresh(module: System.Reflection.Module) -> None:
        ...

    @staticmethod
    @overload
    def refresh(assembly: System.Reflection.Assembly) -> None:
        ...

    @staticmethod
    def remove_association(primary: typing.Any, secondary: typing.Any) -> None:
        ...

    @staticmethod
    def remove_associations(primary: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def remove_provider(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def remove_provider(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def remove_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def remove_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        ...

    @staticmethod
    def sort_descriptor_array(infos: System.Collections.IList) -> None:
        ...


class MultilineStringConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class TimeOnlyConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class ToolboxItemFilterAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def filter_string(self) -> str:
        ...

    @property
    def filter_type(self) -> System.ComponentModel.ToolboxItemFilterType:
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @overload
    def __init__(self, filter_string: str) -> None:
        ...

    @overload
    def __init__(self, filter_string: str, filter_type: System.ComponentModel.ToolboxItemFilterType) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...

    def to_string(self) -> str:
        ...


class MarshalByValueComponent(System.Object, System.ComponentModel.IComponent, IServiceProvider):
    """This class has no documentation."""

    @property
    def disposed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @disposed.setter
    def disposed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def events(self) -> System.ComponentModel.EventHandlerList:
        ...

    @property
    def site(self) -> System.ComponentModel.ISite:
        ...

    @site.setter
    def site(self, value: System.ComponentModel.ISite) -> None:
        ...

    @property
    def container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    def design_mode(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        ...

    def to_string(self) -> str:
        ...


class ContainerFilterService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def filter_components(self, components: System.ComponentModel.ComponentCollection) -> System.ComponentModel.ComponentCollection:
        ...


class ISupportInitializeNotification(System.ComponentModel.ISupportInitialize, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_initialized(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def initialized(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @initialized.setter
    def initialized(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...


class InheritanceLevel(IntEnum):
    """This class has no documentation."""

    INHERITED = 1

    INHERITED_READ_ONLY = 2

    NOT_INHERITED = 3


class InheritanceAttribute(System.Attribute):
    """This class has no documentation."""

    INHERITED: System.ComponentModel.InheritanceAttribute = ...

    INHERITED_READ_ONLY: System.ComponentModel.InheritanceAttribute = ...

    NOT_INHERITED: System.ComponentModel.InheritanceAttribute = ...

    DEFAULT: System.ComponentModel.InheritanceAttribute = ...

    @property
    def inheritance_level(self) -> System.ComponentModel.InheritanceLevel:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, inheritance_level: System.ComponentModel.InheritanceLevel) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...

    def to_string(self) -> str:
        ...


class CharConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class IBindingListView(System.ComponentModel.IBindingList, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def filter(self) -> str:
        ...

    @filter.setter
    def filter(self, value: str) -> None:
        ...

    @property
    @abc.abstractmethod
    def sort_descriptions(self) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    @property
    @abc.abstractmethod
    def supports_advanced_sorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_filtering(self) -> bool:
        ...

    def apply_sort(self, sorts: System.ComponentModel.ListSortDescriptionCollection) -> None:
        ...

    def remove_filter(self) -> None:
        ...


class MaskedTextResultHint(IntEnum):
    """This class has no documentation."""

    UNKNOWN = 0

    CHARACTER_ESCAPED = 1

    NO_EFFECT = 2

    SIDE_EFFECT = 3

    SUCCESS = 4

    ASCII_CHARACTER_EXPECTED = -1

    ALPHANUMERIC_CHARACTER_EXPECTED = -2

    DIGIT_EXPECTED = -3

    LETTER_EXPECTED = -4

    SIGNED_DIGIT_EXPECTED = -5

    INVALID_INPUT = -51

    PROMPT_CHAR_NOT_ALLOWED = -52

    UNAVAILABLE_EDIT_POSITION = -53

    NON_EDIT_POSITION = -54

    POSITION_OUT_OF_RANGE = -55


class MaskedTextProvider(System.Object, System.ICloneable):
    """This class has no documentation."""

    @property
    def allow_prompt_as_input(self) -> bool:
        ...

    @property
    def assigned_edit_position_count(self) -> int:
        ...

    @property
    def available_edit_position_count(self) -> int:
        ...

    @property
    def culture(self) -> System.Globalization.CultureInfo:
        ...

    DEFAULT_PASSWORD_CHAR: str

    @property
    def edit_position_count(self) -> int:
        ...

    @property
    def edit_positions(self) -> System.Collections.IEnumerator:
        ...

    @property
    def include_literals(self) -> bool:
        ...

    @include_literals.setter
    def include_literals(self, value: bool) -> None:
        ...

    @property
    def include_prompt(self) -> bool:
        ...

    @include_prompt.setter
    def include_prompt(self, value: bool) -> None:
        ...

    @property
    def ascii_only(self) -> bool:
        ...

    @property
    def is_password(self) -> bool:
        ...

    @is_password.setter
    def is_password(self, value: bool) -> None:
        ...

    INVALID_INDEX: int

    @property
    def last_assigned_position(self) -> int:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def mask(self) -> str:
        ...

    @property
    def mask_completed(self) -> bool:
        ...

    @property
    def mask_full(self) -> bool:
        ...

    @property
    def password_char(self) -> str:
        ...

    @password_char.setter
    def password_char(self, value: str) -> None:
        ...

    @property
    def prompt_char(self) -> str:
        ...

    @prompt_char.setter
    def prompt_char(self, value: str) -> None:
        ...

    @property
    def reset_on_prompt(self) -> bool:
        ...

    @reset_on_prompt.setter
    def reset_on_prompt(self, value: bool) -> None:
        ...

    @property
    def reset_on_space(self) -> bool:
        ...

    @reset_on_space.setter
    def reset_on_space(self, value: bool) -> None:
        ...

    @property
    def skip_literals(self) -> bool:
        ...

    @skip_literals.setter
    def skip_literals(self, value: bool) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    @overload
    def __init__(self, mask: str) -> None:
        ...

    @overload
    def __init__(self, mask: str, restrict_to_ascii: bool) -> None:
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo) -> None:
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, restrict_to_ascii: bool) -> None:
        ...

    @overload
    def __init__(self, mask: str, password_char: str, allow_prompt_as_input: bool) -> None:
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, password_char: str, allow_prompt_as_input: bool) -> None:
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, allow_prompt_as_input: bool, prompt_char: str, password_char: str, restrict_to_ascii: bool) -> None:
        ...

    @overload
    def add(self, input: str) -> bool:
        ...

    @overload
    def add(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    @overload
    def clear(self) -> None:
        ...

    @overload
    def clear(self, result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[None, System.ComponentModel.MaskedTextResultHint]:
        ...

    def clone(self) -> System.Object:
        ...

    def find_assigned_edit_position_from(self, position: int, direction: bool) -> int:
        ...

    def find_assigned_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        ...

    def find_edit_position_from(self, position: int, direction: bool) -> int:
        ...

    def find_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        ...

    def find_non_edit_position_from(self, position: int, direction: bool) -> int:
        ...

    def find_non_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        ...

    def find_unassigned_edit_position_from(self, position: int, direction: bool) -> int:
        ...

    def find_unassigned_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        ...

    @staticmethod
    def get_operation_result_from_hint(hint: System.ComponentModel.MaskedTextResultHint) -> bool:
        ...

    @overload
    def insert_at(self, input: str, position: int) -> bool:
        ...

    @overload
    def insert_at(self, input: str, position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    def is_available_position(self, position: int) -> bool:
        ...

    def is_edit_position(self, position: int) -> bool:
        ...

    @staticmethod
    def is_valid_input_char(c: str) -> bool:
        ...

    @staticmethod
    def is_valid_mask_char(c: str) -> bool:
        ...

    @staticmethod
    def is_valid_password_char(c: str) -> bool:
        ...

    @overload
    def remove(self) -> bool:
        ...

    @overload
    def remove(self, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    @overload
    def remove_at(self, position: int) -> bool:
        ...

    @overload
    def remove_at(self, start_position: int, end_position: int) -> bool:
        ...

    @overload
    def remove_at(self, start_position: int, end_position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    @overload
    def replace(self, input: str, position: int) -> bool:
        ...

    @overload
    def replace(self, input: str, position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    @overload
    def replace(self, input: str, start_position: int, end_position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    @overload
    def set(self, input: str) -> bool:
        ...

    @overload
    def set(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...

    def to_display_string(self) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, ignore_password_char: bool) -> str:
        ...

    @overload
    def to_string(self, start_position: int, length: int) -> str:
        ...

    @overload
    def to_string(self, ignore_password_char: bool, start_position: int, length: int) -> str:
        ...

    @overload
    def to_string(self, include_prompt: bool, include_literals: bool) -> str:
        ...

    @overload
    def to_string(self, include_prompt: bool, include_literals: bool, start_position: int, length: int) -> str:
        ...

    @overload
    def to_string(self, ignore_password_char: bool, include_prompt: bool, include_literals: bool, start_position: int, length: int) -> str:
        ...

    def verify_char(self, input: str, position: int, hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, System.ComponentModel.MaskedTextResultHint]:
        ...

    def verify_escape_char(self, input: str, position: int) -> bool:
        ...

    @overload
    def verify_string(self, input: str) -> bool:
        ...

    @overload
    def verify_string(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        ...


class DoubleConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class SyntaxCheck(System.Object):
    """This class has no documentation."""

    @staticmethod
    def check_machine_name(value: str) -> bool:
        ...

    @staticmethod
    def check_path(value: str) -> bool:
        ...

    @staticmethod
    def check_rooted_path(value: str) -> bool:
        ...


class IListSource(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def contains_list_collection(self) -> bool:
        ...

    def get_list(self) -> System.Collections.IList:
        ...


class LicenseProviderAttribute(System.Attribute):
    """This class has no documentation."""

    DEFAULT: System.ComponentModel.LicenseProviderAttribute = ...

    @property
    def license_provider(self) -> typing.Type:
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class LookupBindingPropertiesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def data_source(self) -> str:
        ...

    @property
    def display_member(self) -> str:
        ...

    @property
    def value_member(self) -> str:
        ...

    @property
    def lookup_member(self) -> str:
        ...

    DEFAULT: System.ComponentModel.LookupBindingPropertiesAttribute = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, data_source: str, display_member: str, value_member: str, lookup_member: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class SingleConverter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class InstallerTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def installer_type(self) -> typing.Type:
        ...

    @overload
    def __init__(self, installer_type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ArrayConverter(System.ComponentModel.CollectionConverter):
    """This class has no documentation."""

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class InstanceCreationEditor(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def text(self) -> str:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, instance_type: typing.Type) -> System.Object:
        ...


class ComplexBindingPropertiesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def data_source(self) -> str:
        ...

    @property
    def data_member(self) -> str:
        ...

    DEFAULT: System.ComponentModel.ComplexBindingPropertiesAttribute = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, data_source: str) -> None:
        ...

    @overload
    def __init__(self, data_source: str, data_member: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CultureInfoConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_culture_name(self, culture: System.Globalization.CultureInfo) -> str:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class TimeSpanConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...


class DataObjectFieldAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def is_identity(self) -> bool:
        ...

    @property
    def is_nullable(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def primary_key(self) -> bool:
        ...

    @overload
    def __init__(self, primary_key: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool, is_nullable: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool, is_nullable: bool, length: int) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class UInt64Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class AttributeProviderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        ...

    @property
    def property_name(self) -> str:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    @overload
    def __init__(self, type_name: str, property_name: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...


class Int32Converter(System.ComponentModel.BaseNumberConverter):
    """This class has no documentation."""


class NestedContainer(System.ComponentModel.Container, System.ComponentModel.INestedContainer):
    """This class has no documentation."""

    @property
    def owner(self) -> System.ComponentModel.IComponent:
        ...

    @property
    def owner_name(self) -> str:
        ...

    def __init__(self, owner: System.ComponentModel.IComponent) -> None:
        ...

    def create_site(self, component: System.ComponentModel.IComponent, name: str) -> System.ComponentModel.ISite:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        ...


class ComponentResourceManager(System.Resources.ResourceManager):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, t: typing.Type) -> None:
        ...

    @overload
    def apply_resources(self, value: typing.Any, object_name: str) -> None:
        ...

    @overload
    def apply_resources(self, value: typing.Any, object_name: str, culture: System.Globalization.CultureInfo) -> None:
        ...

    def apply_resources_to_registered_type(self, value: typing.Any, object_name: str, culture: System.Globalization.CultureInfo) -> None:
        ...


class DesignTimeVisibleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def visible(self) -> bool:
        ...

    YES: System.ComponentModel.DesignTimeVisibleAttribute = ...

    NO: System.ComponentModel.DesignTimeVisibleAttribute = ...

    DEFAULT: System.ComponentModel.DesignTimeVisibleAttribute = ...

    @overload
    def __init__(self, visible: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class PropertyTabScope(IntEnum):
    """This class has no documentation."""

    STATIC = 0

    GLOBAL = 1

    DOCUMENT = 2

    COMPONENT = 3


class PropertyTabAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def tab_classes(self) -> typing.List[typing.Type]:
        ...

    @property
    def tab_class_names(self) -> typing.List[str]:
        ...

    @property
    def tab_scopes(self) -> typing.List[System.ComponentModel.PropertyTabScope]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, tab_class: typing.Type) -> None:
        ...

    @overload
    def __init__(self, tab_class_name: str) -> None:
        ...

    @overload
    def __init__(self, tab_class: typing.Type, tab_scope: System.ComponentModel.PropertyTabScope) -> None:
        ...

    @overload
    def __init__(self, tab_class_name: str, tab_scope: System.ComponentModel.PropertyTabScope) -> None:
        ...

    @overload
    def equals(self, other: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.ComponentModel.PropertyTabAttribute) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def initialize_arrays(self, tab_class_names: typing.List[str], tab_scopes: typing.List[System.ComponentModel.PropertyTabScope]) -> None:
        ...

    @overload
    def initialize_arrays(self, tab_classes: typing.List[typing.Type], tab_scopes: typing.List[System.ComponentModel.PropertyTabScope]) -> None:
        ...


class _EventContainer(typing.Generic[System_ComponentModel__EventContainer_Callable, System_ComponentModel__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


