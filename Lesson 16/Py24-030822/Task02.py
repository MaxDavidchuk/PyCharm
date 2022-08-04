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


class Arr(object):

    def __init__(self):
        self.__fraction = []

    def __str__(self) -> str:
        return f'\nДодавання дробів ({int(len(self.__fraction) / 2)} прикладів):'

    @property
    def fraction(self):
        return self.__fraction

    def add_fraction(self, fraction: Fraction) -> None:
        self.__fraction.append(fraction)


class Rule(object):

    def __init__(self):
        self.__arr = Arr()

    @property
    def arr(self):
        return self.__arr

    def init_data(self) -> None:
        self.__arr.add_fraction(Fraction(1, 2))
        self.__arr.add_fraction(Fraction(1, 3))
        self.__arr.add_fraction(Fraction(5, 6))
        self.__arr.add_fraction(Fraction(8, 6))
        self.__arr.add_fraction(Fraction(1, 2))
        self.__arr.add_fraction(Fraction(1, 2, 1))
        self.__arr.add_fraction(Fraction(13, 8))
        self.__arr.add_fraction(Fraction(11, 6))
        self.__arr.add_fraction(Fraction(2, 5))
        self.__arr.add_fraction(Fraction(3, 7, 1))


if __name__ == '__main__':
    run = Rule()
    run.init_data()
    print(run.arr)
    for i in range(0, len(run.arr.fraction) - 1, 2):
        print('=========================')
        print(f'{run.arr.fraction[i]} + {run.arr.fraction[i + 1]} = '
              f'{run.arr.fraction[i] + run.arr.fraction[i + 1]}')
