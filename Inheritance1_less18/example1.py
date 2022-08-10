"""
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Успаткування - це таке відношення між двома класами, зя якого
    один клас може:
    - ВИКОРИСТОВУВАТИ (stereotype=USE) атрибути таметоди батьківського класу
    - РОЗШИРЮВАТИ (stereotype=EXTANDS) набір батьківських компонентів
        власними атрибутами та методами
    - ПЕРЕВИЗНАЧАТИ (stereotype=OVERRIDE) окремі батьківські методи
        із заміщенням батьківського коду на власний.
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


class Person(object):

    def __init__(self, name: str, age: float, phone: str):
        self._name = name
        self._age = age
        self._phone = phone

    def __str__(self) -> str:
        return f'{self._name} - {self._age} years; {self._phone}'


class Student(Person):

    def __init__(self, name: str, age: float, phone: str, rate: float):
        super().__init__(name, age, phone)
        self._rate = rate

    def __str__(self) -> str:
        return super().__str__() + f' / rate: {self._rate}'


class Teacher(Person):

    def __init__(self, name: str, age: float, phone: str, subj: str, salary: float):
        super().__init__(name, age, phone)
        self._subj = subj
        self._salary = salary

    def __str__(self) -> str:
        return super().__str__() + f' / subj: {self._subj}; salaru: {self._salary} EUR'


if __name__ == '__main__':
    print(f"\n{Person('Василь Пупкін', 21, '111-22-33')}")
    print(f"\n{Student('Інна Пашніна', 21, '222-33-44', 11.3)}")
    print(f"\n{Teacher('Barak Obama', 60, '222-22-22', 'C++', 2500)}")