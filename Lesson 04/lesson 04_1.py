#-------------------------------------------------------------------------------
# Name:         for_demo1
# Purpose:      Демонстрація синтаксису for.
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def main():
    try:
        # [0;6]
        print('--> 1')
        for k in range(7): print(f'k = {k}')
        # [0;6]
        print('--> 2')
        for x in range(1,7): print(f'x = {x}')
        # 1, 3, 5
        print('--> 3')
        for q in range(1,7,2): print(f'q = {q}')
        # [7,1]
        print('--> 4')
        for w in range(7,0,-1): print(f'w = {w}')

    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    finally: print('Програму завершено!')


if __name__ == '__main__':
    main()
