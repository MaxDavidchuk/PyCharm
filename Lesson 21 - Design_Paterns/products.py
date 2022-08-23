from abc import ABC, abstractmethod


class Transport(ABC):
    def __int__(self, kind: str, model: str, weight: float):
        self._kind = kind
        self._model = model
        self._weight = weight

    def __str__(self) -> str:
        return f'{self._kind} - {self._model} / {self._weight} ton'

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def __init__(self, kind: str, model: str, weight: float, height: float):
        super().__int__(kind, model, weight)
        self._height = height

    def __str__(self) -> str:
        return super().__str__() + f'; height = {self._height} m'

    def deliver(self):
        print('Перевезення по дорогах у межах України та Європи')


class Ship(Transport):
    def __init__(self, kind: str, model: str, weight: float, draft: float):
        super().__int__(kind, model, weight)
        self._draft = draft

    def __str__(self) -> str:
        return super().__str__() + f'; draft = {self._draft} m'

    def deliver(self):
        print('Перевезення по річкам та морям України та Європи')


class AirPlane(Transport):
    def __init__(self, kind: str, model: str, weight: float, distance: float):
        super().__int__(kind, model, weight)
        self._distance = distance

    def __str__(self) -> str:
        return super().__str__() + f'; distance = {self._distance} km'

    def deliver(self):
        print('Вантажні авіа-перевезення по Україні та Європі')
