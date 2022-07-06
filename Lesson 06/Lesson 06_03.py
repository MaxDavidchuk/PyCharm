"""
  Демонстрація роботи з кортежами
  -------------------------------
  1. Кортеж - захичщений список, тобто впорядкований і незмінюваний набір об'єктів

"""
from lib import display_list


def main():
  # Creating tuple
  tom = ('Tom', 23, 7.5, 'tom@ukr.net')
  print(tom)
  print(tom[0])
  print(len(tom))
  temp = list(tom)
  temp[2] = 10.5
  tom = tuple(temp)
  print(tom)

if __name__ == '__main__':
  main()
