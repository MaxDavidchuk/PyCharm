from list_functions.base import *
from sort_functions.bubble_sort import *
from sort_functions.selection_sort import *
from sort_functions.insertion_sort import *


if __name__ == '__main__':

  n = 12

  x = [0] * n
  a = [0] * n
  b = [0] * n
  c = [0] * n

  random_fill(x, 10, 99)
  copy_array(x, a)
  copy_array(x, b)
  copy_array(x, c)

  bubble_sort(a)
  selection_sort(b)
  insertion_sort(c)

  display_array(x)
  display_array(a)
  display_array(b)
  display_array(c)
