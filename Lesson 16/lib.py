import pickle


class Product(object):

    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f'{self.__name} = {self.__price}'


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
        print('\n  Дані успішно завантажені!\n')

    def save_data(self):
        with open('catalog.dat', 'wb') as file:
            pickle.dump(self.__catalog, file)
        print('\n  Дані успішно збережені!\n')


class Menu(object):

    def __init__(self):
        self.__choice = 0
        self.__continue = 'y'

    @staticmethod
    def display() -> None:
        print('==============================')
        print(' Управлыння каталогом товарів ')
        print('==============================')
        print('\t1 - Вивести список товарів')
        print('\t2 - Додати новий товар')
        print('\t3 - Видалити існуючий товар')
        print('\t4 - Знайти існуючий товар')
        print('\t5 - Змінити ціну товару')
        print('\t6 - Вийти із програми')
        print('==============================')

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
    def get_del_number() -> int:
        return int(input('> Введіть номер товару для видалення: '))
