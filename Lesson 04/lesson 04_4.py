#-------------------------------------------------------------------------------
# Name:         factorial
# Purpose:      Обчислення факторіалу натурального числа.
#               Програма виводить назву цього дня
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def input_range():
        print('Введіть додатнє натуральне число (n >= 1):')
        n = int(input('n = '))
        if str(type(n)) == "<class 'float'>":
            raise RuntimeError('Число має бути цілим!')
        return n

def cal_f(n):
    f = 1
    for k in range(1, n + 1): f *= k
    return f

def display_res():
        num = input_range()
        print(f'Сума чисел діапазону складає: {num}! = {cal_f(num)}')

def main():
    try:
        display_res()
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    except RuntimeError as err2: print(f'Помилка даних: \n {err2}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
