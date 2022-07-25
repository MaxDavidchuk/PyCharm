from decor_functions.decor_1 import time_monitor


@time_monitor
def insertion_sort(arr: list) -> None:
  """ Сортування вставками для одновимірних числових масивів """
  n = len(arr)
  for i in range(1, n):
    if arr[i] < arr[i - 1]:
      temp = arr[i]
      j = i - 1     # Індекс попереднього числа
      while arr[j] > temp and j >= 0:
        arr[j + 1] = arr[j]
        j -= 1
      arr[j + 1] = temp
