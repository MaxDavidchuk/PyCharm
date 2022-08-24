from creators import *
from lib.calc_manager import CalcManager


class DialogManager(object):

    def __init__(self):
        self._calc = CalcManager()

    @property
    def calc(self) -> CalcManager:
        return self._calc

    def input_vehicle(self) -> None:
        n = int(input('> Введіть загальну кількість перевезень: '))
        print('  1 - Truck, 2 - Ship, 3 - Air plane, 4 - Bicycle, 5 - Railway')
        for i in range(n):
            case = int(input('> Введіть спосіб доставки: '))
            if case == 1:
                self._calc.add_vehicle(RoadLogisticManager('Київ', 'Львів', 2, 'ТОВ "ПромІнвест"'))
            elif case == 2:
                self._calc.add_vehicle(SeeLogisticManager('Херсон', 'Київ', 4, 'ТОВ "Наші кавуни"'))
            elif case == 3:
                self._calc.add_vehicle(AirLogisticManager('Львів', 'Харків', 1, 'ТОВ "Світоч"'))
            elif case == 4:
                self._calc.add_vehicle(BicycleLogisticManager('вул. Щевченко, 15', 'вул. Героїв, 12/1', 30, 'Світлана', 'хвилин'))
            elif case == 5:
                self._calc.add_vehicle(RailwayLogisticManager('Чернівці', 'Суми', 4, 'ПрАТ "Чернівці-Ліс'))
            else:
                print('  Ви ввели неіснуючий варіант')

    def confirm_clear(self) -> None:
        conf = input('  Ви підтверджуєте намір видалити дані (y/n)? - ')
        if conf == 'y':
            self._calc.clear_vehicle()
            print('  Дані видалені успішно')
        else:
            print('  Видалення даних відмінено!')
