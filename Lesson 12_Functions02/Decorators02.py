import time
import functools


def suma(*args) -> float:
	""" Функція із довільним числом аргументів """
	s = 0
	for x in args:
		s += x
	return s


def action(*args, operator='+'):
	""" Функція із необов'язковим параметром """
	if operator == '+':
		return functools.reduce(lambda x, y: x + y, args)
	elif operator == '-':
		return functools.reduce(lambda x, y: x - y, args)


def universal(*args, **kwargs):
	""" Універсальна функція із довільним числом будь-якмх аргументів"""
	print(args)
	print(kwargs)


def time_monitor(any_func):
	""" Декоратор у ролі таймера заміру часу виконання будь-якої функції"""
	def wrapper(*args, **kwargs):
		start = time.time()
		any_func(*args, **kwargs)
		finish = time.time()
		result = round((finish - start), 6)
		print(f'Час виконання: {result} мс')
	return wrapper

@time_monitor
def test(duration: float):
	""" Тестова функція для створення заданої затримки у часі"""
	time.sleep(duration)
	print(f'duration: {duration}')


if __name__ == '__main__':
	# 1
	print(f'Сума = {suma(10, 20, 30, 40, 50)}')
	# operator - ключовий аргумент # /**kwargs /
	print(f' => {action(10, 20, 30, 40, 50, operator="-")}')
	universal(1, 2, 3, 4, 5, key1=10, key2=20, key3=30)

	# 2
	test(2.345)
