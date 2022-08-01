from math import pi


class Circle(object):
    """ Клас Прямокутник """
    def __init__(self, radius: float):
        self.__r = radius
        self.__s = round(pi * (self.__r ** 2), 2)
        self.__c = round(2 * pi * self.__r, 2)

    def area_print(self):
        print(f'\n  Площа кола із радіусом R = {self.__r} складає S = {self.__s} кв.од.')

    def length_print(self):
        print(f'\n  Довжина кола із радіусом R = {self.__r} складає C = {self.__c} од.')


if __name__ == '__main__':
    r = Circle(float(input('> Введіть радіус кола: R = ')))
    r.area_print()
    r.length_print()
