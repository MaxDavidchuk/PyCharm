#-------------------------------------------------------------------------------
# Name:         data_types
# Purpose:      Демонстрація типів даних у Python
# Author:       Maxim Davidchuk
# Created:     13.06.2022
# Copyright:   (c) dp_ma 2022
#-------------------------------------------------------------------------------

"""
    Змінна - це посилання на певний об'єкт у пам'яті
    ------------------------------------------------
    Типи об'єктів:
        1. Базові типи
        1.1. Integer
        1.2. Floating
        1.3. String
        1.4. Boolean
"""

def main():
    a = 48
    b = 12.46
    c = 'Ha-ha'
    d = True

    print('Hello world!', 123, 3.14, 26+9)

    print('a = ', a, 'type:', type(a))
    print('b = ', b, 'type:', type(b))
    print('c = ', c, 'type:', type(c))
    print('d = ', d, 'type:', type(d))

    old = input('How old r u?: ')

    if int(old) > 25 and d:
        print('Oldmen')

if __name__ == '__main__':
    main()
    print('\nOk')
