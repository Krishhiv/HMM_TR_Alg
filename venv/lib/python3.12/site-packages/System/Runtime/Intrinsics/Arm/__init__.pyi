from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Numerics
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.Arm


class SveMaskPattern(IntEnum):
    """This class has no documentation."""

    LARGEST_POWER_OF_2 = 0

    VECTOR_COUNT_1 = 1

    VECTOR_COUNT_2 = 2

    VECTOR_COUNT_3 = 3

    VECTOR_COUNT_4 = 4

    VECTOR_COUNT_5 = 5

    VECTOR_COUNT_6 = 6

    VECTOR_COUNT_7 = 7

    VECTOR_COUNT_8 = 8

    VECTOR_COUNT_16 = 9

    VECTOR_COUNT_32 = 10

    VECTOR_COUNT_64 = 11

    VECTOR_COUNT_128 = 12

    VECTOR_COUNT_256 = 13

    LARGEST_MULTIPLE_OF_4 = 29

    LARGEST_MULTIPLE_OF_3 = 30

    ALL = 31


class SvePrefetchType(IntEnum):
    """This class has no documentation."""

    LOAD_L_1_TEMPORAL = 0

    LOAD_L_1_NON_TEMPORAL = 1

    LOAD_L_2_TEMPORAL = 2

    LOAD_L_2_NON_TEMPORAL = 3

    LOAD_L_3_TEMPORAL = 4

    LOAD_L_3_NON_TEMPORAL = 5

    STORE_L_1_TEMPORAL = 8

    STORE_L_1_NON_TEMPORAL = 9

    STORE_L_2_TEMPORAL = 10

    STORE_L_2_NON_TEMPORAL = 11

    STORE_L_3_TEMPORAL = 12

    STORE_L_3_NON_TEMPORAL = 13


class ArmBase(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def leading_sign_count(value: int) -> int:
            ...

        @staticmethod
        def leading_zero_count(value: int) -> int:
            ...

        @staticmethod
        def multiply_high(left: int, right: int) -> int:
            ...

        @staticmethod
        def reverse_element_bits(value: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def reverse_element_bits(value: int) -> int:
        ...

    @staticmethod
    def Yield() -> None:
        ...


class Crc32(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def compute_crc_32(crc: int, data: int) -> int:
            ...

        @staticmethod
        def compute_crc_32c(crc: int, data: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def compute_crc_32(crc: int, data: int) -> int:
        ...

    @staticmethod
    def compute_crc_32c(crc: int, data: int) -> int:
        ...


class Sha1(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def fixed_rotate(hash_e: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def hash_update_choose(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def hash_update_majority(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def hash_update_parity(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_e: System.Runtime.Intrinsics.Vector64[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def schedule_update_0(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_4_7: System.Runtime.Intrinsics.Vector128[int], w_8_11: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def schedule_update_1(tw_0_3: System.Runtime.Intrinsics.Vector128[int], w_12_15: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class AdvSimd(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def absolute_compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def absolute_compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def absolute_compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def absolute_compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def absolute_difference(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def absolute_difference_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def abs_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def abs_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def abs_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def add_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_across_widening(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_across_widening(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def add_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def add_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def add_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def compare_test(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_test(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_test_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def compare_test_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def convert_to_double(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_to_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_double_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def convert_to_double_upper(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_int_64_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_int_64_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_single_lower(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def convert_to_single_round_to_odd_lower(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def convert_to_single_round_to_odd_upper(lower: System.Runtime.Intrinsics.Vector64[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_single_upper(lower: System.Runtime.Intrinsics.Vector64[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_u_int_64_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def divide(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def duplicate_to_vector_128(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def duplicate_to_vector_128(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def extract_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def extract_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_scalar_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_add_scalar_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_scalar_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def fused_multiply_subtract_scalar_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int], value_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[int], result_index: int, value: System.Runtime.Intrinsics.Vector128[int], value_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float], value_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector64[float], result_index: int, value: System.Runtime.Intrinsics.Vector128[float], value_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int], value_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector128[int], value_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector128[float], value_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def insert_selected_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float], value_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def load_2_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_2_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_3_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_3_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_4_x_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_4_x_vector_128_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        @overload
        def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
            ...

        @staticmethod
        def load_and_replicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_2(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_3(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_and_replicate_to_vector_128x_4(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_pair_scalar_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            ...

        @staticmethod
        def load_pair_scalar_vector_64_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            ...

        @staticmethod
        def load_pair_vector_128(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_pair_vector_128_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
            ...

        @staticmethod
        def load_pair_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            ...

        @staticmethod
        def load_pair_vector_64_non_temporal(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
            ...

        @staticmethod
        def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def max_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def max_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def max_number_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def max_number_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def max_number_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def max_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def max_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def max_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def max_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def max_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def max_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def max_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def min_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def min_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def min_number_across(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def min_number_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def min_number_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def min_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def min_number_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def min_pairwise(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def min_pairwise(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def min_pairwise_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def min_pairwise_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def min_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def multiply_doubling_saturate_high_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def multiply_doubling_widening_and_add_saturate_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def multiply_doubling_widening_and_subtract_saturate_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def multiply_doubling_widening_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_saturate_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_saturate_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_doubling_widening_scalar_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_extended(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def multiply_extended_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def multiply_extended_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def multiply_extended_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def multiply_rounded_doubling_saturate_high_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def negate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def negate_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def negate_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def negate_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def reciprocal_estimate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def reciprocal_exponent_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def reciprocal_square_root_estimate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def reciprocal_square_root_step_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        def reciprocal_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def reciprocal_step_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def reverse_element_bits(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def reverse_element_bits(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def round_to_nearest(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def shift_arithmetic_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_arithmetic_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_left_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_left_logical_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_logical_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_arithmetic_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_arithmetic_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_arithmetic_rounded_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_logical_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def shift_right_logical_rounded_narrowing_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def sqrt(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[int], value_2: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[float], value_2: System.Runtime.Intrinsics.Vector128[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[int], value_2: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector128[float], value_2: System.Runtime.Intrinsics.Vector128[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_scalar(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_scalar(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_scalar_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[int], value_2: System.Runtime.Intrinsics.Vector64[int]) -> None:
            ...

        @staticmethod
        @overload
        def store_pair_scalar_non_temporal(address: typing.Any, value_1: System.Runtime.Intrinsics.Vector64[float], value_2: System.Runtime.Intrinsics.Vector64[float]) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]], index: int) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]) -> None:
            ...

        @staticmethod
        @overload
        def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]) -> None:
            ...

        @staticmethod
        def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def subtract_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def transpose_even(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def transpose_odd(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def unzip_even(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def unzip_odd(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector128[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def zip_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def zip_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def absolute_compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def absolute_difference_add(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def absolute_difference_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def absolute_difference_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def absolute_difference_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def absolute_difference_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def absolute_difference_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def abs_saturate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def abs_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def abs_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def add_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def add_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def add_pairwise_widening(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise_widening(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise_widening_and_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def add_pairwise_widening_and_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def add_pairwise_widening_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def add_rounded_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def add_rounded_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def add_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def add_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def add_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add_widening_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def add_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector64[int], mask: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector64[float], mask: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def bitwise_clear(value: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def bitwise_select(select: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ceiling(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def ceiling_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def compare_less_than(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def compare_test(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_test(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_int_32_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_int_32_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_int_32_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_int_32_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_int_32_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_single_scalar(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_u_int_32_round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_even(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_even_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32_round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_u_int_32_round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector_64(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_128(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_128(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_64(value: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def duplicate_to_vector_64(value: float) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector64[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector64[float], index: int) -> float:
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def extract(vector: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        ...

    @staticmethod
    def extract_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def extract_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def extract_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def extract_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def extract_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def extract_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(upper: System.Runtime.Intrinsics.Vector128[int], lower: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(upper: System.Runtime.Intrinsics.Vector128[float], lower: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def extract_vector_64(upper: System.Runtime.Intrinsics.Vector64[int], lower: System.Runtime.Intrinsics.Vector64[int], index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_64(upper: System.Runtime.Intrinsics.Vector64[float], lower: System.Runtime.Intrinsics.Vector64[float], index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def floor(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def floor_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def fused_add_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def fused_add_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def fused_add_rounded_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def fused_add_rounded_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add(addend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    def fused_multiply_add_scalar(addend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[float], left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(minuend: System.Runtime.Intrinsics.Vector64[float], left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def fused_subtract_halving(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def fused_subtract_halving(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector64[int], index: int, data: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector64[float], index: int, data: float) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector128[int], index: int, data: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def insert(vector: System.Runtime.Intrinsics.Vector128[float], index: int, data: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def insert_scalar(result: System.Runtime.Intrinsics.Vector128[float], result_index: int, value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def insert_scalar(result: System.Runtime.Intrinsics.Vector128[int], result_index: int, value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def leading_sign_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def leading_sign_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_2_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_2_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_3_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_3_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_4_x_vector_64(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_4_x_vector_64_and_unzip(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector64[int], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector64[float], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector128[int], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(value: System.Runtime.Intrinsics.Vector128[float], index: int, address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    @overload
    def load_and_insert_scalar(values: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int, address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        ...

    @staticmethod
    def load_and_replicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_and_replicate_to_vector_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_2(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_3(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_and_replicate_to_vector_64x_4(address: typing.Any) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_vector_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def max_number(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def max_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def max_number_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def min_number(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def min_number(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def min_number_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_add(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_add_by_selected_scalar(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_by_selected_scalar_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_lower_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_lower_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_lower_by_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_lower_by_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_lower_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_lower_by_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_lower_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_lower_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_upper_by_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_upper_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_saturate_upper_by_selected_scalar(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_upper_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_upper_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_upper_by_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_upper_by_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_doubling_widening_upper_by_selected_scalar_and_subtract_saturate(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_saturate_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_scalar_by_selected_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector128[float], right_index: int) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_by_selected_scalar(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_lower_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_lower_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_upper_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_widening_upper_and_subtract(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def negate_saturate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def negate_saturate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def negate_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def Not(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def Or(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def Or(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def or_not(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def or_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def polynomial_multiply(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def polynomial_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_estimate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_estimate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_square_root_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_step(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_step(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reverse_element_16(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def reverse_element_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def reverse_element_32(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def reverse_element_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def reverse_element_8(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def reverse_element_8(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def round_away_from_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_away_from_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_away_from_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_nearest(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_nearest(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_nearest_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_zero(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_rounded_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_arithmetic_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_arithmetic_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_arithmetic_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_arithmetic_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_arithmetic_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_and_insert(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_and_insert(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], shift: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_left_and_insert_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_left_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate_unsigned(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_saturate_unsigned(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_left_logical_saturate_unsigned_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_left_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_left_logical_widening_lower(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_left_logical_widening_upper(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_logical(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_rounded_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_rounded_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_logical_rounded_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_logical_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_saturate(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_logical_saturate(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_logical_saturate_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_and_insert(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_and_insert(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], shift: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_and_insert_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], shift: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_rounded_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded_add(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_rounded_add(addend: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_add_scalar(addend: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_lower(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def shift_right_logical_scalar(value: System.Runtime.Intrinsics.Vector64[int], count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def sign_extend_widening_lower(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def sign_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector64[int]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector64[float]) -> None:
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
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector64[int], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector64[float], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector128[int], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.Runtime.Intrinsics.Vector128[float], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_selected_scalar(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]], index: int) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_vector_and_zip(address: typing.Any, value: System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]) -> None:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def subtract_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def subtract_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_upper(lower: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def subtract_saturate_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def subtract_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def subtract_widening_lower(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def subtract_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.Runtime.Intrinsics.Vector128[int], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Runtime.Intrinsics.Vector64[int], table: System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]], byte_indexes: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
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
    def zero_extend_widening_lower(value: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def zero_extend_widening_upper(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Sve(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def abs(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def absolute_compare_greater_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def absolute_compare_greater_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def absolute_compare_less_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def absolute_compare_less_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def absolute_difference(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def add(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def add_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def add_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_rotate_complex(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], rotation: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def add_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_sequential_across(initial: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def And(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def and_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def bitwise_clear(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def boolean_not(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compact(mask: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compact(mask: System.Numerics.Vector[int], value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def compare_not_equal_to(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def compare_not_equal_to(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def compare_unordered(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def compute_16_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def compute_32_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def compute_64_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def compute_8_bit_addresses(bases: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[int], default_scalar: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[int], default_value: int, data: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[float], default_scalar: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element(mask: System.Numerics.Vector[float], default_value: float, data: System.Numerics.Vector[float]) -> float:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element_and_replicate(mask: System.Numerics.Vector[int], default_values: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_extract_after_last_active_element_and_replicate(mask: System.Numerics.Vector[float], default_values: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[int], default_scalar: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[int], default_value: int, data: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[float], default_scalar: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element(mask: System.Numerics.Vector[float], default_value: float, data: System.Numerics.Vector[float]) -> float:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element_and_replicate(mask: System.Numerics.Vector[int], default_values: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_extract_last_active_element_and_replicate(mask: System.Numerics.Vector[float], default_values: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def conditional_select(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def conditional_select(mask: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def convert_to_double(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def convert_to_double(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def convert_to_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def convert_to_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def convert_to_single(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def convert_to_u_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def count_16_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    def count_32_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    def count_64_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    def count_8_bit_elements(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    def create_break_after_mask(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_break_after_propagate_mask(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_break_before_mask(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_break_before_propagate_mask(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_break_propagate_mask(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_byte() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_double() -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def create_false_mask_int_16() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_int_32() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_int_64() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_s_byte() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_single() -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def create_false_mask_u_int_16() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_u_int_32() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_false_mask_u_int_64() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_mask_for_first_active_element(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_mask_for_next_active_element(total_mask: System.Numerics.Vector[int], from_mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_byte(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_double(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def create_true_mask_int_16(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_int_32(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_int_64(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_s_byte(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_single(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def create_true_mask_u_int_16(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_u_int_32(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_true_mask_u_int_64(pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_mask_16_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_mask_32_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_mask_64_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_mask_8_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_16_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_32_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_64_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def create_while_less_than_or_equal_mask_8_bit(left: int, right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def divide(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def dot_product(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def dot_product_by_selected_scalar(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector(data: System.Numerics.Vector[int], index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def duplicate_selected_scalar_to_vector(data: System.Numerics.Vector[float], index: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def extract_after_last_active_element(mask: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def extract_after_last_active_element(mask: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def extract_after_last_active_element_scalar(mask: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def extract_after_last_active_element_scalar(mask: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> float:
        ...

    @staticmethod
    @overload
    def extract_last_active_element(mask: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def extract_last_active_element(mask: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def extract_last_active_element_scalar(mask: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def extract_last_active_element_scalar(mask: System.Numerics.Vector[float], data: System.Numerics.Vector[float]) -> float:
        ...

    @staticmethod
    @overload
    def extract_vector(upper: System.Numerics.Vector[int], lower: System.Numerics.Vector[int], index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def extract_vector(upper: System.Numerics.Vector[float], lower: System.Numerics.Vector[float], index: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def floating_point_exponential_accelerator(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_add(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_add_by_selected_scalar(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_add_negated(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_subtract(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_by_selected_scalar(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_negated(minuend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_prefetch_16_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_16_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_32_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_32_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_64_bit(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_64_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_8_bit(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_prefetch_8_bit(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[float], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_int_16_with_byte_offsets_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_int_16_with_byte_offsets_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_int_32_with_byte_offsets_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_int_32_with_byte_offsets_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_u_int_16_with_byte_offsets_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_u_int_16_with_byte_offsets_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_u_int_32_with_byte_offsets_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def gather_vector_u_int_32_with_byte_offsets_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offset_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offset_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offsets(mask: System.Numerics.Vector[float], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def gather_vector_with_byte_offsets(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def get_active_element_count(mask: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def get_active_element_count(mask: System.Numerics.Vector[float], _from: System.Numerics.Vector[float]) -> int:
        ...

    @staticmethod
    def get_ffr_byte() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_int_16() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_int_32() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_int_64() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_s_byte() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_u_int_16() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_u_int_32() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def get_ffr_u_int_64() -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def insert_into_shifted_vector(left: System.Numerics.Vector[int], right: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def insert_into_shifted_vector(left: System.Numerics.Vector[float], right: float) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def leading_sign_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def leading_zero_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_2_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        ...

    @staticmethod
    @overload
    def load_2_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        ...

    @staticmethod
    @overload
    def load_3_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        ...

    @staticmethod
    @overload
    def load_3_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        ...

    @staticmethod
    @overload
    def load_4_x_vector_and_unzip(mask: System.Numerics.Vector[int], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        ...

    @staticmethod
    @overload
    def load_4_x_vector_and_unzip(mask: System.Numerics.Vector[float], address: typing.Any) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        ...

    @staticmethod
    @overload
    def load_vector(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def load_vector_128_and_replicate_to_vector(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_128_and_replicate_to_vector(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_non_faulting_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_byte_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_first_faulting(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_non_faulting_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_16_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_32_non_faulting_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_32_non_faulting_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_int_32_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_non_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_non_faulting(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def load_vector_non_temporal(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def load_vector_non_temporal(mask: System.Numerics.Vector[float], address: typing.Any) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_non_faulting_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_16(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_s_byte_sign_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_non_faulting_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_u_int_32(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_16_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_32_non_faulting_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_32_non_faulting_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_first_faulting(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_to_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def load_vector_u_int_32_zero_extend_to_u_int_64(mask: System.Numerics.Vector[int], address: typing.Any) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def max_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def max_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def max_number(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def max_number_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def min(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def min_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def min_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def min_number(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def min_number_across(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_add_rotate_complex(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], rotation: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_add_rotate_complex_by_selected_scalar(addend: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int, rotation: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_by_selected_scalar(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], right_index: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_extended(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def negate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def Not(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def Or(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def or_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def pop_count(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def prefetch_16_bit(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    def prefetch_32_bit(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    def prefetch_64_bit(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    def prefetch_8_bit(mask: System.Numerics.Vector[int], address: typing.Any, prefetch_type: System.Runtime.Intrinsics.Arm.SvePrefetchType) -> None:
        ...

    @staticmethod
    def reciprocal_estimate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reciprocal_exponent(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reciprocal_sqrt_step(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reciprocal_step(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reverse_bits(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def reverse_element(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def reverse_element(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def reverse_element_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def reverse_element_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def reverse_element_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def round_away_from_zero(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def round_to_nearest(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def round_to_zero(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_16_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_16_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_32_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_32_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_64_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_64_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def saturating_decrement_by_8_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_active_element_count(value: int, _from: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def saturating_decrement_by_active_element_count(value: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_16_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_16_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_32_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_32_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_64_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_64_bit_element_count(value: System.Numerics.Vector[int], scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def saturating_increment_by_8_bit_element_count(value: int, scale: int, pattern: System.Runtime.Intrinsics.Arm.SveMaskPattern = ...) -> int:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_active_element_count(value: int, _from: System.Numerics.Vector[int]) -> int:
        ...

    @staticmethod
    @overload
    def saturating_increment_by_active_element_count(value: System.Numerics.Vector[int], _from: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def scale(left: System.Numerics.Vector[float], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[float], address: typing.Any, indicies: System.Numerics.Vector[int], data: System.Numerics.Vector[float]) -> None:
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[int], address: typing.Any, indicies: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[float], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[float]) -> None:
        ...

    @staticmethod
    @overload
    def scatter(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_16_bit_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_16_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def scatter_16_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_32_bit_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, indices: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_32_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def scatter_32_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def scatter_8_bit_narrowing(mask: System.Numerics.Vector[int], addresses: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def scatter_8_bit_with_byte_offsets_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_with_byte_offsets(mask: System.Numerics.Vector[float], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[float]) -> None:
        ...

    @staticmethod
    @overload
    def scatter_with_byte_offsets(mask: System.Numerics.Vector[int], address: typing.Any, offsets: System.Numerics.Vector[int], data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def set_ffr(value: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    def shift_left_logical(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_for_divide(value: System.Numerics.Vector[int], control: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def sign_extend_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def sign_extend_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def sign_extend_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def sign_extend_widening_lower(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def sign_extend_widening_upper(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def splice(mask: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def splice(mask: System.Numerics.Vector[float], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def sqrt(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[int], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int], System.Numerics.Vector[int]]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.Numerics.Vector[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        ...

    @staticmethod
    @overload
    def store_and_zip(mask: System.Numerics.Vector[float], address: typing.Any, data: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float], System.Numerics.Vector[float]]) -> None:
        ...

    @staticmethod
    def store_narrowing(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_non_temporal(mask: System.Numerics.Vector[int], address: typing.Any, data: System.Numerics.Vector[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_non_temporal(mask: System.Numerics.Vector[float], address: typing.Any, data: System.Numerics.Vector[float]) -> None:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def subtract_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def test_any_true(mask: System.Numerics.Vector[int], right_mask: System.Numerics.Vector[int]) -> bool:
        ...

    @staticmethod
    def test_first_true(left_mask: System.Numerics.Vector[int], right_mask: System.Numerics.Vector[int]) -> bool:
        ...

    @staticmethod
    def test_last_true(left_mask: System.Numerics.Vector[int], right_mask: System.Numerics.Vector[int]) -> bool:
        ...

    @staticmethod
    @overload
    def transpose_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def transpose_even(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def transpose_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def transpose_odd(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def trigonometric_multiply_add_coefficient(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], control: int) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def trigonometric_select_coefficient(value: System.Numerics.Vector[float], selector: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def trigonometric_starting_value(value: System.Numerics.Vector[float], sign: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def unzip_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def unzip_even(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def unzip_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def unzip_odd(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(data: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(data: System.Numerics.Vector[float], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def xor_across(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def zero_extend_16(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def zero_extend_32(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def zero_extend_8(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def zero_extend_widening_lower(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def zero_extend_widening_upper(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def zip_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def zip_high(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def zip_low(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def zip_low(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...


class Sve2(System.Runtime.Intrinsics.Arm.Sve, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.Sve.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def absolute_difference_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def absolute_difference_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def absolute_difference_widening_lower_and_add_even(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def absolute_difference_widening_lower_and_add_odd(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def absolute_difference_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def abs_saturate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_carry_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], carry: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_carry_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], carry: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_high_narrowing_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_high_narrowing_odd(even: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def add_pairwise(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def add_pairwise_widening_and_add(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_rotate_complex(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_rounded_high_narrowing_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_rounded_high_narrowing_odd(even: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_saturate_rotate_complex(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_saturate_with_signed_addend(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_saturate_with_unsigned_addend(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_widening_even_odd(left_even: System.Numerics.Vector[int], right_odd: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def add_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def bitwise_clear_xor(xor: System.Numerics.Vector[int], value: System.Numerics.Vector[int], mask: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def bitwise_select(select: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def bitwise_select_left_inverted(select: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def bitwise_select_right_inverted(select: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def convert_to_double_odd(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def convert_to_single_even_round_to_odd(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def convert_to_single_odd(even: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def convert_to_single_odd_round_to_odd(even: System.Numerics.Vector[float], value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def dot_product_rotate_complex(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def dot_product_rotate_complex_by_selected_index(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int, rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def fused_add_halving(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def fused_add_rounded_halving(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def fused_subtract_halving(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def interleaving_xor_even_odd(odd: System.Numerics.Vector[int], left_even: System.Numerics.Vector[int], right_odd: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def interleaving_xor_odd_even(even: System.Numerics.Vector[int], left_odd: System.Numerics.Vector[int], right_even: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def log_2(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def max_number_pairwise(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def max_pairwise(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def min_number_pairwise(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def min_pairwise(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_add_by_selected_scalar(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_add_rotate_complex(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_add_rotate_complex_by_selected_scalar(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int, rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_add_rounded_doubling_saturate_high_rotate_complex(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_add_rounded_doubling_saturate_high_rotate_complex_by_selected_scalar(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int, rotation: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_even_and_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_even_and_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_odd_and_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_by_selected_scalar_widening_odd_and_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_by_selected_scalar_saturate_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_saturate_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_add_saturate_even(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_add_saturate_even_odd(addend: System.Numerics.Vector[int], left_even: System.Numerics.Vector[int], right_odd: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_add_saturate_odd(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_subtract_saturate_even(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_subtract_saturate_even_odd(minuend: System.Numerics.Vector[int], left_even: System.Numerics.Vector[int], right_odd: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_and_subtract_saturate_odd(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_by_selected_scalar_and_add_saturate_even(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_by_selected_scalar_and_add_saturate_odd(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_by_selected_scalar_and_subtract_saturate_even(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_by_selected_scalar_and_subtract_saturate_odd(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_even_by_selected_scalar(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_doubling_widening_saturate_odd_by_selected_scalar(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_by_selected_scalar_saturate_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_saturate_and_add_high(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_saturate_and_subtract_high(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_saturate_by_selected_scalar_and_add_high(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_saturate_by_selected_scalar_and_subtract_high(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_rounded_doubling_saturate_high(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_subtract_by_selected_scalar(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], right_index: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_even_and_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_even_and_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_odd_and_add(addend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def multiply_widening_odd_and_subtract(minuend: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def negate_saturate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def polynomial_multiply(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def reciprocal_estimate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_arithmetic_rounded(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_arithmetic_rounded_saturate(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_arithmetic_saturate(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_left_and_insert(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], shift: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_left_logical_saturate(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_left_logical_saturate_unsigned(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_left_logical_widening_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_left_logical_widening_odd(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_logical_rounded(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_logical_rounded_saturate(value: System.Numerics.Vector[int], count: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_and_insert(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], shift: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_add(addend: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_narrowing_saturate_unsigned_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_add(addend: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_rounded_narrowing_saturate_unsigned_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_add(addend: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_narrowing_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_add(addend: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_even(value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def shift_right_logical_rounded_narrowing_saturate_odd(even: System.Numerics.Vector[int], value: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_borrow_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], borrow: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_borrow_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], borrow: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_high_narrowing_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_high_narrowing_odd(even: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_rounded_high_narrowing_odd(even: System.Numerics.Vector[int], left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_saturate(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_widening_even(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_widening_even_odd(left_even: System.Numerics.Vector[int], right_odd: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_widening_odd(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def subtract_widening_odd_even(left_odd: System.Numerics.Vector[int], right_even: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Numerics.Vector[int], System.Numerics.Vector[int]], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup(table: System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Numerics.Vector[int], data: System.Numerics.Vector[int], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    @overload
    def vector_table_lookup_extension(default_values: System.Numerics.Vector[float], data: System.Numerics.Vector[float], indices: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def xor(value_1: System.Numerics.Vector[int], value_2: System.Numerics.Vector[int], value_3: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        ...

    @staticmethod
    def xor_rotate_right(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int], count: int) -> System.Numerics.Vector[int]:
        ...


class Rdm(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def multiply_rounded_doubling_and_add_saturate_high_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        def multiply_rounded_doubling_and_subtract_saturate_high_scalar(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

        @staticmethod
        @overload
        def multiply_rounded_doubling_scalar_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_add_saturate_high(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_rounded_doubling_by_selected_scalar_and_subtract_saturate_high(minuend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Sha256(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def hash_update_1(hash_abcd: System.Runtime.Intrinsics.Vector128[int], hash_efgh: System.Runtime.Intrinsics.Vector128[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def hash_update_2(hash_efgh: System.Runtime.Intrinsics.Vector128[int], hash_abcd: System.Runtime.Intrinsics.Vector128[int], wk: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def schedule_update_0(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_4_7: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def schedule_update_1(w_0_3: System.Runtime.Intrinsics.Vector128[int], w_8_11: System.Runtime.Intrinsics.Vector128[int], w_12_15: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Dp(System.Runtime.Intrinsics.Arm.AdvSimd, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.AdvSimd.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def dot_product(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def dot_product(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector64[int], left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector128[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector64[int]:
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def dot_product_by_selected_quadruplet(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector64[int], right_scaled_index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Aes(System.Runtime.Intrinsics.Arm.ArmBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class Arm64(System.Runtime.Intrinsics.Arm.ArmBase.Arm64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def decrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def encrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def inverse_mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_lower(left: System.Runtime.Intrinsics.Vector64[int], right: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def polynomial_multiply_widening_upper(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


