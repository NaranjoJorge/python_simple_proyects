import random
import os

def run():
	number = random.randint(0,100)
	guess = int(input('Guess a number from 0 to 100: '))
	assert guess in range(101), 'Should input a number from 0 to 100'
	i = 0

	while number != guess and i < 1:
		print('You missed by ' + str(abs(number - guess)))
		guess = int(input('Guess a number from 0 to 100: '))
		assert guess in range(101), 'You should input a number from 1 to 100'
		i += 1
		os.system('clear')
	if number == guess:
		print('You won!')
	else:
		print('Game over! You lousy bastard.')

if __name__ == '__main__':
	run()