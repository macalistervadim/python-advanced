"""
данный пример демонстрирует работу дандер-методов
"""

import math
from typing import Any



class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    def __add__(self, other) -> "Vector":
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar: Any) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

