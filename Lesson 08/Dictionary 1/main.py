"""
	Словник іншомовних слів для перекладу із англійської на українську

"""

import json


def read_data(file_name: str) -> dict:
	with open(file_name, 'r', encoding='utf-8') as file:
		return json.load(file)


def break_work() -> bool:
	result = input('> Продовжити (y/n)? - ')
	return result == 'n'


def display_menu() -> None:
	print('1 - Пошук перекладу')
	print('2 - Додавання перекладу')
	print('3 - Видалення перекладу')
	print('4 - Зміна перекладу')
	print('5 - Виведення словника')
	print('6 - Завершення роботу\n')


def get_choice() -> int:
	choice = int(input('> Виберіть потрібний вам варіант: '))
	return choice


def print_dict(x: dict) -> None:
	k = 0
	for key in x:
		k += 1
		print(f'{k}. {key} => {x[key]}')
	print()


def search_translate(x: dict) -> None:
	word = input('> Введіть слово для перекладу: ')
	if word not in x:
		print('  Такого слова немає у словнику.')
	else:
		print(f'  {word} => {x[word]}')


if __name__ == '__main__':
	d = read_data('dictionary.json')
	while True:
		display_menu()
		case = get_choice()
		if case == 1:
			search_translate(d)
		elif case == 2:
			pass
		elif case == 3:
			pass
		elif case == 4:
			pass
		elif case == 5:
			print_dict(d)
		elif case == 6:
			break
		else:
			print('Ви вибрали неіснуючий пункт меню.')
		if break_work():
			break

	print('\nПрограму завершено!')
