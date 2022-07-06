"""
    Доступ до окремих символів у рядках
    ===================================
    № Рядок - це незмінюваний список (кортеж) символів
"""


def main():
  s = 'Вася Пупкін - вічно молодий!'
# prim 1
  print(s[:7])
  print(s[len(s)//2:])
  print(s.count('о'))
  print(s[-2:])
  print(s[::2])   # Кожен 2-ий символ
  print(s[::-1])  # Інверсія - у зворотньому порядку
# prim 2
  print('\n', s.split())
  print(s.split('-'))
  fio = 'Пупкін Василь Петрович'
  print(fio.split())
# Деструктуризація (розпаковка) рядків
  l_name, f_name, m_name = fio.split()
  print(f_name, m_name, l_name)
  print(f'{l_name} {f_name[0]}. {m_name[0]}.\n')
# Replace - заміна фрагментів у рядках
  print(s.replace('вічно', '*****'))


if __name__ == '__main__':
  main()
