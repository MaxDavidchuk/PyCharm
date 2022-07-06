def main(n):
	if n == 1:
		# Find
		s = 'Нехай завжди світить сонце та співають пташки'
		print(s)
		target = input('Введіть слово для пошуку: ')
		result = s.find(target)
		if result == -1:
			print(f'Слова "{target}" в даному рядку не знайдено')
		else:
			print(f'Слово "{target}" знайдено у позиції із індексом: {result}')
	elif n == 2:
		# insert
		s = 'aaa bbb ccc ddd'
		ins = ['1111', '2222', '3333']
		res1 = s[:4] + ins[0] + ' ' + s[4:]
		pos1 = res1.find('b') + 4
		res2 = res1[:pos1] + ins[1] + ' ' + res1[pos1:]
		pos2 = res2.find('c') + 4
		res3 = res2[:pos2] + ins[2] + ' ' + res2[pos2:]
		print(res1)
		print(res2)
		print(res3)
	elif n == 3:
		# remove
		s = '111 222 333 444 555'
		print(s)
		target = input('> Введіть слово для видалення: ')
		pos1 = s.find(target)
		if pos1 == -1:
			print(f'<{target}> not find')
		else:
			pos2 = pos1 + len(target) + 1
			s_new = s[:pos1] + s[pos2:]
			print(s_new)


if __name__ == '__main__':
	main(3)
