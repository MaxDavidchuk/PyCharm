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
            find_employee(data, emp_name)
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
