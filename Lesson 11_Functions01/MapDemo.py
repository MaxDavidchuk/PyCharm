def main():
	"""
		Функція Map
		https://ua.onlinemschool.com/math/library/analytic_geometry/point_point_length/
	"""
	print('map() -> функція відображення (проєкціювання) певної дії на всі елементи певної колекції')

	print('\n_______ Prim 1 ________')
	numbers = [10, 20, 30, 40, 50]
	squares = list(map(lambda x: x ** 3, numbers))
	print(squares)

	print('\n_______ Prim 2 ________')
	data_str = ['100', '200', '300', '400', '500']
	data_num = list(map(int, data_str))
	print(data_num)

	print('\n_______ Prim 3 ________')
	geometry = input('> Введіть сторони трикутника (через пробіл): ').split()
	data_list = list(map(float, geometry))
	print(f'Переметр: p = {2*(data_list[0]+data_list[1])}; Площа: s = {data_list[0]*data_list[1]}')

	print('\n_______ Prim 4 ________')
	prices = [100, 120, 150, 230, 450]
	discount = float(input('> Введіть % скидки: '))
	prices_disc = list(map(lambda p: round(p*(1 - discount / 100), 2), prices))
	print(f'Старі ціни: {prices}')
	print(f'Оновлені ціни: {prices_disc}')

	print('\n_______ Prim 5 ________')
	list1 = [10, 20, 30]
	list2 = [40, 50, 60]
	list3 = list(map(lambda x, y: x + y, list1, list2))
	print(f'Список 1: {list1}')
	print(f'Список 2: {list2}')
	print(f'Новий список становить: {list3}')


if __name__ == '__main__':
	main()
