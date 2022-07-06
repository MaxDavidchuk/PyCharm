#-------------------------------------------------------------------------------
# Name:         calc_digits
# Purpose:      Обчислення кількості та суми числа.
#               Цикл з умовою
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def input_range():
    print('Введіть додатнє натуральне число (n >= 1):')
    n = int(input('n = '))
    if str(type(n)) == "<class 'float'>":
        raise ValueError('Число має бути цілим!')
    return n

def calc(x):
    k = 0 # - кількість цифр
    s = 0 # - сума цифр числа
    temp = x # - робоча зміна циклу
    while temp != 0:
        k += 1
        s += temp % 10
        temp //= 10
    y = (k, s) # створення кортежу (цілісний, незмінний список)
    return y

def display_res(*arg):
    print(f'Кількість цифр: {arg[0]}')
    print(f'Сума цифр: {arg[1]}')

def main():
    try:
        x = input_range()
        y = calc(x)
        display_res(y[0], y[1])
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    except RuntimeError as err2: print(f'Помилка даних: \n {err2}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
