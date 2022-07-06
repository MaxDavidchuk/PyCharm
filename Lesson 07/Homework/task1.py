"""
Name:        Homework07_01
Purpose:
  2. Створіть нову версію програми для цензурування тексту, який
     міститься у певному файлі із заміною небажаних слів на відповідну
     кількість символів *.
Created:     05.07.2022
"""

import lib


def replace_symbol(text: str) -> list:
    print('\nЗаміна небажаних слів:')
    c = 0
    while True:
        old = input('> Яке слово бажаєте замінити? - ')
        if text.count(old) == 0:
            print(f'  Слово "{old}" не знайдено!')
        else:
            text = text.replace(old, '*'*len(old))
            print(f'  Слово "{old}" замінено вдало!\n')
            c += 1
        if int(input('> Бажаєте продовжити (0-"Ні" / 1-"Так")? ')) == 0:
            break
    return [text, c]


if __name__ == '__main__':
    # step 1
    cont_in = lib.read_data('task1_input.txt')
    print('Стара редакція відгуків:')
    print(cont_in)
    # step 2
    cont_rep = replace_symbol(cont_in)
    print(f'\nЗамінено {cont_rep[1]} слово (-а, -ів).')
    print('Відкорегована редакція відгуків:')
    print(cont_rep[0])
    # step 3
    lib.write_data('task1_output.txt', cont_rep[0])
