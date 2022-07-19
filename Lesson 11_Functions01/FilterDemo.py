from random import randint


def main():
	"""
		Функція Filter
		https://ua.onlinemschool.com/math/library/analytic_geometry/point_point_length/
	"""
	print('filter() -> функція виборки (відбору) частини елементів колекції за певним критерієм (умовою)')

	print('\n_______ Prim 1 ________')
	data = [randint(-50, 50) for k in range(25)]    # Генератор списку
	pos = list(filter(lambda x: x > 0, data))
	neg = list(filter(lambda x: x < 0, data))

	print(f'Початковий список: {data}')
	print(f'Позитивний список: {pos}')
	print(f'Негативний список: {neg}')


if __name__ == '__main__':
	main()
