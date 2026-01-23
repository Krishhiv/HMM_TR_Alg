from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections.Generic
import System.Globalization
import System.Numerics
import System.Runtime.Intrinsics

System_Numerics_Vector = typing.Any
T = typing.Any
System_Numerics_Vector4 = typing.Any
System_Numerics_Matrix3x2 = typing.Any
System_Numerics_Vector2 = typing.Any
System_Numerics_Plane = typing.Any
System_Numerics_BFloat16 = typing.Any
System_Numerics_Matrix4x4 = typing.Any
System_Numerics_Vector3 = typing.Any
System_Numerics_Quaternion = typing.Any
System_Numerics_TotalOrderIeee754Comparer = typing.Any

System_Numerics_Vector_T = typing.TypeVar("System_Numerics_Vector_T")
System_Numerics_IAdditiveIdentity_TSelf = typing.TypeVar("System_Numerics_IAdditiveIdentity_TSelf")
System_Numerics_IAdditiveIdentity_TResult = typing.TypeVar("System_Numerics_IAdditiveIdentity_TResult")
System_Numerics_IBinaryInteger_TSelf = typing.TypeVar("System_Numerics_IBinaryInteger_TSelf")
System_Numerics_IUnaryNegationOperators_TSelf = typing.TypeVar("System_Numerics_IUnaryNegationOperators_TSelf")
System_Numerics_IUnaryNegationOperators_TResult = typing.TypeVar("System_Numerics_IUnaryNegationOperators_TResult")
System_Numerics_IMinMaxValue_TSelf = typing.TypeVar("System_Numerics_IMinMaxValue_TSelf")
System_Numerics_IMultiplicativeIdentity_TSelf = typing.TypeVar("System_Numerics_IMultiplicativeIdentity_TSelf")
System_Numerics_IMultiplicativeIdentity_TResult = typing.TypeVar("System_Numerics_IMultiplicativeIdentity_TResult")
System_Numerics_IExponentialFunctions_TSelf = typing.TypeVar("System_Numerics_IExponentialFunctions_TSelf")
System_Numerics_IAdditionOperators_TSelf = typing.TypeVar("System_Numerics_IAdditionOperators_TSelf")
System_Numerics_IAdditionOperators_TOther = typing.TypeVar("System_Numerics_IAdditionOperators_TOther")
System_Numerics_IAdditionOperators_TResult = typing.TypeVar("System_Numerics_IAdditionOperators_TResult")
System_Numerics_IMultiplyOperators_TSelf = typing.TypeVar("System_Numerics_IMultiplyOperators_TSelf")
System_Numerics_IMultiplyOperators_TOther = typing.TypeVar("System_Numerics_IMultiplyOperators_TOther")
System_Numerics_IMultiplyOperators_TResult = typing.TypeVar("System_Numerics_IMultiplyOperators_TResult")
System_Numerics_IPowerFunctions_TSelf = typing.TypeVar("System_Numerics_IPowerFunctions_TSelf")
System_Numerics_IBitwiseOperators_TSelf = typing.TypeVar("System_Numerics_IBitwiseOperators_TSelf")
System_Numerics_IBitwiseOperators_TOther = typing.TypeVar("System_Numerics_IBitwiseOperators_TOther")
System_Numerics_IBitwiseOperators_TResult = typing.TypeVar("System_Numerics_IBitwiseOperators_TResult")
System_Numerics_ITrigonometricFunctions_TSelf = typing.TypeVar("System_Numerics_ITrigonometricFunctions_TSelf")
System_Numerics_IIncrementOperators_TSelf = typing.TypeVar("System_Numerics_IIncrementOperators_TSelf")
System_Numerics_IShiftOperators_TSelf = typing.TypeVar("System_Numerics_IShiftOperators_TSelf")
System_Numerics_IShiftOperators_TOther = typing.TypeVar("System_Numerics_IShiftOperators_TOther")
System_Numerics_IShiftOperators_TResult = typing.TypeVar("System_Numerics_IShiftOperators_TResult")
System_Numerics_ISubtractionOperators_TSelf = typing.TypeVar("System_Numerics_ISubtractionOperators_TSelf")
System_Numerics_ISubtractionOperators_TOther = typing.TypeVar("System_Numerics_ISubtractionOperators_TOther")
System_Numerics_ISubtractionOperators_TResult = typing.TypeVar("System_Numerics_ISubtractionOperators_TResult")
System_Numerics_IFloatingPointIeee754_TSelf = typing.TypeVar("System_Numerics_IFloatingPointIeee754_TSelf")
System_Numerics_IDivisionOperators_TSelf = typing.TypeVar("System_Numerics_IDivisionOperators_TSelf")
System_Numerics_IDivisionOperators_TOther = typing.TypeVar("System_Numerics_IDivisionOperators_TOther")
System_Numerics_IDivisionOperators_TResult = typing.TypeVar("System_Numerics_IDivisionOperators_TResult")
System_Numerics_INumber_TSelf = typing.TypeVar("System_Numerics_INumber_TSelf")
System_Numerics_IBinaryFloatingPointIeee754_TSelf = typing.TypeVar("System_Numerics_IBinaryFloatingPointIeee754_TSelf")
System_Numerics_ISignedNumber_TSelf = typing.TypeVar("System_Numerics_ISignedNumber_TSelf")
System_Numerics_IModulusOperators_TSelf = typing.TypeVar("System_Numerics_IModulusOperators_TSelf")
System_Numerics_IModulusOperators_TOther = typing.TypeVar("System_Numerics_IModulusOperators_TOther")
System_Numerics_IModulusOperators_TResult = typing.TypeVar("System_Numerics_IModulusOperators_TResult")
System_Numerics_IHyperbolicFunctions_TSelf = typing.TypeVar("System_Numerics_IHyperbolicFunctions_TSelf")
System_Numerics_IUnaryPlusOperators_TSelf = typing.TypeVar("System_Numerics_IUnaryPlusOperators_TSelf")
System_Numerics_IUnaryPlusOperators_TResult = typing.TypeVar("System_Numerics_IUnaryPlusOperators_TResult")
System_Numerics_IRootFunctions_TSelf = typing.TypeVar("System_Numerics_IRootFunctions_TSelf")
System_Numerics_IEqualityOperators_TSelf = typing.TypeVar("System_Numerics_IEqualityOperators_TSelf")
System_Numerics_IEqualityOperators_TOther = typing.TypeVar("System_Numerics_IEqualityOperators_TOther")
System_Numerics_IEqualityOperators_TResult = typing.TypeVar("System_Numerics_IEqualityOperators_TResult")
System_Numerics_TotalOrderIeee754Comparer_T = typing.TypeVar("System_Numerics_TotalOrderIeee754Comparer_T")
System_Numerics_IUnsignedNumber_TSelf = typing.TypeVar("System_Numerics_IUnsignedNumber_TSelf")
System_Numerics_IDecrementOperators_TSelf = typing.TypeVar("System_Numerics_IDecrementOperators_TSelf")
System_Numerics_ILogarithmicFunctions_TSelf = typing.TypeVar("System_Numerics_ILogarithmicFunctions_TSelf")
System_Numerics_IFloatingPointConstants_TSelf = typing.TypeVar("System_Numerics_IFloatingPointConstants_TSelf")
System_Numerics_IComparisonOperators_TSelf = typing.TypeVar("System_Numerics_IComparisonOperators_TSelf")
System_Numerics_IComparisonOperators_TOther = typing.TypeVar("System_Numerics_IComparisonOperators_TOther")
System_Numerics_IComparisonOperators_TResult = typing.TypeVar("System_Numerics_IComparisonOperators_TResult")
System_Numerics_INumberBase_TSelf = typing.TypeVar("System_Numerics_INumberBase_TSelf")
System_Numerics_IBinaryNumber_TSelf = typing.TypeVar("System_Numerics_IBinaryNumber_TSelf")
System_Numerics_IFloatingPoint_TSelf = typing.TypeVar("System_Numerics_IFloatingPoint_TSelf")


class Quaternion(System.IEquatable[System_Numerics_Quaternion]):
    """This class has no documentation."""

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    @property
    def w(self) -> float:
        ...

    @w.setter
    def w(self, value: float) -> None:
        ...

    ZERO: System.Numerics.Quaternion

    IDENTITY: System.Numerics.Quaternion

    @property
    def is_identity(self) -> bool:
        ...

    def __add__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    def __eq__(self, value_2: System.Numerics.Quaternion) -> bool:
        ...

    def __getitem__(self, index: int) -> float:
        ...

    def __iadd__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Quaternion:
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        ...

    @overload
    def __init__(self, vector_part: System.Numerics.Vector3, scalar_part: float) -> None:
        ...

    def __isub__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    def __itruediv__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Quaternion:
        ...

    def __ne__(self, value_2: System.Numerics.Quaternion) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Quaternion:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        ...

    def __sub__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    def __truediv__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def add(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def concatenate(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def conjugate(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float, w: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def create(vector_part: System.Numerics.Vector3, scalar_part: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def create_from_axis_angle(axis: System.Numerics.Vector3, angle: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def create_from_rotation_matrix(matrix: System.Numerics.Matrix4x4) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def create_from_yaw_pitch_roll(yaw: float, pitch: float, roll: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def divide(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def dot(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.Quaternion) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def inverse(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    @staticmethod
    def lerp(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion, amount: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Quaternion, value_2: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def negate(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def slerp(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion, amount: float) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        ...

    def to_string(self) -> str:
        ...


class Vector3(System.IEquatable[System_Numerics_Vector3], System.IFormattable):
    """This class has no documentation."""

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector3

    E: System.Numerics.Vector3

    EPSILON: System.Numerics.Vector3

    NA_N: System.Numerics.Vector3

    NEGATIVE_INFINITY: System.Numerics.Vector3

    NEGATIVE_ZERO: System.Numerics.Vector3

    ONE: System.Numerics.Vector3

    PI: System.Numerics.Vector3

    POSITIVE_INFINITY: System.Numerics.Vector3

    TAU: System.Numerics.Vector3

    UNIT_X: System.Numerics.Vector3

    UNIT_Y: System.Numerics.Vector3

    UNIT_Z: System.Numerics.Vector3

    ZERO: System.Numerics.Vector3

    def __add__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __and__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __eq__(self, right: System.Numerics.Vector3) -> bool:
        ...

    def __getitem__(self, index: int) -> float:
        ...

    def __iadd__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __iand__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector3:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector2, z: float) -> None:
        ...

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        ...

    def __invert__(self) -> System.Numerics.Vector3:
        ...

    def __ior__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    def __isub__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector3:
        ...

    def __ixor__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector3:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __ne__(self, right: System.Numerics.Vector3) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Vector3:
        ...

    def __or__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __pos__(self) -> System.Numerics.Vector3:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        ...

    def __sub__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector3:
        ...

    def __xor__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def add(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector3, min: System.Numerics.Vector3, max: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector3, min: System.Numerics.Vector3, max: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector3, left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector3, sign: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector2, z: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def create_scalar(x: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def create_scalar_unsafe(x: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def cross(vector_1: System.Numerics.Vector3, vector_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> float:
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> float:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector3, divisor: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def dot(vector_1: System.Numerics.Vector3, vector_2: System.Numerics.Vector3) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector3, right: System.Numerics.Vector3, addend: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector3, y: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3, amount: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3, amount: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector3, right: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector3, right: System.Numerics.Vector3, addend: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def reflect(vector: System.Numerics.Vector3, normal: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector3, mode: System.MidpointRounding) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector3, x_index: int, y_index: int, z_index: int) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector3) -> System.ValueTuple[System.Numerics.Vector3, System.Numerics.Vector3]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector3) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector3, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def transform_normal(normal: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...


class Matrix4x4(System.IEquatable[System_Numerics_Matrix4x4]):
    """This class has no documentation."""

    @property
    def m_11(self) -> float:
        ...

    @m_11.setter
    def m_11(self, value: float) -> None:
        ...

    @property
    def m_12(self) -> float:
        ...

    @m_12.setter
    def m_12(self, value: float) -> None:
        ...

    @property
    def m_13(self) -> float:
        ...

    @m_13.setter
    def m_13(self, value: float) -> None:
        ...

    @property
    def m_14(self) -> float:
        ...

    @m_14.setter
    def m_14(self, value: float) -> None:
        ...

    @property
    def m_21(self) -> float:
        ...

    @m_21.setter
    def m_21(self, value: float) -> None:
        ...

    @property
    def m_22(self) -> float:
        ...

    @m_22.setter
    def m_22(self, value: float) -> None:
        ...

    @property
    def m_23(self) -> float:
        ...

    @m_23.setter
    def m_23(self, value: float) -> None:
        ...

    @property
    def m_24(self) -> float:
        ...

    @m_24.setter
    def m_24(self, value: float) -> None:
        ...

    @property
    def m_31(self) -> float:
        ...

    @m_31.setter
    def m_31(self, value: float) -> None:
        ...

    @property
    def m_32(self) -> float:
        ...

    @m_32.setter
    def m_32(self, value: float) -> None:
        ...

    @property
    def m_33(self) -> float:
        ...

    @m_33.setter
    def m_33(self, value: float) -> None:
        ...

    @property
    def m_34(self) -> float:
        ...

    @m_34.setter
    def m_34(self, value: float) -> None:
        ...

    @property
    def m_41(self) -> float:
        ...

    @m_41.setter
    def m_41(self, value: float) -> None:
        ...

    @property
    def m_42(self) -> float:
        ...

    @m_42.setter
    def m_42(self, value: float) -> None:
        ...

    @property
    def m_43(self) -> float:
        ...

    @m_43.setter
    def m_43(self, value: float) -> None:
        ...

    @property
    def m_44(self) -> float:
        ...

    @m_44.setter
    def m_44(self, value: float) -> None:
        ...

    IDENTITY: System.Numerics.Matrix4x4

    @property
    def is_identity(self) -> bool:
        ...

    @property
    def translation(self) -> System.Numerics.Vector3:
        ...

    @translation.setter
    def translation(self, value: System.Numerics.Vector3) -> None:
        ...

    @property
    def x(self) -> System.Numerics.Vector4:
        ...

    @x.setter
    def x(self, value: System.Numerics.Vector4) -> None:
        ...

    @property
    def y(self) -> System.Numerics.Vector4:
        ...

    @y.setter
    def y(self, value: System.Numerics.Vector4) -> None:
        ...

    @property
    def z(self) -> System.Numerics.Vector4:
        ...

    @z.setter
    def z(self, value: System.Numerics.Vector4) -> None:
        ...

    @property
    def w(self) -> System.Numerics.Vector4:
        ...

    @w.setter
    def w(self, value: System.Numerics.Vector4) -> None:
        ...

    def __add__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    def __eq__(self, value_2: System.Numerics.Matrix4x4) -> bool:
        ...

    @overload
    def __getitem__(self, row: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __getitem__(self, row: int, column: int) -> float:
        ...

    def __iadd__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __init__(self, m_11: float, m_12: float, m_13: float, m_14: float, m_21: float, m_22: float, m_23: float, m_24: float, m_31: float, m_32: float, m_33: float, m_34: float, m_41: float, m_42: float, m_43: float, m_44: float) -> None:
        ...

    @overload
    def __init__(self, value: System.Numerics.Matrix3x2) -> None:
        ...

    def __isub__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Matrix4x4:
        ...

    def __ne__(self, value_2: System.Numerics.Matrix4x4) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Matrix4x4:
        ...

    @overload
    def __setitem__(self, row: int, value: System.Numerics.Vector4) -> None:
        ...

    @overload
    def __setitem__(self, row: int, column: int, value: float) -> None:
        ...

    def __sub__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def add(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create(value: System.Numerics.Matrix3x2) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create(value: System.Numerics.Vector4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create(x: System.Numerics.Vector4, y: System.Numerics.Vector4, z: System.Numerics.Vector4, w: System.Numerics.Vector4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create(m_11: float, m_12: float, m_13: float, m_14: float, m_21: float, m_22: float, m_23: float, m_24: float, m_31: float, m_32: float, m_33: float, m_34: float, m_41: float, m_42: float, m_43: float, m_44: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_billboard(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_billboard_left_handed(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_constrained_billboard(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, rotate_axis: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3, object_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_constrained_billboard_left_handed(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, rotate_axis: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3, object_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_from_axis_angle(axis: System.Numerics.Vector3, angle: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_from_quaternion(quaternion: System.Numerics.Quaternion) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_from_yaw_pitch_roll(yaw: float, pitch: float, roll: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_look_at(camera_position: System.Numerics.Vector3, camera_target: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_look_at_left_handed(camera_position: System.Numerics.Vector3, camera_target: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_look_to(camera_position: System.Numerics.Vector3, camera_direction: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_look_to_left_handed(camera_position: System.Numerics.Vector3, camera_direction: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_orthographic(width: float, height: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_orthographic_left_handed(width: float, height: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_orthographic_off_center(left: float, right: float, bottom: float, top: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_orthographic_off_center_left_handed(left: float, right: float, bottom: float, top: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective(width: float, height: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective_field_of_view(field_of_view: float, aspect_ratio: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective_field_of_view_left_handed(field_of_view: float, aspect_ratio: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective_left_handed(width: float, height: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective_off_center(left: float, right: float, bottom: float, top: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_perspective_off_center_left_handed(left: float, right: float, bottom: float, top: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_reflection(value: System.Numerics.Plane) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_x(radians: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_x(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_y(radians: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_y(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_z(radians: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_rotation_z(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, z_scale: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, z_scale: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector3, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(scale: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_scale(scale: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_shadow(light_direction: System.Numerics.Vector3, plane: System.Numerics.Plane) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_translation(position: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def create_translation(x_position: float, y_position: float, z_position: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_viewport(x: float, y: float, width: float, height: float, min_depth: float, max_depth: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_viewport_left_handed(x: float, y: float, width: float, height: float, min_depth: float, max_depth: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def create_world(position: System.Numerics.Vector3, forward: System.Numerics.Vector3, up: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def decompose(matrix: System.Numerics.Matrix4x4, scale: typing.Optional[System.Numerics.Vector3], rotation: typing.Optional[System.Numerics.Quaternion], translation: typing.Optional[System.Numerics.Vector3]) -> typing.Tuple[bool, System.Numerics.Vector3, System.Numerics.Quaternion, System.Numerics.Vector3]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.Matrix4x4) -> bool:
        ...

    def get_determinant(self) -> float:
        ...

    def get_element(self, row: int, column: int) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_row(self, index: int) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def invert(matrix: System.Numerics.Matrix4x4, result: typing.Optional[System.Numerics.Matrix4x4]) -> typing.Tuple[bool, System.Numerics.Matrix4x4]:
        ...

    @staticmethod
    def lerp(matrix_1: System.Numerics.Matrix4x4, matrix_2: System.Numerics.Matrix4x4, amount: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix4x4, value_2: float) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def negate(value: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def transform(value: System.Numerics.Matrix4x4, rotation: System.Numerics.Quaternion) -> System.Numerics.Matrix4x4:
        ...

    @staticmethod
    def transpose(matrix: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        ...

    def with_element(self, row: int, column: int, value: float) -> System.Numerics.Matrix4x4:
        ...

    def with_row(self, index: int, value: System.Numerics.Vector4) -> System.Numerics.Matrix4x4:
        ...


class Vector2(System.IEquatable[System_Numerics_Vector2], System.IFormattable):
    """This class has no documentation."""

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector2

    E: System.Numerics.Vector2

    EPSILON: System.Numerics.Vector2

    NA_N: System.Numerics.Vector2

    NEGATIVE_INFINITY: System.Numerics.Vector2

    NEGATIVE_ZERO: System.Numerics.Vector2

    ONE: System.Numerics.Vector2

    PI: System.Numerics.Vector2

    POSITIVE_INFINITY: System.Numerics.Vector2

    TAU: System.Numerics.Vector2

    UNIT_X: System.Numerics.Vector2

    UNIT_Y: System.Numerics.Vector2

    ZERO: System.Numerics.Vector2

    def __add__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __and__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __eq__(self, right: System.Numerics.Vector2) -> bool:
        ...

    def __getitem__(self, index: int) -> float:
        ...

    def __iadd__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __iand__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector2:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, x: float, y: float) -> None:
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        ...

    def __invert__(self) -> System.Numerics.Vector2:
        ...

    def __ior__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    def __isub__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector2:
        ...

    def __ixor__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector2:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __ne__(self, right: System.Numerics.Vector2) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Vector2:
        ...

    def __or__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __pos__(self) -> System.Numerics.Vector2:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        ...

    def __sub__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector2:
        ...

    def __xor__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def add(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector2, min: System.Numerics.Vector2, max: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector2, min: System.Numerics.Vector2, max: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector2, left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector2, sign: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def create(x: float, y: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def create_scalar(x: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def create_scalar_unsafe(x: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def cross(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector2, divisor: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def dot(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector2, right: System.Numerics.Vector2, addend: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector2, y: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2, amount: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2, amount: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector2, right: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector2, right: System.Numerics.Vector2, addend: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def reflect(vector: System.Numerics.Vector2, normal: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector2, mode: System.MidpointRounding) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector2, x_index: int, y_index: int) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector2) -> System.ValueTuple[System.Numerics.Vector2, System.Numerics.Vector2]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector2) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix3x2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector2, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def transform_normal(normal: System.Numerics.Vector2, matrix: System.Numerics.Matrix3x2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def transform_normal(normal: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...


class Vector4(System.IEquatable[System_Numerics_Vector4], System.IFormattable):
    """This class has no documentation."""

    @property
    def x(self) -> float:
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    @property
    def w(self) -> float:
        ...

    @w.setter
    def w(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector4

    E: System.Numerics.Vector4

    EPSILON: System.Numerics.Vector4

    NA_N: System.Numerics.Vector4

    NEGATIVE_INFINITY: System.Numerics.Vector4

    NEGATIVE_ZERO: System.Numerics.Vector4

    ONE: System.Numerics.Vector4

    PI: System.Numerics.Vector4

    POSITIVE_INFINITY: System.Numerics.Vector4

    TAU: System.Numerics.Vector4

    UNIT_X: System.Numerics.Vector4

    UNIT_Y: System.Numerics.Vector4

    UNIT_Z: System.Numerics.Vector4

    UNIT_W: System.Numerics.Vector4

    ZERO: System.Numerics.Vector4

    def __add__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __and__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __eq__(self, right: System.Numerics.Vector4) -> bool:
        ...

    def __getitem__(self, index: int) -> float:
        ...

    def __iadd__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __iand__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector4:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector2, z: float, w: float) -> None:
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector3, w: float) -> None:
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        ...

    def __invert__(self) -> System.Numerics.Vector4:
        ...

    def __ior__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    def __isub__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector4:
        ...

    def __ixor__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector4:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __ne__(self, right: System.Numerics.Vector4) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Vector4:
        ...

    def __or__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __pos__(self) -> System.Numerics.Vector4:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        ...

    def __sub__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector4:
        ...

    def __xor__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def add(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector4, min: System.Numerics.Vector4, max: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector4, min: System.Numerics.Vector4, max: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector4, left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector4, sign: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector2, z: float, w: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector3, w: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float, w: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def create_scalar(x: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def create_scalar_unsafe(x: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def cross(vector_1: System.Numerics.Vector4, vector_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> float:
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> float:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector4, divisor: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def dot(vector_1: System.Numerics.Vector4, vector_2: System.Numerics.Vector4) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector4, right: System.Numerics.Vector4, addend: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector4, y: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    def length(self) -> float:
        ...

    def length_squared(self) -> float:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4, amount: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4, amount: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector4, right: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector4, right: System.Numerics.Vector4, addend: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def normalize(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector4, mode: System.MidpointRounding) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector4, x_index: int, y_index: int, z_index: int, w_index: int) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector4) -> System.ValueTuple[System.Numerics.Vector4, System.Numerics.Vector4]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector4) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector2, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector3, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def transform(vector: System.Numerics.Vector4, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector4, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...


class Plane(System.IEquatable[System_Numerics_Plane]):
    """This class has no documentation."""

    @property
    def normal(self) -> System.Numerics.Vector3:
        ...

    @normal.setter
    def normal(self, value: System.Numerics.Vector3) -> None:
        ...

    @property
    def d(self) -> float:
        ...

    @d.setter
    def d(self, value: float) -> None:
        ...

    def __eq__(self, value_2: System.Numerics.Plane) -> bool:
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, d: float) -> None:
        ...

    @overload
    def __init__(self, normal: System.Numerics.Vector3, d: float) -> None:
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector4) -> None:
        ...

    def __ne__(self, value_2: System.Numerics.Plane) -> bool:
        ...

    @staticmethod
    @overload
    def create(value: System.Numerics.Vector4) -> System.Numerics.Plane:
        ...

    @staticmethod
    @overload
    def create(normal: System.Numerics.Vector3, d: float) -> System.Numerics.Plane:
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float, d: float) -> System.Numerics.Plane:
        ...

    @staticmethod
    def create_from_vertices(point_1: System.Numerics.Vector3, point_2: System.Numerics.Vector3, point_3: System.Numerics.Vector3) -> System.Numerics.Plane:
        ...

    @staticmethod
    def dot(plane: System.Numerics.Plane, value: System.Numerics.Vector4) -> float:
        ...

    @staticmethod
    def dot_coordinate(plane: System.Numerics.Plane, value: System.Numerics.Vector3) -> float:
        ...

    @staticmethod
    def dot_normal(plane: System.Numerics.Plane, value: System.Numerics.Vector3) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.Plane) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Plane) -> System.Numerics.Plane:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    @overload
    def transform(plane: System.Numerics.Plane, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Plane:
        ...

    @staticmethod
    @overload
    def transform(plane: System.Numerics.Plane, rotation: System.Numerics.Quaternion) -> System.Numerics.Plane:
        ...


class Vector(typing.Generic[System_Numerics_Vector_T], System.Runtime.Intrinsics.ISimdVector[System_Numerics_Vector, System_Numerics_Vector_T], System.IFormattable):
    """This class has no documentation."""

    IS_HARDWARE_ACCELERATED: bool

    E: System.Numerics.Vector[T]

    PI: System.Numerics.Vector[T]

    TAU: System.Numerics.Vector[T]

    ALL_BITS_SET: System.Numerics.Vector[System_Numerics_Vector_T]

    COUNT: int

    INDICES: System.Numerics.Vector[System_Numerics_Vector_T]

    IS_SUPPORTED: bool

    ONE: System.Numerics.Vector[System_Numerics_Vector_T]

    ZERO: System.Numerics.Vector[System_Numerics_Vector_T]

    def __add__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __and__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __eq__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Numerics_Vector_T:
        ...

    def __iadd__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __iand__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __ilshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __imul__(self, factor: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __imul__(self, value: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __init__(self, value: System_Numerics_Vector_T) -> None:
        ...

    @overload
    def __init__(self, values: typing.List[System_Numerics_Vector_T]) -> None:
        ...

    @overload
    def __init__(self, values: typing.List[System_Numerics_Vector_T], index: int) -> None:
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[System_Numerics_Vector_T]) -> None:
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def __init__(self, values: System.Span[System_Numerics_Vector_T]) -> None:
        ...

    def __invert__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __ior__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __irshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __isub__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __itruediv__(self, right: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __ixor__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __lshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __mul__(self, factor: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __mul__(self, value: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __ne__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __or__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __pos__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __rshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __sub__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @overload
    def __truediv__(self, right: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    def __xor__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        ...

    @staticmethod
    def as_plane(value: System.Numerics.Vector4) -> System.Numerics.Plane:
        ...

    @staticmethod
    def as_quaternion(value: System.Numerics.Vector4) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def as_vector_2(value: System.Numerics.Vector4) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def as_vector_2(value: System.Numerics.Vector3) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def as_vector_3(value: System.Numerics.Vector4) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def as_vector_3(value: System.Numerics.Vector2) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def as_vector_3_unsafe(value: System.Numerics.Vector2) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Vector3) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Vector2) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Plane) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def as_vector_4_unsafe(value: System.Numerics.Vector3) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def as_vector_4_unsafe(value: System.Numerics.Vector2) -> System.Numerics.Vector4:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Numerics_Vector_T]) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Numerics_Vector_T], start_index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[int]) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Numerics_Vector_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector4, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector3, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector2, index: int) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector4, destination: float) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector4, destination: float, element_offset: System.UIntPtr) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector3, destination: float) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector3, destination: float, element_offset: System.UIntPtr) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector2, destination: float) -> None:
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector2, destination: float, element_offset: System.UIntPtr) -> None:
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector4) -> float:
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector3) -> float:
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector2) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def try_copy_to(self, destination: System.Span[int]) -> bool:
        ...

    @overload
    def try_copy_to(self, destination: System.Span[System_Numerics_Vector_T]) -> bool:
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector4, index: int, value: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector3, index: int, value: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector2, index: int, value: float) -> System.Numerics.Vector2:
        ...


class IAdditiveIdentity(typing.Generic[System_Numerics_IAdditiveIdentity_TSelf, System_Numerics_IAdditiveIdentity_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class BitOperations(System.Object):
    """This class has no documentation."""

    @staticmethod
    def crc_32c(crc: int, data: int) -> int:
        ...

    @staticmethod
    @overload
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_pow_2(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    @overload
    def is_pow_2(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.UIntPtr) -> int:
        ...

    @staticmethod
    @overload
    def log_2(value: int) -> int:
        ...

    @staticmethod
    @overload
    def log_2(value: System.UIntPtr) -> int:
        ...

    @staticmethod
    @overload
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    @overload
    def pop_count(value: System.UIntPtr) -> int:
        ...

    @staticmethod
    @overload
    def rotate_left(value: int, offset: int) -> int:
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def rotate_right(value: int, offset: int) -> int:
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def round_up_to_power_of_2(value: int) -> int:
        ...

    @staticmethod
    @overload
    def round_up_to_power_of_2(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: int) -> int:
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: System.UIntPtr) -> int:
        ...


class IBinaryInteger(typing.Generic[System_Numerics_IBinaryInteger_TSelf], System.Numerics.IBinaryNumber[System_Numerics_IBinaryInteger_TSelf], System.Numerics.IShiftOperators[System_Numerics_IBinaryInteger_TSelf, int, System_Numerics_IBinaryInteger_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_byte_count(self) -> int:
        ...

    def get_shortest_bit_length(self) -> int:
        ...

    def try_write_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_write_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def write_big_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_big_endian(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def write_little_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_little_endian(self, destination: System.Span[int]) -> int:
        ...


class IUnaryNegationOperators(typing.Generic[System_Numerics_IUnaryNegationOperators_TSelf, System_Numerics_IUnaryNegationOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IMinMaxValue(typing.Generic[System_Numerics_IMinMaxValue_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IMultiplicativeIdentity(typing.Generic[System_Numerics_IMultiplicativeIdentity_TSelf, System_Numerics_IMultiplicativeIdentity_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IExponentialFunctions(typing.Generic[System_Numerics_IExponentialFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IExponentialFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class Matrix3x2(System.IEquatable[System_Numerics_Matrix3x2]):
    """This class has no documentation."""

    @property
    def m_11(self) -> float:
        ...

    @m_11.setter
    def m_11(self, value: float) -> None:
        ...

    @property
    def m_12(self) -> float:
        ...

    @m_12.setter
    def m_12(self, value: float) -> None:
        ...

    @property
    def m_21(self) -> float:
        ...

    @m_21.setter
    def m_21(self, value: float) -> None:
        ...

    @property
    def m_22(self) -> float:
        ...

    @m_22.setter
    def m_22(self, value: float) -> None:
        ...

    @property
    def m_31(self) -> float:
        ...

    @m_31.setter
    def m_31(self, value: float) -> None:
        ...

    @property
    def m_32(self) -> float:
        ...

    @m_32.setter
    def m_32(self, value: float) -> None:
        ...

    IDENTITY: System.Numerics.Matrix3x2

    @property
    def is_identity(self) -> bool:
        ...

    @property
    def translation(self) -> System.Numerics.Vector2:
        ...

    @translation.setter
    def translation(self, value: System.Numerics.Vector2) -> None:
        ...

    @property
    def x(self) -> System.Numerics.Vector2:
        ...

    @x.setter
    def x(self, value: System.Numerics.Vector2) -> None:
        ...

    @property
    def y(self) -> System.Numerics.Vector2:
        ...

    @y.setter
    def y(self, value: System.Numerics.Vector2) -> None:
        ...

    @property
    def z(self) -> System.Numerics.Vector2:
        ...

    @z.setter
    def z(self, value: System.Numerics.Vector2) -> None:
        ...

    def __add__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    def __eq__(self, value_2: System.Numerics.Matrix3x2) -> bool:
        ...

    @overload
    def __getitem__(self, row: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __getitem__(self, row: int, column: int) -> float:
        ...

    def __iadd__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Matrix3x2:
        ...

    def __init__(self, m_11: float, m_12: float, m_21: float, m_22: float, m_31: float, m_32: float) -> None:
        ...

    def __isub__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Matrix3x2:
        ...

    def __ne__(self, value_2: System.Numerics.Matrix3x2) -> bool:
        ...

    def __neg__(self) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def __setitem__(self, row: int, value: System.Numerics.Vector2) -> None:
        ...

    @overload
    def __setitem__(self, row: int, column: int, value: float) -> None:
        ...

    def __sub__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    def add(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create(value: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create(x: System.Numerics.Vector2, y: System.Numerics.Vector2, z: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create(m_11: float, m_12: float, m_21: float, m_22: float, m_31: float, m_32: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_rotation(radians: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_rotation(radians: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector2, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(scale: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_scale(scale: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_skew(radians_x: float, radians_y: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_skew(radians_x: float, radians_y: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_translation(position: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def create_translation(x_position: float, y_position: float) -> System.Numerics.Matrix3x2:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.Matrix3x2) -> bool:
        ...

    def get_determinant(self) -> float:
        ...

    def get_element(self, row: int, column: int) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_row(self, index: int) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def invert(matrix: System.Numerics.Matrix3x2, result: typing.Optional[System.Numerics.Matrix3x2]) -> typing.Tuple[bool, System.Numerics.Matrix3x2]:
        ...

    @staticmethod
    def lerp(matrix_1: System.Numerics.Matrix3x2, matrix_2: System.Numerics.Matrix3x2, amount: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix3x2, value_2: float) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    def negate(value: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        ...

    def to_string(self) -> str:
        ...

    def with_element(self, row: int, column: int, value: float) -> System.Numerics.Matrix3x2:
        ...

    def with_row(self, index: int, value: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        ...


class BFloat16(System.IComparable[System_Numerics_BFloat16], System.ISpanFormattable, System.IEquatable[System_Numerics_BFloat16], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[System_Numerics_BFloat16]):
    """This class has no documentation."""

    EPSILON: System.Numerics.BFloat16

    POSITIVE_INFINITY: System.Numerics.BFloat16

    NEGATIVE_INFINITY: System.Numerics.BFloat16

    NA_N: System.Numerics.BFloat16

    MIN_VALUE: System.Numerics.BFloat16

    MAX_VALUE: System.Numerics.BFloat16

    E: System.Numerics.BFloat16

    PI: System.Numerics.BFloat16

    TAU: System.Numerics.BFloat16

    NEGATIVE_ZERO: System.Numerics.BFloat16

    MULTIPLICATIVE_IDENTITY: System.Numerics.BFloat16

    ONE: System.Numerics.BFloat16

    ZERO: System.Numerics.BFloat16

    NEGATIVE_ONE: System.Numerics.BFloat16

    def __add__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __eq__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    def __iadd__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __imod__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __imul__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __isub__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __itruediv__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __le__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Numerics.BFloat16) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    def __mod__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __mul__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __ne__(self, right: System.Numerics.BFloat16) -> bool:
        ...

    def __neg__(self) -> System.Numerics.BFloat16:
        ...

    def __pos__(self) -> System.Numerics.BFloat16:
        ...

    def __sub__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def __truediv__(self, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def abs(value: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def acos(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def acosh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def acos_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def asin(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def asinh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def asin_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def atan(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def atan_2(y: System.Numerics.BFloat16, x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def atan_2_pi(y: System.Numerics.BFloat16, x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def atanh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def atan_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def bit_decrement(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def bit_increment(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def cbrt(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def ceiling(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def clamp(value: System.Numerics.BFloat16, min: System.Numerics.BFloat16, max: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, other: System.Numerics.BFloat16) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.BFloat16, sign: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def cos(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def cosh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def cos_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def exp(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def exp_10(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def exp_10_m_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def exp_2(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def exp_2_m_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def exp_m_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def floor(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.BFloat16, right: System.Numerics.BFloat16, addend: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def hypot(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def ieee_754_remainder(left: System.Numerics.BFloat16, right: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def i_log_b(x: System.Numerics.BFloat16) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_finite(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_infinity(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_integer(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_na_n(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_negative_infinity(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_normal(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_real_number(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_subnormal(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def is_zero(value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def lerp(value_1: System.Numerics.BFloat16, value_2: System.Numerics.BFloat16, amount: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def log(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def log(x: System.Numerics.BFloat16, new_base: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def log_10(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def log_10_p_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def log_2(value: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def log_2_p_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def log_p_1(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def max(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def max_magnitude(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def max_magnitude_number(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def max_number(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def min(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def min_magnitude(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def min_magnitude_number(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def min_number(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def pow(x: System.Numerics.BFloat16, y: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def reciprocal_estimate(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def root_n(x: System.Numerics.BFloat16, n: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def round(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def round(x: System.Numerics.BFloat16, digits: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def round(x: System.Numerics.BFloat16, mode: System.MidpointRounding) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    @overload
    def round(x: System.Numerics.BFloat16, digits: int, mode: System.MidpointRounding) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def scale_b(x: System.Numerics.BFloat16, n: int) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def sign(value: System.Numerics.BFloat16) -> int:
        ...

    @staticmethod
    def sin(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def sin_cos(x: System.Numerics.BFloat16) -> System.ValueTuple[System.Numerics.BFloat16, System.Numerics.BFloat16]:
        ...

    @staticmethod
    def sin_cos_pi(x: System.Numerics.BFloat16) -> System.ValueTuple[System.Numerics.BFloat16, System.Numerics.BFloat16]:
        ...

    @staticmethod
    def sinh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def sin_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def sqrt(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def tan(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def tanh(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def tan_pi(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def truncate(x: System.Numerics.BFloat16) -> System.Numerics.BFloat16:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...


class IAdditionOperators(typing.Generic[System_Numerics_IAdditionOperators_TSelf, System_Numerics_IAdditionOperators_TOther, System_Numerics_IAdditionOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IMultiplyOperators(typing.Generic[System_Numerics_IMultiplyOperators_TSelf, System_Numerics_IMultiplyOperators_TOther, System_Numerics_IMultiplyOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IPowerFunctions(typing.Generic[System_Numerics_IPowerFunctions_TSelf], System.Numerics.INumberBase[System_Numerics_IPowerFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IBitwiseOperators(typing.Generic[System_Numerics_IBitwiseOperators_TSelf, System_Numerics_IBitwiseOperators_TOther, System_Numerics_IBitwiseOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ITrigonometricFunctions(typing.Generic[System_Numerics_ITrigonometricFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_ITrigonometricFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IIncrementOperators(typing.Generic[System_Numerics_IIncrementOperators_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IShiftOperators(typing.Generic[System_Numerics_IShiftOperators_TSelf, System_Numerics_IShiftOperators_TOther, System_Numerics_IShiftOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ISubtractionOperators(typing.Generic[System_Numerics_ISubtractionOperators_TSelf, System_Numerics_ISubtractionOperators_TOther, System_Numerics_ISubtractionOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IFloatingPointIeee754(typing.Generic[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IExponentialFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IFloatingPoint[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IHyperbolicFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.ILogarithmicFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IPowerFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IRootFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.ITrigonometricFunctions[System_Numerics_IFloatingPointIeee754_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IDivisionOperators(typing.Generic[System_Numerics_IDivisionOperators_TSelf, System_Numerics_IDivisionOperators_TOther, System_Numerics_IDivisionOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class INumber(typing.Generic[System_Numerics_INumber_TSelf], System.IComparable[System_Numerics_INumber_TSelf], System.Numerics.IComparisonOperators[System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf, bool], System.Numerics.IModulusOperators[System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf], System.Numerics.INumberBase[System_Numerics_INumber_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IBinaryFloatingPointIeee754(typing.Generic[System_Numerics_IBinaryFloatingPointIeee754_TSelf], System.Numerics.IBinaryNumber[System_Numerics_IBinaryFloatingPointIeee754_TSelf], System.Numerics.IFloatingPointIeee754[System_Numerics_IBinaryFloatingPointIeee754_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ISignedNumber(typing.Generic[System_Numerics_ISignedNumber_TSelf], System.Numerics.INumberBase[System_Numerics_ISignedNumber_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IModulusOperators(typing.Generic[System_Numerics_IModulusOperators_TSelf, System_Numerics_IModulusOperators_TOther, System_Numerics_IModulusOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IHyperbolicFunctions(typing.Generic[System_Numerics_IHyperbolicFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IHyperbolicFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IUnaryPlusOperators(typing.Generic[System_Numerics_IUnaryPlusOperators_TSelf, System_Numerics_IUnaryPlusOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IRootFunctions(typing.Generic[System_Numerics_IRootFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IRootFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IEqualityOperators(typing.Generic[System_Numerics_IEqualityOperators_TSelf, System_Numerics_IEqualityOperators_TOther, System_Numerics_IEqualityOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class TotalOrderIeee754Comparer(typing.Generic[System_Numerics_TotalOrderIeee754Comparer_T], System.Collections.Generic.IComparer[System_Numerics_TotalOrderIeee754Comparer_T], System.Collections.Generic.IEqualityComparer[System_Numerics_TotalOrderIeee754Comparer_T], System.IEquatable[System_Numerics_TotalOrderIeee754Comparer]):
    """This class has no documentation."""

    def compare(self, x: System_Numerics_TotalOrderIeee754Comparer_T, y: System_Numerics_TotalOrderIeee754Comparer_T) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Numerics_TotalOrderIeee754Comparer_T, y: System_Numerics_TotalOrderIeee754Comparer_T) -> bool:
        ...

    @overload
    def equals(self, other: System.Numerics.TotalOrderIeee754Comparer[System_Numerics_TotalOrderIeee754Comparer_T]) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Numerics_TotalOrderIeee754Comparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class IUnsignedNumber(typing.Generic[System_Numerics_IUnsignedNumber_TSelf], System.Numerics.INumberBase[System_Numerics_IUnsignedNumber_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IDecrementOperators(typing.Generic[System_Numerics_IDecrementOperators_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class ILogarithmicFunctions(typing.Generic[System_Numerics_ILogarithmicFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_ILogarithmicFunctions_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IFloatingPointConstants(typing.Generic[System_Numerics_IFloatingPointConstants_TSelf], System.Numerics.INumberBase[System_Numerics_IFloatingPointConstants_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IComparisonOperators(typing.Generic[System_Numerics_IComparisonOperators_TSelf, System_Numerics_IComparisonOperators_TOther, System_Numerics_IComparisonOperators_TResult], System.Numerics.IEqualityOperators[System_Numerics_IComparisonOperators_TSelf, System_Numerics_IComparisonOperators_TOther, System_Numerics_IComparisonOperators_TResult], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class INumberBase(typing.Generic[System_Numerics_INumberBase_TSelf], System.Numerics.IAdditionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IAdditiveIdentity[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IDecrementOperators[System_Numerics_INumberBase_TSelf], System.Numerics.IDivisionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.IEquatable[System_Numerics_INumberBase_TSelf], System.Numerics.IEqualityOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, bool], System.Numerics.IIncrementOperators[System_Numerics_INumberBase_TSelf], System.Numerics.IMultiplicativeIdentity[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IMultiplyOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.ISpanFormattable, System.ISpanParsable[System_Numerics_INumberBase_TSelf], System.Numerics.ISubtractionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IUnaryPlusOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IUnaryNegationOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Numerics_INumberBase_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        ...


class IBinaryNumber(typing.Generic[System_Numerics_IBinaryNumber_TSelf], System.Numerics.IBitwiseOperators[System_Numerics_IBinaryNumber_TSelf, System_Numerics_IBinaryNumber_TSelf, System_Numerics_IBinaryNumber_TSelf], System.Numerics.INumber[System_Numerics_IBinaryNumber_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""


class IFloatingPoint(typing.Generic[System_Numerics_IFloatingPoint_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IFloatingPoint_TSelf], System.Numerics.INumber[System_Numerics_IFloatingPoint_TSelf], System.Numerics.ISignedNumber[System_Numerics_IFloatingPoint_TSelf], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_exponent_byte_count(self) -> int:
        ...

    def get_exponent_shortest_bit_length(self) -> int:
        ...

    def get_significand_bit_length(self) -> int:
        ...

    def get_significand_byte_count(self) -> int:
        ...

    def try_write_exponent_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_write_exponent_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_write_significand_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_write_significand_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def write_exponent_big_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_exponent_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_exponent_big_endian(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def write_exponent_little_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_exponent_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_exponent_little_endian(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def write_significand_big_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_significand_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_significand_big_endian(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def write_significand_little_endian(self, destination: typing.List[int]) -> int:
        ...

    @overload
    def write_significand_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        ...

    @overload
    def write_significand_little_endian(self, destination: System.Span[int]) -> int:
        ...


