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
		dump(data, file, indent=4, ensure_ascii=False)
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


def create_new_dep(data: dict, dep_name: str) -> None:
	""" Створення нового департаменту """
	new_dep = {
		'dep_name': dep_name,
		'employees': []
	}
	data.get('departments').append(new_dep)
	save_data(data, 'data.json')


def find_dep(data: dict, dep_name: str) -> dict:
	""" Пошук чи існує підрозділ """
	for dep in data.get('departments'):
		if dep.get('dep_name') == dep_name:
			return dep
	return {}


def create_new_emp(data: dict, dep_name: str, emp_name: str, emp_pos: str, emp_age: int, emp_salary: float) -> None:
	""" Створення нового співпрбітника """
	new_emp = {
		"emp_name": emp_name,
		"emp_pos" : emp_pos,
		"emp_age" : emp_age,
		"emp_salary": emp_salary
	}
	dep = find_dep(data, dep_name)
	if len(dep.items()) > 0:
		dep.get('employees').append(new_emp)
	save_data(data, 'data.json')


def remove_emp(data: dict, dep_name: str, emp_name: str) -> None:
	""" Видалити співробітника """
	dep = find_dep(data, dep_name)
	if len(dep.get('employees')) > 0:   # Чи існує підрозділ
		index = -1
		for emp in dep.get('employees'):    # Пошук індекса
			index += 1
			if emp.get('emp_name') == emp_name:
				break
		if index > -1:
			dep.get('employees').pop(index)
			save_data(data, 'data.json')
