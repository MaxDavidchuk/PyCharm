#-------------------------------------------------------------------------------
# Name:         quadratic_equation
# Purpose:      Програма розв'язування квадратних рівнянь ax**2+bx + c = 0
# Author:       dp_maxim
# Created:      20.06.2022
#-------------------------------------------------------------------------------
from math import sqrt
def main():
    try:
        print('> Введіть коефіцієнти по одному: ')
        a = float(input(  'a = '))
        b = float(input(  'b = '))
        c = float(input(  'c = '))
        if a == 0: print(f'  Результат: x = {round(-c/b, 2)}')
        else:
            d = b**2 - 4*a*c
            if d < 0: print(' Рівняння не має розв\'язків')
            if d == 0: print(f'  Результат: x = {round(-b/2/a, 2)}')
            else:
                print(f'  Результат 1: x1 = {round((-b-sqrt(d))/2/a, 2)}')
                print(f'  Результат 2: x2 = {round((-b+sqrt(d))/2/a, 2)}')
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    finally: print('Програму завершено!')

if __name__ == '__main__': main()
