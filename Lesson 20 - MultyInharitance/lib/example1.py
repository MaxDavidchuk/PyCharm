class Person(object):

    def __init__(self, class_name: str):
        self._class_name = class_name

    def __str__(self) -> str:
        return self._class_name


class Employee(Person):

    def __init__(self):
        super().__init__('Employee')

    def work(self):
        print(f'Object [{super().__str__()}] works as Employee ...')

    @staticmethod
    def say():
        print('I like to work!')


class Student(Person):

    def __init__(self):
        super().__init__('Student')

    def study(self):
        print(f'Object [{super().__str__()}] studies as Student ...')

    @staticmethod
    def say():
        print('I like to study!')


class WorkingStudent(Employee, Student):

    def __init__(self):
        Person.__init__(self, 'WorkingStudent')

