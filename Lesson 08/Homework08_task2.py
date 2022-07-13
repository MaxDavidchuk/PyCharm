"""
    2. Створіть програму для пошуку назв столиць держав світу за
назвами країн, розмістивши самі дані у окремому json-файлі.
"""

import json


def read_data(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        return json.load(file)


def display_menu(x: list) -> None:
    print('\nВиберіть частину Європи:')
    k = 0
    for eur in x:
        k += 1
        print(f'{k} - {eur}')
    print('0 - Завершити роботу\n')


def get_choice() -> int:
    choice = int(input('> Виберіть потрібний вам варіант: '))
    return choice


def break_work() -> bool:
    result = input('> Продовжити (y/n)? - ')
    return result == 'n'


def search_data(x: dict, s: str) -> None:
    n = len(x)
    temp = []
    print(f'{s} має такі держави:')
    for k in range(n):
        print(f'{k+1:3}. {list(x[k])[0]}')
        temp.append(list(x[k])[0])
    while True:
        print('\nВведіть номер держави, щоб дізнатися назву столиці,')
        print('або введіть "0", щоб повернутися у попереднє меню')
        num = int(input('> '))
        if 1 <= num <= n:
            print(f'  Держава {temp[num - 1]} має таку столицю: {x[num - 1][temp[num - 1]]}')
        elif num == 0:
            break
        else:
            print('  Помилка вводу. Спробуйте ще раз.')


if __name__ == '__main__':
    print("""
    =========================================
    =       Назва столиці держави Європи    =
    =               за її назваою           =
    =========================================""")
    d = read_data('base.json')
    part = ["Західна Європа", "Південна Європа", "Північна Європа", "Східна Європа"]
    while True:
        display_menu(part)
        case = get_choice()
        if 1 <= case <= 4:
            search_data(d[str(case)], part[case - 1])
        elif case == 0:
            break
        else:
            print('Ви вибрали неіснуючий пункт меню.\n')
        if break_work():
            break
    print("""
    =====================
    =       Кінець      =
    =====================""")
