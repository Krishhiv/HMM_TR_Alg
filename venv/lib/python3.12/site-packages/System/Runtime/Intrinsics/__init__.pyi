from typing import overload
from enum import IntEnum
import typing

import System.Numerics
import System.Runtime.Intrinsics

System_Runtime_Intrinsics_Vector128 = typing.Any
T = typing.Any
System_Runtime_Intrinsics_Vector64 = typing.Any
System_Runtime_Intrinsics_Vector512 = typing.Any
System_Runtime_Intrinsics_Vector256 = typing.Any

System_Runtime_Intrinsics_Vector128_T = typing.TypeVar("System_Runtime_Intrinsics_Vector128_T")
System_Runtime_Intrinsics_Vector64_T = typing.TypeVar("System_Runtime_Intrinsics_Vector64_T")
System_Runtime_Intrinsics_Vector512_T = typing.TypeVar("System_Runtime_Intrinsics_Vector512_T")
System_Runtime_Intrinsics_Vector256_T = typing.TypeVar("System_Runtime_Intrinsics_Vector256_T")


class Vector128(typing.Generic[System_Runtime_Intrinsics_Vector128_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector128, System_Runtime_Intrinsics_Vector128_T]):
    """This class has no documentation."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]

    COUNT: int

    INDICES: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]

    IS_SUPPORTED: bool

    ONE: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]

    ZERO: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]

    IS_HARDWARE_ACCELERATED: bool

    E: System.Runtime.Intrinsics.Vector128[T]

    PI: System.Runtime.Intrinsics.Vector128[T]

    TAU: System.Runtime.Intrinsics.Vector128[T]

    def __add__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector128_T:
        ...

    def __iadd__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __isub__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        ...

    def __neg__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __pos__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __sub__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        ...

    @staticmethod
    def as_plane(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Plane:
        ...

    @staticmethod
    def as_quaternion(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Quaternion:
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Plane) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Quaternion) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector2) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector3) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector4) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128_unsafe(value: System.Numerics.Vector2) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def as_vector_128_unsafe(value: System.Numerics.Vector3) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def as_vector_2(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def as_vector_3(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def as_vector_4(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector4:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class Vector64(typing.Generic[System_Runtime_Intrinsics_Vector64_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector64, System_Runtime_Intrinsics_Vector64_T]):
    """This class has no documentation."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]

    COUNT: int

    INDICES: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]

    IS_SUPPORTED: bool

    ONE: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]

    ZERO: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]

    IS_HARDWARE_ACCELERATED: bool

    E: System.Runtime.Intrinsics.Vector64[T]

    PI: System.Runtime.Intrinsics.Vector64[T]

    TAU: System.Runtime.Intrinsics.Vector64[T]

    def __add__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector64_T:
        ...

    def __iadd__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __isub__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        ...

    def __neg__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __pos__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __sub__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class Vector512(typing.Generic[System_Runtime_Intrinsics_Vector512_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector512, System_Runtime_Intrinsics_Vector512_T]):
    """This class has no documentation."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]

    COUNT: int

    INDICES: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]

    IS_SUPPORTED: bool

    ONE: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]

    ZERO: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]

    IS_HARDWARE_ACCELERATED: bool

    E: System.Runtime.Intrinsics.Vector512[T]

    PI: System.Runtime.Intrinsics.Vector512[T]

    TAU: System.Runtime.Intrinsics.Vector512[T]

    def __add__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector512_T:
        ...

    def __iadd__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __isub__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        ...

    def __neg__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __pos__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __sub__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class Vector256(typing.Generic[System_Runtime_Intrinsics_Vector256_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector256, System_Runtime_Intrinsics_Vector256_T]):
    """This class has no documentation."""

    IS_HARDWARE_ACCELERATED: bool

    E: System.Runtime.Intrinsics.Vector256[T]

    PI: System.Runtime.Intrinsics.Vector256[T]

    TAU: System.Runtime.Intrinsics.Vector256[T]

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]

    COUNT: int

    INDICES: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]

    IS_SUPPORTED: bool

    ONE: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]

    ZERO: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]

    def __add__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector256_T:
        ...

    def __iadd__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __isub__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        ...

    def __neg__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __pos__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __sub__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


