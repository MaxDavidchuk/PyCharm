"""
	Домашнє завдання після Уроку 12
	Завдання 1.
	-----------------------------------------------------
	Створіть універсальний декоратор, який виводить список всіх
	позиційних та ключових аргументів функції, а також, точну дату
	її виклику на виконання
	------------------------------------------------------
"""
from datetime import datetime


def decorator(func):
	def inner(*args, **kwargs):
		print(f'\nДата та час запуску програми: {datetime.now().strftime("%d-%m-%Y, %H:%M:%S")}')
		func(*args, **kwargs)
		print('-'*60)
		print(f'            Назава функції: | {func.__name__}')
		print(f'Клас ПОЗИЦІЙНИХ агрументів: | {type(args)}')
		print(f'               Їх значення: | {args}')
		print(f'  Клас КЛЮЧОВИХ агрументів: | {type(kwargs)}')
		print(f'               Їх значення: | {kwargs}')
		print('-'*60)
	return inner


@decorator
def fn(*args, **kwargs):
	pass


if __name__ == '__main__':
	fn(1, 2, x=10, y=20)
