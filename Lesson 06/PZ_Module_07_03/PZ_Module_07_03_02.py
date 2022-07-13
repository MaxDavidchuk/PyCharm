def bin_search(temp: list, low: int, high: int, n: int):
  temp.sort()
  if high >= low:
    mid = (high + low) // 2
    if temp[mid] == n:
      return mid
    elif temp[mid] > n:
      return bin_search(temp, low, mid - 1, n)
    else:
      return bin_search(temp, mid + 1, high, n)
  else:
    return -1
 

def main():
  print("""   Задание 2
Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, 
введенное пользователем. Используйте алгоритм бинарного поиска.
====================================================================================""")
  arr_list = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  high = max(arr_list)
  print('\nДан список из 10-ти элекментов: ', arr_list)
  while True:
    print(f'\nВведите целое число в пределах от 0 до {high}')
    n = int(input('> n = '))
    if n >= 0 and n <= high:
      break
    else:
      print('Число не в диапазоне. Попробуйте еще раз.')
  res = bin_search(arr_list, 0, len(arr_list)-1, n)
  if res != -1:
    print("Число найдено в списке под индексом ", arr_list.index(n))
  else:
    print("Число не найдено в спике.")
  print('\nЗадание выполнено.')  


if __name__ == '__main__':
  main()