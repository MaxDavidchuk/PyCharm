from json import load, dump


def load_data(file_name: str) -> dict:
    """Завантаження даних"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = load(file)
    print('Дані успішно завантажені!\n')
    return data


def display_menu() -> None:
    print('\nВиберіть потрібну задачу:')
    print('\t1 -> Перелік відділів')
    print('\t2 -> Список працівників у конкретному відділі')
    print('\t3 -> Пошук співробітника за назвою відділу та його ім\'ям')
    print('\t4 -> Пошук співробітника лише за його ім\'ям')
    print('\t5 -> Створити новий відділ')
    print('\t6 -> Створити (додати) нового співробітника')
    print('\t7 -> Видалити існуючого співробітника')
    print('\t8 -> Переведення співробітника між відділами')
    print('\t9 -> Збільшення зарплати співробітника')
    print('\t0 -> Завершити роботу\n')


def get_choice() -> int:
    choice = int(input('> Виберіть потрібний вам варіант: '))
    return choice


def break_work() -> bool:
    result = input('> Продовжити (y/n)? - ')
    return result == 'n'


def save_data(data: dict) -> None:
    """Збереження даних"""
    with open('data.json', "w", encoding='utf-8') as file:
        dump(data, file, indent=4, ensure_ascii=False)
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


# 2022-07-11 HomeTask-1
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


# 2022-07-11 HomeTask-2
def find_emp(data: dict, emp_name: str, print_yn: bool) -> bool:
    """ Знайти співробітника із завданим ім'ям """
    success = False
    k = 1
    for dep in data.get('departments'):
        dep_name = dep.get('dep_name')
        for emp in dep.get('employees'):
            if emp.get('emp_name').find(emp_name) > -1:
                success = True
                if print_yn:
                    print(f'{k}. -> {emp.get("emp_name")}\t-> {emp.get("emp_pos")}\t-> {dep_name}')
                k += 1
    return False if not success else True


def create_new_dep(data: dict, dep_name: str) -> None:
    """ Створення нового департаменту """
    new_dep = {'dep_name': dep_name, 'employees': []}
    data.get('departments').append(new_dep)
    save_data(data)


def find_dep(data: dict, dep_name: str) -> dict:
    """ Пошук чи існує підрозділ """
    for dep in data.get('departments'):
        if dep.get('dep_name') == dep_name:
            return dep
    return {}


def create_new_emp(data: dict, dep_name: str, emp_name: str, emp_pos: str, emp_age: int, emp_salary: float) -> None:
    """ Створення нового співпрбітника """
    new_emp = {"emp_name": emp_name, "emp_pos": emp_pos, "emp_age": emp_age, "emp_salary": emp_salary}
    dep = find_dep(data, dep_name)
    if len(dep.items()) > 0:
        dep.get('employees').append(new_emp)
    save_data(data)


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
            save_data(data)


# 2022-07-13 HomeTask-1
def transfer_emp(data: dict) -> None:
    while True:
        emp_name = input('> Введіть ПІБ співробітника: ')
        if find_emp(data, emp_name, False):
            break
        else:
            print(f'Співробітник <{emp_name}> не знайдений.')
    while True:
        dep_name = input('> Введіть назву Cтарого підрозділу: ')
        dep_old = find_dep(data, dep_name)
        if len(dep_old.items()) > 0:
            break
        else:
            print(f'Підрозділ <{dep_name}> не знайдений.')
    while True:
        dep_name = input('> Введіть назву Нового підрозділу: ')
        dep_new = find_dep(data, dep_name)
        if len(dep_new.items()) > 0:
            break
        else:
            print(f'Підрозділ <{dep_name}> не знайдений.')
    for emp in dep_old.get('employees'):
        if emp.get('emp_name') == emp_name:
            remove_emp(data, dep_old.get('dep_name'), emp_name)
            dep_new.get('employees').append(emp)
            print(f'Співробітник <{emp_name}> переміщений у підрозділ <{dep_name}>')
            save_data(data)
            break


# 2022-07-13 HomeTask-2
def salary_change(data: dict, dep_name: str, emp_name: str, emp_salary: float) -> None:
    dep = find_dep(data, dep_name)
    if len(dep.items()) > 0:
        for emp in dep.get('employees'):
            if emp.get('emp_name') == emp_name:
                salary = float(emp.get('emp_salary'))
                if salary < emp_salary:
                    emp.update({"emp_salary": emp_salary})
                    print(f'Зарплату для співробітника {emp_name} збільшено до {emp_salary}.')
                    save_data(data)
                else:
                    print(f'Існуюча зарплата {salary} більша за запропоновану.')
                    print('Зарплату не змінено.')
