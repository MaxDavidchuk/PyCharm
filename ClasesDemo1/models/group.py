# Агрегування - це включення одним класом колекції
# об'єктів іншого класу

from models.student import Student


class Group(object):

    def __init__(self, name: str):
        self.__name = name
        self.__students = []

    def __str__(self):
        return f'\n> Група: {self.__name} / студентів {len(self.__students)}'

    def add_student(self, student: Student) -> None:
        self.__students.append(student)

    def __find_student(self, name: str) -> int:
        index = -1
        result = -1
        for s in self.__students:
            index += 1
            if s.name == name:
                result = index
                break
        if result == -1:
            print(f'  Студент {name} - не знайдений')
        return result

    def del_student(self, name: str) -> None:
        index = self.__find_student(name)
        if index >= 0:
            self.__students.pop(index)
            print(f'\n> Студент {name} - успішно видалений (-a)')

    def rate_change(self, name: str, new_rate: float) ->None:
        index = self.__find_student(name)
        if index >= 0:
            self.__students[index].rate = new_rate
            print(f'\n> Рейтинг студента {name} - успішно змінений')

    def display_students(self) -> None:
        k = 0
        for s in self.__students:
            k += 1
            print(f'\n{k}. {s}')
