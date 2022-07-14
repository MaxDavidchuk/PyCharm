from data_manager import *


if __name__ == '__main__':
    data = load_data('data.json')
    while True:
        display_menu()
        case = get_choice()
        if case == 1:
            display_dep(data)
        elif case == 2:
            dep_name = input('> Введіть назву підрозділу: ')
            display_employees(data, dep_name)
        elif case == 3:
            display_dep(data)
            dep_name = input('> Введіть назву підрозділу: ')
            emp_name = input('> Введіть ім\'я співробітника: ')
            display_emp_info(data, dep_name, emp_name)
        elif case == 4:
            emp_name = input('> Введіть ім\'я співробітника: ')
            if find_emp(data, emp_name, True) == False:
                print(f'Співробітник <{emp_name}> - не знайдений!')
                print('----------------------')
        elif case == 5:
            choice = input('> Бажаєте додати новий підрозділ? (y/n) - ')
            if choice == 'y':
                dep_name = input('> Введіть назву нового підрозділу: ')
                create_new_dep(data, dep_name)
        elif case == 6:
            choice = input('> Бажаєте додати нового співробітника? (y/n) - ')
            if choice == 'y':
                dep_name = input('> Введіть назву підрозділу: ')
                emp_name = input('> Введіть повністю ПІБ: ')
                emp_pos = input('> Введіть бажану посаду: ')
                emp_age = int(input('> Введіть вік: '))
                emp_salary = float(input('> Введіть бажану ЗП: '))
                create_new_emp(data, dep_name, emp_name, emp_pos, emp_age, emp_salary)
        elif case == 7:
            choice = input('> Бажаєте видалити співробітника? (y/n) - ')
            if choice == 'y':
                dep_name = input('> Введіть назву підрозділу: ')
                emp_name = input('> Введіть повністю ПІБ: ')
                remove_emp(data, dep_name, emp_name)
        elif case == 8:
            choice = input('> Бажаєте перевести співробітника в інший відділ? (y/n) - ')
            if choice == 'y':
                transfer_emp(data)
        elif case == 9:
            choice = input('> Бажаєте змінити зарплату співробітнику? (y/n) - ')
            if choice == 'y':
                dep_name = input('> Введіть назву підрозділу: ')
                emp_name = input('> Введіть ПІБ співробітника: ')
                emp_salary = float(input('> Введіть бажану ЗП: '))
                salary_change(data, dep_name, emp_name, emp_salary)
        elif case == 0:
            break
        else:
            print('Ви вибрали неіснуючий пункт меню.')
        if break_work():
            break
    print("""
    =====================
    =       Кінець      =
    =====================""")
