def divisors(x):
	divisor = []
	for i in range(1, x+1):
		if x % i == 0:
			divisor.append(i)
	return(divisor)

def run():
	number = int(input('Select a number'))
	print(divisors(number))

if __name__ == '__main__':
	run()