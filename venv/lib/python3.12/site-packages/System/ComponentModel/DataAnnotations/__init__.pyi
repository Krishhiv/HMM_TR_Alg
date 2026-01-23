from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.ComponentModel
import System.ComponentModel.DataAnnotations
import System.Runtime.Serialization

IServiceProvider = typing.Any


class ValidationResult(System.Object):
    """This class has no documentation."""

    SUCCESS: System.ComponentModel.DataAnnotations.ValidationResult

    @property
    def member_names(self) -> typing.Iterable[str]:
        ...

    @property
    def error_message(self) -> str:
        ...

    @error_message.setter
    def error_message(self, value: str) -> None:
        ...

    @overload
    def __init__(self, error_message: str) -> None:
        ...

    @overload
    def __init__(self, error_message: str, member_names: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @overload
    def __init__(self, validation_result: System.ComponentModel.DataAnnotations.ValidationResult) -> None:
        ...

    def to_string(self) -> str:
        ...


class ValidationContext:
    """This class has no documentation."""

    @property
    def object_instance(self) -> System.Object:
        ...

    @property
    def object_type(self) -> typing.Type:
        ...

    @property
    def display_name(self) -> str:
        ...

    @display_name.setter
    def display_name(self, value: str) -> None:
        ...

    @property
    def member_name(self) -> str:
        ...

    @member_name.setter
    def member_name(self, value: str) -> None:
        ...

    @property
    def items(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        ...

    @overload
    def __init__(self, instance: typing.Any) -> None:
        ...

    @overload
    def __init__(self, instance: typing.Any, items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        ...

    @overload
    def __init__(self, instance: typing.Any, service_provider: typing.Optional[IServiceProvider], items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        ...

    @overload
    def __init__(self, instance: typing.Any, display_name: str, service_provider: typing.Optional[IServiceProvider], items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        ...

    def get_service(self, service_type: typing.Type) -> System.Object:
        ...

    def initialize_service_provider(self, service_provider: typing.Callable[[typing.Type], System.Object]) -> None:
        ...


class ValidationAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def error_message_string(self) -> str:
        ...

    @property
    def requires_validation_context(self) -> bool:
        ...

    @property
    def error_message(self) -> str:
        ...

    @error_message.setter
    def error_message(self, value: str) -> None:
        ...

    @property
    def error_message_resource_name(self) -> str:
        ...

    @error_message_resource_name.setter
    def error_message_resource_name(self, value: str) -> None:
        ...

    @property
    def error_message_resource_type(self) -> typing.Type:
        ...

    @error_message_resource_type.setter
    def error_message_resource_type(self, value: typing.Type) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, error_message: str) -> None:
        ...

    @overload
    def __init__(self, error_message_accessor: typing.Callable[[], str]) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def get_validation_result(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        ...

    @overload
    def is_valid(self, value: typing.Any) -> bool:
        ...

    @overload
    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        ...

    @overload
    def validate(self, value: typing.Any, name: str) -> None:
        ...

    @overload
    def validate(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        ...


class AllowedValuesAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def values(self) -> typing.List[System.Object]:
        ...

    def __init__(self, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class ScaffoldColumnAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def scaffold(self) -> bool:
        ...

    def __init__(self, scaffold: bool) -> None:
        ...


class AssociationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def this_key(self) -> str:
        ...

    @property
    def other_key(self) -> str:
        ...

    @property
    def is_foreign_key(self) -> bool:
        ...

    @is_foreign_key.setter
    def is_foreign_key(self, value: bool) -> None:
        ...

    @property
    def this_key_members(self) -> typing.Iterable[str]:
        ...

    @property
    def other_key_members(self) -> typing.Iterable[str]:
        ...

    def __init__(self, name: str, this_key: str, other_key: str) -> None:
        ...


class RangeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def minimum(self) -> System.Object:
        ...

    @property
    def maximum(self) -> System.Object:
        ...

    @property
    def minimum_is_exclusive(self) -> bool:
        ...

    @minimum_is_exclusive.setter
    def minimum_is_exclusive(self, value: bool) -> None:
        ...

    @property
    def maximum_is_exclusive(self) -> bool:
        ...

    @maximum_is_exclusive.setter
    def maximum_is_exclusive(self, value: bool) -> None:
        ...

    @property
    def operand_type(self) -> typing.Type:
        ...

    @property
    def parse_limits_in_invariant_culture(self) -> bool:
        ...

    @parse_limits_in_invariant_culture.setter
    def parse_limits_in_invariant_culture(self, value: bool) -> None:
        ...

    @property
    def convert_value_in_invariant_culture(self) -> bool:
        ...

    @convert_value_in_invariant_culture.setter
    def convert_value_in_invariant_culture(self, value: bool) -> None:
        ...

    @overload
    def __init__(self, minimum: int, maximum: int) -> None:
        ...

    @overload
    def __init__(self, minimum: float, maximum: float) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, minimum: str, maximum: str) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class DisplayColumnAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def display_column(self) -> str:
        ...

    @property
    def sort_column(self) -> str:
        ...

    @property
    def sort_descending(self) -> bool:
        ...

    @overload
    def __init__(self, display_column: str) -> None:
        ...

    @overload
    def __init__(self, display_column: str, sort_column: str) -> None:
        ...

    @overload
    def __init__(self, display_column: str, sort_column: str, sort_descending: bool) -> None:
        ...


class ConcurrencyCheckAttribute(System.Attribute):
    """This class has no documentation."""


class EditableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def allow_edit(self) -> bool:
        ...

    @property
    def allow_initial_value(self) -> bool:
        ...

    @allow_initial_value.setter
    def allow_initial_value(self, value: bool) -> None:
        ...

    def __init__(self, allow_edit: bool) -> None:
        ...


class DeniedValuesAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def values(self) -> typing.List[System.Object]:
        ...

    def __init__(self, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class ValidationException(System.Exception):
    """This class has no documentation."""

    @property
    def validation_attribute(self) -> System.ComponentModel.DataAnnotations.ValidationAttribute:
        ...

    @property
    def validation_result(self) -> System.ComponentModel.DataAnnotations.ValidationResult:
        ...

    @property
    def value(self) -> System.Object:
        ...

    @overload
    def __init__(self, validation_result: System.ComponentModel.DataAnnotations.ValidationResult, validating_attribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, error_message: str, validating_attribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        ...

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


class DisplayFormatAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def data_format_string(self) -> str:
        ...

    @data_format_string.setter
    def data_format_string(self, value: str) -> None:
        ...

    @property
    def null_display_text(self) -> str:
        ...

    @null_display_text.setter
    def null_display_text(self, value: str) -> None:
        ...

    @property
    def convert_empty_string_to_null(self) -> bool:
        ...

    @convert_empty_string_to_null.setter
    def convert_empty_string_to_null(self, value: bool) -> None:
        ...

    @property
    def apply_format_in_edit_mode(self) -> bool:
        ...

    @apply_format_in_edit_mode.setter
    def apply_format_in_edit_mode(self, value: bool) -> None:
        ...

    @property
    def html_encode(self) -> bool:
        ...

    @html_encode.setter
    def html_encode(self, value: bool) -> None:
        ...

    @property
    def null_display_text_resource_type(self) -> typing.Type:
        ...

    @null_display_text_resource_type.setter
    def null_display_text_resource_type(self, value: typing.Type) -> None:
        ...

    def __init__(self) -> None:
        ...

    def get_null_display_text(self) -> str:
        ...


class Base64StringAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class DataType(IntEnum):
    """This class has no documentation."""

    CUSTOM = 0

    DATE_TIME = 1

    DATE = 2

    TIME = 3

    DURATION = 4

    PHONE_NUMBER = 5

    CURRENCY = 6

    TEXT = 7

    HTML = 8

    MULTILINE_TEXT = 9

    EMAIL_ADDRESS = 10

    PASSWORD = 11

    URL = 12

    IMAGE_URL = 13

    CREDIT_CARD = 14

    POSTAL_CODE = 15

    UPLOAD = 16


class DataTypeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def data_type(self) -> System.ComponentModel.DataAnnotations.DataType:
        ...

    @property
    def custom_data_type(self) -> str:
        ...

    @property
    def display_format(self) -> System.ComponentModel.DataAnnotations.DisplayFormatAttribute:
        ...

    @display_format.setter
    def display_format(self, value: System.ComponentModel.DataAnnotations.DisplayFormatAttribute) -> None:
        ...

    @overload
    def __init__(self, data_type: System.ComponentModel.DataAnnotations.DataType) -> None:
        ...

    @overload
    def __init__(self, custom_data_type: str) -> None:
        ...

    def get_data_type_name(self) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class CreditCardAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class IValidatableObject(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def validate(self, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationResult]:
        ...


class RegularExpressionAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def match_timeout_in_milliseconds(self) -> int:
        ...

    @match_timeout_in_milliseconds.setter
    def match_timeout_in_milliseconds(self, value: int) -> None:
        ...

    @property
    def match_timeout(self) -> datetime.timedelta:
        ...

    @property
    def pattern(self) -> str:
        ...

    def __init__(self, pattern: str) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class MaxLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def length(self) -> int:
        ...

    @overload
    def __init__(self, length: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class AssociatedMetadataTypeTypeDescriptionProvider(System.ComponentModel.TypeDescriptionProvider):
    """This class has no documentation."""

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type, associated_metadata_type: typing.Type) -> None:
        ...

    def get_type_descriptor(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        ...


class UrlAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class UIHintAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def ui_hint(self) -> str:
        ...

    @property
    def presentation_layer(self) -> str:
        ...

    @property
    def control_parameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...

    @overload
    def __init__(self, ui_hint: str) -> None:
        ...

    @overload
    def __init__(self, ui_hint: str, presentation_layer: str) -> None:
        ...

    @overload
    def __init__(self, ui_hint: str, presentation_layer: str, *control_parameters: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CompareAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def other_property(self) -> str:
        ...

    @property
    def other_property_display_name(self) -> str:
        ...

    @property
    def requires_validation_context(self) -> bool:
        ...

    def __init__(self, other_property: str) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        ...


class EnumDataTypeAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def enum_type(self) -> typing.Type:
        ...

    def __init__(self, enum_type: typing.Type) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class StringLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def maximum_length(self) -> int:
        ...

    @property
    def minimum_length(self) -> int:
        ...

    @minimum_length.setter
    def minimum_length(self, value: int) -> None:
        ...

    def __init__(self, maximum_length: int) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class CustomValidationAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def validator_type(self) -> typing.Type:
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @property
    def method(self) -> str:
        ...

    @property
    def requires_validation_context(self) -> bool:
        ...

    def __init__(self, validator_type: typing.Type, method: str) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        ...


class TimestampAttribute(System.Attribute):
    """This class has no documentation."""


class KeyAttribute(System.Attribute):
    """This class has no documentation."""


class EmailAddressAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class FileExtensionsAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def extensions(self) -> str:
        ...

    @extensions.setter
    def extensions(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class LengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def minimum_length(self) -> int:
        ...

    @property
    def maximum_length(self) -> int:
        ...

    def __init__(self, minimum_length: int, maximum_length: int) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class FilterUIHintAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def filter_ui_hint(self) -> str:
        ...

    @property
    def presentation_layer(self) -> str:
        ...

    @property
    def control_parameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        ...

    @overload
    def __init__(self, filter_ui_hint: str) -> None:
        ...

    @overload
    def __init__(self, filter_ui_hint: str, presentation_layer: str) -> None:
        ...

    @overload
    def __init__(self, filter_ui_hint: str, presentation_layer: str, *control_parameters: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class PhoneAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class Validator(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def try_validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        ...

    @staticmethod
    @overload
    def try_validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validate_all_properties: bool) -> bool:
        ...

    @staticmethod
    def try_validate_property(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        ...

    @staticmethod
    def try_validate_value(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validation_attributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> bool:
        ...

    @staticmethod
    @overload
    def validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        ...

    @staticmethod
    @overload
    def validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validate_all_properties: bool) -> None:
        ...

    @staticmethod
    def validate_property(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        ...

    @staticmethod
    def validate_value(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_attributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> None:
        ...


class DisplayAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def short_name(self) -> str:
        ...

    @short_name.setter
    def short_name(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def description(self) -> str:
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def prompt(self) -> str:
        ...

    @prompt.setter
    def prompt(self, value: str) -> None:
        ...

    @property
    def group_name(self) -> str:
        ...

    @group_name.setter
    def group_name(self, value: str) -> None:
        ...

    @property
    def resource_type(self) -> typing.Type:
        ...

    @resource_type.setter
    def resource_type(self, value: typing.Type) -> None:
        ...

    @property
    def auto_generate_field(self) -> bool:
        ...

    @auto_generate_field.setter
    def auto_generate_field(self, value: bool) -> None:
        ...

    @property
    def auto_generate_filter(self) -> bool:
        ...

    @auto_generate_filter.setter
    def auto_generate_filter(self, value: bool) -> None:
        ...

    @property
    def order(self) -> int:
        ...

    @order.setter
    def order(self, value: int) -> None:
        ...

    def get_auto_generate_field(self) -> typing.Optional[bool]:
        ...

    def get_auto_generate_filter(self) -> typing.Optional[bool]:
        ...

    def get_description(self) -> str:
        ...

    def get_group_name(self) -> str:
        ...

    def get_name(self) -> str:
        ...

    def get_order(self) -> typing.Optional[int]:
        ...

    def get_prompt(self) -> str:
        ...

    def get_short_name(self) -> str:
        ...


class RequiredAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def allow_empty_strings(self) -> bool:
        ...

    @allow_empty_strings.setter
    def allow_empty_strings(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class MetadataTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def metadata_class_type(self) -> typing.Type:
        ...

    def __init__(self, metadata_class_type: typing.Type) -> None:
        ...


class MinLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def length(self) -> int:
        ...

    def __init__(self, length: int) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


