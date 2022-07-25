from decor_functions.decor_1 import time_monitor


@time_monitor
def bubble_sort(arr: list) -> None:
  """ Бульбашкове сортування одновимірних числових масивів """
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - 1 - i):
      if arr[j] > arr[j + 1]:   # Сортування за зростанням
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
