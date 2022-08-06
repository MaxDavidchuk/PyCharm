from lib import *


if __name__ == '__main__':

    manager = DataManager()
    manager.load_data()
    menu = Menu()

    while True:
        menu.display()
        k = menu.make_choice()
        if k == 1:      # Вивести
            manager.catalog.display()
        elif k == 2:    # Додати
            manager.catalog.add_product(menu.make_product())
        elif k == 3:    # Видалити
            manager.catalog.del_product(menu.get_number())
        elif k == 4:    # Знайти
            manager.catalog.find_product(menu.get_product())
        elif k == 5:    # Змінити
            manager.catalog.change_price(menu.new_price())
        elif k == 6:    # Вихід
            break
        else:
            print('> Ви ввели неіснуючий номер!')
        if not menu.allow_continue():
            break
    manager.save_data()
    print(' Програму завершено!')
