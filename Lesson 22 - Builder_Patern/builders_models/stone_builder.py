from builders_models.abstract_builder import AbstractBuilder
from houses_models.stone_house import StoneHouse
from houses_models.abstact_house import AbstractHouse


class StoneBuilder(AbstractBuilder):
    @staticmethod
    def build_foundation() -> str:
        return 'Кам\'яний фундамент'

    @staticmethod
    def build_floor() -> str:
        return 'Кам\'яна підлога'

    @staticmethod
    def build_walls() -> str:
        return 'Кам\'яні стіни'

    @staticmethod
    def build_doors() -> str:
        return 'Броньовані двері'

    @staticmethod
    def build_windows() -> str:
        return 'Бронбовані вікна'

    @staticmethod
    def build_roof() -> str:
        return 'Черепичний дах'

    @staticmethod
    def get_result() -> AbstractHouse:
        info = StoneBuilder.build_foundation() + '\n'
        info += StoneBuilder.build_floor() + '\n'
        info += StoneBuilder.build_walls() + '\n'
        info += StoneBuilder.build_doors() + '\n'
        info += StoneBuilder.build_windows() + '\n'
        info += StoneBuilder.build_roof() + '\n'
        return StoneHouse(info)
