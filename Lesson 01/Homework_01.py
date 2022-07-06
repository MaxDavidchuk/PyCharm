#-------------------------------------------------------------------------------
# Name:         My first Homework
# Purpose:      Виконання домашнього завдання
# Author:       Maxim Davidchuk
# Created:      14.06.2022
# Copyright:   (c) dp_maxim 2022
#-------------------------------------------------------------------------------
"""
    Ваше завдання - розробити консольну Python-програму,
    яка реалізує сценарій діалогу із користувачем за таким сюжетом:
    > Як Вас звуть? - ...
    > В якому місті Ви живете? - ...
    > В якій школі Ви навчались? - ...
"""
def main():
    promt = ' - '
    print('Привіт! \nЯк тебе звати?', end=':')
    str_name = input(promt)
    print(f'А яке твоє прізвище, {str_name}?', end=':')
    str_surname = input(promt)
    print('{} {}, а в якому місті ти мешкаєш?'.format(str_name, str_surname), end=':')
    str_city = input(promt)
    print(f'Хотів би ти, {str_name} {str_surname}, з міста {str_city} навчатися у школі ItStep? (Так/Ні)', end=':')
    if input(promt) == 'Так': print('Ласкаво запрошую на навчання!!!')
    else: print('Дякую за відповіді! \nЧекаю на тебе у любий час.')

if __name__ == '__main__':
    main()