from math import sqrt


def usual_add(a: float, b: float, c: float) -> float:
	return a + b + c


unusual_add = lambda a, b, c: a + b + c
distance = lambda a1, b1, a2, b2: round(sqrt((b2 - b1)**2 + (a2 - a1)**2), 2)

if __name__ == '__main__':
	num1 = 10
	num2 = 20
	num3 = 30

	print(f'{num1} + {num2} + {num3} = {usual_add(num1, num2, num3)}')

	print(f'{num1} + {num2} + {num3} = {unusual_add(num1, num2, num3)}')

	x1 = 10
	y1 = 15
	x2 = 45
	y2 = 27
	print(f'Відстань: {distance(x1, y1, x2, y2)}')
