class Rectangle(object):
    """ Клас Прямокутник """
    def __init__(self, side_a: float, side_b: float):
        self.__a = side_a
        self.__b = side_b
        self.__s = round(self.__a * self.__b, 2)

    def area_print(self):
        area_s = f'  Площа прямокутника зі сторонами {self.__a} та {self.__b} складає S = {self.__s} кв.од.'
        print(area_s)


if __name__ == '__main__':
    r = Rectangle(float(input('> Введіть сторону a = ')), float(input('> Введіть сторону b = ')))
    r.area_print()
