"""
    2. Створіть програму для пошуку назв столиць держав світу за
назвами країн, розмістивши самі дані у окремому json-файлі.
"""

import json

def read_data(file_name: str) -> dict:
	with open(file_name, 'r', encoding='utf-8-sig') as file:
		return json.load(file)

def display_menu(x: list) -> None:
    print('Виберіть частину Європи:')
    k = 0
    for part in x:
        k += 1
        print(f'{k} - {part}')
    print('0 - Завершити роботу\n')

def get_choice() -> int:
	choice = int(input('> Виберіть потрібний вам варіант: '))
	return choice

def break_work() -> bool:
	result = input('> Продовжити (y/n)? - ')
	return result == 'n'

def search_data(x: dict, s: str) -> None:
    print(f'{s} має такі держави:')

    #word = input('> Введіть назву держави: ')
    #print(x)
    #for k in range(x):
    #    if x[k][0]:
    #    print('  Такого слова немає у словнику.')
    #else:
	#	print(f'  {word} => {x[word]}')

if __name__ == '__main__':
    d = read_data('base.json')
    part = ["Західна Європа", "Південна Європа", "Північна Європа", "Східна Європа"]
    while True:
        display_menu(part)
        case = get_choice()
        if case == 1:
            search_data(d[str(case)], part[case - 1])
        elif case == 2:
            pass
        elif case == 3:
            pass
        elif case == 4:
            pass
        elif case == 0:
            break
        else:
            print('Ви вибрали неіснуючий пункт меню.')
        if break_work():
            break
    print("""
    =====================
    =       Кінець      =
    =====================""")