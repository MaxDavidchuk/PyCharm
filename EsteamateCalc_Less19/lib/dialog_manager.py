from lib.calc_manager import CalcManager
from lib.circle import Circle
from lib.rectangle import Rectangle
from lib.triangle import Triangle


class DialogManager(object):

    def __init__(self):
        self._calc = CalcManager()

    def input_shapes_pararms(self) -> None:
        n = int(input('\n> Введіть загальну кількість фігур: '))
        for i in range(n):
            case = int(input('Виберіть фігуру (1 - circle, 2 - rectangle, 3 - triangle): '))
            if case == 1:
                circle = Circle(float(input('  радіус = ')))
                self._calc.add_shape(circle)
            elif case == 2:
                rectangle = Rectangle(float(input('  ширина: ')), float(input('  вистоа: ')))
                self._calc.add_shape(rectangle)
            elif case == 3:
                triangle = Triangle(float(input('  a = ')), float(input('  b = ')), float(input('  c = ')))
                self._calc.add_shape(triangle)
            else:
                print('  Ви ввели неіснуючий варіант')

    def call_display_report(self) -> None:
        case = int(input('\n> Вивести короткий звіт (1) чи розгорнутий звіт (2)?: '))
        if case == 1:
            print(f'  Загальна площа: {self._calc.calc_general_square()}')
        elif case == 2:
            self._calc.display_report()

    def confirm_clear(self) -> None:
        conf = input('  Ви підтверджуєте намір видалити дані (y/n)? - ')
        if conf == 'y':
            self._calc.clear_shapes()
            print('  Дані видалені успішно')
        else:
            print('  Видалення даних відмінено!')
