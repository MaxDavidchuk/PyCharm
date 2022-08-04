"""
    Lesson 16, Homework, Task 2, 04/08/2022
    ==========================================
    Запрограмуйте у класі Дріб перевантаження методу для
    додавання двох дробів.
"""


class Fraction(object):

    def __init__(self, num: int, dem: int, whole: int = 0):
        self.__num = num
        self.__dem = dem
        self.__whole = whole

    @property
    def num(self) -> int:
        return self.__num

    @property
    def dem(self) -> int:
        return self.__dem

    @property
    def whole(self) -> int:
        return self.__whole

    def __str__(self) -> str:
        s = '(' + str(self.whole) + ')' if self.whole != 0 else ''
        return f'{s}{self.num}/{self.dem}'

    def __add__(self, other):

        def find_nod(x: int, y: int) -> int:
            if y == 0:
                return int(x)
            else:
                return find_nod(y, x % y)

        def calculate(x: int, y: int):
            if x == y:
                return 1
            elif y == 1:
                return x
            elif x > y:
                return Fraction(int(x - (x // y) * y), y, int(x // y))
            else:
                return Fraction(x, y)

        a = Fraction(self.whole * self.dem + self.num, self.dem)
        b = Fraction(other.whole * other.dem + other.num, other.dem)
        if a.dem == b.dem:
            n = a.num + b.num
            m = a.dem
            nod = find_nod(n, m)
        else:
            n = a.num * b.dem + b.num * a.dem
            m = a.dem * b.dem
            nod = find_nod(n, m)
        return calculate(int(n / nod), int(m / nod))


if __name__ == '__main__':
    print('\nДодавання дробів:')
    print('============================')
    f01 = Fraction(1, 2)
    f02 = Fraction(1, 3)
    print(f'{f01} + {f02} = {f01 + f02}')
    print('============================')
    f11 = Fraction(5, 6)
    f12 = Fraction(8, 6)
    print(f'{f11} + {f12} = {f11 + f12}')
    print('============================')
    f21 = Fraction(1, 2)
    f22 = Fraction(1, 2, 1)
    print(f'{f21} + {f22} = {f21 + f22}')
    print('============================')
    f31 = Fraction(13, 8)
    f32 = Fraction(11, 6)
    print(f'{f31} + {f32} = {f31 + f32}')
    print('============================')
    f41 = Fraction(2, 5)
    f42 = Fraction(3, 7, 1)
    print(f'{f41} + {f42} = {f41 + f42}')
