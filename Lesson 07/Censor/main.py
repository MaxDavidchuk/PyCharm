def read_content(file_name: str) -> str:
  with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
  return content


def replace_dialog(text: str) -> str:
  correct = text
  while True:
    old = input('> Яке слово замінити? - ')
    new = input('> Яким словом замінити? - ')
    correct = correct.replace(old, new)
    choice = input('> Продовжити (y/n)? - ')
    if choice == 'n':
      break
  return correct


def write_correct (file_name: str, text: str) -> None:
  with open(file_name, 'w', encoding='utf-8') as file:
    file.write(text)
  print('\nРезультат корегування успішно збережено.')


if __name__ == '__main__':
  data = read_content('content.txt')
  print(f'{data}\n')
  result = replace_dialog(data)
  print(f'\n{result}')
  write_correct('corrected.txt', result)
