# -------------------------------------------------------------------------------
# Name:         task 407
# Purpose:      https://pythonexercises.rozh2sch.org.ua/#_списки_і_кортежі
# Author:       dp_maxim
# Created:      27.06.2022
# -------------------------------------------------------------------------------


def input_lang() -> list:
  lang_str = input('\nВведіть назви мов в один рядок через пробіл:')
  temp_list = lang_str.split()
  return temp_list


def display_list(target_list: list) -> None:
  print(f'Вихідний список: {target_list}')


def main():
  try:
    lang_list = input_lang()
    lang_list.sort()
    display_list(lang_list)

  except ValueError as err1:
    print(f'Помилка значення: \n {err1}')
  except RuntimeError as err2:
    print(f'Помилка даних: \n {err2}')
  finally:
    print('\nПрограму завершено!')


if __name__ == '__main__':
  main()