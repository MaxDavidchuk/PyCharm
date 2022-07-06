def verify():
  while True:
    n = int(input('> Введіть ціле натуральне число: '))
    if n > 0:
        break
    else:
        print(' Число має бути додатнім.\n')
  return n


def prim(num):
  if num == 1:
    print('\nЗадача 1. Побудова шаблону 1')
    for k in range(1, verify() + 1):
      print(str(k) * k)
  elif num == 2:
    print('\nЗадача 2. Побудова шаблону 2')
    for k in range(verify(), 0, -1):
      print('*' * k)
  elif num == 3:
    print('\nЗадача 3. Таблиця множення числа n')
    n = verify()
    dl = len(str(n))
    for k in range(1, 11):
      print(f'{n:{dl}d} * {k:2d} = {n * k:{dl + 1}d}')
  else:
    print('Невірний номер завдання. Спробуйте ще раз.\n')


def main():
  try:
    print('Домашнє завдання після уроку №4.')
    while True:
      print('\nВведіть номер завдання від "1" до "3".\nДля виходу введіть "0"')
      a = int(input('>> '))
      if a == 0:
        break
      else:
        prim(a)
  except ValueError as err1:
    print(f' Помилка значення:\n  {err1}')
  finally:
    print('\nВиконання завдань завершено!')


if __name__ == "__main__":
  main()
