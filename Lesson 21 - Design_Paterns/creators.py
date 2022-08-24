from products import *


class LogisticManager(ABC):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        self._point = point
        self._dest = dest
        self._term = term
        self._period = period
        self._client = client

    def delivery_order(self) -> None:
        print(f'| {self._client:20}| {self._point:20}| {self._dest:20}| {str(self._term) + " " + self._period:10}| '
              f'{self.choice_transport()}')

    @abstractmethod
    def choice_transport(self) -> Transport:
        pass


class RoadLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        super().__init__(point, dest, term, client, period)

    def choice_transport(self) -> Transport:
        return Truck('Volvo', 25, 4.5)


class SeeLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        super().__init__(point, dest, term, client, period)

    def choice_transport(self) -> Transport:
        return Ship('Ferry', 50000, 6.5)


class AirLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        super().__init__(point, dest, term, client, period)

    def choice_transport(self) -> Transport:
        return AirPlane('Boing', 500000, 4500)


class BicycleLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        super().__init__(point, dest, term, client, period)

    def choice_transport(self) -> Transport:
        return Bicycle('Механічний', 0.005, 30)


class RailwayLogisticManager(LogisticManager):
    def __init__(self, point: str, dest: str, term: float, client: str, period: str = 'дн.'):
        super().__init__(point, dest, term, client, period)

    def choice_transport(self) -> Transport:
        return Railway('Укрзалізниця', 100, 56)
