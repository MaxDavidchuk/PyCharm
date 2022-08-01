class BankAccount(object):
    """ Банкывсий рахунок """
    def __init__(self, number: int, owner: str, amount: float):
        self.__acc_number = number
        self.__acc_owner = owner
        self.__acc_amount = amount

    def __str__(self):
        info = f'\n> Власник рахунку: {self.__acc_owner}'
        info += f'\n  Номер рахунку: {self.__acc_number}'
        info += f'\n  Залишок: {self.__acc_amount}'
        return info

    def get_owner(self):    # Getter - зчитування даних
        return self.__acc_owner

    def get_amount(self) -> float:
        return self.__acc_amount

    def set_amount(self, amount: float):   # Setter - зміна даних
        self.__acc_amount = amount


class BankAccount2(object):
    """ Банкывсий рахунок """
    def __init__(self, number: int, owner: str, amount: float):
        self.__acc_number = number
        self.__acc_owner = owner
        self.__acc_amount = amount

    def __str__(self):
        info = f'\n> Власник рахунку: {self.__acc_owner}'
        info += f'\n  Номер рахунку: {self.__acc_number}'
        info += f'\n  Залишок: {self.__acc_amount}'
        return info

    @property
    def owner(self) ->str:    # Getter - зчитування даних
        return self.__acc_owner

    @property
    def amount(self) -> float:
        return self.__acc_amount

    @amount.setter
    def amount(self, amount: float):   # Setter - зміна даних
        self.__acc_amount = amount
