"""
  task 411
"""


from lib import read_data


def main():
  num = read_data('input.txt')
  for k in range(len(num)):
    if k % 2 == 0:
      print(num[k], end=' ')


if __name__ == '__main__':
  main()
