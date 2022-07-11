from data_manager import *


if __name__ == '__main__':
	data = load_data('data.json')
	display_dep(data)
	dep_name = input('> Введіть назву підрозділу: ')
	display_employees(data, dep_name)
