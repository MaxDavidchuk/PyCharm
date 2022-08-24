from lib.menu import Menu
from lib.dialog_manager import DialogManager


if __name__ == '__main__':
    print('\n\t====================================')
    print('\t|       Транспортна логістика      |')
    manager = DialogManager()
    while True:
        Menu.display_menu()
        k = Menu.choice()
        if k == 1:
            manager.calc.show_info()
        elif k == 2:
            manager.input_vehicle()
        elif k == 3:
            manager.calc.display_report()
        elif k == 4:
            manager.confirm_clear()
        elif k == 0:
            break
        else:
            print('  Ви вказали неіснуючий пункт меню')
        if not Menu.allow_continue():
            break
    print('\n  Програму завершено')
