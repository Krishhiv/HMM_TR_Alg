from typing import overload
from enum import IntEnum
import typing

import System
import System.Buffers.Binary
import System.Numerics


class BinaryPrimitives(System.Object):
    """This class has no documentation."""

    @staticmethod
    def read_b_float_16_big_endian(source: System.ReadOnlySpan[int]) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def read_b_float_16_little_endian(source: System.ReadOnlySpan[int]) -> System.Numerics.BFloat16:
        ...

    @staticmethod
    def read_double_big_endian(source: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    def read_double_little_endian(source: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    def read_half_big_endian(source: System.ReadOnlySpan[int]) -> System.Half:
        ...

    @staticmethod
    def read_half_little_endian(source: System.ReadOnlySpan[int]) -> System.Half:
        ...

    @staticmethod
    def read_int_128_big_endian(source: System.ReadOnlySpan[int]) -> System.Int128:
        ...

    @staticmethod
    def read_int_128_little_endian(source: System.ReadOnlySpan[int]) -> System.Int128:
        ...

    @staticmethod
    def read_int_16_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_16_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_32_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_32_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_64_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_64_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_int_ptr_big_endian(source: System.ReadOnlySpan[int]) -> System.IntPtr:
        ...

    @staticmethod
    def read_int_ptr_little_endian(source: System.ReadOnlySpan[int]) -> System.IntPtr:
        ...

    @staticmethod
    def read_single_big_endian(source: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    def read_single_little_endian(source: System.ReadOnlySpan[int]) -> float:
        ...

    @staticmethod
    def read_u_int_128_big_endian(source: System.ReadOnlySpan[int]) -> System.UInt128:
        ...

    @staticmethod
    def read_u_int_128_little_endian(source: System.ReadOnlySpan[int]) -> System.UInt128:
        ...

    @staticmethod
    def read_u_int_16_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_16_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_32_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_32_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_64_big_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_64_little_endian(source: System.ReadOnlySpan[int]) -> int:
        ...

    @staticmethod
    def read_u_int_ptr_big_endian(source: System.ReadOnlySpan[int]) -> System.UIntPtr:
        ...

    @staticmethod
    def read_u_int_ptr_little_endian(source: System.ReadOnlySpan[int]) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: int) -> int:
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.UIntPtr], destination: System.Span[System.UIntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.IntPtr], destination: System.Span[System.IntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.UInt128], destination: System.Span[System.UInt128]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.Int128], destination: System.Span[System.Int128]) -> None:
        ...

    @staticmethod
    def try_read_b_float_16_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    def try_read_b_float_16_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Numerics.BFloat16]) -> typing.Tuple[bool, System.Numerics.BFloat16]:
        ...

    @staticmethod
    def try_read_double_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    def try_read_double_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    def try_read_half_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    def try_read_half_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    def try_read_int_128_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    def try_read_int_128_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    def try_read_int_16_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_16_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_32_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_32_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_64_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_64_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_int_ptr_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    def try_read_int_ptr_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    def try_read_single_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    def try_read_single_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    def try_read_u_int_128_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    def try_read_u_int_128_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    def try_read_u_int_16_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_16_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_32_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_32_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_64_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_64_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_read_u_int_ptr_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    def try_read_u_int_ptr_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    def try_write_b_float_16_big_endian(destination: System.Span[int], value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def try_write_b_float_16_little_endian(destination: System.Span[int], value: System.Numerics.BFloat16) -> bool:
        ...

    @staticmethod
    def try_write_double_big_endian(destination: System.Span[int], value: float) -> bool:
        ...

    @staticmethod
    def try_write_double_little_endian(destination: System.Span[int], value: float) -> bool:
        ...

    @staticmethod
    def try_write_half_big_endian(destination: System.Span[int], value: System.Half) -> bool:
        ...

    @staticmethod
    def try_write_half_little_endian(destination: System.Span[int], value: System.Half) -> bool:
        ...

    @staticmethod
    def try_write_int_128_big_endian(destination: System.Span[int], value: System.Int128) -> bool:
        ...

    @staticmethod
    def try_write_int_128_little_endian(destination: System.Span[int], value: System.Int128) -> bool:
        ...

    @staticmethod
    def try_write_int_16_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_16_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_32_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_32_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_64_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_64_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_int_ptr_big_endian(destination: System.Span[int], value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def try_write_int_ptr_little_endian(destination: System.Span[int], value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def try_write_single_big_endian(destination: System.Span[int], value: float) -> bool:
        ...

    @staticmethod
    def try_write_single_little_endian(destination: System.Span[int], value: float) -> bool:
        ...

    @staticmethod
    def try_write_u_int_128_big_endian(destination: System.Span[int], value: System.UInt128) -> bool:
        ...

    @staticmethod
    def try_write_u_int_128_little_endian(destination: System.Span[int], value: System.UInt128) -> bool:
        ...

    @staticmethod
    def try_write_u_int_16_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_16_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_32_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_32_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_64_big_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_64_little_endian(destination: System.Span[int], value: int) -> bool:
        ...

    @staticmethod
    def try_write_u_int_ptr_big_endian(destination: System.Span[int], value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def try_write_u_int_ptr_little_endian(destination: System.Span[int], value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def write_b_float_16_big_endian(destination: System.Span[int], value: System.Numerics.BFloat16) -> None:
        ...

    @staticmethod
    def write_b_float_16_little_endian(destination: System.Span[int], value: System.Numerics.BFloat16) -> None:
        ...

    @staticmethod
    def write_double_big_endian(destination: System.Span[int], value: float) -> None:
        ...

    @staticmethod
    def write_double_little_endian(destination: System.Span[int], value: float) -> None:
        ...

    @staticmethod
    def write_half_big_endian(destination: System.Span[int], value: System.Half) -> None:
        ...

    @staticmethod
    def write_half_little_endian(destination: System.Span[int], value: System.Half) -> None:
        ...

    @staticmethod
    def write_int_128_big_endian(destination: System.Span[int], value: System.Int128) -> None:
        ...

    @staticmethod
    def write_int_128_little_endian(destination: System.Span[int], value: System.Int128) -> None:
        ...

    @staticmethod
    def write_int_16_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_16_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_32_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_32_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_64_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_64_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_int_ptr_big_endian(destination: System.Span[int], value: System.IntPtr) -> None:
        ...

    @staticmethod
    def write_int_ptr_little_endian(destination: System.Span[int], value: System.IntPtr) -> None:
        ...

    @staticmethod
    def write_single_big_endian(destination: System.Span[int], value: float) -> None:
        ...

    @staticmethod
    def write_single_little_endian(destination: System.Span[int], value: float) -> None:
        ...

    @staticmethod
    def write_u_int_128_big_endian(destination: System.Span[int], value: System.UInt128) -> None:
        ...

    @staticmethod
    def write_u_int_128_little_endian(destination: System.Span[int], value: System.UInt128) -> None:
        ...

    @staticmethod
    def write_u_int_16_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_16_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_32_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_32_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_64_big_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_64_little_endian(destination: System.Span[int], value: int) -> None:
        ...

    @staticmethod
    def write_u_int_ptr_big_endian(destination: System.Span[int], value: System.UIntPtr) -> None:
        ...

    @staticmethod
    def write_u_int_ptr_little_endian(destination: System.Span[int], value: System.UIntPtr) -> None:
        ...


