import pickle


class Product(object):

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} = {self.__price}'

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        self.__price = new_price


class Catalog(object):

    def __init__(self):
        self.__goods = []

    def add_product(self, product: Product) -> None:
        self.__goods.append(product)
        print('Товар успішно доданий!')

    def display(self):
        count = 0
        for p in self.__goods:
            count += 1
            print(f'{count}. {p}')

    def del_product(self, number: int) -> None:
        self.__goods.pop(number - 1)
        print('Товар успішно видалений!')

    def __find_index(self, name: str) -> int:
        index = -1
        result = -1
        for s in self.__goods:
            index += 1
            if s.name == name:
                result = index
                break
        if result == -1:
            print(f'  Товар <{name}> - не знайдений')
        return result

    def find_product(self, name: str) -> None:
        index = self.__find_index(name)
        if index != -1:
            print(f'  Товар <{self.__goods[index].name}> '
                  f'має таку ціну: {self.__goods[index].price}')

    def change_price(self, product: list) -> None:
        if product[0] <= len(self.__goods):
            self.__goods[product[0]].price = product[1]
            print(f'  Ціна товару <{self.__goods[product[0]].name}> '
                  f'- успішно змінена!')
        else:
            print('  Такого товару не знайдено!')


class DataManager(object):

    def __init__(self):
        self.__catalog = Catalog()

    @property
    def catalog(self) -> Catalog:
        return self.__catalog

    def init_data(self) -> None:
        self.__catalog.add_product(Product('Prod-1', 7.5))
        self.__catalog.add_product(Product('Prod-2', 11.2))
        self.__catalog.add_product(Product('Prod-3', 10))
        self.__catalog.add_product(Product('Prod-4', 15.6))
        self.__catalog.add_product(Product('Prod-5', 11.3))

    def load_data(self) -> None:
        with open('catalog.dat', 'rb') as file:
            self.__catalog = pickle.load(file)
        print('\n  Дані успішно завантажені!')

    def save_data(self):
        with open('catalog.dat', 'wb') as file:
            pickle.dump(self.__catalog, file)
        print('\n Дані успішно збережені!\n')


class Menu(object):

    menu_list = ['Вивести список товарів', 'Додати новий товар', 'Видалити існуючий товар',
                 'Знайти існуючий товар', 'Змінити ціну товару', 'Вийти із програми']
    menu_title = '\n+==============================+\n| Управління каталогом товарів |\n' \
                 '+==============================+'

    def __init__(self):
        self.__choice = 0
        self.__continue = 'y'

    @staticmethod
    def display() -> None:
        print(Menu.menu_title)
        for k in range(len(Menu.menu_list)):
            print(f'\t{k + 1} - {Menu.menu_list[k]}')
        print('================================')

    def make_choice(self) -> int:
        self.__choice = int(input('> Введіть номер операції: '))
        return self.__choice

    def allow_continue(self) -> bool:
        self.__continue = input('> Продовжити (y/n)? - ')
        return self.__continue == 'y'

    @staticmethod
    def make_product() -> Product:
        name = input('> Назва товару: ')
        price = float(input('> Ціна товару: '))
        return Product(name, price)

    @staticmethod
    def get_number() -> int:
        return int(input('> Введіть номер товару: '))

    @staticmethod
    def new_price() -> list:
        index = int(input('> Введіть номер товару: '))
        new_price = float(input('> Введіть нову ціну: '))
        return [index - 1, new_price]

    @staticmethod
    def get_product() -> str:
        return input('> Введіть назву товару, що шукаєте: ')
