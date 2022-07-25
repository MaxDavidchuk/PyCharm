from decor_functions.decor_1 import time_monitor


@time_monitor
def selection_sort(arr: list) -> None:
  """ Сортування вибором одновимірних числових масивів """
  n = len(arr)
  for i in range(n - 1):        # Кількість проходів із пошуком МІН значення
    minim = arr[i]              # Перше число
    index = i                   # Індекс числа
    for j in range(i + 1, n):   # Пошук выд наступного числа до кінця
      if arr[j] < minim:
        minim = arr[j]
        index = j
    arr[i], arr[index] = arr[index], arr[i]   # Обмін знайденого числа із першим не відсортованим
