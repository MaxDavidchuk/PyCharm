from decor_functions.decor_1 import time_monitor


def quick_sort_recursion(arr: list, left: int, right: int) -> None:
  """ Швидке сортування (Хоара) для одновимірних числових масивів """
  if left < right:
    p = arr[(left + right) // 2]
    i = left
    j = right
    while i <= j:
      while arr[i] < p:
        i += 1
      while arr[j] > p:
        j -= 1
      if i < j:
        arr[i], arr[j] = arr[j], arr[i]
      if i <= j:
        i += 1
        j -= 1
    quick_sort_recursion(arr, left, j)
    quick_sort_recursion(arr, i, right)


@time_monitor
def quick_sort(arr: list) -> None:
  quick_sort_recursion(arr, 0, len(arr) - 1)
