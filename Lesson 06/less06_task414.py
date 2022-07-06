"""
  task 414
"""


from lib import read_data


def main():
  num = read_data('input.txt')
  s = 0
  for k in range(len(num)):
    if num[k] > 0:
      s += 1
  print(s)


if __name__ == '__main__':
  main()
