"""
	Розширений нарбір методів роботи із Множинами
"""


def main() -> None:
	user_list = [
		['Tom', '+11112255'],
		['Bob', '+22223366'],
		['Jim', '+33334477']
	]

	print(user_list)
	for item in user_list:
		print(item)

	users_dict = dict(user_list)
	print(users_dict)   # Перетворення списку у словник
	for key in users_dict:
		print(f'{key} => {users_dict[key]}')
	# 1
	name = input('> Введіть ім\'я: ')
	phone = input('> Введіть телефон: ')
	if name in users_dict:
		print(f'{name} -> {users_dict[name]}')
		users_dict[name] = phone
		print('Ok!')
		print(users_dict)
	else:
		print(f'{name} - не знайдена!')
	# 2
	phone1 = users_dict.get('Tom')
	phone2 = users_dict.get('Jim')
	phone3 = users_dict.get('Vasja', 'Unknown person')
	print(phone1)
	print(phone2)
	print(phone3)
	# 3
	rem1 = users_dict.pop('Bob')
	print(users_dict)
	print(rem1)
	rem2 = users_dict.pop('Vasja', 'Delete is imposible for unknown person')
	print(users_dict)
	print(rem2)
	# 4
	users_dict['Vasja'] = '+12345678'
	users_dict.update({
		'Iren': '+55555555',
		'Kate': '+77777777'
	})
	print(users_dict)
	# 5 перебір даний у словнику по Записах
	for key, value in users_dict.items():
		print(f'Person: {key} -> Phone {value}')
	for key in users_dict.keys():
		print(f'Person: {key}')
	for value in users_dict.values():
		print(f'Phone: {value}')


if __name__ == '__main__':
	main()
