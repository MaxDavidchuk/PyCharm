#-------------------------------------------------------------------------------
# Name:         for_demo2
# Purpose:      Демонстрація реверсу.
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

def display_res():
        for k in range(max(a, b), min(a, b) - 1, -1):
            print(k, end=' ')
        print('Done!')

def main():
    try:
        input_range()
        display_res()


    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
