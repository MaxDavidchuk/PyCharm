import pickle


class Contact(object):
    
    def __init__(self, name: str, number: str, email: str):
        self.__name = name
        self.__number = number
        self.__email = email

    def __str__(self):
        return f'{self.name:18}| {self.__number:16}| {self.__email:12}'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, new_number: int):
        self.__number = new_number


class Book(object):

    def __init__(self):
        self.__contacts = []

    def __str__(self):
        return f'\n   Телефона книжка має контактів: {len(self.__contacts)}'

    def add_contact(self, contact: Contact, yes: bool = False) -> None:
        self.__contacts.append(contact)
        if yes:
            print(f'> Контакт <{contact.name}> - успішно додано!')

    def __find_contact(self, name: str) -> int:
        index = -1
        result = -1
        for s in self.__contacts:
            index += 1
            if s.name == name:
                result = index
                break
        if result == -1:
            print(f'  Контакт {name} - не знайдений')
        return result

    def del_contact(self, name: str) -> None:
        index = self.__find_contact(name)
        if index >= 0:
            self.__contacts.pop(index)
            print(f'\n> Контакт <{name}> - успішно видалено!')

    def number_change(self, name: str, new_number: str) -> None:
        index = self.__find_contact(name)
        if index >= 0:
            self.__contacts[index].number = new_number
            print(f'> Номер контакта <{name}> - успішно змінено!')

    def display(self) -> None:
        k = 0
        for c in self.__contacts:
            k += 1
            print(f'{k}. {c}')
            

class BookManager(object):

    def __init__(self):
        self.__book = Book()

    @property
    def book(self) -> Book:
        return self.__book

    def init_data(self) -> None:
        self.__book.add_contact(Contact('Василь Пупкін', '(063) 111 2233', 'vasya@i.ua'))
        self.__book.add_contact(Contact('Катерина Шубкіна', '(066) 222 3344', 'katya@i.ua'))
        self.__book.add_contact(Contact('Наталія Супкіна', '(067) 333 4455', 'nata@i.ua'))
        self.__book.add_contact(Contact('Валентин Щукін', '(068) 444 5566', 'ivan@i.ua'))
        self.__book.add_contact(Contact('Петро Дуркін', '(070) 555 6677', 'pet@i.ua'))

    def load_data(self) -> None:
        with open('book.dat', 'rb') as file:
            self.__book = pickle.load(file)
        print('  Дані успішно завантажені!')

    def save_data(self):
        with open('book.dat', 'wb') as file:
            pickle.dump(self.__book, file)
        print('\n  Дані успішно збережені!')


if __name__ == '__main__':
    manager = BookManager()
    manager.init_data()

    print(manager.book)
    manager.book.display()

    manager.book.del_contact('Петро Дуркін')
    manager.book.add_contact(Contact('Петро Розумник', '(071) 666 7788', 'petro@i.ua'), True)
    manager.book.number_change('Василь Пупкін', '(063) 000 1122')
    manager.save_data()
    manager.load_data()

    print(manager.book)
    manager.book.display()
    print('\nПрограма завершена.')
