# -------------------------------------------------------------------------------
# Name:         for_example1
# Purpose:      Вивести парні числа в заданому діапазоні
# Author:       dp_maxim
# Created:      20.06.2022
# -------------------------------------------------------------------------------
def main():
  try:
    print('> Введіть границі діапазону: ')
    a = int(input('  a = '))
    b = int(input('  b = '))
    if a == b: raise RecursionError('Границі не можуть бути однакові!')
    for k in range(min(a, b), max(a, b) + 1):
      if k % 2 == 0: print(k, end=' ')
    print()
  except ValueError as err1:
    print(f'Помилка значення: \n {err1}')
  except RuntimeError as err2:
    print(f'Помилка умови: \n {err2}')
  finally:
    print('Програму завершено!')


if __name__ == '__main__':
  main()
