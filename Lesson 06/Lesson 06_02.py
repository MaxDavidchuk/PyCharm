# -------------------------------------------------------------------------------
# Name:         Manipulation methods with Liat
# Author:       dp_maxim
# Created:      29.06.2022
# -------------------------------------------------------------------------------


from lib import display_list


def main():
  # Creating list
  people = ['Tom', 'Bob', 'Alice', 'Tom', 'Bill', 'Tom', 'Bob']
  display_list(people)

  k = people.count('Tom')
  k1 = people.count('Vasya')
  print(k, k1)

  i1 = people.index('Tom')
  if people.count('Vasya') > 0:
    print(people.index('Vasya'))
  print(i1)

# agrigate function
  n = [1, 12, 5, 18, 0, 45]
  print(n)
  print(f'min = {min(n)}\nmax = {max(n)}\nsum = {sum(n)}\nagr = {sum(n)/len(n)}\n')

# copy function
  list_main = ['Petrov', 'Sidorov', 'Fedorov', 'Ivanov']
  display_list(list_main)
  list_new = list_main.copy()
  list_new.sort()
  display_list(list_new)
  del list_new[1:3]
  display_list(list_new)


if __name__ == '__main__':
  main()
