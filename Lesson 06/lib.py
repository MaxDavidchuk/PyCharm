def display_list(x: list) -> None:
  """  Function do display in consol list elements """
  k = 0
  for elem in x:
    k += 1
    print(f'{k}. {elem}')
  print()


def read_data(file: str) -> list:
  with open(file, 'r') as f:
    data = f.read().split()
  return [int(x) for x in data]


def write_res(file: str, res: list) -> None:
  with open(file, 'w') as f:
    for k in range(len(res)-1, -1, -1):
      f.write(str(res[k]))
      f.write(' ')
  print('Result list was saved!')
