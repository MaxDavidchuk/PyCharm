from tkinter import messagebox


class Currency(object):

    def __init__(self, rate: float, amount: float):
        self.__amount = amount
        self.__rate = rate

    def __str__(self) -> str:
        return f'Сума: {self.__amount}; курс: {self.__rate}'

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def rate(self) -> float:
        return self.__rate

    def __mul__(self, other):
        return Currency(1, self.__rate * self.__amount)


class CalcManager(object):

    def __init__(self, input_widgets: dict):
        self.__rate1 = input_widgets['rate1']
        self.__amount1 = input_widgets['amount1']
        self.__rate2 = input_widgets['rate2']
        self.__amount2 = input_widgets['amount2']

    def __str__(self) -> str:
        return f'{self.__rate1}, {self.__amount1}, {self.__rate2}, {self.__amount2}'

    def calc(self) -> Currency:
        f1 = Currency(self.__rate1, self.__amount1)
        f2 = Currency(self.__rate2, self.__amount2)
        return f1 * f2

    def validate(self) -> bool:
        try:
            if not self.__amount1:
                self.__amount1 = 0
                return True
            else:
                temp = float(self.__amount1)
                self.__amount1 = temp
                return True
        except ValueError:
            messagebox.showwarning('Value Error', 'Введена сума не э числом.\nПеревірте значення!')
            return False
