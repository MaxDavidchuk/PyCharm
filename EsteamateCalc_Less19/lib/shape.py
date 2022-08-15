from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def calc_square(self) -> float:
        pass

    def __str__(self) -> str:
        return f'Фігура: {self._name}'
