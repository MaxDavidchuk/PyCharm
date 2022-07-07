def read_data(file_name: str) -> str:
    """ Функція зчитування данних із файлу """
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()


def write_data(file_name: str, data: str) ->None:
    """ Функція збереження данних у файл """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f'\nДані успішно збережені у файлі {file_name}!')
