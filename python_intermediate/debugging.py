def divisors(x):
	divisor = []
	for i in range(1, x+1):
		if x % i == 0:
			divisor.append(i)
	return(divisor)

def run():
	try:
		number = int(input('Select a number: '))
		if number < 0 or number == -0:
			raise Exception('Sorry, only positive numbers')
		print(divisors(number))
	except ValueError:
		print('Debes ingresar un número')


if __name__ == '__main__':
	run()