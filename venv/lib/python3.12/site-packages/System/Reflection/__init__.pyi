from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections.Generic
import System.Configuration.Assemblies
import System.Globalization
import System.IO
import System.Reflection
import System.Runtime.Serialization
import System.Security

System_Reflection_CustomAttributeTypedArgument = typing.Any
System_Reflection_CustomAttributeNamedArgument = typing.Any

System_Reflection__EventContainer_Callable = typing.TypeVar("System_Reflection__EventContainer_Callable")
System_Reflection__EventContainer_ReturnType = typing.TypeVar("System_Reflection__EventContainer_ReturnType")


class ExceptionHandlingClauseOptions(IntEnum):
    """This class has no documentation."""

    CLAUSE = ...

    FILTER = ...

    FINALLY = ...

    FAULT = ...


class AssemblyDefaultAliasAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def default_alias(self) -> str:
        ...

    def __init__(self, default_alias: str) -> None:
        ...


class CallingConventions(IntEnum):
    """This class has no documentation."""

    STANDARD = ...

    VAR_ARGS = ...

    ANY = ...

    HAS_THIS = ...

    EXPLICIT_THIS = ...


class ProcessorArchitecture(IntEnum):
    """This class has no documentation."""

    NONE = ...

    MSIL = ...

    X_86 = ...

    IA_64 = ...

    AMD_64 = ...

    ARM = ...


class IReflectableType(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_type_info(self) -> System.Reflection.TypeInfo:
        ...


class ICustomAttributeProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...


class MemberTypes(IntEnum):
    """This class has no documentation."""

    CONSTRUCTOR = ...

    EVENT = ...

    FIELD = ...

    METHOD = ...

    PROPERTY = ...

    TYPE_INFO = ...

    CUSTOM = ...

    NESTED_TYPE = ...

    ALL = ...


class MemberInfo(System.Object, System.Reflection.ICustomAttributeProvider, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def declaring_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def reflected_type(self) -> typing.Type:
        ...

    @property
    def module(self) -> System.Reflection.Module:
        ...

    @property
    def custom_attributes(self) -> typing.Iterable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def is_collectible(self) -> bool:
        ...

    @property
    def metadata_token(self) -> int:
        ...

    def __eq__(self, right: System.Reflection.MemberInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.MemberInfo) -> bool:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_custom_attributes_data(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def get_hash_code(self) -> int:
        ...

    def has_same_metadata_definition_as(self, other: System.Reflection.MemberInfo) -> bool:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...


class EventAttributes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    SPECIAL_NAME = ...

    RT_SPECIAL_NAME = ...

    RESERVED_MASK = ...


class MethodAttributes(IntEnum):
    """This class has no documentation."""

    MEMBER_ACCESS_MASK = ...

    PRIVATE_SCOPE = ...

    PRIVATE = ...

    FAM_AND_ASSEM = ...

    ASSEMBLY = ...

    FAMILY = ...

    FAM_OR_ASSEM = ...

    PUBLIC = ...

    STATIC = ...

    FINAL = ...

    VIRTUAL = ...

    HIDE_BY_SIG = ...

    CHECK_ACCESS_ON_OVERRIDE = ...

    VTABLE_LAYOUT_MASK = ...

    REUSE_SLOT = ...

    NEW_SLOT = ...

    ABSTRACT = ...

    SPECIAL_NAME = ...

    PINVOKE_IMPL = ...

    UNMANAGED_EXPORT = ...

    RT_SPECIAL_NAME = ...

    HAS_SECURITY = ...

    REQUIRE_SEC_OBJECT = ...

    RESERVED_MASK = ...


class MethodImplAttributes(IntEnum):
    """This class has no documentation."""

    CODE_TYPE_MASK = ...

    IL = ...

    NATIVE = ...

    OPTIL = ...

    RUNTIME = ...

    MANAGED_MASK = ...

    UNMANAGED = ...

    MANAGED = ...

    FORWARD_REF = ...

    PRESERVE_SIG = ...

    INTERNAL_CALL = ...

    SYNCHRONIZED = ...

    NO_INLINING = ...

    AGGRESSIVE_INLINING = ...

    NO_OPTIMIZATION = ...

    AGGRESSIVE_OPTIMIZATION = ...

    ASYNC = ...

    MAX_METHOD_IMPL_VAL = ...


class LocalVariableInfo(System.Object):
    """This class has no documentation."""

    @property
    def local_type(self) -> typing.Type:
        ...

    @property
    def local_index(self) -> int:
        ...

    @property
    def is_pinned(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def to_string(self) -> str:
        ...


class ExceptionHandlingClause(System.Object):
    """This class has no documentation."""

    @property
    def flags(self) -> System.Reflection.ExceptionHandlingClauseOptions:
        ...

    @property
    def try_offset(self) -> int:
        ...

    @property
    def try_length(self) -> int:
        ...

    @property
    def handler_offset(self) -> int:
        ...

    @property
    def handler_length(self) -> int:
        ...

    @property
    def filter_offset(self) -> int:
        ...

    @property
    def catch_type(self) -> typing.Type:
        ...

    def __init__(self) -> None:
        ...

    def to_string(self) -> str:
        ...


class MethodBody(System.Object):
    """This class has no documentation."""

    @property
    def local_signature_metadata_token(self) -> int:
        ...

    @property
    def local_variables(self) -> typing.List[System.Reflection.LocalVariableInfo]:
        ...

    @property
    def max_stack_size(self) -> int:
        ...

    @property
    def init_locals(self) -> bool:
        ...

    @property
    def exception_handling_clauses(self) -> typing.List[System.Reflection.ExceptionHandlingClause]:
        ...

    def __init__(self) -> None:
        ...

    def get_il_as_byte_array(self) -> typing.List[int]:
        ...


class BindingFlags(IntEnum):
    """This class has no documentation."""

    DEFAULT = ...

    IGNORE_CASE = ...

    DECLARED_ONLY = ...

    INSTANCE = ...

    STATIC = ...

    PUBLIC = ...

    NON_PUBLIC = ...

    FLATTEN_HIERARCHY = ...

    INVOKE_METHOD = ...

    CREATE_INSTANCE = ...

    GET_FIELD = ...

    SET_FIELD = ...

    GET_PROPERTY = ...

    SET_PROPERTY = ...

    PUT_DISP_PROPERTY = ...

    PUT_REF_DISP_PROPERTY = ...

    EXACT_BINDING = ...

    SUPPRESS_CHANGE_TYPE = ...

    OPTIONAL_PARAM_BINDING = ...

    IGNORE_RETURN = ...

    DO_NOT_WRAP_EXCEPTIONS = ...


class ParameterAttributes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    IN = ...

    OUT = ...

    LCID = ...

    RETVAL = ...

    OPTIONAL = ...

    HAS_DEFAULT = ...

    HAS_FIELD_MARSHAL = ...

    RESERVED_3 = ...

    RESERVED_4 = ...

    RESERVED_MASK = ...


class ParameterInfo(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.IObjectReference):
    """This class has no documentation."""

    @property
    def attributes(self) -> System.Reflection.ParameterAttributes:
        ...

    @property
    def member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def parameter_type(self) -> typing.Type:
        ...

    @property
    def position(self) -> int:
        ...

    @property
    def is_in(self) -> bool:
        ...

    @property
    def is_lcid(self) -> bool:
        ...

    @property
    def is_optional(self) -> bool:
        ...

    @property
    def is_out(self) -> bool:
        ...

    @property
    def is_retval(self) -> bool:
        ...

    @property
    def default_value(self) -> System.Object:
        ...

    @property
    def raw_default_value(self) -> System.Object:
        ...

    @property
    def has_default_value(self) -> bool:
        ...

    @property
    def custom_attributes(self) -> typing.Iterable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def metadata_token(self) -> int:
        ...

    @property
    def attrs_impl(self) -> System.Reflection.ParameterAttributes:
        ...

    @attrs_impl.setter
    def attrs_impl(self, value: System.Reflection.ParameterAttributes) -> None:
        ...

    @property
    def class_impl(self) -> typing.Type:
        ...

    @class_impl.setter
    def class_impl(self, value: typing.Type) -> None:
        ...

    @property
    def default_value_impl(self) -> System.Object:
        ...

    @default_value_impl.setter
    def default_value_impl(self, value: System.Object) -> None:
        ...

    @property
    def member_impl(self) -> System.Reflection.MemberInfo:
        ...

    @member_impl.setter
    def member_impl(self, value: System.Reflection.MemberInfo) -> None:
        ...

    @property
    def name_impl(self) -> str:
        ...

    @name_impl.setter
    def name_impl(self, value: str) -> None:
        ...

    @property
    def position_impl(self) -> int:
        ...

    @position_impl.setter
    def position_impl(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_custom_attributes_data(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def get_modified_parameter_type(self) -> typing.Type:
        ...

    def get_optional_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    def get_real_object(self, context: System.Runtime.Serialization.StreamingContext) -> System.Object:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_required_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def to_string(self) -> str:
        ...


class MethodBase(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def attributes(self) -> System.Reflection.MethodAttributes:
        ...

    @property
    def method_implementation_flags(self) -> System.Reflection.MethodImplAttributes:
        ...

    @property
    def calling_convention(self) -> System.Reflection.CallingConventions:
        ...

    @property
    def is_abstract(self) -> bool:
        ...

    @property
    def is_constructor(self) -> bool:
        ...

    @property
    def is_final(self) -> bool:
        ...

    @property
    def is_hide_by_sig(self) -> bool:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    def is_static(self) -> bool:
        ...

    @property
    def is_virtual(self) -> bool:
        ...

    @property
    def is_assembly(self) -> bool:
        ...

    @property
    def is_family(self) -> bool:
        ...

    @property
    def is_family_and_assembly(self) -> bool:
        ...

    @property
    def is_family_or_assembly(self) -> bool:
        ...

    @property
    def is_private(self) -> bool:
        ...

    @property
    def is_public(self) -> bool:
        ...

    @property
    def is_constructed_generic_method(self) -> bool:
        ...

    @property
    def is_generic_method(self) -> bool:
        ...

    @property
    def is_generic_method_definition(self) -> bool:
        ...

    @property
    def contains_generic_parameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def method_handle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def is_security_critical(self) -> bool:
        ...

    @property
    def is_security_safe_critical(self) -> bool:
        ...

    @property
    def is_security_transparent(self) -> bool:
        ...

    def __eq__(self, right: System.Reflection.MethodBase) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.MethodBase) -> bool:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    def get_current_method() -> System.Reflection.MethodBase:
        ...

    def get_generic_arguments(self) -> typing.List[typing.Type]:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_method_body(self) -> System.Reflection.MethodBody:
        ...

    @staticmethod
    @overload
    def get_method_from_handle(handle: System.RuntimeMethodHandle) -> System.Reflection.MethodBase:
        ...

    @staticmethod
    @overload
    def get_method_from_handle(handle: System.RuntimeMethodHandle, declaring_type: System.RuntimeTypeHandle) -> System.Reflection.MethodBase:
        ...

    def get_method_implementation_flags(self) -> System.Reflection.MethodImplAttributes:
        ...

    def get_parameters(self) -> typing.List[System.Reflection.ParameterInfo]:
        ...

    @overload
    def invoke(self, obj: typing.Any, parameters: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...


class MethodInfo(System.Reflection.MethodBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    def return_parameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def return_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def return_type_custom_attributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    def __eq__(self, right: System.Reflection.MethodInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.MethodInfo) -> bool:
        ...

    @overload
    def create_delegate(self, delegate_type: typing.Type, target: typing.Any) -> System.Delegate:
        ...

    @overload
    def create_delegate(self, delegate_type: typing.Type) -> System.Delegate:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_base_definition(self) -> System.Reflection.MethodInfo:
        ...

    def get_generic_arguments(self) -> typing.List[typing.Type]:
        ...

    def get_generic_method_definition(self) -> System.Reflection.MethodInfo:
        ...

    def get_hash_code(self) -> int:
        ...

    def make_generic_method(self, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> System.Reflection.MethodInfo:
        ...


class EventInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def attributes(self) -> System.Reflection.EventAttributes:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    def add_method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def remove_method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def raise_method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def is_multicast(self) -> bool:
        ...

    @property
    def event_handler_type(self) -> typing.Type:
        ...

    def __eq__(self, right: System.Reflection.EventInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.EventInfo) -> bool:
        ...

    def add_event_handler(self, target: typing.Any, handler: System.Delegate) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def get_add_method(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_add_method(self, non_public: bool) -> System.Reflection.MethodInfo:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_other_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_other_methods(self, non_public: bool) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_raise_method(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_raise_method(self, non_public: bool) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_remove_method(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_remove_method(self, non_public: bool) -> System.Reflection.MethodInfo:
        ...

    def remove_event_handler(self, target: typing.Any, handler: System.Delegate) -> None:
        ...


class FieldAttributes(IntEnum):
    """This class has no documentation."""

    FIELD_ACCESS_MASK = ...

    PRIVATE_SCOPE = ...

    PRIVATE = ...

    FAM_AND_ASSEM = ...

    ASSEMBLY = ...

    FAMILY = ...

    FAM_OR_ASSEM = ...

    PUBLIC = ...

    STATIC = ...

    INIT_ONLY = ...

    LITERAL = ...

    NOT_SERIALIZED = ...

    SPECIAL_NAME = ...

    PINVOKE_IMPL = ...

    RT_SPECIAL_NAME = ...

    HAS_FIELD_MARSHAL = ...

    HAS_DEFAULT = ...

    HAS_FIELD_RVA = ...

    RESERVED_MASK = ...


class FieldInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def attributes(self) -> System.Reflection.FieldAttributes:
        ...

    @property
    @abc.abstractmethod
    def field_type(self) -> typing.Type:
        ...

    @property
    def is_init_only(self) -> bool:
        ...

    @property
    def is_literal(self) -> bool:
        ...

    @property
    def is_not_serialized(self) -> bool:
        warnings.warn("Obsoletions.LegacyFormatterMessage", DeprecationWarning)

    @property
    def is_pinvoke_impl(self) -> bool:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    def is_static(self) -> bool:
        ...

    @property
    def is_assembly(self) -> bool:
        ...

    @property
    def is_family(self) -> bool:
        ...

    @property
    def is_family_and_assembly(self) -> bool:
        ...

    @property
    def is_family_or_assembly(self) -> bool:
        ...

    @property
    def is_private(self) -> bool:
        ...

    @property
    def is_public(self) -> bool:
        ...

    @property
    def is_security_critical(self) -> bool:
        ...

    @property
    def is_security_safe_critical(self) -> bool:
        ...

    @property
    def is_security_transparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def field_handle(self) -> System.RuntimeFieldHandle:
        ...

    def __eq__(self, right: System.Reflection.FieldInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.FieldInfo) -> bool:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def get_field_from_handle(handle: System.RuntimeFieldHandle) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    @overload
    def get_field_from_handle(handle: System.RuntimeFieldHandle, declaring_type: System.RuntimeTypeHandle) -> System.Reflection.FieldInfo:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_modified_field_type(self) -> typing.Type:
        ...

    def get_optional_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    def get_raw_constant_value(self) -> System.Object:
        ...

    def get_required_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    def get_value(self, obj: typing.Any) -> System.Object:
        ...

    def get_value_direct(self, obj: System.TypedReference) -> System.Object:
        ...

    @overload
    def set_value(self, obj: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def set_value(self, obj: typing.Any, value: typing.Any, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, culture: System.Globalization.CultureInfo) -> None:
        ...

    def set_value_direct(self, obj: System.TypedReference, value: typing.Any) -> None:
        ...


class PropertyAttributes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    SPECIAL_NAME = ...

    RT_SPECIAL_NAME = ...

    HAS_DEFAULT = ...

    RESERVED_2 = ...

    RESERVED_3 = ...

    RESERVED_4 = ...

    RESERVED_MASK = ...


class PropertyInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def property_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def attributes(self) -> System.Reflection.PropertyAttributes:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_read(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_write(self) -> bool:
        ...

    @property
    def get_method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def set_method(self) -> System.Reflection.MethodInfo:
        ...

    def __eq__(self, right: System.Reflection.PropertyInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.PropertyInfo) -> bool:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def get_accessors(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_accessors(self, non_public: bool) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def get_constant_value(self) -> System.Object:
        ...

    @overload
    def get_get_method(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_get_method(self, non_public: bool) -> System.Reflection.MethodInfo:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_index_parameters(self) -> typing.List[System.Reflection.ParameterInfo]:
        ...

    def get_modified_property_type(self) -> typing.Type:
        ...

    def get_optional_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    def get_raw_constant_value(self) -> System.Object:
        ...

    def get_required_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_set_method(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_set_method(self, non_public: bool) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_value(self, obj: typing.Any) -> System.Object:
        ...

    @overload
    def get_value(self, obj: typing.Any, index: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def get_value(self, obj: typing.Any, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @overload
    def set_value(self, obj: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def set_value(self, obj: typing.Any, value: typing.Any, index: typing.List[System.Object]) -> None:
        ...

    @overload
    def set_value(self, obj: typing.Any, value: typing.Any, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> None:
        ...


class ParameterModifier:
    """This class has no documentation."""

    def __getitem__(self, index: int) -> bool:
        ...

    def __init__(self, parameter_count: int) -> None:
        ...

    def __setitem__(self, index: int, value: bool) -> None:
        ...


class Binder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def bind_to_field(self, binding_attr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.FieldInfo], value: typing.Any, culture: System.Globalization.CultureInfo) -> System.Reflection.FieldInfo:
        ...

    def bind_to_method(self, binding_attr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.MethodBase], args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, names: typing.List[str], state: typing.Optional[typing.Any]) -> typing.Tuple[System.Reflection.MethodBase, typing.Any]:
        ...

    def change_type(self, value: typing.Any, type: typing.Type, culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    def reorder_argument_array(self, args: typing.List[System.Object], state: typing.Any) -> None:
        ...

    def select_method(self, binding_attr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.MethodBase], types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodBase:
        ...

    def select_property(self, binding_attr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.PropertyInfo], return_type: typing.Type, indexes: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...


class ConstructorInfo(System.Reflection.MethodBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    CONSTRUCTOR_NAME: str = ".ctor"

    TYPE_CONSTRUCTOR_NAME: str = ".cctor"

    def __eq__(self, right: System.Reflection.ConstructorInfo) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.ConstructorInfo) -> bool:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def invoke(self, parameters: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def invoke(self, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...


class TypeInfo(typing.Type, System.Reflection.IReflectableType, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def generic_type_parameters(self) -> typing.List[typing.Type]:
        ...

    @property
    def declared_constructors(self) -> typing.Iterable[System.Reflection.ConstructorInfo]:
        ...

    @property
    def declared_events(self) -> typing.Iterable[System.Reflection.EventInfo]:
        ...

    @property
    def declared_fields(self) -> typing.Iterable[System.Reflection.FieldInfo]:
        ...

    @property
    def declared_members(self) -> typing.Iterable[System.Reflection.MemberInfo]:
        ...

    @property
    def declared_methods(self) -> typing.Iterable[System.Reflection.MethodInfo]:
        ...

    @property
    def declared_nested_types(self) -> typing.Iterable[System.Reflection.TypeInfo]:
        ...

    @property
    def declared_properties(self) -> typing.Iterable[System.Reflection.PropertyInfo]:
        ...

    @property
    def implemented_interfaces(self) -> typing.Iterable[typing.Type]:
        ...

    def __init__(self) -> None:
        ...

    def as_type(self) -> typing.Type:
        ...

    def get_declared_event(self, name: str) -> System.Reflection.EventInfo:
        ...

    def get_declared_field(self, name: str) -> System.Reflection.FieldInfo:
        ...

    def get_declared_method(self, name: str) -> System.Reflection.MethodInfo:
        ...

    def get_declared_methods(self, name: str) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    def get_declared_nested_type(self, name: str) -> System.Reflection.TypeInfo:
        ...

    def get_declared_property(self, name: str) -> System.Reflection.PropertyInfo:
        ...

    def is_assignable_from(self, type_info: System.Reflection.TypeInfo) -> bool:
        ...


class ResourceLocation(IntEnum):
    """This class has no documentation."""

    CONTAINED_IN_ANOTHER_ASSEMBLY = 2

    CONTAINED_IN_MANIFEST_FILE = 4

    EMBEDDED = 1


class ManifestResourceInfo(System.Object):
    """This class has no documentation."""

    @property
    def referenced_assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def file_name(self) -> str:
        ...

    @property
    def resource_location(self) -> System.Reflection.ResourceLocation:
        ...

    def __init__(self, containing_assembly: System.Reflection.Assembly, containing_file_name: str, resource_location: System.Reflection.ResourceLocation) -> None:
        ...


class AssemblyContentType(IntEnum):
    """This class has no documentation."""

    DEFAULT = 0

    WINDOWS_RUNTIME = 1


class AssemblyNameFlags(IntEnum):
    """This class has no documentation."""

    NONE = ...

    PUBLIC_KEY = ...

    ENABLE_JI_TCOMPILE_OPTIMIZER = ...

    ENABLE_JI_TCOMPILE_TRACKING = ...

    RETARGETABLE = ...


class StrongNameKeyPair(System.Object, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def public_key(self) -> typing.List[int]:
        ...

    @overload
    def __init__(self, key_pair_file: System.IO.FileStream) -> None:
        ...

    @overload
    def __init__(self, key_pair_array: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, key_pair_container: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class AssemblyName(System.Object, System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def version(self) -> System.Version:
        ...

    @version.setter
    def version(self, value: System.Version) -> None:
        ...

    @property
    def culture_info(self) -> System.Globalization.CultureInfo:
        ...

    @culture_info.setter
    def culture_info(self, value: System.Globalization.CultureInfo) -> None:
        ...

    @property
    def culture_name(self) -> str:
        ...

    @culture_name.setter
    def culture_name(self, value: str) -> None:
        ...

    @property
    def code_base(self) -> str:
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @code_base.setter
    def code_base(self, value: str) -> None:
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @property
    def escaped_code_base(self) -> str:
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @property
    def processor_architecture(self) -> System.Reflection.ProcessorArchitecture:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @processor_architecture.setter
    def processor_architecture(self, value: System.Reflection.ProcessorArchitecture) -> None:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def content_type(self) -> System.Reflection.AssemblyContentType:
        ...

    @content_type.setter
    def content_type(self, value: System.Reflection.AssemblyContentType) -> None:
        ...

    @property
    def flags(self) -> System.Reflection.AssemblyNameFlags:
        ...

    @flags.setter
    def flags(self, value: System.Reflection.AssemblyNameFlags) -> None:
        ...

    @property
    def hash_algorithm(self) -> System.Reflection.AssemblyHashAlgorithm:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @hash_algorithm.setter
    def hash_algorithm(self, value: System.Reflection.AssemblyHashAlgorithm) -> None:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def version_compatibility(self) -> System.Configuration.Assemblies.AssemblyVersionCompatibility:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @version_compatibility.setter
    def version_compatibility(self, value: System.Configuration.Assemblies.AssemblyVersionCompatibility) -> None:
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def key_pair(self) -> System.Reflection.StrongNameKeyPair:
        warnings.warn("Obsoletions.StrongNameKeyPairMessage", DeprecationWarning)

    @key_pair.setter
    def key_pair(self, value: System.Reflection.StrongNameKeyPair) -> None:
        warnings.warn("Obsoletions.StrongNameKeyPairMessage", DeprecationWarning)

    @property
    def full_name(self) -> str:
        ...

    @overload
    def __init__(self, assembly_name: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    def get_assembly_name(assembly_file: str) -> System.Reflection.AssemblyName:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_public_key(self) -> typing.List[int]:
        ...

    def get_public_key_token(self) -> typing.List[int]:
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    @staticmethod
    def reference_matches_definition(reference: System.Reflection.AssemblyName, definition: System.Reflection.AssemblyName) -> bool:
        ...

    def set_public_key(self, public_key: typing.List[int]) -> None:
        ...

    def set_public_key_token(self, public_key_token: typing.List[int]) -> None:
        ...

    def to_string(self) -> str:
        ...


class CustomAttributeTypedArgument(System.IEquatable[System_Reflection_CustomAttributeTypedArgument]):
    """This class has no documentation."""

    @property
    def argument_type(self) -> typing.Type:
        ...

    @property
    def value(self) -> System.Object:
        ...

    def __eq__(self, right: System.Reflection.CustomAttributeTypedArgument) -> bool:
        ...

    @overload
    def __init__(self, argument_type: typing.Type, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    def __ne__(self, right: System.Reflection.CustomAttributeTypedArgument) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Reflection.CustomAttributeTypedArgument) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CustomAttributeNamedArgument(System.IEquatable[System_Reflection_CustomAttributeNamedArgument]):
    """This class has no documentation."""

    @property
    def member_info(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def typed_value(self) -> System.Reflection.CustomAttributeTypedArgument:
        ...

    @property
    def member_name(self) -> str:
        ...

    @property
    def is_field(self) -> bool:
        ...

    def __eq__(self, right: System.Reflection.CustomAttributeNamedArgument) -> bool:
        ...

    @overload
    def __init__(self, member_info: System.Reflection.MemberInfo, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, member_info: System.Reflection.MemberInfo, typed_argument: System.Reflection.CustomAttributeTypedArgument) -> None:
        ...

    def __ne__(self, right: System.Reflection.CustomAttributeNamedArgument) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Reflection.CustomAttributeNamedArgument) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CustomAttributeData(System.Object):
    """This class has no documentation."""

    @property
    def attribute_type(self) -> typing.Type:
        ...

    @property
    def constructor(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def constructor_arguments(self) -> typing.List[System.Reflection.CustomAttributeTypedArgument]:
        ...

    @property
    def named_arguments(self) -> typing.List[System.Reflection.CustomAttributeNamedArgument]:
        ...

    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(target: System.Reflection.MemberInfo) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(target: System.Reflection.Module) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(target: System.Reflection.Assembly) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(target: System.Reflection.ParameterInfo) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def to_string(self) -> str:
        ...


class Assembly(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def defined_types(self) -> typing.Iterable[System.Reflection.TypeInfo]:
        ...

    @property
    def exported_types(self) -> typing.Iterable[typing.Type]:
        ...

    @property
    def code_base(self) -> str:
        warnings.warn("Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location.", DeprecationWarning)

    @property
    def entry_point(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def full_name(self) -> str:
        ...

    @property
    def image_runtime_version(self) -> str:
        ...

    @property
    def is_dynamic(self) -> bool:
        ...

    @property
    def location(self) -> str:
        ...

    @property
    def reflection_only(self) -> bool:
        ...

    @property
    def is_collectible(self) -> bool:
        ...

    @property
    def is_fully_trusted(self) -> bool:
        ...

    @property
    def custom_attributes(self) -> typing.Iterable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def escaped_code_base(self) -> str:
        warnings.warn("Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location.", DeprecationWarning)

    @property
    def module_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Module], System.Reflection.Module]:
        ...

    @module_resolve.setter
    def module_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Module], System.Reflection.Module]) -> None:
        ...

    @property
    def manifest_module(self) -> System.Reflection.Module:
        ...

    @property
    def modules(self) -> typing.Iterable[System.Reflection.Module]:
        ...

    @property
    def global_assembly_cache(self) -> bool:
        warnings.warn("Obsoletions.GlobalAssemblyCacheMessage", DeprecationWarning)

    @property
    def host_context(self) -> int:
        ...

    @property
    def security_rule_set(self) -> System.Security.SecurityRuleSet:
        ...

    def __eq__(self, right: System.Reflection.Assembly) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.Assembly) -> bool:
        ...

    @overload
    def create_instance(self, type_name: str) -> System.Object:
        ...

    @overload
    def create_instance(self, type_name: str, ignore_case: bool) -> System.Object:
        ...

    @overload
    def create_instance(self, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    def create_qualified_name(assembly_name: str, type_name: str) -> str:
        ...

    def equals(self, o: typing.Any) -> bool:
        ...

    @staticmethod
    def get_assembly(type: typing.Type) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def get_calling_assembly() -> System.Reflection.Assembly:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_custom_attributes_data(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    def get_entry_assembly() -> System.Reflection.Assembly:
        ...

    @staticmethod
    def get_executing_assembly() -> System.Reflection.Assembly:
        ...

    def get_exported_types(self) -> typing.List[typing.Type]:
        ...

    def get_file(self, name: str) -> System.IO.FileStream:
        ...

    @overload
    def get_files(self) -> typing.List[System.IO.FileStream]:
        ...

    @overload
    def get_files(self, get_resource_modules: bool) -> typing.List[System.IO.FileStream]:
        ...

    def get_forwarded_types(self) -> typing.List[typing.Type]:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_loaded_modules(self) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def get_loaded_modules(self, get_resource_modules: bool) -> typing.List[System.Reflection.Module]:
        ...

    def get_manifest_resource_info(self, resource_name: str) -> System.Reflection.ManifestResourceInfo:
        ...

    def get_manifest_resource_names(self) -> typing.List[str]:
        ...

    @overload
    def get_manifest_resource_stream(self, name: str) -> System.IO.Stream:
        ...

    @overload
    def get_manifest_resource_stream(self, type: typing.Type, name: str) -> System.IO.Stream:
        ...

    def get_module(self, name: str) -> System.Reflection.Module:
        ...

    @overload
    def get_modules(self) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def get_modules(self, get_resource_modules: bool) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def get_name(self) -> System.Reflection.AssemblyName:
        ...

    @overload
    def get_name(self, copied_name: bool) -> System.Reflection.AssemblyName:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_referenced_assemblies(self) -> typing.List[System.Reflection.AssemblyName]:
        ...

    @overload
    def get_satellite_assembly(self, culture: System.Globalization.CultureInfo) -> System.Reflection.Assembly:
        ...

    @overload
    def get_satellite_assembly(self, culture: System.Globalization.CultureInfo, version: System.Version) -> System.Reflection.Assembly:
        ...

    @overload
    def get_type(self, name: str) -> typing.Type:
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool) -> typing.Type:
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    def get_types(self) -> typing.List[typing.Type]:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def load(raw_assembly: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def load(raw_assembly: typing.List[int], raw_symbol_store: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def load(assembly_string: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def load(assembly_ref: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def load_file(path: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def load_from(assembly_file: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def load_from(assembly_file: str, hash_value: typing.List[int], hash_algorithm: System.Reflection.AssemblyHashAlgorithm) -> System.Reflection.Assembly:
        ...

    @overload
    def load_module(self, module_name: str, raw_module: typing.List[int]) -> System.Reflection.Module:
        ...

    @overload
    def load_module(self, module_name: str, raw_module: typing.List[int], raw_symbol_store: typing.List[int]) -> System.Reflection.Module:
        ...

    @staticmethod
    def load_with_partial_name(partial_name: str) -> System.Reflection.Assembly:
        warnings.warn("Assembly.LoadWithPartialName has been deprecated. Use Assembly.Load() instead.", DeprecationWarning)

    @staticmethod
    @overload
    def reflection_only_load(raw_assembly: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def reflection_only_load(assembly_string: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def reflection_only_load_from(assembly_file: str) -> System.Reflection.Assembly:
        warnings.warn("Obsoletions.ReflectionOnlyLoadingMessage", DeprecationWarning)

    @staticmethod
    def set_entry_assembly(assembly: System.Reflection.Assembly) -> None:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def unsafe_load_from(assembly_file: str) -> System.Reflection.Assembly:
        ...


class PortableExecutableKinds(IntEnum):
    """This class has no documentation."""

    NOT_A_PORTABLE_EXECUTABLE_IMAGE = ...

    IL_ONLY = ...

    REQUIRED_32_BIT = ...

    PE_32_PLUS = ...

    UNMANAGED_32_BIT = ...

    PREFERRED_32_BIT = ...


class ImageFileMachine(IntEnum):
    """This class has no documentation."""

    I_386 = ...

    IA_64 = ...

    AMD_64 = ...

    ARM = ...


class Module(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def fully_qualified_name(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def md_stream_version(self) -> int:
        ...

    @property
    def module_version_id(self) -> System.Guid:
        ...

    @property
    def scope_name(self) -> str:
        ...

    @property
    def module_handle(self) -> System.ModuleHandle:
        ...

    @property
    def custom_attributes(self) -> typing.Iterable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def metadata_token(self) -> int:
        ...

    FILTER_TYPE_NAME: typing.Callable[[typing.Type, System.Object], bool] = ...

    FILTER_TYPE_NAME_IGNORE_CASE: typing.Callable[[typing.Type, System.Object], bool] = ...

    def __eq__(self, right: System.Reflection.Module) -> bool:
        ...

    def __init__(self) -> None:
        ...

    def __ne__(self, right: System.Reflection.Module) -> bool:
        ...

    def equals(self, o: typing.Any) -> bool:
        ...

    def find_types(self, filter: typing.Callable[[typing.Type, System.Object], bool], filter_criteria: typing.Any) -> typing.List[typing.Type]:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_custom_attributes_data(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @overload
    def get_field(self, name: str) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_field(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_fields(self) -> typing.List[System.Reflection.FieldInfo]:
        ...

    @overload
    def get_fields(self, binding_flags: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_method(self, name: str) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    def get_method_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_methods(self, binding_flags: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_pe_kind(self, pe_kind: typing.Optional[System.Reflection.PortableExecutableKinds], machine: typing.Optional[System.Reflection.ImageFileMachine]) -> typing.Tuple[None, System.Reflection.PortableExecutableKinds, System.Reflection.ImageFileMachine]:
        ...

    @overload
    def get_type(self, class_name: str) -> typing.Type:
        ...

    @overload
    def get_type(self, class_name: str, ignore_case: bool) -> typing.Type:
        ...

    @overload
    def get_type(self, class_name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    def get_types(self) -> typing.List[typing.Type]:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def is_resource(self) -> bool:
        ...

    @overload
    def resolve_field(self, metadata_token: int) -> System.Reflection.FieldInfo:
        ...

    @overload
    def resolve_field(self, metadata_token: int, generic_type_arguments: typing.List[typing.Type], generic_method_arguments: typing.List[typing.Type]) -> System.Reflection.FieldInfo:
        ...

    @overload
    def resolve_member(self, metadata_token: int) -> System.Reflection.MemberInfo:
        ...

    @overload
    def resolve_member(self, metadata_token: int, generic_type_arguments: typing.List[typing.Type], generic_method_arguments: typing.List[typing.Type]) -> System.Reflection.MemberInfo:
        ...

    @overload
    def resolve_method(self, metadata_token: int) -> System.Reflection.MethodBase:
        ...

    @overload
    def resolve_method(self, metadata_token: int, generic_type_arguments: typing.List[typing.Type], generic_method_arguments: typing.List[typing.Type]) -> System.Reflection.MethodBase:
        ...

    def resolve_signature(self, metadata_token: int) -> typing.List[int]:
        ...

    def resolve_string(self, metadata_token: int) -> str:
        ...

    @overload
    def resolve_type(self, metadata_token: int) -> typing.Type:
        ...

    @overload
    def resolve_type(self, metadata_token: int, generic_type_arguments: typing.List[typing.Type], generic_method_arguments: typing.List[typing.Type]) -> typing.Type:
        ...

    def to_string(self) -> str:
        ...


class TargetException(System.ApplicationException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class AssemblyInformationalVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def informational_version(self) -> str:
        ...

    def __init__(self, informational_version: str) -> None:
        ...


class ReflectionTypeLoadException(System.SystemException):
    """This class has no documentation."""

    @property
    def types(self) -> typing.List[typing.Type]:
        ...

    @property
    def loader_exceptions(self) -> typing.List[System.Exception]:
        ...

    @property
    def message(self) -> str:
        ...

    @overload
    def __init__(self, classes: typing.List[typing.Type], exceptions: typing.List[System.Exception]) -> None:
        ...

    @overload
    def __init__(self, classes: typing.List[typing.Type], exceptions: typing.List[System.Exception], message: str) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class AssemblyCopyrightAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def copyright(self) -> str:
        ...

    def __init__(self, copyright: str) -> None:
        ...


class AssemblyMetadataAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def key(self) -> str:
        ...

    @property
    def value(self) -> str:
        ...

    def __init__(self, key: str, value: str) -> None:
        ...


class TargetInvocationException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class ConstructorInvoker(System.Object):
    """This class has no documentation."""

    @staticmethod
    def create(constructor: System.Reflection.ConstructorInfo) -> System.Reflection.ConstructorInvoker:
        ...

    @overload
    def invoke(self, arg_1: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, arg_1: typing.Any, arg_2: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, arg_1: typing.Any, arg_2: typing.Any, arg_3: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, arg_1: typing.Any, arg_2: typing.Any, arg_3: typing.Any, arg_4: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self) -> System.Object:
        ...

    @overload
    def invoke(self, arguments: System.Span[System.Object]) -> System.Object:
        ...


class AssemblyProductAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def product(self) -> str:
        ...

    def __init__(self, product: str) -> None:
        ...


class AssemblyCompanyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def company(self) -> str:
        ...

    def __init__(self, company: str) -> None:
        ...


class AssemblyFlagsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def flags(self) -> int:
        warnings.warn("AssemblyFlagsAttribute.Flags has been deprecated. Use AssemblyFlags instead.", DeprecationWarning)

    @property
    def assembly_flags(self) -> int:
        ...

    @overload
    def __init__(self, assembly_flags: System.Reflection.AssemblyNameFlags) -> None:
        ...

    @overload
    def __init__(self, flags: int) -> None:
        ...

    @overload
    def __init__(self, assembly_flags: int) -> None:
        ...


class AssemblyKeyFileAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def key_file(self) -> str:
        ...

    def __init__(self, key_file: str) -> None:
        ...


class AssemblySignatureKeyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def public_key(self) -> str:
        ...

    @property
    def countersignature(self) -> str:
        ...

    def __init__(self, public_key: str, countersignature: str) -> None:
        ...


class GenericParameterAttributes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    VARIANCE_MASK = ...

    COVARIANT = ...

    CONTRAVARIANT = ...

    SPECIAL_CONSTRAINT_MASK = ...

    REFERENCE_TYPE_CONSTRAINT = ...

    NOT_NULLABLE_VALUE_TYPE_CONSTRAINT = ...

    DEFAULT_CONSTRUCTOR_CONSTRAINT = ...

    ALLOW_BY_REF_LIKE = ...


class AmbiguousMatchException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class AssemblyNameProxy(System.MarshalByRefObject):
    """This class has no documentation."""

    def get_assembly_name(self, assembly_file: str) -> System.Reflection.AssemblyName:
        ...


class AssemblyKeyNameAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def key_name(self) -> str:
        ...

    def __init__(self, key_name: str) -> None:
        ...


class AssemblyVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def version(self) -> str:
        ...

    def __init__(self, version: str) -> None:
        ...


class CustomAttributeExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Assembly, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Module, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, attribute_type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, attribute_type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Assembly, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Module, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...


class ReflectionContext(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def get_type_for_object(self, value: typing.Any) -> System.Reflection.TypeInfo:
        ...

    def map_assembly(self, assembly: System.Reflection.Assembly) -> System.Reflection.Assembly:
        ...

    def map_type(self, type: System.Reflection.TypeInfo) -> System.Reflection.TypeInfo:
        ...


class TypeAttributes(IntEnum):
    """This class has no documentation."""

    VISIBILITY_MASK = ...

    NOT_PUBLIC = ...

    PUBLIC = ...

    NESTED_PUBLIC = ...

    NESTED_PRIVATE = ...

    NESTED_FAMILY = ...

    NESTED_ASSEMBLY = ...

    NESTED_FAM_AND_ASSEM = ...

    NESTED_FAM_OR_ASSEM = ...

    LAYOUT_MASK = ...

    AUTO_LAYOUT = ...

    SEQUENTIAL_LAYOUT = ...

    EXPLICIT_LAYOUT = ...

    EXTENDED_LAYOUT = ...

    CLASS_SEMANTICS_MASK = ...

    CLASS = ...

    INTERFACE = ...

    ABSTRACT = ...

    SEALED = ...

    SPECIAL_NAME = ...

    IMPORT = ...

    SERIALIZABLE = ...

    WINDOWS_RUNTIME = ...

    STRING_FORMAT_MASK = ...

    ANSI_CLASS = ...

    UNICODE_CLASS = ...

    AUTO_CLASS = ...

    CUSTOM_FORMAT_CLASS = ...

    CUSTOM_FORMAT_MASK = ...

    BEFORE_FIELD_INIT = ...

    RT_SPECIAL_NAME = ...

    HAS_SECURITY = ...

    RESERVED_MASK = ...


class InterfaceMapping:
    """This class has no documentation."""

    @property
    def target_type(self) -> typing.Type:
        ...

    @target_type.setter
    def target_type(self, value: typing.Type) -> None:
        ...

    @property
    def interface_type(self) -> typing.Type:
        ...

    @interface_type.setter
    def interface_type(self, value: typing.Type) -> None:
        ...

    @property
    def target_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @target_methods.setter
    def target_methods(self, value: typing.List[System.Reflection.MethodInfo]) -> None:
        ...

    @property
    def interface_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @interface_methods.setter
    def interface_methods(self, value: typing.List[System.Reflection.MethodInfo]) -> None:
        ...


class TypeDelegator(System.Reflection.TypeInfo):
    """This class has no documentation."""

    @property
    def type_impl(self) -> typing.Type:
        ...

    @type_impl.setter
    def type_impl(self, value: typing.Type) -> None:
        ...

    @property
    def guid(self) -> System.Guid:
        ...

    @property
    def metadata_token(self) -> int:
        ...

    @property
    def module(self) -> System.Reflection.Module:
        ...

    @property
    def assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def type_handle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def full_name(self) -> str:
        ...

    @property
    def namespace(self) -> str:
        ...

    @property
    def assembly_qualified_name(self) -> str:
        ...

    @property
    def base_type(self) -> typing.Type:
        ...

    @property
    def is_type_definition(self) -> bool:
        ...

    @property
    def is_sz_array(self) -> bool:
        ...

    @property
    def is_variable_bound_array(self) -> bool:
        ...

    @property
    def is_generic_type_parameter(self) -> bool:
        ...

    @property
    def is_generic_method_parameter(self) -> bool:
        ...

    @property
    def is_by_ref_like(self) -> bool:
        ...

    @property
    def is_constructed_generic_type(self) -> bool:
        ...

    @property
    def is_collectible(self) -> bool:
        ...

    @property
    def is_function_pointer(self) -> bool:
        ...

    @property
    def is_unmanaged_function_pointer(self) -> bool:
        ...

    @property
    def underlying_system_type(self) -> typing.Type:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, delegating_type: typing.Type) -> None:
        ...

    def get_array_rank(self) -> int:
        ...

    def get_attribute_flags_impl(self) -> System.Reflection.TypeAttributes:
        ...

    def get_constructor_impl(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    def get_constructors(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_element_type(self) -> typing.Type:
        ...

    def get_event(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.EventInfo:
        ...

    @overload
    def get_events(self) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def get_events(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.EventInfo]:
        ...

    def get_field(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    def get_fields(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def get_function_pointer_calling_conventions(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_parameter_types(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_return_type(self) -> typing.Type:
        ...

    def get_interface(self, name: str, ignore_case: bool) -> typing.Type:
        ...

    def get_interface_map(self, interface_type: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    def get_interfaces(self) -> typing.List[typing.Type]:
        ...

    def get_member(self, name: str, type: System.Reflection.MemberTypes, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_members(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_member_with_same_metadata_definition_as(self, member: System.Reflection.MemberInfo) -> System.Reflection.MemberInfo:
        ...

    def get_method_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    def get_methods(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def get_nested_type(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.Type:
        ...

    def get_nested_types(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[typing.Type]:
        ...

    def get_properties(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    def get_property_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def has_element_type_impl(self) -> bool:
        ...

    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, named_parameters: typing.List[str]) -> System.Object:
        ...

    def is_array_impl(self) -> bool:
        ...

    def is_assignable_from(self, type_info: System.Reflection.TypeInfo) -> bool:
        ...

    def is_by_ref_impl(self) -> bool:
        ...

    def is_com_object_impl(self) -> bool:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def is_pointer_impl(self) -> bool:
        ...

    def is_primitive_impl(self) -> bool:
        ...

    def is_value_type_impl(self) -> bool:
        ...


class ObfuscateAssemblyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def assembly_is_private(self) -> bool:
        ...

    @property
    def strip_after_obfuscation(self) -> bool:
        ...

    @strip_after_obfuscation.setter
    def strip_after_obfuscation(self, value: bool) -> None:
        ...

    def __init__(self, assembly_is_private: bool) -> None:
        ...


class AssemblyFileVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def version(self) -> str:
        ...

    def __init__(self, version: str) -> None:
        ...


class Pointer(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def box(ptr: typing.Any, type: typing.Type) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def unbox(ptr: typing.Any) -> typing.Any:
        ...


class ResourceAttributes(IntEnum):
    """This class has no documentation."""

    PUBLIC = ...

    PRIVATE = ...


class AssemblyAlgorithmIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def algorithm_id(self) -> int:
        ...

    @overload
    def __init__(self, algorithm_id: System.Reflection.AssemblyHashAlgorithm) -> None:
        ...

    @overload
    def __init__(self, algorithm_id: int) -> None:
        ...


class DefaultMemberAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def member_name(self) -> str:
        ...

    def __init__(self, member_name: str) -> None:
        ...


class AssemblyDescriptionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def description(self) -> str:
        ...

    def __init__(self, description: str) -> None:
        ...


class CustomAttributeFormatException(System.FormatException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class InvalidFilterCriteriaException(System.ApplicationException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class IntrospectionExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_type_info(type: typing.Type) -> System.Reflection.TypeInfo:
        ...


class IReflect(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def underlying_system_type(self) -> typing.Type:
        ...

    def get_field(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    def get_fields(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def get_member(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_members(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.MethodInfo:
        ...

    def get_methods(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def get_properties(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, named_parameters: typing.List[str]) -> System.Object:
        ...


class Missing(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    VALUE: System.Reflection.Missing = ...


class TargetParameterCountException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class AssemblyTitleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def title(self) -> str:
        ...

    def __init__(self, title: str) -> None:
        ...


class MethodInvoker(System.Object):
    """This class has no documentation."""

    @staticmethod
    def create(method: System.Reflection.MethodBase) -> System.Reflection.MethodInvoker:
        ...

    @overload
    def invoke(self, obj: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, arg_1: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, arg_1: typing.Any, arg_2: typing.Any, arg_3: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, arg_1: typing.Any, arg_2: typing.Any, arg_3: typing.Any, arg_4: typing.Any) -> System.Object:
        ...

    @overload
    def invoke(self, obj: typing.Any, arguments: System.Span[System.Object]) -> System.Object:
        ...


class ObfuscationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def strip_after_obfuscation(self) -> bool:
        ...

    @strip_after_obfuscation.setter
    def strip_after_obfuscation(self, value: bool) -> None:
        ...

    @property
    def exclude(self) -> bool:
        ...

    @exclude.setter
    def exclude(self, value: bool) -> None:
        ...

    @property
    def apply_to_members(self) -> bool:
        ...

    @apply_to_members.setter
    def apply_to_members(self, value: bool) -> None:
        ...

    @property
    def feature(self) -> str:
        ...

    @feature.setter
    def feature(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...


class AssemblyDelaySignAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def delay_sign(self) -> bool:
        ...

    def __init__(self, delay_sign: bool) -> None:
        ...


class RuntimeReflectionExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_runtime_base_definition(method: System.Reflection.MethodInfo) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def get_runtime_event(type: typing.Type, name: str) -> System.Reflection.EventInfo:
        ...

    @staticmethod
    def get_runtime_events(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.EventInfo]:
        ...

    @staticmethod
    def get_runtime_field(type: typing.Type, name: str) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    def get_runtime_fields(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.FieldInfo]:
        ...

    @staticmethod
    def get_runtime_interface_map(type_info: System.Reflection.TypeInfo, interface_type: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    @staticmethod
    def get_runtime_method(type: typing.Type, name: str, parameters: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def get_runtime_methods(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    @staticmethod
    def get_runtime_properties(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @staticmethod
    def get_runtime_property(type: typing.Type, name: str) -> System.Reflection.PropertyInfo:
        ...


class AssemblyConfigurationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def configuration(self) -> str:
        ...

    def __init__(self, configuration: str) -> None:
        ...


class AssemblyCultureAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def culture(self) -> str:
        ...

    def __init__(self, culture: str) -> None:
        ...


class AssemblyTrademarkAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def trademark(self) -> str:
        ...

    def __init__(self, trademark: str) -> None:
        ...


class ICustomTypeProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_custom_type(self) -> typing.Type:
        ...


class _EventContainer(typing.Generic[System_Reflection__EventContainer_Callable, System_Reflection__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Reflection__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Reflection__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Reflection__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


