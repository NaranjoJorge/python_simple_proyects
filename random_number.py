#Game that makes you guess the right number.

import random

y = random.randrange(1, 101)

# def numbers ():
# 	x = int(input('Chose a number: '))
# 	if x == y:
# 		print ('You win')
# 	elif x > y:
# 		print ('Chose a smaller number')
# 		numbers()
# 	else:
# 		print ('Chose a bigger number')
# 		numbers()
# numbers()
	
x = int(input('Chose a number: '))
while x != y:
	if x > y:
		print('Chose a smaller number')
	else:
		print('Chose a bigger number')
	x = int(input('Chose a number: '))
if x == y:
	print('You win')