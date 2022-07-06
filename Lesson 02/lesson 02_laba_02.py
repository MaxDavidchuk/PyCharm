#-------------------------------------------------------------------------------
# Name:        rectangle_calc
# Purpose:     Самостійна робота Laba 2
# Site:         https://pythonexercises.rozh2sch.org.ua/#_зміні_і_типи_даних
# Author:      Maxim Davidchuk
# Created:     15.06.2022
#-------------------------------------------------------------------------------

def calc(n):
    s = 123*n
    return(s)

def main():
        # 1. Введення початкових данихІ
        print('\n> Введіть 3 (три) цілих числа:')
        a, b, c = int(input('  a = ')), int(input('  b = ')), int(input('  c = '))

        # 2. Виконання і виведення обчислень
        print(calc(a))
        print(calc(b))
        print(calc(c))

if __name__ == '__main__':
    main()