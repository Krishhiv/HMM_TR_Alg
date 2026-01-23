from typing import overload
from enum import IntEnum
import abc
import typing
import warnings

import System
import System.Collections.Generic
import System.Diagnostics.SymbolStore
import System.Globalization
import System.IO
import System.Reflection
import System.Reflection.Emit
import System.Runtime.InteropServices

System_Reflection_Emit_OpCode = typing.Any
System_Reflection_Emit_Label = typing.Any


class FieldBuilder(System.Reflection.FieldInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def set_constant(self, default_value: typing.Any) -> None:
        ...

    def set_constant_core(self, default_value: typing.Any) -> None:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_offset(self, i_offset: int) -> None:
        ...

    def set_offset_core(self, i_offset: int) -> None:
        ...


class EnumBuilder(System.Reflection.TypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def underlying_field(self) -> System.Reflection.Emit.FieldBuilder:
        ...

    @property
    @abc.abstractmethod
    def underlying_field_core(self) -> System.Reflection.Emit.FieldBuilder:
        ...

    def __init__(self) -> None:
        ...

    def create_type(self) -> typing.Type:
        ...

    def create_type_info(self) -> System.Reflection.TypeInfo:
        ...

    def create_type_info_core(self) -> System.Reflection.TypeInfo:
        ...

    def define_literal(self, literal_name: str, literal_value: typing.Any) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_literal_core(self, literal_name: str, literal_value: typing.Any) -> System.Reflection.Emit.FieldBuilder:
        ...

    @overload
    def make_array_type(self) -> typing.Type:
        ...

    @overload
    def make_array_type(self, rank: int) -> typing.Type:
        ...

    def make_by_ref_type(self) -> typing.Type:
        ...

    def make_pointer_type(self) -> typing.Type:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...


class PEFileKinds(IntEnum):
    """This class has no documentation."""

    DLL = ...

    CONSOLE_APPLICATION = ...

    WINDOW_APPLICATION = ...


class PackingSize(IntEnum):
    """This class has no documentation."""

    UNSPECIFIED = 0

    SIZE_1 = 1

    SIZE_2 = 2

    SIZE_4 = 4

    SIZE_8 = 8

    SIZE_16 = 16

    SIZE_32 = 32

    SIZE_64 = 64

    SIZE_128 = 128


class ParameterBuilder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def attributes(self) -> int:
        ...

    @property
    def is_in(self) -> bool:
        ...

    @property
    def is_optional(self) -> bool:
        ...

    @property
    def is_out(self) -> bool:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def position(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    def set_constant(self, default_value: typing.Any) -> None:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...


class Label(System.IEquatable[System_Reflection_Emit_Label]):
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    def __eq__(self, b: System.Reflection.Emit.Label) -> bool:
        ...

    def __ne__(self, b: System.Reflection.Emit.Label) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Reflection.Emit.Label) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class OperandType(IntEnum):
    """This class has no documentation."""

    INLINE_BR_TARGET = 0

    INLINE_FIELD = 1

    INLINE_I = 2

    INLINE_I_8 = 3

    INLINE_METHOD = 4

    INLINE_NONE = 5

    INLINE_PHI = 6

    INLINE_R = 7

    INLINE_SIG = 9

    INLINE_STRING = 10

    INLINE_SWITCH = 11

    INLINE_TOK = 12

    INLINE_TYPE = 13

    INLINE_VAR = 14

    SHORT_INLINE_BR_TARGET = 15

    SHORT_INLINE_I = 16

    SHORT_INLINE_R = 17

    SHORT_INLINE_VAR = 18


class FlowControl(IntEnum):
    """This class has no documentation."""

    BRANCH = 0

    BREAK = 1

    CALL = 2

    COND_BRANCH = 3

    META = 4

    NEXT = 5

    PHI = 6

    RETURN = 7

    THROW = 8


class OpCodeType(IntEnum):
    """This class has no documentation."""

    ANNOTATION = 0

    MACRO = 1

    NTERNAL = 2

    OBJMODEL = 3

    PREFIX = 4

    PRIMITIVE = 5


class StackBehaviour(IntEnum):
    """This class has no documentation."""

    POP_0 = 0

    POP_1 = 1

    POP_1_POP_1 = 2

    POPI = 3

    POPI_POP_1 = 4

    POPI_POPI = 5

    POPI_POPI_8 = 6

    POPI_POPI_POPI = 7

    POPI_POPR_4 = 8

    POPI_POPR_8 = 9

    POPREF = 10

    POPREF_POP_1 = 11

    POPREF_POPI = 12

    POPREF_POPI_POPI = 13

    POPREF_POPI_POPI_8 = 14

    POPREF_POPI_POPR_4 = 15

    POPREF_POPI_POPR_8 = 16

    POPREF_POPI_POPREF = 17

    PUSH_0 = 18

    PUSH_1 = 19

    PUSH_1_PUSH_1 = 20

    PUSHI = 21

    PUSHI_8 = 22

    PUSHR_4 = 23

    PUSHR_8 = 24

    PUSHREF = 25

    VARPOP = 26

    VARPUSH = 27

    POPREF_POPI_POP_1 = 28


class OpCode(System.IEquatable[System_Reflection_Emit_OpCode]):
    """This class has no documentation."""

    @property
    def evaluation_stack_delta(self) -> int:
        ...

    @property
    def operand_type(self) -> System.Reflection.Emit.OperandType:
        ...

    @property
    def flow_control(self) -> System.Reflection.Emit.FlowControl:
        ...

    @property
    def op_code_type(self) -> System.Reflection.Emit.OpCodeType:
        ...

    @property
    def stack_behaviour_pop(self) -> System.Reflection.Emit.StackBehaviour:
        ...

    @property
    def stack_behaviour_push(self) -> System.Reflection.Emit.StackBehaviour:
        ...

    @property
    def size(self) -> int:
        ...

    @property
    def value(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    def __eq__(self, b: System.Reflection.Emit.OpCode) -> bool:
        ...

    def __ne__(self, b: System.Reflection.Emit.OpCode) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Reflection.Emit.OpCode) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class LocalBuilder(System.Reflection.LocalVariableInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def set_local_sym_info(self, name: str) -> None:
        ...

    def set_local_sym_info_core(self, name: str) -> None:
        ...


class ILGenerator(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def il_offset(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    def begin_catch_block(self, exception_type: typing.Type) -> None:
        ...

    def begin_except_filter_block(self) -> None:
        ...

    def begin_exception_block(self) -> System.Reflection.Emit.Label:
        ...

    def begin_fault_block(self) -> None:
        ...

    def begin_finally_block(self) -> None:
        ...

    def begin_scope(self) -> None:
        ...

    @staticmethod
    def create_label(id: int) -> System.Reflection.Emit.Label:
        ...

    @overload
    def declare_local(self, local_type: typing.Type) -> System.Reflection.Emit.LocalBuilder:
        ...

    @overload
    def declare_local(self, local_type: typing.Type, pinned: bool) -> System.Reflection.Emit.LocalBuilder:
        ...

    def define_label(self) -> System.Reflection.Emit.Label:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, arg: int) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, arg: float) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, meth: System.Reflection.MethodInfo) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, signature: System.Reflection.Emit.SignatureHelper) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, con: System.Reflection.ConstructorInfo) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, cls: typing.Type) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, label: System.Reflection.Emit.Label) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, labels: typing.List[System.Reflection.Emit.Label]) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, field: System.Reflection.FieldInfo) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, str: str) -> None:
        ...

    @overload
    def emit(self, opcode: System.Reflection.Emit.OpCode, local: System.Reflection.Emit.LocalBuilder) -> None:
        ...

    def emit_call(self, opcode: System.Reflection.Emit.OpCode, method_info: System.Reflection.MethodInfo, optional_parameter_types: typing.List[typing.Type]) -> None:
        ...

    @overload
    def emit_calli(self, opcode: System.Reflection.Emit.OpCode, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], optional_parameter_types: typing.List[typing.Type]) -> None:
        ...

    @overload
    def emit_calli(self, opcode: System.Reflection.Emit.OpCode, unmanaged_call_conv: System.Runtime.InteropServices.CallingConvention, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> None:
        ...

    @overload
    def emit_write_line(self, value: str) -> None:
        ...

    @overload
    def emit_write_line(self, local_builder: System.Reflection.Emit.LocalBuilder) -> None:
        ...

    @overload
    def emit_write_line(self, fld: System.Reflection.FieldInfo) -> None:
        ...

    def end_exception_block(self) -> None:
        ...

    def end_scope(self) -> None:
        ...

    def mark_label(self, loc: System.Reflection.Emit.Label) -> None:
        ...

    def mark_sequence_point(self, document: System.Diagnostics.SymbolStore.ISymbolDocumentWriter, start_line: int, start_column: int, end_line: int, end_column: int) -> None:
        ...

    def mark_sequence_point_core(self, document: System.Diagnostics.SymbolStore.ISymbolDocumentWriter, start_line: int, start_column: int, end_line: int, end_column: int) -> None:
        ...

    def throw_exception(self, exc_type: typing.Type) -> None:
        ...

    def using_namespace(self, using_namespace: str) -> None:
        ...


class GenericTypeParameterBuilder(System.Reflection.TypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def set_base_type_constraint(self, base_type_constraint: typing.Type) -> None:
        ...

    def set_base_type_constraint_core(self, base_type_constraint: typing.Type) -> None:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_generic_parameter_attributes(self, generic_parameter_attributes: System.Reflection.GenericParameterAttributes) -> None:
        ...

    def set_generic_parameter_attributes_core(self, generic_parameter_attributes: System.Reflection.GenericParameterAttributes) -> None:
        ...

    def set_interface_constraints(self, *interface_constraints: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> None:
        ...

    def set_interface_constraints_core(self, *interface_constraints: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> None:
        ...


class MethodBuilder(System.Reflection.MethodInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def init_locals(self) -> bool:
        ...

    @init_locals.setter
    def init_locals(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def init_locals_core(self) -> bool:
        ...

    @init_locals_core.setter
    def init_locals_core(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...

    def define_generic_parameters(self, *names: typing.Union[str, typing.Iterable[str]]) -> typing.List[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def define_generic_parameters_core(self, *names: typing.Union[str, typing.Iterable[str]]) -> typing.List[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def define_parameter(self, position: int, attributes: System.Reflection.ParameterAttributes, str_param_name: str) -> System.Reflection.Emit.ParameterBuilder:
        ...

    def define_parameter_core(self, position: int, attributes: System.Reflection.ParameterAttributes, str_param_name: str) -> System.Reflection.Emit.ParameterBuilder:
        ...

    @overload
    def get_il_generator(self) -> System.Reflection.Emit.ILGenerator:
        ...

    @overload
    def get_il_generator(self, size: int) -> System.Reflection.Emit.ILGenerator:
        ...

    def get_il_generator_core(self, size: int) -> System.Reflection.Emit.ILGenerator:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_implementation_flags(self, attributes: System.Reflection.MethodImplAttributes) -> None:
        ...

    def set_implementation_flags_core(self, attributes: System.Reflection.MethodImplAttributes) -> None:
        ...

    def set_parameters(self, *parameter_types: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> None:
        ...

    def set_return_type(self, return_type: typing.Type) -> None:
        ...

    def set_signature(self, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> None:
        ...

    def set_signature_core(self, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> None:
        ...


class PropertyBuilder(System.Reflection.PropertyInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def add_other_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def add_other_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_constant(self, default_value: typing.Any) -> None:
        ...

    def set_constant_core(self, default_value: typing.Any) -> None:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_get_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_get_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_set_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_set_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...


class ConstructorBuilder(System.Reflection.ConstructorInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def init_locals(self) -> bool:
        ...

    @init_locals.setter
    def init_locals(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def init_locals_core(self) -> bool:
        ...

    @init_locals_core.setter
    def init_locals_core(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...

    def define_parameter(self, i_sequence: int, attributes: System.Reflection.ParameterAttributes, str_param_name: str) -> System.Reflection.Emit.ParameterBuilder:
        ...

    def define_parameter_core(self, i_sequence: int, attributes: System.Reflection.ParameterAttributes, str_param_name: str) -> System.Reflection.Emit.ParameterBuilder:
        ...

    @overload
    def get_il_generator(self) -> System.Reflection.Emit.ILGenerator:
        ...

    @overload
    def get_il_generator(self, stream_size: int) -> System.Reflection.Emit.ILGenerator:
        ...

    def get_il_generator_core(self, stream_size: int) -> System.Reflection.Emit.ILGenerator:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_implementation_flags(self, attributes: System.Reflection.MethodImplAttributes) -> None:
        ...

    def set_implementation_flags_core(self, attributes: System.Reflection.MethodImplAttributes) -> None:
        ...


class EventBuilder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def add_other_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def add_other_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_add_on_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_add_on_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_raise_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_raise_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_remove_on_method(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...

    def set_remove_on_method_core(self, md_builder: System.Reflection.Emit.MethodBuilder) -> None:
        ...


class TypeBuilder(System.Reflection.TypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    UNSPECIFIED_TYPE_SIZE: int = 0

    @property
    def packing_size(self) -> System.Reflection.Emit.PackingSize:
        ...

    @property
    @abc.abstractmethod
    def packing_size_core(self) -> System.Reflection.Emit.PackingSize:
        ...

    @property
    def size(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def size_core(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    def add_interface_implementation(self, interface_type: typing.Type) -> None:
        ...

    def add_interface_implementation_core(self, interface_type: typing.Type) -> None:
        ...

    def create_type(self) -> typing.Type:
        ...

    def create_type_info(self) -> System.Reflection.TypeInfo:
        ...

    def create_type_info_core(self) -> System.Reflection.TypeInfo:
        ...

    @overload
    def define_constructor(self, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    @overload
    def define_constructor(self, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, parameter_types: typing.List[typing.Type], required_custom_modifiers: typing.List[typing.List[typing.Type]], optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_constructor_core(self, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, parameter_types: typing.List[typing.Type], required_custom_modifiers: typing.List[typing.List[typing.Type]], optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_default_constructor(self, attributes: System.Reflection.MethodAttributes) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_default_constructor_core(self, attributes: System.Reflection.MethodAttributes) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_event(self, name: str, attributes: System.Reflection.EventAttributes, eventtype: typing.Type) -> System.Reflection.Emit.EventBuilder:
        ...

    def define_event_core(self, name: str, attributes: System.Reflection.EventAttributes, eventtype: typing.Type) -> System.Reflection.Emit.EventBuilder:
        ...

    @overload
    def define_field(self, field_name: str, type: typing.Type, attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    @overload
    def define_field(self, field_name: str, type: typing.Type, required_custom_modifiers: typing.List[typing.Type], optional_custom_modifiers: typing.List[typing.Type], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_field_core(self, field_name: str, type: typing.Type, required_custom_modifiers: typing.List[typing.Type], optional_custom_modifiers: typing.List[typing.Type], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_generic_parameters(self, *names: typing.Union[str, typing.Iterable[str]]) -> typing.List[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def define_generic_parameters_core(self, *names: typing.Union[str, typing.Iterable[str]]) -> typing.List[System.Reflection.Emit.GenericTypeParameterBuilder]:
        ...

    def define_initialized_data(self, name: str, data: typing.List[int], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_initialized_data_core(self, name: str, data: typing.List[int], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    @overload
    def define_method(self, name: str, attributes: System.Reflection.MethodAttributes) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_method(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_method(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_method(self, name: str, attributes: System.Reflection.MethodAttributes, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_method(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_method_core(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_method_override(self, method_info_body: System.Reflection.MethodInfo, method_info_declaration: System.Reflection.MethodInfo) -> None:
        ...

    def define_method_override_core(self, method_info_body: System.Reflection.MethodInfo, method_info_declaration: System.Reflection.MethodInfo) -> None:
        ...

    @overload
    def define_nested_type(self, name: str) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, interfaces: typing.List[typing.Type]) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, type_size: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, pack_size: System.Reflection.Emit.PackingSize) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_nested_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, pack_size: System.Reflection.Emit.PackingSize, type_size: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    def define_nested_type_core(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, interfaces: typing.List[typing.Type], pack_size: System.Reflection.Emit.PackingSize, type_size: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_p_invoke_method(self, name: str, dll_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_p_invoke_method(self, name: str, dll_name: str, entry_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_p_invoke_method(self, name: str, dll_name: str, entry_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_p_invoke_method_core(self, name: str, dll_name: str, entry_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_property(self, name: str, attributes: System.Reflection.PropertyAttributes, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @overload
    def define_property(self, name: str, attributes: System.Reflection.PropertyAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @overload
    def define_property(self, name: str, attributes: System.Reflection.PropertyAttributes, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.PropertyBuilder:
        ...

    @overload
    def define_property(self, name: str, attributes: System.Reflection.PropertyAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.PropertyBuilder:
        ...

    def define_property_core(self, name: str, attributes: System.Reflection.PropertyAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, return_type_required_custom_modifiers: typing.List[typing.Type], return_type_optional_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], parameter_type_required_custom_modifiers: typing.List[typing.List[typing.Type]], parameter_type_optional_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.PropertyBuilder:
        ...

    def define_type_initializer(self) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_type_initializer_core(self) -> System.Reflection.Emit.ConstructorBuilder:
        ...

    def define_uninitialized_data(self, name: str, size: int, attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_uninitialized_data_core(self, name: str, size: int, attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    @staticmethod
    def get_constructor(type: typing.Type, constructor: System.Reflection.ConstructorInfo) -> System.Reflection.ConstructorInfo:
        ...

    @staticmethod
    def get_field(type: typing.Type, field: System.Reflection.FieldInfo) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    def get_method(type: typing.Type, method: System.Reflection.MethodInfo) -> System.Reflection.MethodInfo:
        ...

    def is_created(self) -> bool:
        ...

    def is_created_core(self) -> bool:
        ...

    @overload
    def make_array_type(self) -> typing.Type:
        ...

    @overload
    def make_array_type(self, rank: int) -> typing.Type:
        ...

    def make_by_ref_type(self) -> typing.Type:
        ...

    def make_generic_type(self, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> typing.Type:
        ...

    def make_pointer_type(self) -> typing.Type:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...

    def set_parent(self, parent: typing.Type) -> None:
        ...

    def set_parent_core(self, parent: typing.Type) -> None:
        ...


class ModuleBuilder(System.Reflection.Module, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def create_global_functions(self) -> None:
        ...

    def create_global_functions_core(self) -> None:
        ...

    @overload
    def define_document(self, url: str, language: System.Guid, language_vendor: System.Guid, document_type: System.Guid) -> System.Diagnostics.SymbolStore.ISymbolDocumentWriter:
        ...

    @overload
    def define_document(self, url: str, language: System.Guid = ...) -> System.Diagnostics.SymbolStore.ISymbolDocumentWriter:
        ...

    def define_document_core(self, url: str, language: System.Guid = ...) -> System.Diagnostics.SymbolStore.ISymbolDocumentWriter:
        ...

    def define_enum(self, name: str, visibility: System.Reflection.TypeAttributes, underlying_type: typing.Type) -> System.Reflection.Emit.EnumBuilder:
        ...

    def define_enum_core(self, name: str, visibility: System.Reflection.TypeAttributes, underlying_type: typing.Type) -> System.Reflection.Emit.EnumBuilder:
        ...

    @overload
    def define_global_method(self, name: str, attributes: System.Reflection.MethodAttributes, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_global_method(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_global_method(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, required_return_type_custom_modifiers: typing.List[typing.Type], optional_return_type_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], required_parameter_type_custom_modifiers: typing.List[typing.List[typing.Type]], optional_parameter_type_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_global_method_core(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, required_return_type_custom_modifiers: typing.List[typing.Type], optional_return_type_custom_modifiers: typing.List[typing.Type], parameter_types: typing.List[typing.Type], required_parameter_type_custom_modifiers: typing.List[typing.List[typing.Type]], optional_parameter_type_custom_modifiers: typing.List[typing.List[typing.Type]]) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_initialized_data(self, name: str, data: typing.List[int], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_initialized_data_core(self, name: str, data: typing.List[int], attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    @overload
    def define_p_invoke_method(self, name: str, dll_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_p_invoke_method(self, name: str, dll_name: str, entry_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    def define_p_invoke_method_core(self, name: str, dll_name: str, entry_name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], native_call_conv: System.Runtime.InteropServices.CallingConvention, native_char_set: System.Runtime.InteropServices.CharSet) -> System.Reflection.Emit.MethodBuilder:
        ...

    @overload
    def define_type(self, name: str) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, interfaces: typing.List[typing.Type]) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, typesize: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, packsize: System.Reflection.Emit.PackingSize) -> System.Reflection.Emit.TypeBuilder:
        ...

    @overload
    def define_type(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, packing_size: System.Reflection.Emit.PackingSize, typesize: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    def define_type_core(self, name: str, attr: System.Reflection.TypeAttributes, parent: typing.Type, interfaces: typing.List[typing.Type], packing_size: System.Reflection.Emit.PackingSize, typesize: int) -> System.Reflection.Emit.TypeBuilder:
        ...

    def define_uninitialized_data(self, name: str, size: int, attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def define_uninitialized_data_core(self, name: str, size: int, attributes: System.Reflection.FieldAttributes) -> System.Reflection.Emit.FieldBuilder:
        ...

    def get_array_method(self, array_class: typing.Type, method_name: str, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    def get_array_method_core(self, array_class: typing.Type, method_name: str, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    def get_field_metadata_token(self, field: System.Reflection.FieldInfo) -> int:
        ...

    @overload
    def get_method_metadata_token(self, method: System.Reflection.MethodInfo) -> int:
        ...

    @overload
    def get_method_metadata_token(self, constructor: System.Reflection.ConstructorInfo) -> int:
        ...

    def get_signature_metadata_token(self, signature: System.Reflection.Emit.SignatureHelper) -> int:
        ...

    def get_string_metadata_token(self, string_constant: str) -> int:
        ...

    def get_type_metadata_token(self, type: typing.Type) -> int:
        ...

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...


class AssemblyBuilderAccess(IntEnum):
    """This class has no documentation."""

    RUN = 1

    RUN_AND_COLLECT = ...


class AssemblyBuilder(System.Reflection.Assembly, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def code_base(self) -> str:
        warnings.warn("Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location instead.", DeprecationWarning)

    @property
    def location(self) -> str:
        ...

    @property
    def entry_point(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def is_dynamic(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def define_dynamic_assembly(name: System.Reflection.AssemblyName, access: System.Reflection.Emit.AssemblyBuilderAccess) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    @staticmethod
    @overload
    def define_dynamic_assembly(name: System.Reflection.AssemblyName, access: System.Reflection.Emit.AssemblyBuilderAccess, assembly_attributes: System.Collections.Generic.IEnumerable[System.Reflection.Emit.CustomAttributeBuilder]) -> System.Reflection.Emit.AssemblyBuilder:
        ...

    def define_dynamic_module(self, name: str) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def define_dynamic_module_core(self, name: str) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def get_dynamic_module(self, name: str) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def get_dynamic_module_core(self, name: str) -> System.Reflection.Emit.ModuleBuilder:
        ...

    def get_exported_types(self) -> typing.List[typing.Type]:
        ...

    def get_file(self, name: str) -> System.IO.FileStream:
        ...

    def get_files(self, get_resource_modules: bool) -> typing.List[System.IO.FileStream]:
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

    @overload
    def set_custom_attribute(self, con: System.Reflection.ConstructorInfo, binary_attribute: typing.List[int]) -> None:
        ...

    @overload
    def set_custom_attribute(self, custom_builder: System.Reflection.Emit.CustomAttributeBuilder) -> None:
        ...

    def set_custom_attribute_core(self, con: System.Reflection.ConstructorInfo, binary_attribute: System.ReadOnlySpan[int]) -> None:
        ...


class DynamicMethod(System.Reflection.MethodInfo):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def declaring_type(self) -> typing.Type:
        ...

    @property
    def reflected_type(self) -> typing.Type:
        ...

    @property
    def module(self) -> System.Reflection.Module:
        ...

    @property
    def method_handle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def attributes(self) -> System.Reflection.MethodAttributes:
        ...

    @property
    def calling_convention(self) -> System.Reflection.CallingConventions:
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
    def return_type(self) -> typing.Type:
        ...

    @property
    def return_parameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def return_type_custom_attributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    @property
    def init_locals(self) -> bool:
        ...

    @init_locals.setter
    def init_locals(self, value: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type]) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type], restricted_skip_visibility: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type], m: System.Reflection.Module) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type], m: System.Reflection.Module, skip_visibility: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], m: System.Reflection.Module, skip_visibility: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type], owner: typing.Type) -> None:
        ...

    @overload
    def __init__(self, name: str, return_type: typing.Type, parameter_types: typing.List[typing.Type], owner: typing.Type, skip_visibility: bool) -> None:
        ...

    @overload
    def __init__(self, name: str, attributes: System.Reflection.MethodAttributes, calling_convention: System.Reflection.CallingConventions, return_type: typing.Type, parameter_types: typing.List[typing.Type], owner: typing.Type, skip_visibility: bool) -> None:
        ...

    @overload
    def create_delegate(self, delegate_type: typing.Type, target: typing.Any) -> System.Delegate:
        ...

    @overload
    def create_delegate(self, delegate_type: typing.Type) -> System.Delegate:
        ...

    def define_parameter(self, position: int, attributes: System.Reflection.ParameterAttributes, parameter_name: str) -> System.Reflection.Emit.ParameterBuilder:
        ...

    def get_base_definition(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_custom_attributes(self, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def get_custom_attributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    def get_dynamic_il_info(self) -> System.Reflection.Emit.DynamicILInfo:
        ...

    @overload
    def get_il_generator(self) -> System.Reflection.Emit.ILGenerator:
        ...

    @overload
    def get_il_generator(self, stream_size: int) -> System.Reflection.Emit.ILGenerator:
        ...

    def get_method_implementation_flags(self) -> System.Reflection.MethodImplAttributes:
        ...

    def get_parameters(self) -> typing.List[System.Reflection.ParameterInfo]:
        ...

    def invoke(self, obj: typing.Any, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    def is_defined(self, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def to_string(self) -> str:
        ...


class OpCodes(System.Object):
    """This class has no documentation."""

    NOP: System.Reflection.Emit.OpCode = ...

    BREAK: System.Reflection.Emit.OpCode = ...

    LDARG_0: System.Reflection.Emit.OpCode = ...

    LDARG_1: System.Reflection.Emit.OpCode = ...

    LDARG_2: System.Reflection.Emit.OpCode = ...

    LDARG_3: System.Reflection.Emit.OpCode = ...

    LDLOC_0: System.Reflection.Emit.OpCode = ...

    LDLOC_1: System.Reflection.Emit.OpCode = ...

    LDLOC_2: System.Reflection.Emit.OpCode = ...

    LDLOC_3: System.Reflection.Emit.OpCode = ...

    STLOC_0: System.Reflection.Emit.OpCode = ...

    STLOC_1: System.Reflection.Emit.OpCode = ...

    STLOC_2: System.Reflection.Emit.OpCode = ...

    STLOC_3: System.Reflection.Emit.OpCode = ...

    LDARG_S: System.Reflection.Emit.OpCode = ...

    LDARGA_S: System.Reflection.Emit.OpCode = ...

    STARG_S: System.Reflection.Emit.OpCode = ...

    LDLOC_S: System.Reflection.Emit.OpCode = ...

    LDLOCA_S: System.Reflection.Emit.OpCode = ...

    STLOC_S: System.Reflection.Emit.OpCode = ...

    LDNULL: System.Reflection.Emit.OpCode = ...

    LDC_I_4_M_1: System.Reflection.Emit.OpCode = ...

    LDC_I_4_0: System.Reflection.Emit.OpCode = ...

    LDC_I_4_1: System.Reflection.Emit.OpCode = ...

    LDC_I_4_2: System.Reflection.Emit.OpCode = ...

    LDC_I_4_3: System.Reflection.Emit.OpCode = ...

    LDC_I_4_4: System.Reflection.Emit.OpCode = ...

    LDC_I_4_5: System.Reflection.Emit.OpCode = ...

    LDC_I_4_6: System.Reflection.Emit.OpCode = ...

    LDC_I_4_7: System.Reflection.Emit.OpCode = ...

    LDC_I_4_8: System.Reflection.Emit.OpCode = ...

    LDC_I_4_S: System.Reflection.Emit.OpCode = ...

    LDC_I_4: System.Reflection.Emit.OpCode = ...

    LDC_I_8: System.Reflection.Emit.OpCode = ...

    LDC_R_4: System.Reflection.Emit.OpCode = ...

    LDC_R_8: System.Reflection.Emit.OpCode = ...

    DUP: System.Reflection.Emit.OpCode = ...

    POP: System.Reflection.Emit.OpCode = ...

    JMP: System.Reflection.Emit.OpCode = ...

    CALL: System.Reflection.Emit.OpCode = ...

    CALLI: System.Reflection.Emit.OpCode = ...

    RET: System.Reflection.Emit.OpCode = ...

    BR_S: System.Reflection.Emit.OpCode = ...

    BRFALSE_S: System.Reflection.Emit.OpCode = ...

    BRTRUE_S: System.Reflection.Emit.OpCode = ...

    BEQ_S: System.Reflection.Emit.OpCode = ...

    BGE_S: System.Reflection.Emit.OpCode = ...

    BGT_S: System.Reflection.Emit.OpCode = ...

    BLE_S: System.Reflection.Emit.OpCode = ...

    BLT_S: System.Reflection.Emit.OpCode = ...

    BNE_UN_S: System.Reflection.Emit.OpCode = ...

    BGE_UN_S: System.Reflection.Emit.OpCode = ...

    BGT_UN_S: System.Reflection.Emit.OpCode = ...

    BLE_UN_S: System.Reflection.Emit.OpCode = ...

    BLT_UN_S: System.Reflection.Emit.OpCode = ...

    BR: System.Reflection.Emit.OpCode = ...

    BRFALSE: System.Reflection.Emit.OpCode = ...

    BRTRUE: System.Reflection.Emit.OpCode = ...

    BEQ: System.Reflection.Emit.OpCode = ...

    BGE: System.Reflection.Emit.OpCode = ...

    BGT: System.Reflection.Emit.OpCode = ...

    BLE: System.Reflection.Emit.OpCode = ...

    BLT: System.Reflection.Emit.OpCode = ...

    BNE_UN: System.Reflection.Emit.OpCode = ...

    BGE_UN: System.Reflection.Emit.OpCode = ...

    BGT_UN: System.Reflection.Emit.OpCode = ...

    BLE_UN: System.Reflection.Emit.OpCode = ...

    BLT_UN: System.Reflection.Emit.OpCode = ...

    SWITCH: System.Reflection.Emit.OpCode = ...

    LDIND_I_1: System.Reflection.Emit.OpCode = ...

    LDIND_U_1: System.Reflection.Emit.OpCode = ...

    LDIND_I_2: System.Reflection.Emit.OpCode = ...

    LDIND_U_2: System.Reflection.Emit.OpCode = ...

    LDIND_I_4: System.Reflection.Emit.OpCode = ...

    LDIND_U_4: System.Reflection.Emit.OpCode = ...

    LDIND_I_8: System.Reflection.Emit.OpCode = ...

    LDIND_I: System.Reflection.Emit.OpCode = ...

    LDIND_R_4: System.Reflection.Emit.OpCode = ...

    LDIND_R_8: System.Reflection.Emit.OpCode = ...

    LDIND_REF: System.Reflection.Emit.OpCode = ...

    STIND_REF: System.Reflection.Emit.OpCode = ...

    STIND_I_1: System.Reflection.Emit.OpCode = ...

    STIND_I_2: System.Reflection.Emit.OpCode = ...

    STIND_I_4: System.Reflection.Emit.OpCode = ...

    STIND_I_8: System.Reflection.Emit.OpCode = ...

    STIND_R_4: System.Reflection.Emit.OpCode = ...

    STIND_R_8: System.Reflection.Emit.OpCode = ...

    ADD: System.Reflection.Emit.OpCode = ...

    SUB: System.Reflection.Emit.OpCode = ...

    MUL: System.Reflection.Emit.OpCode = ...

    DIV: System.Reflection.Emit.OpCode = ...

    DIV_UN: System.Reflection.Emit.OpCode = ...

    REM: System.Reflection.Emit.OpCode = ...

    REM_UN: System.Reflection.Emit.OpCode = ...

    AND: System.Reflection.Emit.OpCode = ...

    OR: System.Reflection.Emit.OpCode = ...

    XOR: System.Reflection.Emit.OpCode = ...

    SHL: System.Reflection.Emit.OpCode = ...

    SHR: System.Reflection.Emit.OpCode = ...

    SHR_UN: System.Reflection.Emit.OpCode = ...

    NEG: System.Reflection.Emit.OpCode = ...

    NOT: System.Reflection.Emit.OpCode = ...

    CONV_I_1: System.Reflection.Emit.OpCode = ...

    CONV_I_2: System.Reflection.Emit.OpCode = ...

    CONV_I_4: System.Reflection.Emit.OpCode = ...

    CONV_I_8: System.Reflection.Emit.OpCode = ...

    CONV_R_4: System.Reflection.Emit.OpCode = ...

    CONV_R_8: System.Reflection.Emit.OpCode = ...

    CONV_U_4: System.Reflection.Emit.OpCode = ...

    CONV_U_8: System.Reflection.Emit.OpCode = ...

    CALLVIRT: System.Reflection.Emit.OpCode = ...

    CPOBJ: System.Reflection.Emit.OpCode = ...

    LDOBJ: System.Reflection.Emit.OpCode = ...

    LDSTR: System.Reflection.Emit.OpCode = ...

    NEWOBJ: System.Reflection.Emit.OpCode = ...

    CASTCLASS: System.Reflection.Emit.OpCode = ...

    ISINST: System.Reflection.Emit.OpCode = ...

    CONV_R_UN: System.Reflection.Emit.OpCode = ...

    UNBOX: System.Reflection.Emit.OpCode = ...

    THROW: System.Reflection.Emit.OpCode = ...

    LDFLD: System.Reflection.Emit.OpCode = ...

    LDFLDA: System.Reflection.Emit.OpCode = ...

    STFLD: System.Reflection.Emit.OpCode = ...

    LDSFLD: System.Reflection.Emit.OpCode = ...

    LDSFLDA: System.Reflection.Emit.OpCode = ...

    STSFLD: System.Reflection.Emit.OpCode = ...

    STOBJ: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_1_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_2_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_4_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_8_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_1_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_2_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_4_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_8_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_UN: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_UN: System.Reflection.Emit.OpCode = ...

    BOX: System.Reflection.Emit.OpCode = ...

    NEWARR: System.Reflection.Emit.OpCode = ...

    LDLEN: System.Reflection.Emit.OpCode = ...

    LDELEMA: System.Reflection.Emit.OpCode = ...

    LDELEM_I_1: System.Reflection.Emit.OpCode = ...

    LDELEM_U_1: System.Reflection.Emit.OpCode = ...

    LDELEM_I_2: System.Reflection.Emit.OpCode = ...

    LDELEM_U_2: System.Reflection.Emit.OpCode = ...

    LDELEM_I_4: System.Reflection.Emit.OpCode = ...

    LDELEM_U_4: System.Reflection.Emit.OpCode = ...

    LDELEM_I_8: System.Reflection.Emit.OpCode = ...

    LDELEM_I: System.Reflection.Emit.OpCode = ...

    LDELEM_R_4: System.Reflection.Emit.OpCode = ...

    LDELEM_R_8: System.Reflection.Emit.OpCode = ...

    LDELEM_REF: System.Reflection.Emit.OpCode = ...

    STELEM_I: System.Reflection.Emit.OpCode = ...

    STELEM_I_1: System.Reflection.Emit.OpCode = ...

    STELEM_I_2: System.Reflection.Emit.OpCode = ...

    STELEM_I_4: System.Reflection.Emit.OpCode = ...

    STELEM_I_8: System.Reflection.Emit.OpCode = ...

    STELEM_R_4: System.Reflection.Emit.OpCode = ...

    STELEM_R_8: System.Reflection.Emit.OpCode = ...

    STELEM_REF: System.Reflection.Emit.OpCode = ...

    LDELEM: System.Reflection.Emit.OpCode = ...

    STELEM: System.Reflection.Emit.OpCode = ...

    UNBOX_ANY: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_1: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_1: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_2: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_2: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_4: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_4: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I_8: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U_8: System.Reflection.Emit.OpCode = ...

    REFANYVAL: System.Reflection.Emit.OpCode = ...

    CKFINITE: System.Reflection.Emit.OpCode = ...

    MKREFANY: System.Reflection.Emit.OpCode = ...

    LDTOKEN: System.Reflection.Emit.OpCode = ...

    CONV_U_2: System.Reflection.Emit.OpCode = ...

    CONV_U_1: System.Reflection.Emit.OpCode = ...

    CONV_I: System.Reflection.Emit.OpCode = ...

    CONV_OVF_I: System.Reflection.Emit.OpCode = ...

    CONV_OVF_U: System.Reflection.Emit.OpCode = ...

    ADD_OVF: System.Reflection.Emit.OpCode = ...

    ADD_OVF_UN: System.Reflection.Emit.OpCode = ...

    MUL_OVF: System.Reflection.Emit.OpCode = ...

    MUL_OVF_UN: System.Reflection.Emit.OpCode = ...

    SUB_OVF: System.Reflection.Emit.OpCode = ...

    SUB_OVF_UN: System.Reflection.Emit.OpCode = ...

    ENDFINALLY: System.Reflection.Emit.OpCode = ...

    LEAVE: System.Reflection.Emit.OpCode = ...

    LEAVE_S: System.Reflection.Emit.OpCode = ...

    STIND_I: System.Reflection.Emit.OpCode = ...

    CONV_U: System.Reflection.Emit.OpCode = ...

    PREFIX_7: System.Reflection.Emit.OpCode = ...

    PREFIX_6: System.Reflection.Emit.OpCode = ...

    PREFIX_5: System.Reflection.Emit.OpCode = ...

    PREFIX_4: System.Reflection.Emit.OpCode = ...

    PREFIX_3: System.Reflection.Emit.OpCode = ...

    PREFIX_2: System.Reflection.Emit.OpCode = ...

    PREFIX_1: System.Reflection.Emit.OpCode = ...

    PREFIXREF: System.Reflection.Emit.OpCode = ...

    ARGLIST: System.Reflection.Emit.OpCode = ...

    CEQ: System.Reflection.Emit.OpCode = ...

    CGT: System.Reflection.Emit.OpCode = ...

    CGT_UN: System.Reflection.Emit.OpCode = ...

    CLT: System.Reflection.Emit.OpCode = ...

    CLT_UN: System.Reflection.Emit.OpCode = ...

    LDFTN: System.Reflection.Emit.OpCode = ...

    LDVIRTFTN: System.Reflection.Emit.OpCode = ...

    LDARG: System.Reflection.Emit.OpCode = ...

    LDARGA: System.Reflection.Emit.OpCode = ...

    STARG: System.Reflection.Emit.OpCode = ...

    LDLOC: System.Reflection.Emit.OpCode = ...

    LDLOCA: System.Reflection.Emit.OpCode = ...

    STLOC: System.Reflection.Emit.OpCode = ...

    LOCALLOC: System.Reflection.Emit.OpCode = ...

    ENDFILTER: System.Reflection.Emit.OpCode = ...

    UNALIGNED: System.Reflection.Emit.OpCode = ...

    VOLATILE: System.Reflection.Emit.OpCode = ...

    TAILCALL: System.Reflection.Emit.OpCode = ...

    INITOBJ: System.Reflection.Emit.OpCode = ...

    CONSTRAINED: System.Reflection.Emit.OpCode = ...

    CPBLK: System.Reflection.Emit.OpCode = ...

    INITBLK: System.Reflection.Emit.OpCode = ...

    RETHROW: System.Reflection.Emit.OpCode = ...

    SIZEOF: System.Reflection.Emit.OpCode = ...

    REFANYTYPE: System.Reflection.Emit.OpCode = ...

    READONLY: System.Reflection.Emit.OpCode = ...

    @staticmethod
    def takes_single_byte_argument(inst: System.Reflection.Emit.OpCode) -> bool:
        ...


