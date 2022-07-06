def prim(n):
  if n == 1:
    print('\nЗадача 1. Стан погоди')
    for k in range(1,4):
      a = float(input(f'> ({k} з 3) Введіть значення температури: '))
      if a <= 0: print('  A cold, isn\'nt it?')
      elif 0 < a < 10: print('  Cool.')
      else: print('  Nice weathe we\'re having.')
  elif n == 2:
    print('\nЗадача 2. Визначення оцінки')
    for k in range(1,4):
      b = int(input(f'> ({k} з 3) Введіть Ваш тестовий бал: '))
      if b < 60: b = "F"
      elif 60 <= b < 70: b = 'D'
      elif 70 <= b < 80: b = 'C'
      elif 80 <= b < 90: b = 'B'
      else: b = 'A'
      print(f'Your grade is {b}')
  elif n == 3:
    print('\nЗадача 3. Калькулятор')
    for k in range(1, 4):
      print(f'\nВаріант {k} з 3')
      a = float(input('> Введіть перше число: a = '))
      b = float(input('> Введіть друге число: b = '))
      s = input('> Введіть арифметичну дію [+, -, /, *, mod, pow, div]: ')
      if s == 'mod': s = '%'
      elif s == 'pow': s = '**'
      elif s == 'div': s = '//'
      print('Результат: ', end=' ')
      if b == 0.0 and s == '/': print('Division by 0!')
      else: print(round(eval(f'{a}{s}{b}'),2))
  elif n == 4:
    print('\nЗадача 4. Друк m разів числа n')
    n = int(input('> Введіть ціле число: n = '))
    m = int(input('> Введіть ціле число: m = '))
    print((str(n)+' ')*m)
  elif n == 5:
    print('\nЗадача 5. Друк квардартів цілих чисел від 1 до n')
    n = int(input('> Введіть ціле число: n = '))
    for k in range(1, n+1):
      print(k**2, end=' ')
    print()
  else: print('Невірний номер завдання. Спробуйте ще раз.\n')

   
def main():
  try:
    print('Домашнє завдання після уроку №3.')
    while True:
      print('\nВведіть номер завдання від "1" до "5".\nДля виходу введіть "0"')
      a = int(input('>> '))
      if a != 0: prim(a)
      else: break
        
  except ValueError as err1: print(f' Помилка значення:\n  {err1}')
  finally: print('\nВиконання завдань завершено!')
  
if __name__ == "__main__":
  main()