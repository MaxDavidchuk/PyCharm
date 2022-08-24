from abc import ABC, abstractmethod
from houses_models.abstact_house import AbstractHouse


class AbstractBuilder(ABC):
    @staticmethod
    @abstractmethod
    def build_foundation() -> str:
        pass

    @staticmethod
    @abstractmethod
    def build_floor() -> str:
        pass

    @staticmethod
    @abstractmethod
    def build_walls() -> str:
        pass

    @staticmethod
    @abstractmethod
    def build_doors() -> str:
        pass

    @staticmethod
    @abstractmethod
    def build_windows() -> str:
        pass

    @staticmethod
    @abstractmethod
    def build_roof() -> str:
        pass

    @staticmethod
    @abstractmethod
    def get_result() -> AbstractHouse:
        pass
