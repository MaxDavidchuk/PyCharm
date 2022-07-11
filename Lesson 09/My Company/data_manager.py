from json import load, dump


def load_data(file_name: str) -> dict:
	"""Завантаження даний"""
	with open(file_name, 'r', encoding='utf-8') as file:
		data = load(file)
	print('Дані успішно завантажені!\n')
	return data


def save_data(data: dict, file_name: str) -> None:
	"""Збереження даний"""
	with open(file_name, "w", encoding='utf-8') as file:
		dump(data, file)
	print('Дані успішно збережені!\n')


def display_dep(data: dict) -> None:
	print('----------------------')
	print(f'\t{data.get("company")}')
	print('----------------------')
	k = 1
	for dep in data.get('departments'):
		print(f'{k}. {dep.get("dep_name")}')
		k += 1
	print('----------------------')


def display_employees(data: dict, dep_name: str) -> None:
	print('\n----------------------')
	print(f'\t{dep_name}')
	print('----------------------')
	success = False
	for dep in data.get('departments'):
		if dep.get('dep_name') == dep_name:
			success = True
			k = 1
			for emp in dep.get('employees'):
				print(f'{k}. {emp.get("emp_name")}')
				k += 1
			break
	if not success:
		print(f'Департаменту {dep_name} - не знайдений')
		print('----------------------')


# HomeTask-1
def display_emp_info(data: dict, dep_name: str, emp_name: str) -> None:
	""" вивести інформацію про даного співробітника даного підрозділу """
	pass


# HomeTask-2
def find_employee(data: dict, emp_name: str) -> None:
	""" Знайти співробітника із завданим ім'ям """
	pass
