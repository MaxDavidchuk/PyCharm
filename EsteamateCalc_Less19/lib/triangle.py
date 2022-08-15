from lib.shape import Shape
from math import sqrt


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):
        super().__init__('трикутник')
        self._a = a
        self._b = b
        self._c = c

    def __str__(self) -> str:
        return super().__str__() + f'; сторона A: {self._a}; сторона B: {self._b}; сторона C: {self._c}'

    def calc_square(self) -> float:
        a = self._a
        b = self._b
        c = self._c
        if a < b + c and b < a + c and c < a + b:
            p = (a + b + c) / 2
            return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        else:
            return 0
