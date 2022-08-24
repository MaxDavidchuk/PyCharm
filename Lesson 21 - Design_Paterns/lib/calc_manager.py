from creators import LogisticManager
from products import *
from client import Client


class CalcManager(object):

    def __init__(self):
        self._way = []

    def add_vehicle(self, vehicle: LogisticManager) -> None:
        self._way.append(vehicle)

    def clear_vehicle(self) -> None:
        self._way.clear()

    def display_report(self) -> None:
        if not self._way:
            print('  Ви ще не зформували замовлення.')
        else:
            print(f'  Прийняті замовлення складаються із {len(self._way)} маршрутів, а саме:')
            print('-'*170)
            print(f'{" №":3}| {"Замовник":20}| {"з пункту":20}| {"до пункту":20}| {"термін":10}| {"тип транспорту"}')
            print('-'*170)
            k = 0
            for client in self._way:
                k += 1
                print(f'{k:2}.', end='')
                Client(client).demo()
            print('-'*170)

    @staticmethod
    def show_info() -> None:
        k = 0
        for t in [Truck, Ship, AirPlane, Bicycle, Railway]:
            k += 1
            print(f'  {k}. ', end='')
            t.info()
