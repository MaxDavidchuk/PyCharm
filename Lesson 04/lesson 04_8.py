#-------------------------------------------------------------------------------
# Name:         pifagor_table
# Purpose:      Генерація таблиці Піфагора. (Таблиця множення)
# Author:       dp_maxim
# Created:      22.06.2022
#-------------------------------------------------------------------------------

def main():
    try:
        for i in range(1,10):
            for j in range(1,10):
                x = i * j
                print(f'{x:3d}', end='')
            print()
    except ValueError as err1: print(f'Помилка значення: \n {err1}')
    except RuntimeError as err2: print(f'Помилка даних: \n {err2}')
    finally: print('\nПрограму завершено!')


if __name__ == '__main__':
    main()
