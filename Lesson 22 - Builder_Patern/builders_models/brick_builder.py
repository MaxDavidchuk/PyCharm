from builders_models.abstract_builder import AbstractBuilder
from houses_models.brick_house import BrickHouse
from houses_models.abstact_house import AbstractHouse


class BrickBuilder(AbstractBuilder):
    @staticmethod
    def build_foundation() -> str:
        return 'Залізо-бетонний фундамент'

    @staticmethod
    def build_floor() -> str:
        return 'Бетонна підлога'

    @staticmethod
    def build_walls() -> str:
        return 'Цегляні стіни'

    @staticmethod
    def build_doors() -> str:
        return 'Залізні двері'

    @staticmethod
    def build_windows() -> str:
        return 'Пластинові вікна'

    @staticmethod
    def build_roof() -> str:
        return 'Жестяний дах'

    @staticmethod
    def get_result() -> AbstractHouse:
        info = BrickBuilder.build_foundation() + '\n'
        info += BrickBuilder.build_floor() + '\n'
        info += BrickBuilder.build_walls() + '\n'
        info += BrickBuilder.build_doors() + '\n'
        info += BrickBuilder.build_windows() + '\n'
        info += BrickBuilder.build_roof() + '\n'
        return BrickHouse(info)
