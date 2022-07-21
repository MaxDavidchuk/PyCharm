"""
	Агрегуючі функції вищих порядків
	Знайомство з декораторами
	Рекурсивні функції та алгоритми
"""
import functools
import random


def main():
	# 1 - Підрахувати сууму елементів заданого списку:
	numb = [10, 20, 30, 40, 50, 60, 70]
	s = functools.reduce(lambda x, y: x + y, numb)
	print(numb)
	print(s)

	# 2 - Знайти мінімальне число у заданому списку
	numb = [random.randint(10, 99) for i in range(15)]
	m = functools.reduce(lambda x, y: x if x < y else y, numb)
	print(numb)
	print(f'Min = {m}')

	# 3 - Знайти максимальне число у заданому списку
	m = functools.reduce(lambda x, y: x if x > y else y, numb)
	print(f'Max = {m}')


if __name__ == '__main__':
	main()
