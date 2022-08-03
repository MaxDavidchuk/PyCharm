from lib import *


if __name__ == '__main__':

    manager = DataManager()
    manager.load_data()
    menu = Menu()

    while True:
        menu.display()
        k = menu.make_choice()
        if k == 1:
            manager.catalog.display()
        elif k == 2:
            manager.catalog.add_product(menu.make_product())
        elif k == 3:
            manager.catalog.del_product(menu.get_del_number())
        elif k == 4:
            pass
        elif k == 5:
            pass
        elif k == 6:
            break
        else:
            print('> Ви ввели неіснуючий номер!')

        if not menu.allow_continue():
            break

    manager.save_data()
    print('Програму завершено!')
