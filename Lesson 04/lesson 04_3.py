#-------------------------------------------------------------------------------
# Name:         for_demo3
# Purpose:      Сума чисел діапазону.
#               Програма виводить назву цього дня
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------
a = 0
b = 0

def input_range():
        global a, b
        print('Введіть границі Вашого діапазону:')
        a = int(input('a = '))
        b = int(input('b = '))

def cal_sum():
    s = 0
    for k in range(max(a, b), min(a, b) - 1, -1): s += k
    return s

def display_res():
        print(f'Сума чисел діапазону складає: S = {cal_sum()}')

def main():
    try:
        input_range()
        display_res()
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
