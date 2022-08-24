class Menu(object):

    @staticmethod
    def display_menu() -> None:
        print('\t====================================')
        print('\t   1 - Переглянути види доставок')
        print('\t   2 - Зформувати замовлення')
        print('\t   3 - Переглянути замовлення')
        print('\t   4 - Очистити замовлення')
        print('\t   0 - Вихід')
        print('\t====================================')

    @staticmethod
    def choice() -> int:
        return int(input('> Виберіть потрібну операцію: '))

    @staticmethod
    def allow_continue() -> bool:
        return input('> Продовжити (y/n)?: ') == 'y'
