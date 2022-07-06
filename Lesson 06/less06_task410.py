"""
  task 410
"""


from lib import read_data, write_res


def main():
  num = read_data('input.txt')
  for k in range(len(num)-1, -1, -1):
    print(num[k], end=' ')
  print()
  write_res('output.txt', num)


if __name__ == '__main__':
  main()
