from lib.shape import Shape


class CalcManager(object):

    def __init__(self):
        self._shapes = []

    def add_shape(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def clear_shapes(self) -> None:
        self._shapes.clear()

    def calc_general_square(self) -> float:
        s = 0
        for shape in self._shapes:
            s += shape.calc_square()
        return s

    def display_report(self) -> None:
        if not self._shapes:
            print('\n> Колекція фігур - порожня')
        else:
            print(f'\n> Колекція містить {len(self._shapes)} фігур, а саме:')
            k = 1
            for shape in self._shapes:
                print(f'{k}. {shape}: {shape.calc_square()}')
                k += 1
            print(f'\n> Загальна площа складає: {self.calc_general_square()}')
