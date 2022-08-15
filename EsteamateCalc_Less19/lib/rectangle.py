from lib.shape import Shape


class Rectangle(Shape):

    def __init__(self, a: float, b: float):
        super().__init__('прямокутник')
        self._width = a
        self._height = b

    def __str__(self) -> str:
        return super().__str__() + f'; ширина: {self._width}; висота: {self._height}'

    def calc_square(self) -> float:
        return round(self._height * self._width, 2)
