from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.Wasm


class PackedSimd(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def add_pairwise_widening(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def all_true(value: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        ...

    @staticmethod
    @overload
    def all_true(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> bool:
        ...

    @staticmethod
    @overload
    def all_true(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> bool:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def any_true(value: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        ...

    @staticmethod
    @overload
    def any_true(value: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    @overload
    def any_true(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> bool:
        ...

    @staticmethod
    @overload
    def any_true(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> bool:
        ...

    @staticmethod
    def average_rounded(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def bitmask(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> int:
        ...

    @staticmethod
    @overload
    def bitmask(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> int:
        ...

    @staticmethod
    @overload
    def bitwise_select(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], select: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def bitwise_select(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], select: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def bitwise_select(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr], select: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def bitwise_select(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr], select: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def convert_narrowing_saturate_signed(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_narrowing_saturate_unsigned(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_double_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_double_lower(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_int_32_saturate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_u_int_32_saturate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def dot(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_scalar(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def extract_scalar(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        ...

    @staticmethod
    @overload
    def extract_scalar(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], index: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def extract_scalar(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], index: int) -> System.UIntPtr:
        ...

    @staticmethod
    def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def load_scalar_and_insert(address: typing.Any, vector: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def load_scalar_and_insert(address: typing.Any, vector: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def load_scalar_and_insert(address: typing.Any, vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], index: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def load_scalar_and_insert(address: typing.Any, vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], index: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def load_scalar_and_splat_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_scalar_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_widening_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply_rounded_saturate_q_15(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def pop_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def pseudo_max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def pseudo_min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def replace_scalar(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def replace_scalar(vector: System.Runtime.Intrinsics.Vector128[float], imm: int, value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def replace_scalar(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], imm: int, value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def replace_scalar(vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], imm: int, value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def round_to_nearest(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], count: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def sign_extend_widening_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def sign_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def splat(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def splat(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def splat(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[System.IntPtr], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[System.UIntPtr], index: int) -> None:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def swizzle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def truncate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    def zero_extend_widening_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def zero_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


