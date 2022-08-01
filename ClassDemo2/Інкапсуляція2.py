"""
    Властивість класу (Class Property)- це геттер із спрщеним синтаксисом,
    для якого можна включити статус Сеттера

"""
from lib import BankAccount2


if __name__ == '__main__':
    acc = BankAccount2(26001234567234, 'Василь Пупкін', 25615)
    print('\nВласник рахунку: ', acc.owner)

    debet = float(input('  Введіть суму переказу: '))
    acc.amount = debet + acc.amount
    print(acc)

    print('\n*** Finish ***')
