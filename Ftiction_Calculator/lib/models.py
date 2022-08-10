from tkinter import messagebox


class Fraction(object):

    def __init__(self, num: int, den: int, ip: int = 0):
        self.__num = num
        self.__den = den
        self.__ip = ip

    def __str__(self) -> str:
        if self.__ip == 0:
            return f'{self.__num}/{self.__den}'
        else:
            return f'({self.__ip}){self.__num}/{self.__den}'

    @property
    def num(self) -> int:
        return  self.__num

    @property
    def den(self) -> int:
        return  self.__den

    @property
    def ip(self) -> int:
        return  self.__ip

    def __add__(self, other):
        x = self.__num * other.__den + self.__den * other.__num
        y = self.__den * other.__den
        return Fraction(x, y)

    def __sub__(self, other):
        x = self.__num * other.__den - self.__den * other.__num
        y = self.__den * other.__den
        return Fraction(x, y)

    def __mul__(self, other):
        x = self.__num * other.__num
        y = self.__den * other.__den
        return Fraction(x, y)

    def __truediv__(self, other):
        x = self.__num * other.__den
        y = self.__den * other.__num
        return Fraction(x, y)

    def reduce(self) -> None:
        a = self.__num
        b = self.__den
        if a < 0:
            a *= -1
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        self.__num /= a + b
        self.__den /= a + b

    def normalize(self) -> None:
        #
        if self.__num > self.__den:
            self.__ip = self.__num // self.__den
            self.__num = self.__num % self.__den
        elif self.num == self.__den:
            self.__ip = 1
        #
        self.__num = int(self.__num)
        self.__den = int(self.__den)
        self.__ip = int(self.__ip)


class CalcManager(object):

    def __init__(self, input_widgets: dict):
        self.__num1 = input_widgets['a1'].get()
        self.__den1 = input_widgets['b1'].get()
        self.__num2 = input_widgets['a2'].get()
        self.__den2 = input_widgets['b2'].get()
        self.__action = input_widgets['op'].get()

    def __str__(self) -> str:
        return f'{self.__num1}, {self.__den1}, {self.__num2}, ' \
               f'{self.__den2}, {self.__action}'

    def validate(self) -> bool:
        try:
            if not self.__num1.strip():
                raise RuntimeError('Ви не введи значення чисельника 1-го дробу')
            elif not self.__den1.strip():
                raise RuntimeError('Ви не введи значення знаменника 1-го дробу')
            elif not self.__num2.strip():
                raise RuntimeError('Ви не введи значення чисельника 2-го дробу')
            elif not self.__den2.strip():
                raise RuntimeError('Ви не введи значення знаменника 2-го дробу')
            elif not self.__action.strip():
                raise RuntimeError('Ви не введи символ дії між дробави')
            #
            self.__num1 = int(self.__num1)
            self.__num2 = int(self.__num2)
            self.__den1 = int(self.__den1)
            self.__den2 = int(self.__den2)
            #
            if self.__action not in ['+', '-', '*', '/']:
                raise RuntimeError(f'Ви ввели <{self.__action}> - це некоректний символ арифметичної дії!')
            return True

        except ValueError:
            messagebox.showwarning('Value Error', 'Серед вхідних даних є некоректні.\nПеревірте значення!')
            return False
        except RuntimeError as mess:
            messagebox.showwarning('Empty data', str(mess))
            return False

    def calc(self) -> Fraction:
        f1 = Fraction(self.__num1, self.__den1)
        f2 = Fraction(self.__num2, self.__den2)
        f3 = None
        #
        if self.__action == '+':
            f3 = f1 + f2
        elif self.__action == '-':
            f3 = f1 - f2
        elif self.__action == '*':
            f3 = f1 * f2
        elif self.__action == '/':
            f3 = f1 / f2
        #
        f3.reduce()
        f3.normalize()
        return f3
