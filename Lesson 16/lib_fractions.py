class Fraction(object):

    def __init__(self, num: int, dem: int, whole: int = 0):
        self.__num = num
        self.__dem = dem
        self.__whole = whole

    def __str__(self) -> str:
        if self.__whole != 0:
            return f'({self.__whole}){self.__num}/{self.__dem}'
        else:
            return f'{self.__num}/{self.__dem}'
