#Function that exchanges currency to dollars

option = int(input('''
	Please select which currency you wish to exchange (only select the number): 
	1- Canadian dollars
	2- Brazilian real
	3- Congolese franc 
	'''))
amount = float(input('Please select the amount you want to exchange: '))

def exchange(x):
	if x == 1:
		print('That would be: ' + str(amount * 0.79) + ' dollars.')
	elif x == 2:
		print('That would be: ' + str(amount * 0.19) + ' dollars.')
	elif x == 3:
		print('That would be: ' + str(amount * 0.00050) + ' dollars.')
	else:
		print('Your option is out of range')

exchange(option)