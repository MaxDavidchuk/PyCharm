class Menu(object):

    @staticmethod
    def display_menu() -> None:
        print('\t==========================')
        print('\t   1 - Введення даних')
        print('\t   2 - Виведення звіту')
        print('\t   3 - Видалення даних')
        print('\t   0 - Вихід')
        print('\t==========================')

    @staticmethod
    def choice() -> int:
        choice = int(input('> Виберіть потрібну операцію: '))
        return choice

    @staticmethod
    def allow_continue() -> bool:
        allow = input('\n> Продовжити (y/n)?: ')
        return allow == 'y'
