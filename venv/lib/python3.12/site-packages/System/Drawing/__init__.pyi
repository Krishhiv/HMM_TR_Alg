from typing import overload
from enum import IntEnum
import typing

import System
import System.Collections
import System.ComponentModel
import System.Drawing
import System.Globalization
import System.Numerics

System_Drawing_RectangleF = typing.Any
System_Drawing_Size = typing.Any
System_Drawing_Point = typing.Any
System_Drawing_Color = typing.Any
System_Drawing_Rectangle = typing.Any
System_Drawing_SizeF = typing.Any
System_Drawing_PointF = typing.Any


class PointF(System.IEquatable[System_Drawing_PointF]):
    """This class has no documentation."""

    EMPTY: System.Drawing.PointF

    @property
    def is_empty(self) -> bool:
        ...

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

    @overload
    def __add__(self, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @overload
    def __add__(self, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    def __eq__(self, right: System.Drawing.PointF) -> bool:
        ...

    @overload
    def __iadd__(self, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @overload
    def __iadd__(self, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    @overload
    def __init__(self, x: float, y: float) -> None:
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        ...

    @overload
    def __isub__(self, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @overload
    def __isub__(self, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    def __ne__(self, right: System.Drawing.PointF) -> bool:
        ...

    @overload
    def __sub__(self, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @overload
    def __sub__(self, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    @staticmethod
    @overload
    def add(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @staticmethod
    @overload
    def add(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.PointF) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def subtract(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        ...

    @staticmethod
    @overload
    def subtract(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        ...

    def to_string(self) -> str:
        ...

    def to_vector_2(self) -> System.Numerics.Vector2:
        ...


class SizeF(System.IEquatable[System_Drawing_SizeF]):
    """This class has no documentation."""

    EMPTY: System.Drawing.SizeF

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float) -> None:
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float) -> None:
        ...

    def __add__(self, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    def __eq__(self, sz_2: System.Drawing.SizeF) -> bool:
        ...

    def __iadd__(self, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    @overload
    def __imul__(self, right: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    @overload
    def __imul__(self, right: float) -> System.Drawing.SizeF:
        ...

    @overload
    def __init__(self, size: System.Drawing.SizeF) -> None:
        ...

    @overload
    def __init__(self, pt: System.Drawing.PointF) -> None:
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        ...

    @overload
    def __init__(self, width: float, height: float) -> None:
        ...

    def __isub__(self, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    def __itruediv__(self, right: float) -> System.Drawing.SizeF:
        ...

    @overload
    def __mul__(self, right: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    @overload
    def __mul__(self, right: float) -> System.Drawing.SizeF:
        ...

    def __ne__(self, sz_2: System.Drawing.SizeF) -> bool:
        ...

    def __sub__(self, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    def __truediv__(self, right: float) -> System.Drawing.SizeF:
        ...

    @staticmethod
    def add(sz_1: System.Drawing.SizeF, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.SizeF) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def subtract(sz_1: System.Drawing.SizeF, sz_2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        ...

    def to_point_f(self) -> System.Drawing.PointF:
        ...

    def to_size(self) -> System.Drawing.Size:
        ...

    def to_string(self) -> str:
        ...

    def to_vector_2(self) -> System.Numerics.Vector2:
        ...


class RectangleF(System.IEquatable[System_Drawing_RectangleF]):
    """This class has no documentation."""

    EMPTY: System.Drawing.RectangleF

    @property
    def location(self) -> System.Drawing.PointF:
        ...

    @location.setter
    def location(self, value: System.Drawing.PointF) -> None:
        ...

    @property
    def size(self) -> System.Drawing.SizeF:
        ...

    @size.setter
    def size(self, value: System.Drawing.SizeF) -> None:
        ...

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
    def width(self) -> float:
        ...

    @width.setter
    def width(self, value: float) -> None:
        ...

    @property
    def height(self) -> float:
        ...

    @height.setter
    def height(self, value: float) -> None:
        ...

    @property
    def left(self) -> float:
        ...

    @property
    def top(self) -> float:
        ...

    @property
    def right(self) -> float:
        ...

    @property
    def bottom(self) -> float:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    def __eq__(self, right: System.Drawing.RectangleF) -> bool:
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        ...

    @overload
    def __init__(self, location: System.Drawing.PointF, size: System.Drawing.SizeF) -> None:
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector4) -> None:
        ...

    def __ne__(self, right: System.Drawing.RectangleF) -> bool:
        ...

    @overload
    def contains(self, x: float, y: float) -> bool:
        ...

    @overload
    def contains(self, pt: System.Drawing.PointF) -> bool:
        ...

    @overload
    def contains(self, rect: System.Drawing.RectangleF) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.RectangleF) -> bool:
        ...

    @staticmethod
    def from_ltrb(left: float, top: float, right: float, bottom: float) -> System.Drawing.RectangleF:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def inflate(self, x: float, y: float) -> None:
        ...

    @overload
    def inflate(self, size: System.Drawing.SizeF) -> None:
        ...

    @staticmethod
    @overload
    def inflate(rect: System.Drawing.RectangleF, x: float, y: float) -> System.Drawing.RectangleF:
        ...

    @overload
    def intersect(self, rect: System.Drawing.RectangleF) -> None:
        ...

    @staticmethod
    @overload
    def intersect(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        ...

    def intersects_with(self, rect: System.Drawing.RectangleF) -> bool:
        ...

    @overload
    def offset(self, pos: System.Drawing.PointF) -> None:
        ...

    @overload
    def offset(self, x: float, y: float) -> None:
        ...

    def to_string(self) -> str:
        ...

    def to_vector_4(self) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def union(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        ...


class Point(System.IEquatable[System_Drawing_Point]):
    """This class has no documentation."""

    EMPTY: System.Drawing.Point

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def x(self) -> int:
        ...

    @x.setter
    def x(self, value: int) -> None:
        ...

    @property
    def y(self) -> int:
        ...

    @y.setter
    def y(self, value: int) -> None:
        ...

    def __add__(self, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    def __eq__(self, right: System.Drawing.Point) -> bool:
        ...

    def __iadd__(self, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    @overload
    def __init__(self, x: int, y: int) -> None:
        ...

    @overload
    def __init__(self, sz: System.Drawing.Size) -> None:
        ...

    @overload
    def __init__(self, dw: int) -> None:
        ...

    def __isub__(self, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    def __ne__(self, right: System.Drawing.Point) -> bool:
        ...

    def __sub__(self, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    @staticmethod
    def add(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    @staticmethod
    def ceiling(value: System.Drawing.PointF) -> System.Drawing.Point:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.Point) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def offset(self, dx: int, dy: int) -> None:
        ...

    @overload
    def offset(self, p: System.Drawing.Point) -> None:
        ...

    @staticmethod
    def round(value: System.Drawing.PointF) -> System.Drawing.Point:
        ...

    @staticmethod
    def subtract(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def truncate(value: System.Drawing.PointF) -> System.Drawing.Point:
        ...


class Size(System.IEquatable[System_Drawing_Size]):
    """This class has no documentation."""

    EMPTY: System.Drawing.Size

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def width(self) -> int:
        ...

    @width.setter
    def width(self, value: int) -> None:
        ...

    @property
    def height(self) -> int:
        ...

    @height.setter
    def height(self, value: int) -> None:
        ...

    def __add__(self, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    def __eq__(self, sz_2: System.Drawing.Size) -> bool:
        ...

    def __iadd__(self, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @overload
    def __imul__(self, right: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @overload
    def __imul__(self, right: int) -> System.Drawing.Size:
        ...

    @overload
    def __imul__(self, right: System.Drawing.Size) -> System.Drawing.SizeF:
        ...

    @overload
    def __imul__(self, right: float) -> System.Drawing.SizeF:
        ...

    @overload
    def __init__(self, pt: System.Drawing.Point) -> None:
        ...

    @overload
    def __init__(self, width: int, height: int) -> None:
        ...

    def __isub__(self, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @overload
    def __itruediv__(self, right: int) -> System.Drawing.Size:
        ...

    @overload
    def __itruediv__(self, right: float) -> System.Drawing.SizeF:
        ...

    @overload
    def __mul__(self, right: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @overload
    def __mul__(self, right: int) -> System.Drawing.Size:
        ...

    @overload
    def __mul__(self, right: System.Drawing.Size) -> System.Drawing.SizeF:
        ...

    @overload
    def __mul__(self, right: float) -> System.Drawing.SizeF:
        ...

    def __ne__(self, sz_2: System.Drawing.Size) -> bool:
        ...

    def __sub__(self, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @overload
    def __truediv__(self, right: int) -> System.Drawing.Size:
        ...

    @overload
    def __truediv__(self, right: float) -> System.Drawing.SizeF:
        ...

    @staticmethod
    def add(sz_1: System.Drawing.Size, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    @staticmethod
    def ceiling(value: System.Drawing.SizeF) -> System.Drawing.Size:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.Size) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def round(value: System.Drawing.SizeF) -> System.Drawing.Size:
        ...

    @staticmethod
    def subtract(sz_1: System.Drawing.Size, sz_2: System.Drawing.Size) -> System.Drawing.Size:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def truncate(value: System.Drawing.SizeF) -> System.Drawing.Size:
        ...


class KnownColor(IntEnum):
    """This class has no documentation."""

    ACTIVE_BORDER = 1

    ACTIVE_CAPTION = 1

    ACTIVE_CAPTION_TEXT = 2

    APP_WORKSPACE = 3

    CONTROL = 4

    CONTROL_DARK = 5

    CONTROL_DARK_DARK = 6

    CONTROL_LIGHT = 7

    CONTROL_LIGHT_LIGHT = 8

    CONTROL_TEXT = 9

    DESKTOP = 10

    GRAY_TEXT = 11

    HIGHLIGHT = 12

    HIGHLIGHT_TEXT = 13

    HOT_TRACK = 14

    INACTIVE_BORDER = 15

    INACTIVE_CAPTION = 16

    INACTIVE_CAPTION_TEXT = 17

    INFO = 18

    INFO_TEXT = 19

    MENU = 20

    MENU_TEXT = 21

    SCROLL_BAR = 22

    WINDOW = 23

    WINDOW_FRAME = 24

    WINDOW_TEXT = 25

    TRANSPARENT = 26

    ALICE_BLUE = 27

    ANTIQUE_WHITE = 28

    AQUA = 29

    AQUAMARINE = 30

    AZURE = 31

    BEIGE = 32

    BISQUE = 33

    BLACK = 34

    BLANCHED_ALMOND = 35

    BLUE = 36

    BLUE_VIOLET = 37

    BROWN = 38

    BURLY_WOOD = 39

    CADET_BLUE = 40

    CHARTREUSE = 41

    CHOCOLATE = 42

    CORAL = 43

    CORNFLOWER_BLUE = 44

    CORNSILK = 45

    CRIMSON = 46

    CYAN = 47

    DARK_BLUE = 48

    DARK_CYAN = 49

    DARK_GOLDENROD = 50

    DARK_GRAY = 51

    DARK_GREEN = 52

    DARK_KHAKI = 53

    DARK_MAGENTA = 54

    DARK_OLIVE_GREEN = 55

    DARK_ORANGE = 56

    DARK_ORCHID = 57

    DARK_RED = 58

    DARK_SALMON = 59

    DARK_SEA_GREEN = 60

    DARK_SLATE_BLUE = 61

    DARK_SLATE_GRAY = 62

    DARK_TURQUOISE = 63

    DARK_VIOLET = 64

    DEEP_PINK = 65

    DEEP_SKY_BLUE = 66

    DIM_GRAY = 67

    DODGER_BLUE = 68

    FIREBRICK = 69

    FLORAL_WHITE = 70

    FOREST_GREEN = 71

    FUCHSIA = 72

    GAINSBORO = 73

    GHOST_WHITE = 74

    GOLD = 75

    GOLDENROD = 76

    GRAY = 77

    GREEN = 78

    GREEN_YELLOW = 79

    HONEYDEW = 80

    HOT_PINK = 81

    INDIAN_RED = 82

    INDIGO = 83

    IVORY = 84

    KHAKI = 85

    LAVENDER = 86

    LAVENDER_BLUSH = 87

    LAWN_GREEN = 88

    LEMON_CHIFFON = 89

    LIGHT_BLUE = 90

    LIGHT_CORAL = 91

    LIGHT_CYAN = 92

    LIGHT_GOLDENROD_YELLOW = 93

    LIGHT_GRAY = 94

    LIGHT_GREEN = 95

    LIGHT_PINK = 96

    LIGHT_SALMON = 97

    LIGHT_SEA_GREEN = 98

    LIGHT_SKY_BLUE = 99

    LIGHT_SLATE_GRAY = 100

    LIGHT_STEEL_BLUE = 101

    LIGHT_YELLOW = 102

    LIME = 103

    LIME_GREEN = 104

    LINEN = 105

    MAGENTA = 106

    MAROON = 107

    MEDIUM_AQUAMARINE = 108

    MEDIUM_BLUE = 109

    MEDIUM_ORCHID = 110

    MEDIUM_PURPLE = 111

    MEDIUM_SEA_GREEN = 112

    MEDIUM_SLATE_BLUE = 113

    MEDIUM_SPRING_GREEN = 114

    MEDIUM_TURQUOISE = 115

    MEDIUM_VIOLET_RED = 116

    MIDNIGHT_BLUE = 117

    MINT_CREAM = 118

    MISTY_ROSE = 119

    MOCCASIN = 120

    NAVAJO_WHITE = 121

    NAVY = 122

    OLD_LACE = 123

    OLIVE = 124

    OLIVE_DRAB = 125

    ORANGE = 126

    ORANGE_RED = 127

    ORCHID = 128

    PALE_GOLDENROD = 129

    PALE_GREEN = 130

    PALE_TURQUOISE = 131

    PALE_VIOLET_RED = 132

    PAPAYA_WHIP = 133

    PEACH_PUFF = 134

    PERU = 135

    PINK = 136

    PLUM = 137

    POWDER_BLUE = 138

    PURPLE = 139

    RED = 140

    ROSY_BROWN = 141

    ROYAL_BLUE = 142

    SADDLE_BROWN = 143

    SALMON = 144

    SANDY_BROWN = 145

    SEA_GREEN = 146

    SEA_SHELL = 147

    SIENNA = 148

    SILVER = 149

    SKY_BLUE = 150

    SLATE_BLUE = 151

    SLATE_GRAY = 152

    SNOW = 153

    SPRING_GREEN = 154

    STEEL_BLUE = 155

    TAN = 156

    TEAL = 157

    THISTLE = 158

    TOMATO = 159

    TURQUOISE = 160

    VIOLET = 161

    WHEAT = 162

    WHITE = 163

    WHITE_SMOKE = 164

    YELLOW = 165

    YELLOW_GREEN = 166

    BUTTON_FACE = 167

    BUTTON_HIGHLIGHT = 168

    BUTTON_SHADOW = 169

    GRADIENT_ACTIVE_CAPTION = 170

    GRADIENT_INACTIVE_CAPTION = 171

    MENU_BAR = 172

    MENU_HIGHLIGHT = 173

    REBECCA_PURPLE = 174


class Color(System.IEquatable[System_Drawing_Color]):
    """This class has no documentation."""

    EMPTY: System.Drawing.Color

    TRANSPARENT: System.Drawing.Color

    ALICE_BLUE: System.Drawing.Color

    ANTIQUE_WHITE: System.Drawing.Color

    AQUA: System.Drawing.Color

    AQUAMARINE: System.Drawing.Color

    AZURE: System.Drawing.Color

    BEIGE: System.Drawing.Color

    BISQUE: System.Drawing.Color

    BLACK: System.Drawing.Color

    BLANCHED_ALMOND: System.Drawing.Color

    BLUE: System.Drawing.Color

    BLUE_VIOLET: System.Drawing.Color

    BROWN: System.Drawing.Color

    BURLY_WOOD: System.Drawing.Color

    CADET_BLUE: System.Drawing.Color

    CHARTREUSE: System.Drawing.Color

    CHOCOLATE: System.Drawing.Color

    CORAL: System.Drawing.Color

    CORNFLOWER_BLUE: System.Drawing.Color

    CORNSILK: System.Drawing.Color

    CRIMSON: System.Drawing.Color

    CYAN: System.Drawing.Color

    DARK_BLUE: System.Drawing.Color

    DARK_CYAN: System.Drawing.Color

    DARK_GOLDENROD: System.Drawing.Color

    DARK_GRAY: System.Drawing.Color

    DARK_GREEN: System.Drawing.Color

    DARK_KHAKI: System.Drawing.Color

    DARK_MAGENTA: System.Drawing.Color

    DARK_OLIVE_GREEN: System.Drawing.Color

    DARK_ORANGE: System.Drawing.Color

    DARK_ORCHID: System.Drawing.Color

    DARK_RED: System.Drawing.Color

    DARK_SALMON: System.Drawing.Color

    DARK_SEA_GREEN: System.Drawing.Color

    DARK_SLATE_BLUE: System.Drawing.Color

    DARK_SLATE_GRAY: System.Drawing.Color

    DARK_TURQUOISE: System.Drawing.Color

    DARK_VIOLET: System.Drawing.Color

    DEEP_PINK: System.Drawing.Color

    DEEP_SKY_BLUE: System.Drawing.Color

    DIM_GRAY: System.Drawing.Color

    DODGER_BLUE: System.Drawing.Color

    FIREBRICK: System.Drawing.Color

    FLORAL_WHITE: System.Drawing.Color

    FOREST_GREEN: System.Drawing.Color

    FUCHSIA: System.Drawing.Color

    GAINSBORO: System.Drawing.Color

    GHOST_WHITE: System.Drawing.Color

    GOLD: System.Drawing.Color

    GOLDENROD: System.Drawing.Color

    GRAY: System.Drawing.Color

    GREEN: System.Drawing.Color

    GREEN_YELLOW: System.Drawing.Color

    HONEYDEW: System.Drawing.Color

    HOT_PINK: System.Drawing.Color

    INDIAN_RED: System.Drawing.Color

    INDIGO: System.Drawing.Color

    IVORY: System.Drawing.Color

    KHAKI: System.Drawing.Color

    LAVENDER: System.Drawing.Color

    LAVENDER_BLUSH: System.Drawing.Color

    LAWN_GREEN: System.Drawing.Color

    LEMON_CHIFFON: System.Drawing.Color

    LIGHT_BLUE: System.Drawing.Color

    LIGHT_CORAL: System.Drawing.Color

    LIGHT_CYAN: System.Drawing.Color

    LIGHT_GOLDENROD_YELLOW: System.Drawing.Color

    LIGHT_GREEN: System.Drawing.Color

    LIGHT_GRAY: System.Drawing.Color

    LIGHT_PINK: System.Drawing.Color

    LIGHT_SALMON: System.Drawing.Color

    LIGHT_SEA_GREEN: System.Drawing.Color

    LIGHT_SKY_BLUE: System.Drawing.Color

    LIGHT_SLATE_GRAY: System.Drawing.Color

    LIGHT_STEEL_BLUE: System.Drawing.Color

    LIGHT_YELLOW: System.Drawing.Color

    LIME: System.Drawing.Color

    LIME_GREEN: System.Drawing.Color

    LINEN: System.Drawing.Color

    MAGENTA: System.Drawing.Color

    MAROON: System.Drawing.Color

    MEDIUM_AQUAMARINE: System.Drawing.Color

    MEDIUM_BLUE: System.Drawing.Color

    MEDIUM_ORCHID: System.Drawing.Color

    MEDIUM_PURPLE: System.Drawing.Color

    MEDIUM_SEA_GREEN: System.Drawing.Color

    MEDIUM_SLATE_BLUE: System.Drawing.Color

    MEDIUM_SPRING_GREEN: System.Drawing.Color

    MEDIUM_TURQUOISE: System.Drawing.Color

    MEDIUM_VIOLET_RED: System.Drawing.Color

    MIDNIGHT_BLUE: System.Drawing.Color

    MINT_CREAM: System.Drawing.Color

    MISTY_ROSE: System.Drawing.Color

    MOCCASIN: System.Drawing.Color

    NAVAJO_WHITE: System.Drawing.Color

    NAVY: System.Drawing.Color

    OLD_LACE: System.Drawing.Color

    OLIVE: System.Drawing.Color

    OLIVE_DRAB: System.Drawing.Color

    ORANGE: System.Drawing.Color

    ORANGE_RED: System.Drawing.Color

    ORCHID: System.Drawing.Color

    PALE_GOLDENROD: System.Drawing.Color

    PALE_GREEN: System.Drawing.Color

    PALE_TURQUOISE: System.Drawing.Color

    PALE_VIOLET_RED: System.Drawing.Color

    PAPAYA_WHIP: System.Drawing.Color

    PEACH_PUFF: System.Drawing.Color

    PERU: System.Drawing.Color

    PINK: System.Drawing.Color

    PLUM: System.Drawing.Color

    POWDER_BLUE: System.Drawing.Color

    PURPLE: System.Drawing.Color

    REBECCA_PURPLE: System.Drawing.Color

    RED: System.Drawing.Color

    ROSY_BROWN: System.Drawing.Color

    ROYAL_BLUE: System.Drawing.Color

    SADDLE_BROWN: System.Drawing.Color

    SALMON: System.Drawing.Color

    SANDY_BROWN: System.Drawing.Color

    SEA_GREEN: System.Drawing.Color

    SEA_SHELL: System.Drawing.Color

    SIENNA: System.Drawing.Color

    SILVER: System.Drawing.Color

    SKY_BLUE: System.Drawing.Color

    SLATE_BLUE: System.Drawing.Color

    SLATE_GRAY: System.Drawing.Color

    SNOW: System.Drawing.Color

    SPRING_GREEN: System.Drawing.Color

    STEEL_BLUE: System.Drawing.Color

    TAN: System.Drawing.Color

    TEAL: System.Drawing.Color

    THISTLE: System.Drawing.Color

    TOMATO: System.Drawing.Color

    TURQUOISE: System.Drawing.Color

    VIOLET: System.Drawing.Color

    WHEAT: System.Drawing.Color

    WHITE: System.Drawing.Color

    WHITE_SMOKE: System.Drawing.Color

    YELLOW: System.Drawing.Color

    YELLOW_GREEN: System.Drawing.Color

    @property
    def r(self) -> int:
        ...

    @property
    def g(self) -> int:
        ...

    @property
    def b(self) -> int:
        ...

    @property
    def a(self) -> int:
        ...

    @property
    def is_known_color(self) -> bool:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def is_named_color(self) -> bool:
        ...

    @property
    def is_system_color(self) -> bool:
        ...

    @property
    def name(self) -> str:
        ...

    def __eq__(self, right: System.Drawing.Color) -> bool:
        ...

    def __ne__(self, right: System.Drawing.Color) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.Color) -> bool:
        ...

    @staticmethod
    @overload
    def from_argb(argb: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(alpha: int, red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(alpha: int, base_color: System.Drawing.Color) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_known_color(color: System.Drawing.KnownColor) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_name(name: str) -> System.Drawing.Color:
        ...

    def get_brightness(self) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_hue(self) -> float:
        ...

    def get_saturation(self) -> float:
        ...

    def to_argb(self) -> int:
        ...

    def to_known_color(self) -> System.Drawing.KnownColor:
        ...

    def to_string(self) -> str:
        ...


class SystemColors(System.Object):
    """This class has no documentation."""

    ACTIVE_BORDER: System.Drawing.Color

    ACTIVE_CAPTION: System.Drawing.Color

    ACTIVE_CAPTION_TEXT: System.Drawing.Color

    APP_WORKSPACE: System.Drawing.Color

    BUTTON_FACE: System.Drawing.Color

    BUTTON_HIGHLIGHT: System.Drawing.Color

    BUTTON_SHADOW: System.Drawing.Color

    CONTROL: System.Drawing.Color

    CONTROL_DARK: System.Drawing.Color

    CONTROL_DARK_DARK: System.Drawing.Color

    CONTROL_LIGHT: System.Drawing.Color

    CONTROL_LIGHT_LIGHT: System.Drawing.Color

    CONTROL_TEXT: System.Drawing.Color

    DESKTOP: System.Drawing.Color

    GRADIENT_ACTIVE_CAPTION: System.Drawing.Color

    GRADIENT_INACTIVE_CAPTION: System.Drawing.Color

    GRAY_TEXT: System.Drawing.Color

    HIGHLIGHT: System.Drawing.Color

    HIGHLIGHT_TEXT: System.Drawing.Color

    HOT_TRACK: System.Drawing.Color

    INACTIVE_BORDER: System.Drawing.Color

    INACTIVE_CAPTION: System.Drawing.Color

    INACTIVE_CAPTION_TEXT: System.Drawing.Color

    INFO: System.Drawing.Color

    INFO_TEXT: System.Drawing.Color

    MENU: System.Drawing.Color

    MENU_BAR: System.Drawing.Color

    MENU_HIGHLIGHT: System.Drawing.Color

    MENU_TEXT: System.Drawing.Color

    SCROLL_BAR: System.Drawing.Color

    WINDOW: System.Drawing.Color

    WINDOW_FRAME: System.Drawing.Color

    WINDOW_TEXT: System.Drawing.Color

    use_alternative_color_set: bool


class Rectangle(System.IEquatable[System_Drawing_Rectangle]):
    """This class has no documentation."""

    EMPTY: System.Drawing.Rectangle

    @property
    def location(self) -> System.Drawing.Point:
        ...

    @location.setter
    def location(self, value: System.Drawing.Point) -> None:
        ...

    @property
    def size(self) -> System.Drawing.Size:
        ...

    @size.setter
    def size(self, value: System.Drawing.Size) -> None:
        ...

    @property
    def x(self) -> int:
        ...

    @x.setter
    def x(self, value: int) -> None:
        ...

    @property
    def y(self) -> int:
        ...

    @y.setter
    def y(self, value: int) -> None:
        ...

    @property
    def width(self) -> int:
        ...

    @width.setter
    def width(self, value: int) -> None:
        ...

    @property
    def height(self) -> int:
        ...

    @height.setter
    def height(self, value: int) -> None:
        ...

    @property
    def left(self) -> int:
        ...

    @property
    def top(self) -> int:
        ...

    @property
    def right(self) -> int:
        ...

    @property
    def bottom(self) -> int:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    def __eq__(self, right: System.Drawing.Rectangle) -> bool:
        ...

    @overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        ...

    @overload
    def __init__(self, location: System.Drawing.Point, size: System.Drawing.Size) -> None:
        ...

    def __ne__(self, right: System.Drawing.Rectangle) -> bool:
        ...

    @staticmethod
    def ceiling(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        ...

    @overload
    def contains(self, x: int, y: int) -> bool:
        ...

    @overload
    def contains(self, pt: System.Drawing.Point) -> bool:
        ...

    @overload
    def contains(self, rect: System.Drawing.Rectangle) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.Rectangle) -> bool:
        ...

    @staticmethod
    def from_ltrb(left: int, top: int, right: int, bottom: int) -> System.Drawing.Rectangle:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def inflate(self, width: int, height: int) -> None:
        ...

    @overload
    def inflate(self, size: System.Drawing.Size) -> None:
        ...

    @staticmethod
    @overload
    def inflate(rect: System.Drawing.Rectangle, x: int, y: int) -> System.Drawing.Rectangle:
        ...

    @overload
    def intersect(self, rect: System.Drawing.Rectangle) -> None:
        ...

    @staticmethod
    @overload
    def intersect(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        ...

    def intersects_with(self, rect: System.Drawing.Rectangle) -> bool:
        ...

    @overload
    def offset(self, pos: System.Drawing.Point) -> None:
        ...

    @overload
    def offset(self, x: int, y: int) -> None:
        ...

    @staticmethod
    def round(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def truncate(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        ...

    @staticmethod
    def union(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        ...


class ColorTranslator(System.Object):
    """This class has no documentation."""

    @staticmethod
    def from_html(html_color: str) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_ole(ole_color: int) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_win_32(win_32_color: int) -> System.Drawing.Color:
        ...

    @staticmethod
    def to_html(c: System.Drawing.Color) -> str:
        ...

    @staticmethod
    def to_ole(c: System.Drawing.Color) -> int:
        ...

    @staticmethod
    def to_win_32(c: System.Drawing.Color) -> int:
        ...


class SizeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

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


class PointConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

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


class SizeFConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

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


class RectangleConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

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


class ColorConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def __init__(self) -> None:
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

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


