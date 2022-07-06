"""
						Демонстрація множин
				=========================
	Множина (set) - це НЕвпорядкований набір унікальних об'єктів
	Множини використовуються із кількома наборами даних відповідно
	до математичної теорії множин
"""
from typing import Set


def main() -> None:
	users_list = ['Вася', 'Петро', 'Іван', 'Коля', 'Саша', 'Маша', 'Наташа', 'Петро', 'Коля', 'Саша']
	print(users_list)
	users_set = set(users_list)
	print(users_set)

	# print(user_set[0]) - множини не підтримує індексації

	print(len(users_set))

	users_set.add('Barak') # додавання елементів до множини
	users_set.add('Angela')
	print(users_set)

	# Delete set elements
	# name = input('> Введіть ім\'я для видалення: ')
	name = '1'
	if name not in users_set:
		print('Користувач із таким іменем не знайдено.')
	else:
		users_set.remove(name)
		print(f'Користувач із іменем <{name}> видалено.')

# Copy
	number = {100, 200, 300, 400, 500}
	print(number)
	num_copy = number.copy()
	print(num_copy)

	# Об'єднання
	num2 = {300, 400, 500, 600, 700}
	res1 = num2.union(number)
	print(res1)

	# Перетин множин
	res2 = number.intersection(num2)
	print(res2)

	# Різниця множин
	res3 = number.difference(num2)
	print(res3)
	res4 = num2.difference(number)
	print(res4)

	# Симетрична різниця
	res5 = number.symmetric_difference(num2)
	print(res5)


if __name__ == '__main__':
	main()
