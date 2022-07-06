#-------------------------------------------------------------------------------
# Name:         fibonachi
# Purpose:      Циклічне введення даних (розумний input).
#               Програма виводить назву цього дня
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def input_range():
    while True:
        x = float(input('>Введіть додатнє число: x = '))
        if x == 0: print('  Число має бути додатнім!')
        else: break
    return x

def smth_calc(x):
    y = x ** 5
    return y

def display_res(x, y):
    print(f'{x} ^ 5 = {y}')

def main():
    try:
        a = input_range()
        b = smth_calc(a)
        display_res(a, b)
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    except RuntimeError as err2: print(f'Помилка даних: \n {err2}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
