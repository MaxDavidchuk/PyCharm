from random import randint


def ex1():
  print('\nTask 1. What to do?')
  print("""  Calculate the following in a list filled with random numbers:
  - (s1) Sum of negative numbers;
  - (s2) Sum of even numbers;
  - (s3) Sum of odd numbers;
  - (p1) Product of elements with indices divisible by 3;
  - (p2) Product of elements between the smallest and the largest element;
  - (s4) The sum of the elements between the first and the last positive elements. """)
  print('\nEnter the number list elements:')
  n = int(input('> '))
  rand_list = []
  s1 = s2 = s3 = s4 = 0
  p1 = p2 = 1
  for k in range(n):
    rand_list.append(randint(-n, n + 1))
    t = rand_list[k]
    if t < 0:
      s1 += t
    if t % 2 == 0:
      s2 += t
    else:
      s3 += t
    if k % 3 == 0:
      p1 *= k
# find p2
  m1 = rand_list.index(min(rand_list))
  m2 = rand_list.index(max(rand_list))
  if m1 > m2:
    p2 = 'MIN index is more then MAX index'
  elif m2 - m1 == 1:
    p2 = 'Between MIN and MAX no elements'
  else:
    for k in range(m1 + 1, m2):
      p2 *= rand_list[k]
# find s4
  for k in range(n):
    if rand_list[k] > 0:
      n1 = rand_list.index(rand_list[k])
      break
  for k in range(n - 1, 0, -1):
    if rand_list[k] > 0:
      n2 = rand_list.index(rand_list[k])
      break
  if n1 == n2:
    s4 = 'First and Last positive elements is the same element!'
  elif m2 - m1 == 1:
    s4 = 'Between MIN and MAX no elements'
  else:
    for k in range(n1 + 1, n2):
      s4 += rand_list[k]

  if p1 == 1:
    p1 = 'Not calculated'
  elif p2 == 1:
    p2 = 'Not calculated'
  print(f'\nList with random numbers:\n{rand_list}')
  print(
    f'\nResult of calculation is:\n s1 = {s1}\n s2 = {s2}\n s3 = {s3}\n p1 = '
    f'{p1}\n p2 = {p2} (min = {rand_list[m1]} max = {rand_list[m2]})\n s4 = {s4} '
    f'(first = {rand_list[n1]} last = {rand_list[n2]})')


def ex2():
  print('\nЗадача 2.')
  rand_list = []
  for k in range(1, 10):
    rand_list.append(randint(-100, 101))
  print(rand_list)
  print(f' min = {rand_list.index(min(rand_list))}\n max = {rand_list.index(max(rand_list))}')


def main():
  print('Module 3. String. Lists. Part 3')
  while True:
    print('\n  Select "1", "2" or "0" to Exit')
    s = int(input('> '))
    if s == 1:
      ex1()
    elif s == 2:
      ex2()
    elif s == 0:
      break
    else:
      print('  No such task.\n  Tre again.')
  print('\n Done!')


if __name__ == "__main__":
  main()
