from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.X86


class X86Base(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def div_rem(lower: int, upper: int, divisor: int) -> System.ValueTuple[int, int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def cpu_id(function_id: int, sub_function_id: int) -> System.ValueTuple[int, int, int, int]:
        ...

    @staticmethod
    @overload
    def div_rem(lower: int, upper: int, divisor: int) -> System.ValueTuple[int, int]:
        ...

    @staticmethod
    @overload
    def div_rem(lower: System.UIntPtr, upper: System.UIntPtr, divisor: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def div_rem(lower: System.UIntPtr, upper: System.IntPtr, divisor: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        ...

    @staticmethod
    def pause() -> None:
        ...


class Sse(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

        @staticmethod
        def convert_to_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_ordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_unordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def convert_to_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_aligned_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_high(lower: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_low(upper: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_scalar_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def min_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_high_to_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_low_to_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def move_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def prefetch_0(address: typing.Any) -> None:
        ...

    @staticmethod
    def prefetch_1(address: typing.Any) -> None:
        ...

    @staticmethod
    def prefetch_2(address: typing.Any) -> None:
        ...

    @staticmethod
    def prefetch_non_temporal(address: typing.Any) -> None:
        ...

    @staticmethod
    def reciprocal(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def reciprocal_sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def shuffle(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_fence() -> None:
        ...

    @staticmethod
    def store_high(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_low(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...


class Sse2(System.Runtime.Intrinsics.X86.Sse, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_scalar_to_vector_128_int_64(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_scalar_to_vector_128_u_int_64(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
            ...

        @staticmethod
        @overload
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

        @staticmethod
        def convert_to_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

        @staticmethod
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
            ...

        @staticmethod
        def store_non_temporal(address: typing.Any, value: int) -> None:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
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
    def and_not(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def and_not(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
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
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
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
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_ordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_ordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_scalar_unordered_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_scalar_unordered_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_int_32(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_u_int_32(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def convert_to_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_aligned_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_fence() -> None:
        ...

    @staticmethod
    def load_high(lower: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_low(upper: System.Runtime.Intrinsics.Vector128[float], address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_scalar_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def load_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def mask_move(source: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], address: typing.Any) -> None:
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
    def max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def memory_fence() -> None:
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
    def min_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    @overload
    def move_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def move_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
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
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
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
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector128[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector128[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shuffle(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def sqrt_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
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
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_high(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_low(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    def store_non_temporal(address: typing.Any, value: int) -> None:
        ...

    @staticmethod
    @overload
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[float]) -> None:
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
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def xor(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...


class Sse3(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def add_subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_and_duplicate_to_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_dqu_vector_128(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def move_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_high_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_low_and_duplicate(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...


class Ssse3(System.Runtime.Intrinsics.X86.Sse3, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse3.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def horizontal_add_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def horizontal_subtract_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def sign(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Sse41(System.Runtime.Intrinsics.X86.Ssse3, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Ssse3.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
            ...

        @staticmethod
        def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def ceiling(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ceiling_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ceiling_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def dot_product(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def extract(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def extract(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        ...

    @staticmethod
    def floor(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def floor_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def floor_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def insert(value: System.Runtime.Intrinsics.Vector128[int], data: int, index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def insert(value: System.Runtime.Intrinsics.Vector128[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def load_aligned_vector_128_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def min_horizontal(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def round_current_direction(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_current_direction_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_current_direction_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_nearest_integer(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_nearest_integer_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_nearest_integer_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_negative_infinity_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_positive_infinity_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def round_to_zero(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_zero_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_to_zero_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def test_c(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        ...

    @staticmethod
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        ...

    @staticmethod
    def test_z(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> bool:
        ...


class Sse42(System.Runtime.Intrinsics.X86.Sse41, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse41.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def crc_32(crc: int, data: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def crc_32(crc: int, data: int) -> int:
        ...


class FloatComparisonMode(IntEnum):
    """This class has no documentation."""

    ORDERED_EQUAL_NON_SIGNALING = 0

    ORDERED_LESS_THAN_SIGNALING = 1

    ORDERED_LESS_THAN_OR_EQUAL_SIGNALING = 2

    UNORDERED_NON_SIGNALING = 3

    UNORDERED_NOT_EQUAL_NON_SIGNALING = 4

    UNORDERED_NOT_LESS_THAN_SIGNALING = 5

    UNORDERED_NOT_LESS_THAN_OR_EQUAL_SIGNALING = 6

    ORDERED_NON_SIGNALING = 7

    UNORDERED_EQUAL_NON_SIGNALING = 8

    UNORDERED_NOT_GREATER_THAN_OR_EQUAL_SIGNALING = 9

    UNORDERED_NOT_GREATER_THAN_SIGNALING = 10

    ORDERED_FALSE_NON_SIGNALING = 11

    ORDERED_NOT_EQUAL_NON_SIGNALING = 12

    ORDERED_GREATER_THAN_OR_EQUAL_SIGNALING = 13

    ORDERED_GREATER_THAN_SIGNALING = 14

    UNORDERED_TRUE_NON_SIGNALING = 15

    ORDERED_EQUAL_SIGNALING = 16

    ORDERED_LESS_THAN_NON_SIGNALING = 17

    ORDERED_LESS_THAN_OR_EQUAL_NON_SIGNALING = 18

    UNORDERED_SIGNALING = 19

    UNORDERED_NOT_EQUAL_SIGNALING = 20

    UNORDERED_NOT_LESS_THAN_NON_SIGNALING = 21

    UNORDERED_NOT_LESS_THAN_OR_EQUAL_NON_SIGNALING = 22

    ORDERED_SIGNALING = 23

    UNORDERED_EQUAL_SIGNALING = 24

    UNORDERED_NOT_GREATER_THAN_OR_EQUAL_NON_SIGNALING = 25

    UNORDERED_NOT_GREATER_THAN_NON_SIGNALING = 26

    ORDERED_FALSE_SIGNALING = 27

    ORDERED_NOT_EQUAL_SIGNALING = 28

    ORDERED_GREATER_THAN_OR_EQUAL_NON_SIGNALING = 29

    ORDERED_GREATER_THAN_NON_SIGNALING = 30

    UNORDERED_TRUE_SIGNALING = 31


class Avx(System.Runtime.Intrinsics.X86.Sse42, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse42.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def add_subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def blend(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def broadcast_scalar_to_vector_128(source: typing.Any) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def broadcast_scalar_to_vector_256(source: typing.Any) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def ceiling(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def compare_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def divide(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def dot_product(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def duplicate_even_indexed(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def duplicate_odd_indexed(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def floor(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def load_aligned_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def load_dqu_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def load_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector256[float]) -> int:
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def permute(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_var(left: System.Runtime.Intrinsics.Vector128[float], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def permute_var(left: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def reciprocal(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def reciprocal_sqrt(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def round_current_direction(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def round_to_nearest_integer(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def round_to_negative_infinity(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def round_to_positive_infinity(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def round_to_zero(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def sqrt(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        ...

    @staticmethod
    @overload
    def test_c(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        ...

    @staticmethod
    @overload
    def test_not_z_and_not_c(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> bool:
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> bool:
        ...

    @staticmethod
    @overload
    def test_z(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> bool:
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...


class FloatRoundingMode(IntEnum):
    """This class has no documentation."""

    TO_EVEN = ...

    TO_NEGATIVE_INFINITY = ...

    TO_POSITIVE_INFINITY = ...

    TO_ZERO = ...


class Gfni(System.Runtime.Intrinsics.X86.Sse41, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse41.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    class V256(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector256[int], a: System.Runtime.Intrinsics.Vector256[int], b: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector256[int], a: System.Runtime.Intrinsics.Vector256[int], b: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def galois_field_multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector512[int], a: System.Runtime.Intrinsics.Vector512[int], b: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector512[int], a: System.Runtime.Intrinsics.Vector512[int], b: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def galois_field_multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def galois_field_affine_transform(x: System.Runtime.Intrinsics.Vector128[int], a: System.Runtime.Intrinsics.Vector128[int], b: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def galois_field_affine_transform_inverse(x: System.Runtime.Intrinsics.Vector128[int], a: System.Runtime.Intrinsics.Vector128[int], b: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def galois_field_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Popcnt(System.Runtime.Intrinsics.X86.Sse42, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse42.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def pop_count(value: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def pop_count(value: int) -> int:
        ...


class Fma(System.Runtime.Intrinsics.X86.Avx, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_add(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_add(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def multiply_add_negated(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_add_negated(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_add_subtract(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_add_subtract(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_add(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_add(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...


class Avx2(System.Runtime.Intrinsics.X86.Avx, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def blend(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(source: typing.Any) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(source: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_256(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_16(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[float], scale: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_128(source: System.Runtime.Intrinsics.Vector128[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector128[float], scale: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[int], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[float], scale: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def gather_mask_vector_256(source: System.Runtime.Intrinsics.Vector256[float], base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector256[float], scale: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def gather_vector_128(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_128(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_256(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector256[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def gather_vector_256(base_address: typing.Any, index: System.Runtime.Intrinsics.Vector128[int], scale: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def horizontal_add(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def horizontal_add_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def horizontal_subtract(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def horizontal_subtract_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector256[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def load_aligned_vector_256_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_32(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_32(left: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector256[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector256[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def sign(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...


class Avx512F(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def align_right_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def align_right_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def align_right_64(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def align_right_64(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_not_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_ordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compare_unordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float], value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float], value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def fixup(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def fixup(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], table: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def get_exponent(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def get_exponent(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def get_mantissa(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def get_mantissa(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
            ...

        @staticmethod
        @overload
        def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def reciprocal_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def reciprocal_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def rotate_left(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def rotate_left(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def rotate_left_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def rotate_left_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def rotate_right(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def rotate_right(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def rotate_right_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def rotate_right_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def round_scale(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def round_scale(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def scale(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def scale(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector128[int], b: System.Runtime.Intrinsics.Vector128[int], c: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector256[int], b: System.Runtime.Intrinsics.Vector256[int], c: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def ternary_logic(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            ...

        @staticmethod
        def convert_to_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def add(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def align_right_32(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def align_right_64(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mask: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def compare_ordered(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def compare_unordered(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector512[float], mask: System.Runtime.Intrinsics.Vector512[float], value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        ...

    @staticmethod
    def convert_to_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_256_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_32(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_16(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def convert_to_vector_512_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def convert_to_vector_512_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def divide(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def divide(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def duplicate_even_indexed(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def duplicate_odd_indexed(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector512[float], mask: System.Runtime.Intrinsics.Vector512[float], value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], merge: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def fixup(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], table: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def fixup_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_add_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_add(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def fused_multiply_subtract_negated(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def get_exponent(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def get_mantissa(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def load_aligned_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def load_aligned_vector_512_non_temporal(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def load_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], merge: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], merge: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[float], source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector512[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector512[float]) -> int:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def permute_2x_64(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def permute_4x_32(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def permute_4x_64(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def permute_var_16x_32(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def permute_var_16x_32(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def permute_var_16x_32x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def permute_var_16x_32x_2(lower: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def permute_var_2x_64(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def permute_var_4x_32(left: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_64(value: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_64(value: System.Runtime.Intrinsics.Vector512[float], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_64x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_64x_2(lower: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def rotate_left(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def rotate_right(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def round_scale(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def round_scale_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_scale_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shuffle(value: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def shuffle_4x_128(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def shuffle_4x_128(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def sqrt(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def sqrt(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    @overload
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[float]) -> None:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def subtract(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector512[int], b: System.Runtime.Intrinsics.Vector512[int], c: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector512[float], b: System.Runtime.Intrinsics.Vector512[float], c: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...


class Avx512BW(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def blend_variable(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
            ...

        @staticmethod
        def permute_var_16x_16(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def permute_var_16x_16x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def permute_var_8x_16(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def permute_var_8x_16x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def abs(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def add(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def add_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def align_right(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def average(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def blend_variable(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def broadcast_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_less_than(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def convert_to_vector_256_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_s_byte(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_512_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def convert_to_vector_512_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def load_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    def max(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def min(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector512[int]) -> int:
        ...

    @staticmethod
    def multiply_add_adjacent(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def multiply_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def multiply_high_round_scale(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def pack_signed_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def pack_unsigned_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def permute_var_32x_16(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def permute_var_32x_16x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_left_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector512[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Runtime.Intrinsics.Vector512[int], count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_right_logical_128_bit_lane(value: System.Runtime.Intrinsics.Vector512[int], num_bytes: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector512[int], count: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shuffle(value: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shuffle_high(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def shuffle_low(value: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def store(address: typing.Any, source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    def subtract(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def subtract_saturate(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def sum_absolute_differences(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def unpack_high(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def unpack_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...


class Avx10v1(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

        @staticmethod
        @overload
        def convert_to_u_int_64(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
            ...

        @staticmethod
        def convert_to_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
            ...

    class V512(System.Runtime.Intrinsics.X86.Avx512BW, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        class X64(System.Runtime.Intrinsics.X86.Avx512BW.X64, metaclass=abc.ABCMeta):
            """This class has no documentation."""

            IS_SUPPORTED: bool

        IS_SUPPORTED: bool

        @staticmethod
        def And(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def and_not(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def classify(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def compress(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def expand(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        @overload
        def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def move_mask(value: System.Runtime.Intrinsics.Vector512[float]) -> int:
            ...

        @staticmethod
        @overload
        def move_mask(value: System.Runtime.Intrinsics.Vector512[int]) -> int:
            ...

        @staticmethod
        def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def multi_shift(control: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def Or(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def permute_var_64x_8(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def permute_var_64x_8x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def range(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def reduce(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def xor(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def abs(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def add_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def align_right_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def align_right_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def align_right_64(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def align_right_64(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def blend_variable(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def broadcast_pair_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def classify(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def classify(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def classify_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatComparisonMode) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_greater_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_greater_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_less_than(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_not_less_than_or_equal(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_ordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_ordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compare_unordered(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compare_unordered(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def compress(merge: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float], value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    def convert_scalar_to_vector_128_double(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int, mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_scalar_to_vector_128_single(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def convert_to_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    def convert_to_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_s_byte_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_16_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_saturation(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_128_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def convert_to_vector_128_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def convert_to_vector_256_u_int_32_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def divide_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector128[float], mask: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def expand(merge: System.Runtime.Intrinsics.Vector256[float], mask: System.Runtime.Intrinsics.Vector256[float], value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def fixup(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def fixup(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], table: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def fixup_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], table: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_add_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_add_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_negated_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def fused_multiply_subtract_scalar(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_exponent(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_exponent(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_exponent_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def get_mantissa_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], merge: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], merge: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def mask_load_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[float], source: System.Runtime.Intrinsics.Vector128[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[float], source: System.Runtime.Intrinsics.Vector256[float]) -> None:
        ...

    @staticmethod
    @overload
    def mask_store_aligned(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def max(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def min(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[float]) -> int:
        ...

    @staticmethod
    @overload
    def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def multiply_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def multi_shift(control: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multi_shift(control: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_var_16x_16(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_var_16x_16x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_var_16x_8(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def permute_var_16x_8x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def permute_var_2x_64x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def permute_var_32x_8(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_var_32x_8x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_32x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[float], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_64(value: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_var_4x_64x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def permute_var_8x_16(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def permute_var_8x_16x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def permute_var_8x_32x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def range(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def range(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def range_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reciprocal_sqrt_14_scalar(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reduce(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reduce(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def reduce_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reduce_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def rotate_left_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def rotate_right_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def round_scale(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_scale(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def round_scale_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round_scale_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def scale(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def scale_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_left_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector128[int], count: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def shift_right_logical_variable(value: System.Runtime.Intrinsics.Vector256[int], count: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def shuffle_2x_128(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    def sqrt_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def subtract_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def sum_absolute_differences_in_block_32(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector128[int], b: System.Runtime.Intrinsics.Vector128[int], c: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector128[float], b: System.Runtime.Intrinsics.Vector128[float], c: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector256[int], b: System.Runtime.Intrinsics.Vector256[int], c: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def ternary_logic(a: System.Runtime.Intrinsics.Vector256[float], b: System.Runtime.Intrinsics.Vector256[float], c: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...


class Avx10v2(System.Runtime.Intrinsics.X86.Avx10v1, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx10v1.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    class V512(System.Runtime.Intrinsics.X86.Avx10v1.V512, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        class X64(System.Runtime.Intrinsics.X86.Avx10v1.V512.X64, metaclass=abc.ABCMeta):
            """This class has no documentation."""

            IS_SUPPORTED: bool

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        @overload
        def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def min_max(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
            ...

        @staticmethod
        def multiple_sum_absolute_differences(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], mask: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def convert_to_s_byte_with_truncated_saturation_and_zero_extend_to_int_32(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def min_max(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def min_max(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def min_max_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def move_scalar(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def store_scalar(address: typing.Any, source: System.Runtime.Intrinsics.Vector128[int]) -> None:
        ...


class AvxVnniInt8(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector512[int], left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector512[int], left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...


class Bmi2(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def multiply_no_flags(left: int, right: int, low: typing.Any) -> int:
            ...

        @staticmethod
        @overload
        def multiply_no_flags(left: int, right: int) -> int:
            ...

        @staticmethod
        def parallel_bit_deposit(value: int, mask: int) -> int:
            ...

        @staticmethod
        def parallel_bit_extract(value: int, mask: int) -> int:
            ...

        @staticmethod
        def zero_high_bits(value: int, index: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_no_flags(left: int, right: int, low: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def multiply_no_flags(left: int, right: int) -> int:
        ...

    @staticmethod
    def parallel_bit_deposit(value: int, mask: int) -> int:
        ...

    @staticmethod
    def parallel_bit_extract(value: int, mask: int) -> int:
        ...

    @staticmethod
    def zero_high_bits(value: int, index: int) -> int:
        ...


class Pclmulqdq(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class V256(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def carryless_multiply(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int], control: int) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def carryless_multiply(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int], control: int) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def carryless_multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


class Avx512CD(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def detect_conflicts(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def leading_zero_count(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def detect_conflicts(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def leading_zero_count(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...


class Avx512Vbmi(System.Runtime.Intrinsics.X86.Avx512BW, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Runtime.Intrinsics.X86.Avx512BW.VL, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def multi_shift(control: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def multi_shift(control: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def permute_var_16x_8(left: System.Runtime.Intrinsics.Vector128[int], control: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def permute_var_16x_8x_2(lower: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def permute_var_32x_8(left: System.Runtime.Intrinsics.Vector256[int], control: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        def permute_var_32x_8x_2(lower: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512BW.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def multi_shift(control: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def permute_var_64x_8(left: System.Runtime.Intrinsics.Vector512[int], control: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def permute_var_64x_8x_2(lower: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...


class Avx512DQ(System.Runtime.Intrinsics.X86.Avx512F, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Runtime.Intrinsics.X86.Avx512F.VL, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def broadcast_pair_scalar_to_vector_128(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def broadcast_pair_scalar_to_vector_256(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def classify(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def classify(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        def convert_to_vector_128_double(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_vector_128_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_128_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_128_single(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        def convert_to_vector_128_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_128_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        def convert_to_vector_256_double(value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def convert_to_vector_256_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def multiply_low(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def multiply_low(left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def range(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def range(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

        @staticmethod
        @overload
        def reduce(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
            ...

        @staticmethod
        @overload
        def reduce(value: System.Runtime.Intrinsics.Vector256[float], control: int) -> System.Runtime.Intrinsics.Vector256[float]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512F.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def And(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def and_not(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def broadcast_pair_scalar_to_vector_512(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def broadcast_vector_128_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def broadcast_vector_256_to_vector_512(address: typing.Any) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def classify(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def classify_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_256_single(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_double(value: System.Runtime.Intrinsics.Vector512[int], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector256[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64(value: System.Runtime.Intrinsics.Vector512[float], mode: System.Runtime.Intrinsics.X86.FloatRoundingMode) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def convert_to_vector_512_u_int_64_with_truncation(value: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_128(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[int], index: int) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def extract_vector_256(value: System.Runtime.Intrinsics.Vector512[float], index: int) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector128[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def insert_vector_128(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector128[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[int], data: System.Runtime.Intrinsics.Vector256[int], index: int) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    @overload
    def insert_vector_256(value: System.Runtime.Intrinsics.Vector512[float], data: System.Runtime.Intrinsics.Vector256[float], index: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[float]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[float]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector256[int]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector512[float]) -> int:
        ...

    @staticmethod
    @overload
    def move_mask(value: System.Runtime.Intrinsics.Vector512[int]) -> int:
        ...

    @staticmethod
    def multiply_low(left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def Or(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def range(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def range_scalar(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def reduce(value: System.Runtime.Intrinsics.Vector512[float], control: int) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def reduce_scalar(value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def reduce_scalar(upper: System.Runtime.Intrinsics.Vector128[float], value: System.Runtime.Intrinsics.Vector128[float], control: int) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def xor(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...


class AvxVnni(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...


class Lzcnt(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def leading_zero_count(value: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...


class X86Serialize(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def serialize() -> None:
        ...


class Bmi1(System.Runtime.Intrinsics.X86.X86Base, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.X86Base.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def and_not(left: int, right: int) -> int:
            ...

        @staticmethod
        @overload
        def bit_field_extract(value: int, start: int, length: int) -> int:
            ...

        @staticmethod
        @overload
        def bit_field_extract(value: int, control: int) -> int:
            ...

        @staticmethod
        def extract_lowest_set_bit(value: int) -> int:
            ...

        @staticmethod
        def get_mask_up_to_lowest_set_bit(value: int) -> int:
            ...

        @staticmethod
        def reset_lowest_set_bit(value: int) -> int:
            ...

        @staticmethod
        def trailing_zero_count(value: int) -> int:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    def and_not(left: int, right: int) -> int:
        ...

    @staticmethod
    @overload
    def bit_field_extract(value: int, start: int, length: int) -> int:
        ...

    @staticmethod
    @overload
    def bit_field_extract(value: int, control: int) -> int:
        ...

    @staticmethod
    def extract_lowest_set_bit(value: int) -> int:
        ...

    @staticmethod
    def get_mask_up_to_lowest_set_bit(value: int) -> int:
        ...

    @staticmethod
    def reset_lowest_set_bit(value: int) -> int:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...


class AvxVnniInt16(System.Runtime.Intrinsics.X86.Avx2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Avx2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    class V512(System.Object, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector512[int], left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

        @staticmethod
        def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector512[int], left: System.Runtime.Intrinsics.Vector512[int], right: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
            ...

    IS_SUPPORTED: bool

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector128[int], left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def multiply_widening_and_add_saturate(addend: System.Runtime.Intrinsics.Vector256[int], left: System.Runtime.Intrinsics.Vector256[int], right: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        ...


class Avx512Vbmi2(System.Runtime.Intrinsics.X86.Avx512Vbmi, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class VL(System.Runtime.Intrinsics.X86.Avx512Vbmi.VL, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def compress(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], source: System.Runtime.Intrinsics.Vector128[int]) -> None:
            ...

        @staticmethod
        @overload
        def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], source: System.Runtime.Intrinsics.Vector256[int]) -> None:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector128[int], mask: System.Runtime.Intrinsics.Vector128[int], value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def expand(merge: System.Runtime.Intrinsics.Vector256[int], mask: System.Runtime.Intrinsics.Vector256[int], value: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector128[int], merge: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
            ...

        @staticmethod
        @overload
        def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector256[int], merge: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
            ...

    class X64(System.Runtime.Intrinsics.X86.Avx512Vbmi.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def compress(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def compress_store(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], source: System.Runtime.Intrinsics.Vector512[int]) -> None:
        ...

    @staticmethod
    def expand(merge: System.Runtime.Intrinsics.Vector512[int], mask: System.Runtime.Intrinsics.Vector512[int], value: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...

    @staticmethod
    def expand_load(address: typing.Any, mask: System.Runtime.Intrinsics.Vector512[int], merge: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        ...


class Aes(System.Runtime.Intrinsics.X86.Sse2, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class X64(System.Runtime.Intrinsics.X86.Sse2.X64, metaclass=abc.ABCMeta):
        """This class has no documentation."""

        IS_SUPPORTED: bool

    IS_SUPPORTED: bool

    @staticmethod
    def decrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def decrypt_last(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def encrypt(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def encrypt_last(value: System.Runtime.Intrinsics.Vector128[int], round_key: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def inverse_mix_columns(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    def keygen_assist(value: System.Runtime.Intrinsics.Vector128[int], control: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...


