#-------------------------------------------------------------------------------
# Name:         fibonachi
# Purpose:      Обчислення чисел ряду Фібоначчі.
#               Програма виводить назву цього дня
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def input_range():
        print('Введіть додатнє натуральне число (n >= 1):')
        n = int(input('n = '))
        if str(type(n)) == "<class 'float'>":
            raise ValueError('Число має бути цілим!')
        return int(n)

def generate_fibo(n):
    if n == 1: print(1)
    elif n == 2: print(1, 1)
    else:
        a = 1
        b = 1
        print(a, b, end=' ')
        for k in range(n -2):
            x = a + b
            print(x, end=' ')
            a = b
            b = x
    print()


def display_res():
        generate_fibo(input_range())

def main():
    try:
        display_res()
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    except RuntimeError as err2: print(f'Помилка даних: \n {err2}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
