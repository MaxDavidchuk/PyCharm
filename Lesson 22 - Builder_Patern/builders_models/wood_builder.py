from builders_models.abstract_builder import AbstractBuilder
from houses_models.wood_house import WoodHouse
from houses_models.abstact_house import AbstractHouse


class WoodBuilder(AbstractBuilder):
    @staticmethod
    def build_foundation() -> str:
        return 'Бетонний фундамент'

    @staticmethod
    def build_floor() -> str:
        return 'Дерев\'яна підлога'

    @staticmethod
    def build_walls() -> str:
        return 'Дерев\'яні стіни'

    @staticmethod
    def build_doors() -> str:
        return 'Дерев\'яні двері'

    @staticmethod
    def build_windows() -> str:
        return 'Дерев\'яні вікна'

    @staticmethod
    def build_roof() -> str:
        return 'Металеві дах'

    @staticmethod
    def get_result() -> AbstractHouse:
        info = WoodBuilder.build_foundation() + '\n'
        info += WoodBuilder.build_floor() + '\n'
        info += WoodBuilder.build_walls() + '\n'
        info += WoodBuilder.build_doors() + '\n'
        info += WoodBuilder.build_windows() + '\n'
        info += WoodBuilder.build_roof() + '\n'
        return WoodHouse(info)
