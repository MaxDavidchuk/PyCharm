"""
  Домашня робота після уроку 6
  -------------------------------
"""


def read_data(file: str) -> list:
  with open(file, 'r') as f:
    data = f.read().split()
  return [int(x) for x in data]


def main():
  data = read_data('input.txt')
  print('\nСписок елементів для аналізу:')
  n_list = []
  for k in range(len(data)):
    print(data[k], end=' ')
    if data.count(data[k]) == 1:
      n_list.append(data[k])
  n = len(n_list)
  if n >= 1:
    print('\nЕлементи, що трапляються у списку лише 1 раз:')
    for k in range(n):
      print(n_list[k], end=' ')
  else:
    print('\nЕлементи, що зустрічаються у списку лише один раз, відсутні')
  print('\nЗавдання виконане.')


if __name__ == '__main__':
  main()
