"""
    Множине успадкування - це прийом пректування класів, при якому
    один клас (клас-нащадок) успадковує одразу деккілька інших класів.
"""
from lib.example1 import *
from lib.example2 import *
from lib.example3 import *


class MyStudent(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __int__(self):
        return f'{self.__name} - {self.__age}'


if __name__ == '__main__':
    # 1
    emp = Employee()
    emp.work()
    # 2
    stud = Student()
    stud.study()
    # 3
    print()
    work_stud = WorkingStudent()
    work_stud.work()
    work_stud.study()
    # 4
    print()
    work_stud.say()
    # 5
    print('\n> MRO: Methods Resolution Order')
    print(WorkingStudent.mro())
    k = 1
    for cls in WorkingStudent.mro():
        print(f'{k} -> {cls.__name__}')
        k += 1
    # ===============================================
    print()
    car = Car()
    boat = Boat()
    phone = Smartphone()
    radio = Radio()

    car.play_music('Пісня для авто')
    boat.play_music('Пісня для моряків')
    phone.play_music('Пісня для телефону')
    radio.play_music('Пісня для радіщ')
    # ===============================================

    print()
    ufm = UniversalFileManager()
    """
    ufm.write_text_to_file('message.txt', 'Vasja Pupkin - forever young!')
    ufm.write_dict_to_file('data.json', {
        "Ukraine": "Kyiv",
        'Turkey': 'Ankara',
        'Paris': 'France'
    })
    ufm.write_object_to_file('student.dat', MyStudent('Vasya', 21))
    # ===============================================
    """
    print()
    ufm.read_text_from_file('message.txt')
    ufm.read_dict_from_file('data.json')
    ufm.read_object_from_file('student.dat')
