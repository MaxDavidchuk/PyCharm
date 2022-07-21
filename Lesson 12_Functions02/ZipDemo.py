"""
	Агрегуючі функції вищих порядків
	Знайомство з декораторами
	Рекурсивні функції та алгоритми
"""


def zip_example_for_3_lists(list1: list, list2: list, list3: list) -> list:
	return list(zip(list1, list2, list3))


def main():
	a = [10, 20, 30]
	b = [40, 50, 60]
	c = [70, 80, 90]

	print(f'=> {zip_example_for_3_lists(a, b, c)}')


if __name__ == '__main__':
	main()
