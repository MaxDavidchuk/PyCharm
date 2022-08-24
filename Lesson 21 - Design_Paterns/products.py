from abc import ABC, abstractmethod


class Transport(ABC):
    n = 10

    def __int__(self, model: str, weight: float, kind: str = ''):
        self._kind = kind
        self._model = model
        self._weight = weight

    def __str__(self) -> str:
        return f'{self._kind:10} -> модель: {self._model:15} max вага: {str(self._weight) + " тон":12}'

    @staticmethod
    @abstractmethod
    def info():
        pass


class Truck(Transport):
    def __init__(self, model: str, weight: float, height: float, kind: str = 'Вантажівка'):
        super().__int__(model, weight, kind)
        self._height = height

    def __str__(self) -> str:
        return super().__str__() + f'{"висота:":15} {self._height} м.'

    @staticmethod
    def info():
        print(f'{"Truck":10} -> Перевезення по дорогах України та Європи')


class Ship(Transport):
    def __init__(self, model: str, weight: float, draft: float, kind: str = 'Корабель'):
        super().__int__(model, weight, kind)
        self._draft = draft

    def __str__(self) -> str:
        return super().__str__() + f'{"max draft:":15} {self._draft} m'

    @staticmethod
    def info():
        print(f'{"Ship":10} -> Перевезення по річкам та морям України та Європи')


class AirPlane(Transport):
    def __init__(self, model: str, weight: float, distance: float, kind: str = 'Літак'):
        super().__int__(model, weight, kind)
        self._distance = distance

    def __str__(self) -> str:
        return super().__str__() + f'{"дальність:":15} {self._distance} км'

    @staticmethod
    def info():
        print(f'{"Air plane":10} -> Повітряні перевезення по Україні та Європі')


class Bicycle(Transport):
    def __init__(self, model: str, weight: float, speed: float, kind: str = 'Велосипед'):
        super().__int__(model, weight, kind)
        self._speed = speed

    def __str__(self) -> str:
        return super().__str__() + f'{"швидкість:":15} {self._speed} км/год.'

    @staticmethod
    def info():
        print(f'{"Bicycle":10} -> Доставка продуктів харчування в обласних центрах України')


class Railway(Transport):
    def __init__(self, model: str, weight: float, carriage: int, kind: str = 'Залізниця'):
        super().__int__(model, weight, kind)
        self._carriage = carriage

    def __str__(self) -> str:
        return super().__str__() + f'{"кіл-ть вагонів:":15} {self._carriage} шт.'

    @staticmethod
    def info():
        print(f'{"Railway":10} -> Вантажні залізничні перевезення по Україні та Європі')