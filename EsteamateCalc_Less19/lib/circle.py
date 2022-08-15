from lib.shape import Shape


class Circle(Shape):

    def __init__(self, r: float):
        super().__init__('коло')
        self._radius = r

    def __str__(self) -> str:
        return super().__str__() + f'; радіус: {self._radius}'

    def calc_square(self) -> float:
        return round(3.1415 * self._radius ** 2, 2)
