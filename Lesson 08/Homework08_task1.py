"""
    1. В двох текстових файлах містяться списки пенсіонерів,
        при чому окремі прізвища повторюються в обох списках. За
        допомогою множин потрібно знайти створити список тих з них,
        які повторюються, список тих, хто присутній лише в першому
        із файлів та список тих, хто присутній лише в другому з них.
        Отримані списки треба відобразити на екрані консолі.
"""

def read_data(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def print_set(s: set) -> None:
    k = 0
    for fio in s:
        k += 1
        print(f'{k}. {fio}', end=' ')
    print()

if __name__ == '__main__':
    pens1 = set(read_data('task1_1.txt').split())
    pens2 = set(read_data('task1_2.txt').split())
    print("""
    =====================
    =   Вхідні дані:    =
    ===================== """)
    print('\nПрізвища пенсіонерів у 1-му спику:')
    print_set(pens1)
    print('\nПрізвища пенсіонерів у 2-му спику:')
    print_set(pens2)
    print("""
    =====================
    =   Вихідні дані:   =
    ===================== """)
    print('\nПрізвища пенсіонерів, які присутні у двох списках:')
    print_set(pens1.intersection(pens2))
    print('\nПрізвища пенсіонерів, які присутні лише у 1-му списку:')
    print_set(pens1.difference(pens2))
    print('\nПрізвища пенсіонерів, які присутні лише у 2-му списку:')
    print_set(pens2.difference(pens1))
    print("""
    =====================
    =       Кінець      =
    =====================""")