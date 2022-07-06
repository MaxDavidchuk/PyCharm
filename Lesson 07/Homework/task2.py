"""
Name:        Homework07_02
Purpose:
  2. У прикладі на створення шифрувальника текстових повідомлень
  за дпомогою алгоритму Цезаря створіть функцію для дешифрування
  із демонстрацією результату на екрані консолі.
Created:     05.07.2022
"""

import lib


def decoding_symbol(text: str, key: int) -> str:
    s = ''
    for x in text:
        s += chr(ord(x) - key)
    return s


if __name__ == '__main__':
    # step 1
    cont_in = lib.read_data('task2_input.txt')
    # Очистка від non-pritable символів
    cont_in = ''.join(list(s for s in cont_in if s.isprintable()))
    print(f'\nЗашифроване повідомлення:\n{cont_in}')

    # step 2
    cont_dec = decoding_symbol(cont_in, 5)
    print(f'\nДешифроване повідомлення:\n{cont_dec}')

    # step 3
    lib.write_data('task2_output.txt', cont_dec)
