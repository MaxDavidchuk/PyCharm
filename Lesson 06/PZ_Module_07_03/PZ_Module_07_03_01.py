def line_search(temp: list, n: int) -> int:
  find_res = -1
  for k in range(len(temp)):
    if temp[k] == n:
      find_res = k
      break
  return find_res
 

def main():
  print("""   Задание 1
Есть список из 10 элементов, заполненный случайными числами. Необходимо найти число, 
введенное пользователем. Используйте алгоритм линейного поиска.
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
      print('Введенное число не в диапазоне. Попробуйте еще раз.')
  res = line_search(arr_list, n)
  if res != -1:
    print("\nЧисло найдено в списке под индексом ", res)
  else:
    print("\nЧисло не найдено в спике.")
  print('\nЗадание выполнено.')  


if __name__ == '__main__':
  main()