from data_manager import *


if __name__ == '__main__':
	data = load_data('data.json')
	# dep_name = input('> Введіть назву підрозділу: ')
	# display_employees(data, dep_name)

	display_dep(data)
	# Створення підрозділу
	choice = input('> Бажаєте додати новий підрозділ? (y/n) - ')
	if choice == 'y':
		dep_name = input('> Введіть назву нового підрозділу: ')
		create_new_dep(data, dep_name)
	# Додавання співробітника
	choice = input('> Бажаєте додати нового співробітника? (y/n) - ')
	if choice == 'y':
		dep_name = input('> Введіть назву підрозділу: ')
		emp_name = input('> Введіть повністю ПІБ: ')
		emp_pos = input('> Введіть бажану посаду: ')
		emp_age = int(input('> Введіть вік: '))
		emp_salary = float(input('> Введіть бажану ЗП: '))
		create_new_emp(data, dep_name, emp_name, emp_pos, emp_age, emp_salary)
	# Видалення співробітника
	choice = input('> Бажаєте видалити співробітника? (y/n) - ')
	if choice == 'y':
		dep_name = input('> Введіть назву підрозділу: ')
		emp_name = input('> Введіть повністю ПІБ: ')
		remove_emp(data, dep_name, emp_name)

