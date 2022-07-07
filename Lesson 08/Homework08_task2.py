"""
    2. Створіть програму для пошуку назв столиць держав світу за
назвами країн, розмістивши самі дані у окремому json-файлі.
"""

import json

def read_data(file_name: str) -> dict:
	with open(file_name, 'r', encoding='utf-8') as file:
		return json.load(file)


def search_data(x: dict) -> None:
	word = input('> Введіть слово для перекладу: ')
	if word not in x:
		print('  Такого слова немає у словнику.')
	else:
		print(f'  {word} => {x[word]}')

def print_set(s: set) -> None:
    k = 0
    for fio in s:
        k += 1
        print(f'{k}. {fio}', end=' ')
    print()

if __name__ == '__main__':
    d = read_data('base.json')

    print("""
    =====================
    =       Кінець      =
    =====================""")