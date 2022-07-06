# -------------------------------------------------------------------------------
# Name:         list add/remove methods
# Purpose:      Methods demonstration of adding/removing elements in list
# Author:       dp_maxim
# Created:      29.06.2022
# -------------------------------------------------------------------------------


from lib import display_list


def main():
  # Creating list
  people = ['Tom', 'Bob']
  display_list(people)
  # Adding methods
  people.append('Alice')
  people.insert(1, 'Bill')
  people.extend(['Mike', 'Sam', 'Ivan'])
  display_list(people)
  # Removing methods
  people.pop()            # delete LAST element in list
  people.pop(3)           # delete element by index
  person = 'Kolya'
  if person in people:
    people.remove(person)   # delete element by element
  else:
    print(f'{person} is not in people list.')
  del people[-1]             #
  display_list(people)


if __name__ == '__main__':
  main()

