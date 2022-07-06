def read_content(file_name: str) -> str:
	with open(file_name, 'r', encoding='utf-8') as file:
		content = file.read()
	return content


def write_content(file_name: str, text: str) -> None:
	with open(file_name, 'w', encoding='utf-8') as file:
		file.write(text)
	print('\nРезультат шифрування успішно збережено.')


def encode(text: str, key: int) -> str:
	s = ''
	for x in text:
		code = ord(x) + key
		s += chr(code)
	return s


if __name__ == '__main__':
	mes = read_content('message.txt')
	print(mes)
	secret = encode(mes, 5)
	print(secret)
