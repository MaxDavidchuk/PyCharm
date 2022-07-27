class Student(object):
    """ Клас Студенти """
    def __init__(self, name: str, age: int, rate: float):
        """ Конструктор об'єктів класу - визначає набір атрибутів кожного об'єкту"""
        self.__name = name
        self.__age = age
        self.__rate = rate

    def __str__(self):
        """ Метод строкового представлення інформації про об'єкт """
        info = f'\n> Ім\'я студента: {self.__name}'
        info += f'\n  Вік студента: {self.__age} років'
        info += f'\n  Рейтинг студента: {self.__rate}'
        return info

    def method1(self):
        print(f'Студент {self.__name} витирає дошку')
