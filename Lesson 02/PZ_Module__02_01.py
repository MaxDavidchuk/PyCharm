def ex(n):
  if n == 1:
    print('> Odd/Even')
    number = int(input('  Enter number: '))
    if (number % 2) == 0: print(f'  {number} Even number.')
    else: print(f'  {number} Odd number.')
  elif n == 2:
    print('> Multiple 7')
    if (int(input('  Enter number: ')) % 7) == 0: print('  Number is multiple 7.')
    else: print('  Number is not multiple 7.')
  elif n == 3 or n == 4:
    print(f'> {"MAX" if n == 3 else "MIN"} number')
    n1 = int(input('  Enter 1st number: '))
    n2 = int(input('  Enter 2nd number: '))
    print(f'  {"MAX" if n==3 else "MIN"} number is: {max(n1, n2) if n==3 else min(n1, n2)}')
  elif n == 5:
    print('> MAKE choice')
    n1 = int(input('  Enter 1st number: '))
    n2 = int(input('  Enter 2nd number: '))
    ch = int(input('> Press "1" to SUM, "2" to DIFFERENCE, "3" to AVERAGE, "4" to PRODUCT: '))
    if ch==1: print('  SUM = n1 + n2 = ', n1 + n2)
    if ch==2: print('  DIF = n1 - n2 = ', n1 - n2)
    if ch==3: print('  AVR = (n1 + n2) / 2 = ', (n1 + n2) / 2)
    if ch==4: print('  PRO = n1 * n2 = ', n1 * n2)
  else: print("  No such Exercise :(")
  return('Done!')

  
def main(): 
  from datetime import datetime
  print("\t Сьогодні: ", datetime.now().strftime('%d-%b-%Y'))
  print('\t----------------------------------------')
  print('\t Модуль 2. Операторы ветвлений Часть 1')
  print('\t----------------------------------------')

  print(""" 
  1. Complete ALL exercises (press "0")
  2. Complete SEPERATE exercise (press from "1" to "5")
  3. Exit (press "9")""")
  k = 0
  while k != 9:
    k = int(input("# "))
    if k == 0: 
      for x in range(5): print(f'Exercise {x+1}: {ex(x+1)}\n')
    elif k == 9: break
    else: print(f'Exercise {k}: {ex(k)}\n')
  
  print('\nThank you!\nSee you :)')

if __name__ == '__main__': main()