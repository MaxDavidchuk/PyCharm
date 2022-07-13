from json import load, dump


def load_data(file_name: str) -> dict:
	"""Завантаження даних"""
	with open(file_name, 'r', encoding='utf-8') as file:
		data = load(file)
	print('Дані успішно завантажені!\n')
	return data


def display_menu() -> None:
    print('\nВиберіть потрібну задачу:')
    print('\t1 - Перелік департаментів')
    print('\t2 - Список працівників у конкретному департаменті')
    print('\t3 - Пошук співробітника за назвою підрозділу та його ім\'ям')
    print('\t4 - Пошук співробітника лише за його ім\'ям')
    print('\t0 - Завершити роботу\n')


def get_choice() -> int:
	choice = int(input('> Виберіть потрібний вам варіант: '))
	return choice


def break_work() -> bool:
	result = input('> Продовжити (y/n)? - ')
	return result == 'n'


def save_data(data: dict, file_name: str) -> None:
	"""Збереження даних"""
	with open(file_name, "w", encoding='utf-8') as file:
		dump(data, file)
	print('Дані успішно збережені!\n')


def display_dep(data: dict) -> None:
	print('----------------------')
	print(f'\t{data.get("company")}')
	print('----------------------')
	k = 1
	for dep in data.get('departments'):
		print(f'\t{k}. {dep.get("dep_name")}')
		k += 1
	print('----------------------\n')


def display_employees(data: dict, dep_name: str) -> None:
	""" Вивести прізвища у вибраному Департаменті """
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
		print(f'Підрозділ {dep_name} - не знайдений')
		print('----------------------')


# HomeTask-1
def display_emp_info(data: dict, dep_name: str, emp_name: str) -> None:
	""" Вивести інформацію про даного співробітника даного підрозділу """
	print('\n----------------------')
	print(f'\tПошук співробітника <{emp_name}> у підрозділі <{dep_name}>')
	print('----------------------')
	success1 = False
	success2 = False
	for dep in data.get('departments'):
		if dep.get('dep_name') == dep_name:
			success1 = True
			for emp in dep.get('employees'):
				temp_emp = emp.get('emp_name').split()
				if temp_emp[1] == emp_name:
					success2 = True
					break
	if success1 and success2:
		print(f'Співробітник <{emp_name}> дійсно працює у <{dep_name}>')
		print('----------------------\n')
	else:
		print(f'{"Співробітника " + emp_name if not success2 else dep_name} - не знайдено!')
		print('----------------------\n')


# HomeTask-2
def find_employee(data: dict, emp_name: str) -> None:
	""" Знайти співробітника із завданим ім'ям """
	k = 1
	print('\n----------------------')
	print(f'\tПошук співробітника <{emp_name}>')
	print('----------------------')
	success = False
	for dep in data.get('departments'):
		dep_name = dep.get('dep_name')
		for emp in dep.get('employees'):
			e_name = emp.get('emp_name').split()
			if e_name[1] == emp_name:
				print(f'{k}. -> {emp.get("emp_name")}\t-> {emp.get("emp_pos")}\t-> {dep_name}')
				k += 1
				success = True
	if not success:
		print(f'Співробітник <{emp_name}> - не знайдений!')
		print('----------------------')