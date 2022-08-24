''' http://www.uml3.ru/ '''
from general_models.director import Director
from builders_models.brick_builder import BrickBuilder
from builders_models.stone_builder import StoneBuilder
from builders_models.wood_builder import WoodBuilder


if __name__ == '__main__':
    director = Director()

    print('\nOrder-1')
    director.choose_builder(WoodBuilder())
    director.build()

    print('\nOrder-2')
    director.choose_builder(BrickBuilder())
    director.build()

    print('\nOrder-3')
    director.choose_builder(StoneBuilder())
    director.build()
