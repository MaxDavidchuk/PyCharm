from builders_models.abstract_builder import AbstractBuilder


class Director(object):

    def __init__(self):
        self._builder = None

    def choose_builder(self, builder: AbstractBuilder) -> None:
        self._builder = builder

    def build(self):
        if not self._builder:
            print('Не призначено будівельника')
        else:
            house = self._builder.get_result()
            house.display_info()
