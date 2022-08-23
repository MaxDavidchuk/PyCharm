from lib.menu import Menu
from lib.dialog_manager import DialogManager


if __name__ == '__main__':
    print('\n\t+=========================+')
    print('\t| Кошторисний калькулятор |')
    print('\t+=========================+\n')

    manager = DialogManager()
    while True:
        Menu.display_menu()
        k = Menu.choice()
        if k == 1:
            manager.input_shapes()
        elif k == 2:
            manager.display_report()
        elif k == 3:
            manager.confirm_clear()
        elif k == 0:
            break
        else:
            print('  Ви вказали неіснуючий пункт меню')
        if not Menu.allow_continue():
            break
    print('\n  Програму завершено')
