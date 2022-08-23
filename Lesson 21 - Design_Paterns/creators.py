from abc import ABC, abstractmethod
from products import *


class LogisticManager(ABC):
    def __init__(self, point: str, dest: str, term: float, client: str):
        self._point = point
        self._dest = dest
        self._term = term
        self._client = client

    def delivery_order(self) -> None:
        print(f'\nПрийнято завмовлення від {self._client} на перевезення'
              f' із {self._point} до {self._dest}\nу термін - {self._term} транспортом {self.choice_transport()} ')

    @abstractmethod
    def choice_transport(self) -> Transport:
        pass


class RoadLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def choice_transport(self) -> Transport:
        # ...
        return Truck('Traler', 'GM', 25, 4.5)


class SeeLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def choice_transport(self) -> Transport:
        # ...
        return Ship('Balcker', 'Dnipro', 50000, 6.5)


class AirLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str):
        super().__init__(point, dest, term, client)

    def choice_transport(self) -> Transport:
        # ...
        return AirPlane('Boing', 'Mriya', 500000, 4500)
