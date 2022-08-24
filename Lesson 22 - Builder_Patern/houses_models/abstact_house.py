from abc import ABC


class AbstractHouse(ABC):

    def __init__(self, name: str, info: str):
        self._name = name
        self._info = info

    def display_info(self):
        print(f'> Будинок: {self._name}')
        print('---------------------------')
        print(self._info)
        print('---------------------------')
