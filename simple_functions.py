#Program that uses a function to print multiple statements.

def conversation(option):
	print('Hello')
	print('Are you feeling good today?')
	print('you choose option: ' + option)
	print('See you later.')

option = input('Choose an option (1, 2 or 3): ')
if option == '1':
	conversation(option)
elif option == '2':
	conversation(option)
elif option == '3':
	conversation(option)
else:
	print('Option out of range.')

