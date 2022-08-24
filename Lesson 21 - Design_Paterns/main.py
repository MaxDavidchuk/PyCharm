from client import *
from creators import *
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

"""    
    print('\nПрийняті замовлення:')
    print('-'*170)
    print(f'{" №":3}| {"Замовник":20}| {"з пункту":20}| {"до пункту":20}| {"термін":10}| {"тип транспорту"}')
    print('-'*170)
    clients = [Client(RoadLogisticManager('Київ', 'Львів', 2, 'ТОВ "ПромІнвест"')),
               Client(SeeLogisticManager('Херсон', 'Київ', 4, 'ТОВ "Наші кавуни"')),
               Client(AirLogisticManager('Львів', 'Харків', 1, 'ТОВ "Світоч"')),
               Client(BicycleLogisticManager('вул. Щевченко, 15', 'вул. Героїв, 12/1', 30, 'Світлана', 'хвилин')),
               Client(RailwayLogisticManager('Чернівці', 'Суми', 4, 'ПрАТ "Чернівці-Ліс'))]
    k = 0
    for client in clients:
        k += 1
        print(f'{k:2}.', end='')
        client.demo()
    print('-'*170)
"""