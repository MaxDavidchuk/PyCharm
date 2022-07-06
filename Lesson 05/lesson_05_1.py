# -------------------------------------------------------------------------------
# Name:         task 405
# Purpose:      https://pythonexercises.rozh2sch.org.ua/#_списки_і_кортежі
# Author:       dp_maxim
# Created:      27.06.2022
# -------------------------------------------------------------------------------


def input_numbers() -> list:
  n = int(input('Enter numbers of list elements: '))
  print('Введіть ваші числа по-одному:')
  temp_list = [0] * n
  for i in range(n):
    temp_list[i] = int(input(f'{i + 1} -> '))
  return temp_list


def display_part(any_list: list) -> None:
  print(f'Вхідний список: {any_list}')
  print(f'Вихідний список: {any_list[len(any_list) // 2:]}')


def main():
  try:
    display_part(input_numbers())
  except ValueError as err1:
    print(f'Помилка значення: \n {err1}')
  except RuntimeError as err2:
    print(f'Помилка даних: \n {err2}')
  finally:
    print('Програму завершено!')


if __name__ == '__main__':
  main()
