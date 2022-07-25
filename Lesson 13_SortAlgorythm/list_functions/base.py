def display_array(arr: list) -> None:
  """ Відображення на екрані одновимірних списків (масивів) """
  for elem in arr:
    print(elem, end=' ')
  print('---')


def random_fill(arr: list, a: int, b: int) -> None:
  """ Заповнення одновимірних масивів рандомними числами в заданому діапазоні """
  import random
  for i in range(len(arr)):
    arr[i] = random.randint(a, b)


def copy_array(arr_x: list, arr_y: list) -> None:
  """ Копіювання одного числового масиву в інший """
  for i in range(len(arr_x)):
    arr_y[i] = arr_x[i]
