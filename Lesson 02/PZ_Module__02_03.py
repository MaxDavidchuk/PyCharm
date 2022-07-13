def verify(*arg):
  if arg[0] != 3: return(False if len(arg[1]) != arg[2] else True)
  else: return(False if int(arg[1]) > arg[2] or int(arg[1]) <= 0 else True)

def ex1():
  print('\nЗадача 1.')
  while True:
    n = input('>> Введите целое шестизначное число: n = ')
    if not verify(1, n, 6): print('   Вы ввели не шестизначное число! Попробуйте еще раз.\n')
    else:
      n1 = list(n[0:3])
      n2 = list(n[3:6])
      n11 = 0
      n22 = 0
      for i in range(3):
        n11 += int(n1[i])
        n22 += int(n2[i])
      print(f'   Введенное число {n} - ' + ('Счастливое' if n11 == n22 else 'Несчастливое'))
      break

def ex2():
  print('\nЗадача 2.')
  while True:
    n = input('>> Введите целое шестизначное число: n = ')
    if not verify(2, n, 6): print('   Вы ввели не шестизначное число! Попробуйте еще раз.\n')
    else:
      n = list(n)
      for i in range(2):
        temp = n[i]
        n[i] = n[5-i]
        n[5-i] = temp
      print('   Введенное число превратилось в ' + ''.join(n))
      break

def ex3():
  print('\nЗадача 3.')
  m_name = ['Зима', 'Весна', 'Лето', 'Осень']
  m_numb = {1:[12,1,2], 2:[3,4,5], 3:[6,7,8], 4:[9,10,11]}
  while True:
    n = input('>> Введите номер месяца: ')
    if not verify(3, n, 12): print('   Номер месяца не может быть больше 12, равняться "0" или быть меньше "0"! Попробуйте еще раз.\n')
    else:
      for i in range(len(m_name)):
        for j in range(3):
          if m_numb[i+1][j] == int(n):
            print(f'   {n}-й месяц - это {m_name[i]}')
            break
      break
   
def main():
  print('Модуль 2. Операторы ветвлений Часть 3')
  while True:
    print('\n  Ввыберите задание "1", "2", "3" или введите "0" для выхода')
    s = int(input('> '))
    if s == 1: ex1()
    elif s == 2: ex2()
    elif s == 3: ex3()
    elif s == 0: break
    else: print('  Такого задания нет.\n  Попбробуйте еще раз.')
  print('\n Выполнение заданий окончено!')
  
if __name__ == "__main__":
  main()