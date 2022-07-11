"""
	Вкладені (комплексні) словники - nested dicts
"""


def main() -> None:
	users = {
		'Tom': {
			'phone': '+1111',
			'email': 'tom@i.ua',
		},
		'Bob': {
			'phone': '+2222',
			'email': 'bob@i.ua',
			'skype': 'bob123'
		}
	}
	print(users)
	print(users['Tom']['phone'])
	print(users['Bob']['email'])
	name = 'Tom'
	if name in users:
		person = users[name]
		value = 'phone'
		if value in person:
			phone = person[value]
			print(phone)
		else:
			print(f'Відсутні відомоісті про {value} користувача {name}')
	else:
		print(f'Користувач {name} - відсутній у словнику')


if __name__ == '__main__':
	main()
